# Central Hub — canonical namespace migration 2026-11-11

## Trạng thái hiện hành

Hồ sơ migration ngày 2026-11-11. Bộ lúc migration gồm Architecture/Catalog 1.18, Router 1.1 và CI 1.2. Để cài bản hiện hành, xem [bộ active trong repository](README.md). Đây là migration canonical identity một lần đã được người dùng cho phép; không là đổi role hoặc thiết kế lại runtime.

PROJECT / LIBRARY DEPLOYMENT: NOT_PERFORMED. SUCCESSOR LIBRARY RETRIEVAL / LIVE BEHAVIOR: NOT_RUN. NESTED LIBRARY FOLDER CAPABILITY: NOT_VERIFIED. Bằng chứng live trước migration giữ nguyên scope/revision cũ; không xác nhận identity successor. Không push, tạo branch hoặc tag trong tác vụ này.

Baseline: `c818c1954c0a54b2f777687e07e4ae32530f1845`, `main`, working tree sạch. Root có sáu package; AIS giữ LEGACY_PROJECT_SOURCE. User Profile schema/resource ID 1.0 và Context Snapshot giữ hợp đồng riêng, không tham gia namespace module.

## Mapping được chấp thuận và phiên bản successor

| Identity trước migration | Identity successor | Artifact Version | Nguồn successor trong repository |
| --- | --- | --- | --- |
| `HUB-DOM-TECHNICAL` | `HUB-TECH-ENTRY` | 1.0 → 1.1 | `library_modules/Technical/HUB-TECH-ENTRY_v1.1.md` |
| `HUB-DOM-CONCEPT-DEVELOPMENT` | `HUB-CON-ENTRY` | 1.5 → 1.6 | `library_modules/Concept Development/HUB-CON-ENTRY_v1.6.md` |
| `HUB-CATALOG-CONCEPT-DEVELOPMENT` | `HUB-CON-CATALOG` | 1.5 → 1.6 | `library_modules/Concept Development/HUB-CON-CATALOG_v1.6.yaml` |
| `HUB-DOM-CREATIVE` | `HUB-CON-GEN-CREATIVE` | 1.1 → 1.2 | `library_modules/Concept Development/General/HUB-CON-GEN-CREATIVE_v1.2.md` |
| `HUB-CAP-BRAINSTORM` | `HUB-CON-GEN-BRAINSTORM` | 1.1 → 1.2 | `library_modules/Concept Development/General/HUB-CON-GEN-BRAINSTORM_v1.2.md` |
| `HUB-CAP-DEBATE` | `HUB-CON-GEN-DEBATE` | 1.0 → 1.1 | `library_modules/Concept Development/General/HUB-CON-GEN-DEBATE_v1.1.md` |
| `HUB-DOM-NAMING` | `HUB-CON-GEN-NAMING` | 1.0 → 1.1 | `library_modules/Concept Development/General/HUB-CON-GEN-NAMING_v1.1.md` |
| `HUB-DOM-ANTI-PRIOR` | `HUB-CON-AD-ANTI-PRIOR` | 1.1 → 1.2 | `library_modules/Concept Development/Anti Drift/HUB-CON-AD-ANTI-PRIOR_v1.2.md` |
| `HUB-DOM-MODULAR-CONCEPT-ARCHITECTURE` | `HUB-CON-AD-MODULAR-CONCEPT-ARCHITECTURE` | 1.2 → 1.3 | `library_modules/Concept Development/Anti Drift/HUB-CON-AD-MODULAR-CONCEPT-ARCHITECTURE_v1.3.md` |
| `HUB-DOM-WORLDBUILDING-INTERNAL-LOGIC` | `HUB-CON-AD-WORLDBUILDING-INTERNAL-LOGIC` | 1.1 → 1.2 | `library_modules/Concept Development/Anti Drift/HUB-CON-AD-WORLDBUILDING-INTERNAL-LOGIC_v1.2.md` |
| `HUB-DOM-ACTOR-RECEPTION` | `HUB-CON-AD-ACTOR-RECEPTION` | 1.0 → 1.1 | `library_modules/Concept Development/Anti Drift/HUB-CON-AD-ACTOR-RECEPTION_v1.1.md` |
| `HUB-DOM-NARRATIVE-RESOLUTION` | `HUB-CON-AD-NARRATIVE-RESOLUTION` | 1.0 → 1.1 | `library_modules/Concept Development/Anti Drift/HUB-CON-AD-NARRATIVE-RESOLUTION_v1.1.md` |
| `HUB-CAP-AUTHORING` | `HUB-AUTH-ENTRY` | 0.8 → 0.9 | `library_modules/Authoring/HUB-AUTH-ENTRY_v0.9.md` |
| `HUB-DOM-SHOPPING` | `HUB-SHOP-ENTRY` | 1.0 → 1.1 | `library_modules/Shopping/HUB-SHOP-ENTRY_v1.1.md` |
| `HUB-CATALOG-SHOPPING` | `HUB-SHOP-CATALOG` | 1.0 → 1.1 | `library_modules/Shopping/HUB-SHOP-CATALOG_v1.1.yaml` |
| `HUB-PROC-SHOPPING-SEARCH` | `HUB-SHOP-SEARCH` | 1.0 → 1.1 | `library_modules/Shopping/HUB-SHOP-SEARCH_v1.1.md` |
| `HUB-PIPE-IMAGET` | `HUB-IMAGET-ENTRY` | 1.3 → 1.4 | `library_modules/ImageT/HUB-IMAGET-ENTRY_v1.4.md` |
| `HUB-CATALOG-IMAGET` | `HUB-IMAGET-CATALOG` | 0.1 → 0.2 | `library_modules/ImageT/HUB-IMAGET-CATALOG_v0.2.yaml` |
| `HUB-IMAGET-MANIFEST` | `HUB-IMAGET-CORE-MANIFEST` | 2.3.0 → 2.4.0 | `library_modules/ImageT/Core/HUB-IMAGET-CORE-MANIFEST_v2.4.0.yaml` |
| `HUB-IMAGET-CONTROLLER` | `HUB-IMAGET-CORE-CONTROLLER` | 1.3 → 1.4 | `library_modules/ImageT/Core/HUB-IMAGET-CORE-CONTROLLER_v1.4.md` |
| `HUB-IMAGET-ROUTER` | `HUB-IMAGET-CORE-ROUTER` | 3.2.0 → 3.3.0 | `library_modules/ImageT/Core/HUB-IMAGET-CORE-ROUTER_v3.3.0.yaml` |
| `HUB-IMAGET-READY-GATE` | `HUB-IMAGET-CORE-READY-GATE` | 1.1 → 1.2 | `library_modules/ImageT/Core/HUB-IMAGET-CORE-READY-GATE_v1.2.md` |
| `HUB-IMAGET-ANTI-PRIOR` | `HUB-IMAGET-AD-ANTI-PRIOR` | 1.2.0 → 1.3.0 | `library_modules/ImageT/Anti Drift/HUB-IMAGET-AD-ANTI-PRIOR_v1.3.0.md` |
| `HUB-IMAGET-ANTI-DRIFT` | `HUB-IMAGET-AD-ANTI-DRIFT` | 2.1.0 → 2.2.0 | `library_modules/ImageT/Anti Drift/HUB-IMAGET-AD-ANTI-DRIFT_v2.2.0.md` |
| `HUB-IMAGET-HUMANOID-CONSTRUCTION` | `HUB-IMAGET-HUM-CONSTRUCTION` | 0.1 → 0.2 | `library_modules/ImageT/Humanoid/HUB-IMAGET-HUM-CONSTRUCTION_v0.2.md` |
| `HUB-IMAGET-HUMANOID-DESIGN-PREFERENCE` | `HUB-IMAGET-HUM-DESIGN-PREFERENCE` | 0.2 → 0.3 | `library_modules/ImageT/Humanoid/HUB-IMAGET-HUM-DESIGN-PREFERENCE_v0.3.md` |

