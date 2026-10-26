# Concept Development — migration miniConcept và hai singleton

Ngày: 2026-10-26 (Asia/Bangkok). Phạm vi: repository local. Proposal: `ACCEPT WITH LOCAL CORRECTION`.

Baseline: repository `lead21pc/chatgpt-ci-worldbuilding`, branch `main`, HEAD `ee104645e89939341cd45deba465b5d71da64521`; remote main trả cùng SHA tại preflight. Index sạch; tệp untracked `candidates/library_trial/New Text Document.txt` được giữ nguyên, không thuộc tác vụ.

## Quyết định và topology

Architecture hiện có đã sở hữu growing package, local catalog, scoped module sets và Library verification. Dùng nguyên các primitive đó; không thêm Router, role, registry, state engine hoặc ontology chung. Core mới dùng `DOMAIN_CONTROL`; catalog dùng `PACKAGE_CATALOG`. Hub CI giữ operation/stage/truth/state/action/verification/explanation; không sửa Hub CI. Router chỉ đổi pin Architecture/Catalog, không đổi thuật toán hoặc Library identity rules.

```text
Hub CI 1.1 -> Hub Router 1.1 -> Architecture 1.1 / root Catalog 1.1
  TECHNICAL (unchanged)
  HUB-PKG-CONCEPT-DEVELOPMENT
    HUB-DOM-CONCEPT-DEVELOPMENT / DOMAIN_CONTROL / 1.0
    HUB-CATALOG-CONCEPT-DEVELOPMENT / PACKAGE_CATALOG / 1.0
      HUB-DOM-CREATIVE / DOMAIN_CONTROL / 1.1
      HUB-CAP-BRAINSTORM / CAPABILITY / 1.1
  AIS (unchanged)
  ImageT (unchanged)
```

Root chỉ biết package entrypoint và interface local catalog. Applicability/trigger chi tiết của leaf nằm trong local catalog; catalog là dữ liệu lựa chọn, entrypoint thực hiện lựa chọn trong phạm vi Hub đã giao. Core luôn là discipline của phần concept được chọn; zero leaf là hợp lệ cho concept audit/analysis. Creative và Brainstorm vẫn là hai Library object độc lập, không nhúng kỹ thuật vào entrypoint hoặc Router.

Không có hard Requires giữa hai leaf hoặc sang AIS/ImageT. Entrypoint và local catalog là interface phải đọc để chọn leaf; không autoload mọi leaf vì có package membership. Selected leaf thiếu/chưa verified chặn đúng phần phụ thuộc; không thay leaf bằng core hoặc gọi đó là capability đã thực thi.

## Revision và ownership

| Artifact | Trước | Sau | Lý do |
| --- | --- | --- | --- |
| Root Catalog | 1.0, năm package | 1.1, bốn package | Thay hai standalone owner bằng growing package |
| Architecture | 1.0 | 1.1 | Khai báo topology/interface mới; giữ Library identity contract |
| Hub Router | 1.1 | 1.1 | Chỉ cập nhật hai pin exact compatible; algorithm không đổi |
| Hub CI | 1.1 | 1.1, nguyên byte | Không có gap CI-level |
| Concept core / local catalog | chưa có | 1.0 / 1.0 | Hai artifact cần cho shared discipline và local selection |
| CREATIVE | HUB-PKG-CREATIVE / 1.0 | HUB-PKG-CONCEPT-DEVELOPMENT / 1.1 | Đổi runtime owner và thu hẹp body vào realization |
| BRAINSTORM | HUB-PKG-BRAINSTORM / 1.0 | HUB-PKG-CONCEPT-DEVELOPMENT / 1.1 | Đổi runtime owner/delegation; kỹ thuật từ Branching trở đi nguyên byte |

Hai leaf giữ Module ID và role. Đây là revision mới, không sửa bound 1.0 tại chỗ. `ACTIVE` và root `runtime_ready: true` giữ nghĩa eligibility của bộ contract đã được chấp nhận, không chứng minh cài Library; location UNRESOLVED vẫn chặn phần thực thi phụ thuộc. Không tạo global blocker cho các phần Hub độc lập. Không chuyển ID hoặc UI verification của 1.0 sang 1.1. TECHNICAL/AIS/ImageT root entries và toàn bộ control/pipeline bytes giữ nguyên; chỉ package count/topology metadata thay đổi.

## Mapping từng section miniConcept 2.2

