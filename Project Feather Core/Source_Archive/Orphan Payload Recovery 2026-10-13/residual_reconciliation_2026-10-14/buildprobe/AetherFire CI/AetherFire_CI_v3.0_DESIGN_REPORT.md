# AetherFire CI 3.0 — báo cáo thiết kế

> Trạng thái: `AUDIT → RE-DERIVE → PROPOSAL`, ngày 2026-09-29. Hai tệp 3.0 chỉ là bản đề xuất; chưa cài vào ChatGPT Project, chưa sửa Router, anti-drift hoặc lore. Tên `AetherFire_CI_v3.0_PROPOSAL.md` cố ý không khớp mẫu tự chọn phiên bản của Router 3.2.

Mọi đường dẫn nguồn trong báo cáo này tính từ thư mục gốc `AetherFire Project/`; hai tệp đầu ra nằm trong `AetherFire CI/`.

## 1. Nguồn và giới hạn

| Nguồn đã đọc | Vai trò |
| --- | --- |
| `../ChatGPT Plus+ Era/chatgpt v8.7.txt` | Nền trực tiếp; SHA-256 `C8EA882AD2731A552C0C39D5C1CB00986B3595BA5C2EF5A6342DA55679AAAE2E`. |
| `AetherFire CI/AetherFire_CI_version_v2.6.md` | Đối chứng lịch sử; SHA-256 `CFC10185DEF3D3F027FAC83DA11DF5BCB909192D385FB26CB76C54B5F8987A9C`. Không dùng làm bản mẫu để vá. |
| `Anti-Drift Source/AetherFire_Anti_Drift_Source_Router_v3.2.md` | Hợp đồng route hiện có; SHA-256 `CC46C94E1A0D81C130F9CFE58ABA905A8F39823695F35B7D38315A405AF8C2B4`. |
| Năm overlay active trong `Anti-Drift Source/` | Đã đọc nguyên tệp: Economy v1.1, Modular Concept v1.0, Mortality v1.1, Total War RP v1.1, Worldbuilding Internal Logic v1.1. Chúng là điều khiển phụ thuộc, không là nguồn canon. |
| `AetherFire_Architecture_Audit_2026-09-26/` | Đã đọc `02`, `04`, `06`, `07`, `09`, `10` về breakpoint, kiến trúc, CI/Router vNext, kiểm chứng và quyết định mở. Chúng là audit/proposal, chưa kích hoạt. |
| `AetherFire_Node_Routing_Feasibility_Audit_2026-09-29/` | Đã đọc `01`–`07` và `09`; `08` là glossary. Dùng kết luận về Project runtime, closure, fallback, rủi ro và shadow test; node mode chưa được xác minh trong Project thật. |
| `tests/control-regressions/README.md` | Chín ranh giới thử nghiệm hiện đều `DRAFT`; công cụ chỉ kiểm cấu trúc, không chạy model. |

Đường chạy Project được người dùng nêu và audit ngày 2026-09-29 ghi lại là **CI nằm trực tiếp trong Project instructions → Router điều phối source**. Bản `.md` trong kho chỉ dùng phát triển/đối chiếu. Đã đọc đúng bản 8.7 local; chưa xem được byte của 8.7 hoặc CI đang cài trong Project, và chưa kiểm runtime truy xuất closure. Vì vậy đây là thiết kế, không phải chứng nhận triển khai.

## 2. Dẫn xuất `8.7 → CI 3.0`

ChatGPT 8.7 đã quy định `CONTROL GROUNDING`, `DISCOURSE FIDELITY`, `EPISTEMIC NON-ESCALATION`, giữ giai đoạn thảo luận, kiểm chứng mệnh đề phụ thuộc, cập nhật kết luận theo bằng chứng, diễn giải đủ cơ chế và tiếng Việt dễ hiểu. CI 3.0 kế thừa trực tiếp các điều đó. Nền 8.7 ngăn lời nói lặp lại hoặc một đề xuất hợp lý tự thành sự thật, nhưng không xác định ai có quyền chốt canon AetherFire, nguồn nào hiện hành, cách đọc module đủ bằng chứng, hay overlay nào áp dụng. Đó là phần riêng của Project.

