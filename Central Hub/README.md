# Central Hub

## Bộ active trong repository

[CI 1.3](HUB_CI_v1.3.md), [Router 1.2](HUB_ROUTER_v1.2.yaml), [Architecture 1.21](HUB_ARCHITECTURE_v1.21.md) và [root Catalog 1.21](HUB_PACKAGE_CATALOG_v1.21.yaml) là bộ pin hiện hành. Catalog là nguồn định danh, revision, applicability và binding của bảy package.

- Technical, Authoring và Food là singleton. Concept giữ Entry/Catalog và lá theo nhu cầu.
- AIS dùng một [Project Source](tool_pipelines/AIS/AIS_PIPELINE_v1.3.md). Shopping Entry tự chọn Search tùy nhu cầu.
- ImageT dùng Entry, Controller, Anti-Prior và Ready Gate cho sinh ảnh. ANALYZE không dùng Ready Gate. Catalog và hai lá humanoid chỉ đọc khi cần. [Inventory kiểm cài đặt ImageT](tool_pipelines/ImageT/IMAGET_INSTALL_INTEGRITY.yaml) không phải Project Source hoặc Library control.
- [Context Snapshot](shared_resources/CONTEXT_SNAPSHOT.md) và [hợp đồng Profile](shared_resources/HUB-USER-PROFILE-CONTRACT_v1.0.yaml) là Project Sources dùng theo nhu cầu. [Profile](shared_resources/USER_PROFILE.md) có bốn object dữ liệu riêng do người dùng quản lý.

## Layout Library và cài đặt

Root duy nhất là `Central Hub Config`. Sáu folder package trực tiếp là Technical, Concept Development, Authoring, ImageT, Shopping và Food. Mỗi artifact Library trong `library_modules/<package>/` đặt trực tiếp trong folder package tương ứng. `Shared/` chứa object dữ liệu Profile riêng, người dùng tạo thủ công từ hợp đồng hiện hành. Các template repository chỉ là mẫu. Không dùng thư mục chức năng cấp hai.

Khi được phép cài, đồng bộ cả bộ Project Instructions, Project Sources và các binding Library đã đổi. Đối chiếu exact ID/role/status/version và toàn văn, kiểm không có match trùng, giữ đúng một binding đang dùng và kiểm từng đường bị tác động. Rollback theo Git và bộ binding tương thích đã ghi nhận. Các báo cáo cũ phía dưới phục vụ đối chiếu lịch sử.

Người dùng đã xác nhận khả năng phân giải, đọc và dùng nội dung trong folder Library lồng nhau ở runtime đã thử. [Changelog](RUNTIME_EVIDENCE_CHANGELOG.md) ghi phạm vi. Lần refactor repository này chưa cài bộ mới. [Cách dùng](<How to use.md>) giữ cú pháp và hành vi đang áp dụng.

## Hồ sơ lịch sử

Các report sau giữ revision cũ và không là hướng dẫn cài successor: [Concept](CONCEPT_DEVELOPMENT_MIGRATION.md), [Authoring](AUTHORING_PROMOTION.md), [Shopping](SHOPPING_PROMOTION.md), [ImageT](IMAGET_LIBRARY_PROMOTION.md), [migration ban đầu](MIGRATION_REPORT.md). [README trước migration](<Source_archive/Canonical namespace migration 2026-11-11/README.md>) và predecessor controls được giữ byte-exact trong [archive receipt](<Source_archive/Canonical namespace migration 2026-11-11/ARCHIVE_RECEIPT.json>). Archive/candidate không là fallback runtime.