| Section nguồn | Xử lý | Owner sau migration |
| --- | --- | --- |
| Output Contract | Không copy, bỏ trùng | Hub CI OUTPUT CONTRACT |
| Purpose and Authority | Concept analysis/expansion chuyển vào scope; quyền chốt không copy | Concept core + Hub CI |
| Core Invariants | Retire ba trục bắt buộc và output NOT MATERIAL; institution chuyển thành conditional | Concept core |
| Operational Control | Không copy grounding/discourse/epistemic, turn/stage hoặc quyền hành động | Hub CI |
| Axis 1: Institution | Port ngắn phần cơ chế, information/authority/capacity và failure; chỉ khi material | Concept core |
| Axis 2: Consistency | Port definitions/state/timeline/limits/relations/interfaces/dependencies và propagation | Concept core |
| Axis 2: claim/fact/source/status/update policy chung | Không copy kernel global; core dùng trạng thái/ràng buộc Hub đã giao | Hub CI |
| Axis 2: typed relations | Giữ các anti-collapse về containment/dependency/authority/causality/coupling | Concept core |
| Axis 3: Causal Chain | Rút thành đường nhân quả ngắn đủ dùng; giữ link, information path và không rationalize endpoint | Concept core |
| Concept Expansion Procedure | Port phát triển theo state/consequence và primitive chỉ khi cần; bỏ mapping institution bắt buộc | Core; realization -> Creative, premise variation -> Brainstorm |
| Audit and Proposal Boundary | Port checklist concept có điều kiện; audit không tự redesign | Core; quyền đổi stage/action vẫn Hub CI |
| Anti-Target: Generic Appeal | Guardrail ngắn chống thay cấu trúc tác giả bằng trope/genre/spectacle; incidental appeal không là lỗi | Concept core |
| Explanation and Reader Calibration | Không copy explanation/calibration/safety chung | Hub CI |
| CI v2.2 nguyên bản và v2.1 | Lưu nguyên byte, không còn standalone runtime owner | Historical source only |

Không đưa miniConcept vào Requires, runtime source list hoặc fallback của Hub. Retirement ở repository không xóa hoặc xác nhận đã retire ChatGPT Project thật.

## Artifact cần cài và trạng thái bằng chứng

Tất cả bốn artifact sau phải được đặt trong **Library / Central Hub Config**, không ở Project Sources:

| File repository | Identity / role / version |
| --- | --- |
| `library_modules/HUB-DOM-CONCEPT-DEVELOPMENT_v1.0.md` | HUB-DOM-CONCEPT-DEVELOPMENT / DOMAIN_CONTROL / 1.0 |
| `library_modules/HUB-CATALOG-CONCEPT-DEVELOPMENT_v1.0.yaml` | HUB-CATALOG-CONCEPT-DEVELOPMENT / PACKAGE_CATALOG / 1.0 |
| `library_modules/HUB-DOM-CREATIVE_v1.1.md` | HUB-DOM-CREATIVE / DOMAIN_CONTROL / 1.1 |
| `library_modules/HUB-CAP-BRAINSTORM_v1.1.md` | HUB-CAP-BRAINSTORM / CAPABILITY / 1.1 |

Package ID của cả bốn là `HUB-PKG-CONCEPT-DEVELOPMENT`, Status `ACTIVE`. YAML catalog dùng `module_id`, `package_id`, `runtime_role`, `scope`, `status`, `version` tương ứng năm header và Scope; đây là syntax catalog đã dùng, không là identity scheme mới.

Trạng thái của cả bốn: Library installation **NOT_PERFORMED**, retrieval/identity **NOT_VERIFIED**, binding **UNRESOLVED**, behavioral/live routing **NOT_RUN**. Không upload, sửa Library, deploy Project hoặc xóa miniConcept Project trong tác vụ này. Root/local Catalog giữ internal IDs/locator null và không nhập evidence revision cũ.

BRAINSTORM 1.0 trước migration từng được Codex quan sát qua UI/full rendered text trong đúng root, với kiểm tra trùng có phạm vi. Bằng chứng đó chỉ áp dụng `HUB-PKG-BRAINSTORM / 1.0`; nằm cùng stack cũ đã lưu. Không chứng minh 1.1 hoặc đường package mới. Không có micro execution hoặc AFM-015 A/B/C PASS từ migration này.

## Cài đặt thủ công an toàn

