# Hoàn thiện AetherFire CI 3.0

> Kết quả: `AetherFire CI/AetherFire_CI_version_v3.0.md` là bản điều khiển local hoàn chỉnh để người dùng duyệt và đưa vào ChatGPT Project instructions. Việc tạo file trong kho không kích hoạt nó trong Project.

Các đường dẫn nguồn dưới đây tính từ thư mục gốc `AetherFire Project/`.

## Nguồn đã đối chiếu

| Nguồn | SHA-256 / vai trò |
| --- | --- |
| `../ChatGPT Plus+ Era/chatgpt v8.7.txt` | `C8EA882AD2731A552C0C39D5C1CB00986B3595BA5C2EF5A6342DA55679AAAE2E`; đọc trực tiếp. Trùng hash 8.7 đã ghi khi tạo proposal, nên không có delta nền cần dẫn xuất lại. |
| `AetherFire CI/AetherFire_CI_v3.0_PROPOSAL.md` | `8557442A7B018C467F4D2C34F36C8F8339E65E0F6018509363264182511EE68A`; nguồn thiết kế trực tiếp. Tệp thực nằm trong `AetherFire CI/`, không nằm trong thư mục báo cáo này. |
| `AetherFire CI/AetherFire_CI_v3.0_DESIGN_REPORT.md` | `C4282AB32BC3B747955C6AD57636A5167ECA924427E7D67F888BF776D10EE1D3`; căn cứ phân loại control và hồi quy. |
| `AetherFire CI/AetherFire_CI_version_v2.6.md` | `CFC10185DEF3D3F027FAC83DA11DF5BCB909192D385FB26CB76C54B5F8987A9C`; chỉ đối chứng hồi quy/provenance. |
| `AetherFire_Router_4_Proposal/ROUTER_4_ARCHITECTURE.md` | `2E28B398D07354757F67EE268EECFFE46F1B0FFFF6738CC79CB34851D400F2BA`; chỉ kiểm ranh giới giao tiếp, chưa là Router đang chạy. |
| File CI 3.0 cuối | `30060D4FD7D851D2CFAFD893A3F73FFABDA19918C7A8FF118470809DE2686B46`; 5.043 byte. |

## Từ bản thiết kế sang file cuối

- Bỏ phần đầu tự mô tả là bản nháp, lời nhắc triển khai và bình luận dành cho người phát triển. File cuối chỉ chứa lệnh điều khiển có thể copy vào Project instructions.
- Thay tên phiên bản Router cố định bằng `the active installed AetherFire Source Router`. Quan hệ quyền hạn vẫn rõ: Router ở dưới CI, quyết định định tuyến nguồn/overlay, không quyết định canon. Thêm chốt tương thích: nếu Router đang cài không thực hiện được hợp đồng đọc và quyền nguồn của CI 3.0 thì chặn kết luận canon phụ thuộc.
- Giữ hai dạng đọc `FULL_FILE` và `VERIFIED_MODULE_CLOSURE`; closure phải chứa toàn bộ tiền đề quyết định và đã thực sự được nạp. Lỗi route dẫn tới mở rộng/full file, rồi `SOURCE_LOAD_BLOCKED` nếu nguồn quyết định vẫn thiếu. `SOURCE_LOAD_PARTIAL` chỉ dành cho thiếu nguồn thứ cấp không thể đổi kết luận có giới hạn.
- Giữ quyền canon của người dùng, các trạng thái mở, cách ly nguồn lịch sử, cấm tự tăng quyền nguồn mới/metadata, route trước execution, các phân biệt quan hệ và quyền hạn, đường thông tin actor, mô phỏng không chọn trước kết quả. Anti-drift được nạp trọn file sau đối chiếu nguồn trong giai đoạn module ban đầu.
- Để quy tắc hội thoại, bằng chứng, tiếng Việt và diễn giải chung cho ChatGPT 8.7. Không đưa danh sách module, faction, file, node ID, catalog, đồ thị phụ thuộc hay schema lore vào CI.

## Kiểm hồi quy

Kiểm tĩnh trên file cuối cho thấy các chốt sau có câu điều khiển tương ứng:

| Failure cần chặn | Chốt trong CI 3.0 |
| --- | --- |
| Gợi ý/nháp hoặc mô phỏng → canon; nguồn mới → tự lên canon | Quyết định rõ của người dùng trong phạm vi nêu; nguồn mới và metadata không tự cấp quyền. |
| `UNKNOWN` → sự kiện tự dựng; `DEFERRED`/`CONFLICTED` tự đóng | Giữ trạng thái; thiếu tiền đề quyết định thì rẽ nhánh có giả định rõ hoặc chặn. |
| Nguồn lịch sử hồi sinh, kể cả khi retrieval lỗi | Chỉ provenance/so sánh; cấm baseline, fallback, analogy anchor. |
| Route → kết luận sớm | `PROMPT_ROUTE_ONLY` chỉ chọn phạm vi, ứng viên và bằng chứng; kết luận sau nạp nguồn, đối chiếu và controls. |
| Nguồn quyết định thiếu → vẫn tiếp tục; route lỗi → dùng memory | Mở rộng closure/full file; nếu vẫn thiếu thì `SOURCE_LOAD_BLOCKED`; cấm trí nhớ, nguồn gần giống và liên kết tự dựng. |
| Interaction → containment; co-occurrence → dependency; power → authority | Bốn bất đẳng thức quan hệ/quyền hạn được giữ trực tiếp trong kernel. |
| Actor có tri thức ẩn; mechanism chọn endpoint | Đường tiếp cận thông tin bắt buộc; mechanism chỉ đặt điều kiện; nhánh/mô phỏng không đổi canon. |
| Module/header → tự có authority | Metadata chỉ dẫn đường; Router phải xác minh quyền nguồn và tiền đề thực đọc. |
| Router tìm CI file; source tree cố định; mọi file luôn full-read | CI đứng trước Router đang cài; không có resolver CI/file inventory trong CI; closure được xác minh là cách đọc hợp lệ thứ hai. |

Kiểm từ khóa không thấy `PROPOSAL`, `PENDING`, tên Router cố định, hay tham chiếu CI 2.x trong file cuối. Đây là kiểm văn bản và đối chiếu hợp đồng, chưa phải phép thử hành vi của ChatGPT Project. Các ca hồi quy hiện có vẫn `DRAFT`; không đổi vòng đời của chúng.

## Còn cần kiểm khi cài vào Project

Chưa xác minh byte của ChatGPT 8.7 và CI trong phần cài đặt Project, giới hạn ký tự của Project instructions, khả năng backend nạp đủ một `VERIFIED_MODULE_CLOSURE`, hoặc phản hồi thực của model. Router 4.0 hiện chỉ là bản đề xuất, nên phải có bản Router tương thích và phép thử trên Project trước khi kích hoạt CI 3.0.

Router 3.2 trong kho có quy tắc chọn tên phiên bản cao nhất; tên file chính thức `AetherFire_CI_version_v3.0.md` có thể được công cụ dựa vào quy tắc đó chọn khi quét kho. Điều này **không** chứng minh Project instructions đã đổi, và Router 3.2 không đáp ứng hợp đồng closure mới. Không dùng cặp 3.0/3.2 để tuyên bố runtime đạt.

Không sửa Router, anti-drift, `00–92`, lore, module, catalog hoặc builder; không upload, commit hay push.
