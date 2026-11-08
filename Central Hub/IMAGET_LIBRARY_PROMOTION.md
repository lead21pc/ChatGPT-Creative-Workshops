# ImageT Library promotion — 2026-11-09

## Trạng thái và phạm vi

REPOSITORY: PROMOTED / STATICALLY VERIFIED sau các kiểm tra ghi ở dưới.
LIBRARY / PROJECT DEPLOYMENT: NOT PERFORMED — runtime access unavailable.
ACTIVE PROJECT RUNTIME của Library revision: NOT VERIFIED. L01–L06: NOT RUN.
ROLLBACK BASELINE: PRESERVED. Không push trong tác vụ này.

Codex không có công cụ được hỗ trợ để cài/sửa `Central Hub Config` và Project Sources hoặc chạy chat Project thật trong environment này. Không dùng API/model mô phỏng thay cho live Project. Baseline legacy ImageT 1.2 có USER_CONFIRMED_INSTALLED_AND_LIVE / USER_CONFIRMED_LIVE_PASS theo record 2026-11-08; không chuyển PASS đó sang package Library.

Preflight: repository `C:\Users\Sheeplark\Desktop\CI Versioning Audit & Changelog`, branch `main`, HEAD `2898d2358f6b3eebd4de65e78d5033af7c27dd12`, working tree/index sạch. `origin/main` trực tiếp trả cùng SHA, tracking relation 0/0. Full static baseline: 295 passed.

## Delta và ownership

Root ImageT chuyển duy nhất từ `LEGACY_PROJECT_SOURCE / controller 1.2` sang `LIBRARY_MODULE / HUB-PIPE-IMAGET 1.3`, local Catalog 0.1. [Architecture 1.14](HUB_ARCHITECTURE_v1.14.md) và [root Catalog 1.14](HUB_PACKAGE_CATALOG_v1.14.yaml) ghi topology/binding mới; [Router 1.1](HUB_ROUTER_v1.1.yaml) chỉ đổi exact pins 1.13 → 1.14. Hub CI 1.2 và mọi package khác không đổi nội dung/binding.

10 predecessor candidate và Architecture/Catalog 1.13 được chuyển byte-exact vào [archive chung của promotion](<Source_archive/ImageT Library promotion 2026-11-09/>). Router trước sửa được snapshot cùng nhóm; [receipt](<Source_archive/ImageT Library promotion 2026-11-09/ARCHIVE_RECEIPT.json>) giữ SHA-256 của đủ 13 file. Legacy stack ở `tool_pipelines/ImageT/` giữ nguyên byte, không chuyển/xóa/sửa. Archive không làm runtime fallback.

Entrypoint chỉ bootstrap/delegate; controller giữ operation/Open Gate/field authority/Prompt Gate/visible verification; Router resolve core và chọn leaf sau authority; manifest giữ required core/integrity; local Catalog giữ hai optional leaves. Ready Gate giữ snapshot/approval/freshness/one-call. Preference ACTIVE chỉ là artifact có sẵn, phải được chọn riêng theo current-operation authority, không auto-active.

## Artifact phải cài

Tất cả nằm trực tiếp trong `library_modules/`, Package ID `HUB-PKG-IMAGET`, Status `ACTIVE`. Mỗi hàng là một object riêng trong Library root **Central Hub Config**; upload nguyên full file. Filename là gợi ý discovery, không thay canonical identity.

