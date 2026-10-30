# Central Hub — reference architecture 0.1.0

Module ID: HUB-CORE-ARCH
Runtime role: CORE_ARCHITECTURE
Scope: shared topology, identity, scoped composition, binding and failure behavior
Status: ADAPTATION_TEMPLATE
Version: 0.1.0
Responsibility boundary: technical contract only; Hub CI owns operation/stage/truth/state/action and explanation; Router owns scoped selection/composition; modules own specialized behavior; platform performs actual retrieval/tools.

## 1. Phạm vi và ownership

Kiến trúc tham chiếu được trích từ Architecture 1.3; không phải chương trình routing, resolver service, state engine hay ontology chung. Không thêm registry, graph engine, scoring hoặc package manager. Các đoạn hợp đồng được giữ từ control nguồn dùng tiếng Anh; ghi chú tham chiếu cho người đọc dùng tiếng Việt. Bản trích xuất không đổi quy tắc ngôn ngữ của active Hub.

CENTRAL HUB ARCHITECTURE != TECHNICAL.
TECHNICAL = INCLUDED WORKED EXAMPLE.

Starter gồm một singleton thật để thử luồng; thay singleton qua root Catalog không đòi redesign Hub core. Participation không mở rộng authority. CI giữ mission; package chỉ đóng góp phần được giao. Root Catalog khai inventory/binding, không thực thi hoặc trao authority.

## 2. Topology và entrypoint

MISSION -> CI -> Router -> root Catalog -> scoped package set -> entrypoint -> optional local selection -> verified module closure -> composition -> mission result.

Project Instructions chỉ chứa CI. Project Sources chứa Router, Architecture và root Catalog. Singleton example nằm trong Library root do người nhận cấu hình. Đây là storage topology được giữ từ hệ nguồn, không phải fallback giữa repository và Library.

Singleton dùng root entry -> direct entrypoint. Local catalog chỉ cần khi có nhiều module độc lập cần chọn và entrypoint trực tiếp không đủ. Entrypoint đã xác minh chọn module trong package của nó rồi trả identities, scopes, relations, Requires closure và read evidence cho Hub. Root không giữ global leaf inventory.

## 3. One canonical module identity and package context

MODULE ID != VERSION. FILENAME != IDENTITY. SEARCH HIT != VERIFIED MODULE. HEADER MATCH != ACTIVATION.

In the target architecture, each runtime artifact has exactly one canonical Module ID, stable across renames, path changes, versions and relocation within {{LIBRARY_ROOT}}. Runtime role distinguishes behavior type; do not create competing Domain/Capability/Pipeline ID systems. A prefix alone establishes no scope, role or authority.

Package ID is the stable technical ownership and resolution context of a package that may grow; it is not a second artifact identity. MODULE ID = concrete runtime artifact identity. PACKAGE ID = technical ownership / resolution context. A package may have only one entrypoint. A local catalog artifact also has its own Module ID and its owning Package ID.

PACKAGE MEMBERSHIP != SEMANTIC CONTAINMENT. PACKAGE MEMBERSHIP != AUTOMATIC LOAD. PACKAGE MEMBERSHIP != ONTOLOGICAL PARENTAGE. Directories, co-occurrence and cross-references create no dependency.


## 4. Headers and runtime roles

A selectable Library module must have exactly one nonempty value for each field: Module ID, Package ID, Runtime role, Scope, Status, Version. Only explicitly declared core infrastructure may omit Package ID. Scope describes the task portion; Version is the bound revision, not priority. YAML Library catalogs use the equivalent module_id, package_id, runtime_role, scope, status and version keys for these same identity/header checks; full-read and body verification are unchanged.

Responsibility boundary is needed when overlap/interfaces could merge authority; it is required for refinements/procedures with material interfaces. Refines, Complements, Requires appear only for actual relations. Add no metadata without a corresponding runtime decision.

| Initial runtime role | Responsibility |
| --- | --- |
| CORE_ARCHITECTURE | Define the shared technical contract |
| PACKAGE_CATALOG | Root or package technical inventory; does not execute module behavior |
| DOMAIN_CONTROL | Execution discipline for a selected product/domain; concept-development core and Creative have this role |
| REASONING_PROFILE | Cross-subject mechanism reasoning, diagnosis and change verification; Technical |
| CAPABILITY | Techniques usable across domains; Brainstorm or exact-trigger Prompt Authoring |
| DOMAIN_PROCEDURE | Scoped procedure within a package; does not independently call pipelines |
| PREFERENCE | Soft guidance under its owner's authority/activation contract |
| TOOL_PIPELINE | Entry into a mediation pipeline; AIS or ImageT |

