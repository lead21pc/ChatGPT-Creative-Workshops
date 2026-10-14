# AetherFire — audit và triển khai cold storage

Ngày: 2026-10-02. Repository baseline: `98d563a4b638018b10621d094b2a54ae51f62810`.

## Kết luận và evidence boundary

Một package duy nhất chứa 91, 90 và năm overlay hiện hành. Bảy payload có tổng 254.830 byte; package hoàn chỉnh có 261.454 byte. Tách source identity khỏi vị trí lưu; không đổi canon, ontology, các priority addendum hoặc overlay body.

Kho GitHub đã được đọc trực tiếp qua connector ở SHA cố định, không dùng search excerpts làm bằng chứng source read. Clone bị lỗi kết nối proxy; workspace là snapshot các đường dẫn liên quan, không phải full git clone. Đã kiểm tra nội dung, metadata, cấu trúc section, reference và control gates; không suy chức năng từ filename. Audit về storage/routing không chứng nhận lại mọi lore assertion. `SOURCE_STORAGE_INVENTORY.md` ghi từng file đã inspect và reference callers trong phạm vi snapshot.

Không có công cụ truy cập inventory, thay source attachment hoặc kiểm installed instruction bytes của ChatGPT Project. Kho có 12 source root 00/10–80/90/91/92; 5 overlay active candidates, 2 Router versions, 14 file trong AetherFire CI (gồm lịch sử), và auxiliary/development/archive material. Số khoảng 22 live source slots là author-reported, chưa directly observed. CI README ghi baseline 2.6/Router 3.2; Router 4.0 tự khai final local cần CI 3.0 installed, và báo cáo finalization nói chưa deploy. Không dùng version mới nhất trong Git để suy installed state.

Mục tiêu upload profile có đúng **11 source attachments**: 00, tám modules, 92 và Router 4.0 đã cập nhật. CI 3.0 là instruction surface riêng, không tự chọn/cài từ repo. Nếu 7 cold candidates đều nằm trong inventory 22 hiện tại, chỉ bỏ chúng sẽ cho **22 → 15**, giải phóng 7 slot. Phần giảm tiếp về 11 phụ thuộc việc live inventory có auxiliary/historical attachments nào; không ghi 15 hay 11 thành live count đã xác minh.

## Audit các nguồn hiện hành

Tần suất bên dưới là access pattern được Router quy định; repository không có telemetry để định lượng số lần dùng thực tế. Source có chữ CURRENT không tự chứng minh admission; các AFM-001–008 khớp header, catalog và maintained-package checks.

