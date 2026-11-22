# User Profile dùng chung

[Hợp đồng 2.0](HUB-USER-PROFILE-CONTRACT_v2.0.yaml) quy định quyền đọc và schema payload 1.0. Người dùng quản lý giá trị riêng và tự sửa thủ công. Model có quyền đọc theo phạm vi đã khai báo, kiểm nhu cầu trước khi truy xuất và không ghi lại giá trị.

Tự tạo bốn object riêng trong thư mục `Central Hub Config/Shared` từ mẫu rỗng tương ứng:

| Object | Mẫu | Dữ liệu |
| --- | --- | --- |
| GENERAL | [Mẫu](HUB-USER-PROFILE-GENERAL-TEMPLATE_v1.0.yaml) | Bối cảnh do người dùng khai báo |
| PREFERENCES | [Mẫu](HUB-USER-PROFILE-PREFERENCES-TEMPLATE_v1.0.yaml) | Sở thích và xu hướng |
| DIETARY_CONSTRAINTS | [Mẫu](HUB-USER-PROFILE-DIETARY_CONSTRAINTS-TEMPLATE_v1.0.yaml) | Ràng buộc ăn uống |
| HEALTH_CONTEXT | [Mẫu](HUB-USER-PROFILE-HEALTH_CONTEXT-TEMPLATE_v1.0.yaml) | Bối cảnh sức khỏe do người dùng khai báo |

Payload 1.0 đang có vẫn hợp lệ. Nếu muốn giữ sở thích diễn đạt dùng lại, tự thêm `expression_preference` dưới `data` trong PREFERENCES, chỉ điền xu hướng đã xác nhận. Các giá trị viết cũ chưa phân loại giữ trạng thái UNKNOWN. Kiểm đúng resource ID, object ID và schema trong toàn bộ object. Giá trị null hoặc vắng mặt là UNKNOWN. Chỉ lưu mẫu rỗng hoặc fixture tổng hợp trong repository.

Shopping và Food dùng quyền theo từng object và mục đích trong hợp đồng. Hub viết trực tiếp có thể dùng riêng `expression_preference` khi yêu cầu và nguồn còn để ngỏ một lựa chọn diễn đạt quan trọng. Chỉ dẫn hiện tại chi phối tác vụ hiện tại và dữ liệu lưu giữ nguyên. Media và Authoring dùng đầu vào được giao theo phạm vi của chúng.

## Kiểm thử thủ công sau khi cài

Dùng payload tổng hợp. Đối chiếu dấu vết nếu runtime hiển thị và giữ UNKNOWN khi thiếu căn cứ.

1. So giá đã cung cấp, rồi so tương thích với thành phần. Lượt đầu bỏ qua Profile khi không cần, lượt sau chỉ đọc object đủ dùng.
2. Yêu cầu Hub viết trực tiếp theo cách diễn đạt cá nhân với một lựa chọn còn bỏ ngỏ, rồi lặp lại khi đã ghi rõ cách diễn đạt ưu tiên. Lượt đầu chỉ dùng trường được phép, lượt sau áp dụng chỉ dẫn hiện tại.
3. Thử thiếu hoặc trùng object đúng định danh. Phần cá nhân hóa phụ thuộc giữ chưa giải quyết và phần đủ căn cứ tiếp tục.
4. Đối chiếu payload trước và sau các lượt để kiểm không có thay đổi.
