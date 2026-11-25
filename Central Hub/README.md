# Central Hub

## Bộ active trong repository

[CI 2.1](HUB_CI_v2.1.md), [Router 2.0](HUB_ROUTER_v2.0.yaml), [Architecture 2.1](HUB_ARCHITECTURE_v2.1.md) và [root Catalog 2.1](HUB_PACKAGE_CATALOG_v2.1.yaml) là bộ pin hiện hành. Catalog là nguồn định danh, revision, applicability và binding của năm package.

- Technical, Authoring và Food là singleton. Media Entry chọn Movie và Music độc lập theo phần việc.
- [AIS 2.0](tool_pipelines/AIS/AIS_PIPELINE_v2.0.md) là Project Source core dùng theo nhu cầu bằng chứng. Shopping Entry tự chọn Search tùy nhu cầu.
- [Context Snapshot](shared_resources/CONTEXT_SNAPSHOT.md) và [hợp đồng Profile 2.0](shared_resources/HUB-USER-PROFILE-CONTRACT_v2.0.yaml) được đọc theo nhu cầu. [Profile](shared_resources/USER_PROFILE.md) giữ bốn object riêng. Hub có thể dùng trường diễn đạt trong PREFERENCES khi viết trực tiếp và đáp ứng đúng mục đích, quyền và nhu cầu.

## Layout Library và cài đặt

Root duy nhất là `Central Hub Config`. Năm thư mục package trực tiếp là Technical, Authoring, Shopping, Food và Media. Mỗi artifact Library trong `library_modules/<package>/` đặt trực tiếp trong folder package tương ứng. `Shared/` chứa bốn object Profile riêng, người dùng tạo thủ công từ hợp đồng hiện hành. Các template repository chỉ là mẫu. Không dùng thư mục chức năng cấp hai.

Khi được phép cài, đồng bộ cả bộ Project Instructions, Project Sources và các binding Library đã đổi. Đối chiếu exact ID/role/status/version và toàn văn, kiểm không có match trùng, giữ đúng một binding đang dùng và kiểm từng đường bị tác động. Rollback theo Git và bộ binding tương thích đã ghi nhận. Các báo cáo cũ phía dưới phục vụ đối chiếu lịch sử.

Người dùng đã xác nhận khả năng phân giải, đọc và dùng nội dung trong folder Library lồng nhau ở runtime đã thử. [Changelog](RUNTIME_EVIDENCE_CHANGELOG.md) ghi phạm vi. Ngày 2026-11-24, người dùng báo đã cài và đang chạy bộ CI 2.1, Router 2.0, Architecture 2.0 và Catalog 2.0. Việc xác minh độc lập bộ đã cài chưa được chạy. Bộ hiện hành trong repository dùng Architecture và Catalog 2.1. Việc cài đặt và kiểm chứng live cho bộ kế nhiệm chưa được thực hiện. [Cách dùng](<How to use.md>) giữ cú pháp và hành vi đang áp dụng.

## Hồ sơ lịch sử

Các report sau giữ revision cũ và không là hướng dẫn cài successor: [Concept](CONCEPT_DEVELOPMENT_MIGRATION.md), [Authoring](AUTHORING_PROMOTION.md), [Shopping](SHOPPING_PROMOTION.md), [ImageT](IMAGET_LIBRARY_PROMOTION.md), [migration ban đầu](MIGRATION_REPORT.md). [README trước migration](<Source_archive/Canonical namespace migration 2026-11-11/README.md>) và predecessor controls được giữ byte-exact trong [archive receipt](<Source_archive/Canonical namespace migration 2026-11-11/ARCHIVE_RECEIPT.json>). Archive/candidate không là fallback runtime.
