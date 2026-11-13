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

## C2-CORRECTION-004 — 2026-11-08 — Gọi Router trong source gate như FTH CI 3.4

Đối chiếu trực tiếp FTH CI 3.4: locator nằm ngay trong chỉ thị FULL_FILE → PROMPT_ROUTE_ONLY, kèm Router REQUIRED và thiếu Router chặn phần phụ thuộc. C2 trước đó chỉ đặt locator trong header rồi gọi “the named Router”; checker cũng kiểm metadata thay vì lời gọi tại source gate.

Theo yêu cầu tác giả, bỏ Router metadata header, ghi đường dẫn chính xác trong chỉ thị FULL_FILE tại source gate và nêu rõ missing Router blocks dependent work. Checker kiểm lời gọi trong đúng section, test từ chối trường hợp chỉ có header. Giữ nguyên Router, stages, family, các cơ chế CI khác và lore. CI cuối 7990 ký tự, gồm newline cuối, dưới 8.000. Không push; bằng chứng kiểm tra chỉ là tĩnh.

## C2-CORRECTION-005 — 2026-11-08 — CI dùng nguồn của ChatGPT web

Tác giả làm rõ CI được dán vào phần chỉ dẫn trên ChatGPT web. C2-CORRECTION-004 trước đó chép cách ghi path repository nhưng chưa chỉ ra đường truy xuất tài liệu trên web; static checker còn coi đúng chuỗi local path là đủ. Quyết định này thay cách gọi đó, không thay các cổng kiến trúc.

CI yêu cầu truy xuất `C2_Anti_Drift_Source_Router_v1.0.json` từ nguồn thực sự có của Project (Project Sources hoặc file Library được gắn vào chat), xác minh identity/version, đọc FULL_FILE rồi vào PROMPT_ROUTE_ONLY. Thiếu/trùng/một phần Router phải chặn phần phụ thuộc và yêu cầu file, không bịa nội dung. Router áp cùng contract cho source/control tiếp theo; local path, directory/direct-child chỉ là metadata bảo trì, không là web filesystem hoặc tự truy cập GitHub. Không có registry/locator schema mới.

Checker vẫn kiểm file local để bảo trì, nhưng CI gate dùng tên tài liệu và web-source contract; test từ chối metadata-only, local-path-only, summary thay full read và bỏ điều kiện chặn. README ghi rõ việc cung cấp Router/control/source trên web là bước riêng, không tự xảy ra sau commit/push. Tham chiếu sản phẩm đã đọc: https://learn.chatgpt.com/docs/projects . CI 7991 ký tự gồm newline cuối, dưới 8.000. LIVE VERIFIED: NOT RUN; không upload/cài Project hoặc push trong correction này.

## C2-INGESTION-001 — 2026-11-14 — Nhập lore theo nguồn có thẩm quyền

Căn cứ: yêu cầu nhập lore sau kiểm định ổn định, phần lore do tác giả cung cấp trong [Audit Cosmic Core CI](https://chatgpt.com/c/6af31549-72d8-83ec-86de-73dd8b28c708) và xác nhận về câu chú trong [Project Cosmic Core Control](https://chatgpt.com/c/6ae98537-1a10-83ec-a3e9-6b9948fa317b).

`C2M-021` giữ định nghĩa câu chú riêng Os s5shi của 25_1. `C2M-022` giữ năng lực riêng của 25_2. `C2M-110` giữ thánh tích trong phạm vi World 1. 02 định tuyến tới các nguồn này. Tên Rongo được ghi ở 11 cho đoàn tàu và ở 10 cho tổ chức quản trị, với hai identity tra cứu riêng ở 01.

Nhận `C2M-112` cho diễn biến Campaign 01. 110 giữ sự thật bền của World 1 và 111 giữ thông tin được cấp cho nhiệm vụ. Chỉ ghi các mốc được nêu rõ trong yêu cầu. Kết quả tranh đoạt, cơ chế chi tiết và xuất xứ từng dữ kiện giữ theo mức bằng chứng hiện có.

## C2-INGESTION-002 — 2026-11-14 — Nhập delta tiền đề và World 1

Căn cứ: tác giả duyệt nhập các bổ sung tương thích trong `C2_INITIAL_PREMISE_AND_WORLD1_LORE_DELTA_2026-11-14.md` sau `DELTA_AUDIT` và chỉnh cách phân loại nhãn đội. Nguồn gốc riêng của từng dữ kiện vẫn chưa xác lập.

`C2M-021` giữ câu chú Os s5shi và cơ chế sao lưu ký ức. Quyền dùng phép của người khác vẫn là đề xuất. `C2M-022` giữ cơ chế bảo hộ bản chất của 25_2. Cả hai dùng module hiện hành.

`C2M-110` giữ sự thật bền và định nghĩa thánh tích. `C2M-112` giữ diễn biến tranh đoạt, vượt mê cung và trích xuất. Mốc niệm chú trước trích xuất và quan hệ bên lấy vật thuộc đội khác đã xác lập. Giữ mốc “Team 1 trở về trước”. Ánh xạ giữa nhãn “Team 1” và Team 25 là `UNKNOWN`, cùng với danh tính bên lấy vật và kết quả khôi phục thực tế.
