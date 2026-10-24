# The Kingdom

**The Kingdom** là project/paracosm; **Hyperborea** là quốc gia trong paracosm. Hyperborea là tên quốc gia hiện hành; tên giữ chỗ cũ đã ngừng dùng trong nguồn current, chỉ giữ trong archive/provenance. Namespace `TK-*` không đổi vì đổi tên quốc gia.

Đây là worldbuilding cá nhân: thế giới vận động, lịch sử/hệ quả tích lũy; không có nhân vật chính trung tâm. Nhân vật là camera, fantasy tạo hệ quả qua con người và hệ thống. Repository chỉ externalize một phần thế giới của tác giả; thiếu dữ kiện không chứng minh tác giả chưa biết.

## Cấu trúc nguồn

```text
The Kingdom/
├─ README.md
├─ THE_KINGDOM_CHECKPOINT_STATE_INDEX.md
├─ TK_CURRENT_SOURCE_INDEX.md
├─ TK_RECONCILIATION_RECORD.md
├─ TK_OPEN_ISSUES_CURRENT.md
├─ MANIFEST.md
├─ TK_TIMELINE_*.md
├─ TK_METHOD_*.md
├─ TK_DOMAIN_*.md
├─ controls/
│  └─ anti_drift/
├─ tools/
├─ tests/
└─ Source_archive/
```

- Active root là owner current trong scope và theo nhãn từng phần; ACTIVE không biến mọi draft/proposal thành canon.
- `controls/` giữ CI, anti-drift, workflow và câu hỏi kiểm tra. CONTROL != LORE SOURCE. CI repository hiện hành là TK CI v1.0; trạng thái CI đang cài trong live Project chưa được kiểm chứng.
- `Source_archive/` là lịch sử/provenance chỉ đọc sau migration; không current authority, không fallback, không tự nạp. Không sửa ngược lịch sử để khớp current.

```text
DO NOT USE Source_archive TO FILL A GAP IN ACTIVE SOURCES.
```

Chỉ đọc khi tác giả yêu cầu history/provenance/audit/recovery hoặc active source dẫn rõ historical record cần đối chiếu. Link provenance không nhập cả handoff thành canon hoặc cho phép phục hồi lore. Khi thiếu current source, giữ UNKNOWN/repository gap.

## Nguồn active và điều hướng

Bắt đầu từ [current source index](TK_CURRENT_SOURCE_INDEX.md); khi thời gian quan trọng dùng thêm [timeline index](THE_KINGDOM_CHECKPOINT_STATE_INDEX.md). Bảng sau chỉ điều hướng owner, không là registry hoặc bảng xếp authority.

