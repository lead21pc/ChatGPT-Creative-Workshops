[CmdletBinding()]
param(
    [ValidateSet('READ_ONLY')]
    [string]$Mode = 'READ_ONLY',

    [string[]]$ChangedControlFile = @(),

    [switch]$ListDrafts,

    # Optional JSON snapshot: { "root": "<repository root>", "files": [
    #   { "path": "<repository-relative path>", "sha256": "<SHA-256>" } ] }
    [string]$ProtectedSnapshotJson,

    # Supplied by a human; this runner never invokes or judges a model.
    [string]$ManualResultJson,

    # Only for an independently approved manual experiment; never activates a DRAFT.
    [switch]$ApprovedDraftExperiment,

    # Input-only probe for numeric ordering and duplicate-highest behavior.
    [string]$VersionProbeJson,

    # Input-only probe: { "path": "<project-relative control file>", "sha256": "<SHA-256>" }.
    [string]$AnchorProbeJson
)

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

$projectRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '..\..')).Path
$repositoryRoot = (Resolve-Path -LiteralPath (Join-Path $projectRoot '..')).Path
$caseRoot = Join-Path $PSScriptRoot 'cases'
$checks = [Collections.Generic.List[object]]::new()
$caseIssues = [Collections.Generic.List[string]]::new()
$cases = [Collections.Generic.List[object]]::new()
$staleCases = [Collections.Generic.List[object]]::new()
$draftReviewMatches = [Collections.Generic.List[object]]::new()
$staleReviewMatches = [Collections.Generic.List[object]]::new()

function Add-Check {
    param([string]$Name, [string]$Status, [object]$Detail)
    $checks.Add([pscustomobject]@{ name = $Name; status = $Status; detail = $Detail })
}

