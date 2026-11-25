# Central Hub

## Bộ điều khiển hiện hành

Dùng [CI 2.1](HUB_CI_v2.1.md) làm chỉ dẫn điều khiển. Cung cấp các tệp sau trong tập nguồn được chấp nhận của môi trường chạy, với đường dẫn giữ đúng như khai báo:

- [Router 2.1](HUB_ROUTER_v2.1.yaml), [Architecture 2.2](HUB_ARCHITECTURE_v2.2.md), [Catalog 2.2](HUB_PACKAGE_CATALOG_v2.2.yaml) và [AIS 2.0](tool_pipelines/AIS/AIS_PIPELINE_v2.0.md).
- [Technical](library_modules/Technical/HUB-TECH-ENTRY_v1.2.md), [Authoring](library_modules/Authoring/HUB-AUTH-ENTRY_v1.1.md), [Food](library_modules/Food/HUB-FOOD-ENTRY_v0.4.md).
- [Shopping Entry](library_modules/Shopping/HUB-SHOP-ENTRY_v1.3.md) và [Shopping Search](library_modules/Shopping/HUB-SHOP-SEARCH_v1.2.md).
- [Media Entry](library_modules/Media/HUB-MEDIA-ENTRY_v1.2.md), [Movie](library_modules/Media/HUB-MEDIA-MOVIE_v1.1.md) và [Music](library_modules/Media/HUB-MEDIA-MUSIC_v1.1.md).

Cung cấp một bản đúng cho mỗi nguồn đã ghim và bảo đảm môi trường có thể đọc toàn văn. Đường dẫn thư mục trong kho Git giúp xác định đúng tệp. Router vẫn chọn gói theo từng phần việc. Shopping và Media chỉ đọc các lá cần dùng. AIS xử lý nhu cầu bằng chứng qua Hub.

Bộ này đã thay đổi trong kho Git. Cài đặt và kiểm chứng trên môi trường chạy là bước riêng. Bằng chứng về các bộ trước giữ phạm vi ghi trong [nhật ký](RUNTIME_EVIDENCE_CHANGELOG.md). Xem [cách dùng](<How to use.md>).

## Hồ sơ lịch sử

Các report sau giữ revision cũ và không là hướng dẫn cài successor: [Concept](CONCEPT_DEVELOPMENT_MIGRATION.md), [Authoring](AUTHORING_PROMOTION.md), [Shopping](SHOPPING_PROMOTION.md), [ImageT](IMAGET_LIBRARY_PROMOTION.md), [migration ban đầu](MIGRATION_REPORT.md). [README trước migration](<Source_archive/Canonical namespace migration 2026-11-11/README.md>) và predecessor controls được giữ byte-exact trong [archive receipt](<Source_archive/Canonical namespace migration 2026-11-11/ARCHIVE_RECEIPT.json>). Archive/candidate không là fallback runtime.