| Source | Phân loại | Chức năng thực / Router frequency | Bootstrap / caller / load và semantics khi move |
| --- | --- | --- | --- |
| 00_AETHERFIRE_CONSOLIDATION_INDEX.md | HOT; DO NOT MOVE | Global index, catalog dẫn xuất, các boundary và integration decisions; mọi canon-dependent task | Full bootstrap; Router 2/3. Không chuyển vì cold discovery cần nó. Catalog không là dependency graph hay admission. |
| 10_WORLD_INSTITUTIONS_GEOPOLITICS_CURRENT.md | HOT; DO NOT MOVE | AFM-001: world/institutions/geopolitics và Academy; thường theo domain | Không luôn bootstrap; Router Module Gate/00, cross-owner từ 40/60/70/80. FULL_FILE; không chuyển current canon chỉ để tiết kiệm slot. |
| 20_STATUS_CIVIL_LABOR_CURRENT.md | HOT; DO NOT MOVE | AFM-002: legal/civic status, Civil/labor và shared axes | 00/92, owner interface với 30. FULL_FILE; các embedded provenance không làm toàn file cold. |
| 30_UNDIE_SYSTEM_CURRENT.md | HOT; DO NOT MOVE | AFM-003: Undie/Undi intake, rank/mobility, economy/access, White và visual | 00/92, interfaces 20/50/70. FULL_FILE; mixed embedded quotations giữ status và authority boundary. |
| 40_METAFICTION_CANON_TIMELINE_CURRENT.md | HOT; DO NOT MOVE | AFM-004: fiction layers, causal overlap, canon timeline và cross-world status | 00/92; controlling owner cho 50 và identity/cross-world interfaces. FULL_FILE. |
| 50_NARRATORS_POV_AND_HUMOR_CURRENT.md | HOT; DO NOT MOVE | AFM-005: narrator/POV/humor; giữ DESIGN INTENT/PROPOSAL labels | 00; clash causality thuộc 40, clothing thuộc 30. FULL_FILE; không promote presentation thành causal authority. |
| 60_MC4_IDENTITY_CURRENT.md | HOT; DO NOT MOVE | AFM-006: một identity, hai configurations, Academy và legacy exclusion | 00/92; Academy owner 10, metafiction owner 40. FULL_FILE; genealogy không nhập legacy cosmology/mechanics. |
| 70_MATRIARCHS_LAMENT_CURRENT.md | HOT; DO NOT MOVE | AFM-007: internal ML governance/relics/operations | 00/92; global owner 10, status 30, cross-world 40. FULL_FILE; vẫn separate owner. |
| 80_STABLE_AVIATION_RF_AIRSPACE_CURRENT.md | HOT; DO NOT MOVE | AFM-008: stable aviation, sovereignty/ATC/economy và route dependency | 00/92; global owner 10. Baseline list mention 91 không tự tạo unconditional cold fetch. FULL_FILE. |
| 92_OPEN_ISSUES_CURRENT.md | HOT; DO NOT MOVE | Compact open-state routing control, không resolve entries | Full bootstrap; Router 2/6 và new-source comparisons. Hooks tới 90/91 chỉ fetch khi decisive history/reconciliation cần. |
| 90_DESIGN_HISTORY_AND_RECONSIDERATIONS.md | COLD CANDIDATE → bundled | Temporal layer: genealogy, retired designs, surviving legacy, reconsiderations, current-status corrections và proposals | 00 entry 9; 10 genealogy reference; 92 AF-OPEN-029; explicit history/proposal/provenance task. Không bootstrap. FULL_FILE khi selected vì mixed status; không section-only shortcut. Preserve toàn bộ labels, supersession notices, order và references. |
| 91_RECONCILIATION_RECORD.md | COLD CANDIDATE → bundled | Audit/control: addenda + reconciliation summary + assertion-level AF-CX conflicts/priority/provenance | Router 6, 92 hooks, current-domain conflict/supersession callers. Không normal-current-canon baseline. FULL_FILE khi decisive; reference alone không kích hoạt. Giữ latest addenda trước older record, source quotes, all resolutions/conflicts. |
| Source Router v4.0 | HOT; DO NOT MOVE | Bootstrap, Module Gate, FULL_FILE/closure, reconciliation và overlay gates | Installed CI 3.0 required; luôn runtime bootstrap control. Chỉ thêm resolver và pinned overlay routing. Không chuyển hoặc tạo secondary Router. |
| Source Router v3.2 | KEEP SEPARATE | Older control contract: numeric CI resolver, fixed domain table, full-read gates | Không sửa để giả deployment; giữ comparison/rollback riêng. Nếu live vẫn dùng 3.2, migration chưa active; không claim new behavior. |

## Overlay audit

Tất cả năm overlay có scope/activation hooks và authority inheritance; không overlay nào là canon source hoặc bootstrap bắt buộc cho mọi prompt. Phiên bản package là exact reviewed generation, không resolve latest main trong task. FULL_FILE của overlay vẫn bắt buộc khi activate; pack load không activate phần còn lại.