Mỗi control đổi canonical identity tăng minor version vì header/binding và byte thay đổi material; suffix patch được giữ ở dòng ba thành phần. Architecture/Catalog 1.17 → 1.18 xác lập hợp đồng mới. Router giữ 1.1, chỉ đổi exact pins; CI giữ 1.2 nguyên byte. Package IDs và runtime roles giữ nguyên. Đây không phải tăng phiên bản của AIS, User Profile hoặc release distribution.

## Tổ chức và cài đặt

`library_modules/` có các thư mục Technical, Concept Development, Authoring, Shopping và ImageT. Concept có General và Anti Drift; ImageT có Core, Anti Drift và Humanoid. Entrypoint/Catalog ở gốc package. Thư mục chỉ phục vụ bảo trì; namespace không tạo runtime relation hoặc quyền.

Mỗi file successor là một object Library riêng. Tất cả phải nằm dưới sole discovery root `Central Hub Config`. Chưa chứng minh Library hỗ trợ folder lồng nhau. Cách cài an toàn khi chưa có bằng chứng đó: tạo 26 object trực tiếp dưới root, dùng basename duy nhất của các file successor. `location.artifact` và manifest `file` là đường dẫn nguồn/cài đặt theo `library_modules/`, không là runtime locator; object vẫn được resolve bằng exact identity, bound version và FULL_FILE. Nếu nền tảng hỗ trợ folder, có thể mirror layout repository nhưng kiểm duplicate phải giữ coverage across root/subfolders, không chỉ thư mục của package.

Bộ cài tại mốc migration gồm Architecture 1.18, root Catalog 1.18, Router 1.1 đã đổi pins và CI 1.2. Hợp đồng User Profile 1.0 tiếp tục cài ở Project Sources khi dùng Profile; bốn object riêng do người dùng quản lý không bị model di chuyển/sửa. AIS pipeline/router giữ nguyên Project Sources.

