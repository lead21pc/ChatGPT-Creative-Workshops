# Fiction and Worldbuilding Engine (FWE)

FWE là dự án cá nhân, phi thương mại để sáng tác hư cấu, xây dựng thế giới, phát triển lore và concept, khám phá ý tưởng và suy luận về hệ thống hư cấu. FWE được thiết kế như một Project độc lập. Nó không thay Central Hub, không quản lý canon của dự án khác, không phải trợ lý đa năng, công cụ hỗ trợ cảm xúc hay nền tảng công cộng.

Friendly Support Project (FSP) là tiền nhiệm cung cấp một phần di sản hành vi sáng tạo; FWE là sản phẩm mới. Archive FSP giữ vai trò lịch sử và không được dùng làm control khi chạy.

- Bắt đầu ở [Kiến trúc FWE](FWE_ARCHITECTURE.md) để hiểu thẩm quyền, đường sáng tác trực tiếp, nguồn và ranh giới các thành phần.
- Xem [Kế hoạch phát triển](FWE_DEVELOPMENT_PLAN.md) để biết mốc hiện tại, điều kiện đạt và bước được phép giao tiếp theo.

Bộ điều khiển hiện hành trong repository gồm [CI v1.0](controls/FWE_CI_v1.0.md) và [Router v1.0](controls/FWE_ROUTER_v1.0.yaml). Cả hai ở trạng thái `ACTIVE / STATIC PASS / LIVE NOT RUN`. CI gọi đúng Project Source có tên `FWE_ROUTER_v1.0.yaml` tại `ROUTE_ONLY` khi có phụ thuộc cần giải quyết. Chưa cài hay thử truy xuất tệp này trong ChatGPT Project.

Router có bốn tuyến `SOURCE`, `EVIDENCE`, `PROFILE` và `CONTROL`. Phiên bản này chưa có liên kết AIS, quyền và liên kết Profile dành cho FWE, hay kiểm soát chọn lọc được liên kết. [Hồ sơ tiền nhiệm và CI ứng viên](source_archive/) dùng để đối chiếu lịch sử. Kết quả M0–M3 được ghi theo bộ v0.1 trong [kế hoạch phát triển](FWE_DEVELOPMENT_PLAN.md).
