$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

$tempRoot = $PSScriptRoot
$sourceRoot = Join-Path $tempRoot 'Source_Archive'
$utf8NoBom = [System.Text.UTF8Encoding]::new($false)

function Read-MarkdownSource {
    param([Parameter(Mandatory)][string]$Name)

    $path = Join-Path $sourceRoot $Name
    if (-not (Test-Path -LiteralPath $path -PathType Leaf)) {
        throw "Missing source: $Name"
    }

    $text = [System.IO.File]::ReadAllText($path, $utf8NoBom)
    return (($text -replace "`r`n", "`n") -replace "`r", "`n")
}

function Get-Range {
    param(
        [Parameter(Mandatory)][string]$Text,
        [Parameter(Mandatory)][string]$Start,
        [string]$End
    )

    $startIndex = $Text.IndexOf($Start, [System.StringComparison]::Ordinal)
    if ($startIndex -lt 0) {
        throw "Start anchor not found: $Start"
    }

    if ([string]::IsNullOrEmpty($End)) {
        return $Text.Substring($startIndex).Trim()
    }

    $endIndex = $Text.IndexOf($End, $startIndex + $Start.Length, [System.StringComparison]::Ordinal)
    if ($endIndex -lt 0) {
        throw "End anchor not found: $End"
    }

    return $Text.Substring($startIndex, $endIndex - $startIndex).Trim()
}

function Get-H1Section {
    param(
        [Parameter(Mandatory)][string]$Text,
        [Parameter(Mandatory)][string]$Heading
    )

    $needle = "`n$Heading"
    if ($Text.StartsWith($Heading, [System.StringComparison]::Ordinal)) {
        $startIndex = 0
    }
    else {
        $found = $Text.IndexOf($needle, [System.StringComparison]::Ordinal)
        if ($found -lt 0) {
            throw "H1 heading not found: $Heading"
        }
        $startIndex = $found + 1
    }

    $searchFrom = $startIndex + $Heading.Length
    $nextIndex = $Text.IndexOf("`n# ", $searchFrom, [System.StringComparison]::Ordinal)
    if ($nextIndex -lt 0) {
        return $Text.Substring($startIndex).Trim()
    }

    return $Text.Substring($startIndex, $nextIndex - $startIndex).Trim()
}

function Join-H1Sections {
    param(
        [Parameter(Mandatory)][string]$Text,
        [Parameter(Mandatory)][string[]]$Headings
    )

    $parts = foreach ($heading in $Headings) {
        Get-H1Section -Text $Text -Heading $heading
    }
    return ($parts -join "`n`n---`n`n")
}

function Shift-MarkdownHeadings {
    param(
        [Parameter(Mandatory)][string]$Text,
        [int]$Levels = 1
    )

    $shifted = $Text
    foreach ($step in 1..$Levels) {
        $shifted = [regex]::Replace(
            $shifted,
            '(?m)^(#{1,5})(?=\s)',
            { param($match) '#' + $match.Value }
        )
    }

    return $shifted.Trim()
}

function Write-MarkdownOutput {
    param(
        [Parameter(Mandatory)][string]$Name,
        [Parameter(Mandatory)][string]$Content
    )

    $normalized = (($Content -replace "`r`n", "`n") -replace "`r", "`n").TrimEnd() + "`n"
    [System.IO.File]::WriteAllText((Join-Path $tempRoot $Name), $normalized, $utf8NoBom)
}

function Replace-Required {
    param(
        [Parameter(Mandatory)][string]$Text,
        [Parameter(Mandatory)][string]$Old,
        [Parameter(Mandatory)][string]$New,
        [Parameter(Mandatory)][string]$Label
    )

    if (-not $Text.Contains($Old, [System.StringComparison]::Ordinal)) {
        throw "Required reconciliation text not found: $Label"
    }

    return $Text.Replace($Old, $New, [System.StringComparison]::Ordinal)
}

function Remove-RequiredRange {
    param(
        [Parameter(Mandatory)][string]$Text,
        [Parameter(Mandatory)][string]$Start,
        [Parameter(Mandatory)][string]$End,
        [Parameter(Mandatory)][string]$Label
    )

    $startIndex = $Text.IndexOf($Start, [System.StringComparison]::Ordinal)
    if ($startIndex -lt 0) {
        throw "Required range start not found: $Label"
    }

    $endIndex = $Text.IndexOf($End, $startIndex + $Start.Length, [System.StringComparison]::Ordinal)
    if ($endIndex -lt 0) {
        throw "Required range end not found: $Label"
    }

    return ($Text.Substring(0, $startIndex) + $Text.Substring($endIndex)).Trim()
}

function Apply-UndieRankTerminology {
    param([Parameter(Mandatory)][string]$Text)

    $replacements = [ordered]@{
        'functional color/track/cấp nghề' = 'Undie rank'
        'functional colors/tracks' = 'Undie ranks'
        'functional color / track' = 'Undie rank'
        'functional color/track' = 'Undie rank'
        'functional color/Career Rank' = 'Undie rank/Career Rank'
        'functional color labels' = 'Undie rank labels'
        'functional color label' = 'Undie rank label'
        'functional-color axis' = 'Undie-rank axis'
        'functional track/color' = 'Undie rank'
        'functional colors' = 'Undie ranks'
        'functional track' = 'Undie rank'
        'functional color' = 'Undie rank color'
        'Undie functional graph' = 'Undie-rank graph'
        'functional graph' = 'Undie-rank graph'
        'Undie rank Undie' = 'Undie rank'
        'Undie Undie rank' = 'Undie rank'
    }

    $normalized = $Text
    foreach ($old in $replacements.Keys) {
        $normalized = [regex]::Replace(
            $normalized,
            [regex]::Escape($old),
            $replacements[$old],
            [System.Text.RegularExpressions.RegexOptions]::IgnoreCase
        )
    }
    return $normalized
}

$merged = Read-MarkdownSource 'aetherfire_canon_hop_nhat_merged_v2.md'
$ontology = Read-MarkdownSource 'aetherfire_current_status_ontology_map.md'
$civil = Read-MarkdownSource 'aetherfire_civil_entry_allocation_law_canon.md'
$revamp = Read-MarkdownSource 'aetherfire_undie_civil_citizen_revamp_canon_1_42.md'
$undieMobility = Read-MarkdownSource 'aetherfire_anti_drift_sex_worker_consent_mobility_white.md'
$uniform = Read-MarkdownSource 'aetherfire_undie_undi_uniform_system_and_mc2_visual_fall.md'
$undiHoaNguyet = Read-MarkdownSource 'aetherfire_undi_hoa_nguyet_cultural_humiliation_design_philosophy.md'
$delta = Read-MarkdownSource 'aetherfire_delta_since_last_anti_drift_export.md'
$history = Read-MarkdownSource 'aetherfire_design_history_and_reconsiderations.md'
$rpHistory = Read-MarkdownSource 'aetherfire_rp_cu_ba_truc_lich_su_va_de_xuat.md'
foreach ($anchor in @('# 2. Nguồn gốc RP cũ', '# 4. Thánh quốc thời kỳ cũ', '# 5. Hoa Nguyệt thời kỳ cũ', '# 9. RP cũ chạy trên ba trục đồng thời', '# 17. Các đề xuất tái sử dụng genealogy cũ')) {
    if (-not $rpHistory.Contains($anchor, [System.StringComparison]::Ordinal)) {
        throw "RP history source anchor missing: $anchor"
    }
}
$report = Read-MarkdownSource 'aetherfire_reconciliation_report.md'
$register = Read-MarkdownSource 'aetherfire_conflict_register.md'
$fictionModel = Read-MarkdownSource 'aetherfire_fiction0_fiction1_model.md'
$canonComparison = Read-MarkdownSource 'aetherfire_canon1_canon2.md'
$storyOverlap = Read-MarkdownSource 'aetherfire_canon_story_line_v0_5_v1_0_overlap.md'
$narrators = Read-MarkdownSource 'aetherfire_narrators_pov_clash_humor.md'
$matriarch = Read-MarkdownSource 'matriarchs_lament_working_retcon_canon.md'
$mc4Source = Read-MarkdownSource 'aetherfire_mc4_identity_remake_working.md'
$academySource = Read-MarkdownSource 'aetherfire_battlemage_academy_setting_working.md'
$rfAxesSource = Read-MarkdownSource 'aetherfire_rf_nguyen_chu_dynastic_power_axes_chat_consolidation.md'
$rfGeopoliticsSource = Read-MarkdownSource 'aetherfire_rf_crossworld_geopolitics_chat_consolidation_2026-09-15.md'
$taintedCosmosMerged = Read-MarkdownSource 'The Tainted Cosmos - MERGED.md'
$openIssuesSeed = Read-MarkdownSource 'aetherfire_open_issues_current_restored_2026-09-15.md'
$aviationSource = Read-MarkdownSource 'aetherfire_stable_aviation_rf_airspace_control_canon_delta_2026-09-16.md'

$storyFenceCount = [regex]::Matches($storyOverlap, '(?m)^```').Count
if (($storyFenceCount % 2) -ne 0) {
    $storyOverlap = Replace-Required -Text $storyOverlap -Old "ENDING EXISTS`n≠`nEXACT CANON-1 IMPLEMENTATION IS GUARANTEED." -New ("ENDING EXISTS`n≠`nEXACT CANON-1 IMPLEMENTATION IS GUARANTEED.`n" + '```') -Label 'story-overlap final code fence'
}

$matriarchFenceCount = [regex]::Matches($matriarch, '(?m)^```').Count
if (($matriarchFenceCount % 2) -ne 0) {
    $matriarch = $matriarch.TrimEnd() + "`n" + '```'
}

$matriarchCurrent = Replace-Required -Text $matriarch -Old "# Matriarch's Lament — Working Retcon Canon" -New "# Matriarch's Lament — Current Regional Canon" -Label 'Matriarch title promotion'
$matriarchCurrent = Replace-Required -Text $matriarchCurrent -Old '> **Trạng thái:** WORKING CANON / USER-CONFIRMED STATE trước vòng cập nhật canon tiếp theo' -New '> **Trạng thái:** CURRENT CANON / CONTROLLING REGIONAL RETCON — integrated 2026-09-11' -Label 'Matriarch status promotion'
$matriarchCurrent = Remove-RequiredRange -Text $matriarchCurrent -Start '## 13. Gián điệp và Undie punitive rule' -End '## 14. Transfusion EasterFire' -Label 'remove foreign-spy punitive Undie route'
$matriarchCurrent = $matriarchCurrent.Replace('- exact legal threshold cho spy punitive route;' + "`n", '', [System.StringComparison]::Ordinal)
$matriarchCurrent = Replace-Required -Text $matriarchCurrent -Old '> **Trạng thái:** CURRENT CANON / CONTROLLING REGIONAL RETCON — integrated 2026-09-11' -New @'
> **Trạng thái:** CURRENT CANON / CONTROLLING MATRIARCH'S LAMENT DOMAIN — integrated 2026-09-11; architecture split recorded 2026-09-16  
> **Authority boundary:** this file controls internal Matriarch's Lament governance, Temple/Cult/Creed, Holy Guard, Trinity/relic economy, Trần Trúc Nha's regional role and doctrine, ML–TE routes/covert operations, and the northeastern tribes. Cross-domain interfaces are summarized in `10`; Undie status interfaces are controlled by `30`; cross-world status is controlled by `40`.  
> **Trúc Nha boundary:** membership and regional role in ML are current canon. A summoned/cross-world origin remains `UNDER CONSTRUCTION / NOT CURRENT CANON`.
'@ -Label 'Matriarch child-domain authority boundary'

$aviationCurrent = Replace-Required -Text $aviationSource -Old '# AetherFire — Stable Aviation, RF Dependency & Airspace Control' -New '# AetherFire — Stable Aviation & RF Airspace Current Canon' -Label 'stable aviation title promotion'
$aviationCurrent = Replace-Required -Text $aviationCurrent -Old '> **Trạng thái:** USER-CONFIRMED DESIGN DIRECTION / CANON DELTA từ chat 2026-09-16, chờ merge vào current canon package.' -New @'
> **Trạng thái:** CURRENT CANON / CONTROLLING STABLE AVIATION & RF AIRSPACE DOMAIN — integrated 2026-09-17.
> **Authority boundary:** this file controls AF stable/scalable aviation, the AF–RF aviation dependency, airspace/ATC/economy separation, mixed airspace and air-route leverage. `10` retains only the world/geopolitics interface.
> **Interpretation boundary:** AF is the only currently confirmed actor with stable, scalable aviation infrastructure; this is not proof that no other actor can ever possess it. Statements about RF response describe incentives and strategic direction for relevant RF/member-state authorities, not proof of a unitary RF policy or completed implementation.
> **Cross-project exclusion:** the source sentence about The Kingdom airspace is not imported as AetherFire lore or as a claim about The Kingdom canon.
'@ -Label 'stable aviation status promotion'
$aviationCurrent = Replace-Required -Text $aviationCurrent -Old '## 2. Chốt capability: AF độc quyền **stable aviation**, không độc quyền khả năng bay' -New '## 2. Chốt capability: AF là actor duy nhất hiện được xác nhận có **stable aviation**, không độc quyền khả năng bay' -Label 'stable aviation nonexclusive heading'
$aviationCurrent = $aviationCurrent.Replace('hàng nghìn hoặc hàng vạn chuyến bay diễn ra như một utility', 'hoạt động bay hàng loạt, theo lịch và có thể scale diễn ra như một utility', [System.StringComparison]::Ordinal)
$aviationCurrent = Replace-Required -Text $aviationCurrent -Old 'RF sẽ cố tách ít nhất ba miền:' -New 'Các authority liên quan ở cấp RF/member-state có incentive tách ít nhất ba miền; exact actor và phân quyền giữ `UNKNOWN`:' -Label 'RF aviation actor granularity'
$aviationCurrent = Replace-Required -Text $aviationCurrent -Old 'RF sẽ cố giảm dependency theo từng lớp thay vì tự cô lập:' -New @'
Các authority liên quan ở cấp RF/member-state có incentive giảm dependency theo từng lớp thay vì tự cô lập. Chuỗi dưới đây là một **dependency-reduction pathway**, không phải chronology đã được xác nhận là đã xảy ra:
'@ -Label 'RF aviation localization pathway'
$aviationCurrent = Replace-Required -Text $aviationCurrent -Old 'Đây là logic đã chốt ở cấp direction, không phải danh sách ban ngành canon:' -New 'Đây là logic đã chốt ở cấp strategic direction, không phải danh sách ban ngành canon hoặc bằng chứng rằng các safeguard đã được triển khai đầy đủ:' -Label 'RF aviation safeguards status'
$aviationCurrent = $aviationCurrent.Replace("THE KINGDOM AIRSPACE CONCEPTS = RETIRED FOR THIS CHAT.`n`n", '', [System.StringComparison]::Ordinal)
$aviationCurrent = Replace-Required -Text $aviationCurrent -Old 'AF MONOPOLIZES / LEADS STABLE, SCALABLE AVIATION AS INFRASTRUCTURE.' -New 'AF IS THE ONLY CURRENTLY CONFIRMED ACTOR WITH STABLE, SCALABLE AVIATION AS INFRASTRUCTURE.' -Label 'stable aviation sole-confirmed anti-drift rule'

$index = @'
# AetherFire — Consolidation Index