| File | Module ID | Role | Version |
| --- | --- | --- | --- |
| [HUB-PIPE-IMAGET_v1.3.md](library_modules/HUB-PIPE-IMAGET_v1.3.md) | HUB-PIPE-IMAGET | TOOL_PIPELINE | 1.3 |
| [HUB-IMAGET-CONTROLLER_v1.3.md](library_modules/HUB-IMAGET-CONTROLLER_v1.3.md) | HUB-IMAGET-CONTROLLER | DOMAIN_PROCEDURE | 1.3 |
| [HUB-IMAGET-ROUTER_v3.2.0.yaml](library_modules/HUB-IMAGET-ROUTER_v3.2.0.yaml) | HUB-IMAGET-ROUTER | DOMAIN_PROCEDURE | 3.2.0 |
| [HUB-IMAGET-MANIFEST_v2.3.0.yaml](library_modules/HUB-IMAGET-MANIFEST_v2.3.0.yaml) | HUB-IMAGET-MANIFEST | PIPELINE_MANIFEST | 2.3.0 |
| [HUB-IMAGET-READY-GATE_v1.1.md](library_modules/HUB-IMAGET-READY-GATE_v1.1.md) | HUB-IMAGET-READY-GATE | DOMAIN_PROCEDURE | 1.1 |
| [HUB-IMAGET-ANTI-PRIOR_v1.2.0.md](library_modules/HUB-IMAGET-ANTI-PRIOR_v1.2.0.md) | HUB-IMAGET-ANTI-PRIOR | DOMAIN_PROCEDURE | 1.2.0 |
| [HUB-IMAGET-ANTI-DRIFT_v2.1.0.md](library_modules/HUB-IMAGET-ANTI-DRIFT_v2.1.0.md) | HUB-IMAGET-ANTI-DRIFT | DOMAIN_PROCEDURE | 2.1.0 |
| [HUB-CATALOG-IMAGET_v0.1.yaml](library_modules/HUB-CATALOG-IMAGET_v0.1.yaml) | HUB-CATALOG-IMAGET | PACKAGE_CATALOG | 0.1 |
| [HUB-IMAGET-HUMANOID-CONSTRUCTION_v0.1.md](library_modules/HUB-IMAGET-HUMANOID-CONSTRUCTION_v0.1.md) | HUB-IMAGET-HUMANOID-CONSTRUCTION | DOMAIN_PROCEDURE | 0.1 |
| [HUB-IMAGET-HUMANOID-DESIGN-PREFERENCE_v0.2.md](library_modules/HUB-IMAGET-HUMANOID-DESIGN-PREFERENCE_v0.2.md) | HUB-IMAGET-HUMANOID-DESIGN-PREFERENCE | PREFERENCE | 0.2 |

Core manifest có exact SHA-256 cho controller/router/Ready Gate/Anti-Prior/Anti-Drift. Không tự hash manifest vào chính nó; entrypoint và Catalog phải được kiểm identity/full body theo accepted Hub binding. Library IDs, locator và Library revision chưa quan sát: giữ null/UNRESOLVED/NOT_VERIFIED, không lấy filesystem path làm locator.

## Correction của visible verification

Chỉ controller, mục `Verify and respond`, nhận thay đổi hành vi:

1. Mục tiêu thị giác được giao: đối chiếu ảnh với visual job/priority thực sự nằm trong request, operation lock hoặc preserved payload. Hierarchy, visibility/readability, detail competition, composition là bằng chứng/failure mode.
2. Độ trung thành với requirement và preserved state: counts/identity/anatomy/topology, reference roles, negatives, accepted/provisional/rejected/open state và preservation vẫn kiểm riêng.

High detail không tự FAIL; không suy priority khi không có; giữ uniform density, flat hierarchy, multiple equal elements, fragmentation và unbalanced design có chủ ý. Không tạo score/lifecycle/module mới. Giữ PASS/LOCAL_FAIL/STRUCTURAL_FAIL/UNVERIFIABLE; thiếu bằng chứng cho required region không được bịa kết luận.

Finding phải nối requirement bị ảnh hưởng → visible evidence → bounded correction proposal. Proposal không mở field bị khóa hoặc cấp quyền execute. Giữ payload/reference roles/state/counts/identity và mọi constraint ngoài delta; cần đổi field bị khóa thì nêu quyết định cần user. Không rewrite toàn prompt. Correction hợp lệ quay lại controller/Prompt Gate → NEW Ready Snapshot → NEW approval → ONE call; approval cũ đã consumed.

Ready Gate giữ nguyên phần `Preserved approval protocol`. Wording chỉ làm rõ equality thuộc exact **ImageT-controlled execution artifact**, không bảo đảm byte-exact prompt sau platform-owned safety/internal transformations không quan sát được. Không đổi protocol hoặc chuyển execution authority sang verifier.

## Deployment thủ công — thực hiện trước smoke

