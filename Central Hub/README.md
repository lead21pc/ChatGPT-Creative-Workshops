# Central Hub

## Bộ active trong repository

[CI 2.1](HUB_CI_v2.1.md), [Router 2.0](HUB_ROUTER_v2.0.yaml), [Architecture 2.0](HUB_ARCHITECTURE_v2.0.md) và [root Catalog 2.0](HUB_PACKAGE_CATALOG_v2.0.yaml) là bộ pin hiện hành. Catalog là nguồn định danh, revision, applicability và binding của sáu package.

- Technical, Authoring và Food là singleton. Media Entry chọn Movie và Music độc lập theo phần việc.
- [AIS 2.0](tool_pipelines/AIS/AIS_PIPELINE_v2.0.md) là Project Source core dùng theo nhu cầu bằng chứng. Shopping Entry tự chọn Search tùy nhu cầu.
- ImageT dùng Entry, Controller và Anti-Prior. Controller kiểm tra thẩm quyền rồi giới hạn ImageT vào bốn nhóm tham chiếu gồm nhận dạng/tài liệu, nhân vật, vật phẩm/trang bị và công trình/vùng môi trường. Mỗi yêu cầu cần một mục tiêu tham chiếu thống nhất hoặc một vùng giới hạn. Controller tiếp tục kiểm tra độ trung thành của prompt và mức sẵn sàng trước khi gửi. Yêu cầu sinh ảnh trực tiếp đủ điều kiện cho phép tối đa một lần gọi công cụ. Yêu cầu xem trước hiển thị bản chuẩn bị rồi dừng. ANALYZE chỉ kiểm tra mục tiêu hoặc vùng đã chỉ rõ trong ảnh nguồn. Catalog và hai lá humanoid chỉ đọc khi cần. [Inventory kiểm cài đặt ImageT](tool_pipelines/ImageT/IMAGET_INSTALL_INTEGRITY.yaml) không phải Project Source hoặc Library control.
- [Context Snapshot](shared_resources/CONTEXT_SNAPSHOT.md) và [hợp đồng Profile 2.0](shared_resources/HUB-USER-PROFILE-CONTRACT_v2.0.yaml) được đọc theo nhu cầu. [Profile](shared_resources/USER_PROFILE.md) giữ bốn object riêng. Hub có thể dùng trường diễn đạt trong PREFERENCES khi viết trực tiếp và đáp ứng đúng mục đích, quyền và nhu cầu.

## Layout Library và cài đặt

Root duy nhất là `Central Hub Config`. Sáu folder package trực tiếp là Technical, Authoring, ImageT, Shopping, Food và Media. Mỗi artifact Library trong `library_modules/<package>/` đặt trực tiếp trong folder package tương ứng. `Shared/` chứa bốn object Profile riêng, người dùng tạo thủ công từ hợp đồng hiện hành. Các template repository chỉ là mẫu. Không dùng thư mục chức năng cấp hai.

Khi được phép cài, đồng bộ cả bộ Project Instructions, Project Sources và các binding Library đã đổi. Đối chiếu exact ID/role/status/version và toàn văn, kiểm không có match trùng, giữ đúng một binding đang dùng và kiểm từng đường bị tác động. Rollback theo Git và bộ binding tương thích đã ghi nhận. Các báo cáo cũ phía dưới phục vụ đối chiếu lịch sử.

Người dùng đã xác nhận khả năng phân giải, đọc và dùng nội dung trong folder Library lồng nhau ở runtime đã thử. [Changelog](RUNTIME_EVIDENCE_CHANGELOG.md) ghi phạm vi. Bộ hiện hành là CI 2.1, Router 2.0, Architecture 2.0 và Catalog 2.0. Người dùng xác nhận ngày 2026-11-24 rằng bộ điều khiển hiện hành đã được cài và đang chạy. INSTALLED: USER-REPORTED. LIVE ACTIVE: USER-REPORTED. INDEPENDENT LIVE VERIFICATION: NOT RUN. Báo cáo này không xác nhận mọi probe hoặc hồi quy đã đạt. [Cách dùng](<How to use.md>) giữ cú pháp và hành vi đang áp dụng.

## Hồ sơ lịch sử

Các report sau giữ revision cũ và không là hướng dẫn cài successor: [Concept](CONCEPT_DEVELOPMENT_MIGRATION.md), [Authoring](AUTHORING_PROMOTION.md), [Shopping](SHOPPING_PROMOTION.md), [ImageT](IMAGET_LIBRARY_PROMOTION.md), [migration ban đầu](MIGRATION_REPORT.md). [README trước migration](<Source_archive/Canonical namespace migration 2026-11-11/README.md>) và predecessor controls được giữ byte-exact trong [archive receipt](<Source_archive/Canonical namespace migration 2026-11-11/ARCHIVE_RECEIPT.json>). Archive/candidate không là fallback runtime.