> **Generated consolidation baseline:** 2026-09-08; latest integration: 2026-09-17
> **Location:** self-contained `AetherFire Project/` package. Canon outputs live at the project root; immutable build inputs are preserved under `Source_Archive/`.  
> **Truth rule:** `ABSENCE OF CANON ≠ CANONICAL NEGATION`; `NOT ESTABLISHED ≠ FALSE`; unresolved relations remain `UNKNOWN / UNRESOLVED`.

## 1. Canonical reading order

1. `10_WORLD_INSTITUTIONS_GEOPOLITICS_CURRENT.md` — project identity, state, institutions, geopolitics and dynastic conflict.
2. `20_STATUS_CIVIL_LABOR_CURRENT.md` — status ontology, Citizen/Civil/Yellow/POW/Criminal, Civil entry/allocation/lifecycle and cross-status mobility.
3. `30_UNDIE_SYSTEM_CURRENT.md` — Undie identity, intake, consent, Undie ranks, mobility, White, work/economy/access and Undi visual system.
4. `40_METAFICTION_CANON_TIMELINE_CURRENT.md` — Fiction 0/Fiction 1, Fictionize/POC, V0.5, Canon 1/Canon 2, both clashes, causal overlap and knowledge asymmetry.
5. `50_NARRATORS_POV_AND_HUMOR_CURRENT.md` — narrator personification, Elena POV, deadpan humor and the narrator split at Clash #2.
6. `60_MC4_IDENTITY_CURRENT.md` — current MC4 identity, Academy membership and strict legacy-import boundaries.
7. `70_MATRIARCHS_LAMENT_CURRENT.md` — internal Matriarch's Lament governance, Temple/Cult/Creed, Holy Guard, Trinity/relic economy, Trần Trúc Nha, ML–TE operations and northeastern tribes.
8. `80_STABLE_AVIATION_RF_AIRSPACE_CURRENT.md` — AF stable/scalable aviation, AF–RF aviation dependency, RF airspace/ATC/economy separation, mixed airspace and route leverage.
9. `90_DESIGN_HISTORY_AND_RECONSIDERATIONS.md` — genealogy, retired designs, surviving mechanisms and proposals under consideration; not a current world bible.
10. `91_RECONCILIATION_RECORD.md` — resolved conflicts, unresolved questions and source provenance.
11. `92_OPEN_ISSUES_CURRENT.md` — compact control ledger; not a world-bible source.

## 2. Document architecture

```text
AETHERFIRE CURRENT CANON
├─ World / institutions / geopolitics
│  ├─ AetherFire state, RF, Academy and global interfaces
│  ├─ Matriarch's Lament / Transfusion EasterFire cross-domain interface
│  └─ Quad Night retirement and orphaned relations
├─ Status / Civil / labor
│  ├─ ontology schema
│  ├─ Civil entry and allocation
│  ├─ operational lifecycle
│  └─ transitions among Citizen, Civil, Yellow, POW and Criminal
├─ Undie subsystem
   ├─ class identity and social function
   ├─ intake and consent
   ├─ Undie ranks and mobility
   ├─ economy, work and access
   ├─ White exit pathway
   └─ Undi visual and administrative interface
├─ Metafiction / canon timeline
│  ├─ Fiction 0 / Fiction 1 and ability boundaries
│  ├─ V0.5 continuations and Canon 1 / Canon 2
│  └─ causal overlap, clashes and knowledge asymmetry
├─ Narrative presentation
   ├─ narrator personification and POV grammar
   └─ deadpan humor, tragedy and narrator split
└─ Character identity
   └─ MC4 identity, dual biological/cognitive configurations and Academy membership

CHILD CURRENT-CANON DOMAIN
├─ Matriarch's Lament
│  ├─ puppet state / Temple / apocalyptic cult
│  ├─ Creed / Holy Guard / Trần Trúc Nha
│  ├─ Trinity Hexagon / relic economy
│  └─ ML–TE routes, covert operations and northeastern tribes
└─ Stable aviation / RF airspace
   ├─ AF institutional aviation capacity
   ├─ airspace sovereignty / ATC / aviation economy
   ├─ mixed airspace and operational separation
   └─ AF–RF mutual dependency and internal route leverage

SEPARATE TEMPORAL / CONTROL LAYERS
├─ Design history and reconsiderations
├─ Reconciliation and conflict provenance
└─ Open-issues routing
```

This is document containment, not a claim that every relation in the setting is parent–child. Ontology must preserve typed relations such as `THUỘC_VỀ`, `ÁP_DỤNG_CHO`, `ĐI_VÀO`, `ĐI_RA`, `QUẢN_TRỊ`, `TƯƠNG_TÁC_VỚI` and `DẪN_XUẤT_TỪ`.

## 3. Required semantic boundaries

```text
STATUS
≠ SOCIAL HIERARCHY / CIVIC STANDING
≠ CLASS
≠ JOB / LABOR REGIME
≠ UNDIE RANK / FUNCTIONAL ROLE
≠ CAREER RANK
≠ ZONE
≠ ECONOMIC VARIABLE
≠ ACCESS PROFILE
≠ BACKGROUND / PROVENANCE
```

- `Undie` is a class inside the Slave umbrella.
- `Undi` is the official uniform applied to Undie; it is not a legal status.
- `Undie rank` is the current term for Red/Scarlet/Pink/Gray/Purple/Hazel/White and expresses function, responsibility, agency and track.
- `Career Rank` remains a separate axis with Entry/Intermediate/Support/Advanced/Ultimate. Unqualified `rank` inside the Undie domain means Undie rank, not Career Rank.
- White remains Undie until the Citizen transition completes.
- Yellow is a temporary disciplinary status; wearing Undi does not establish full Undie-class membership.
- Civil, Criminal and POW must not be flattened into the Undie-rank graph.
- Genealogy explains origin but does not define current containment, authority or dependency.

## 4. Latest retcon decisions — 2026-09-09

- Visual reading order: `Hoa Nguyệt maiden → closer look → collar/identification ink/Undie rank → Undie`. This supersedes the older rule that the silhouette alone must identify Undie immediately.
- MC2 genealogy remains Raging Fire / Prince 9. MC2 does not gain Hoa Nguyệt origin from the new visual-design source.
- Mismatch with older snapshots is expected and must be resolved through explicit supersession rather than silent coexistence.

## 5. Meta-story consolidation — 2026-09-10

- `aetherfire_canon_story_line_v0_5_v1_0_overlap.md` controls causal timeline where older simplified models differ.
- Canon 1 is authored, Fictionize-realized and retained as a reference/causal ancestry; Canon 2 is the current live world-state.
- The two continuations share V0.5, differ in realization mode and later overlap causally; they are not independent universes or a state merge.
- Narrator personification and POV remain a sibling presentation domain. Narrator separation does not establish transfer or loss of the underlying esper abilities.
- The narrator source's clothing section is not imported. All Undi clothing and perception canon remains controlled by `30_UNDIE_SYSTEM_CURRENT.md`.

## 6. Regional retcon consolidation — 2026-09-11

- `matriarchs_lament_working_retcon_canon.md` controls Holy State → Matriarch's Lament, T.Gear → Transfusion EasterFire, Trinity Hexagon, Creed, Trần Trúc Nha, regional routes and the ML relic dependency.
- `Quad Night` and its four-member-state ontology are retired. Relations that depended on that alliance remain `UNKNOWN / ORPHANED` unless the regional source explicitly replaces them.
- The AF↔TE treaty is direct and does not transit through ML. The prior 100 km corridor and Academy-flank mapping are not automatically remapped.
- The former foreign-spy punitive Undie route is removed because it no longer fits the political-centric setting. Archived wording is provenance only; legal/status treatment of spies remains `UNKNOWN`, and Criminal Slave → Undie remains prohibited.
- Mother MC2's Raging Fire / Prince 9 genealogy remains current; her post-Quad-Night custodian is `UNKNOWN`.

## 7. Intentionally excluded source

- `aetherfire_chat_anti_drift.md` — explicitly excluded by user because it was revised in another chat.
- `modular_engine_concept_anti_drift_revised.md` — not imported. Its typed-relation discipline informed this index, but the generic reusable core remains independent from AetherFire canon.

## 8. RF, Academy and MC4 integration — 2026-09-15

- RF is a continental union of cultivation member states, not one kingdom. The Raging Fire lineage, the RF union, the strongest bloc/member polity of MC2's mother and Prince 9's lower-ranked member polity remain distinct nodes.
- MC2's mother is the **Trưởng công chúa** of the strongest RF bloc/member polity. Prince 9 belongs to a lower-ranked member polity. Current unnamed polity and academy names remain placeholders.
- The strongest bloc's secession strategy, Prince 9 succession manipulation, guarded RF–AF alliance and the AF noble lineage-exploitation agenda are current canon only in the bounded form stated in `10`.
- The Academy's six-year structure, five-person combat team, twelve competency blocks, daily training rhythm, multi-axis scholarship profile and concrete functional uniform direction are current canon. Exact hours, weights, thresholds and official names remain `UNKNOWN`.
- The former Academy-failure-to-Undie route is removed from current and reconsideration layers. Archived sources retain it only as byte-exact provenance; it must not be reactivated.
- MC4 is a current Academy actor with one continuous identity and two biological/cognitive configurations. Legacy mastery, Fusion, Spear mechanics, morphology and in-world cross-world origin are not imported.
- Trần Trúc Nha belongs to Matriarch's Lament in current canon. Her proposed summoned/cross-world origin and the other unconfirmed cross-world/cross-time candidates are `UNDER CONSTRUCTION / NOT CURRENT CANON`.
- `70_MATRIARCHS_LAMENT_CURRENT.md` is the authority for ML's internal domain. `10` retains only the global/cross-domain interface; this architecture split changes no lore status.

## 9. Stable aviation and RF airspace integration — 2026-09-17

- AF is the only currently confirmed actor with stable, scalable aviation infrastructure; this does not establish a universal or permanent monopoly on flight or aviation.
- RF cultivators, artifacts, formations and flying creatures may exceed AF aircraft in raw or exceptional capability. Individual flight capability remains distinct from mass scheduled aviation.
- Relevant RF/member-state authorities have incentives to retain airspace sovereignty, localize ATC/data/maintenance/manpower and domesticate dependency. Exact constitutional authority and current implementation remain `UNKNOWN`.
- The staged localization sequence is a strategic dependency-reduction pathway, not a confirmed chronology. Exact capacity/throughput remains `UNKNOWN`; no numerical flight volume is canonized.
- `80_STABLE_AVIATION_RF_AIRSPACE_CURRENT.md` controls the detailed domain. `10` retains only its global and geopolitical interface.

## 10. Rollback

Use Git revert/history to roll back the project package. `Source_Archive/` preserves the exact build inputs, so regeneration does not depend on files outside `AetherFire Project/`.
'@
Write-MarkdownOutput '00_AETHERFIRE_CONSOLIDATION_INDEX.md' $index

$mergedIntroThroughIdentity = Get-Range -Text $merged -Start '# AetherFire — Canon hợp nhất' -End '# 2. Genealogy và triết lý thiết kế'
$mergedState = Join-H1Sections -Text $merged -Headings @(
    '# 3. Premise đế quốc AetherFire',
    '# 4. Triều đại, kế vị và khủng hoảng chính trị',
    '# 5. Cấu trúc nhà nước đa cực'
)
$mergedGlobal = Get-Range -Text $merged -Start '# 20. Quốc tế' -End '# 27. Cross-reference siêu hư cấu'
$mergedIntroThroughIdentity = Apply-UndieRankTerminology $mergedIntroThroughIdentity
$mergedState = Apply-UndieRankTerminology $mergedState
$mergedGlobal = Apply-UndieRankTerminology $mergedGlobal

$mergedIntroThroughIdentity = Remove-RequiredRange -Text $mergedIntroThroughIdentity -Start '## J. Quad Night — liên minh bốn quốc gia, không phải một quốc gia đơn lẻ' -End "---`n`n# 0. Nguồn được hợp nhất" -Label 'retired Quad Night intro blocks'
$mergedGlobal = Remove-RequiredRange -Text $mergedGlobal -Start '## 20.0d Quad Night — alliance ontology và bốn member state' -End '## 20.1 Nhóm phản đối' -Label 'retired Quad Night international blocks'

$oldIntroCorridor = 'Phía phải/đông của AF có một **hành lang kiểm soát khoảng 100 km** nối sang Quad Night, với Holy State là cửa vào chính của chuỗi. Hành lang có nhánh chính với nhà nghỉ/dịch vụ; vùng xung quanh thường xảy ra cướp. Bên trong hành lang có các micro-polity/bộ tộc tự xưng chủ quyền dưới quyền/bảo hộ thuộc địa của AF, làm **buffer + trade relay + road security**. Một polity ở phần nối gần Quad Night chiếm khoảng 50 km còn lại; exact partition chi tiết chưa chốt.'
$newCorridorBoundary = 'Mô hình hành lang 100 km AF↔Quad Night và Holy State làm cửa vào đã bị retire cùng Quad Night. Exact map mới giữa AF, ML và TE giữ `UNKNOWN`; không tự remap các buffer/micro-polity cũ sang actor mới.'
$mergedIntroThroughIdentity = Replace-Required -Text $mergedIntroThroughIdentity -Old $oldIntroCorridor -New $newCorridorBoundary -Label 'retired intro corridor'

$oldGlobalCorridor = 'AF↔Quad Night có một **hành lang kiểm soát khoảng 100 km**, Holy State là cửa vào chính. Nhánh chính có nhà nghỉ/dịch vụ; vùng xung quanh thường xuyên có cướp. Bên trong hành lang có các micro-polity/bộ tộc tự nhận chủ quyền nhưng hoạt động như **thuộc địa/buffer dưới quyền AF**, đảm nhiệm giao thương và an ninh tuyến đường. Một polity ở phần nối gần Quad Night chiếm khoảng 50 km còn lại; exact partition không tự suy thêm.'
$mergedGlobal = Replace-Required -Text $mergedGlobal -Old $oldGlobalCorridor -New $newCorridorBoundary -Label 'retired international corridor'

$oldQueenIntro = 'Hoàng hậu hiện tại **đang bị Quad Night tạm giữ ở cấp liên minh**; địa điểm giam giữ có thể được luân phiên giữa các thành viên để chống gián điệp và giải cứu.'
$newQueenCustody = 'Quan hệ giam giữ cũ phụ thuộc Quad Night đã bị orphan. Current custodian của Hoàng hậu/mẹ MC2 giữ `UNKNOWN`; không tự chuyển bà sang ML hoặc TE.'
$mergedIntroThroughIdentity = Replace-Required -Text $mergedIntroThroughIdentity -Old $oldQueenIntro -New $newQueenCustody -Label 'queen custody in identity section'

$oldQueenState = 'Hoàng hậu hiện đang **bị Quad Night tạm giữ ở cấp liên minh**; nơi giam có thể được luân phiên giữa các thành viên khi cần để chống gián điệp và giải cứu.'
$mergedState = Replace-Required -Text $mergedState -Old $oldQueenState -New $newQueenCustody -Label 'queen custody in state section'