1. Giữ bản sao cấu hình Project đang cài. Xác nhận Hub CI trong Project Instructions khớp nguyên [HUB_CI_v1.2.md](HUB_CI_v1.2.md); nếu chưa khớp, chưa chạy smoke với bộ pin này. CI không bị sửa bởi promotion.
2. Cài đủ 10 object ở bảng vào **Central Hub Config**, chưa đổi root binding trước khi core sẵn sàng. Không upload candidate/archive/test/report làm runtime control. Với mỗi identity, mở FULL_FILE; kiểm Module ID, Package ID, role, ACTIVE, exact artifact Version và body. Hoàn tất relevant pagination/plausible-match checks; nhiều valid matches hoặc coverage thiếu thì dừng, không đoán newest. Ghi exact observed identity/URL/revision/hash nếu thực sự có; không suy từ filename.
3. Kiểm năm core hashes so với manifest bằng cơ chế quan sát được; nếu runtime không tính hash thì báo UNVERIFIED_HASH, vẫn kiểm exact identity/full body theo contract. Xác nhận hai Catalog leaves có đúng ACTIVE identities; preference chỉ `explicit_current_operation_only`.
4. Thay đồng bộ ba Project Sources bằng Router 1.1 hiện tại, Architecture 1.14 và root Catalog 1.14. Loại bản Architecture/Catalog cũ khỏi nguồn runtime để tránh conflicting pins. Giữ AIS và package khác nguyên trạng; không upload thêm ImageT core vào Project Sources.
5. Kiểm root chỉ có một entry `HUB-PKG-IMAGET`, `LIBRARY_MODULE`, entrypoint 1.3, local Catalog 0.1. Legacy v1.2 retained không được chọn như đường chạy thứ hai; nếu Sources cũ còn nhìn thấy thì chúng không là binding/fallback được phép. Không xóa rollback files local. Missing Library/core phải block, không tự dùng legacy.
6. Mở chat mới trong đúng Project. Chỉ sau deployment/identity checks trên mới chạy L01–L06. Không coi việc model đọc file local/repo hoặc prompt nhắc Library là proof của Library retrieval.

## Live smoke L01–L06

Chưa chạy bất kỳ ca nào trong tác vụ Codex này. Các prompt dưới là thao tác của người kiểm thử trong ChatGPT Project, không là quyền gọi tool trong repository task.

Ghi mỗi ca: Project/surface/model, exact installed revisions, original input/attachments, FULL_FILE/identity evidence có thể quan sát, snapshot/version, reply approval, tool-call count, visible output, hai nhóm verification, finding/correction và execution status. Không yêu cầu private reasoning. Tách kết quả từng ca; không suy trace từ lời model tự nhận.

| Ca | Trạng thái hiện tại | Điều kiện và thao tác | Acceptance |
| --- | --- | --- | --- |
| L01 | NOT RUN | Fresh chat A: gửi prompt A dưới đây, chưa approve. | Hub chọn HUB-PKG-IMAGET; exact Library entrypoint/core resolve, không dùng legacy execution path; hiện Ready Snapshot, zero calls. Thiếu retrieval evidence thì UNKNOWN cho retrieval, không tự PASS. |
| L02 | NOT RUN | Fresh chat B: gửi prompt B, inspect snapshot rồi dừng trước approval. | RAW; construction chỉ field overlap được phép, material/pose còn mở; preference không auto-active; zero calls trước Ready approval. |
| L03 | NOT RUN | Fresh chat C: gửi toàn bộ prompt C, kể cả current-user preservation instruction ngoài artifact. Dừng trước approval. | PRESERVED_AUTHORED; semantic pass-through; giữ accepted/provisional/rejected/open và thiết kế khác thường; không tự chọn leaf sửa field. Nếu execution thật sự cần semantic decision, hỏi nhỏ nhất/block đúng contract. |
| L04 | NOT RUN | Trở lại chat A, inspect exact snapshot còn identifiable và nguồn không đổi. Gửi `Có, tôi duyệt đúng READY SNAPSHOT v1 đang hiển thị.` chỉ nếu version thật là v1; nếu khác dùng đúng số hiện tại. | Một approval → một unchanged ImageT-controlled submission/call. Kiểm ảnh bằng cả mục tiêu thị giác và fidelity. Legitimate PASS hợp lệ; không bắt buộc gây lỗi. |
| L05 | NOT RUN | Chỉ khi L04 hoặc một ảnh có explicit priority/known constraints thực sự có bounded issue. Gửi prompt D kèm đúng ảnh/snapshot/request liên quan. | Finding có requirement/evidence/delta; zero automatic second call. Nếu user cho phép đúng delta, hiện snapshot mới; chỉ approval rõ cho version mới mới cho một call. Field khóa phải được surface, không tự mở. Không có issue phù hợp thì NOT RUN, không chế FAIL. |
| L06 | NOT RUN | Fresh chat D: gửi prompt E; inspect snapshot rồi approve đúng version nếu đạt. | Sau ảnh, không fail chỉ vì uniform density/flat hierarchy/fragmentation có chủ ý; vẫn kiểm count/reference/preservation và giới hạn nhìn thấy. |

