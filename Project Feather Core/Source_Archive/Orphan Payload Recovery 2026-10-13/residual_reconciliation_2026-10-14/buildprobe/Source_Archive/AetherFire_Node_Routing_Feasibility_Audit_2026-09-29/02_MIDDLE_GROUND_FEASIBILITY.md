# 02 — Tính khả thi của phương án trung gian

> **AUDIT / PROPOSAL**. Các nhãn dưới đây áp cho từng thành phần, không phải điểm số tổng thể. `UNVERIFIED_RUNTIME` nghĩa là cấu trúc repo không thể xác nhận cơ chế truy xuất trong ChatGPT Project.

| Thành phần | Kết luận | Bằng chứng và điều kiện |
| --- | --- | --- |
| Markdown là bề mặt điều khiển runtime | **FEASIBLE** | CI/Router/overlay hiện là prose Markdown; Project instructions và Project sources được người dùng xác nhận đã cài. Không cần service để giữ đường `FULL_FILE`. |
| `MANDATORY HEADER + LOCAL ROUTING INDEX + semantic node` trong cùng current-domain file | **FEASIBLE_WITH_CONDITIONS** | Cấu trúc này đọc được bằng mắt và parse được local, nhưng phải sinh từ builder/copy có kiểm soát, đánh dấu span ổn định, review boundary và giữ toàn bộ canon bytes/meaning. Các priority late-file ở `10`, `30` bác bỏ giả định “header hiện tại vài dòng là đủ”. |
| `REQUIRES` là dependency semantic bắt buộc duy nhất ở phase đầu | **FEASIBLE_WITH_CONDITIONS** | Có ích khi một conclusion thiếu tiền đề quyết định ở node/file khác; cần human review. Mention, keyword, related section hay authority boundary không tự tạo `REQUIRES`. Nếu nhiều edge làm closure gần full file, dùng `FULL_FILE`. Chưa thấy failure buộc primitive thứ hai. |
| `NODE_OR_FULL` giữ `FULL_FILE` làm baseline | **FEASIBLE_WITH_CONDITIONS** | Cần sửa contract CI dòng 33 và Router dòng 81, route table và pre-response gate; phải định nghĩa điều gì là “đã đọc” ở node mode. Fallback phải resolve được file thật; thiếu file vẫn block. |
| Backend Project chọn chính xác node/range và giữ marker | **UNVERIFIED_RUNTIME** | Repo và OpenAI Projects documentation không bảo đảm truy xuất chính xác đoạn. Cần blind/shadow comparison trong Project thật; nếu không chứng minh được, chỉ `FULL_FILE`. |
| `00` / `92` `FULL_FILE` | **FEASIBLE** | Cả hai ngắn và chứa control có tính toàn cục; node hóa không chứng minh ROI đủ bù rủi ro. |
| `60` / active overlays `FULL_FILE` ở phase đầu | **FEASIBLE** | `60` nhỏ; overlay là control contract với điều kiện kích hoạt và phụ thuộc. Chưa có bằng chứng bottleneck nghiêm trọng. |
| `91` `RECORD_OR_FULL` | **FEASIBLE_WITH_CONDITIONS** | `AF-CX` có ID, nhưng addenda ở đầu, priority và comparison tables phía cuối tạo closure không chỉ một record. Chỉ dùng cho query hẹp sau review; audit domain/provenance/conflict rộng vẫn full file. |
| `90` history-cluster routing | **NOT_NEEDED_YET** | File lớn nhưng status mixed: `DESIGN HISTORY`, `CURRENT CANON`, `UNDER CONSIDERATION`, `PARTIALLY SUPERSEDED` đan xen; giảm read mà lẫn authority là thiệt hại lớn hơn. Cần tách eligibility/status từng cluster trước pilot. |
| JSON/YAML runtime registry, node database, graph engine, retrieval service | **REJECT** cho phase đầu | Không có failure đã chứng minh mà Markdown + fallback không xử lý; tăng mặt đồng bộ và độ lệch package. Local derived data để validate là chuyện khác. |
| Parser/index local để kiểm tra cấu trúc | **FEASIBLE_WITH_CONDITIONS** | Chỉ là dụng cụ build/validate trên bản sao; không được biến thành runtime prerequisite. Phải kiểm stale mapping bằng anchor/content hash hoặc span check, không chỉ kiểm ID tồn tại. |
| Tự sinh `REQUIRES` từ text similarity/cross-reference | **REJECT** | Mention không chứng minh decisive premise. Nhãn `REVIEW_REQUIRED` đúng hơn khi semantic chưa được người đọc duyệt. |
| Tiết kiệm token/latency trong Project | **UNVERIFIED_RUNTIME** | Cần đo trên cùng prompt/source generation/CI/Router/model tương đương; local byte giảm không chứng minh backend đọc ít hơn. |

## Kết luận có điều kiện

Phương án `Markdown local index + semantic nodes + REQUIRES + full-file fallback` **khả thi như một đường thử nghiệm có fail-safe**, chưa đủ bằng chứng để kích hoạt. Nó có thể nằm trong chính các Project source files hiện có, giữ CI trong instruction setting, giữ overlay/`00`/`92` full-file và không cần thêm source file runtime. Điều kiện quyết định là sửa rõ CI/Router contract, sinh cấu trúc bền qua builder, review closure bằng người và chạy shadow tests Project thật. Nếu Project không chứng minh được node retrieval hoặc hành vi tương đương, quyết định vận hành là `FULL_FILE` cho class/file đó.

## Điều không được hiểu quá mức

- `FEASIBLE` về Markdown structure không phải xác nhận backend có API đọc section range.
- `REQUIRES` không phải dependency graph canon hay tuyên bố sở hữu authority; nó chỉ ràng buộc premise tối thiểu của câu trả lời hẹp.
- `92` là hook cho unresolved routing, không phải bộ chỉ mục đầy đủ của mọi ngoại lệ trong corpus.
- Việc giữ 90/91 ở phase sau không làm phase 1 phụ thuộc chúng về runtime; những query cần chúng vẫn dùng full-file theo gate hiện hành.
