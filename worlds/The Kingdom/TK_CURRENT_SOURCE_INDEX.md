# The Kingdom — Current Source Index v1.0

Status: ACTIVE
Version: 1.0
Role: CURRENT_DISCOVERY

## Contract nguồn

Index quản discovery SOURCE_ID → path/role/scope, không canon authority, world ontology, dependency graph hoặc timeline log. Manifest nhận current source paths; header của từng owner giữ RUNTIME_ROLE, ROLE, STATUS, SCOPE, AUTHORITY_BOUNDARY, CROSS_OWNER_BOUNDARY, LOAD_MODE. CROSS_OWNER_BOUNDARY chỉ là ranh giới/interface, không hard dependency; đọc owner khác khi claim đang dùng cần nó. Không có trường không được Router/validator dùng.

Giữ persistent domain/actor state, temporal delta và actor-information riêng. Future country/actor/event owner chỉ thêm khi material đủ và có quyết định scope; không tạo placeholder. V1.0 chỉ FULL_FILE; không giả node closure. SOURCE_ID không đổi chỉ vì tên tệp đổi. Catalog stale không cho phép suy current từ archive; chặn dependent use và bảo trì đúng generated region.

<!-- BEGIN GENERATED SOURCE CATALOG -->
| SOURCE_ID | Path | ROLE | SCOPE |
| --- | --- | --- | --- |
| `TK-DOM-COUNTERINTEL` | `TK_DOMAIN_COUNTERINTELLIGENCE.md` | DOMAIN | Phản gián, quyền tiếp cận, tri thức và attribution; cơ chế đề xuất giữ riêng. |
| `TK-DOM-DELEGATION` | `TK_DOMAIN_OPENING_DELEGATION.md` | DOMAIN / OPENING DESIGN | Mandate xác minh, itinerary draft và câu hỏi; không phải event log. |
| `TK-DOM-GEO` | `TK_DOMAIN_GEOPOLITICS.md` | DOMAIN | Địa chính trị, DMZ, đối ngoại, động cơ mở cửa và các lựa chọn còn mở. |
| `TK-DOM-HEALTH` | `TK_DOMAIN_HEALTH.md` | DOMAIN | An toàn sinh học, điều trị và quyền y tế; chi tiết chưa xác định vẫn mở. |
| `TK-DOM-INFRA` | `TK_DOMAIN_INFRASTRUCTURE.md` | DOMAIN | Hạ tầng, không lưu và capabilities thường trực; phương án mở cửa giữ status riêng. |
| `TK-DOM-LANGUAGE-RELIGION` | `TK_DOMAIN_LANGUAGE_RELIGION.md` | DOMAIN / DESIGN PHILOSOPHY | Universal Language, thần tính, World Tree và triết lý; không xác nhận quyền tiếp cận. |
| `TK-DOM-LAW` | `TK_DOMAIN_LAW.md` | DOMAIN | Luật V2 đang tái thiết kế; Luật Ngoại Nhân chỉ áp dụng ngoại nhân đã bị bắt. |
| `TK-DOM-POT` | `TK_DOMAIN_POT.md` | DOMAIN | Thiết bị POT; canon khả năng và chi tiết còn mở. |
| `TK-METHOD-FICTION` | `TK_METHOD_FICTION.md` | RUNTIME / AUTHORING METHOD | World-state, checkpoint/interval, progression và giới hạn tri thức. |
| `TK-METHOD-POV` | `TK_METHOD_POV_PERSPECTIVE.md` | RUNTIME / AUTHORING METHOD | POV xuyên timeline; nguyên tắc đã xác lập và thiết kế chưa accepted giữ riêng. |
| `TK-TL-CP01` | `TK_TIMELINE_CP01_OPENING.md` | CHECKPOINT | Breakpoint mở cửa; pre-state tối thiểu, direct delta và boundary state CP1. |
| `TK-TL-CP02` | `TK_TIMELINE_CP02_REVEAL.md` | CHECKPOINT | Vụ thử nước, đánh chặn, attribution và military/mage reveal; boundary tức thời, không sở hữu phản ứng nhiều ngày sau. |
| `TK-TL-I01-02` | `TK_TIMELINE_INTERVAL_CP01_CP02.md` | INTERVAL | Sau boundary CP1 đến ngay trước CP2; progression, phản ứng và state tích lũy có nguồn. |
| `TK-TL-POST02` | `TK_TIMELINE_POST_CP02.md` | POST-CHECKPOINT MATERIAL | Sau reveal CP2; premise logistics chưa có số checkpoint và phụ lục simulation lịch sử, không là baseline phản ứng current. Không xác định CP3. |

<!-- END GENERATED SOURCE CATALOG -->

## Navigation

[Timeline index](THE_KINGDOM_CHECKPOINT_STATE_INDEX.md) giữ CP1 → interval → CP2 → POST02; không CP3. [Open issues](TK_OPEN_ISSUES_CURRENT.md) giữ unknown/conflict/deferred có hệ quả; entry không resolve. [Reconciliation](TK_RECONCILIATION_RECORD.md) chỉ truy quyết định/provenance khi điều kiện Router đòi hỏi. [CI](controls/TK_CI_v1.0.md) → [Router](controls/TK_ROUTER_v1.0.yaml) → [Pipeline](controls/TK_AUTHORING_PIPELINE_v1.0.md) theo chức năng yêu cầu, không bắt mọi task qua authoring.

Current thiếu thì UNKNOWN/gap, không tự nạp archive. Repository ACTIVE != live Project deployed. Header/index/manifest/hash không nâng epistemic status của lore.
