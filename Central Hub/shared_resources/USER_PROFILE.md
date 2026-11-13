# User Profile dùng chung — hợp đồng 1.1, schema payload 1.0

`HUB-USER-PROFILE` là tài nguyên dữ liệu **ACTIVE trong repository**, do người dùng sở hữu. Hợp đồng công khai: [HUB-USER-PROFILE-CONTRACT_v1.1.yaml](HUB-USER-PROFILE-CONTRACT_v1.1.yaml). Đây là schema/access contract; không chứa dữ liệu cá nhân thật và không tạo package mới.

`PROFILE MUTATION BY MODEL: NEVER`. `customizable: true` chỉ cho phép người dùng tự chỉnh thủ công. Quyền sửa repository, chỉ dẫn trong chat hoặc dữ liệu mới không cho phép model sửa Profile. Nếu thấy dữ liệu có thể cũ, model chỉ báo chênh lệch hoặc đề xuất sửa để người dùng tự thực hiện.

## Năm object riêng để tự tạo trong Library

Tự tạo **năm object riêng** trong `Central Hub Config/Shared/`. Sao chép toàn bộ payload của từng tệp dưới đây vào object tương ứng rồi tự điền giá trị riêng tư. Không tải một tệp gộp nhiều object; `FULL_FILE` luôn chỉ đọc một object. Các bản mẫu công khai được giữ trống; không đưa bản có giá trị thật vào repository hoặc commit.

| Tên gợi ý cho object riêng | Payload trống chính xác | Nội dung |
| --- | --- | --- |
| HUB-USER-PROFILE / GENERAL | [GENERAL](HUB-USER-PROFILE-GENERAL-TEMPLATE_v1.0.yaml) | Bối cảnh chung do người dùng khai báo |
| HUB-USER-PROFILE / PREFERENCES | [PREFERENCES](HUB-USER-PROFILE-PREFERENCES-TEMPLATE_v1.0.yaml) | Sở thích; không tự thành yêu cầu bắt buộc |
| HUB-USER-PROFILE / DIETARY_CONSTRAINTS | [DIETARY_CONSTRAINTS](HUB-USER-PROFILE-DIETARY_CONSTRAINTS-TEMPLATE_v1.0.yaml) | Ràng buộc ăn uống do người dùng khai báo |
| HUB-USER-PROFILE / HEALTH_CONTEXT | [HEALTH_CONTEXT](HUB-USER-PROFILE-HEALTH_CONTEXT-TEMPLATE_v1.0.yaml) | Bối cảnh sức khỏe khai báo, schema nông |
| HUB-USER-PROFILE / WRITING_PROFILE | [WRITING_PROFILE](HUB-USER-PROFILE-WRITING_PROFILE-TEMPLATE_v1.0.yaml) | Cách diễn đạt do bạn khai báo |

Để tự điền `WRITING_PROFILE`, thay `profile_text: null` bằng `profile_text: |-` rồi dán nguyên nội dung `USER_WRITING_PROFILE v1` vào khối văn bản, thụt thêm hai dấu cách so với dòng `profile_text`. Bốn object hiện có tiếp tục dùng payload schema 1.0.

Tên hiển thị chỉ giúp tìm; identity phải khớp `resource_id`, `object_id`, `schema_version: '1.0'` trong toàn bộ payload. Các field đều tùy chọn và nhận `null`; `null`/field thiếu là UNKNOWN. Danh sách trống chỉ nói chưa cung cấp mục nào, không chứng minh không có dị ứng hoặc bệnh lý. Chỉ tự điền điều đã khai báo, không nhờ model suy diễn rồi ghi lại. Object không cần header module, Package ID hoặc runtime role.

Khi cài, dùng bộ Project Sources và binding consumer trong [README](../README.md).
Cài hợp đồng Profile vào Project Sources. Tạo từng object giá trị riêng trong folder Shared.
Không dùng tệp hướng dẫn hoặc template repository thay cho object runtime.

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
| HUB_DIRECT_WRITING | WRITING_PROFILE | preserve_user_expression |

Không có khai báo phù hợp thì từ chối. Có quyền nhưng không cần cho tác vụ thì không đọc. Với consumer package, Hub chọn package trước. Với thao tác viết trực tiếp, Hub xác lập định danh từ phần việc hiện tại. Hub kiểm định danh, quyền và nhu cầu trước khi truy xuất đúng object và đọc FULL_FILE. Shopping và Food có quyền theo bảng. Health vẫn là FUTURE / NOT REGISTERED. Food luôn xét yếu tố sức khỏe khi khuyến nghị. Chỉ yêu cầu HEALTH_CONTEXT khi dữ kiện sức khỏe có thể đổi một quyết định cụ thể, input hiện tại chưa đủ và object có thể giải quyết điểm thiếu. Làm rõ tiêu chí mơ hồ trước khi đọc.