$oldAcademyFlank = 'Trong concept/canon gốc, site Đông Bắc được đặt **ngay sau sườn Quad Night**, theo hướng có thể chọc vào flank của liên minh; nếu phải tạo pressure thì T.Gear là phía phù hợp nhất vì môi trường mở. Bộ Ngoại giao AF cố hết sức che đậy site; Quad Night hoặc không biết nó tồn tại, hoặc biết quá ít để hiểu đúng bản chất. Exact current awareness của Quad Night giữ `UNKNOWN`.'
$newAcademyBoundary = 'Placement cũ của site Đông Bắc theo sườn Quad Night/T.Gear chỉ còn là design genealogy. Current relation giữa Học viện, ML, TE và các bộ tộc mẫu hệ phía đông bắc tuân theo regional retcon; exact full map giữ `UNKNOWN`.'
$mergedGlobal = Replace-Required -Text $mergedGlobal -Old $oldAcademyFlank -New $newAcademyBoundary -Label 'academy flank orphaning'

$mergedIntroThroughIdentity = Replace-Required -Text $mergedIntroThroughIdentity -Old 'long mạch, Holy State, Hoa Nguyệt' -New "long mạch, Matriarch's Lament, Hoa Nguyệt" -Label 'current pressure-node rename'

$oldStoryCustody = 'Hoàng hậu hiện bị **Quad Night** tạm giữ ở cấp liên minh; nơi giam có thể luân phiên giữa các member state.'
$storyOverlap = Replace-Required -Text $storyOverlap -Old $oldStoryCustody -New 'Quan hệ custody cũ dưới Quad Night đã bị orphan; current custodian của Hoàng hậu giữ `UNKNOWN`.' -Label 'story timeline queen custody'

$mergedIntroThroughIdentity = $mergedIntroThroughIdentity.Replace('hoàng tộc Raging Fire (RF) ở phía Nam', 'huyết hệ hoàng tộc Raging Fire bên trong liên hiệp RF ở phía Nam', [System.StringComparison]::Ordinal)
$mergedIntroThroughIdentity = $mergedIntroThroughIdentity.Replace('Hoàng tộc RF có một **trait ẩn**', 'Hoàng tộc mang huyết hệ Raging Fire có một **trait ẩn**', [System.StringComparison]::Ordinal)
$mergedIntroThroughIdentity = $mergedIntroThroughIdentity.Replace('Prince 9 của một hoàng gia chư hầu thuộc RF', 'Prince 9 của hoàng gia một quốc gia thành viên rank thấp hơn trong RF', [System.StringComparison]::Ordinal)
$mergedGlobal = $mergedGlobal.Replace('một hoàng gia chư hầu thuộc Raging Fire', 'hoàng gia một quốc gia thành viên rank thấp hơn trong RF', [System.StringComparison]::Ordinal)
$mergedGlobal = $mergedGlobal.Replace('vua hiện tại của RF', 'vua hiện tại của quốc gia thành viên nơi Prince 9 xuất thân', [System.StringComparison]::Ordinal)
$mergedGlobal = $mergedGlobal.Replace('lật vị vua hiện tại của quốc gia thành viên nơi Prince 9 xuất thân/đăng cơ', 'lật vị vua hiện tại của quốc gia thành viên nơi Prince 9 xuất thân và đăng cơ tại quốc gia đó', [System.StringComparison]::Ordinal)
$mergedGlobal = $mergedGlobal.Replace('Hoàng tộc RF có một trait ẩn', 'Hoàng tộc mang huyết hệ Raging Fire có một trait ẩn', [System.StringComparison]::Ordinal)
$mergedGlobal = $mergedGlobal.Replace('Hoàng gia Raging Fire **cố tình che giấu** quan hệ này để tránh khủng hoảng chính trị.', 'Genealogy này bị che giấu có chủ ý bên trong RF để tránh khủng hoảng chính trị; exact actor chịu trách nhiệm và phạm vi biết của từng khối giữ `UNKNOWN`.', [System.StringComparison]::Ordinal)
$storyOverlap = $storyOverlap.Replace('Prince 9 của một hoàng gia chư hầu RF', 'Prince 9 của hoàng gia một quốc gia thành viên rank thấp hơn trong RF', [System.StringComparison]::Ordinal)
$storyOverlap = $storyOverlap.Replace('RF cố tình che giấu relation này.', 'Relation này bị che giấu có chủ ý bên trong RF; exact responsible actor và knowledge distribution giữ `UNKNOWN`.', [System.StringComparison]::Ordinal)
$storyOverlap = $storyOverlap.Replace('MC2.2 lật vua RF hiện tại và lên ngôi', 'MC2.2 lật vị vua hiện tại của quốc gia thành viên nơi Prince 9 xuất thân và lên ngôi tại quốc gia đó', [System.StringComparison]::Ordinal)
$matriarchCurrent = $matriarchCurrent.Replace('→ Raging Fire tham gia', '→ một actor thuộc RF/Raging Fire tham gia; exact cấp lineage/liên hiệp/member-state giữ `UNKNOWN`', [System.StringComparison]::Ordinal)
$matriarchCurrent = $matriarchCurrent.Replace('├─ DEPENDS_ON Raging Fire', '├─ DEPENDS_ON RF arrangement / Raging Fire lineage', [System.StringComparison]::Ordinal)

$rfCurrentCanon = @'
## RF continental union, dynastic fault line and AF dependency — current canon 2026-09-15

### Ontology

RF is a **continental union of cultivation member states**, not one kingdom. Its exact constitutional form remains `UNKNOWN`; do not silently choose federation, confederation, tributary hierarchy or empire-of-states.

```text
Raging Fire lineage
≠ RF continental union
≠ strongest bloc/member polity of MC2's mother
≠ lower-ranked member polity of Prince 9
```

The four blocs currently foregrounded do not establish the full number of RF member states. Exact bloc-to-state containment remains `UNKNOWN`.

### Four foregrounded blocs

- The strongest bloc/member polity is the origin of MC2's mother, actively seeks secession, seeks AetherFire patronage and wants AF forced-magic technology to scale cultivation.
- Two other blocs oppose that secession and hold enough economic/political leverage that Prince 9's polity depends on both. They are not assumed to share identical institutions or motives.
- Prince 9's lower-ranked polity is the fourth foregrounded bloc and lies between the strongest secessionist bloc and the two opposing blocs.
- The former UK/Greenland/Alaska/Australia labels are design references only, never canon names.

### Prince 9 and MC2's mother

MC2's mother is the **Trưởng công chúa** of the strongest RF bloc/member polity. Prince 9 is the ninth prince of a lower-ranked RF member polity, her true husband and the biological father of MC2 and MC2.2.

```text
strongest bloc already seeks secession
→ manipulates the Crown Prince of Prince 9's polity
→ Crown Prince kills Prince 9 to consolidate power
→ strongest bloc uses the death of its Trưởng công chúa's husband
  as a grievance supporting secession
```

The relevant inner circle of the strongest bloc knows that the Trưởng công chúa's fetus is Prince 9's child. It sends the Trưởng công chúa and fetus to AetherFire for an alliance/patronage route, long-term dynastic leverage and a possible future-marriage route. That future marriage is an option, not a locked outcome, and does not erase MC2's agency.

Do not write “RF knew” for this information. Knowledge of pregnancy, father identity and the full operation differs among blocs and actors. The Trưởng công chúa's own knowledge of the manipulation remains `UNKNOWN`.

### Guarded RF–AetherFire alliance

The strongest bloc and AetherFire cooperate without mutual trust:

```text
strongest bloc wants AF technology
→ reduce its dependency on RF

AF wants access to RF lineage capability
→ reduce its dependency on RF
```

The other three foregrounded blocs deliberately raise distrust around that alliance. “Rare pure blood” is propaganda/framing, not proof of the true Raging Fire inheritance mechanism.

### AF noble agenda around MC2

After the AF king flees and the previous balance weakens, a noble faction pressures MC2 in an attempt to expose or exploit Raging Fire capability without knowing the true mechanics. Its confirmed goals are:

1. reduce or escape AF's dependency on RF;
2. research/extract enough capability to create an AF-controlled suppression array;
3. increase total military force-generation capacity.

This is a factional agenda, not proof of a unified state policy or a successful research program. It does not turn MC2's whole Princess → Civil → Undie trajectory into one master plan; MC2's Civil → Undie choice remains her own.

### Dependency boundary

AF's firewall and founding-seal history still depend on Raging Fire lineage/RF arrangements. The exact provider, contracting actor, maintenance authority and member-state allocation remain `UNKNOWN`; do not assign them automatically to the RF union or the strongest bloc.
'@

$aviationGlobalInterface = @'
## Stable aviation and RF airspace — global interface

> **Authority boundary:** `80_STABLE_AVIATION_RF_AIRSPACE_CURRENT.md` controls the detailed aviation, airspace, ATC, mixed-flight and route-leverage domain. This section keeps only the interfaces required by the wider world/geopolitics model.

- AF and RF are separated by an ocean where Seaborne make maritime transport extremely dangerous, so exchange depends strongly on aviation.
- AF is the only currently confirmed actor able to operate stable, scheduled and scalable aviation as infrastructure. This does not mean AF monopolizes flight or that no other actor can ever build comparable infrastructure.
- RF cultivators, artifacts, formations and flying creatures can possess exceptional flight or combat capability. Raw flight capability does not establish mass aviation capacity, and AF aviation does not establish automatic air supremacy.
- Direct AF↔RF member-state air routes can alter transit dependency, trade autonomy, diplomatic access and secession leverage.
- Relevant RF/member-state authorities have strategic incentives to retain airspace sovereignty, localize ATC and traffic data, and domesticate aviation dependency. Exact union/member-state/shared authority and current implementation remain `UNKNOWN`.
- AF carrier/engineering capacity and RF market/airspace/cultivation leverage produce bargaining and mutual dependency rather than automatic dominance by either side.
'@

$academyCurrentCanon = @'
## Battlemage Academy — current canon 2026-09-15

> **Official name:** `[ACADEMY NAME — PLACEHOLDER]`. “Học viện Lục Quang” is not canon.

### Institutional position

The Academy is an institution/faction within the northeastern Mage Council site behind a volcano. The site contains the Academy, a body-research lab using subjects from Elf, Beastman and Dragon powers, and a teleport gate linked to an isolated capital district containing elite forces. Exact Academy–branch–Council command authority remains `UNKNOWN`.

The cult is not part of the Academy. It exploits the apparent-POW-to-Mage-Council-specialist interface. Exact infiltration, Academy awareness and gate access remain `UNKNOWN`.

### Battlemage doctrine

The Academy trains genuine battlemages. Two schools are current:

1. martial-arts-based battlemage: body, martial arts and magic integrated into movement/close combat;
2. versatile magic plus multiple weapon families: situational tool-switching and adaptation without implying equal mastery of every weapon.

Training follows this competence order:

```text
self-control
→ self-preservation
→ independent reliability
→ teammate reliability
→ team operations
```

DI and consultant functions are separate. DI maintains combat/professional standards; consultants handle adolescent development and psychological readiness. Neither function replaces the other.

### Six-year model

1. Year 1 — control.
2. Year 2 — self-preservation and simple missions.
3. Year 3 — independent battlemage qualification.
4. Year 4 — team operations.
5. Year 5 — adaptive operations.
6. Year 6 — transition into professional personnel.

### Group structure

The standard combat team has **5 members** and is used only after the individual competence floor is met. Exact administrative cohort size, specialist-group size, dangerous-practice grouping, internal role allocation and activation threshold remain `UNKNOWN / NOT YET PROMOTED`; the approval of a five-person team does not canonize those adjacent working-design values.

### Twelve competency blocks

1. body control;
2. foundational martial arts;
3. magic control;
4. magical defense;
5. foundational weapons;
6. battlefield mobility;
7. battlefield awareness;
8. resource management;
9. medicine and incident response;
10. equipment and maintenance;
11. combat judgment;
12. team combat.

Exact distribution of the twelve blocks across terms and qualification gates remains `UNKNOWN`.

### Daily training rhythm

```text
physical block
→ applied magic / weapon / technical-theory block
→ long drill / lab / scenario block
→ self-study / maintenance / preparation
```

Exercises preserve the full cycle `briefing → preparation → execution → cleanup → after-action review`. Exact clock hours, weeks per year and holidays remain `UNKNOWN`.

### Funding and scholarship

The state funds part of training and all baseline meals. Students may take controlled commissions and side jobs. Full scholarship assessment uses a multi-axis profile:

- professional competence;
- progress;
- reliability;
- safety discipline;
- resource efficiency;
- team performance;
- mission performance.

Exact weights, thresholds, funding percentage, approving authority and external-work liability remain `UNKNOWN`. Supplement access may depend on `quality`, but `quality` remains a separate undefined variable and is not automatically rank, GPA, status, money, scholarship tier or morality score.

### Functional female battlemage uniform

The standard direction is:

- technical underlayer;
- short split jacket/tunic;
- leggings or technical trousers;
- optional hip-cover/outer shorts where function requires;
- forearm guards;
- knee/shin protection;
- equipment belt;
- combat boots;
- hair kept short, tied, braided or in a bun.

The two battlemage schools may differ in armor load, outer-layer length and equipment load. Protection, movement, spellcasting and equipment carriage control the design; sexual appeal is not a functional requirement. This Academy uniform is a separate domain and does not modify Undi clothing canon in `30_UNDIE_SYSTEM_CURRENT.md`.

### Lab boundary and removed route

Lab subjects may be used as live targets. Personhood, awareness, pain, consent/coercion, regeneration, death permanence, legal status, oversight and exact student protocol remain `UNKNOWN`; moral grayness is a design requirement, not permission to invent those facts.

```text
Academy failure → Undie = REMOVED FROM CURRENT SETTING
```

Academic failure does not create an automatic Undie transition. The former route is excluded from current canon and reconsideration layers.
'@
$matriarchGlobalInterface = @'
## Matriarch's Lament / Transfusion EasterFire — global interface

> **Authority boundary:** internal Matriarch's Lament governance, Temple/Cult/Creed, Holy Guard, Trinity/relic economy, Trần Trúc Nha doctrine, ML–TE operations and northeastern-tribe relations are controlled by `70_MATRIARCHS_LAMENT_CURRENT.md`. This section keeps only the interfaces needed by the wider AetherFire world model.

### Regional supersession and chronology

- `Quad Night` and its four-member-state ontology are retired.
- `Holy State` → `Matriarch's Lament (ML)`.
- `T.Gear` → `Transfusion EasterFire (TE)`.
- `Trinity Hexagon` is a district inside ML, not an independent state.
- ML is approximately 500 years old; AetherFire is approximately 200 years old.
- ML participated in the sealing event before AetherFire's foundation. An RF/Raging Fire actor also participated, but the exact lineage/union/member-state level remains `UNKNOWN`.

### AetherFire dependencies and treaty edge

```text
AF dependency on RF arrangement / Raging Fire lineage
≠
AF periodic dependency on ML relic access
```

ML controls access to a regenerative-consumable relic that AetherFire periodically needs to reinforce the seal. Political hostility and mandatory commerce may therefore coexist.

The AF↔TE treaty is direct and was negotiated inside AetherFire. It does not transit through ML.

### Orphaned geography and custody

The old 100 km AF↔Quad Night corridor, Academy-flank mapping and Quad-Night custody of MC2's mother are orphaned by the regional retcon. Current geometry and custodian remain `UNKNOWN`; they are not automatically reassigned to ML or TE.

### Trần Trúc Nha and Undie boundaries

Trần Trúc Nha's membership and regional role in ML are current canon. Her proposed summoned/cross-world origin is `UNDER CONSTRUCTION / NOT CURRENT CANON` and is routed to `40_METAFICTION_CANON_TIMELINE_CURRENT.md`.