function Normalize-RelativePath {
    param([string]$Path)
    if ([string]::IsNullOrWhiteSpace($Path)) { throw 'Empty relative path.' }
    $normalized = $Path.Replace('\', '/').Trim()
    if ($normalized.StartsWith('./')) { $normalized = $normalized.Substring(2) }
    if ([IO.Path]::IsPathRooted($normalized) -or
        $normalized -match '(^|/)\.\.(/|$)' -or
        $normalized.StartsWith('/') -or
        $normalized.Contains(':')) {
        throw "Path must stay inside the repository: $Path"
    }
    return $normalized
}

function Read-JsonObject {
    param([string]$Json)
    $value = ConvertFrom-Json -InputObject $Json -AsHashtable -Depth 20
    if ($value -isnot [System.Collections.IDictionary]) {
        throw 'Expected a JSON object.'
    }
    return $value
}

function Resolve-NumericVersion {
    param(
        [string]$Family,
        [string[]]$Names,
        [string]$Pattern
    )
    $parsed = [Collections.Generic.List[object]]::new()
    $malformed = [Collections.Generic.List[string]]::new()
    foreach ($name in $Names) {
        $match = [regex]::Match($name, $Pattern, 'IgnoreCase')
        if (-not $match.Success) {
            $malformed.Add($name)
            continue
        }
        try {
            $parts = $match.Groups['version'].Value.Split('.')
            $major = [long]::Parse($parts[0])
            $minor = [long]::Parse($parts[1])
            $patch = if ($parts.Count -eq 3) { [long]::Parse($parts[2]) } else { [long]0 }
            $parsed.Add([pscustomobject]@{
                name = $name
                major = $major
                minor = $minor
                patch = $patch
            })
        }
        catch {
            $malformed.Add($name)
        }
    }
    if ($Names.Count -eq 0) {
        return [pscustomobject]@{ family = $Family; status = 'FAIL'; reason = 'NO_CANDIDATE'; highest = $null; version = $null }
    }
    if ($malformed.Count -gt 0) {
        return [pscustomobject]@{ family = $Family; status = 'FAIL'; reason = 'MALFORMED_VERSION'; files = @($malformed); highest = $null; version = $null }
    }
    $sorted = @($parsed | Sort-Object -Property major, minor, patch -Descending)
    $top = $sorted[0]
    $ties = @($sorted | Where-Object { $_.major -eq $top.major -and $_.minor -eq $top.minor -and $_.patch -eq $top.patch })
    $version = "$($top.major).$($top.minor).$($top.patch)"
    if ($ties.Count -gt 1) {
        return [pscustomobject]@{ family = $Family; status = 'FAIL'; reason = 'DUPLICATE_HIGHEST_VERSION'; files = @($ties | ForEach-Object name); highest = $null; version = $version }
    }
    return [pscustomobject]@{ family = $Family; status = 'PASS'; reason = 'NUMERIC_HIGHEST'; highest = $top.name; version = $version }
}

function Test-NonemptyString {
    param([System.Collections.IDictionary]$Item, [string]$Key)
    return ($Item.Contains($Key) -and $Item[$Key] -is [string] -and -not [string]::IsNullOrWhiteSpace($Item[$Key]))
}

$required = @(
    '00_AETHERFIRE_CONSOLIDATION_INDEX.md',
    '91_RECONCILIATION_RECORD.md',
    '92_OPEN_ISSUES_CURRENT.md',
    'MANIFEST.md',
    'build_consolidation.ps1',
    'Source_Archive'
)
$missing = @($required | Where-Object { -not (Test-Path -LiteralPath (Join-Path $projectRoot $_)) })
Add-Check 'package_presence' $(if ($missing.Count) { 'FAIL' } else { 'PASS' }) ([pscustomobject]@{ missing = $missing })

$families = @(
    [pscustomobject]@{ name = 'CI'; directory = 'Project Feather Core CI'; stem = 'FTH_CI_version_v'; pattern = '^FTH_CI_version_v(?<version>\d+\.\d+(?:\.\d+)?)\.md$' },
    [pscustomobject]@{ name = 'Source_Router'; directory = 'Anti-Drift Source'; stem = 'FTH_Anti_Drift_Source_Router_v'; pattern = '^FTH_Anti_Drift_Source_Router_v(?<version>\d+\.\d+(?:\.\d+)?)\.(?:md|yaml)$' },
    [pscustomobject]@{ name = 'Authoring_Pipeline'; directory = 'Anti-Drift Source'; stem = 'FTH_Authoring_Pipeline_v'; pattern = '^FTH_Authoring_Pipeline_v(?<version>\d+\.\d+(?:\.\d+)?)\.md$' },
    [pscustomobject]@{ name = 'Worldbuilding_Internal_Logic'; directory = 'Anti-Drift Source'; stem = 'FTH_Anti_Drift_Worldbuilding_Internal_Logic_v'; pattern = '^FTH_Anti_Drift_Worldbuilding_Internal_Logic_v(?<version>\d+\.\d+(?:\.\d+)?)\.md$' },
    [pscustomobject]@{ name = 'Interface_Economy_State_Stabilization'; directory = 'Anti-Drift Source'; stem = 'FTH_Anti_Drift_Interface_Economy_State_Stabilization_v'; pattern = '^FTH_Anti_Drift_Interface_Economy_State_Stabilization_v(?<version>\d+\.\d+(?:\.\d+)?)\.md$' },
    [pscustomobject]@{ name = 'Modular_Concept_Architecture'; directory = 'Anti-Drift Source'; stem = 'FTH_Anti_Drift_Modular_Concept_Architecture_v'; pattern = '^FTH_Anti_Drift_Modular_Concept_Architecture_v(?<version>\d+\.\d+(?:\.\d+)?)\.md$' },
    [pscustomobject]@{ name = 'Total_War_RP'; directory = 'Anti-Drift Source'; stem = 'FTH_Anti_Drift_Total_War_RP_v'; pattern = '^FTH_Anti_Drift_Total_War_RP_v(?<version>\d+\.\d+(?:\.\d+)?)\.md$' },
    [pscustomobject]@{ name = 'Mortality_Relationship_Plot_Immunity'; directory = 'Anti-Drift Source'; stem = 'FTH_Anti_Drift_Mortality_Relationship_Plot_Immunity_v'; pattern = '^FTH_Anti_Drift_Mortality_Relationship_Plot_Immunity_v(?<version>\d+\.\d+(?:\.\d+)?)\.md$' },
    [pscustomobject]@{ name = 'Actor_Reception_Normative_Signals'; directory = 'Anti-Drift Source'; stem = 'FTH_Anti_Drift_Actor_Reception_Normative_Signals_v'; pattern = '^FTH_Anti_Drift_Actor_Reception_Normative_Signals_v(?<version>\d+\.\d+(?:\.\d+)?)\.md$' },
    [pscustomobject]@{ name = 'Belief_Culture'; directory = 'Anti-Drift Source'; stem = 'FTH_Anti_Drift_Belief_Culture_v'; pattern = '^FTH_Anti_Drift_Belief_Culture_v(?<version>\d+\.\d+(?:\.\d+)?)\.md$' },
    [pscustomobject]@{ name = 'Undie_Professional_Gray_Zone'; directory = 'Anti-Drift Source'; stem = 'FTH_Anti_Drift_Undie_Professional_Gray_Zone_v'; pattern = '^FTH_Anti_Drift_Undie_Professional_Gray_Zone_v(?<version>\d+\.\d+(?:\.\d+)?)\.md$' }
)
$resolutions = @(
    foreach ($family in $families) {
        $directory = Join-Path $projectRoot $family.directory
        $names = if (Test-Path -LiteralPath $directory -PathType Container) {
            @(Get-ChildItem -LiteralPath $directory -File |
                Where-Object { $_.Name.StartsWith($family.stem, [StringComparison]::OrdinalIgnoreCase) -and $_.Extension -in @('.md', '.yaml') } |
                ForEach-Object Name)
        }
        else { @() }
        Resolve-NumericVersion -Family $family.name -Names $names -Pattern $family.pattern
    }
)
Add-Check 'numeric_versions' $(if (@($resolutions | Where-Object status -eq 'FAIL').Count) { 'FAIL' } else { 'PASS' }) $resolutions

# The upstream ChatGPT CI revision is declared by the selected Project CI.
# Versioned files merely present in the lineage are never selected by recency.
$currentVersioned = @{}
foreach ($family in $families) {
    $resolution = @($resolutions | Where-Object family -eq $family.name)[0]
    if ($resolution.status -eq 'PASS') {
        $currentVersioned[$family.name] = "$($family.directory)/$($resolution.highest)"
    }
}
$selectedUpstreamPath = $null
$baseDetail = $null
try {
    if (-not $currentVersioned.ContainsKey('CI')) { throw 'No resolved Project Feather Core CI.' }
    $ciPath = Join-Path $projectRoot $currentVersioned['CI']
    $declaration = [regex]::Match(
        [IO.File]::ReadAllText($ciPath),
        '^# Project Feather Core CI v(?<project>\d+\.\d+(?:\.\d+)?)\s+\(FTH\)\s+[—-]\s+ChatGPT v?(?<base>\d+\.\d+(?:\.\d+)?)(?<qualifier> temp(?: \d+)?)? base\s*$',
        [Text.RegularExpressions.RegexOptions]::Multiline -bor [Text.RegularExpressions.RegexOptions]::IgnoreCase
    )
    if (-not $declaration.Success) { throw 'Selected Project CI has no unambiguous ChatGPT CI base declaration.' }
    $declaredParts = @($declaration.Groups['project'].Value.Split('.') | ForEach-Object { [long]::Parse($_) })
    if ($declaredParts.Count -eq 2) { $declaredParts += [long]0 }
    $selectedVersion = @($resolutions | Where-Object family -eq 'CI')[0].version
    if (($declaredParts -join '.') -ne $selectedVersion) {
        throw 'Selected Project CI filename and declared Project CI version disagree.'
    }
    $selectedUpstreamPath = "llm-controls/global-instructions/ChatGPT Plus+ Era/chatgpt v$($declaration.Groups['base'].Value)$($declaration.Groups['qualifier'].Value).txt"
    $upstreamFile = Join-Path $repositoryRoot $selectedUpstreamPath
    if (-not (Test-Path -LiteralPath $upstreamFile -PathType Leaf)) {
        throw "Declared ChatGPT CI base is unavailable: $selectedUpstreamPath"
    }
    $baseDetail = [pscustomobject]@{ project_ci = $currentVersioned['CI']; upstream = $selectedUpstreamPath; origin = 'EXPLICIT_PROJECT_CI_DECLARATION' }
    Add-Check 'selected_upstream_base' 'PASS' $baseDetail
}
catch { Add-Check 'selected_upstream_base' 'BLOCKED' $_.Exception.Message }

function Get-ControlFamily {
    param([string]$Path)
    foreach ($family in $families) {
        if ($Path.StartsWith("$($family.directory)/$($family.stem)", [StringComparison]::OrdinalIgnoreCase) -and
            ([IO.Path]::GetFileName($Path) -match $family.pattern)) { return $family.name }
    }
    return $null
}

function Get-AnchorFile {
    param([string]$Path)
    if ($Path.StartsWith('llm-controls/global-instructions/ChatGPT Plus+ Era/', [StringComparison]::OrdinalIgnoreCase)) {
        return Join-Path $repositoryRoot $Path
    }
    return Join-Path $projectRoot $Path
}

if (-not (Test-Path -LiteralPath $caseRoot -PathType Container)) {
    $caseIssues.Add('Missing cases directory.')
}
else {
    $caseFiles = @(Get-ChildItem -LiteralPath $caseRoot -File -Filter '*.json' | Sort-Object Name)
    if ($caseFiles.Count -eq 0) { $caseIssues.Add('No JSON cases.') }
    $ids = [Collections.Generic.HashSet[string]]::new([StringComparer]::OrdinalIgnoreCase)
    foreach ($file in $caseFiles) {
        try {
            $item = Read-JsonObject ([IO.File]::ReadAllText($file.FullName))
            foreach ($key in @('id','layer','status','operation','boundary','input','protected_distinction','forbidden_conversion')) {
                if (-not (Test-NonemptyString $item $key)) { throw "Missing or invalid $key." }
            }
            if ($item['id'] -ne $file.BaseName -or -not $ids.Add($item['id'])) { throw 'Case ID must match its unique filename.' }
            if ($item['layer'] -notin @('STRUCTURAL','CONTROL_SEMANTIC','LIVE_RUNTIME')) { throw 'Invalid layer.' }
            if ($item['status'] -notin @('DRAFT','ACTIVE','STALE_CANDIDATE','RETIRED')) { throw 'Invalid lifecycle status.' }
            if ($item['provenance'] -isnot [System.Collections.IDictionary] -or
                -not (Test-NonemptyString $item['provenance'] 'kind') -or
                -not (Test-NonemptyString $item['provenance'] 'reference') -or
                -not (Test-NonemptyString $item['provenance'] 'note')) { throw 'Invalid provenance.' }
            if ($item['recheck_on'] -isnot [array] -or $item['recheck_on'].Count -eq 0) { throw 'Invalid recheck_on.' }
            foreach ($pattern in $item['recheck_on']) {
                if ($pattern -isnot [string]) { throw 'Invalid recheck_on entry.' }
                [void](Normalize-RelativePath $pattern)
            }
            $effectiveStatus = $item['status']
            $anchorReasons = [Collections.Generic.List[string]]::new()
            if ($item.Contains('control_anchor') -and $item.Contains('active_control_anchors')) {
                throw 'Use one anchor representation, not both.'
            }
            $anchors = if ($item.Contains('active_control_anchors')) {
                if ($item['active_control_anchors'] -isnot [array] -or $item['active_control_anchors'].Count -eq 0) {
                    throw 'Invalid active_control_anchors.'
                }
                @($item['active_control_anchors'])
            }
            elseif ($item.Contains('control_anchor')) { @($item['control_anchor']) }
            else { @() }
            $anchorPaths = [Collections.Generic.HashSet[string]]::new([StringComparer]::OrdinalIgnoreCase)
            foreach ($anchor in $anchors) {
                if ($anchor -isnot [System.Collections.IDictionary] -or
                    -not (Test-NonemptyString $anchor 'path') -or
                    -not (Test-NonemptyString $anchor 'sha256') -or
                    $anchor['sha256'] -notmatch '^[a-fA-F0-9]{64}$') { throw 'Invalid control_anchor.' }
                $relative = Normalize-RelativePath $anchor['path']
                if (-not $anchorPaths.Add($relative)) { throw "Duplicate active anchor: $relative" }
                $anchorPath = Get-AnchorFile $relative
                if (-not (Test-Path -LiteralPath $anchorPath -PathType Leaf)) {
                    $anchorReasons.Add("ANCHOR_MISSING: $relative")
                }
                elseif ((Get-FileHash -LiteralPath $anchorPath -Algorithm SHA256).Hash -ne $anchor['sha256']) {
                    $anchorReasons.Add("ANCHOR_HASH_CHANGED: $relative")
                }
                $anchorFamily = Get-ControlFamily $relative
                if ($anchorFamily -and $currentVersioned.ContainsKey($anchorFamily) -and
                    $relative -ne $currentVersioned[$anchorFamily]) {
                    $anchorReasons.Add("ACTIVE_VERSION_CHANGED: $relative -> $($currentVersioned[$anchorFamily])")
                }
                if ($relative.StartsWith('llm-controls/global-instructions/ChatGPT Plus+ Era/chatgpt v', [StringComparison]::OrdinalIgnoreCase) -and
                    $relative -ne $selectedUpstreamPath) {
                    $anchorReasons.Add("SELECTED_BASE_CHANGED: $relative -> $selectedUpstreamPath")
                }
            }
            $record = [pscustomobject]@{
                id = $item['id']
                layer = $item['layer']
                recorded_status = $item['status']
                effective_status = $effectiveStatus
                review_required = ($anchorReasons.Count -gt 0)
                anchor_reason = if ($anchorReasons.Count) { $anchorReasons[0] } else { $null }
                anchor_reasons = @($anchorReasons)
                active_anchor_paths = @($anchorPaths)
                recheck_on = @($item['recheck_on'])
            }
            $cases.Add($record)
            if ($effectiveStatus -eq 'STALE_CANDIDATE' -or
                ($effectiveStatus -eq 'ACTIVE' -and $record.review_required)) { $staleCases.Add($record) }
        }
        catch {
            $caseIssues.Add("$($file.Name): $($_.Exception.Message)")
        }
    }
}
Add-Check 'case_schema' $(if ($caseIssues.Count) { 'FAIL' } else { 'PASS' }) ([pscustomobject]@{ count = $cases.Count; issues = @($caseIssues) })

$changed = [Collections.Generic.List[string]]::new()
$unmapped = [Collections.Generic.List[string]]::new()
$selected = [Collections.Generic.List[object]]::new()
foreach ($path in $ChangedControlFile) {
    try { $changed.Add((Normalize-RelativePath $path)) }
    catch { Add-Check 'changed_path' 'FAIL' $_.Exception.Message }
}
if ($changed.Count -eq 0) {
    foreach ($item in $cases) {
        if ($item.effective_status -eq 'ACTIVE' -and -not $item.review_required) { $selected.Add($item) }
    }
}
else {
    foreach ($path in $changed) {
        $changedFamily = Get-ControlFamily $path
        $isInactiveVersion = $changedFamily -and $currentVersioned.ContainsKey($changedFamily) -and
            $path -ne $currentVersioned[$changedFamily]
        $isInactiveUpstream = $path.StartsWith('llm-controls/global-instructions/ChatGPT Plus+ Era/chatgpt v', [StringComparison]::OrdinalIgnoreCase) -and
            $path -ne $selectedUpstreamPath
        $hits = @($cases | Where-Object {
            $case = $_
            if ($case.effective_status -eq 'RETIRED') { return $false }
            if ($isInactiveVersion -or $isInactiveUpstream) { return $false }
            if (@($case.recheck_on | Where-Object { $path -like $_ }).Count -gt 0) { return $true }
            if ($changedFamily -and $currentVersioned[$changedFamily] -eq $path) {
                return @($case.active_anchor_paths | Where-Object { (Get-ControlFamily $_) -eq $changedFamily }).Count -gt 0
            }
            if ($selectedUpstreamPath -eq $path) {
                return @($case.active_anchor_paths | Where-Object {
                    $_.StartsWith('llm-controls/global-instructions/ChatGPT Plus+ Era/chatgpt v', [StringComparison]::OrdinalIgnoreCase)
                }).Count -gt 0
            }
            return $false
        })
        if ($hits.Count -eq 0) { $unmapped.Add($path) }
        foreach ($hit in $hits) {
            if ($hit.effective_status -eq 'ACTIVE' -and -not $hit.review_required -and
                -not @($selected | Where-Object id -eq $hit.id).Count) { $selected.Add($hit) }
            elseif ($hit.effective_status -eq 'DRAFT' -and
                -not @($draftReviewMatches | Where-Object id -eq $hit.id).Count) { $draftReviewMatches.Add($hit) }
            elseif (($hit.effective_status -eq 'STALE_CANDIDATE' -or
                     ($hit.effective_status -eq 'ACTIVE' -and $hit.review_required)) -and
                -not @($staleReviewMatches | Where-Object id -eq $hit.id).Count) { $staleReviewMatches.Add($hit) }
        }
    }
}

$snapshotDetail = [pscustomobject]@{ coverage = 'NO_TASK_START_SNAPSHOT'; checked = 0; mismatches = @() }
if ([string]::IsNullOrWhiteSpace($ProtectedSnapshotJson)) {
    Add-Check 'protected_snapshot' 'LIMITED_CHECK' $snapshotDetail
}
else {
    try {
        $snapshot = Read-JsonObject $ProtectedSnapshotJson
        if (-not (Test-NonemptyString $snapshot 'root') -or $snapshot['files'] -isnot [array]) {
            throw 'Snapshot needs root and files array.'
        }
        $snapshotRoot = [IO.Path]::GetFullPath($snapshot['root'])
        if ($snapshotRoot.TrimEnd('\') -ne $repositoryRoot.TrimEnd('\')) { throw 'Snapshot root differs from repository root.' }
        $mismatches = [Collections.Generic.List[string]]::new()
        $seen = [Collections.Generic.HashSet[string]]::new([StringComparer]::OrdinalIgnoreCase)
        foreach ($entry in $snapshot['files']) {
            if ($entry -isnot [System.Collections.IDictionary] -or
                -not (Test-NonemptyString $entry 'path') -or
                -not (Test-NonemptyString $entry 'sha256') -or
                $entry['sha256'] -notmatch '^[a-fA-F0-9]{64}$') { throw 'Invalid snapshot entry.' }
            $relative = Normalize-RelativePath $entry['path']
            if (-not $seen.Add($relative)) { throw "Duplicate snapshot path: $relative" }
            $filePath = Join-Path $repositoryRoot $relative
            if (-not (Test-Path -LiteralPath $filePath -PathType Leaf)) {
                $mismatches.Add("MISSING: $relative")
            }
            elseif ((Get-FileHash -LiteralPath $filePath -Algorithm SHA256).Hash -ne $entry['sha256']) {
                $mismatches.Add("HASH_CHANGED: $relative")
            }
        }
        $snapshotDetail = [pscustomobject]@{ coverage = 'SUPPLIED_FILES_ONLY'; checked = $seen.Count; mismatches = @($mismatches) }
        Add-Check 'protected_snapshot' $(if ($mismatches.Count) { 'FAIL' } else { 'LIMITED_CHECK' }) $snapshotDetail
    }
    catch { Add-Check 'protected_snapshot' 'BLOCKED' $_.Exception.Message }
}

$gitState = $null
try {
    $gitState = @(git -c "safe.directory=$($repositoryRoot.Replace('\','/'))" -C $repositoryRoot status --short --branch)
    if ($LASTEXITCODE -ne 0) { throw "git status exit code $LASTEXITCODE" }
    Add-Check 'git_inspection' 'PASS' ([pscustomobject]@{ status = $gitState })
}
catch { Add-Check 'git_inspection' 'BLOCKED' $_.Exception.Message }

$manual = $null
if (-not [string]::IsNullOrWhiteSpace($ManualResultJson)) {
    try {
        $result = Read-JsonObject $ManualResultJson
        foreach ($key in @('case_id','target','response','result_label','assessment_note')) {
            if (-not (Test-NonemptyString $result $key)) { throw "Missing or invalid $key." }
        }
        if ($result['result_label'] -notin @('PASS','POTENTIAL_VIOLATION','AMBIGUOUS','BLOCKED')) {
            throw 'Invalid semantic result label.'
        }
        $matchCase = @($cases | Where-Object id -eq $result['case_id'])
        if ($matchCase.Count -ne 1) { throw 'Manual result must reference one valid case.' }
        if ($matchCase[0].recorded_status -eq 'DRAFT' -and -not $ApprovedDraftExperiment) {
            throw 'DRAFT_RESULT_REQUIRES_APPROVED_EXPERIMENT'
        }
        if ($matchCase[0].recorded_status -in @('STALE_CANDIDATE','RETIRED') -or
            ($matchCase[0].recorded_status -eq 'ACTIVE' -and $matchCase[0].review_required)) {
            throw 'CASE_REQUIRES_REVIEW_BEFORE_RESULT_INGESTION'
        }
        $sha = [Security.Cryptography.SHA256]::HashData([Text.Encoding]::UTF8.GetBytes($result['response']))
        $manual = [pscustomobject]@{
            case_id = $result['case_id']
            target = $result['target']
            result_label = $result['result_label']
            assessment_note = $result['assessment_note']
            response_sha256 = [Convert]::ToHexString($sha)
            response_characters = $result['response'].Length
            case_status = $matchCase[0].effective_status
            advisory_only = $true
            draft_experiment_declared = [bool]($matchCase[0].recorded_status -eq 'DRAFT' -and $ApprovedDraftExperiment)
            origin = 'USER_SUPPLIED_NOT_AUTOMATICALLY_EVALUATED'
        }
        Add-Check 'manual_ingestion' 'PASS' 'Supplied result validated in memory; no model was called.'
    }
    catch {
        $manualStatus = if ($_.Exception.Message -in @(
            'DRAFT_RESULT_REQUIRES_APPROVED_EXPERIMENT',
            'CASE_REQUIRES_REVIEW_BEFORE_RESULT_INGESTION'
        )) { 'BLOCKED' } else { 'FAIL' }
        Add-Check 'manual_ingestion' $manualStatus $_.Exception.Message
    }
}

$probe = $null
if (-not [string]::IsNullOrWhiteSpace($VersionProbeJson)) {
    try {
        $inputObject = Read-JsonObject $VersionProbeJson
        if ($inputObject['names'] -isnot [array] -or $inputObject['family'] -notin @($families.name)) {
            throw 'Probe needs names array and known family.'
        }
        $family = @($families | Where-Object name -eq $inputObject['family'])[0]
        $probe = Resolve-NumericVersion -Family $family.name -Names $inputObject['names'] -Pattern $family.pattern
        Add-Check 'version_probe' $probe.status $probe
    }
    catch { Add-Check 'version_probe' 'BLOCKED' $_.Exception.Message }
}

$anchorProbe = $null
if (-not [string]::IsNullOrWhiteSpace($AnchorProbeJson)) {
    try {
        $anchorInput = Read-JsonObject $AnchorProbeJson
        if (-not (Test-NonemptyString $anchorInput 'path') -or
            -not (Test-NonemptyString $anchorInput 'sha256') -or
            $anchorInput['sha256'] -notmatch '^[a-fA-F0-9]{64}$') { throw 'Invalid anchor probe.' }
        $anchorRelative = Normalize-RelativePath $anchorInput['path']
        $anchorFile = Join-Path $projectRoot $anchorRelative
        $anchorReason = if (-not (Test-Path -LiteralPath $anchorFile -PathType Leaf)) { 'ANCHOR_MISSING' }
                        elseif ((Get-FileHash -LiteralPath $anchorFile -Algorithm SHA256).Hash -ne $anchorInput['sha256']) { 'ANCHOR_HASH_CHANGED' }
                        else { $null }
        $anchorProbe = [pscustomobject]@{
            path = $anchorRelative
            effective_status = if ($anchorReason) { 'STALE_CANDIDATE' } else { 'ACTIVE' }
            reason = $anchorReason
        }
        Add-Check 'anchor_probe' 'PASS' $anchorProbe
    }
    catch { Add-Check 'anchor_probe' 'BLOCKED' $_.Exception.Message }
}

Add-Check 'package_integrity' 'LIMITED_CHECK' 'Default mode checks presence only. Existing package verifier, manifest hashes, and build were not invoked.'
$overall = if (@($checks | Where-Object status -eq 'FAIL').Count) { 'FAIL' }
           elseif (@($checks | Where-Object status -eq 'BLOCKED').Count) { 'BLOCKED' }
           else { 'LIMITED_CHECK' }

[pscustomobject]@{
    mode = $Mode
    overall = $overall
    checks = @($checks)
    changed_control_files = @($changed)
    selected_cases = @($selected | ForEach-Object { [pscustomobject]@{ id = $_.id; layer = $_.layer; status = $_.recorded_status; anchor_reasons = $_.anchor_reasons } })
    draft_cases = @(if ($ListDrafts) { $cases | Where-Object recorded_status -eq 'DRAFT' | ForEach-Object {
        [pscustomobject]@{ id = $_.id; status = 'DRAFT'; anchor_reasons = $_.anchor_reasons; review_only = $true }
    } })
    draft_review_matches = @($draftReviewMatches | ForEach-Object {
        [pscustomobject]@{ id = $_.id; status = 'DRAFT'; anchor_reasons = $_.anchor_reasons; review_only = $true }
    })
    draft_anchor_warnings = @($cases | Where-Object {
        $_.recorded_status -eq 'DRAFT' -and $_.review_required
    } | ForEach-Object {
        [pscustomobject]@{ id = $_.id; status = 'DRAFT'; reasons = $_.anchor_reasons; review_only = $true }
    })
    stale_candidates = @($staleCases | ForEach-Object {
        [pscustomobject]@{
            id = $_.id
            recorded_status = $_.recorded_status
            reasons = if ($_.anchor_reasons.Count) { $_.anchor_reasons } else { @('RECORDED_STALE') }
            review_only = $true
        }
    })
    stale_review_matches = @($staleReviewMatches | ForEach-Object {
        [pscustomobject]@{ id = $_.id; recorded_status = $_.recorded_status; reasons = $_.anchor_reasons; review_only = $true }
    })
    unmapped = @($unmapped)
    manual_result = $manual
    version_probe = $probe
    anchor_probe = $anchorProbe
    effective_control = $baseDetail
    model_executed = $false
    build_executed = $false
} | ConvertTo-Json -Depth 12

if ($overall -eq 'FAIL') { exit 1 }
if ($overall -eq 'BLOCKED') { exit 2 }