Chỉ thao tác viết trực tiếp của Hub được cấp quyền đọc `WRITING_PROFILE`. Shopping và Food không được cấp quyền này. Hub chỉ đọc khi tác vụ cần giữ cách diễn đạt cá nhân và còn một quyết định diễn đạt quan trọng mà dữ liệu này có thể giúp giải quyết. Viết trung tính, dịch đơn giản hoặc yêu cầu đã nêu đủ cách diễn đạt thì bỏ qua. Profile chỉ hỗ trợ cách diễn đạt nội dung có căn cứ. Khi thiếu object hoặc không xác minh được, Hub tiếp tục phần viết có đủ dữ kiện và nêu giới hạn nếu phần cá nhân hóa phụ thuộc vào Profile.

Profile cung cấp dữ liệu; consumer tự diễn giải trong hợp đồng chuyên môn. Chỉ dẫn tường minh hiện tại thắng giá trị lưu cho tác vụ hiện tại; không cập nhật object lưu. Thiếu Profile chỉ để phần cá nhân hóa phụ thuộc ở trạng thái chưa giải quyết. Phần Food hoặc Shopping có đủ dữ kiện độc lập vẫn tiếp tục. Profile và Context Snapshot độc lập, không tự chuyển đổi hoặc lưu chat.

## Chuẩn bị kiểm thử live thủ công

Chỉ dùng giá trị tổng hợp được đánh dấu rõ nếu muốn thử trước khi tự điền dữ liệu thật. Không yêu cầu model tạo hoặc chỉnh giá trị thật. Quan sát trace truy xuất nếu nền tảng cung cấp; nếu không quan sát được việc không đọc object khác, ghi UNVERIFIABLE thay vì PASS.

1. Yêu cầu Shopping chỉ so giá: kỳ vọng không đọc Profile khi không cần cá nhân hóa.
2. Yêu cầu so sản phẩm theo sở thích đã khai báo: chỉ đọc PREFERENCES với purpose phù hợp; không đọc HEALTH_CONTEXT.
3. Yêu cầu kiểm tương thích thành phần theo ràng buộc ăn uống: chỉ đọc DIETARY_CONSTRAINTS nếu đó là dữ liệu đủ dùng. Tác vụ thật sự cần bối cảnh sức khỏe mới có thể đọc HEALTH_CONTEXT.
4. Kiểm root, resource/object/schema và FULL_FILE; khi có nhiều object cùng identity hoặc coverage không đủ, kỳ vọng UNRESOLVED, không chọn bản đầu/mới nhất.
5. Thử thiếu object cần thiết: phần cá nhân hóa phụ thuộc chưa giải quyết, phần so sánh đủ chứng cứ vẫn tiếp tục. Field thiếu là UNKNOWN.
6. Cho chỉ dẫn hiện tại khác sở thích lưu: chỉ dẫn hiện tại chi phối tác vụ; tự so payload trước/sau để xác nhận object không bị sửa. Quyền ghi file chung không thay đổi cấm sửa Profile.

7. Yêu cầu Hub viết trực tiếp theo giọng cá nhân, với một quyết định diễn đạt chưa được nguồn hoặc chỉ dẫn xác định. Dùng payload tổng hợp. Kỳ vọng chỉ đọc đúng WRITING_PROFILE trong Shared. Lặp lại với bản dịch đơn giản hoặc chỉ dẫn giọng viết đã đủ và kiểm Hub bỏ qua đọc.
8. Dùng một ca WRITING_PROFILE thiếu hoặc có identity trùng. Kỳ vọng phần viết độc lập vẫn tiếp tục, phần cá nhân hóa phụ thuộc chưa được xác lập. Tự đối chiếu payload để xác nhận model không sửa dữ liệu.

**STATIC PASS != LIVE BEHAVIOR PROVEN.** Tác vụ chỉ triển khai repository: không cài Library/Project, không tạo Profile thật, không kiểm chứng truy xuất live hoặc cơ chế bảo vệ riêng tư của nền tảng. Baseline PASS cũ giữ đúng scope/revision cũ.