The former `foreign spy / infiltrator → punitive Undie` route is `RESOLVED / REMOVED` because it no longer fits the political-centric setting. No replacement legal/status route is inferred; Undie-related interfaces are controlled by `30_UNDIE_SYSTEM_CURRENT.md`.
'@
$worldContent = @"
# AetherFire — World, Institutions & Geopolitics Current Canon

> Consolidated current-domain view. Detailed Citizen/Civil/Undie material was moved to sibling files. Design genealogy remains in ``90_DESIGN_HISTORY_AND_RECONSIDERATIONS.md``.  
> **Genealogy lock — 2026-09-09:** MC2 remains tied to Raging Fire / Prince 9; the Undi–Hoa Nguyệt visual retcon does not create Hoa Nguyệt ancestry or origin for MC2.
> Detailed Fiction 0/Fiction 1 and Canon 1/Canon 2 causality is routed to ``40_METAFICTION_CANON_TIMELINE_CURRENT.md``; narrator/POV presentation is routed to ``50_NARRATORS_POV_AND_HUMOR_CURRENT.md``.
> Detailed stable-aviation and RF-airspace canon is routed to ``80_STABLE_AVIATION_RF_AIRSPACE_CURRENT.md``.

$(Shift-MarkdownHeadings $mergedIntroThroughIdentity)

---

$(Shift-MarkdownHeadings $mergedState)

---

$(Shift-MarkdownHeadings $mergedGlobal)

---

$rfCurrentCanon

---

$aviationGlobalInterface

---

$academyCurrentCanon

---

$matriarchGlobalInterface

---

## Metafiction interfaces

- World-state facts established here feed the live Canon 2 context but do not by themselves define metafiction mechanics.
- ``40_METAFICTION_CANON_TIMELINE_CURRENT.md`` controls the fiction layers, continuation modes, causal overlap and clash timeline.
- ``50_NARRATORS_POV_AND_HUMOR_CURRENT.md`` controls narrator personification, POV grammar and humor design.
"@
Write-MarkdownOutput '10_WORLD_INSTITUTIONS_GEOPOLITICS_CURRENT.md' $worldContent

Write-MarkdownOutput '70_MATRIARCHS_LAMENT_CURRENT.md' $matriarchCurrent

Write-MarkdownOutput '80_STABLE_AVIATION_RF_AIRSPACE_CURRENT.md' $aviationCurrent

$statusRevamp = Join-H1Sections -Text $revamp -Headings @(
    '# 0. Nguyên tắc đọc',
    '# 1. Thứ bậc xã hội chính thức',
    '# 2. Civil → Undie là một chiều',
    '# 5. Yellow',
    '# 6. POW',
    '# 7. Civil Slave — Citizen-equivalent nhưng bị phân công',
    '# 8. Civil → Citizen',
    '# 14. Undie vi phạm pháp luật',
    '# 15. Criminal',
    '# 28. Bailout — correction',
    '# 29. Bia rượu',
    '# 32. Citizen career system',
    '# 33. Civil → Citizen có tax privilege',
    '# 34. Citizen → Civil → Citizen để hưởng policy',
    '# 35. Citizen → Undie',
    '# 36. Citizen có thể thất bại kinh tế',
    '# 37. Civil là fallback ổn định; Undie là fallback khác',
    '# 41. Civil được ưu đãi phí khi dùng Undie',
    '# 42. Không có homeless population ổn định',
    '# 42A. Disability và debt',
    '# 43. Core exploitation design — bản chốt',
    '# 44. Mobility graph hiện tại',
    '# 46. UNKNOWN bắt buộc giữ',
    '# 47. Bản nén anti-drift'
)
$ontologyCurrent = Apply-UndieRankTerminology $ontology
$statusRevamp = Apply-UndieRankTerminology $statusRevamp
$civilDelta = Join-H1Sections -Text $delta -Headings @(
    '# 1. Civil Slave — chức năng chiến lược',
    '# 2. Voluntary Civil Slave — background bị vô hiệu hóa về mặt vận hành'
)
$statusContent = @"
# AetherFire — Status, Civil & Labor Current Canon

> **Domain:** status ontology, social hierarchy, Citizen/Civil/Yellow/POW/Criminal, Civil entry/allocation/lifecycle, cross-status transitions and shared economic/access namespaces.  
> Dedicated Civil law controls its exact scope. The ontology map controls axis separation. Remaining gaps stay ``UNKNOWN / UNRESOLVED``.  
> **Terminology retcon — 2026-09-09:** within the Undie domain, unqualified ``rank`` means the Red/Scarlet/Pink/Gray/Purple/Hazel/White functional-role axis. ``Career Rank`` remains the separate Entry/Intermediate/Support/Advanced/Ultimate axis. Older source wording has been normalized to ``Undie rank`` in this derived current-canon file.

## Part I — Resolved status and ontology map

$(Shift-MarkdownHeadings -Text $ontologyCurrent -Levels 2)

---

## Part II — Civil entry and allocation law

$(Shift-MarkdownHeadings -Text $civil -Levels 2)

---

## Part III — Current cross-status and labor canon

> Imported once from the revamp anchor; Undie-specialized sections are located in the sibling Undie file.

$(Shift-MarkdownHeadings -Text $statusRevamp -Levels 2)

---

## Part IV — Civil strategic rationale and provenance boundary

$(Shift-MarkdownHeadings -Text $civilDelta -Levels 2)
"@
Write-MarkdownOutput '20_STATUS_CIVIL_LABOR_CURRENT.md' $statusContent

$mobilityPreamble = Get-Range -Text $undieMobility -Start '# AetherFire — Anti-Drift: Sex Worker System, Consent, Mobility, White' -End '# 1. ĐỊNH HƯỚNG CHUNG'
$mobilityHeadings = @()
foreach ($number in 1..29) {
    $match = [regex]::Match($undieMobility, "(?m)^# $number\. .+$")
    if (-not $match.Success) {
        throw "Missing Undie mobility section number: $number"
    }
    $mobilityHeadings += $match.Value
}
$mobilityHeadings += '# 31. CÁC UNKNOWN PHẢI GIỮ'
$mobilityCurrent = Join-H1Sections -Text $undieMobility -Headings $mobilityHeadings
$mobilityPreamble = Apply-UndieRankTerminology $mobilityPreamble
$mobilityCurrent = Apply-UndieRankTerminology $mobilityCurrent
$mobilityPreamble = Replace-Required -Text $mobilityPreamble -Old '| Criminal không thể vào Undie | CURRENT |' -New '| Criminal Slave không thể chuyển vào Undie | CURRENT; former foreign-spy punitive Undie route đã bị xóa và không tạo ngoại lệ |' -Label 'criminal table spy scope'
$mobilityCurrent = Replace-Required -Text $mobilityCurrent -Old 'Criminal có ontology và pipeline riêng.' -New @'
Criminal có ontology và pipeline riêng.

**Phạm vi sau quyết định 2026-09-16:** assertion này áp dụng cho subject đã được xác lập là `Criminal Slave`. Former foreign-spy punitive Undie route đã bị xóa vì không còn phù hợp với hướng political-centric của setting. Exact legal/status treatment của spy giữ `UNKNOWN`; không được tự suy spy đã đi qua Criminal pipeline, vào voluntary Undie hoặc mở Criminal Slave → Undie.
'@ -Label 'criminal section spy scope'

$spyPunitiveBoundary = @'
### Foreign-spy punitive Undie route — removed 2026-09-16

Nguồn gốc bị supersede: `matriarchs_lament_working_retcon_canon.md`.

```text
foreign spy / infiltrator
→ punitive Undie route
= REMOVED FROM CURRENT CANON AND RECONSIDERATION
```

Lý do ghi nhận: route này không còn phù hợp với hướng political-centric của setting. Việc xóa route không tự xác lập quy trình thay thế; legal classification, evidentiary/judicial handling và status outcome của spy giữ `UNKNOWN`. Không tự đồng nhất spy với `Criminal Slave`, voluntary Undie hoặc bất kỳ route hiện hành nào khác.
'@

$teTransferBoundary = @'
### AetherFire → Transfusion EasterFire Undie transfer — bounded interface

Current regional canon establishes only this event-level relation:

```text
AetherFire
→ transfers some Undie
→ to Transfusion EasterFire
→ to strengthen relations / friendship
```

The exact legal mechanism, consent process, selection criteria, status after transfer, and return/exit rights remain `UNKNOWN`. This statement does not establish sale, compulsory reassignment, voluntary migration, citizenship, or unchanged AetherFire status after transfer.
'@

$undieRevamp = Join-H1Sections -Text $revamp -Headings @(
    '# 3. Triệt sản Undie',
    '# 4. White → Citizen không đảo triệt sản',
    '# 9. Red / Pink workload',
    '# 10. Undi và Hoa Nguyệt',
    '# 11. Purple / Hazel',
    '# 12. Undie được ra khỏi phố đèn đỏ',
    '# 13. Premium summon / lane giao thông',
    '# 16. Shop và tín dụng nội bộ Undie',
    '# 17. Credit thường ≠ credit tín dụng',
    '# 18. Collar / terminal / retina / audio',
    '# 19. Pink mở liên lạc hai chiều',
    '# 20. Commission forum trên terminal',
    '# 21. Sensitive commission',
    '# 22. Hình ảnh nhà nước tiến bộ/dân chủ',
    '# 23. Khu ăn chơi',
    '# 24. Undie trong và ngoài khu ăn chơi — bắt buộc 1 vs 1',
    '# 25. Phân bố tầng lớp và sĩ quan',
    '# 26. Thành phố vệ tinh',
    '# 27. Undie là tài sản quốc gia',
    '# 30. Công quyền không được tùy tiện chặn Undie',
    '# 31. Payment hợp pháp',
    '# 38. Undie là “way out” cực đắt',
    '# 38A. Quyền thừa kế sau Citizen → Undie',
    '# 39. Gender intake và couple bonus',
    '# 40. Yellow genealogy và bonus “đã từng thử”',
    '# 45. Geographic deployment'
)
$undieDelta = Join-H1Sections -Text $delta -Headings @(
    '# 3. Sex Worker subsystem — van giải áp xã hội',
    '# 4. Framing thể loại của subsystem',
    '# 5. Tên chính thức của class: Undie',
    '# 6. Năm lớp nghĩa miệt thị của “Undie”',
    '# 7. Huấn luyện bắt buộc chấp nhận danh phận',
    '# 8. Không tự nhận Undie nội bộ, nhưng phải xác nhận khi giao tiếp bên ngoài',
    '# 9. Quyền sử dụng từ “Undie” là ngoại lệ class-specific',
    '# 10. Công quyền phải trung lập về thủ tục',
    '# 11. Thái độ xã hội đối với Undie là hỗn hợp',
    '# 12. Undie là class; phương thức hành nghề là biến riêng',
    '# 16. Mục tiêu chính trị của humiliation regime',
    '# 17. White và cạnh tranh',
    '# 18. Tiêu chuẩn thiết kế',
    '# 20. Latest anti-drift — Undie không phải global center'
)
$undieRevamp = Apply-UndieRankTerminology $undieRevamp
$undieDelta = Apply-UndieRankTerminology $undieDelta

$uniformBeforeRetcon = Join-H1Sections -Text $uniform -Headings @(
    '# 0. Anti-drift centrality — Undie sâu nhưng không phải trung tâm của AetherFire',
    '# 1. Quan hệ thuật ngữ',
    '# 2. Genealogy của đồng phục',
    '# 3. Bối cảnh thời trang Neo Fantasy',
    '# 4. Triết lý hình ảnh cốt lõi của Undi',
    '# 5. Nguyên mẫu Undi cơ sở',
    '# 6. Triết lý functional color/track'
)
$oldUniformReading = @'
Mục tiêu là tạo một mã xã hội:

```text
silhouette Hanfu/Yukata cách tân
→ liên tưởng nghề nghiệp ngoại lai
→ nhận ra Undie
→ sau đó mới đọc functional color/track và collar
```

Người nhìn phải có khả năng nhận ra **Undie trước khi đọc status trên vòng cổ**.
'@
$newUniformReading = @'
Mục tiêu hiện hành là tạo một chuỗi đọc hai lớp:

```text
silhouette thiếu nữ Hoa Nguyệt
→ tạo ấn tượng nữ tính ban đầu
→ người nhìn chú ý thêm
→ collar + mực định danh + Undie rank phá bố cục
→ nhận ra Undie ở cái nhìn thứ hai
```

Silhouette không còn phải tự nó làm người nhìn nhận ra Undie ngay lập tức. Latest visual retcon trong phần sau điều khiển public readability.
'@
$uniformBeforeRetcon = Replace-Required -Text $uniformBeforeRetcon -Old $oldUniformReading -New $newUniformReading -Label 'old immediate-Undie uniform reading order'
$uniformBeforeRetcon = Apply-UndieRankTerminology $uniformBeforeRetcon
$uniformBeforeRetcon = Replace-Required -Text $uniformBeforeRetcon -Old '- tự nhận diện class và Undie rank từ xa;' -New '- khiến class và Undie rank đọc được ở cái nhìn thứ hai qua apparatus;' -Label 'old distant class-and-rank recognition'
$uniformBeforeRetcon = Replace-Required -Text $uniformBeforeRetcon -Old '> nhìn tổng thể từ xa phải biết bộ đó thuộc Undie rank nào.' -New '> ở cái nhìn thứ hai, người nhìn phải đọc được Undie rank rõ mà không làm mất lớp thiếu nữ Hoa Nguyệt ở ấn tượng đầu.' -Label 'old distant rank recognition'

$uniformAfterRetcon = Join-H1Sections -Text $uniform -Headings @(
    '# 8. Tùy biến qua shop',
    '# 9. Chức năng xã hội của cá nhân hóa',
    '# 10. Undi như công cụ humiliation có hệ thống',
    '# 11. MC2 trước fall — váy công chúa',
    '# 12. MC2 sau fall — váy Undi',
    '# 13. Đối chiếu hình ảnh MC2 trước/sau fall',
    '# 14. Cặp triết lý hình ảnh',
    '# 15. Vì sao vẫn giữ “váy”',
    '# 16. Vì sao không dùng mini skirt / hở ngẫu nhiên',
    '# 17. Ranh giới thiết kế bắt buộc',
    '# 18. Bản nén chống drift',
    '# 19. UNKNOWN / Deferred'
)
$uniformAfterRetcon = Replace-Required -Text $uniformAfterRetcon -Old '- giữ silhouette Undie;' -New '- giữ silhouette thiếu nữ Hoa Nguyệt của Undi;' -Label 'old MC2 Undie silhouette wording'
$uniformAfterRetcon = Replace-Required -Text $uniformAfterRetcon -Old '| **Silhouette** | nghi lễ, hoàng gia, chiếm không gian | ngoại lai, Hanfu/Yukata cách tân, nhận diện Undie |' -New '| **Silhouette** | nghi lễ, hoàng gia, chiếm không gian | thiếu nữ Hoa Nguyệt; apparatus làm lộ Undie ở cái nhìn thứ hai |' -Label 'old immediate-read comparison row'
$uniformAfterRetcon = Apply-UndieRankTerminology $uniformAfterRetcon
$uniformAfterRetcon = Replace-Required -Text $uniformAfterRetcon -Old 'MÀU TỔNG THỂ PHẢI ĐỌC ĐƯỢC Undie rank TỪ XA.' -New 'Ở CÁI NHÌN THỨ HAI, MÀU TỔNG THỂ PHẢI ĐỌC ĐƯỢC UNDIE RANK MÀ KHÔNG PHÁ LỚP THIẾU NỮ BAN ĐẦU.' -Label 'old compressed distant-rank rule'