| SOURCE_ID | Tệp | Vai trò và phạm vi |
|---|---|---|
| TK-DOM-GEO | [TK_DOMAIN_GEOPOLITICS.md](TK_DOMAIN_GEOPOLITICS.md) | DOMAIN — Địa chính trị, DMZ, đối ngoại, động cơ mở cửa và các lựa chọn còn mở. |
| TK-DOM-INFRA | [TK_DOMAIN_INFRASTRUCTURE.md](TK_DOMAIN_INFRASTRUCTURE.md) | DOMAIN — Hạ tầng, không lưu và capabilities thường trực; phương án mở cửa giữ status riêng. |
| TK-DOM-COUNTERINTEL | [TK_DOMAIN_COUNTERINTELLIGENCE.md](TK_DOMAIN_COUNTERINTELLIGENCE.md) | DOMAIN — Phản gián, quyền tiếp cận, tri thức và attribution; cơ chế đề xuất giữ riêng. |
| TK-DOM-HEALTH | [TK_DOMAIN_HEALTH.md](TK_DOMAIN_HEALTH.md) | DOMAIN — An toàn sinh học, điều trị và quyền y tế; chi tiết chưa xác định vẫn mở. |
| TK-DOM-LANGUAGE-RELIGION | [TK_DOMAIN_LANGUAGE_RELIGION.md](TK_DOMAIN_LANGUAGE_RELIGION.md) | DOMAIN / DESIGN PHILOSOPHY — Universal Language, thần tính, World Tree và triết lý; không xác nhận quyền tiếp cận. |
| TK-DOM-LAW | [TK_DOMAIN_LAW.md](TK_DOMAIN_LAW.md) | DOMAIN — Luật V2 đang tái thiết kế; Luật Ngoại Nhân chỉ áp dụng ngoại nhân đã bị bắt. |
| TK-METHOD-FICTION | [TK_METHOD_FICTION.md](TK_METHOD_FICTION.md) | RUNTIME / AUTHORING METHOD — World-state, checkpoint/interval, progression và giới hạn tri thức. |
| TK-DOM-POT | [TK_DOMAIN_POT.md](TK_DOMAIN_POT.md) | DOMAIN — Thiết bị POT; canon khả năng và chi tiết còn mở. |
| TK-METHOD-POV | [TK_METHOD_POV_PERSPECTIVE.md](TK_METHOD_POV_PERSPECTIVE.md) | RUNTIME / AUTHORING METHOD — POV xuyên timeline; nguyên tắc đã xác lập và thiết kế chưa accepted giữ riêng. |
| TK-DOM-DELEGATION | [TK_DOMAIN_OPENING_DELEGATION.md](TK_DOMAIN_OPENING_DELEGATION.md) | DOMAIN / OPENING DESIGN — Mandate xác minh, itinerary draft và câu hỏi; không phải event log. |
| TK-TL-CP01 | [TK_TIMELINE_CP01_OPENING.md](TK_TIMELINE_CP01_OPENING.md) | CHECKPOINT — Breakpoint mở cửa; pre-state tối thiểu, direct delta và boundary state CP1. |
| TK-TL-I01-02 | [TK_TIMELINE_INTERVAL_CP01_CP02.md](TK_TIMELINE_INTERVAL_CP01_CP02.md) | INTERVAL — Sau boundary CP1 đến ngay trước CP2; progression, phản ứng và state tích lũy có nguồn. |
| TK-TL-CP02 | [TK_TIMELINE_CP02_REVEAL.md](TK_TIMELINE_CP02_REVEAL.md) | CHECKPOINT — Vụ thử nước, đánh chặn, attribution và military/mage reveal; boundary tức thời, không sở hữu phản ứng nhiều ngày sau. |
| TK-TL-POST02 | [TK_TIMELINE_POST_CP02.md](TK_TIMELINE_POST_CP02.md) | POST-CHECKPOINT MATERIAL — Premise logistics sau CP2 chưa có số checkpoint; phụ lục simulation lịch sử không là baseline phản ứng current. |

## Cách vận hành và giới hạn tri thức

```text
CHECKPOINT → INTERVAL → CHECKPOINT
CP1 → I01-02 (≈ 2 năm) → CP2 → POST02
```

Checkpoint giữ breakpoint/direct boundary delta. Interval giữ progression, thích nghi, tiếp xúc, phản ứng/state tích lũy; không đủ nguồn để tự viết hai năm lịch sử. Domain giữ hệ thống thường trực, method giữ cách kể. Không đồng nhất S1 tức thời với final pre-CP2 state.

WORLD STATE là trục cấu trúc. POV dùng **ACTOR + TIME + AVAILABLE INFORMATION**: world truth, quan sát, phân tích nội bộ, công bố và diễn giải xã hội khác nhau. Không kéo tri thức tương lai về quá khứ, không có phản ứng chung cho nhân loại.

[Method fiction](TK_METHOD_FICTION.md) khóa payoff: **vả assumption/model, không làm actor ngu**; CP1 sửa ước lượng, CP2 phá mô hình/phân loại, cargo sau CP2 bộc lộ normality gap. Đây là chức năng tác giả, không là kết luận đồng nhất mọi actor. CP3 chỉ là candidate đang cân nhắc trong method, không có timeline owner.

## Tham chiếu thực tế

**IRL REFERENCE != CURRENT THE KINGDOM STATE.** Phân biệt IRL REFERENCE @ TIME, KINGDOM DIVERGENCE và ACTOR STATE @ T; nền khoảng 2003 không tự thành trạng thái IRL 2026. Chỉ externalize divergence ảnh hưởng quyết định; không tự nhập lịch sử/chính sách thật vào fiction.

## Giới hạn kiểm chứng

Giữ riêng CANON, USER-PROVIDED STATE, DECIDED, PROPOSAL, UNDER CONSIDERATION, INFERENCE, UNKNOWN, STALE, CONFLICTED. Method POV còn thiết kế chưa accepted; luật còn reset/recovery ngoại nhân có phạm vi; itinerary chưa là lịch sử. Luật nội quốc chưa thiết kế; handoff báo prototype Tree nhưng repository chưa có asset để kiểm chứng.