1. Giữ bộ Project Instructions/source roster hiện đang chạy và các Library object cũ. Không xóa/retire chúng trước khi replacement path được kiểm. Snapshot Router trước migration cùng Root Catalog/Architecture cũ và leaf 1.0 nằm trong archive nêu dưới.
2. Kiểm trong đúng `Central Hub Config` xem đã có từng identity mới hay chưa. Nếu cần, upload nguyên bốn artifact ở bảng trên. Không tạo ACTIVE duplicate. Không dùng filename, header riêng lẻ hoặc trạng thái “Current version” làm identity proof.
3. Đọc FULL_FILE entrypoint, local catalog và từng leaf cần cho smoke test. Theo Router hiện hành: dùng verified direct internal identity khi khả dụng, hoặc root-scoped listing/search + mở object cụ thể + full-read/header/body + đủ coverage/duplicate check. Hoàn tất pagination/loading và xét plausible candidates khác tên. Hidden IDs có thể giữ null; không suy Library revision từ artifact Version. Nhiều valid identity hoặc coverage thiếu thì dừng phần phụ thuộc. UI/backend không quan sát được giữ UNKNOWN.
4. Ghi riêng binding/read evidence thực vào location của root entry/interface và các entry local catalog tương ứng. Chỉ ghi locator bền vững nếu nền tảng chứng minh tính hữu ích/ổn định. Không suy từ bằng chứng leaf 1.0. Metadata verified không thay việc đọc/xác minh object trong lượt runtime mới.
5. Khi interface mới đã resolve đủ cho controlled switch, cài `HUB_ROUTER_v1.1.yaml` đã pin **Architecture 1.1 / Root Catalog 1.1**, cùng `HUB_ARCHITECTURE_v1.1.md` và `HUB_PACKAGE_CATALOG_v1.1.yaml` đã ghi evidence thật vào Project Sources. Hub CI vẫn nguyên `HUB_CI_v1.1.md` trong Project Instructions. Thay bộ root cũ, không giữ hai root Catalog làm authority song song. AIS/ImageT/TECHNICAL giữ bộ source/binding hiện có; không upload local catalog/leaf vào Project Sources.
6. Chạy C01–C12 dưới đây trong actual Hub; ghi input, model/surface/date, exact root/artifact/version/package, actual read evidence, selected scopes, output và blocker. Không lấy model tự khai đã đọc làm retrieval proof. Giữ smoke FAIL/UNVERIFIABLE thật; không sửa control âm thầm để PASS.
7. Chỉ sau exact identity/full reads và smoke đủ đạt mới retire standalone Creative/Brainstorm bindings/objects cũ khỏi deployment dùng mới. Full identity gồm Package ID và Version phân biệt revision; không chọn “mới nhất”. Giữ bản cũ để khôi phục có chủ đích, chẳng hạn di chuyển recoverable ra khỏi root discovery hoặc giữ inactive theo khả năng nền tảng. Không tự xóa vĩnh viễn. Không để chúng làm automatic fallback.
8. Sau replacement được xác nhận, người dùng tự retire miniConcept Project/Instructions độc lập trong ChatGPT nếu còn tồn tại. Không tự nhập lore, xóa chat/history hoặc coi Project đã retire chỉ từ Git. Hub không được load CI miniConcept cũ ở bất kỳ bước nào.

### Rollback có chủ đích

Nếu chưa switch deployment, giữ bộ đang chạy. Nếu new interface/read/smoke thất bại sau switch, người dùng chủ động khôi phục Router snapshot `HUB_ROUTER_v1.1.yaml`, Architecture 1.0, Root Catalog 1.0 từ nhóm archive dưới đây vào Project Sources, cùng Hub CI 1.1 không đổi. Restore đúng hai leaf 1.0/Package ID cũ trong Library nếu đã retire; dùng known prior binding/evidence đúng revision và xác minh lại nguồn. Không dùng Creator/Brainstorm 1.1 để giả artifact 1.0.

New package path không tự rollback khi Library lỗi. Không chạy đồng thời hai bộ root authority; không tự restore miniConcept thành runtime owner của Hub. `ROLLBACK != FALLBACK`.

## C01–C12 — SPEC / LIVE NOT_RUN

Các fixture chỉ khai báo yêu cầu ngữ nghĩa; static oracle không nhận diện ngôn ngữ hoặc chạy model. Core được chọn như package entrypoint; leaf chỉ đọc khi applicability độc lập khớp.