| Logical identity trong Anti-Drift Source/ | Phân loại / gate và callers | Identity/provenance khi bundle |
| --- | --- | --- |
| AetherFire_Anti_Drift_Interface_Economy_State_Stabilization_v1.1.md | COLD CANDIDATE; Router economy/institution interface; worldbuilding dependency khi economy/labor/housing/trade/logistics/market/stabilization material | Scope clamp/MUST_OPEN/MAY_STOP và state capacity không bị đổi; worldbuilding không override depth. Filename reference vẫn resolve logical source. |
| AetherFire_Anti_Drift_Modular_Concept_Architecture_v1.0.md | COLD CANDIDATE; architecture/typed relation/actor information; named dependency của mortality | Module autonomy, actor agency/information và stop rule giữ riêng. Multiple named things không tự activate. |
| AetherFire_Anti_Drift_Mortality_Relationship_Plot_Immunity_v1.1.md | COLD CANDIDATE; survival/lethal exposure/relationship protection/dynasty/captivity/return | Requires modular; total-war conditional nếu operational conflict. Giữ symmetric UNKNOWN survival gate, không death bias. |
| AetherFire_Anti_Drift_Total_War_RP_v1.1.md | COLD CANDIDATE; total-war hoặc bounded operational conflict; độc lập với mortality gate | Scope contraction không giảm rigor; preserve route/timing/authority/persistent loss và UNKNOWN. |
| AetherFire_Anti_Drift_Worldbuilding_Internal_Logic_v1.1.md | COLD CANDIDATE; systemic design/coherence/feedback/propagation; local lookup không đủ trigger | Conditional economy hook giữ nguyên; không mở full-world design khi package đã loaded. |

## Auxiliary, retired và provenance material

Giữ riêng trên GitHub, không mặc định bundle/upload: MANIFEST (maintenance/hash inventory, không admission); build_consolidation.py/ps1 (current-header/catalog/hash validator); tools/legacy builder (former reconstruction, không current workflow); tests/control-regressions và maintenance tests (development checks); ROUTER_4_FINALIZATION_REPORT (development/deployment evidence, không runtime control).

AetherFire CI/README và mọi historical/compact CI/router snapshot được inspect theo nội dung/version/status và control references. Installed CI giữ riêng; không copy toàn thư mục vào Project. `Project CI/AetherFire CI/` là management/comparison mirror, không tự có runtime authority. Old chat anti-drift snapshots chứa superseded embedded canon, không eligible fallback. Rejected v3 không được activate hoặc reconstruct. Raw Source_Archive và Anti-Drift Source/Source_Archive vẫn là historical/provenance theo 00 và Router quarantine, không nhét toàn archive vào cold package. Task explicit cần raw archive ngoài 7 identities là ngoài fetch bound của migration này; không giả cold package có đầy đủ raw provenance. 91 vẫn giữ trail/reference, không sao chép hay sửa source archive để tạo đủ bằng chứng.

Các filename/path bên trong payload là logical source/provenance identity. Bảo toàn nguyên văn và resolver trong 00/Router là đủ; không rewrite lore references. Source_Archive path không được alias thành cold current control. Same basename ở archive/CI mirror không được dùng thay payload declared.

## Proposal và access cost

Một package hợp lý vì một task có thể cần reconciliation + nhiều overlay/dependency; mọi cold activation đều dùng complete source reads, và receipt chung loại fetch fanout. History không cùng frequency với overlays, nhưng vẫn có status boundaries và storage compatibility; không có observed hard transport failure buộc tách.

Chi phí thực: 90 chiếm 123.716 byte, gần một nửa package; một overlay đơn cũng nạp 261.454 byte. Đây là tăng context đáng kể, không phải tăng tool calls. Connector đã được thử bằng một full fetch ở commit SHA và trả nội dung exact, không truncation. Điều đó chứng minh transport trong phiên audit này, chưa chứng minh ChatGPT Project có cùng output budget/context retention. Nếu shadow runtime chứng minh truncation hoặc context-budget failure, phương án tối thiểu tiếp theo là **2 packages**: history riêng và reconciliation + overlays chung; không per-file fetch. Không triển khai split dựa trên giả định alone.

## Before / after và deployment profile

```text
Before (author-reported live ≈22, exact attachment inventory unknown)
  Project: 00 + 10–80 + 90 + 91 + 92 + Router + overlays + unknown auxiliaries

After (prepared target; live attachment update not performed)
  Project: 00 + 10–80 + 92 + updated Router 4.0 = 11 sources
  Installed instructions: compatible AetherFire CI 3.0, separately
  GitHub runtime cold route: Cold Storage/AETHERFIRE_COLD_PACKAGE.md
    PART 1: 91
    PART 2: 90
    PART 3–7: economy, modular, mortality, total-war, worldbuilding
  GitHub authoring: original seven files retained, excluded from Project upload
  GitHub development/provenance: manifest/build/tests/history/archive, separate
```