Migration local không cài CI, không cập nhật ChatGPT Project/Library và không chứng minh runtime. README chỉ định hướng; source chi tiết và xác nhận mới hơn của tác giả giữ thẩm quyền tương ứng. Stack quản lý v1.0 bên dưới thay giới hạn không-Router của migration trước; không có archive promotion hoặc registry ontology.


## Stack quản lý v1.0

Tất cả control v1.0 dưới đây có Status: ACTIVE trong repository; REPOSITORY ACTIVE != LIVE CHATGPT PROJECT DEPLOYED. Task này không deploy hoặc xác nhận runtime retrieval/compliance.

- [TK CI v1.0](controls/TK_CI_v1.0.md): kernel tự chứa semantics Global Native v9.0; FTH CI 3.4 chỉ là structural reference, không runtime dependency.
- [TK Router v1.0](controls/TK_ROUTER_v1.0.yaml): default cho mọi current-dependent task; generic task tự đủ có thể bỏ qua. CI sở hữu entry, Router sở hữu chọn/nạp/đối chiếu owner và overlay, không tự chọn CI runtime.
- [Authoring Pipeline](controls/TK_AUTHORING_PIPELINE_v1.0.md): biến đổi được yêu cầu và điểm dừng, không source authority.
- [Glossary](controls/TK_CONTROL_VOCABULARY_GLOSSARY_v1.0.md): hỗ trợ viết/đọc, không prerequisite runtime.
- Chín overlay trong `controls/anti_drift/`: Temporal, Actor, Relation, Institution, IRL, Economy, Belief, Crisis, Narrative. Chỉ chọn khi semantic applicability quyết định task, highest ACTIVE numeric; không keyword-only hoặc candidate lifecycle.
- [Current source index](TK_CURRENT_SOURCE_INDEX.md) tách [temporal index](THE_KINGDOM_CHECKPOINT_STATE_INDEX.md); [reconciliation](TK_RECONCILIATION_RECORD.md) giữ quyết định/migration và coverage; [open issues](TK_OPEN_ISSUES_CURRENT.md) giữ unresolved, không tạo canon.
- [Manifest](MANIFEST.md) nhận current paths/hashes và nêu bảo trì. `tools/validate_kingdom_package.py` chỉ kiểm; `--write` chỉ vùng generated catalog/hash, không source text hoặc lore.

```text
PROMPT_ROUTE_ONLY → BOOTSTRAP_GATE → OWNER_GATE → TEMPORAL_GATE
→ SOURCE_LOAD → RECONCILIATION → ANTI_DRIFT_OVERLAY_GATE
→ PROMPT_EXECUTION → PRE_RESPONSE_CHECK
```

Header owner gồm SOURCE_ID, RUNTIME_ROLE, ROLE, STATUS, SCOPE, AUTHORITY_BOUNDARY, CROSS_OWNER_BOUNDARY, LOAD_MODE. V1.0 chỉ FULL_FILE; future actor/event owner cần material và scoped admission, không file trống. FULL MANAGEMENT STACK != FTH CLONE: TK giữ persistent owner + temporal delta + actor information, không AFM/country/module assumptions của FTH.

## Bảo trì và bằng chứng

Từ repository root:

```powershell
python -B "worlds/The Kingdom/tools/validate_kingdom_package.py" --check
python -B -m unittest discover -s "worlds/The Kingdom/tests"
```

Mặc định tool chỉ đọc. Khi đã xem lỗi stale và kiểm cấu trúc, `--write` chỉ cập nhật generated catalog/hash rồi phải chạy `--check` lại. PyYAML dùng để đọc YAML (môi trường tác vụ có sẵn 6.0.3). Numeric version: 1.9 < 1.10; chỉ ACTIVE được chọn, archived/superseded/retired hoặc status khác không đủ điều kiện.

Tests kiểm structural contracts, dependency resolution và mutation failures; sáu tình huống trong `tests/control_cases.json` là protocol chưa chạy model, không semantic PASS qua substring. Không current build input từ archive; rollback dùng Git history.

Bốn CI và anti-drift cũ được thay sau coverage, lưu tại `Source_archive/controls_legacy/`. Workflow seed nhiều paracosm và bộ câu hỏi stress-test giữ độc lập, không cạnh tranh CI/Router. Archive cũ giữ byte, không chỉnh wording cho giống stack mới.
