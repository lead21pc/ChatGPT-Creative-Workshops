# The Kingdom

**The Kingdom** là project/paracosm; **Hyperborea** là quốc gia trong paracosm. Hyperborea là tên quốc gia hiện hành; tên giữ chỗ cũ đã ngừng dùng trong nguồn current, chỉ giữ trong archive/provenance. Namespace `TK-*` không đổi vì đổi tên quốc gia.

Đây là worldbuilding cá nhân: thế giới vận động, lịch sử/hệ quả tích lũy; không có nhân vật chính trung tâm. Nhân vật là camera, fantasy tạo hệ quả qua con người và hệ thống. Repository chỉ externalize một phần thế giới của tác giả; thiếu dữ kiện không chứng minh tác giả chưa biết.

## Cấu trúc nguồn

```text
The Kingdom/
├─ README.md
├─ THE_KINGDOM_CHECKPOINT_STATE_INDEX.md
├─ TK_TIMELINE_*.md
├─ TK_METHOD_*.md
├─ TK_DOMAIN_*.md
├─ controls/
└─ Source_archive/
```

- Active root là owner current trong scope và theo nhãn từng phần; ACTIVE không biến mọi draft/proposal thành canon.
- `controls/` giữ CI, anti-drift, workflow và câu hỏi kiểm tra. CONTROL != LORE SOURCE. Chưa xác định CI nào đang cài trong ChatGPT Project; vị trí tệp không chứng minh activation/runtime.
- `Source_archive/` là lịch sử/provenance chỉ đọc sau migration; không current authority, không fallback, không tự nạp. Không sửa ngược lịch sử để khớp current.

```text
DO NOT USE Source_archive TO FILL A GAP IN ACTIVE SOURCES.
```

Chỉ đọc khi tác giả yêu cầu history/provenance/audit/recovery hoặc active source dẫn rõ historical record cần đối chiếu. Link provenance không nhập cả handoff thành canon hoặc cho phép phục hồi lore. Khi thiếu current source, giữ UNKNOWN/repository gap.

## Nguồn active và điều hướng

Bắt đầu từ [timeline index](THE_KINGDOM_CHECKPOINT_STATE_INDEX.md) khi câu hỏi có thời điểm. Bảng sau chỉ điều hướng owner, không là registry hoặc bảng xếp authority.

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

Migration local không cài CI, không cập nhật ChatGPT Project/Library và không chứng minh runtime. README chỉ định hướng; source chi tiết và xác nhận mới hơn của tác giả giữ thẩm quyền tương ứng. Không có Router, Manifest, registry hay archive promotion trong layout này.