$newVisualHeadings = @()
foreach ($number in 1..30) {
    if ($number -eq 13) {
        continue
    }
    $match = [regex]::Match($undiHoaNguyet, "(?m)^# $number\. .+$")
    if (-not $match.Success) {
        throw "Missing Undi–Hoa Nguyệt section number: $number"
    }
    $newVisualHeadings += $match.Value
}
$newVisualCanon = Join-H1Sections -Text $undiHoaNguyet -Headings $newVisualHeadings

$newVisualCanon = Replace-Required -Text $newVisualCanon -Old @'
class trước
→ rank sau
→ cá nhân sau cùng
'@ -New @'
hình tượng thiếu nữ Hoa Nguyệt trước
→ apparatus làm lộ class ở cái nhìn thứ hai
→ rank sau
→ cá nhân sau cùng
'@ -Label 'new source wearer reading order'

$newVisualCanon = Replace-Required -Text $newVisualCanon -Old '> **nhìn tổng thể từ xa phải đọc được rank.**' -New '> **ở cái nhìn thứ hai, màu rank phải đọc được rõ mà không phá lớp đọc thiếu nữ ban đầu.**' -Label 'new source distant-rank instruction'
$newVisualCanon = Replace-Required -Text $newVisualCanon -Old '→ xã hội đọc class trước' -New '→ ở cái nhìn thứ hai, xã hội đọc class trước cá nhân' -Label 'new source MC2 second-look order'

$newVisualCanon = Replace-Required -Text $newVisualCanon -Old '# 14. MC2 — humiliation cá nhân hóa theo nguồn gốc' -New '# 14. MC2 — humiliation cá nhân hóa theo status fall, không theo nguồn gốc Hoa Nguyệt' -Label 'MC2 section heading'

$oldMc2Origin = @'
Với MC2, cơ chế này nặng hơn vì cô có nguồn gốc Hoa Nguyệt trong current story context.

Vì vậy váy Undi không chỉ có nghĩa:

```text
Princess
→ Undie
```

Mà còn:

```text
hình tượng nữ tính / văn hóa gần với nguồn gốc của cô
→ bị AetherFire tái mã hóa
→ thành đồng phục mại dâm
→ chính cô phải mặc
```

Do đó humiliation của MC2 có thể đồng thời chạm:

- địa vị;
- class;
- văn hóa;
- ký ức;
- căn tính;
- biểu tượng nữ tính;
- quan hệ chính trị.
'@
$newMc2Origin = @'
MC2 không có nguồn gốc Hoa Nguyệt trong current canon. Genealogy đã khóa của cô vẫn là Raging Fire / Prince 9.

Vì vậy váy Undi của MC2 có hai lớp nghĩa không phụ thuộc vào Hoa Nguyệt ancestry:

```text
Princess
→ Undie

biểu tượng nữ tính của quốc gia đối địch bị AetherFire chiếm dụng
→ thành đồng phục mại dâm
→ MC2 bị buộc phải mang apparatus và class-reading của hệ thống đó
```

Do đó humiliation của MC2 có thể đồng thời chạm:

- địa vị;
- class;
- biểu tượng nữ tính;
- cơ chế quản trị;
- quan hệ chính trị.
'@
$newVisualCanon = Replace-Required -Text $newVisualCanon -Old $oldMc2Origin -New $newMc2Origin -Label 'incorrect MC2 Hoa Nguyet origin'

$latestVisualPriority = @'
### Latest visual priority — 2026-09-09

The source `aetherfire_undi_hoa_nguyet_cultural_humiliation_design_philosophy.md` is imported here as the latest Undi visual canon/design intent with three explicit resolutions:

1. `Hoa Nguyệt maiden → closer look → apparatus → Undie` supersedes every older immediate-recognition rule.
2. MC2 remains Raging Fire / Prince 9; the candidate source's Hoa Nguyệt-origin statement was rejected as chat bias.
3. `Rank` is the current Undie-domain term for Red/Scarlet/Pink/Gray/Purple/Hazel/White; `Career Rank` remains separate.

Older material below is retained only for compatible construction, operation, customization and before/after visual facts. It cannot override these three resolutions.
'@
$undieContent = @"
# AetherFire — Undie System Current Canon

> **Domain:** Undie class identity, social function, intake, consent, work obligations, Undie ranks, mobility, Credit Score, White, economy/access, geographic deployment and Undi visual system.  
> ``Undie ≠ Undi``. Unqualified ``rank`` in this domain means Red/Scarlet/Pink/Gray/Purple/Hazel/White; ``Career Rank`` means Entry/Intermediate/Support/Advanced/Ultimate and remains separate. Older source terminology has been normalized to ``Undie rank`` in this derived current-canon file. Civil, Criminal, POW and Yellow remain separate axes/interfaces as defined in the sibling status file.

## Part I — Class identity, social purpose and institutional meaning

$(Shift-MarkdownHeadings -Text $undieDelta -Levels 2)

---

## Part II — Intake, consent, functional mobility and White

$(Shift-MarkdownHeadings -Text $mobilityPreamble -Levels 2)

$(Shift-MarkdownHeadings -Text $mobilityCurrent -Levels 2)

$spyPunitiveBoundary

$teTransferBoundary

---

## Part III — Work, economy, access, law and deployment

$(Shift-MarkdownHeadings -Text $undieRevamp -Levels 2)

---

## Part IV — Undi uniform, visual identity and MC2 visual fall

$latestVisualPriority

$(Shift-MarkdownHeadings -Text $uniformBeforeRetcon -Levels 2)

$(Shift-MarkdownHeadings -Text $uniformAfterRetcon -Levels 2)

---

### Latest cultural-humiliation and two-stage-perception canon

$(Shift-MarkdownHeadings -Text $newVisualCanon -Levels 2)
"@
Write-MarkdownOutput '30_UNDIE_SYSTEM_CURRENT.md' $undieContent

$fictionFoundation = Join-H1Sections -Text $fictionModel -Headings @(
    '# 1. Định nghĩa hai tầng',
    '# 2. MC1 trong Fiction 0',
    '# 3. MC3 trong Fiction 0',
    '# 4. Workflow sáng tác bình thường trước AetherFire',
    '# 13. Ma trận năng lực và miền tác dụng',
    '# 14. Các quan hệ bắt buộc tách riêng',
    '# 15. UNKNOWN'
)

$canonReference = Join-H1Sections -Text $canonComparison -Headings @(
    '# 7. Ma trận so sánh Canon 1 / Canon 2',
    '# 8. Ma trận mismatch khi MC1 xuất hiện',
    '# 9. Hai canon đều đúng nhưng không có quyền lực như nhau đối với hiện tại',
    '# 10. Quy tắc nhân quả bắt buộc',
    '# 11. Quan hệ MC1–MC3',
    '# 12. Các điểm chưa chốt'
)
$canonReference = $canonReference.Replace('một hoàng gia chư hầu thuộc RF', 'hoàng gia một quốc gia thành viên rank thấp hơn trong RF', [System.StringComparison]::Ordinal)
$canonReference = $canonReference.Replace('RF cố tình che giấu', 'genealogy bị che giấu có chủ ý bên trong RF; exact responsible actor giữ `UNKNOWN`', [System.StringComparison]::Ordinal)

$crossWorldBoundary = @'
## Part IV — Cross-world status boundary

### Confirmed

MC1 and MC3 are confirmed Fiction 0 → Fiction 1 cases. Raging Fire rebirth potential is a different mechanism: bearing the trait does not establish that MC2 or her mother has died and been reborn.

Trần Trúc Nha currently belongs to Matriarch's Lament and holds the role established in `70_MATRIARCHS_LAMENT_CURRENT.md`.

### Under construction / not current canon

```text
Trần Trúc Nha summoned from another world
= UNDER CONSTRUCTION / NOT CURRENT CANON
```

This origin is not current canon unless a later dedicated file is finalized and approved. Her current ML membership and regional role do not depend on that origin.

### Other unconfirmed cross-world/cross-time candidates

MC4, the undead west of Hoa Nguyệt, the sheep-man in the northern Beastman power, the painter, bard, time-traveling businessperson and political prisoner remain `UNDER CONSTRUCTION / NOT CURRENT CANON` as cross-world/cross-time candidates. They do not share a mechanism, cosmology, faction or mutual knowledge by default.
'@

$metaContent = @"
# AetherFire — Metafiction Canon & Timeline Current

> **Domain:** Fiction 0/Fiction 1, Fictionize, Proof of Concept, V0.5, Canon 1/Canon 2, Clash #1/Clash #2, realization mode, causal overlap and knowledge asymmetry.  
> **Priority:** ``aetherfire_canon_story_line_v0_5_v1_0_overlap.md`` controls the causal timeline. The fiction model controls layer/ability definitions where compatible; the Canon 1/Canon 2 source supplies comparison and mismatch matrices.  
> Older simplified descriptions of two independent parallel branches or MC1 being pulled directly from an external operator position are not imported. ``UNKNOWN`` mechanics remain unresolved.

## Part I — Fiction layers, actors and ability boundaries

$(Shift-MarkdownHeadings -Text $fictionFoundation -Levels 2)

---

## Part II — Controlling V0.5/V1.0 story line and causal overlap

$(Shift-MarkdownHeadings -Text $storyOverlap -Levels 2)

---

## Part III — Canon comparison, mismatch and authority boundaries

$(Shift-MarkdownHeadings -Text $canonReference -Levels 2)

---

$crossWorldBoundary
"@
Write-MarkdownOutput '40_METAFICTION_CANON_TIMELINE_CURRENT.md' $metaContent

$narratorCore = Join-H1Sections -Text $narrators -Headings @(
    '# 1. Nguồn gốc của “chúng tôi”',
    '# 2. Cấu trúc đại từ của tuyến Elena',
    '# 3. Vai trò của Fictionize trong cặp người kể chuyện',
    '# 4. Vai trò của Proof of Concept trong cặp người kể chuyện',
    '# 5. Proof of Concept là người tự sự đôi',
    '# 6. Cơ chế hài của cặp người kể chuyện',
    '# 7. Mẫu gag chuẩn — Elena ở ngã ba',
    '# 8. Elena là straight man của hệ gag'
)

$narratorStory = Join-H1Sections -Text $narrators -Headings @(
    '# 9. Fall from grace tự thân là một dark humor',
    '# 10. Dark humor của thể chế',
    '# 12. Dark humor của Canon 1 / Canon 2',
    '# 13. Clash #2 — “chúng tôi” bị tách làm đôi',
    '# 14. Vì sao POC + MC1 là một cặp bi kịch',
    '# 15. Vì sao Fictionize + Elena là một cặp bi kịch',
    '# 16. Đối xứng clash #1 / clash #2',
    '# 17. Không tự suy việc tách narrator = tách năng lực',
    '# 18. Joke khi POC gặp MC1 lần đầu'
)
$narratorStory = Replace-Required -Text $narratorStory -Old '→ rank / credits / facility / upkeep' -New '→ Undie rank / credits / facility / upkeep' -Label 'narrator institutional Undie-rank terminology'

$narratorLanguage = Join-H1Sections -Text $narrators -Headings @(
    '# 19. Hướng chuyển joke sang tiếng Anh',
    '# 20. “We” không đồng nghĩa consensus',
    '# 21. Sự im lặng như một phần của grammar hài và bi kịch',
    '# 22A. Lưu ý quan trọng — narrator nói thật nhưng Elena có thể đọc thành joke',
    '# 22. Đặc trưng narrator xuyên fiction',
    '# 23. Bản nén chống drift',
    '# 24. Các điểm chưa tự suy thêm'
)

$narratorContent = @"
# AetherFire — Narrators, POV & Deadpan Humor Current

> **Domain:** narrator personification, Elena POV grammar, Fictionize/POC narrative functions, deadpan humor, tragedy and the narrator split at Clash #2.  
> **Causal dependency:** ``40_METAFICTION_CANON_TIMELINE_CURRENT.md`` controls the clash and Canon 1/Canon 2 timeline. Narrator personification does not establish transfer or loss of the underlying esper ability.  
> **Clothing exclusion:** source section ``# 11. Dark humor của trang phục`` is deliberately not imported. This file does not restate or revive its older visual reading. All Undi clothing, rank-color and two-stage perception canon remains controlled exclusively by ``30_UNDIE_SYSTEM_CURRENT.md``.  
> Source labels such as ``CANON``, ``DESIGN INTENT`` and ``PROPOSAL / KHÔNG PHẢI CANON`` retain their original truth status.

## Part I — Narrator ontology, POV and comic grammar

$(Shift-MarkdownHeadings -Text $narratorCore -Levels 2)

---

## Part II — Fall, clashes and narrator separation

$(Shift-MarkdownHeadings -Text $narratorStory -Levels 2)

---

## Part III — Language, silence, anti-drift and unresolved mechanics

$(Shift-MarkdownHeadings -Text $narratorLanguage -Levels 2)
"@
Write-MarkdownOutput '50_NARRATORS_POV_AND_HUMOR_CURRENT.md' $narratorContent

$mc4Content = @'
# AetherFire — MC4 Identity Current Canon

> **Domain:** MC4 identity, biological/cognitive configurations, Academy membership and legacy-import boundaries.  
> **Genealogy:** derived from `The Tainted Cosmos - MERGED.md`; genealogy does not import its cosmology, power scale, artifacts or history.  
> **Institution boundary:** Academy doctrine is controlled by `10_WORLD_INSTITUTIONS_GEOPOLITICS_CURRENT.md`.

## 1. Current identity

MC4 is a current AetherFire character and belongs to the Battlemage Academy faction.

```text
MC4
= one person
+ one continuous self and consciousness
+ one memory stream
+ one responsibility stream
+ one core value system
+ two biological/cognitive configurations
```

A state change is not an identity change. The configurations share knowledge, memories, learned skills, muscle memory, values, responsibility and metacognition.

## 2. Biological trait

MC4 has a secret biological trait. MC4 is currently the only confirmed bearer in AetherFire; this wording does not prove no other bearer can exist.

The configurations differ in endocrine/cognitive information-processing priorities. The trait is biological rather than a learned spell. Exact interaction with medicine, poison, injury, fatigue, biological magic and AF medical technology remains `UNKNOWN`.

Who knows or can detect the secret—including family, Academy staff, medical staff, Mage Council and the lab—remains `UNKNOWN`.

## 3. Configuration profiles

Configuration A prioritizes analysis, planning, prediction, risk management, independence and preparation. Without setup time it retains skills but cannot exploit its natural preparation advantage.

Configuration B prioritizes execution, adaptation, improvisation, social processing and immediate action. Under stress it may spend resources too quickly and damage endurance/reserves.

Both remain the same accountable person.

## 4. Academy boundary

MC4 receives no exemption from Academy qualification because of protagonist status or biological rarity.

```text
unique biology
≠ combat mastery
≠ rank
≠ authority
≠ command
≠ scholarship
≠ lab access
```

Academy membership does not establish knowledge of the cult, geopolitics, the teleport gate or the lab. MC4–Lab, MC4–Cult, MC4–northern-powers and MC4–Mage-Council-authority relations remain `UNKNOWN / NOT ESTABLISHED` without a specific causal path.

## 5. Legacy quarantine

