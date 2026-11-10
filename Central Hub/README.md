# Central Hub

## User Profile dùng chung — 2026-11-11

`HUB-USER-PROFILE` schema 1.0 là **ACTIVE shared data resource trong repository**, do người dùng tự quản lý; không là package hoặc control module. Architecture/Catalog 1.17 kế nhiệm 1.16; Router 1.1 chỉ đổi exact pins; CI 1.2 giữ nguyên và vẫn có sáu root package. Shopping 1.0 chỉ thêm giao diện đọc tùy nhu cầu, không đổi phần khuyến nghị/so sánh hiện có. Food chưa có trong working tree; Health chưa đăng ký. Candidate 0.1 giữ riêng làm lịch sử, không là nguồn runtime.

Bốn object GENERAL, PREFERENCES, DIETARY_CONSTRAINTS và HEALTH_CONTEXT có ranh giới đọc riêng. Chọn package và kiểm consumer/object/purpose + nhu cầu trước khi đọc FULL_FILE đúng object. `customizable: true` chỉ cho người dùng tự chỉnh; **PROFILE MUTATION BY MODEL: NEVER**, kể cả có quyền ghi repository. Xem [hợp đồng, bốn payload trống và cách tự cài/kiểm thử](shared_resources/USER_PROFILE.md).

**PROJECT / LIBRARY DEPLOYMENT: NOT_PERFORMED; LIVE PROFILE RETRIEVAL / SHOPPING PROFILE USE: NOT_RUN.** Không tạo giá trị cá nhân thật. Predecessor Architecture/Catalog 1.16 và Router trước đổi pin được giữ nguyên byte trong `Source_archive/`, với `USER_PROFILE_ARCHIVE_RECEIPT_2026-11-11.json`. Bằng chứng live cũ giữ đúng scope/revision, không chuyển sang delta Profile.

## Context Snapshot — 2026-11-10

