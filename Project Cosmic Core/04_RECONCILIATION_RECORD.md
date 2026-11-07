# C2 — Quyết định và reconciliation

## C2-BASELINE-001 — 2026-11-07 — Quyền tạo skeleton

Căn cứ: yêu cầu implementation của tác giả sau audit ACCEPT WITH LOCAL CORRECTIONS. Phạm vi chấp nhận là skeleton quản lý, control/tooling, static verification và đúng lượng dữ kiện tối thiểu được prompt chỉ định; không phải nhập toàn bộ lore hoặc chốt mọi premise chưa được ghi.

Tạo 15 current modules cùng index, history/reconciliation/open state, manifest, CI/Router, bốn family Anti-Drift và test bảo trì. Không có predecessor C2 hoặc owner transfer để xử lý trong mốc đầu.

Các quyết định quản lý: Module ID/path tường minh và ổn định; FULL_FILE; ba semantic catalog chỉ định tuyến; provenance/chấp nhận tách trục; owner world/briefing/scenario tách riêng; accepted consequence cập nhật từng owner thực bị ảnh hưởng; dải chục không là quota. Không có engine tự xử lý các quyết định này.

## C2-BASELINE-002 — Phạm vi dữ kiện được ghi

Chỉ nhập premise tối thiểu ở [06](06_C2_PREMISE_CORE_CURRENT.md); nguồn gốc project ở [07](07_C2_PREMISE_PROVENANCE_CURRENT.md); Rongo/tàu ở 10/11; Team 25 và năm identity ở 20–25; minimal World 1 ở 110. 111 chỉ giữ boundary và các mục briefing chưa được nhập.

Character 25_1/A: Cosmic Mage thực và elemental-mage cover Rongo biết là hai lớp riêng. Character 25_2/B: Battle Shaman / Battle Priest thực; không nhập full profile/divine-backer detail. 25_3–25_5 chỉ giữ slot/identity. Không gán xuất xứ lucid-dream/later-addition cho từng assertion khi tác giả chưa cung cấp.

## Giới hạn và hồ sơ sau này

[03](03_DESIGN_HISTORY_AND_RECONSIDERATIONS.md) giữ lịch sử; [05](05_OPEN_ISSUES_CURRENT.md) giữ mục mở. Reconciliation về sau ghi căn cứ chấp nhận, assertion/scope bị thay, predecessor/owner mới khi có, và vị trí current source đã cập nhật; không tự hòa giải conflict. File này không là world-truth fallback.

Static verification không chứng minh live GPT Project. LIVE VERIFIED: NOT RUN.

## C2-CORRECTION-001 — 2026-11-08 — Gỡ owner nhân vật quá sớm

Căn cứ: tác giả yêu cầu local correction trên baseline repository `d3a0b705331dd0a2680577d71058466d3f33de1c`. Các ghi nhận tạo 15 module/năm hồ sơ tại C2-BASELINE-001/002 phía trên là lịch sử mốc đầu, đã được thay trong đúng phạm vi này.

Gỡ các source `23_CHARACTER_25_3_CURRENT.md`, `24_CHARACTER_25_4_CURRENT.md`, `25_CHARACTER_25_5_CURRENT.md` và admission `C2M-023`, `C2M-024`, `C2M-025`. Không tái cấp các ID đó hoặc đổi ID của module còn lại. Git giữ bản tiền nhiệm; không tạo archive hoặc nguồn dự phòng hoạt động.

Ba identity/slot `25_3`, `25_4`, `25_5` và membership Team 25 vẫn tồn tại; [20](20_TEAM_25_TAIYI_ZHENREN_CURRENT.md#slot-mo) giữ slot mở cho tới khi có trạng thái độc lập và quyết định tác giả riêng cho hồ sơ mới. [01](01_C2_ACTOR_ORGANIZATION_CATALOG_CURRENT.md) và [05](05_OPEN_ISSUES_CURRENT.md) định tuyến về 20. Không nhập nội dung nhân vật mới. Giữ 21/22 và owner thông tin nhiệm vụ 111.

Package sau correction có 12 current modules / 16 numbered current-file hashes. Generated catalog/hash được đồng bộ bằng builder; topology, header contract và những owner khác giữ nguyên.

## C2-CORRECTION-002 — 2026-11-08 — Chuẩn hóa control và viết lại CI

Theo cùng yêu cầu tác giả: sáu control active (CI, Router, MCA, WIL, Actor Reception, Operational Mission) chỉ dùng tiếng Anh. Giữ paths/version, bốn family, stages và dependencies của Router. Không tạo continuation CI, Pipeline, family hoặc architecture mới.

Đã đọc đầy đủ `llm-controls/global-instructions/ChatGPT Project Global Native/chatgpt v9.0.txt` làm kernel/base, `Project Feather Core/Project Feather Core CI/FTH_CI_version_v3.4.md` làm tham chiếu chuyên biệt project, và C2 CI v1.0 cũ để giữ delta C2. Đây là căn cứ biên soạn/bảo trì, không phải thêm cổng đọc file Global/FTH trong runtime C2.

Global giữ grounding/discourse/epistemic control, turn/state, claim/dependency, cập nhật và giải thích chung. CI C2 chuyên biệt quyền tác giả/canon, source gate, owner/truth-state và các ranh giới C2; Router/Anti-Drift tiếp tục giữ chi tiết chọn/nạp nguồn và suy luận. Không nhập ontology hoặc Pipeline của project tham chiếu. Ngôn ngữ control tiếng Anh không tự đổi hợp đồng trả lời tiếng Việt được kế thừa từ Global.

Đây là sửa tại chỗ; lịch sử tiền nhiệm nằm trong Git. Static verification không chứng minh live GPT Project; LIVE VERIFIED: NOT RUN.

Kiểm chứng correction: builder đạt 12 module/16 hash; Router structural check đạt bốn family; 26 unit/contract tests đạt. CI cuối dài 6.664 ký tự, tính cả newline cuối, dưới 8.000. Đã đối chiếu các ID còn lại và cấu trúc Router với baseline: không renumber, không đổi stages/paths/dependencies. Chỉ file trong C2 thay đổi; không sửa FTH và không push. Đây là bằng chứng tĩnh, không là live GPT Project verification.

## C2-CORRECTION-003 — 2026-11-08 — Trích cơ chế Global vào CI tự chứa

Tác giả sửa cách hiểu “base”: phải đưa cơ chế thực sự của Global v9.0 vào CI, không chỉ ghi nhãn hoặc giả định được kế thừa. Quyết định này thay phần diễn giải kế thừa tại C2-CORRECTION-002; các correction về slot, tiếng Anh và kiến trúc khác giữ nguyên.

CI hiện có quy tắc vận hành trực tiếp cho CONTROL GROUNDING, DISCOURSE FIDELITY, EPISTEMIC NON-ESCALATION cùng thứ tự áp dụng; xác định thao tác/giai đoạn; kiểm căn cứ mệnh đề; cập nhật và rút kết luận phụ thuộc; xử lý bất định; điều chỉnh giải thích/người đọc; hợp đồng tiếng Việt. Không còn Base header hoặc giả định cần file Global ngầm để có các cơ chế đó. Giữ source gate và boundary C2, rút phần lặp để còn 7985 ký tự, tính cả newline cuối, dưới 8.000. Test không còn dùng nhãn Base làm tiêu chí đúng. Không đổi Router/Anti-Drift, admission hoặc lore; không push. Live verification chưa chạy.