Prompt A — L01 và L04:

```text
Tạo đúng một hình vuông xanh dương phẳng trên nền trắng, không chữ, không object khác. Mục tiêu thị giác: hình vuông phải nhìn thấy trọn vẹn và đọc rõ. Không dùng ảnh tham chiếu. Chuẩn bị theo ImageT và dừng ở Ready Snapshot để tôi duyệt. Cho biết các identity/version và bằng chứng đọc nguồn quan sát được dùng cho lần này; không cần trình bày suy luận nội bộ.
```

Prompt B — L02:

```text
Chuẩn bị ảnh một humanoid, đúng hai tay, mặc đúng hai lớp áo, monochrome, không phụ kiện. Chỉ làm rõ quan hệ chồng lớp đã có giữa hai lớp; không chọn thêm garment, màu hoặc material. Pose và material chưa được xác lập; để mở nếu execution không cần quyết định. Không chọn Humanoid Design Preference. Dừng ở Ready Snapshot, chưa tạo ảnh.
```

Prompt C — L03:

```text
Tôi cung cấp artifact đã author cho image execution dưới đây và yêu cầu giữ nguyên semantic payload. Không mở field nào cho construction hoặc preference; chỉ adaptation execution tối thiểu không đổi nghĩa. Dừng ở Ready Snapshot, chưa tạo ảnh.

ACCEPTED: đúng một humanoid, đúng hai tay, đúng hai lớp áo, monochrome; silhouette cố ý fragmented; detail phân bố uniformly dense, flat hierarchy, không ưu tiên mặt.
PROVISIONAL: lighting A hoặc B là hai phương án chưa chọn; không tự chọn hoặc promote một phương án thành accepted.
REJECTED: gold trim và mọi phụ kiện.
OPEN: material chưa xác lập; không đóng state từ output của generator.
NEGATIVES: không chữ, không thêm nhân vật.
REFERENCE ROLES: NONE.
```

Prompt D — L05, chỉ dùng khi có issue thật và input đúng:

```text
Kiểm ảnh vừa tạo đối chiếu request và snapshot đã duyệt. Nếu có lỗi thị giác có bằng chứng, nêu requirement bị ảnh hưởng, bằng chứng nhìn thấy và correction nhỏ nhất. Chỉ đề xuất, chưa sửa prompt hoặc gọi lại. Giữ mọi semantic state/reference role/constraint ngoài delta; nếu delta chạm field khóa, nêu quyết định tôi cần cho phép.
```

Nếu chấp nhận proposal, người kiểm thử gửi yêu cầu riêng chỉ định exact authorized delta, yêu cầu snapshot mới và dừng. Sau khi inspect snapshot mới mới approve đúng version. Không reuse approval cũ. Đừng dùng ảnh kết quả như reference asset mới nếu role/asset chưa được resolve và cho phép.

Prompt E — L06:

```text
Tạo đúng ba tháp vuông trong landscape two-color phẳng, không nhân vật, không chữ. Ba tháp ngang quyền thị giác. Detail phải uniformly dense trên toàn ảnh, flat lighting và flat hierarchy là chủ ý, không cần focal point đơn hoặc quiet region. Giữ thiết kế này; dừng ở Ready Snapshot để tôi duyệt trước khi tạo.
```

