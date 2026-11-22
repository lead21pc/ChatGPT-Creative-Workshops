#Requires -Version 7.0
[CmdletBinding()]
param([Parameter(Mandatory)][string]$Path)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

if (-not $IsWindows -or [Threading.Thread]::CurrentThread.GetApartmentState() -ne 'STA') {
    throw 'Chạy tray bằng PowerShell 7 trên Windows với -STA.'
}

$created = $false
$mutex = [Threading.Mutex]::new($true, 'Local\GitSideWatcherTray', [ref]$created)
if (-not $created) { $mutex.Dispose(); return }

$child = $null
$snapshot = $null
$icon = $null
$menu = $null
$context = $null
$timer = $null
$failure = $null
$parentStartTicks = (Get-Process -Id $PID).StartTime.ToUniversalTime().Ticks

function Set-TrayDisplay {
    param([string]$State, [string]$Detail)

    $image = switch ($State) {
        'CONFLICT' { [Drawing.SystemIcons]::Warning }
        'ERROR' { [Drawing.SystemIcons]::Error }
        'OPERATION' { [Drawing.SystemIcons]::Information }
        'PAUSED' { [Drawing.SystemIcons]::Question }
        default { [Drawing.SystemIcons]::Application }
    }
    $text = if ($Detail) { "$State · $Detail" } else { $State }
    $tooltip = "Git Side Watcher · $text"
    if ($tooltip.Length -gt 63) { $tooltip = $text }
    $icon.Icon = $image
    $icon.Text = $tooltip.Substring(0, [Math]::Min(63, $tooltip.Length))
    $statusItem.Text = $text.Replace('&', '&&').Replace("`r", ' ').Replace("`n", ' ')
    $toggleItem.Text = if ($script:child) { 'Pause' } else { 'Enable' }
}

function Show-TrayBalloon {
    param([string]$Message, [Windows.Forms.ToolTipIcon]$Kind)

    try { $icon.ShowBalloonTip(5000, 'Git Side Watcher', $Message, $Kind) }
    catch { Write-Verbose $_.Exception.Message }
}

function Format-GitSnapshot {
    param($State)

    if ($null -ne $State) {
        @(if ($State.unmergedCount) { "$($State.unmergedCount) tệp xung đột" }
          if ($State.operations.Count) { $State.operations -join ', ' }) -join ' · '
    }
}

function Show-TrayError {
    param([string]$Message)

    $previousDetail = Format-GitSnapshot $script:snapshot
    $detail = if ($previousDetail) { "$previousDetail (lần đọc cuối) · $Message" } else { $Message }
    Set-TrayDisplay 'ERROR' $detail
    if ($script:failure -cne $Message) { Show-TrayBalloon $Message Error }
    $script:failure = $Message
}

function Receive-WatcherLine {
    param([string]$Line)

    $event = ConvertFrom-Json -InputObject $Line -AsHashtable -ErrorAction Stop
    if ($event.type -eq 'error') {
        $script:child.FatalReported = [bool]$event.fatal
        Show-TrayError $event.message
        return
    }
    if ($event.type -ne 'state') { throw 'Watcher trả kết quả không hợp lệ.' }

    $old = $script:snapshot
    $script:snapshot = $event
    $script:failure = $null
    $state = if ($event.unmergedCount) { 'CONFLICT' }
             elseif ($event.operations.Count) { 'OPERATION' }
             else { 'ACTIVE' }
    $detail = Format-GitSnapshot $event
    Set-TrayDisplay $state $detail

    $newConflict = $event.unmergedCount -gt 0 -and
        ($null -eq $old -or $event.conflictRevision -ne $old.conflictRevision)
    $newOperation = $event.operations | Where-Object { $null -eq $old -or $_ -notin $old.operations }
    if ($newConflict -or $newOperation) { Show-TrayBalloon $detail Warning }
}

function Close-Watcher {
    if (-not $script:child) { return }

    $process = $script:child.Process
    if (-not $process.HasExited) {
        try { $process.Kill($true) }
        catch { if (-not $process.HasExited) { throw } }
        if (-not $process.WaitForExit(1000)) { throw 'Watcher chưa dừng.' }
    }
    $script:child = $null
    $timer.Stop()
    $process.Dispose()
}