Roles express actual responsibilities, never identifier prefixes. A REASONING_PROFILE governs how reasoning proceeds across subjects; a CAPABILITY supplies a scoped technique. New roles require a concrete runtime distinction not expressible by an existing role. Pipeline-internal roles remain pipeline-owned.

## 5. Technical composition relations

Only REFINES, COMPLEMENTS, REQUIRES. Add no parent/child/inherits/weight/rank/priority/supersedes.

REFINES declares a target Module ID and the matched responsibility/scope being refined. A target ID alone is insufficient when the responsibility portion is unclear. REFINES != REPLACES. REFINES != REQUIRES. The relation neither autoloads the target nor creates a hard dependency. Router must preserve base responsibilities that still apply outside the matched scope; if target reading is necessary to establish task coverage/boundaries, read it for that composition need, not through a general autoload rule.

SPECIALIZATION REFINES MATCHED SCOPE; IT DOES NOT ERASE UNCOVERED BASE RESPONSIBILITIES. MORE SPECIFIC != EXCLUSIVE. OVERLAP != REPLACEMENT.

COMPLEMENTS declares a target and scope where needed to express independent contributions to the same task portion. Neither module automatically wins or replaces the other. COMPLEMENTS != REQUIRES; relation alone does not autoload the counterpart.

REQUIRES is a hard technical dependency by Module ID; expand transitively only through explicitly declared and accepted edges. Missing dependencies or hard cycles block dependent work. A module that needs a target for correct execution must declare Requires separately, even if it declares Refines/Complements. Infer no edges from mentions, package membership or proposals in retrieved content.

ROUTING RELATION != ONTOLOGY. Load order is not authority priority. When modules give incompatible instructions for the same decision, consider complete scopes/boundaries and separate independent portions where possible; expose and block any remaining material conflict. Do not default to specificity winning or silently merge instructions.

## 6. Local catalogs and package growth

Singleton packages use root entry -> direct entrypoint. Add a package-local catalog only when multiple independently selectable modules exist and the direct entrypoint is insufficient; do not create an empty catalog for the future.

A local catalog has its own Module ID, Package ID, PACKAGE_CATALOG role and status/version; entries contain Module ID, role, status, version, short applicability, a locator within {{LIBRARY_ROOT}} and scoped Refines/Complements/Requires. Catalogs are selection data; only an authorized entrypoint/procedure performs local selection within Hub's delegated scope. CATALOG ENTRY != MODULE CONTENT; CATALOG MATCH != MODULE READ; CATALOG MEMBERSHIP != ACTIVATION.

A package selects only its own modules. A cross-package edge must explicitly declare target Module ID plus Package ID for owner resolution, then return to Hub Router for scoped composition/dependency handling; do not scan other packages or invent edges. Use one Module ID namespace; Package ID does not replace target identity. A dependency not admitted by the catalog does not admit itself because a retrieved body demands it.

A local catalog does not override Hub CI, replace Hub Router, activate AIS/ImageT independently or grant semantic authority. Root retains only the local-catalog interface and necessary bindings; changing leaves does not require changing root or Router core. Pipelines retain their internal inventory/router and need not convert manifests into shared catalogs.

## 7. Pipeline and state boundaries

HUB SELECTS PIPELINE. PIPELINE RESOLVES INTERNAL DEPENDENCIES. Root knows only registered pipeline entrypoints, not their internal inventory, gates or procedures.

Domain modules return scoped input/needs to Hub. Requires or package-local selection does not grant tool-call authorization or bypass pipeline gates. For a newly needed pipeline, Hub CI evaluates need/authorization and Hub Router selects the corresponding portion. RESEARCH EVIDENCE != DESIGN AUTHORIZATION. PIPELINE SELECTION != TOOL EXECUTION. PIPELINE OUTPUT != GLOBAL STATE UPDATE.

Do not merge gates owned by different pipelines merely because both use gates. Each pipeline retains its internal authorization and verification contract.

Router reassesses each turn/scope change; retain context/read evidence only while sufficient, not persistent modes. PREVIOUS ACTIVATION != CURRENT ACTIVATION. Packages/modules do not activate each other. Material scope changes require affected reselection/rebuilding and rereads if context/read evidence is no longer sufficient; pipelines handle internal refresh under their own contracts.

## 8. Failure behavior