| Case | Input / áp lực | Kỳ vọng cần quan sát |
| --- | --- | --- |
| C01 | Audit concept về consistency/causal gap, không yêu cầu cảnh hoặc nhánh | Concept core + catalog; zero leaf; audit không redesign |
| C02 | Phát triển cảnh trong premise cho trước bằng hành động, nhịp và chi tiết chức năng | Concept + Creative; không Brainstorm |
| C03 | Đảo/nới giả định và phát triển nhánh | Concept + Brainstorm; không Creative nếu chưa yêu cầu realization |
| C04 | Đổi premise thành ba nhánh rồi viết scene ngắn mỗi nhánh | Core + cả hai leaf, đóng góp có scope; không winner-take-all |
| C05 | “Brainstorm vài tên ngắn”, baseline đủ, không kỹ thuật chuyên biệt | NONE; từ brainstorm không tự ép package/leaf |
| C06 | Tương tác nhân vật không phụ thuộc institution | Creative theo nhu cầu; không institutional checklist/NOT MATERIAL/systems analysis |
| C07 | Concept tổ chức với authority/information/resources/enforcement material | Core xét institution có điều kiện, chỉ phần cần; không ép leaf |
| C08 | Selected leaf chưa identity/FULL_FILE verified | BLOCK_DEPENDENT đúng phần; không repo/Project Source/archive fallback; phần Hub độc lập có thể tiếp tục |
| C09 | Sau Brainstorm, chuyển sang lời cảm ơn đơn giản | Recompute; không giữ package/Brainstorm mode |
| C10 | Concept có cấu trúc riêng, không yêu cầu genre transformation | Không tự archetype hóa, tăng spectacle hoặc generic normalization; incidental appeal không là defect |
| C11 | Creative realize một branch giả định do Brainstorm tạo | Giữ branch/proposal/unknown status; realization không thành accepted/current |
| C12 | Package mới hoạt động không có CI miniConcept | Không load/Requires CI cũ; source cũ chỉ provenance |

Giữ các fixture trigger rõ “thử động não”, “brainstorm sâu”, biến thể imperative và các ca mention/negation trong test Hub. Root không chứa trigger/leaf inventory; package-local applicability giữ `TRIGGER PHRASE != KEYWORD CONTAINS`. Không có trigger vẫn có thể chọn leaf theo kỹ thuật thực tế.

## Provenance và archive

Nhóm predecessor Hub dùng chung `Source_archive/Concept development migration 2026-10-26/`, giữ relative paths của Root Catalog 1.0, Architecture 1.0 và hai leaf 1.0. `HUB_ROUTER_v1.1.yaml` là snapshot rollback nguyên byte trước thay pin; hướng dẫn singleton cũ cũng được lưu nguyên byte. `MIGRATION_REPORT.md` và candidate/result snapshots lịch sử khác không bị viết lại.

Nhóm miniConcept riêng dùng `../llm-controls/project-instruction-designs/Project CI/source_archive/miniConcept_CI_v2.1.md` và `miniConcept_CI_v2.2.md`; cả hai rời vùng active cũ, giữ nguyên byte. Không chuyển các Project CI khác. Hai nhóm có artifact root/purpose riêng; checker trả `PASS_SHARED` cho Hub và `PASS_CREATE_ONE` cho nhóm CI cũ. Archive không là Library source hoặc runtime dependency.

`STATIC PASS != LIVE ROUTING VERIFIED`; `LIBRARY ARTIFACT PREPARED != LIBRARY INSTALLED`; `OLD REVISION VERIFIED != NEW REVISION VERIFIED`; `REPOSITORY ACTIVE != PROJECT DEPLOYED`.

### SHA-256 predecessor

Các hash sau xác nhận bytes lưu; không là runtime source locator. Test đối chiếu lại toàn bộ bytes với baseline Git cố định ở trên.

| Predecessor | SHA-256 |
| --- | --- |
| Hub `HUB_ARCHITECTURE_v1.0.md` | `da62208fd10ed46d2a453fb72c55a0475185583d107edc2196b5b503eae738b5` |
| Hub `HUB_PACKAGE_CATALOG_v1.0.yaml` | `4d841f8f0ca37220772cec1253d633004a38dfae330656f917554e7058a6d443` |
| Hub `HUB_ROUTER_v1.1.yaml` | `b63baa9a9461b90f12c61b35dbe572270ac16826e38c66f8a95128ad32e705de` |
| Hub `HUB_LIBRARY_SINGLETON_MIGRATION.md` | `0d0538d7068e28aab9b3c1db63209c1924cbc8e5cc2650a02db7b32bcdd68fdc` |
| Hub `library_modules/HUB-DOM-CREATIVE_v1.0.md` | `65c93c057eb130f8263051f9666c5be4f7799ff2e1bf11959e112087c2b9f009` |
| Hub `library_modules/HUB-CAP-BRAINSTORM_v1.0.md` | `4f25d9f93f92b6d9b6c6aa8793ae9b8eb159843d3d150cf0214915ff29470e99` |
| miniConcept `miniConcept_CI_v2.1.md` | `4d30f2e1ade1429e0ce93f14fbf9838d307a6fa2238f167fdffa25808ea3552d` |
| miniConcept `miniConcept_CI_v2.2.md` | `d4dcff5848f6d686bd29becf63592f59d72dd6e0f0fe15e8effb01d01a538079` |