This is relocation of the **runtime attachment set**, not destructive movement of maintained source files. Keeping standalone authoring inputs avoids redesigning the current validator, preserves independent provenance/hash/history, and does not add runtime source fetch routes.

Deployment order: publish pinned package; upload matching 00/92/modules and updated Router; verify installed CI compatibility; remove the seven cold attachments and auxiliary/history attachments outside the 11-file hot profile; never attach the bundle itself. Retain existing attachment copies until the replacement hot profile and connector access are usable. Do not claim deployment from commit alone. There is no connector in this task capable of completing that final live attachment step.

## Version consistency

00 pins repository/path/exact commit SHA, generation, package byte length and SHA-256. Package manifest binds all cold identities plus fingerprints of eight hot modules and 92. Task freezes the declaration, compares generation/digest/boundaries and selected hot-source fingerprints; invalid/missing validation blocks required cold work. Never use main or substitute another ref. Package publication commit precedes the hot-index integration commit, avoiding a self-referential SHA. Current builder refreshes 00's manifest hash; new offline pack checker detects maintained hot/cold changes not reflected in the bundle/declaration.

Future maintenance: edit authoritative maintained inputs; regenerate with tools/build_cold_package.py --write; publish a new package commit; update 00 pin/digest/bytes/generation; refresh current manifest; run both checks and deploy a matching hot snapshot. No daemon, runtime DB, invalidation subsystem, sync service, registry framework or new governance layer.

## Fetch limits và trace expectations

Successful complete load, contents retained in current task; no automatic retries/pagination/search/version discovery:

| Case | Max cold package fetch | Required trace |
| --- | --- | --- |
| Normal canon lookup, no materially required cold dependency | 0 | 00/92 → selected hot owners → answer; mention of 91 alone does not activate. |
| One cold dependency | 1 | resolve frozen key → fetch/validate full package → selected logical source FULL_FILE. |
| Multiple cold overlays | 1 | first required overlay loads package; later overlays/dependencies reuse exact contents. |
| Reconciliation + overlay | 1 | 91 requirement loads package before new-source comparison; later applicable overlays reuse after reconciliation. |
| History + reconciliation + all applicable overlays | 1 | same pinned key; no standalone-file fanout. |
| Fetch failed/partial, wrong path/ref, access denied | at most 1 attempt | FAILED receipt → no automatic retry/fallback → block required dependent work. |

Normal *canon task* that actually needs an overlay/reconciliation belongs to the corresponding cold case, not the 0-fetch case. These are Router contract limits, not measured live ChatGPT behavioral guarantees. Source loss during compaction blocks reuse-dependent work; it does not license a false FULL_FILE claim or proactive refetch. No persistent cache across chat/conversation.

## Failures, tests và unresolved runtime evidence

Unavailable GitHub, permission denied, wrong path/ref, mismatch, partial response, duplicate/missing source: required cold work blocked; optional demonstrably nondecisive evidence gap continues with SOURCE_LOAD_PARTIAL and explicit unverified scope. Hot independent work may continue. No guess, current-silence archive fallback or free main read.

Tests: existing 20 maintained-package tests; new byte-exact payload, partial/corrupt package, wrong digest/generation, missing identity/boundary, hot-generation-change and source-nonmutation checks; both maintenance checks; actual pinned one-call GitHub full-package fetch compared exact with generated contents. Static review of Router gates/trace table preserves FULL_FILE, VERIFIED_MODULE_CLOSURE, 91 requirement and conditional overlay dependency gates. Offline checks do not prove live routing/semantics. Existing PowerShell semantic runner cannot run here (pwsh unavailable; no model runner configured), and its older CI-base parser incompatibility with 3.0 is already documented in Router finalization; not repaired in this scope.

Actual unresolved failures/limits: live attachment inventory/installed state inaccessible; live migration and Project shadow retrieval/retention/compliance remain unverified; clone proxy route unavailable; package imposes larger context load; authoring maintenance must republish/repin after relevant changes. Hypothetical only: need for persistent caching, invalidation/synchronization services, secondary Router, new authority/governance or module ontology redesign. No such framework added.

Final invariant: HOT LOCAL; COLD BUNDLED; FETCH ONCE PER PACKAGE VERSION PER TASK. Project-file reduction becomes observed only after the live attachment set is updated and counted.
