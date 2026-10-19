# Central Hub

Trạng thái repository: **Central Hub v1.1 ACTIVE**. REPOSITORY ACTIVE != PROJECT DEPLOYED. Việc stage/commit/push repository không upload module, sửa Project hoặc xác nhận deployment.

[Hub CI v1.1](HUB_CI_v1.1.md) kế thừa ngữ nghĩa ChatGPT v9.0; [Hub Router v1.1](HUB_ROUTER_v1.1.yaml), [shared architecture v1.0](HUB_ARCHITECTURE_v1.0.md) và [root package Catalog v1.0](HUB_PACKAGE_CATALOG_v1.0.yaml) là bộ active. Router chọn package set có phạm vi; chat/support/viết thông thường có thể dùng baseline NONE. Module không tự kích hoạt nhau hoặc công cụ.

AIS là pipeline nghiên cứu; [ImageT controller v1.1](tool_pipelines/ImageT/IMAGE_CONTROLLER_v1.1.md) xây dựng thao tác/prompt và xác minh ảnh; [Ready Gate v1.0](tool_pipelines/ImageT/READY_GATE_v1.0.md) là control active bắt buộc, có version/hash riêng trong manifest ImageT, duyệt đúng snapshot cho một call. AIS/ImageT cùng dependency nội bộ giữ nguyên. Preference humanoid vẫn thử nghiệm, inactive, chỉ nhận full text trực tiếp khi được chọn riêng cho một operation.

Trong deployment v1.1, chỉ Hub CI ở Project Instructions; Router/Architecture/Catalog và AIS/ImageT core ở Project Sources. TECHNICAL/CREATIVE/BRAINSTORM dùng Library / `Central Hub Config`, mỗi package một binding. Đường dẫn repository không thay nguồn runtime; tests, kế hoạch và evidence records không phải runtime control.

[Báo cáo migration](MIGRATION_REPORT.md) ghi nguồn, mapping, hashes và bằng chứng kiểm tra. [Các ca Hub](tests/HUB_ROUTE_TEST_CASES.md) là đặc tả, không chứng minh hành vi model. [Source_archive](Source_archive/README.md) chỉ giữ lịch sử; không fallback hoặc tự rollback.

[Trial tích hợp v1.1](candidates/integration_v1.1/HUB_V1_1_LIVE_INTEGRATION_RESULT.md) có **LIVE INTEGRATION PARTIAL** theo báo cáo người dùng: I01–I07/I09–I10 PASS; I08 UNVERIFIABLE, không có lỗi chức năng tích hợp còn mở được báo. Kết quả đó kiểm TECHNICAL Library và CREATIVE/BRAINSTORM legacy, không chứng minh hai Library binding mới. Bộ [promotion đã chấp nhận](candidates/promotion_v1.1/HUB_V1_1_PROMOTION_PLAN.md) giữ làm snapshot trước migration, không là bộ active hiện tại.

TECHNICAL giữ `REASONING_PROFILE`, ACTIVE/1.0 và exact Library object đã kiểm. [CREATIVE](library_modules/HUB-DOM-CREATIVE_v1.0.md) giữ `DOMAIN_CONTROL`; [BRAINSTORM](library_modules/HUB-CAP-BRAINSTORM_v1.0.md) giữ `CAPABILITY`. Hai artifact mới ACTIVE/1.0 trong repository, thân giữ nguyên; locator **UNRESOLVED**, live verification **NOT_PERFORMED** trước upload. Router chặn phần phụ thuộc, không dùng source cũ làm fallback. Xem [kế hoạch upload, cài đặt và S01–S04](HUB_LIBRARY_SINGLETON_MIGRATION.md).

[CI v1.0](<Source_archive/Central Hub legacy v1.0/HUB_CI_v1.0.md>), [Router v1.0](<Source_archive/Central Hub legacy v1.0/HUB_ROUTER_v1.0.yaml>), cùng các Project Source TECHNICAL/CREATIVE/BRAINSTORM cũ được lưu byte-exact dưới `Source_archive/Central Hub legacy v1.0/` phục vụ rollback/history; không còn ở vùng active. Chúng không là active route của v1.1. Candidate/design/trial cũ vẫn là bản ghi riêng; tên file hoặc sự hiện diện không cấp activation. Không tạo active-version registry khác.

Receipt của lần lưu này: [HUB_LEGACY_ARCHIVE_RECEIPT_2026-10-19.json](Source_archive/HUB_LEGACY_ARCHIVE_RECEIPT_2026-10-19.json). Candidate snapshots/evidence giữ nguyên để kiểm lịch sử, không runtime control.