function Start-Watcher {
    if ($script:child) { return }

    $script:snapshot = $null
    $script:failure = $null
    $process = [Diagnostics.Process]::new()
    try {
        $info = $process.StartInfo
        $info.FileName = [Environment]::ProcessPath
        $info.UseShellExecute = $false
        $info.CreateNoWindow = $true
        $info.RedirectStandardOutput = $true
        $info.RedirectStandardError = $true
        $info.StandardOutputEncoding = [Text.Encoding]::UTF8
        $info.StandardErrorEncoding = [Text.Encoding]::UTF8
        foreach ($argument in @('-NoLogo', '-NoProfile', '-NonInteractive', '-File',
                (Join-Path $PSScriptRoot 'watch-git-state.ps1'), '-Path', $Path, '-StructuredOutput',
                '-ParentProcessId', "$PID", '-ParentStartTimeTicks', "$parentStartTicks")) {
            $info.ArgumentList.Add($argument)
        }
        if (-not $process.Start()) { throw 'Không khởi chạy được watcher.' }
        $script:child = [pscustomobject]@{
            Process = $process; Output = $null; ErrorOutput = $null
            LastError = ''; FatalReported = $false
        }
        Set-TrayDisplay 'STARTING' ''
        $script:child.Output = $process.StandardOutput.ReadLineAsync()
        $script:child.ErrorOutput = $process.StandardError.ReadLineAsync()
        $timer.Start()
    } catch {
        $message = $_.Exception.Message
        if ($script:child) { Close-Watcher } else { $process.Dispose() }
        Show-TrayError $message
    }
}

function Read-WatcherStreams {
    if (-not $script:child) { return }

    $running = $script:child
    try {
        # The WinForms timer runs on the UI thread. Only consume completed async reads.
        foreach ($stream in @('Output', 'ErrorOutput')) {
            for ($i = 0; $i -lt 32 -and $running.$stream -and $running.$stream.IsCompleted; $i++) {
                $line = $running.$stream.GetAwaiter().GetResult()
                $running.$stream = $null
                if ($null -eq $line) { break }
                if ($stream -eq 'Output') {
                    Receive-WatcherLine $line
                    $running.Output = $running.Process.StandardOutput.ReadLineAsync()
                } else {
                    $running.LastError = $line
                    $running.ErrorOutput = $running.Process.StandardError.ReadLineAsync()
                }
            }
        }
        if ($running.Process.HasExited -and -not $running.Output -and -not $running.ErrorOutput) {
            $message = "Watcher đã thoát (mã $($running.Process.ExitCode)). $($running.LastError)".Trim()
            Close-Watcher
            if ($running.FatalReported) { $toggleItem.Text = 'Enable' }
            else { Show-TrayError $message }
        }
    } catch {
        $message = $_.Exception.Message
        Close-Watcher
        Show-TrayError $message
    }
}

try {
    Add-Type -AssemblyName System.Windows.Forms
    $context = [Windows.Forms.ApplicationContext]::new()
    $menu = [Windows.Forms.ContextMenuStrip]::new()
    $statusItem = $menu.Items.Add('Git Side Watcher')
    $statusItem.Enabled = $false
    $toggleItem = $menu.Items.Add('Enable')
    $exitItem = $menu.Items.Add('Exit')
    $icon = [Windows.Forms.NotifyIcon]::new()
    $icon.ContextMenuStrip = $menu
    Set-TrayDisplay 'PAUSED' ''
    $icon.Visible = $true

    $toggleItem.add_Click({
        try {
            if ($script:child) {
                Close-Watcher
                Set-TrayDisplay 'PAUSED' ''
            } else { Start-Watcher }
        } catch { Show-TrayError $_.Exception.Message }
    })
    $exitItem.add_Click({
        try { Close-Watcher; $context.ExitThread() }
        catch { Show-TrayError $_.Exception.Message }
    })
    $timer = [Windows.Forms.Timer]::new()
    $timer.Interval = 100
    $timer.add_Tick({
        try { Read-WatcherStreams }
        catch { Show-TrayError $_.Exception.Message }
    })
    Start-Watcher
    [Windows.Forms.Application]::Run($context)
} finally {
    try { Close-Watcher }
    finally {
        if ($timer) { $timer.Dispose() }
        if ($icon) { $icon.Visible = $false; $icon.Dispose() }
        if ($menu) { $menu.Dispose() }
        if ($context) { $context.Dispose() }
        $mutex.ReleaseMutex()
        $mutex.Dispose()
    }
}