Thay bộ Library cũ theo mapping đã duyệt; không để hai identity cùng là đường runtime ACTIVE. Chỉ ghi internal IDs/revision hoặc observed paths sau quan sát thực; giá trị cũ không được kế thừa như evidence của successor. Dùng exact headers/body, FULL_FILE và scoped duplicate checks; không fallback sang repository, Project Sources hoặc old identity.

## Quan hệ và integrity giữ nguyên

- Concept Actor Reception Requires successor Modular Concept Architecture. Các leaf còn lại không được thêm quan hệ. General và Anti Drift không là quan hệ ontology hay activation.
- ImageT manifest sở hữu năm required core; Anti Drift vẫn required theo operation. Controller Requires Router, Anti-Prior và Anti-Drift; ANALYZE không cần Ready Gate, các call generation/retry vẫn cần. Catalog chỉ sở hữu hai optional humanoid leaves. Preference vẫn cần quyền riêng cho operation hiện tại và không Requires Construction.
- Shopping Search không gọi AIS; Hub chọn AIS độc lập. Technical/Authoring vẫn singleton không Catalog. Admission, triggers, presets, isolation và authority giữ nguyên.

## Predecessor, lịch sử và rollback

[Archive receipt](<Source_archive/Canonical namespace migration 2026-11-11/ARCHIVE_RECEIPT.json>) giữ đường dẫn, mapping và SHA-256 của 31 snapshot: 26 control, Architecture/Catalog, Router trước pin, README và hướng dẫn trước migration. Archive chỉ là provenance/test/rollback có chủ đích, không runtime fallback hoặc alias resolver.

Các promotion report, candidate, archive và runtime evidence cũ tiếp tục mô tả revision cũ bằng identity cũ. Không dùng chúng làm danh sách cài đặt hiện hành. Khi rollback được cho phép riêng, phục hồi trọn bộ binding/source tương thích của predecessor; không chỉ đổi filename hoặc giữ dual-active objects. Không có rollback/deployment nào được thực hiện trong migration này.

Release distribution 0.1.0 giữ nguyên bytes và tên lịch sử. Test release phải đối chiếu source revision phát hành, không buộc release cũ trùng active namespace mới. Digest toàn FTH đã lệch trước migration; không sửa FTH để làm test PASS.

## Kiểm chứng

Các kiểm tra promotion cũ trỏ chính xác predecessor snapshot; chúng không chứng minh successor. `tests/test_canonical_namespace.py` kiểm riêng active successors: mapping, headers/versions/roles, inventory, bound references, exact semantic preservation ngoài identity/path/version và observation metadata, graph/operation closure, hashes, namespace uniqueness, archive và no-fallback boundaries. Không là runtime resolver, model test hoặc live Library test.

Kiểm live thủ công sau cài đặt được cho phép riêng: xác nhận 26 identity/version và FULL_FILE dưới root; kiểm old object không còn là active match; thử Concept operation + Actor Reception/MCA, Shopping có/không research, Technical/Authoring singleton và ImageT ANALYZE/generation/preference. Chỉ ghi PASS với evidence quan sát được; thiếu trace thì giữ giới hạn tương ứng.

### Kết quả kiểm chứng repository

- `python -B -m pytest -p no:cacheprovider tests -q --tb=short`: 359 passed (346 kiểm tra revision trước và 13 kiểm tra successor mới).
- `python -B -m pytest -p no:cacheprovider tests/test_canonical_namespace.py -q --tb=short`: 13 passed sau kiểm tra cuối.
- `python -B -m pytest -p no:cacheprovider ../distribution/tests -q --tb=short`: 15 passed, 1 skipped, 1 failed. Failure còn lại là digest `Project Feather Core` của `test_protected_sources_unchanged`, đã FAIL trước migration với cùng digest. Baseline trước migration: 13 passed, 1 skipped, 3 failed; hai lỗi Hub stale-reference được sửa bằng source revision phát hành.
- `python -B -m pytest -p no:cacheprovider ../distribution/tests -q -k 'not test_protected_sources_unchanged' --tb=short`: 15 passed, 1 skipped, 1 deselected. Assertion digest Hub được kiểm trực tiếp trong test TECHNICAL và PASS; release source revision `7dd8ce9ceae77b09b6e20f0c686f41f9b1945807` khớp digest đã ghi.
- Archive group: PASS_SHARED; 31 predecessor snapshots khớp SHA-256/nguồn baseline. Existing archives không bị rewrite. UTF-8/BOM/EOF/trailing whitespace, local links tài liệu current và `git diff --check`: PASS. Cảnh báo Git về checkout CRLF không làm thay đổi archive.

Không có live call, Library/Project deployment hoặc kiểm chứng nested folder. Lỗi FTH ngoài phạm vi giữ nguyên; không sửa expected digest để ép PASS. Thay đổi local được giữ để review, chưa commit/stage/push.
