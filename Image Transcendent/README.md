# Image Transcendent

Project độc lập để phân tích, chuẩn bị và tạo ảnh tham chiếu trong bốn nhóm do CI quy định. Mỗi thao tác tập trung vào một mục tiêu tham chiếu thống nhất hoặc một vùng giới hạn.

| Vị trí cài đặt | Tệp active trong repository |
| --- | --- |
| Project Instructions | [IMAGE_TRANSCENDENT_CI_v1.0.md](IMAGE_TRANSCENDENT_CI_v1.0.md) |
| Project Sources | [IMAGE_SOURCE_ROUTER_v1.0.yaml](IMAGE_SOURCE_ROUTER_v1.0.yaml), [IMAGE_ANTI_PRIOR_v1.0.md](sources/IMAGE_ANTI_PRIOR_v1.0.md), [HUMANOID_CONSTRUCTION_v1.0.md](sources/HUMANOID_CONSTRUCTION_v1.0.md), [HUMANOID_DESIGN_PREFERENCE_v1.0.md](sources/HUMANOID_DESIGN_PREFERENCE_v1.0.md) |

CI điều khiển thao tác và xác lập nguồn cần dùng. Router phân giải đúng tên tệp trong Project Sources. CI gọi công cụ ảnh trực tiếp khi yêu cầu hiện tại cấp quyền và các điều kiện đã đạt.

[Old_Source_Archive](Old_Source_Archive/) giữ lịch sử của CI và module từ kho Central Hub. Chỉ dùng để đối chiếu lịch sử. Kho lưu trữ nằm ngoài Project Sources và ngoài đường phân giải của Router. [Biên nhận di chuyển ban đầu](<../Central Hub/Source_archive/ARCHIVE_RECEIPT.json>) ghi đường dẫn và SHA-256.

ImageT của Central Hub tiếp tục hoạt động như một hệ thống riêng trong giai đoạn chuyển đổi. Việc cho hệ thống đó ngừng hoạt động thuộc tác vụ riêng. Global Native 9.1.1 là nguồn gốc thiết kế của CI. Các tệp trong bảng là toàn bộ cấu hình cần cài cho bản độc lập.

[Đặc tả hồi quy](tests/TEST_CASES.md) ghi kỳ vọng và cách quan sát khi chạy trên Project. Baseline hiện tại đã được dựng ở repository.
