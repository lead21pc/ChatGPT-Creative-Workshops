# Central Hub

## Bộ active trong repository

[Architecture 1.19](HUB_ARCHITECTURE_v1.19.md), [root Catalog 1.19](HUB_PACKAGE_CATALOG_v1.19.yaml), [Router 1.1](HUB_ROUTER_v1.1.yaml) và [CI 1.2](HUB_CI_v1.2.md) là bộ active trong repository. Sáu package giữ nguyên; identity của 26 Library controls chuyển sang namespace package-oriented theo [hồ sơ migration 2026-11-11](NAMESPACE_MIGRATION.md). Phase 1 cập nhật Concept Entry để dùng hệ quả của tiền đề hiện có xác định phần cần phát triển.

**REPOSITORY ACTIVE != PROJECT DEPLOYED.** Project/Library deployment chưa thực hiện; successor Library retrieval/live behavior NOT_RUN. Khả năng folder Library lồng nhau NOT_VERIFIED; có thể cài các object successor trực tiếp dưới sole root `Central Hub Config`. Path repository không là runtime locator. Catalog/manifest và exact identity/FULL_FILE/body checks tiếp tục sở hữu binding, dependency và verification; thư mục không tạo quan hệ runtime.

| Package ID | Entrypoint | Revision | Binding |
| --- | --- | --- | --- |
| HUB-PKG-TECHNICAL | HUB-TECH-ENTRY | 1.1 | LIBRARY_MODULE |
| HUB-PKG-CONCEPT-DEVELOPMENT | HUB-CON-ENTRY | 1.7 | LIBRARY_MODULE |
| HUB-PKG-AUTHORING | HUB-AUTH-ENTRY | 0.9 | LIBRARY_MODULE |
| HUB-PKG-AIS | HUB-PIPE-AIS | 1.2 | LEGACY_PROJECT_SOURCE |
| HUB-PKG-IMAGET | HUB-IMAGET-ENTRY | 1.4 | LIBRARY_MODULE |
| HUB-PKG-SHOPPING | HUB-SHOP-ENTRY | 1.1 | LIBRARY_MODULE |

Concept dùng local Catalog 1.6 và nhóm General/Anti Drift; ImageT dùng Catalog 0.2, manifest 2.4.0 cùng Core/Anti Drift/Humanoid; Shopping dùng Catalog 1.1. Technical và Authoring vẫn singleton. Xem inventory có thẩm quyền trong Catalog/manifest; không chọn module theo prefix hoặc thư mục.

[User Profile](shared_resources/USER_PROFILE.md) tiếp tục là `HUB-USER-PROFILE` schema 1.0 do người dùng sở hữu, model read-only, bốn object riêng, default deny và need-before-read. Shopping là consumer hiện hành, không là owner. Context Snapshot là artifact dữ liệu độc lập; không tạo package/module hoặc lưu tự động.

[Cách dùng](<How to use.md>) giữ syntax/behavior hiện hành. [Runtime evidence changelog](RUNTIME_EVIDENCE_CHANGELOG.md) giữ continuity đúng scope/revision; không chuyển PASS cũ sang successor namespace. CI, AIS, User Profile và legacy ImageT rollback stack giữ nguyên byte.

## Hồ sơ lịch sử

Các report sau giữ revision cũ và không là hướng dẫn cài successor: [Concept](CONCEPT_DEVELOPMENT_MIGRATION.md), [Authoring](AUTHORING_PROMOTION.md), [Shopping](SHOPPING_PROMOTION.md), [ImageT](IMAGET_LIBRARY_PROMOTION.md), [migration ban đầu](MIGRATION_REPORT.md). [README trước migration](<Source_archive/Canonical namespace migration 2026-11-11/README.md>) và predecessor controls được giữ byte-exact trong [archive receipt](<Source_archive/Canonical namespace migration 2026-11-11/ARCHIVE_RECEIPT.json>). Archive/candidate không là fallback runtime.