- Legacy professional mastery is not imported into teenage MC4.
- Legacy specializations may inform provenance but do not establish current certification or specialization.
- Fusion is not imported; its actual legacy effect is itself `UNKNOWN`.
- The old Spear of Restraint and its absolute anti-death/soul mechanics are not current canon.
- Physical sex/morphology across configurations is `UNKNOWN`.
- Trigger, direction, speed and control of switching are `UNKNOWN`.
- The official character name remains a placeholder.
- Authorial remake genealogy does not establish in-world cross-fiction provenance; MC4 as a cross-world actor remains `UNDER CONSTRUCTION / NOT CURRENT CANON`.

## 6. Visual boundary

MC4 follows the current functional Academy uniform standard. Legacy colors or visual tendencies may inform later personal accents only if they do not override protection, movement, spellcasting, equipment carriage or Academy standards.
'@
Write-MarkdownOutput '60_MC4_IDENTITY_CURRENT.md' $mc4Content

$historyCurrent = $history
$historyCurrent = Replace-Required -Text $historyCurrent -Old 'Mẹ MC2 thuộc **hoàng tộc Raging Fire ở phía Nam**.' -New 'Mẹ MC2 thuộc **huyết hệ hoàng tộc Raging Fire bên trong liên hiệp RF ở phía Nam**.' -Label 'history RF lineage versus union'
$historyCurrent = Replace-Required -Text $historyCurrent -Old 'Sau succession struggle ở RF:' -New 'Sau succession struggle tại quốc gia thành viên nơi Prince 9 xuất thân:' -Label 'history RF succession scope'
$historyCurrent = Replace-Required -Text $historyCurrent -Old 'Hoàng hậu hiện tại **đang bị Quad Night tạm giữ ở cấp liên minh**; nơi giam có thể được luân phiên giữa các member state để chống gián điệp/giải cứu.' -New 'Quan hệ giam giữ cũ phụ thuộc Quad Night đã bị orphan. Current custodian của Hoàng hậu/mẹ MC2 giữ `UNKNOWN`; không tự chuyển bà sang ML hoặc TE.' -Label 'history queen custody boundary'
$historyCurrent = Replace-Required -Text $historyCurrent -Old 'Hoàng tộc RF có một trait ẩn:' -New 'Hoàng tộc mang huyết hệ Raging Fire có một trait ẩn:' -Label 'history RF lineage trait'
$historyCurrent = Replace-Required -Text $historyCurrent -Old '## 25C.1 CURRENT CANON — AetherFire là seal-state khoảng 200 năm tuổi' -New '## 25C.1 PARTIALLY SUPERSEDED 2026-09-11 — AetherFire age survives; old east geometry retired' -Label 'history old east geometry status'
$historyCurrent = Replace-Required -Text $historyCurrent -Old @'
East/right
→ ~100 km controlled corridor
→ Holy State as main Quad Night entrance
'@ -New @'
East/right
→ old 100 km / Quad Night geometry is orphaned
→ exact current map between AF, ML and TE = UNKNOWN
'@ -Label 'history old east geometry body'
$historyCurrent = Replace-Required -Text $historyCurrent -Old '## 25C.2 CURRENT CANON — 100 km corridor và các buffer micro-polity' -New '## 25C.2 SUPERSEDED 2026-09-11 — 100 km corridor và các buffer micro-polity' -Label 'history old corridor status'
$historyCurrent = Replace-Required -Text $historyCurrent -Old @'
Ví dụ Y2 trong concept gốc được nhớ dưới node **Học viện Phép thuật / Hội đồng Pháp sư**:

```text
học viên tài năng
→ đào tạo / đánh giá
→ hữu dụng: trả về AF làm việc
→ failure: hạ xuống Undie nội bộ học viện
```

Vì vậy khi hỏi “Undie có gì?”, Y2 có thể không tự bật ra. Khi hỏi “Học viện xử lý học viên thất bại thế nào?”, pipeline mới hiện đầy đủ. Đây là **cách index trí nhớ**, không phải chi tiết nhỏ.
'@ -New @'
Học viện hiện được index dưới node **Hội đồng Pháp sư / site Đông Bắc / đào tạo battlemage / lab / teleport gate / grievance phía Bắc**. Đây là cách index institution/process-first phù hợp với hướng political-centric hiện tại.

Route cũ `Academy failure → Undie` đã bị người dùng xóa khỏi setting hiện hành và khỏi reconsideration layer. Nó không còn là fallback để giải thích cách Học viện xử lý học viên thất bại.
'@ -Label 'remove Academy failure to Undie memory example'
$historyCurrent = $historyCurrent.Replace('# 25B. Y — Mage Council Đông Bắc, human experimentation và institutional failure sink', '# 25B. Y — Mage Council Đông Bắc, human experimentation và political-security pressure', [System.StringComparison]::Ordinal)
$historyCurrent = Remove-RequiredRange -Text $historyCurrent -Start '## 25B.4 Y2 DESIGN HISTORY — academy tuyển civilian talent, useful output và Undie failure sink' -End '# 25C. Z / AA — Quad Night, strategic geography và Học viện như forward node' -Label 'remove Academy failure to Undie history and reconsideration'
$historyCurrent = $historyCurrent.Replace('một hoàng gia chư hầu thuộc Raging Fire', 'hoàng gia một quốc gia thành viên rank thấp hơn trong RF', [System.StringComparison]::Ordinal)
$historyCurrent = $historyCurrent.Replace('RF cố tình che giấu để tránh khủng hoảng chính trị', 'genealogy bị che giấu có chủ ý bên trong RF; exact responsible actor giữ `UNKNOWN`', [System.StringComparison]::Ordinal)
$historyCurrent = $historyCurrent.Replace('MC2.2 lật vua RF hiện tại/đăng cơ', 'MC2.2 lật vua của quốc gia thành viên nơi Prince 9 xuất thân/đăng cơ tại quốc gia đó', [System.StringComparison]::Ordinal)
$historyCurrent = Replace-Required -Text $historyCurrent -Old '## 25C.3 CURRENT CANON — Quad Night là alliance, Holy State chỉ là member/representative' -New '## 25C.3 SUPERSEDED 2026-09-11 — Quad Night alliance ontology' -Label 'history Quad Night status'
$historyCurrent = Replace-Required -Text $historyCurrent -Old '## 25C.4 CURRENT CANON — Queen custody là alliance-level rotating containment' -New '## 25C.4 SUPERSEDED 2026-09-11 — Queen custody under Quad Night' -Label 'history queen custody status'
$historyCurrent = Replace-Required -Text $historyCurrent -Old '## 25C.5 CURRENT CANON — T.Gear Undie treaty và Holy State covert interference' -New '## 25C.5 PARTIALLY SUPERSEDED 2026-09-11 — legacy treaty route and surviving covert pattern' -Label 'history treaty status'
$historyCurrent = Replace-Required -Text $historyCurrent -Old 'Việc phục hồi exact forced-Undie sanction sẽ cần một chốt canon riêng; trạng thái `UNDER CONSIDERATION` của R2 không tự sửa current Undie ontology.' -New 'Quyết định 2026-09-16 xóa toàn bộ foreign-spy punitive Undie route khỏi current canon và reconsideration vì nó không còn phù hợp với hướng political-centric của setting. Exact legal/status treatment thay thế cho spy giữ `UNKNOWN`; Criminal Slave → Undie vẫn bị cấm.' -Label 'history spy reconsideration removal'
$historyCurrent = Replace-Required -Text $historyCurrent -Old '**CURRENT-CANON CONFLICT:** legacy forced punitive transfer of infiltrators into Undie không tự tương thích với current voluntary/consent-based Undie ontology và **không được tự phục hồi**.' -New '**SUPERSEDED / REMOVED — 2026-09-16:** foreign spy / infiltrator không còn punitive Undie route riêng. Archived implementation là provenance-only; không được dùng làm fallback cho xử lý gián điệp.' -Label 'history spy conflict removal'
$historyCurrent = Replace-Required -Text $historyCurrent -Old '## 20.6 R2 — Holy State infiltration / T counteraction' -New '## 20.6 PROVENANCE ONLY — Holy State infiltration / T counteraction; punitive Undie endpoint removed' -Label 'history R2 provenance status'
$historyCurrent = Replace-Required -Text $historyCurrent -Old '### CURRENT-CANON COMPATIBILITY ISSUE' -New '### REMOVAL RECORD — 2026-09-16' -Label 'history R2 removal heading'
$historyCurrent = Replace-Required -Text $historyCurrent -Old 'Do đó nếu R2 được tái nhập:' -New 'Các function chính trị dưới đây chỉ được giữ để đọc design genealogy; chúng không phải đề xuất tái nhập R2 hoặc punitive Undie endpoint:' -Label 'history R2 no-reimport boundary'
$historyCurrent = Replace-Required -Text $historyCurrent -Old @'
## 20.6 PROVENANCE ONLY — Holy State infiltration / T counteraction; punitive Undie endpoint removed

**DESIGN HISTORY + UNDER CONSIDERATION**
'@ -New @'
## 20.6 PROVENANCE ONLY — Holy State infiltration / T counteraction; punitive Undie endpoint removed

**DESIGN HISTORY / PROVENANCE ONLY — punitive Undie endpoint removed 2026-09-16**
'@ -Label 'history R2 status no longer under consideration'

$historyCurrent = Replace-Required -Text $historyCurrent -Old '# 21. S — Hội đồng Pháp sư: contingency institution và technical-magical power center' -New @'
## 20.8 DESIGN HISTORY — học thuyết Thánh quốc cũ và nguồn tên Matriarch's Lament

**Lời kể lịch sử của người dùng, chưa phục hồi:** Thánh quốc thời RP cũ thờ Nữ thần Sự sống. Học thuyết của họ không công nhận lựa chọn tự nguyện bán dâm của phụ nữ là hợp lệ, nên diễn giải Undie như bằng chứng có cấu trúc ép buộc phía sau và nhiều lần tổ chức “giải cứu”. AetherFire xem các hành động đó là can thiệp vào nội bộ và chủ quyền. Đây là genealogy của tranh chấp tôn giáo, quyền lựa chọn và chủ quyền, không phải học thuyết được gán cho Matriarch's Lament hiện hành.

**Lời kể lịch sử của người dùng, chưa phục hồi:** `Matriarch's Lament` là tên từng có trong lore cũ. Bản cũ gắn tên này với một thánh nữ sáng lập: người xuyên thế giới cùng thế giới gốc với MC1 và MC3, esper có năng lực thanh tẩy cấp 7, về sau bị một tác nhân được gọi là AetherFire ám toán. Việc tên được dùng lại hiện nay không phục hồi tiểu sử hay sự kiện ám toán đó. Vị sáng lập này là một node riêng; **không đồng nhất với Trần Trúc Nha**.

**Chưa xác định:** thời điểm vị sáng lập sống, lập quốc và bị ám toán; tác nhân “AetherFire” là nhà nước hiện hành hay tiền thân; quan hệ giữa vụ ám toán với học thuyết chống Undie hoặc Total War cũ. Tuổi đời hiện hành của Matriarch's Lament và AetherFire không đủ để tự giải quyết niên đại này. Tuyến gián điệp nước ngoài → Undie trừng phạt ở §20.6 vẫn đã bị loại bỏ; lời kể về RP cũ không mở lại tuyến ấy.

Nguồn: `Source_Archive/aetherfire_rp_cu_ba_truc_lich_su_va_de_xuat.md`, mục 4; đây là bản thuật lại và phân tích, không phải biên bản RP độc lập.

# 21. S — Hội đồng Pháp sư: contingency institution và technical-magical power center
'@ -Label 'RP history Holy State and ML name'

$historyCurrent = Replace-Required -Text $historyCurrent -Old '## 23.2 DESIGN HISTORY — MC1 và MC3 lúc đó mới là proto-concepts' -New @'
## 23.1A DESIGN HISTORY — Undie ban đầu và lý do subsystem lan rộng

**Lời kể lịch sử của người dùng:** ở giai đoạn RP đầu, Undie được hình dung là mại dâm cao cấp với người tham gia về nguyên tắc tự nguyện, chưa phải nô lệ hay nô lệ tình dục. RP quanh dịch vụ này nhanh chóng lặp lại; câu hỏi thiết kế chuyển sang phản ứng của xã hội và thế giới, kéo theo luật, tiền công, điều kiện sống, chợ đen, thuế, du lịch, ngoại giao, tôn giáo và phản gián. Đây là giai đoạn thiết kế cũ, không phủ nhận các giai đoạn về sau đã viết Undie theo mô hình khác.

**Suy luận của bản tổng hợp RP:** vai trò làm điểm chạm cho nhiều miền có thể giải thích vì sao subsystem Undie trở nên dày hơn chức năng ban đầu. Đây là cách đọc genealogy, không phải nguyên nhân đã được kiểm chứng độc lập.

**Ranh giới hiện hành:** người dùng dự định thiết kế lại Undie cho cả Canon 1 và Canon 2 sau điểm tách nhánh V0.5, rồi chốt riêng. Ý định đó đang được cân nhắc; mục lịch sử này không sửa ontology, tình trạng pháp lý hay niên đại của hai canon.

Nguồn: `Source_Archive/aetherfire_rp_cu_ba_truc_lich_su_va_de_xuat.md`, mục 2–3; bản thuật lại, không phải biên bản RP độc lập.

## 23.2 DESIGN HISTORY — MC1 và MC3 lúc đó mới là proto-concepts
'@ -Label 'RP history earliest Undie'

$historyCurrent = Replace-Required -Text $historyCurrent -Old '# 24. V — Hoa Nguyệt / Tây quốc: đối trọng văn minh, dark foundation và hai triết lý phép thuật' -New @'
## 23.11 DESIGN HISTORY / INFERENCE / PROPOSAL — ba trục và vòng phản hồi RP cũ

**Lịch sử do người dùng kể, được bản tổng hợp sắp xếp thành ba trục:** (1) MC2 và đời sống Undie là camera RP trực tiếp; (2) bộ máy AetherFire phải giải thích, quản lý và phản ứng với hệ quả; (3) các nước ngoài phản ứng qua kinh tế, văn hóa, tôn giáo, tình báo và quân sự. Cách phân trục là công cụ phân tích, không phải sơ đồ thể chế canon.

**Suy luận:** một hành động của nhân vật đòi hỏi thể chế phản ứng; phản ứng đó tạo hệ quả quốc tế; sức ép quốc tế lại buộc thể chế thích nghi và tác động ngược lên nhân vật. Vòng lặp giúp giải thích vì sao các mắt xích cục bộ có thể hợp nhân quả dù điểm đầu và kết quả Total War nghe lệch tông. Nó không chứng minh mọi xung đột cũ đều bắt nguồn từ Undie hoặc bắt buộc dẫn tới chiến tranh.

**Đề xuất để cân nhắc:** nếu tái dùng genealogy, tách ngòi nổ RP khỏi nền lợi ích và điều kiện cho phép leo thang; giữ đường hạ nhiệt qua thương lượng, thông tin không đầy đủ, giới hạn thẩm quyền, chia rẽ nội bộ, chi phí chiến tranh và hậu cần. Tránh buộc mọi trục hội tụ vào một người hoặc một subsystem. Không đề xuất nào ở đây tự trở thành quy tắc canon.

Nguồn: `Source_Archive/aetherfire_rp_cu_ba_truc_lich_su_va_de_xuat.md`, mục 9–11, 16–17. Các mục về dead-heart và Total War đã có trong §23.8–23.10 nên không lặp lại.

# 24. V — Hoa Nguyệt / Tây quốc: đối trọng văn minh, dark foundation và hai triết lý phép thuật
'@ -Label 'RP history three-axis feedback'