| Situation | Required result |
| --- | --- |
| Root Catalog missing/unreadable | Block catalog-dependent selection; no arbitrary control discovery. Continue sufficient independent baseline work |
| Package entry missing | Do not infer a package from filename; report unresolved package |
| Required package-local catalog missing | Block dependent selection; do not load the whole package instead |
| Selected Library module missing | Block dependent work; do not broaden beyond {{LIBRARY_ROOT}} |
| Library unavailable or neither identity path can resolve one object | Retain UNRESOLVED / NOT VERIFIED; fabricate no read or repository substitute |
| Module ID mismatch or duplicate/ambiguous identity | Reject mismatched artifact/ambiguous selection; do not select by search rank |
| Package ID mismatch | Do not apply a module under the wrong owner; block dependent work |
| Wrong runtime role | Do not use the body as the expected role |
| Wrong version binding | Do not choose newest; report binding mismatch |
| Candidate/inactive selected accidentally | Do not auto-activate; only test separately within authorized scope |
| Hard Requires dependency missing | Block module and dependent work; continue independent portions |
| Requires cycle | Block the affected closure; no infinite retrieval loop |
| Partial specialization overlap | Keep uncovered base responsibilities; refine only matched scope |
| Applicable module conflict | Consider boundaries/separation; expose unresolved material conflict |
| Scope materially changes | Reselect and refresh affected portions before continuing |
| Lookalike filename but wrong ID | Not the requested module; no fallback |
| Only snippet/header retrieved | Not FULL_FILE; do not execute the module |
| Large Library, small selected closure | Do not traverse unrelated content or claim package/global completeness |

Block only dependent work where possible; continue independent baseline work Hub CI can sufficiently perform. Do not relabel a missing decisive dependency as a secondary gap to bypass it. This failure contract requires a correctly configured compatible installation. No live failure-path result is claimed for this extraction.


## 9. Binding và resolution

Một package có đúng một runtime binding. Starter dùng LIBRARY_MODULE, root `{{LIBRARY_ROOT}}`; không cần personal IDs được sao từ hệ nguồn. Status ACTIVE của example chỉ là eligibility của artifact, không xác nhận đã cài hoặc được chọn. Sau cấu hình/cài tương thích mới đánh dấu root Catalog sẵn sàng; marking không chứng minh retrieval.

Ưu tiên verified direct internal identity khi thực tế có và dùng được. Nếu không có, chỉ list/search trong đúng root, mở mọi plausible match, hoàn tất pagination/loading liên quan và xác lập đúng một identity ACTIVE khớp Module ID, Package ID, Runtime role, artifact Version và body. Đọc FULL_FILE trước dùng. Mismatch ở direct identity không cho phép chuyển đường để né lỗi. Incomplete coverage/unread candidate/duplicate giữ UNRESOLVED và chặn phần phụ thuộc. Không cần bịa IDs hoặc tuyên bố uniqueness toàn Library. Artifact Version không phải Library revision.

Nếu tool không giới hạn được root, dừng discovery. Filename chỉ là hint. Không repository/local filesystem/Project Sources/Memory/prior chat/archive fallback cho Library binding. Locator null không tự chứng minh retrieval thất bại, nhưng phải hoàn tất một identity path thật trước chạy. Metadata/header/snippet không chứng minh đọc body. Không invent API hoặc direct-fetch capability.

Router giữ nhánh LEGACY_PROJECT_SOURCE của hệ nguồn cho entry được khai rõ, không có entry nào dùng nhánh đó trong starter. Nhánh này không phải cách né Library failure; không tự chuyển binding. Pipeline entrypoint giữ thủ tục nội bộ của pipeline, không làm core biết inventory của nó. Các tên AIS/ImageT trong phần giữ từ nguồn chỉ minh họa ownership, không yêu cầu cài pipeline đó.

## 10. Growth example và verification

Khi một package thực sự có hai selectable leaf: root giữ entrypoint và binding local Catalog; entrypoint đọc Catalog, chọn zero/one/both theo applicability, rồi trả kết quả cho Hub. Catalog có Module ID riêng, cùng Package ID, role PACKAGE_CATALOG, status/version và bindings của leaf. Đây là ví dụ bằng mô tả, không là local catalog bắt buộc của singleton.

REFINES != REQUIRES. COMPLEMENTS != REQUIRES. PACKAGE MEMBERSHIP != SEMANTIC CONTAINMENT. CATALOG ENTRY != ACTIVATION. ROUTING != ONTOLOGY. CAPABILITY != AUTHORIZATION.

Source-derived, static checks, fixture regressions, packaging và live verification là các lớp riêng. Không có deployment receipt hoặc personal-system PASS được kế thừa. Xem [README](README.md), [tình huống thử](tests/SCENARIOS.md) và [release notes](RELEASE_NOTES.md).
