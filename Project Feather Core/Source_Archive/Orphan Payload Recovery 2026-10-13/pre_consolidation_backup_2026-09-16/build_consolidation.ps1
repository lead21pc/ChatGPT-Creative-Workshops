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
$report = Read-MarkdownSource 'aetherfire_reconciliation_report.md'
$register = Read-MarkdownSource 'aetherfire_conflict_register.md'
$fictionModel = Read-MarkdownSource 'aetherfire_fiction0_fiction1_model.md'
$canonComparison = Read-MarkdownSource 'aetherfire_canon1_canon2.md'
$storyOverlap = Read-MarkdownSource 'aetherfire_canon_story_line_v0_5_v1_0_overlap.md'
$narrators = Read-MarkdownSource 'aetherfire_narrators_pov_clash_humor.md'

$storyFenceCount = [regex]::Matches($storyOverlap, '(?m)^```').Count
if (($storyFenceCount % 2) -ne 0) {
    $storyOverlap = Replace-Required -Text $storyOverlap -Old "ENDING EXISTS`n≠`nEXACT CANON-1 IMPLEMENTATION IS GUARANTEED." -New ("ENDING EXISTS`n≠`nEXACT CANON-1 IMPLEMENTATION IS GUARANTEED.`n" + '```') -Label 'story-overlap final code fence'
}

$index = @'
# AetherFire — Consolidation Index

> **Generated consolidation baseline:** 2026-09-08; latest integration: 2026-09-12  
> **Location:** self-contained `AetherFire Project/` package. Canon outputs live at the project root; immutable build inputs are preserved under `Source_Archive/`.  
> **Truth rule:** `ABSENCE OF CANON ≠ CANONICAL NEGATION`; `NOT ESTABLISHED ≠ FALSE`; unresolved relations remain `UNKNOWN / UNRESOLVED`.

## 1. Required source-load order

After opening this index, read in this order:

1. `92_OPEN_ISSUES_CURRENT.md` — compact routing register for material `OPEN / UNKNOWN / DEFERRED / CONFLICTED` items.
2. Relevant current-domain files:
   - `10_WORLD_INSTITUTIONS_GEOPOLITICS_CURRENT.md` — project identity, state, institutions, geopolitics and dynastic conflict.
   - `20_STATUS_CIVIL_LABOR_CURRENT.md` — status ontology, Citizen/Civil/Yellow/POW/Criminal, Civil entry/allocation/lifecycle and cross-status mobility.
   - `30_UNDIE_SYSTEM_CURRENT.md` — Undie identity, intake, consent, Undie ranks, mobility, White, work/economy/access and Undi visual system.
   - `40_METAFICTION_CANON_TIMELINE_CURRENT.md` — Fiction 0/Fiction 1, Fictionize/POC, V0.5, Canon 1/Canon 2, both clashes, causal overlap and knowledge asymmetry.
   - `50_NARRATORS_POV_AND_HUMOR_CURRENT.md` — narrator personification, Elena POV, deadpan humor and the narrator split at Clash #2.
3. Relevant entries in `91_RECONCILIATION_RECORD.md` when an open item, conflict, supersession or provenance trail needs full evidence.
4. `90_DESIGN_HISTORY_AND_RECONSIDERATIONS.md` when genealogy, retired design or reconsideration is in scope; it is not a current world bible.
5. Newly supplied sources, which remain unconfirmed until the user accepts them.

Read order is not authority order. The open-issues file constrains reasoning but does not outrank current confirmed canon.

## 2. Document architecture