Architecture/Catalog 1.16 là **ACTIVE PRODUCTION CONTRACT trong repository**. Context Snapshot là artifact dữ liệu có phạm vi: một ID gắn với một payload cố định, giữ riêng nguồn gốc và trạng thái, provenance theo từng mệnh đề, ràng buộc và vấn đề chưa giải quyết. Tạo bằng yêu cầu tự nhiên tường minh; không có lệnh `/PACKAGE`, package/capability mới hoặc lưu tự động. CI 1.2, Router logic và hành vi các package giữ nguyên; Router 1.1 chỉ đổi exact pins. Xem [hợp đồng](HUB_ARCHITECTURE_v1.17.md#13-shared-immutable-context-snapshot-artifact), [cách dùng](<How to use.md#context-snapshot>) và [đặc tả kiểm chứng](tests/CONTEXT_SNAPSHOT_TEST_CASES.md).

**PROJECT DEPLOYMENT: NOT_PERFORMED; LIVE VERIFICATION / REAL-CONTEXT STRESS: NOT_RUN.** ID không bảo đảm có thể truy xuất ở chat khác; chỉ tái dùng khi payload thực sự có sẵn và đọc được. Baseline live PASS giữ đúng scope/revision cũ. Architecture/Catalog 1.15 được lưu nguyên byte trong `Source_archive/Context Snapshot contract 2026-11-10/`; archive không là fallback runtime.

## ImageT Library — 2026-11-09

ImageT đã được promotion trong repository: `HUB-PKG-IMAGET → LIBRARY_MODULE → HUB-PIPE-IMAGET 1.3`, local Catalog 0.1 và 10 artifact trong `library_modules/`. Controller kiểm mục tiêu thị giác được giao và độ trung thành với yêu cầu; preference chỉ áp khi được chọn riêng cho operation hiện tại. **LIBRARY/PROJECT DEPLOYMENT: NOT_PERFORMED; L01–L06: NOT RUN.** Legacy v1.2 giữ nguyên byte để rollback có chủ đích, không tự fallback. Xem [artifact, thứ tự cài, smoke test và rollback](IMAGET_LIBRARY_PROMOTION.md).

## Naming — 2026-11-09

Naming 1.0 được thêm trong repository với Concept core/catalog 1.4 và Architecture/root Catalog 1.13; CI/Router giữ 1.2/1.1. Dùng `/NAME ... #` và preset tùy chọn P1/P2/P3. Hướng dẫn thực hành: [How to use.md](<How to use.md>). Đây là tài liệu người dùng, không là Library runtime Config. Naming không có mode kéo dài hoặc duyệt bắt buộc mọi yêu cầu; dừng qua lượt cần span mới.

**IMPLEMENTED IN REPOSITORY; PROJECT/LIBRARY DEPLOYMENT: NOT_PERFORMED; REAL-CONTEXT STRESS: NOT RUN.** Baseline PASS trước đây giữ đúng scope, không chứng minh Naming mới. [Bộ stress thật](tests/NAMING_REAL_CONTEXT_STRESS.md) đang chờ chạy. Predecessor được lưu byte-exact trong `Source_archive/Naming 1.0 integration 2026-11-09/`. Các bản ghi có ngày cũ bên dưới giữ phạm vi lịch sử.

## Bản ghi CI 1.2 trước Naming — 2026-11-09

[Hub CI v1.2](HUB_CI_v1.2.md) ACTIVE trong repository; nội dung giữ nguyên byte từ correction local ở commit `4ff4b34` (bỏ emotional-support default, làm correction trực tiếp theo current turn). Router vẫn 1.1, Architecture/Catalog vẫn 1.12, các package/pipeline không đổi. CI v1.2 chưa deploy hoặc live-test; baseline PASS trước correction giữ nguyên phạm vi. Xem [runtime evidence](RUNTIME_EVIDENCE_CHANGELOG.md) và CF01–CF08 trong [regression spec](tests/HUB_ROUTE_TEST_CASES.md).

Bản v1.1 đã correction được lưu byte-exact tại `Source_archive/Hub CI 1.2 promotion 2026-11-09/`; snapshot v1.1 trước correction vẫn giữ nguyên cho provenance. Archive không là fallback runtime.

## Bản ghi — 2026-11-08

Production baseline CI/Router 1.1, Architecture/Catalog 1.11, Concept core/catalog 1.2, Authoring 0.7, năm control production, Shopping 1.0 và AIS/ImageT: **USER_CONFIRMED_INSTALLED_AND_LIVE / USER_CONFIRMED_LIVE_PASS** theo xác nhận người dùng trong tác vụ này. Không phải Codex tái hiện độc lập; không suy ngày chạy, kết quả từng ca, FULL_FILE/duplicate receipts hoặc Library IDs/locator chưa được cung cấp.

Correction hiện hành: Architecture/Catalog 1.12, Authoring 0.8, Concept core/catalog 1.3, MCA 1.2; CI/Router giữ 1.1. **IMPLEMENTED / STATICALLY VERIFIED; LIVE VERIFICATION OF NEW DELTA: NOT RUN**. Baseline PASS không bị reset. Tác vụ này không deploy.

Contributor Authoring đã retire: mọi `+ CREATIVE` / `+ BRAINSTORM` không activation và không được bỏ suffix để chạy plain Authoring. Creative/Brainstorm vẫn là exact Concept operations độc lập. Kết quả được cung cấp hoặc referenced rõ là ordinary source/context theo Authoring, không phải contributor. Clarification phải hướng dẫn exact call/span mới; không giữ mode, target, preset hay isolation ngầm.

Xem [runtime evidence](RUNTIME_EVIDENCE_CHANGELOG.md). Các đoạn có ngày/revision cũ dưới đây giữ provenance lịch sử; status hiện hành nằm ở mục này.


## Bộ runtime hiện hành

Trạng thái repository: **Central Hub CI v1.2 / Router v1.1 với Architecture/Catalog v1.17, Authoring 0.8 và Shopping 1.0 ACTIVE**. ImageT Library controller 1.3 giữ Open Gate nội bộ; legacy 1.2 chỉ còn là rollback baseline. REPOSITORY ACTIVE != PROJECT DEPLOYED. Việc stage/commit/push repository không upload module, sửa Project hoặc xác nhận deployment.

[Hub CI v1.2](HUB_CI_v1.2.md) kế thừa ngữ nghĩa ChatGPT v9.0 cùng correction đã được chấp thuận; [Hub Router v1.1](HUB_ROUTER_v1.1.yaml), [shared architecture v1.17](HUB_ARCHITECTURE_v1.17.md) và [root package Catalog v1.17](HUB_PACKAGE_CATALOG_v1.17.yaml) là bộ active trong repository. Router chọn package set có phạm vi; chat/support/viết thông thường có thể dùng baseline NONE. Module không tự kích hoạt nhau hoặc công cụ.

AIS chính thức trong repository dùng [pipeline v1.2](tool_pipelines/AIS/AIS_PIPELINE_v1.2.md) và [router v1.3](tool_pipelines/AIS/AIS_ROUTER_v1.3.yaml); revision mới chưa deploy/live-test. Baseline pipeline 1.1/router 1.2 giữ **USER_CONFIRMED_INSTALLED_AND_LIVE** trong phạm vi cũ. AIS dùng vòng tìm/đọc nguồn trong Chat để trả chứng cứ cho phần việc Hub đã giao; THOROUGH/EXTENSIVE tăng yêu cầu chứng cứ, không tự gọi Deep Research hoặc Work. Không có bộ chọn executor, quota hay chuyển Chat sang Work trong AIS. Xem [báo cáo promotion và chỉnh sửa](tool_pipelines/AIS/AIS_PROMOTION_REPORT.md) và [ca hồi quy](tool_pipelines/AIS/tests/RESEARCH_CORE_TEST_CASES.md). [ImageT Library entrypoint 1.3](library_modules/HUB-PIPE-IMAGET_v1.3.md) dẫn tới core do manifest ImageT sở hữu. Controller 1.3 giữ Open Gate, Prompt Gate và visible verification; Ready Gate 1.1 duyệt exact ImageT-controlled snapshot cho một call. Humanoid preference 0.2 có sẵn nhưng cần explicit current-operation authority riêng. Legacy controller/router/manifest và dependencies không đổi byte, chỉ dùng khi rollback binding được chỉ định. Xem [hồ sơ promotion](IMAGET_LIBRARY_PROMOTION.md).

Trong topology hiện hành, chỉ Hub CI 1.2 ở Project Instructions; Router 1.1 pin Architecture/Catalog 1.17; AIS core ở Project Sources, ImageT ở Library / `Central Hub Config`. Shopping là package thứ sáu. [Authoring 0.8](library_modules/HUB-CAP-AUTHORING_v0.8.md) là singleton CAPABILITY trong Library / `Central Hub Config`, giữ exact single-target và P1/P2/P3; mọi plus-suffix form đã bị loại bỏ; thêm suffix `ISOLATED` hoặc `P<n> ISOLATED` theo từng lượt để giới hạn task material được nhận. Đường single-target không suffix giữ cách dùng context trước đây; contributor đã loại bỏ. Người dùng xác nhận v0.7 trên bộ Architecture/Catalog 1.9 đã chạy live thành công ngày 2026-11-05: **USER_CONFIRMED_LIVE_PASS** trong phạm vi được báo; Codex chưa trực tiếp tái hiện và exact Library identity/FULL_FILE receipts chưa được cung cấp; điều đó không phủ định baseline production live. Candidate/API-local live evidence giữ phạm vi riêng. Xem [promotion, bằng chứng và rollback](AUTHORING_PROMOTION.md).

[Shopping 1.0](SHOPPING_PROMOTION.md) dùng core, Catalog cục bộ và thủ tục Search trong Library / `Central Hub Config`. Hub chọn AIS độc lập khi cần chứng cứ bên ngoài. Shopping production: **USER_CONFIRMED_INSTALLED_AND_LIVE / USER_CONFIRMED_LIVE_PASS**; Codex chưa tái hiện độc lập.

Hồ sơ lịch sử Authoring 0.6: [M4 preset strategies](candidates/authoring_m4/README.md) đã hoàn tất promotion 0.6 trong repository. [Bản ghi L1/L2](candidates/authoring_m4/AUTHORING_M4_TESTS.md) ghi USER_CONFIRMED_LIVE_PASS trên candidate được cung cấp trực tiếp: P2 CONTRACT bảo toàn quan hệ và đường không chọn preset vẫn hoạt động. Đây là bằng chứng hành vi candidate, chưa chứng minh routing của Hub active hoặc deployment. Authoring 0.5 và các nguồn tiền nhiệm được lưu nguyên byte để rollback có chủ đích; không có fallback tự động.

[Báo cáo migration](MIGRATION_REPORT.md) ghi nguồn, mapping, hashes và bằng chứng kiểm tra. [Runtime evidence changelog](RUNTIME_EVIDENCE_CHANGELOG.md) giữ continuity của các kết quả runtime đã được xác nhận cho maintenance/provenance; nó không là runtime control, Project Source, Library object hay nguồn activation. [Các ca Hub](tests/HUB_ROUTE_TEST_CASES.md) là đặc tả, không chứng minh hành vi model. [Source_archive](Source_archive/README.md) chỉ giữ lịch sử; không fallback hoặc tự rollback.

[Trial tích hợp v1.1](candidates/integration_v1.1/HUB_V1_1_LIVE_INTEGRATION_RESULT.md) có **LIVE INTEGRATION PARTIAL** theo báo cáo người dùng: I01–I07/I09–I10 PASS; I08 UNVERIFIABLE, không có lỗi chức năng tích hợp còn mở được báo. Kết quả đó kiểm TECHNICAL Library và CREATIVE/BRAINSTORM legacy, không chứng minh hai Library binding mới. Bộ [promotion đã chấp nhận](candidates/promotion_v1.1/HUB_V1_1_PROMOTION_PLAN.md) giữ làm snapshot trước migration, không là bộ active hiện tại.

TECHNICAL giữ `REASONING_PROFILE`, ACTIVE/1.0 và binding cũ. `HUB-PKG-CONCEPT-DEVELOPMENT` dùng [shared core 1.5](library_modules/HUB-DOM-CONCEPT-DEVELOPMENT_v1.5.md) / DOMAIN_CONTROL và [local catalog 1.5](library_modules/HUB-CATALOG-CONCEPT-DEVELOPMENT_v1.5.yaml). [CREATIVE 1.1](library_modules/HUB-DOM-CREATIVE_v1.1.md) giữ DOMAIN_CONTROL cho realization trong premise được giao; [BRAINSTORM 1.1](library_modules/HUB-CAP-BRAINSTORM_v1.1.md) giữ CAPABILITY cho biến đổi premise/phân nhánh. Core chỉ chọn operation leaf cho span user-directive hợp lệ `/CREATIVE ... #`, `/DEBATE ... #`, `/BRAINSTORM ... #` hoặc `/NAME ... #`; không chọn theo semantic fit hay cụm từ tự nhiên. [DEBATE 1.0](library_modules/HUB-CAP-DEBATE_v1.0.md) kiểm proposal bằng phản biện có hệ quả, cập nhật và ngừng lặp các phản biện đã giải quyết. Core vẫn xử lý phần việc thông thường không có trigger. Production baseline Concept 1.2 và các control đã được người dùng xác nhận cài/test live; core/catalog 1.3 và MCA 1.2 là correction delta chưa live. Bằng chứng bốn object/smoke cũ vẫn giữ phạm vi riêng. Root cập nhật exact binding và cue package-level `/AD`; Root không giữ leaf inventory/trigger chi tiết. Smoke inspection hậu migration do ChatGPT quan sát/người dùng cung cấp đã xác nhận bốn object đúng trong `Central Hub Config`, đọc `FULL_FILE`, khớp identity/content và byte-exact với repository; không thấy duplicate khác cho bốn identity trong scoped listing đã kiểm. `locator` và `library_version_id` vẫn chưa biết; không repository/Project Source fallback. Ngày 2026-10-27, người dùng xác nhận một integrated Central Hub runtime smoke đã PASS với exact Hub/AIS/TECHNICAL/Concept/Brainstorm/Creative revisions; PASS này không chứng minh từng internal retrieval trace, toàn bộ C01-C12 hoặc global Hub behavior.

miniConcept được retire như standalone runtime owner trong repository; phần riêng về consistency/causal reasoning/audit và institution có điều kiện đã port vào core, phần global để Hub CI sở hữu. Hai CI miniConcept cũ được lưu nguyên byte làm historical source, không là dependency của Hub. Library installation của bốn object mới đã được quan sát và kiểm chứng ở mức nêu trên; integrated runtime path đã có user-confirmed PASS đúng scope trong changelog. Việc retire miniConcept Project thật và receipts riêng cho mọi retrieval trace/toàn bộ C01-C12 chưa được cung cấp; production baseline deployment/live đã được người dùng xác nhận ở mục trạng thái hiện hành. Xem [mapping, current evidence, C01–C12 và thứ tự cài/rollback](CONCEPT_DEVELOPMENT_MIGRATION.md). Stack singleton trước migration và hướng dẫn cũ nằm tại [archive của migration](<Source_archive/Concept development migration 2026-10-26/>), không phải active source.

[CI v1.0](<Source_archive/Central Hub legacy v1.0/HUB_CI_v1.0.md>), [Router v1.0](<Source_archive/Central Hub legacy v1.0/HUB_ROUTER_v1.0.yaml>), cùng các Project Source TECHNICAL/CREATIVE/BRAINSTORM cũ được lưu byte-exact dưới `Source_archive/Central Hub legacy v1.0/` phục vụ rollback/history; không còn ở vùng active. Chúng không là active route của v1.1. Candidate/design/trial cũ vẫn là bản ghi riêng; tên file hoặc sự hiện diện không cấp activation. Không tạo active-version registry khác.

Receipt của lần lưu này: [HUB_LEGACY_ARCHIVE_RECEIPT_2026-10-19.json](Source_archive/HUB_LEGACY_ARCHIVE_RECEIPT_2026-10-19.json). Candidate snapshots/evidence giữ nguyên để kiểm lịch sử, không runtime control.

Quy tắc ngôn ngữ control/runtime: chỉ dùng tiếng Anh trong CI, Router, Architecture, Catalog, module được chọn và control/config pipeline. Không áp cho nội dung người dùng, trích dẫn bằng chứng, nguồn/domain/worldbuilding, lịch sử hoặc ghi chú dành cho người đọc không làm runtime control; ngôn ngữ trả lời người dùng vẫn theo CI.

## Concept Development anti-drift production 1.3

Core/local Catalog 1.5 dùng năm control ACTIVE theo phạm vi: Anti-Prior 1.1, MCA 1.2, WIL 1.1, Actor Reception 1.0 và Narrative Resolution 1.0. AUTO và token `/AD` chính xác trong directive hiện tại dùng chung cổng xét applicability; có thể chọn rỗng hoặc nhiều control. `/AD` có đường vào package ngay cả khi thông thường root chọn NONE, không tự chọn operation leaf hoặc tải mọi control. MCA và WIL độc lập; Actor Reception Requires MCA. A/B đã ngừng làm cấu hình hiện hành, lịch sử nằm trong Source_archive/Concept production anti-drift 2026-11-07.

Production baseline đã được người dùng xác nhận live; delta mới chỉ kiểm tĩnh và chưa deploy trong tác vụ này. Không suy internal IDs/locator hay per-case receipts từ xác nhận tổng quát.

## SEARCH — 2026-11-09

AIS pipeline 1.2/router 1.3, Concept core/catalog 1.5 và Architecture/Catalog 1.15 đã ACTIVE trong repository. AUTO vẫn hoạt động. `/SEARCH <instruction> #` yêu cầu thao tác bên ngoài mới, trừ khi người dùng chỉ định tái sử dụng/không làm mới. Chưa deploy; live và stress của delta mới: NOT_RUN. Xem [quy trình stress](SEARCH_REAL_CONTEXT_STRESS.md) và [glossary bảo trì](CONTROL_VOCABULARY_GLOSSARY.md); cả hai không phải dependency runtime.