$historyCurrent = Replace-Required -Text $historyCurrent -Old '# 25. W — Tam cường phương Bắc, long mạch và chiến tranh bị khóa bởi lợi ích tồn vong' -New @'
## 24.7 DESIGN HISTORY — dòng tiền, kế vị và bất đối xứng quân sự trong RP cũ

**Lời kể lịch sử của người dùng:** ma sát Hoa Nguyệt–AetherFire có từ thời chợ đen. Một bộ phận công dân Hoa Nguyệt lén sang AetherFire dùng dịch vụ Undie, tạo dòng người và tiền xuyên biên giới. AetherFire dùng nguồn thu này khi thiếu vốn; một số lãnh đạo Hoa Nguyệt thấy lợi ích kinh doanh và nhà nước cũng hưởng thuế liên quan. Chỉ trích về lương và điều kiện sống của Undie có thể đi cùng lợi ích kinh tế đó. Tính hợp pháp, cơ chế thuế và tỷ lệ thu chính xác vẫn chưa xác định.

**Lời kể lịch sử của người dùng:** một Thái tử Hoa Nguyệt bí mật sang AetherFire rồi đột tử; lý do công bố là “lao lực”. Sau đó AetherFire cáo buộc Thái tử kế nhiệm là con của tiên đế với người hầu, trái với phả hệ chính thức. Tính đúng sai và bằng chứng của cáo buộc chưa được xác nhận. **Suy luận:** khi một người kế vị chết trên đất AetherFire rồi nước này công kích chính danh người kế nhiệm, tranh chấp chuyển từ sự cố ngoại giao sang vấn đề kế vị; sự kiện đơn lẻ không đủ để suy ra chiến tranh tất yếu.

**Lời kể lịch sử của người dùng:** thế đối trọng cũ đặt khoa học–phép thuật AetherFire cạnh ưu thế đại trận của Hoa Nguyệt. Sau dead-heart, MC2/Raging Phoenix bị AetherFire khai thác như tài sản chiến lược, làm lệch tính toán sức mạnh trong RP cũ. Thời điểm chính xác và năng lực tác chiến không đủ rõ để ánh xạ vào canon hiện hành.

Nguồn: `Source_Archive/aetherfire_rp_cu_ba_truc_lich_su_va_de_xuat.md`, mục 5–8. Những quan hệ kinh tế, triều đại và quân sự này là genealogy; không cập nhật Hoa Nguyệt hay MC2 trong current canon.

# 25. W — Tam cường phương Bắc, long mạch và chiến tranh bị khóa bởi lợi ích tồn vong
'@ -Label 'RP history Hoa Nguyet economics succession and military'

$historyContent = @"
# AetherFire — Design History & Reconsiderations

> Preserved as a separate temporal layer. ``DESIGN HISTORY``, ``RETIRED``, ``SURVIVING LEGACY``, ``UNDER CONSIDERATION``, ``CURRENT CANON`` and ``UNKNOWN`` retain their original meanings. Nothing in this file becomes current canon merely because it appears here.

## Regional supersession notice — 2026-09-11

- Quad Night and the old four-member-state model are retired.
- Holy State → Matriarch's Lament; T.Gear → Transfusion EasterFire; Trinity Hexagon → district inside ML.
- Old Queen custody, 100 km corridor and Academy-flank relations are orphaned, not silently remapped.
- The AF↔TE treaty and covert-interference pattern survive only in the form stated by the new regional canon; the Holy-State transit chokepoint is retired.
- The former foreign-spy punitive Undie route is removed as a current or reconsideration candidate because it no longer fits the political-centric setting. Archived source and generated history references remain provenance/removal records only; replacement legal/status treatment remains ``UNKNOWN``.

## Latest source-state boundary — updated 2026-09-16

- Internal Matriarch's Lament current canon is routed to ``70_MATRIARCHS_LAMENT_CURRENT.md``. ``10`` now retains only its global/cross-domain interface; this is a document-authority split, not a lore retcon.
- RF single-kingdom wording is superseded by the continental-union/member-state ontology now recorded in ``10``.
- The former Academy-failure-to-Undie route is removed from both current canon and reconsideration. It survives only inside byte-preserved archived sources as provenance.
- The Academy's six-year model, five-person team, twelve competency blocks, daily rhythm, multi-axis scholarship profile and functional uniform direction are no longer working proposals; they are current canon in ``10``.
- MC4 legacy mastery, Fusion and Spear mechanics remain genealogy-only and are not current.
- Trần Trúc Nha's membership and regional role in Matriarch's Lament remain current. Her proposed summoned/cross-world origin, MC4's proposed in-world cross-fiction origin and the other unconfirmed cross-world/cross-time candidates are ``UNDER CONSTRUCTION / NOT CURRENT CANON``.
- The ``Nguyên Chủ / Nguyên Anh`` concept and the ``元主 / 元嬰`` wordplay remain proposal/design material. They are not assigned to MC2's mother by this integration.

## RP history import boundary — 2026-09-25

- The user-supplied RP-history synthesis is archived byte-exactly. Selected history, inference and proposals enter this file only; its claims have not been independently checked against the original RP transcript.
- A future Undie revamp for Canon 1 and Canon 2, after their V0.5 split, is being designed separately and has not been canonized by this import.

$(Shift-MarkdownHeadings $historyCurrent)
"@
Write-MarkdownOutput '90_DESIGN_HISTORY_AND_RECONSIDERATIONS.md' $historyContent

$reconciliationContent = @"
# AetherFire — Reconciliation Record

> Audit/control layer only. Part I summarizes the completed reconciliation. Part II preserves assertion-level conflicts, provenance, priority and resolutions.

## Stable aviation and RF airspace integration — 2026-09-17

1. **Source priority:** ``aetherfire_stable_aviation_rf_airspace_control_canon_delta_2026-09-16.md`` controls AF stable/scalable aviation, AF–RF aviation dependency, RF airspace/ATC/economy separation, mixed airspace and air-route leverage within its declared scope.
2. **Document authority:** ``80_STABLE_AVIATION_RF_AIRSPACE_CURRENT.md`` controls the detailed domain. ``10_WORLD_INSTITUTIONS_GEOPOLITICS_CURRENT.md`` retains only the global/geopolitical interface.
3. **AF-AV-001 — RESOLVED:** AF is the only currently confirmed actor with stable, scalable aviation infrastructure. This does not establish that AF owns all flight, that no other actor can ever possess comparable infrastructure, or that AF automatically has air supremacy.
4. **RF actor boundary:** statements about RF response are strategic incentives/direction for relevant RF/member-state authorities. Exact union/member-state/shared sovereignty and ATC authority remain ``UNKNOWN``; no unitary RF implementation is inferred.
5. **AF-AV-003 boundary:** the initial AF-supported stage followed by RF localization is a dependency-reduction pathway, not a confirmed chronology or current implementation state.
6. **AF-AV-004 — RESOLVED:** the source's illustrative ``thousands or tens of thousands`` flight volume is not imported because exact capacity/throughput remains ``UNKNOWN``. Current canon uses non-numeric mass/scheduled/scalable wording.
7. **Axis separation:** ``AIRSPACE SOVEREIGNTY ≠ AIR TRAFFIC CONTROL ≠ AVIATION ECONOMY``. Access, expertise or carrier service does not establish ownership or sovereign authority.
8. **Cross-project exclusion:** the source sentence about The Kingdom airspace is an anti-drift boundary for the source chat, not AetherFire lore and not a claim that changes The Kingdom canon.

## Matriarch's Lament follow-up decisions — 2026-09-16

1. **Trần Trúc Nha:** her membership and regional role in Matriarch's Lament are current canon.
2. **Cross-world construction boundary:** Trúc Nha's proposed summoned/cross-world origin, MC4's proposed in-world cross-fiction origin and the other unconfirmed cross-world/cross-time candidates are ``UNDER CONSTRUCTION / NOT CURRENT CANON``. This does not alter the already confirmed Fiction 0 → Fiction 1 status of MC1 and MC3.
3. **AF-ML-009 — RESOLVED / REMOVED:** the former foreign-spy punitive Undie route is deleted from current canon and reconsideration because it no longer fits the political-centric setting. Archived source wording remains provenance only and cannot reactivate the route.
4. **Post-removal boundary:** legal classification, evidentiary/judicial handling and status outcome for foreign spies remain ``UNKNOWN``. Removal does not map spies into ``Criminal Slave``, voluntary Undie or another existing status route; Criminal Slave → Undie remains prohibited.

## Matriarch's Lament document-authority integration — 2026-09-16

1. **Architecture only:** splitting the ML material is a document-authority refactor, not a change to canon truth values.
2. **Internal ML authority:** ``70_MATRIARCHS_LAMENT_CURRENT.md`` controls ML governance, Temple/Cult/Creed, Holy Guard, Trinity/relic economy, Trần Trúc Nha's regional role and doctrine, ML–TE routes/covert operations, and northeastern tribes.
3. **Global interface:** ``10_WORLD_INSTITUTIONS_GEOPOLITICS_CURRENT.md`` retains only the ML/TE facts required by the global AetherFire institutional and geopolitical model.
4. **Undie interface:** ``30_UNDIE_SYSTEM_CURRENT.md`` controls Undie status boundaries, including the removed foreign-spy route and the bounded AF→TE transfer statement.
5. **Cross-world interface:** ``40_METAFICTION_CANON_TIMELINE_CURRENT.md`` controls the ``UNDER CONSTRUCTION / NOT CURRENT CANON`` status of Trúc Nha's proposed cross-world origin.
6. **Source preservation:** ``matriarchs_lament_working_retcon_canon.md`` remains byte-exact in ``Source_Archive``; no source outside ``Temp`` was rewritten.

## RF, Academy and MC4 canon integration addendum — 2026-09-15

1. **RF ontology:** RF is now a continental union of cultivation member states, not one kingdom. ``Raging Fire lineage``, ``RF union``, the strongest bloc/member polity of MC2's mother and Prince 9's lower-ranked member polity are distinct nodes.
2. **Succession wording:** old ``vua RF`` and ``hoàng gia chư hầu RF`` wording is superseded. MC2.2's Canon 1 accession applies to the member polity where Prince 9 originated; official polity names and exact rank remain ``UNKNOWN``.
3. **Knowledge boundary:** do not write ``RF knows`` as a unitary actor. The strongest bloc's relevant inner circle knows the fetus's father; knowledge elsewhere and the Trưởng công chúa's own knowledge remain differentiated/``UNKNOWN``.
4. **RF–AF politics:** the strongest bloc's secession strategy, manipulation leading to Prince 9's death, guarded alliance with AF and three-bloc distrust campaign are current. Temporary real-world-inspired bloc labels are not canon names.
5. **MC2 exploitation:** after the AF king flees, an AF noble faction seeks to reduce RF dependency, reverse-engineer a suppression array and increase military force generation by pressuring/researching MC2's lineage. This is not proof of a unified state policy, known mechanism or successful program, and it does not erase MC2's Civil → Undie agency.
6. **Academy promotion:** the six-year model, five-person combat team, twelve competency blocks, daily training rhythm, multi-axis scholarship profile and concrete functional uniform direction are promoted from working design to current canon. Exact hours, weights, thresholds, official name and command chain remain ``UNKNOWN``; the Academy name uses a placeholder.
7. **Removed route:** ``Academy failure → Undie`` is deleted from current and reconsideration layers because it no longer fits the political-centric setting. Archived source bytes remain provenance only and cannot reactivate it.
8. **MC4:** MC4 is current, belongs to the Academy, is one continuous identity with two biological/cognitive configurations and is the only confirmed bearer of the secret trait. Legacy mastery, Fusion, Spear mechanics, morphology and in-world cross-world origin are not imported.
9. **Trần Trúc Nha:** membership and regional role in Matriarch's Lament remain current canon. Summoned/cross-world origin is ``UNDER CONSTRUCTION / NOT CURRENT CANON``.
10. **Open-issues control:** ``92_OPEN_ISSUES_CURRENT.md`` is restored as a generated control view and extended for RF, Academy, MC4 and cross-world boundaries. It is not a canon authority.
11. **Source priority:** RF geopolitics deltas are controlled by ``aetherfire_rf_crossworld_geopolitics_chat_consolidation_2026-09-15.md`` over overlapping older wording; ``aetherfire_rf_nguyen_chu_dynastic_power_axes_chat_consolidation.md`` controls the initial RF correction and preserves Nguyên Chủ/Nguyên Anh as proposal; the Academy and MC4 working files control their approved scopes.

## Metafiction consolidation addendum — 2026-09-10

1. **Causal timeline priority:** ``aetherfire_canon_story_line_v0_5_v1_0_overlap.md`` controls V0.5/V1.0, realization mode, pathway overlap and both clashes where older simplified descriptions differ.
2. **Canon 1 / Canon 2:** Canon 1 is authored and Fictionize-realized; Canon 2 is the current five-year live history. They share a V0.5 source, are not independent universes, do not merge world-states and later overlap at the MC1 summon point.
3. **MC1 entry:** MC1 is pulled while Fictionizing/stress-testing Canon 1 at the overlap, not directly from a purely external operator position.
4. **Narrator boundary:** the known narrator split is ``POC-personification → MC1`` and ``Fictionize-personification → Elena``. It does not establish transfer or loss of MC1/MC3's underlying esper abilities; exact Clash #2 mechanics remain ``UNKNOWN``.
5. **Clothing exclusion:** section ``# 11. Dark humor của trang phục`` from ``aetherfire_narrators_pov_clash_humor.md`` was deliberately not imported. ``30_UNDIE_SYSTEM_CURRENT.md`` remains the sole current authority for Undi clothing and the two-stage visual reading.

## Regional canon reconciliation addendum — 2026-09-11

1. **Source priority:** ``matriarchs_lament_working_retcon_canon.md`` controls its declared regional scope.
2. **Retired ontology:** Quad Night and its four-member-state graph are retired; old names remain only as aliases or design history.
3. **Current actors:** Holy State → Matriarch's Lament; T.Gear → Transfusion EasterFire; Trinity Hexagon is a district inside ML; northeastern matriarchal tribes remain separate actors under supply/protection relations.
4. **Treaty route:** AF↔TE is direct and negotiated inside AF. The former Holy-State transit chokepoint and Quad-Night security leverage are superseded. The covert-interference pattern remains current under ML↔TE.
5. **Queen custody:** Raging Fire / Prince 9 genealogy remains current. Post-Quad-Night custody is ``UNKNOWN`` and is not assigned to ML or TE.
6. **Spy boundary — superseded 2026-09-16:** the earlier regional integration briefly treated a foreign-spy punitive route as current. The later decision removes that route for political-setting fit; see the 2026-09-16 addendum. Criminal Slave → Undie remains prohibited.
7. **Map boundary:** the old 100 km corridor and Academy-flank relations are orphaned. No replacement geometry is inferred.
8. **Unchanged domains:** current Undi clothing/two-stage perception, Undie-rank terminology and metafiction authority remain unchanged.

## Latest reconciliation addendum — 2026-09-09

1. **Visual recognition order:** ``Hoa Nguyệt maiden → closer look → apparatus → Undie`` is latest canon and supersedes older ``silhouette → Undie immediately`` wording.
2. **MC2 genealogy:** remains Raging Fire / Prince 9. The statement that MC2 has Hoa Nguyệt origin was rejected as chat bias and is not imported.
3. **Rank namespace:** unqualified ``rank`` in the Undie domain means Red/Scarlet/Pink/Gray/Purple/Hazel/White. ``Career Rank`` remains Entry/Intermediate/Support/Advanced/Ultimate. Earlier wording ``functional color/track`` remains readable as a descriptive synonym, not a separate axis.
4. These decisions override incompatible statements retained in the older reconciliation snapshot below.