```text
AETHERFIRE CURRENT CANON
├─ World / institutions / geopolitics
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
└─ Narrative presentation
   ├─ narrator personification and POV grammar
   └─ deadpan humor, tragedy and narrator split

SEPARATE TEMPORAL / CONTROL LAYERS
├─ Design history and reconsiderations
└─ Reconciliation and conflict provenance
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

## 6. Intentionally excluded source

- `aetherfire_chat_anti_drift.md` — explicitly excluded by user because it was revised in another chat.
- `modular_engine_concept_anti_drift_revised.md` — not imported. Its typed-relation discipline informed this index, but the generic reusable core remains independent from AetherFire canon.

## 7. Old-canon quarantine

Old, excluded, retired, rejected and `SUPERSEDED` sources are provenance/comparison evidence only. They must not become the current baseline, fallback, analogy anchor, default, or gap filler. Current silence or missing retrieval does not reactivate them. Only an explicit current user confirmation can restore a former claim, and restoring one claim does not restore its old dependency tree.

## 8. Rollback

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
$worldContent = @"
# AetherFire — World, Institutions & Geopolitics Current Canon

> Consolidated current-domain view. Detailed Citizen/Civil/Undie material was moved to sibling files. Design genealogy remains in ``90_DESIGN_HISTORY_AND_RECONSIDERATIONS.md``.  
> **Genealogy lock — 2026-09-09:** MC2 remains tied to Raging Fire / Prince 9; the Undi–Hoa Nguyệt visual retcon does not create Hoa Nguyệt ancestry or origin for MC2.
> Detailed Fiction 0/Fiction 1 and Canon 1/Canon 2 causality is routed to ``40_METAFICTION_CANON_TIMELINE_CURRENT.md``; narrator/POV presentation is routed to ``50_NARRATORS_POV_AND_HUMOR_CURRENT.md``.

$(Shift-MarkdownHeadings $mergedIntroThroughIdentity)

---

$(Shift-MarkdownHeadings $mergedState)

---

$(Shift-MarkdownHeadings $mergedGlobal)

---

## Metafiction interfaces

- World-state facts established here feed the live Canon 2 context but do not by themselves define metafiction mechanics.
- ``40_METAFICTION_CANON_TIMELINE_CURRENT.md`` controls the fiction layers, continuation modes, causal overlap and clash timeline.
- ``50_NARRATORS_POV_AND_HUMOR_CURRENT.md`` controls narrator personification, POV grammar and humor design.
"@
Write-MarkdownOutput '10_WORLD_INSTITUTIONS_GEOPOLITICS_CURRENT.md' $worldContent

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

$historyContent = @"
# AetherFire — Design History & Reconsiderations

> Preserved as a separate temporal layer. ``DESIGN HISTORY``, ``RETIRED``, ``SURVIVING LEGACY``, ``UNDER CONSIDERATION``, ``CURRENT CANON`` and ``UNKNOWN`` retain their original meanings. Nothing in this file becomes current canon merely because it appears here.

$(Shift-MarkdownHeadings $history)
"@
Write-MarkdownOutput '90_DESIGN_HISTORY_AND_RECONSIDERATIONS.md' $historyContent

$reconciliationContent = @"
# AetherFire — Reconciliation Record

> Audit/control layer only. Part I summarizes the completed reconciliation. Part II preserves assertion-level conflicts, provenance, priority and resolutions.

## Metafiction consolidation addendum — 2026-09-10

1. **Causal timeline priority:** ``aetherfire_canon_story_line_v0_5_v1_0_overlap.md`` controls V0.5/V1.0, realization mode, pathway overlap and both clashes where older simplified descriptions differ.
2. **Canon 1 / Canon 2:** Canon 1 is authored and Fictionize-realized; Canon 2 is the current five-year live history. They share a V0.5 source, are not independent universes, do not merge world-states and later overlap at the MC1 summon point.
3. **MC1 entry:** MC1 is pulled while Fictionizing/stress-testing Canon 1 at the overlap, not directly from a purely external operator position.
4. **Narrator boundary:** the known narrator split is ``POC-personification → MC1`` and ``Fictionize-personification → Elena``. It does not establish transfer or loss of MC1/MC3's underlying esper abilities; exact Clash #2 mechanics remain ``UNKNOWN``.
5. **Clothing exclusion:** section ``# 11. Dark humor của trang phục`` from ``aetherfire_narrators_pov_clash_humor.md`` was deliberately not imported. ``30_UNDIE_SYSTEM_CURRENT.md`` remains the sole current authority for Undi clothing and the two-stage visual reading.

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

$openIssuesContent = @'
# AetherFire — Open Issues Current

> **Generated control view:** compact routing layer derived from the active reconciliation record; not a world-bible source and not authority to resolve its own entries.  
> **Use:** read after `00_AETHERFIRE_CONSOLIDATION_INDEX.md` and before relevant current canon, new sources, or substantive prompt execution.  
> **Truth rule:** `UNKNOWN / NOT ESTABLISHED` is neither `FALSE` nor permission to invent.

## 1. Processing rule

This register is read first to expose unstable premises. Read order is not authority order. For every touched item, open the named current-domain file; before reading a new source, open the cited section of `91_RECONCILIATION_RECORD.md` when provenance or conflict reasoning matters.

A newly supplied source remains `UNCONFIRMED` until explicit user acceptance. Compare it with both the current baseline and every affected entry here. Do not silently close, overwrite or fill an open item.

## 2. Old-canon quarantine

Old, legacy, excluded, retired, rejected and `SUPERSEDED` material is provenance/comparison evidence only. Never use it as a baseline, fallback, analogy anchor, default answer, missing bridge, mapping, transition or mechanism.

```text
CURRENT SILENCE ≠ OLD CANON REACTIVATED
MISSING RETRIEVAL ≠ PERMISSION TO FALL BACK
FORMER BASELINE ≠ PRESENT REFERENCE POINT
```

Only explicit current user confirmation can restore an old claim. Restoring one claim does not restore its former dependency tree.

## 3. Requires user resolution

| ID | Type / state | Open issue | Required baseline and dependency |
| --- | --- | --- | --- |
| AF-OPEN-001 | CONFLICT / OPEN | Whether the older Criminal labor catalogue (`metallurgy / construction / human-operated factory`) survives beside the newer dirty/dangerous-work definition. | Read `20`; full evidence: `91` AF-CX-017. Do not merge the lists silently. |
| AF-OPEN-002 | UNKNOWN / OPEN | Whether a distinct penal class named Brown exists outside the affected current sources. | Read `20` and `30`; full evidence: `91` AF-CX-003/004. Current confirmed Brown use is Civil jumpsuit color; this does not prove a separate penal Brown exists or does not exist. |
| AF-OPEN-003 | UNKNOWN / OPEN | Whether Temp-Y is currently operating and, if so, its law, duration and interface. | Read `20`; full evidence: `91` AF-CX-002. Do not merge Temp-Y with disciplinary Yellow. |
| AF-OPEN-004 | UNKNOWN / OPEN | Whether Yellow repeat offense occurs only after return to Citizen or can occur during the Yellow week. | Read `20`; full evidence: `91` AF-CX-001. Current destination is Red/Undie, not Brown. |
| AF-OPEN-005 | UNKNOWN / OPEN | Exact crosswalk or compatibility, if any, between Undie ranks and Career Rank. | Read `20` and `30`; full evidence: `91` AF-CX-005. Distinct axes do not prove mapping, non-mapping or compatibility. |
| AF-OPEN-006 | UNKNOWN / OPEN | Exact variable behind bare `credit` uses: terminal display, Pink contact cost, two +50% bonuses and uniform customization unlock. | Read `20` and `30`; full evidence: `91` AF-CX-007/008/009. Do not collapse Credits, Credit Score, Contribution Points or Credit Line. |

## 4. Intentionally unknown implementation details

| ID | State | Unknown | Required baseline and dependency |
| --- | --- | --- | --- |
| AF-OPEN-007 | UNKNOWN | Civil unilateral right to quit after conversion. | `20`; `91` AF-CX-011. |
| AF-OPEN-008 | UNKNOWN | Full Civil employer powers, liability and public-service access matrix. | `20`; `91` AF-CX-014. Receiving/demand authority is not allocation authority. |
| AF-OPEN-009 | UNKNOWN | Civil-specific marriage rule and any resident-status pathway. | `20`; `91` AF-CX-014. Absence of a rule in reviewed sources is not canonical negation. |
| AF-OPEN-010 | UNKNOWN | Exact year-5 review criteria, authority and exceptions. | `20`; `91` AF-CX-013. The current 5/10-year lifecycle does not supply these details. |
| AF-OPEN-011 | UNKNOWN | Exact relocation reimbursement, housing, reassignment duration and geographic limits after Civil conversion. | `20`; `91` AF-CX-012/014. |
| AF-OPEN-012 | UNKNOWN | Full Criminal rights, mobility and labor matrix. | `20`; `91` AF-CX-004/017. Do not revive Brown-to-Black mobility. |
| AF-OPEN-013 | UNKNOWN | Full Undie-rank graph, Career Rank rules, Credit Score thresholds and Contribution Points formulas. | `20` and `30`; `91` AF-CX-005/007. |
| AF-OPEN-014 | UNKNOWN | Full Credit Line underwriting, valuation, debt accounting and dispute/exit procedure. | `30`; `91` AF-CX-008/009. |
| AF-OPEN-015 | UNKNOWN | Exact Clash #2 mechanics beyond the confirmed narrator split and ability-boundary statements. | `40` and `50`; `91` Metafiction consolidation addendum. Do not infer ability transfer or loss from narrator separation. |

## 5. Scope boundary

This compact register carries the material open items recorded by the current reconciliation layer. It does not replace local `UNKNOWN` sections inside `10`–`50`, and it is not proof that no other unknown exists. When a domain file exposes another relevant unknown, preserve it and route to the full reconciliation record if provenance is needed.
'@
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
- Current canon, design history and audit provenance remain separate layers.
- ``92_OPEN_ISSUES_CURRENT.md`` is a generated routing/control view; it does not resolve issues or become canon evidence.
- Old or ``SUPERSEDED`` canon is comparison/provenance evidence only and cannot become a fallback baseline when current canon is silent or unavailable.
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
