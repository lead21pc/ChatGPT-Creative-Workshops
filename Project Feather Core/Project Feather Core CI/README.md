# Project Feather Core CI

## Bản hiện hành

Cập nhật 2026-10-11: [FTH CI 3.3](FTH_CI_version_v3.3.md) là control local hiện hành; [FTH CI 3.2](FTH_CI_version_v3.2.md) giữ nguyên làm rollback. [AetherFire CI 3.1](AetherFire_CI_version_v3.1.md) giữ tên lịch sử; `source_archive/` tiếp tục giữ các tiền nhiệm byte-exact.

FTH CI 3.3 ghi nền ChatGPT 8.8 và tự chứa các quy tắc cần dùng; nhãn nền là thông tin xuất xứ, không phải lệnh đọc một CI ngoài để áp dụng lúc chạy. Phần ngôn ngữ yêu cầu tiếng Việt phổ thông nhưng giữ nguyên tên riêng trong lore, gồm tên quốc gia và địa danh; không dịch nghĩa đen hoặc tự đặt dạng Việt hóa. Tên được nhận diện từ nguồn/ngữ cảnh, không chỉ từ chữ viết hoa.

## Ứng viên 3.4

[FTH CI 3.4](candidates/FTH_CI_version_v3.4.md) là ứng viên dựa trên ChatGPT 8.9. Trạng thái ứng viên do vị trí file và tài liệu này quản lý; instruction không chứa marker tự chặn hoặc tự xác nhận deployment. Bản này chưa tham gia active resolution, chưa thay CI 3.3 và chưa chứng minh đã được cài trong ChatGPT Project.

So với CI 3.3, ứng viên chỉ đổi khai báo nền, hợp đồng giữ nguyên tên/mã/lệnh/trích dẫn phù hợp, xử lý rephrase không đổi nghĩa, và cấm phát hiện tự mở rộng phạm vi hay cấp quyền cho bước tiếp theo. Router 5.0, Pipeline 1.1, source authority và canon contract giữ nguyên.

## Ranh giới

Đây là thư mục điều khiển hành vi cho Project Feather Core, không phải canon, world bible, đầu vào build hoặc bằng chứng lore. AetherFire vẫn là tên quốc gia trong setting. Vị trí thư mục không cấp thẩm quyền nguồn hay nhập nội dung vào canon.

CI giữ quyền quyết định canon của người dùng, trạng thái chưa rõ/xung đột và hợp đồng đọc nguồn. [Source Router và các overlay](../Anti-Drift%20Source/) riêng chịu trách nhiệm định tuyến và suy luận trong phạm vi được khai báo, dưới CI; chúng không được thay CI hoặc tự chốt canon. [Sổ vấn đề hiện hành](../92_OPEN_ISSUES_CURRENT.md) giữ các vấn đề chưa chốt.

## Lưu nguồn cũ

[source_archive](source_archive/) giữ nguyên byte các CI tiền nhiệm, bản compact cũ và tài liệu anti-drift/router cũ trước đây nằm trong thư mục này. Các tài liệu ấy không hoạt động: không dùng làm mặc định, fallback, tiền đề, đầu vào build hoặc mốc đối chiếu hiện hành.

Chỉ đọc lại nguồn lưu trữ khi người dùng chỉ định rõ file hoặc phạm vi lịch sử cần đối chiếu. Quyền đối chiếu không tự khôi phục hiệu lực; việc phục hồi cần quyết định rõ về phạm vi thay thế. Không sửa, gộp hoặc ghi đè tài liệu đã lưu.

## Kiểm chứng

Việc lưu trữ dùng SHA-256 trước/sau để xác nhận không đổi nội dung. Tham chiếu CI trong glossary và fixture được cập nhật sang FTH CI 3.2; các fixture giữ trạng thái DRAFT. Các neo overlay khác vẫn cần được xem xét riêng nếu runner báo lệch.

Kiểm tra cấu trúc, hash và đường dẫn không chứng minh hành vi ChatGPT Project hay việc cài đặt runtime. Lưu trữ không thay canon hoặc tự triển khai control.
