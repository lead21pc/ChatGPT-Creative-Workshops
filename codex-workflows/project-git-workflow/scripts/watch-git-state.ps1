#Requires -Version 7.0
<#
.SYNOPSIS
    Theo dõi xung đột và thao tác Git còn dở trên một checkout. Dừng bằng Ctrl+C.
.EXAMPLE
    pwsh -NoProfile -File ./watch-git-state.ps1 -Path .
#>
[CmdletBinding()]
param(
    [string]$Path = '.',
    [switch]$StructuredOutput,
    [int]$ParentProcessId,
    [long]$ParentStartTimeTicks
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$PSNativeCommandUseErrorActionPreference = $false
if ($StructuredOutput) { [Console]::OutputEncoding = [Text.UTF8Encoding]::new($false) }

function Write-WatcherError {
    param([string]$Message, [switch]$Fatal)

    if ($StructuredOutput) {
        @{ type = 'error'; message = $Message; fatal = $Fatal.IsPresent } | ConvertTo-Json -Compress
    } else {
        "[GIT WATCH] $Message"
    }
}

function Read-Git {
    param([string[]]$GitArguments, [switch]$AllowMissingRef)

    $result = @(& $gitExecutable --no-optional-locks --no-lazy-fetch -C $checkout @GitArguments 2>&1)
    $exitCode = $LASTEXITCODE
    if ($AllowMissingRef -and $exitCode -eq 1 -and $result.Count -eq 0) {
        return
    }
    if ($exitCode -ne 0) {
        throw "Git ($exitCode) $($result | Select-Object -First 1)"
    }
    $result | Where-Object { $_ -isnot [System.Management.Automation.ErrorRecord] }
}

function Read-GitState {
    if (Test-Path -LiteralPath $indexLockPath) {
        throw 'Git đang cập nhật index.'
    }

    $entries = (Read-Git -GitArguments @('ls-files', '--unmerged', '-z')) -join "`n"
    $paths = [System.Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
    foreach ($entry in ($entries -split "`0")) {
        if ($entry.Length -gt 0) {
            [void]$paths.Add($entry.Substring($entry.IndexOf("`t") + 1))
        }
    }
    $unmerged = [string[]]::new($paths.Count)
    $paths.CopyTo($unmerged)
    [Array]::Sort($unmerged, [StringComparer]::Ordinal)

    $merge = Test-Path -LiteralPath $mergeHeadPath -PathType Leaf
    $rebase = (Test-Path -LiteralPath $rebaseMergePath -PathType Container) -or
        (Test-Path -LiteralPath $rebasingPath -PathType Leaf)
    $cherryPick = $false
    if (-not $rebase) {
        $cherryPick = [bool](Read-Git -GitArguments @('rev-parse', '--verify', '--quiet', 'CHERRY_PICK_HEAD') -AllowMissingRef)
        if (-not $cherryPick -and (Test-Path -LiteralPath $todoPath -PathType Leaf)) {
            $cherryPick = (Get-Content -LiteralPath $todoPath -TotalCount 1) -cmatch '^(pick|p)[\t ]'
        }
    }

    if (Test-Path -LiteralPath $indexLockPath) {
        throw 'Git đang cập nhật index.'
    }
    [pscustomobject]@{ Unmerged = $unmerged; Merge = $merge; Rebase = $rebase; CherryPick = $cherryPick }
}

function Write-GitTransition {
    param($Previous, $Current)

    if (($Current.Unmerged -join "`0") -cne ($Previous.Unmerged -join "`0")) {
        if ($Current.Unmerged.Count -gt 0) {
            '[GIT WATCH] Tệp còn xung đột'
            $Current.Unmerged | ForEach-Object { "  $_" }
        } else {
            '[GIT WATCH] Index đã hết xung đột.'
        }
    }
    foreach ($operation in @{ Merge = 'merge'; Rebase = 'rebase'; CherryPick = 'cherry-pick' }.GetEnumerator() | Sort-Object Name) {
        if ($Current.($operation.Key) -ne $Previous.($operation.Key)) {
            if ($Current.($operation.Key)) {
                "[GIT WATCH] $($operation.Value) đang dở."
            } else {
                "[GIT WATCH] $($operation.Value) đã kết thúc."
            }
        }
    }
}

try {
    $gitExecutable = (Get-Command git -CommandType Application | Select-Object -First 1).Source
    $checkout = (Resolve-Path -LiteralPath $Path).ProviderPath
    $checkout = Read-Git -GitArguments @('rev-parse', '--show-toplevel')
    $gitDir, $indexPath, $mergeHeadPath, $rebaseMergePath, $rebasingPath, $todoPath,
        $cherryPickHeadPath, $reftablePath = Read-Git -GitArguments @(
        'rev-parse', '--path-format=absolute', '--git-dir', '--git-path', 'index',
        '--git-path', 'MERGE_HEAD', '--git-path', 'rebase-merge',
        '--git-path', 'rebase-apply/rebasing', '--git-path', 'sequencer/todo',
        '--git-path', 'CHERRY_PICK_HEAD', '--git-path', 'reftable'
    )
} catch {
    Write-WatcherError -Fatal -Message "Không thể mở worktree. $($_.Exception.Message)"
    exit 1
}

$indexLockPath = "$indexPath.lock"
$gitDir = [IO.Path]::GetFullPath($gitDir)
$indexDir = [IO.Path]::GetDirectoryName($indexPath)
$metadataPaths = @($mergeHeadPath, $rebaseMergePath, $rebasingPath, $todoPath, $cherryPickHeadPath,
    (Split-Path -Parent $rebasingPath), (Split-Path -Parent $todoPath), $reftablePath,
    (Join-Path $reftablePath 'tables.list'))
$pathComparer = if ($IsWindows) { [StringComparer]::OrdinalIgnoreCase } else { [StringComparer]::Ordinal }
$watchedPaths = [System.Collections.Generic.HashSet[string]]::new($pathComparer)
foreach ($watchedPath in ($metadataPaths + $indexPath + $indexLockPath)) {
    [void]$watchedPaths.Add([IO.Path]::GetFullPath($watchedPath))
}
$watchers = @()
$sourcePrefix = "git-watch-$([guid]::NewGuid())-"
$previous = [pscustomobject]@{ Unmerged = @(); Merge = $false; Rebase = $false; CherryPick = $false }
$readFailed = $false
$fatalWatchError = $null
$hasSnapshot = $false
$conflictRevision = 0
$parent = $null
$parentExitSource = "${sourcePrefix}parent-exit"

try {
    if ($ParentProcessId) {
        try {
            $parent = [Diagnostics.Process]::GetProcessById($ParentProcessId)
            if ($parent.StartTime.ToUniversalTime().Ticks -ne $ParentStartTimeTicks) { return }
            Register-ObjectEvent -InputObject $parent -EventName Exited -SourceIdentifier $parentExitSource
            $parent.EnableRaisingEvents = $true
            if ($parent.HasExited) { return }
        } catch [ArgumentException], [InvalidOperationException] {
            return
        }
    }

    $metadataWatcher = [IO.FileSystemWatcher]::new($gitDir)
    $watchers += $metadataWatcher
    $metadataWatcher.IncludeSubdirectories = $true
    foreach ($metadataPath in $metadataPaths) {
        $metadataWatcher.Filters.Add([IO.Path]::GetFileName($metadataPath))
    }

    $indexWatcher = $metadataWatcher
    if (-not $pathComparer.Equals($indexDir, $gitDir)) {
        $indexWatcher = [IO.FileSystemWatcher]::new($indexDir)
        $watchers += $indexWatcher
    }
    $indexWatcher.Filters.Add([IO.Path]::GetFileName($indexPath))
    $indexWatcher.Filters.Add([IO.Path]::GetFileName($indexLockPath))

    foreach ($watcher in $watchers) {
        foreach ($eventName in @('Changed', 'Created', 'Deleted', 'Renamed', 'Error')) {
            Register-ObjectEvent -InputObject $watcher -EventName $eventName -SourceIdentifier "$sourcePrefix$([guid]::NewGuid())"
        }
        $watcher.EnableRaisingEvents = $true
    }

    $firstRead = $true
    while ($true) {
        if ($parent -and $parent.HasExited) { return }
        try {
            $current = Read-GitState
            if ($StructuredOutput) {
                $conflictsChanged = ($current.Unmerged -join "`0") -cne ($previous.Unmerged -join "`0")
                if ($conflictsChanged) { $conflictRevision++ }
                if (-not $hasSnapshot -or $readFailed -or $conflictsChanged -or
                    $current.Merge -ne $previous.Merge -or $current.Rebase -ne $previous.Rebase -or
                    $current.CherryPick -ne $previous.CherryPick) {
                    $operations = @(
                        if ($current.Merge) { 'merge' }
                        if ($current.Rebase) { 'rebase' }
                        if ($current.CherryPick) { 'cherry-pick' }
                    )
                    @{
                        type = 'state'; unmergedCount = $current.Unmerged.Count
                        conflictRevision = $conflictRevision; operations = $operations
                    } | ConvertTo-Json -Compress
                }
            } else {
                Write-GitTransition -Previous $previous -Current $current
                if ($readFailed) { '[GIT WATCH] Đã đọc lại được trạng thái Git.' }
            }
            $previous = $current
            $hasSnapshot = $true
            $readFailed = $false
        } catch {
            if (-not $readFailed) {
                Write-WatcherError -Message "Không đọc được trạng thái Git. $($_.Exception.Message)"
            }
            $readFailed = $true
        }

        if ($fatalWatchError) { throw $fatalWatchError }
        if ($firstRead -and -not $StructuredOutput) {
            "[GIT WATCH] Đang theo dõi $checkout"
            $firstRead = $false
        }

        # Wait in the dedicated terminal process. Events arriving during a Git read stay queued.
        do {
            [void](Wait-Event)
            if ($parent -and $parent.HasExited) { return }
            Start-Sleep -Milliseconds 150
            $readAgain = $false
            foreach ($watchEvent in (Get-Event | Where-Object SourceIdentifier -Like "$sourcePrefix*")) {
                $eventArgs = $watchEvent.SourceEventArgs
                if ($eventArgs -is [IO.ErrorEventArgs]) {
                    $readAgain = $true
                    $watchError = $eventArgs.GetException()
                    if ($watchError -isnot [IO.InternalBufferOverflowException]) {
                        $fatalWatchError = $watchError.Message
                    }
                } elseif ($watchedPaths.Contains($eventArgs.FullPath) -or
                    ($eventArgs -is [IO.RenamedEventArgs] -and $watchedPaths.Contains($eventArgs.OldFullPath))) {
                    $readAgain = $true
                }
                Remove-Event -EventIdentifier $watchEvent.EventIdentifier
            }
        } until ($readAgain)
    }
} catch {
    Write-WatcherError -Fatal -Message "Đã dừng theo dõi. $($_.Exception.Message)"
    exit 1
} finally {
    Get-EventSubscriber | Where-Object SourceIdentifier -Like "$sourcePrefix*" | Unregister-Event
    Get-Event | Where-Object SourceIdentifier -Like "$sourcePrefix*" | Remove-Event
    foreach ($watcher in $watchers) { $watcher.Dispose() }
    if ($parent) { $parent.Dispose() }
}
