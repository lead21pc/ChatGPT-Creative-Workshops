# Project Feather Core CI

## Bản hiện hành

Cập nhật 2026-10-16: [FTH CI 3.4](FTH_CI_version_v3.4.md) là control local hiện hành, dựa trên ChatGPT 8.9. Các bản CI 3.1, 3.2 và 3.3 đã được chuyển nguyên byte vào [source_archive](source_archive/).

So với CI 3.3, CI 3.4 đổi khai báo nền, hợp đồng giữ nguyên tên/mã/lệnh/trích dẫn phù hợp, xử lý rephrase không đổi nghĩa, và cấm phát hiện tự mở rộng phạm vi hay cấp quyền cho bước tiếp theo. Router 5.0, Pipeline 1.1, source authority và canon contract giữ nguyên.

## Ranh giới

Đây là thư mục điều khiển hành vi cho Project Feather Core, không phải canon, world bible, đầu vào build hoặc bằng chứng lore. AetherFire vẫn là tên quốc gia trong setting. Vị trí thư mục không cấp thẩm quyền nguồn hay nhập nội dung vào canon.

CI giữ quyền quyết định canon của người dùng, trạng thái chưa rõ/xung đột và hợp đồng đọc nguồn. [Source Router và các overlay](../Anti-Drift%20Source/) riêng chịu trách nhiệm định tuyến và suy luận trong phạm vi được khai báo, dưới CI; chúng không được thay CI hoặc tự chốt canon. [Sổ vấn đề hiện hành](../92_OPEN_ISSUES_CURRENT.md) giữ các vấn đề chưa chốt.

## Lưu nguồn cũ

[source_archive](source_archive/) giữ nguyên byte các CI tiền nhiệm, bản compact cũ và tài liệu anti-drift/router cũ trước đây nằm trong thư mục này. Các tài liệu ấy không hoạt động: không dùng làm mặc định, fallback, tiền đề, đầu vào build hoặc mốc đối chiếu hiện hành.

Chỉ đọc lại nguồn lưu trữ khi người dùng chỉ định rõ file hoặc phạm vi lịch sử cần đối chiếu. Quyền đối chiếu không tự khôi phục hiệu lực; việc phục hồi cần quyết định rõ về phạm vi thay thế. Không sửa, gộp hoặc ghi đè tài liệu đã lưu.

## Kiểm chứng

Việc lưu trữ dùng SHA-256 trước/sau để xác nhận không đổi nội dung. Các fixture lịch sử giữ trạng thái DRAFT; đường dẫn archive không khôi phục hiệu lực cho control cũ. Các neo overlay khác vẫn cần được xem xét riêng nếu runner báo lệch.

Kiểm tra cấu trúc, hash và đường dẫn không chứng minh hành vi ChatGPT Project hay việc cài đặt runtime. Lưu trữ không thay canon hoặc tự triển khai control.