## Part I — Reconciliation summary

$(Shift-MarkdownHeadings -Text $report -Levels 2)

---

## Part II — Conflict register and evidence trail

$(Shift-MarkdownHeadings -Text $register -Levels 2)
"@
Write-MarkdownOutput '91_RECONCILIATION_RECORD.md' $reconciliationContent

$newOpenIssues = @'
## 5. RF, Academy, MC4 and cross-world open issues — updated 2026-09-16

| ID | Type / state | Open issue | Required baseline and dependency |
| --- | --- | --- | --- |
| AF-OPEN-016 | UNKNOWN / OPEN | Exact RF constitutional form and whether the four foregrounded blocs are member states, coalitions of member states or another internal layer. | `10`; `91` RF/Academy/MC4 addendum. Do not collapse bloc, state, union and lineage. |
| AF-OPEN-017 | UNKNOWN / OPEN | Exact RF actor that supplies, contracts, maintains or authorizes the Raging Fire firewall and founding-seal dependency. | `10`; do not assign automatically to the union or strongest bloc. |
| AF-OPEN-018 | UNKNOWN / OPEN | Official names/ranks of the mother-MC2 and Prince-9 polities, plus exact RF authority over succession and royal marriage. | `10` and `40`; old `vua RF` wording is superseded. |
| AF-OPEN-019 | UNKNOWN / OPEN | Trưởng công chúa knowledge, public murder narrative and exact chronology of Prince 9's death, pregnancy transfer, alliance and secession escalation. | `10`; knowledge must remain actor-specific. |
| AF-OPEN-020 | UNKNOWN / OPEN | Academy official name, command chain, exact map, student/staff scale, administrative/specialist/dangerous-practice group sizes, five-person-team role allocation and activation threshold, entry age, per-term curriculum gates and field-deployment authorization. | `10`; official name remains `[ACADEMY NAME — PLACEHOLDER]`; only the five-person standard itself is promoted. |
| AF-OPEN-021 | UNKNOWN / OPEN | Scholarship weights, thresholds, funding percentage, approving authority and external-work liability. | `10`; the seven-factor profile is canon, exact numeric formula is not supplied. |
| AF-OPEN-022 | UNKNOWN / OPEN | Definition of Academy `quality` and its exact relation to supplement access. | `10`; do not map it to rank, GPA, status, money, scholarship tier or morality. |
| AF-OPEN-023 | UNKNOWN / OPEN | Lab-subject personhood, awareness, pain, consent/coercion, regeneration, death permanence, legal status, oversight and live-target protocol. | `10`; intended moral grayness does not resolve these facts. |
| AF-OPEN-024 | UNKNOWN / OPEN | Current teleport-gate access and post-divergence sabotage/lab operational state. | `10` and `40`. |
| AF-OPEN-025 | UNKNOWN / OPEN | MC4 morphology, switching trigger/control, medical/magical interaction, official name and who knows/detects the secret. | `60`. |
| AF-OPEN-026 | UNKNOWN / OPEN | MC4 current specialization and any future import of Fusion, restraint philosophy or a redesigned Spear. | `60`; legacy mastery and absolute Spear mechanics are not current. |
| AF-OPEN-027 | UNDER CONSTRUCTION / NOT CURRENT CANON | Whether Trần Trúc Nha was summoned from another world. | `40`; her membership and regional role in ML remain canon, while the proposed cross-world origin is not current. |
| AF-OPEN-028 | UNDER CONSTRUCTION / NOT CURRENT CANON | Cross-world/cross-time status of MC4 and the other proposed outsiders, plus origin, mechanism, body/soul/memory transfer, return path and chronology. | `40` and `60`; no shared mechanism is established and none of these candidate origins is current canon. |
| AF-OPEN-029 | PROPOSAL / OPEN | Whether to canonize Nguyên Chủ/Nguyên Anh generally, adopt `元主 / 元嬰`, or assign the ontology/title to MC2's mother. | `90`; none of these three decisions is made by the RF retcon. |
| AF-OPEN-031 | CONFLICT / OPEN | Legacy label `khu nghiên cứu cơ thể người` coexists with canon Academy subjects listed as Elf, Beastman and Dragon. | `10`; decide whether this is a technical umbrella label or must be renamed to a species-neutral body-research term. Do not infer personhood from the label. |

## 6. Matriarch's Lament open interfaces — updated 2026-09-16

| ID | Type / state | Open issue | Required baseline and dependency |
| --- | --- | --- | --- |
| AF-ML-003 | UNKNOWN / OPEN | Whether ML's apocalyptic cult and the cult operating through the AF/Academy-side interface are the same organization, branches, affiliates, or merely share a label. | `70` and `10`; do not merge organizations from label overlap. |
| AF-ML-004 | UNKNOWN / OPEN | Exact relation between ML's central Temple and the religious/Temple network operating inside AetherFire. | `70`; influence and information flow are current, but branch/subordinate/affiliate status is not established. |
| AF-ML-005 | UNKNOWN / OPEN | Exact distinction and interaction among the three-clergy Creed quorum, the three priests witnessing relic loans, and activation/issuance of a Holy Guard oath. | `70`; shared number or personnel does not establish one procedure. |
| AF-ML-006 | UNKNOWN / OPEN | Exact relation between the plural relic catalogue and the singular regenerative-consumable seal relic, including seal target, renewal interval, custody, ownership, authority and cost. | `70` and `10`; periodic AF access is current, these mechanics are not. |
| AF-ML-007 | UNKNOWN / OPEN | Exact legal mechanism, consent, selection criteria, post-transfer status, and return/exit rights for the Undie transferred by AF to TE. | `30` and `70`; do not infer sale, compulsory reassignment, voluntary migration, citizenship, or unchanged AF status. |
| AF-ML-008 | UNKNOWN / OPEN | Status, rights, destination and legal recognition of Undie “freed on site” through ML covert interference. | `70` and `30`; liberation wording does not establish citizenship, custody, return or exit route. |
| AF-ML-010 | UNKNOWN / OPEN | Granularity of Saintess/Temple knowledge concerning leaks and covert activity. | `70`; institution-level awareness does not establish knowledge or authorization of every operative or operation. |

## 7. Stable aviation and RF airspace open issues — updated 2026-09-17

| ID | Type / state | Open issue | Required baseline and dependency |
| --- | --- | --- | --- |
| AF-AV-002 | UNKNOWN / OPEN | Exact actor holding airspace sovereignty, route-opening authority, ATC authority and military-flight authority: RF union, member-state, or shared structure. | `80`; depends on AF-OPEN-016. Do not treat RF as a unitary authority. |
| AF-AV-003 | UNKNOWN / OPEN | Current stage and achieved degree of RF domestic aviation, including crew, maintenance, spare-parts, ground operations, navigation and ATC localization. | `80`; the staged sequence is a strategic pathway, not confirmed chronology. |
| AF-AV-005 | UNKNOWN / OPEN | Exact aircraft technology/resources, altitude bands, capacity/throughput and route-network topology. | `80`; do not infer numerical traffic volume from scalable capability. |
| AF-AV-006 | UNKNOWN / OPEN | Airport ownership, cabotage law, customs/tax allocation and cross-member-state air-service authority. | `80`; carrier access does not establish domestic operating rights or sovereignty. |
| AF-AV-007 | UNKNOWN / OPEN | Exact identification, crossing, separation, restricted-zone, rescue, accident-investigation and military-control rules for mixed airspace. | `80`; the three airspace categories are current, their implementation is not supplied. |
| AF-AV-008 | UNKNOWN / OPEN | Exact flight/combat capabilities of each RF cultivation tradition, artifact, formation or flying creature. | `80`; exceptional capability must not be converted into a uniform RF-wide metric. |

## 8. Closed/superseded items from these integrations

| ID | State | Resolution |
| --- | --- | --- |
| AF-AV-001 | RESOLVED | AF is the only currently confirmed actor with stable, scalable aviation infrastructure; this is not a universal/permanent monopoly claim and does not negate other actors' flight capability. |
| AF-AV-004 | RESOLVED | No numeric flight volume is canonized. Exact capacity/throughput remains `UNKNOWN`; current wording is mass, scheduled and scalable operation. |
| AF-OPEN-030 | RESOLVED / REMOVED | `Academy failure → Undie` is not a current or reconsideration route. Archived occurrence is provenance only. |
| AF-ML-002 | RESOLVED | Trần Trúc Nha's ML membership and regional role are current canon; her proposed summoned/cross-world origin is `UNDER CONSTRUCTION / NOT CURRENT CANON`. |
| AF-OPEN-032 / AF-ML-009 | RESOLVED / REMOVED | `foreign spy / infiltrator → punitive Undie` is removed from current canon and reconsideration because it no longer fits the political-centric setting. Archived occurrence is provenance only; replacement legal/status handling remains `UNKNOWN`. |

## 9. Scope boundary
'@
$openIssuesContent = Replace-Required -Text $openIssuesSeed -Old '## 5. Scope boundary' -New $newOpenIssues -Label 'restore and extend open issues register'
$openIssuesContent = Replace-Required -Text $openIssuesContent -Old 'It does not replace local `UNKNOWN` sections inside `10`–`50`' -New 'It does not replace local `UNKNOWN` sections inside current-domain files `10`–`80`' -Label 'open-issues current-domain range'
Write-MarkdownOutput '92_OPEN_ISSUES_CURRENT.md' $openIssuesContent

$sourceHashes = Get-ChildItem -LiteralPath $sourceRoot -File -Filter '*.md' |
    Sort-Object Name |
    ForEach-Object {
        $hash = (Get-FileHash -LiteralPath $_.FullName -Algorithm SHA256).Hash
        "| ``$($_.Name)`` | ``$hash`` |"
    }

$generatedNames = @(
    '00_AETHERFIRE_CONSOLIDATION_INDEX.md',
    '10_WORLD_INSTITUTIONS_GEOPOLITICS_CURRENT.md',
    '20_STATUS_CIVIL_LABOR_CURRENT.md',
    '30_UNDIE_SYSTEM_CURRENT.md',
    '40_METAFICTION_CANON_TIMELINE_CURRENT.md',
    '50_NARRATORS_POV_AND_HUMOR_CURRENT.md',
    '60_MC4_IDENTITY_CURRENT.md',
    '70_MATRIARCHS_LAMENT_CURRENT.md',
    '80_STABLE_AVIATION_RF_AIRSPACE_CURRENT.md',
    '90_DESIGN_HISTORY_AND_RECONSIDERATIONS.md',
    '91_RECONCILIATION_RECORD.md',
    '92_OPEN_ISSUES_CURRENT.md'
)
$outputHashes = foreach ($name in $generatedNames) {
    $path = Join-Path $tempRoot $name
    $hash = (Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash
    "| ``$name`` | ``$hash`` |"
}

$manifest = @"
# AetherFire Consolidation Manifest

## Scope

- Generated canon files live at the ``AetherFire Project`` root.
- Exact original Markdown inputs are preserved under ``Source_Archive`` and are read but not modified by the build.
- ``aetherfire_chat_anti_drift.md`` was explicitly excluded.
- ``modular_engine_concept_anti_drift_revised.md`` was not imported.
- ``aetherfire_undi_hoa_nguyet_cultural_humiliation_design_philosophy.md`` was imported into the Undi visual domain with explicit reconciliation of recognition order, MC2 genealogy and rank namespace.
- ``aetherfire_fiction0_fiction1_model.md``, ``aetherfire_canon1_canon2.md`` and ``aetherfire_canon_story_line_v0_5_v1_0_overlap.md`` were consolidated into the metafiction/canon-timeline domain with the story-line source controlling causal conflicts.
- ``aetherfire_narrators_pov_clash_humor.md`` was consolidated into a separate narrator/POV domain. Its clothing section was explicitly excluded so it cannot override the latest Undi visual canon in ``30_UNDIE_SYSTEM_CURRENT.md``.
- ``matriarchs_lament_working_retcon_canon.md`` was imported as the controlling regional retcon. Its unmatched final source fence is repaired only in generated output; the archived source remains byte-preserved.
- ``70_MATRIARCHS_LAMENT_CURRENT.md`` controls the internal ML domain. ``10_WORLD_INSTITUTIONS_GEOPOLITICS_CURRENT.md`` retains only ML/TE global and cross-domain interfaces; this split is architectural and does not change lore status.
- ``aetherfire_stable_aviation_rf_airspace_control_canon_delta_2026-09-16.md`` was imported with explicit reconciliation of sole-confirmed versus literal-monopoly wording, non-numeric throughput, RF actor granularity and localization-pathway status.
- ``80_STABLE_AVIATION_RF_AIRSPACE_CURRENT.md`` controls the detailed stable-aviation/RF-airspace domain. ``10_WORLD_INSTITUTIONS_GEOPOLITICS_CURRENT.md`` retains only its global/geopolitical interface.
- The source sentence about The Kingdom airspace was excluded from generated AetherFire canon because it is a cross-project anti-drift boundary, not AetherFire lore or a The Kingdom canon decision.
- The four 2026-09-15 candidate files were archived byte-exactly and imported only according to the explicit user decisions recorded in ``91_RECONCILIATION_RECORD.md``.
- ``The Tainted Cosmos - MERGED.md`` is archived for MC4 identity genealogy; its cosmology, power scale, mastery, Fusion and Spear mechanics are not imported into current AetherFire canon.
- ``aetherfire_open_issues_current_restored_2026-09-15.md`` preserves the restored control file as a build seed. The generated ``92_OPEN_ISSUES_CURRENT.md`` extends it without granting it canon authority.
- The former Academy-failure-to-Undie route was removed from generated current/reconsideration layers and remains visible only in immutable archived provenance.
- The former foreign-spy punitive Undie route was removed as an active current/reconsideration candidate for political-setting fit. ``90``/``91`` retain only provenance and the removal log; no replacement legal/status route is inferred.
- The AF→TE transfer of some Undie is retained only as a bounded event. Legal mechanism, consent, selection, post-transfer status and return/exit rights remain ``UNKNOWN``.
- ``30_UNDIE_SYSTEM_CURRENT.md`` remains the sole authority for Undi clothing. The Academy combat uniform is a separate functional-uniform domain.
- Current canon, design history and audit provenance remain separate layers.
- ``aetherfire_rp_cu_ba_truc_lich_su_va_de_xuat.md`` is archived byte-exactly and curated into ``90`` as design history, inference and proposals only. It does not alter either Undie canon or restore the removed punitive spy route.
- Rollback uses Git history. ``Source_Archive`` keeps the package reproducible without parent-folder dependencies.

## Generated outputs

| File | SHA-256 |
| --- | --- |
$($outputHashes -join "`n")

## Archived source snapshot

| File | SHA-256 |
| --- | --- |
$($sourceHashes -join "`n")

## Build

From the repository root, run ``& '.\AetherFire Project\build_consolidation.ps1'`` to regenerate the package from its byte-preserved ``Source_Archive`` inputs.
"@
Write-MarkdownOutput 'MANIFEST.md' $manifest

Write-Output "Generated $($generatedNames.Count) consolidated Markdown files, plus manifest and build script, in self-contained project root $tempRoot"