| Control của 2.6 | Phân loại | Lý do và xử lý ở 3.0 |
| --- | --- | --- |
| Output Contract tiếng Việt, cách diễn giải, kiểm nguồn khách quan/thông tin sản phẩm, không suy người dùng từ hiện vật | `GLOBAL-8.7-ALREADY-COVERS` | 8.7 có `OUTPUT CONTRACT`, `CLAIM DEPENDENCY`, `UPDATING AND UNCERTAINTY`, `EXPLANATION`. Dùng 8.7 trực tiếp, không nhân đôi. |
| Control grounding, discourse fidelity, epistemic non-escalation; stage/turn discipline | `GLOBAL-8.7-ALREADY-COVERS` | 8.7 nêu cả ba invariant và thứ tự áp dụng. CI chỉ bổ sung ranh giới canon cụ thể. |
| User authors canon/outcomes; proposal, simulation, inference không tự thành canon | `RE-DERIVE` | 8.7 giữ trạng thái lời nói và mệnh đề nói chung; AetherFire cần quyền chốt canon theo quyết định rõ, đúng phạm vi. |
| Nhãn `CANON`, `USER-PROVIDED STATE`, `UNKNOWN`, `DEFERRED`, `CONFLICTED`, `PROPOSAL`, v.v. | `RE-DERIVE` | Giữ các phân biệt khi ảnh hưởng kết luận; không bắt buộc in bộ nhãn cho mọi câu trả lời. Router xác định trạng thái nguồn, CI ngăn nâng cấp ngầm. |
| Gọi Router 3.2 theo tên, để Router tự tìm CI cao nhất | `REPLACE` | CI thực đã nằm ở Project instructions; Router 4.0 được gọi sau CI và không tìm file CI lúc chạy. Cơ chế repo numeric chỉ còn giá trị lịch sử/tooling nếu được giữ riêng. |
| `PROMPT_ROUTE_ONLY`, route trước khi kết luận và thực thi | `PRESERVE` | Failure vẫn còn: lựa chọn nguồn dựa trên kết luận hình thành trước có thể bỏ nguồn phủ định/issue. Giữ gate ở CI; Router định tuyến cụ thể. |
| Mọi routed file phải đọc trọn; excerpt/hit/summary/memory không là read | `REPLACE` + `RE-DERIVE` | Giữ cấm giả vờ đã đọc; cho phép `FULL_FILE` hoặc `VERIFIED_MODULE_CLOSURE` khi đã thật sự nạp đầy đủ premise bắt buộc. Closure không chứng minh được → mở rộng/full file; source quyết định thiếu → block. |
| Thứ tự nguồn, file/domain inventory, overlay selection/dependency, reconciliation entry | `ROUTER-OWNED` | Router 4.0 chịu discovery, eligibility, closure, mode, reconciliation và overlay routing. CI nêu hợp đồng/ranh giới, không chứa bảng tuyến hay node ID. |
| Source thiếu → `SOURCE_LOAD_BLOCKED`; gap thứ cấp không đổi kết luận → `SOURCE_LOAD_PARTIAL` | `RE-DERIVE` | Failure không được global 8.7 giải ở cấp Project: snippet hoặc metadata không thể thay decisive source. Giữ ranh giới partial rất hẹp. |
| Historical/`SUPERSEDED` không hồi sinh; source mới không tự promotion | `RE-DERIVE` | 8.7 cấm tăng certainty thiếu bằng chứng, nhưng không biết vòng đời canon AetherFire. Giữ quarantine và admission theo quyết định người dùng. |
| Quan hệ có kiểu; interaction/containment, co-occurrence/dependency, genealogy/hierarchy, power/authority | `RE-DERIVE` | Các lỗi này thuộc ontology/quan hệ riêng của Project; giữ các phủ định quyết định, không sao chép danh sách edge cố định của 2.6. |
| Actor knowledge, authority, agency; mô phỏng không chọn endpoint trước | `RE-DERIVE` | Global 8.7 đòi căn cứ nhưng không định nghĩa đường thông tin và chuyển trạng thái của mô phỏng AetherFire. Giữ kernel ngắn; chi tiết ở overlay. |
| Checklist mô phỏng/audit dài, ví dụ `engine/host/lore/story`, guardrail output, real-world reference | `REMOVE` khỏi CI kernel | Mục nào global 8.7 đã xử lý thì kế thừa; độ sâu theo domain nằm ở overlay. Phân biệt canon/ontology cụ thể do source điều khiển. |

