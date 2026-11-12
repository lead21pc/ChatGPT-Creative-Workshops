# User Profile dùng chung — schema 1.0

`HUB-USER-PROFILE` là tài nguyên dữ liệu **ACTIVE trong repository**, do người dùng sở hữu. Hợp đồng công khai: [HUB-USER-PROFILE-CONTRACT_v1.0.yaml](HUB-USER-PROFILE-CONTRACT_v1.0.yaml). Đây là schema/access contract; không chứa dữ liệu cá nhân thật và không tạo package mới.

`PROFILE MUTATION BY MODEL: NEVER`. `customizable: true` chỉ cho phép người dùng tự chỉnh thủ công. Quyền sửa repository, chỉ dẫn trong chat hoặc dữ liệu mới không cho phép model sửa Profile. Nếu thấy dữ liệu có thể cũ, model chỉ báo chênh lệch hoặc đề xuất sửa để người dùng tự thực hiện.

## Bốn object riêng để tự tạo trong Library

Tự tạo **bốn object riêng** dưới đúng root `Central Hub Config`. Sao chép toàn bộ payload của từng tệp dưới đây vào object tương ứng rồi tự điền giá trị riêng tư. Không tải một tệp gộp bốn object; `FULL_FILE` luôn chỉ đọc một object. Các bản mẫu công khai được giữ trống; không đưa bản có giá trị thật vào repository hoặc commit.

| Tên gợi ý cho object riêng | Payload trống chính xác | Nội dung |
| --- | --- | --- |
| HUB-USER-PROFILE / GENERAL | [GENERAL](HUB-USER-PROFILE-GENERAL-TEMPLATE_v1.0.yaml) | Bối cảnh chung do người dùng khai báo |
| HUB-USER-PROFILE / PREFERENCES | [PREFERENCES](HUB-USER-PROFILE-PREFERENCES-TEMPLATE_v1.0.yaml) | Sở thích; không tự thành yêu cầu bắt buộc |
| HUB-USER-PROFILE / DIETARY_CONSTRAINTS | [DIETARY_CONSTRAINTS](HUB-USER-PROFILE-DIETARY_CONSTRAINTS-TEMPLATE_v1.0.yaml) | Ràng buộc ăn uống do người dùng khai báo |
| HUB-USER-PROFILE / HEALTH_CONTEXT | [HEALTH_CONTEXT](HUB-USER-PROFILE-HEALTH_CONTEXT-TEMPLATE_v1.0.yaml) | Bối cảnh sức khỏe khai báo, schema nông |

Tên hiển thị chỉ giúp tìm; identity phải khớp `resource_id`, `object_id`, `schema_version: '1.0'` trong toàn bộ payload. Các field đều tùy chọn và nhận `null`; `null`/field thiếu là UNKNOWN. Danh sách trống chỉ nói chưa cung cấp mục nào, không chứng minh không có dị ứng hoặc bệnh lý. Chỉ tự điền điều đã khai báo, không nhờ model suy diễn rồi ghi lại. Object không cần header module, Package ID hoặc runtime role.

Để dùng hợp đồng mới, tự cập nhật Project Sources với Architecture 1.20, Catalog 1.20, Router 1.1 đã đổi pins và hợp đồng Profile 1.0; dùng Shopping core 1.1 và cài Food Entry 0.1 trong Library để dùng từng consumer tương ứng. CI 1.2 không đổi. Việc cài đặt này chưa được thực hiện trong tác vụ. Không cài tệp hướng dẫn này hoặc tệp mẫu công khai làm nguồn giá trị runtime thay thế.

## Quyền đọc hiện hành

| Consumer | Object | Purpose được khai báo |
| --- | --- | --- |
| HUB-PKG-SHOPPING | GENERAL | purchase_filtering |
| HUB-PKG-SHOPPING | PREFERENCES | purchase_filtering, product_comparison |
| HUB-PKG-SHOPPING | DIETARY_CONSTRAINTS | product_compatibility |
| HUB-PKG-SHOPPING | HEALTH_CONTEXT | product_compatibility |
| HUB-PKG-FOOD | GENERAL | food_context |
| HUB-PKG-FOOD | PREFERENCES | food_selection |
| HUB-PKG-FOOD | DIETARY_CONSTRAINTS | food_compatibility |
| HUB-PKG-FOOD | HEALTH_CONTEXT | food_compatibility |

Không có khai báo phù hợp thì từ chối. Có quyền nhưng không cần cho tác vụ thì không đọc. Hub chọn package trước, consumer xác định object/purpose cần thiết, Hub kiểm access và nhu cầu, rồi mới truy xuất đúng object và đọc FULL_FILE. Shopping và Food có quyền theo bảng. Health vẫn là FUTURE / NOT REGISTERED. Food luôn xét yếu tố sức khỏe khi khuyến nghị. Chỉ yêu cầu HEALTH_CONTEXT khi dữ kiện sức khỏe có thể đổi một quyết định cụ thể, input hiện tại chưa đủ và object có thể giải quyết điểm thiếu. Làm rõ tiêu chí mơ hồ trước khi đọc.

Profile cung cấp dữ liệu; consumer tự diễn giải trong hợp đồng chuyên môn. Chỉ dẫn tường minh hiện tại thắng giá trị lưu cho tác vụ hiện tại; không cập nhật object lưu. Thiếu Profile chỉ để phần cá nhân hóa phụ thuộc ở trạng thái chưa giải quyết. Phần Food hoặc Shopping có đủ dữ kiện độc lập vẫn tiếp tục. Profile và Context Snapshot độc lập, không tự chuyển đổi hoặc lưu chat.

## Chuẩn bị kiểm thử live thủ công

Chỉ dùng giá trị tổng hợp được đánh dấu rõ nếu muốn thử trước khi tự điền dữ liệu thật. Không yêu cầu model tạo hoặc chỉnh giá trị thật. Quan sát trace truy xuất nếu nền tảng cung cấp; nếu không quan sát được việc không đọc object khác, ghi UNVERIFIABLE thay vì PASS.

1. Yêu cầu Shopping chỉ so giá: kỳ vọng không đọc Profile khi không cần cá nhân hóa.
2. Yêu cầu so sản phẩm theo sở thích đã khai báo: chỉ đọc PREFERENCES với purpose phù hợp; không đọc HEALTH_CONTEXT.
3. Yêu cầu kiểm tương thích thành phần theo ràng buộc ăn uống: chỉ đọc DIETARY_CONSTRAINTS nếu đó là dữ liệu đủ dùng. Tác vụ thật sự cần bối cảnh sức khỏe mới có thể đọc HEALTH_CONTEXT.
4. Kiểm root, resource/object/schema và FULL_FILE; khi có nhiều object cùng identity hoặc coverage không đủ, kỳ vọng UNRESOLVED, không chọn bản đầu/mới nhất.
5. Thử thiếu object cần thiết: phần cá nhân hóa phụ thuộc chưa giải quyết, phần so sánh đủ chứng cứ vẫn tiếp tục. Field thiếu là UNKNOWN.
6. Cho chỉ dẫn hiện tại khác sở thích lưu: chỉ dẫn hiện tại chi phối tác vụ; tự so payload trước/sau để xác nhận object không bị sửa. Quyền ghi file chung không thay đổi cấm sửa Profile.

**STATIC PASS != LIVE BEHAVIOR PROVEN.** Tác vụ chỉ triển khai repository: không cài Library/Project, không tạo Profile thật, không kiểm chứng truy xuất live hoặc cơ chế bảo vệ riêng tư của nền tảng. Baseline PASS cũ giữ đúng scope/revision cũ.