Phân loại: PASS/FAIL theo bằng chứng đúng scope; thiếu attachment/deployment/fresh-chat isolation hoặc approval cần thiết là INVALID / INCOMPLETE TEST. Không phân biệt được là UNKNOWN. Static fixture và lời model tự nhận không thay real Library read/tool trace. Một image-quality miss không tự chứng minh lỗi package hoặc cần rollback.

## Rollback có chủ đích

Known-good ImageT target đã xác lập tại preflight:

```text
HUB-PKG-IMAGET
entrypoint_module_id: HUB-PIPE-IMAGET
runtime_role: TOOL_PIPELINE
status: LEGACY_EXISTING
version: '1.2'
binding_mode: LEGACY_PROJECT_SOURCE
location.class: PROJECT_SOURCES
location.declared_source_path: tool_pipelines/ImageT/IMAGE_CONTROLLER_v1.2.md
location.source_name: IMAGE_CONTROLLER_v1.2.md
local_catalog: null
requires: []
controller SHA256: cf327b4008c5952c898875ebdd9142fd604ff56190c4400bbde37a5b6cc02355
manifest: tool_pipelines/ImageT/manifest.yaml, version 2.2.0
router: IMAGE_SOURCE_ROUTER.yaml, version 3.1.0
Ready Gate: READY_GATE_v1.0.md, version 1.0
Anti-Prior: IMAGE_ANTI_PRIOR.md, version 1.1.0
Anti-Drift: config.md, version 2.0.0
legacy preference: 0.1.1-candidate, inactive/direct-input-only
```

Exact predecessor ImageT entry nằm trong archived root Catalog 1.13; toàn bộ old source stack vẫn tại `tool_pipelines/ImageT/`. Rollback không cần tái dựng source. Ghi failure evidence trước; trigger gồm core không resolve/ambiguous, Open Gate regression, approval bypass, dual binding, leaf mở field trái phép, verifier tự execute hoặc package không load ổn định.

Đường khôi phục đồng bộ nhỏ nhất đã có sẵn: thay ba Hub Project Sources bằng snapshot Router 1.1 + Architecture/Catalog 1.13 trong archive promotion; khôi phục các exact legacy ImageT Project Sources từ stack giữ nguyên nếu đã gỡ khỏi Project. CI giữ nguyên 1.2 như preflight. Root chỉ có legacy entry sau restore, không giữ cả Library entry. Các package khác trong hai Catalog không đổi. Đây là rollback binding/topology có chủ đích, không phải fallback tự động hoặc claim toàn bộ Hub 1.13 từng live-tested. Không cần xóa Library objects để đổi route. Xác minh lại exact legacy binding/core và chạy bounded smoke trước claim rollback runtime PASS.

## Kiểm chứng repository

Lệnh baseline: `python -B -m pytest -p no:cacheprovider tests -q` — 295 passed.
Focused: `python -B -m pytest -p no:cacheprovider tests/test_imaget_library_promotion.py tests/test_imaget_library_candidate.py tests/test_hub_contracts.py -q` — **55 passed**. Full suite sau sửa: **308 passed**. Tests dùng declared intent/evidence fixtures và byte/identity checks, không nhận diện pixels/ngôn ngữ hoặc chạy Project/Library. P01–P05, O01–O05 và V01–V06 nằm trong `tests/test_imaget_library_promotion.py`, tái dùng selection/approval oracles hiện có; candidate history tests đọc đúng archived snapshot. Không chuyển static PASS thành LIVE BEHAVIOR PROVEN.

Không mở milestone mới; không Reference/Edit/GIF/animation/scoring/critic/learning loop hoặc automatic preference machinery.

Kiểm format: 26 file mới/sửa ngoài archive đều UTF-8, LF, có newline cuối, không BOM/trailing whitespace. `git diff --check` PASS; liên kết local của README/hồ sơ promotion resolve. Toàn bộ legacy ImageT stack, Hub CI và unrelated Library bodies được đối chiếu byte với preflight; receipt của 13 predecessor khớp bytes tại commit baseline. Archive không bị chuẩn hóa lại.