`PRESERVE` ở đây chỉ nghĩa là giữ một bất biến có failure độc lập; không xem câu chữ 2.6 là authority. `RE-DERIVE` nghĩa là viết lại từ failure và 8.7, không copy điều khoản cũ. Node routing chỉ tối ưu cách đọc: `module`, `node`, `header`, `routing metadata` không tự có quyền canon.

## 3. Ranh giới trách nhiệm

| Lớp | Sở hữu | Không được làm |
| --- | --- | --- |
| ChatGPT 8.7 | Ngôn ngữ, chức năng lượt nói, bằng chứng, độ chắc chắn, giải thích và cập nhật suy luận nói chung. | Tự quyết authority nguồn/canon AetherFire. |
| AetherFire CI 3.0 | Quyền chốt của người dùng; truth-status invariant; source-read gate; route trước execution; quarantine; typed-relation và mô phỏng ở mức kernel; fallback/block. | Chứa inventory, module ID, bảng route, lore, hoặc tự kích hoạt bằng file repo. |
| Router 4.0 | Khám phá module, xét eligibility/source authority, chọn và nạp closure/file, đối chiếu open/reconciliation, chọn overlay và dependency; ghi phạm vi đọc thực. | Thay CI, chốt canon, nâng quyền module vì header hợp lệ. |
| Anti-drift overlays | Điều khiển phân tích theo scope: economy depth, modular relations, mortality, conflict, world logic; phase đầu đọc nguyên file khi kích hoạt. | Đặt source hierarchy cạnh tranh hoặc tự tạo canon. |
| Source/module | Chứa mệnh đề, phạm vi, trạng thái, bằng chứng và ranh giới nội dung được chấp nhận; metadata hỗ trợ dẫn đường. | Tự nhận authority từ sự tồn tại, tên `CURRENT`, index hoặc node ID. |

Router 4.0 chưa được tạo trong lượt này. Bản 3.0 không tương thích vận hành với bước Router 3.2 tìm CI file và luật full-file tuyệt đối. Hai thay đổi phải được review thành một bộ trước mọi thử nghiệm kích hoạt.

## 4. Bản CI 3.0

Văn bản dán Project instructions nằm ở `AetherFire_CI_v3.0_PROPOSAL.md`. Nó bắt đầu từ contract 8.7 và chỉ thêm các bất biến cấp Project. Không liệt kê faction, `10–80`, node, dependency graph, routing table hoặc schema lore. Nó không được cài vào Project trong lượt này.

## 5. Bản đồ hồi quy và lỗi kiến trúc

| Ca kiểm | Điều khoản 3.0 giữ ranh giới | Kết quả đúng ở mức thiết kế |
| --- | --- | --- |
| Proposal → canon; kết quả simulation → canon | Authority and truth; Interpretation and simulation | Giữ `PROPOSAL`/`HYPOTHETICAL`; chỉ quyết định người dùng đúng scope mới đổi canon. |
| `UNKNOWN` → fact tự dựng; source mới tự promotion | Authority and truth; Route before execution | Giữ unknown/unconfirmed; không lấy plausibility hoặc metadata làm bằng chứng. |
| Historical revival | Authority and truth | Chỉ provenance; không làm fallback/anchor khi current im lặng hay retrieval lỗi. |
| Source quyết định thiếu nhưng model tiếp tục | Route before execution | Mở rộng closure/full file; nếu vẫn thiếu thì `SOURCE_LOAD_BLOCKED`. Secondary gap chỉ `SOURCE_LOAD_PARTIAL` nếu không đổi kết luận giới hạn. |
| Route tự hình thành kết luận | Route before execution | `PROMPT_ROUTE_ONLY` chỉ chọn scope/nguồn/quyền; đối chiếu rồi mới execution. |
| Authority flattening; power → authority | Interpretation and simulation | Giữ trục quyền, khả năng, thông tin, nguồn lực, tài phán và phép dùng riêng. |
| Interaction → containment; co-occurrence → dependency | Interpretation and simulation | Quan hệ phải có kiểu và nguồn; không chuyển cạnh theo sự cùng xuất hiện. |
| Hidden actor knowledge | Interpretation and simulation | Đường thông tin của từng actor là tiền đề; không cấp tri thức người đọc cho actor. |
| Router tìm CI file; CI chứa inventory cố định | Header deployment; Route before execution | CI nằm ở Project instructions; Router không resolve CI từ thư mục; CI không chứa danh sách module. |
| Full-file wording cản kiến trúc module | Route before execution | Thừa nhận `VERIFIED_MODULE_CLOSURE` có điều kiện; snippet/hit không tự thành closure. |
| Node/index hợp lệ nhưng thiếu qualifier, header mới tự tăng authority | Authority and truth; Route before execution | Read gate đòi đủ qualifier/status/owner/dependency đã thực sự đọc; nếu không chứng minh được thì full file hoặc block. |

Chín case hiện có ở `tests/control-regressions/cases/` vẫn `DRAFT`. Bảng này là đối chiếu tĩnh giữa failure và câu chữ proposal, chưa phải kết quả chạy model. Các ca `interaction_containment`, `cooccurrence_dependency`, `power_authority`, `unknown_invention`, `relationship_immunity`, `simulation_canon` có ứng viên tái dùng sau khi người dùng chấp thuận phạm vi thử; không tự nâng chúng lên `ACTIVE`. Các lỗi về Router tìm CI, đóng closure sai và retrieval chỉ trả snippet cần ca shadow riêng khi Router 4.0 tồn tại.

## 6. Phát hiện và quyết định mở

| ID | Loại / trạng thái | Bằng chứng và hệ quả | Xử lý trong proposal |
| --- | --- | --- | --- |
| AF-CI3-01 | `LOGIC / PROPOSED` | Router 3.2 §1–2 tự resolve CI numeric và bắt đọc toàn bộ routed file; runtime Project được người dùng xác định là CI instruction trước Router. Áp nguyên hợp đồng cũ sẽ xung đột với 3.0. | Đặt tên proposal ngoài mẫu resolver; thiết kế Router 4.0 riêng trước activation. |
| AF-CI3-02 | `UNKNOWN / OPEN` | Audit node 2026-09-29 §01–03, §06–07 chưa chứng minh Project backend trả đủ header/index/node/dependency; local hash/parser chỉ kiểm cấu trúc. | `VERIFIED_MODULE_CLOSURE` là điều kiện, mặc định full file cho đến khi Project shadow test xác minh từng scope. |
| AF-CI3-03 | `UNKNOWN / OPEN` | Bản 8.7 trên ổ đĩa đã đọc nhưng không có snapshot byte của global instructions đang cài. | Trước activation, so bản global 8.7 đang cài với SHA ở §1; nếu khác, re-derive delta. |
| AF-CI3-04 | `UNKNOWN / OPEN` | Audit 2026-09-26 §10 còn quyết định về release/snapshot, schema, test và rollback; proposal node 2026-09-29 §09 còn lựa chọn shadow và ngưỡng sai lệch. | Không nhét quyết định vào CI; giữ ở kế hoạch Router/activation riêng. |

Không có phát hiện nào ở đây thay `OPEN/UNKNOWN/DEFERRED/CONFLICTED` của lore. Kiểm chứng giới hạn ở văn bản và cấu trúc local. Bản CI dài 4.661 byte; chưa xác minh giới hạn thực tế của Project instructions, tác dụng trong ChatGPT Project, node retrieval hay semantic parity với full-file. Không commit hoặc push hai tệp proposal này.
