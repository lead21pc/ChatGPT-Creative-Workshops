# Schema module, node, interface và snapshot

Trạng thái: **PROPOSAL / CONTRACT DRAFT**. Đây là hợp đồng dữ liệu để review, chưa là schema được cài vào package. Không có script trong báo cáo này được gọi là validator đầy đủ của schema này. ID minh họa không đăng ký module hoặc canon mới.

## 1. Quy ước chung

- Encoding metadata: UTF-8; JSON strict, không duplicate key, không executable expression. Mọi object từ chối field ngữ nghĩa lạ; field trình bày mở rộng chỉ dưới `annotations`, không được Router dùng quyết định.
- `ID`: chuỗi ASCII opaque, ổn định; dạng đề xuất `<kind>-<uuid>` với kind `M/N/I/Q/D/S`. Alias dễ đọc là trường riêng, không quyết định ownership. Không tái dùng ID retired.
- `Ref`: `{id, revision}` hoặc `{path, sha256, selector}` trong shadow. Revision là digest nội dung record theo canonical serialization đã được version hóa; release pin binding ID→revision.
- `Path`: tương đối project, slash `/`, không `..`, absolute path, symlink/reparse traversal ra ngoài root; kiểm casefold collisions trên target Windows. Không normalize bytes archive.
- `Sha256`:64 hex digits. Hash raw file bytes, không normalize newline khi xác minh file. Hash metadata canonical dùng quy tắc riêng để tránh khác biệt thứ tự key; quy tắc phải được pin phiên bản, chưa tự chọn thuật toán mơ hồ.
- `EvidenceRef`: path/hash/selector trong một snapshot, mục đích `AUTHORITY_DECISION`, `SOURCE_BINDING`, `DEPENDENCY_REVIEW`, `PROVENANCE` hoặc `RESOLUTION`.
- Trường thiếu không tương đương `false`, `[]` hoặc UNKNOWN. Trường bắt buộc thiếu → structural error. Thông tin chưa có phải ghi status được phép và nêu scope bị giới hạn.
- Với status chưa xác định, dùng `{state:"UNASSESSED", reason:...}`; không fabricate source reference hoặc decision ID để làm form hợp lệ.

## 2. Descriptor và catalog

| Record / field | Kiểu, bắt buộc | Ý nghĩa / validation |
|---|---|---|
| Release.schema_version | string, có | Chính xác version metadata được hỗ trợ |
| Release.required_features | set<string>, có | Feature chưa hiểu → block; không bỏ qua |
| Release.snapshot_id | ID, có | Identity generation; không đồng nghĩa ngày build |
| Release.publication | object, có | `LOCAL_AUDIT`, `ACCEPTED_LOCAL`, `PUBLISHED`; evidence cho trạng thái, target/revision riêng |
| Release.controls | object, có | CI/Router/glossary refs; overlay candidate refs; hash/version compatibility |
| Release.catalog | file ref, có | Pin catalog bytes |
| Release.artifacts | list<file ref>, có | Chính xác output/input/schema/recipe cần để verify bundle; unique path |
| Release.activation | evidence record, có | `UNAPPROVED` chỉ chạy shadow; `APPROVED` cần căn cứ scope |
| Release.generator | object, có nếu generated | Tool/recipe hashes và format version, không chỉ tên tool |
| Catalog.modules | list, có | `{module_id, manifest_ref, discovery_labels}`; ID/path unique |

Manifest không hash chính nó vào vòng tham chiếu. `snapshot_id` gắn digest một danh sách artifact không tự chứa descriptor, hoặc gắn Git commit bên ngoài payload; tool phải chọn **một** công thức được test. Không ghi commit SHA tự tham chiếu vào file của chính commit ấy. `generated_at` chỉ là thông tin ngoài digest tái lập nếu có, không là freshness proof.

## 3. Module

| Field | Kiểu / bắt buộc | Quy tắc |
|---|---|---|
| schema_version, module_id | string / có | Unique; không đổi khi rename path |
| aliases | list<string> / có | Có thể rỗng; alias không encode owner bắt buộc |
| role | enum / có | `CANON_SOURCE`, `CONTROL`, `ISSUE_STATE`, `RECONCILIATION`, `HISTORY`, `NAVIGATION` |
| materialization | enum / có | `AUTHORED`, `GENERATED`, `ARCHIVED_INPUT`; độc lập role |
| lifecycle | enum / có | `PROPOSED`, `ACTIVE`, `SUPERSEDED`, `RETIRED`; active do release có approval |
| source_bindings | list<Binding> / có | Read source, edit input, provenance/recipe phân biệt |
| authority_scopes | list<Scope> / có | Khai báo scope + evidence; không inference từ filename |
| nodes | list<Node> / có | Ít nhất một node với module active được route |
| mandatory_nodes | set<NodeRef> / có | Chỉ mandatory **khi module vào closure**, không mọi module trên toàn thế giới |
| interfaces | list<Interface> / có | Records do module này giữ; các module khác reference |
| dependencies | list<Edge> / có | Module-level prerequisites; empty phải đi cùng trạng thái review |
| dependency_review | Review / có | `UNASSESSED`, `REVIEWED`; pin source+manifest revisions và scope/task families |
| coverage | list<Coverage> / có | Theo task/scope; có thể chỉ `UNASSESSED` |
| issue_refs | set<IssueRef> / có | Không tuyên bố toàn bộ unknown của source đều được đăng ký |
| retirement | object / conditional | Supersession/tombstone, scope map, evidence khi retired/superseded |

`Scope = {scope_id, description, dimensions, exclusivity, decision_refs, review}`. `dimensions` phân biệt timeline/world layer/POV/claim facet khi có căn cứ. Không tự gán Canon1/Canon2 cho đoạn chưa rõ. `exclusivity` có `EXCLUSIVE`, `FACET_PARTITIONED`, `UNVERIFIED`; `UNVERIFIED` không được cấp authority mutation.

Overlap checker bắt scope ID trùng/exclusivity và scope ancestry được khai báo; **không chứng minh hai câu mô tả scope tự do không chồng nhau**. Scope creation/transfer cần review ngữ nghĩa, kèm evidence. Taxonomy scope chỉ là metadata trong manifests; không tạo thêm một global authority database.

`Binding = {binding_id, kind, artifact_ref, transform_ref?, decision_refs, import_scope}`. `kind`: `READ_CURRENT`, `EDIT_INPUT`, `TRANSFORM_INPUT`, `PROVENANCE_ONLY`, `PRESENCE_CHECK`. Raw archived input không override output đã reconcile. `import_scope` có thể ghi excluded ranges để bảo vệ phần chưa được nhập.

## 4. Node và selector

```text
Node {
  node_id: ID;
  owner_module: ModuleRef;
  aliases: string[];
  source_ref: {path, sha256, selector};
  scope_refs: ScopeRef[1..n];
  load_policy: ALWAYS | ON_DEMAND | FULL_SCOPE_ONLY;
  context_requires: NodeRef[];
  dependencies: Edge[];
  claim_status_refs: EvidenceRef[];
  issue_refs: IssueRef[];
  coverage: Coverage[];
  dependency_review: Review;
}
```

- `WHOLE_FILE`: selector không cần markers. Hợp cho module60 hoặc giai đoạn đầu.
- `MARKER_RANGE`: marker đầu/cuối immutable, mỗi marker xuất hiện đúng một lần, không nằm trong fence; hash toàn source vẫn được pin. Sibling spans không overlap trừ khi explicitly shared context.
- `LEGACY_SECTION`: section path+expected occurrence1+source hash; dùng ở shadow. Hash đổi → selector stale, không tự tìm gần giống. Line numbers chỉ trong báo cáo, không là selector lâu dài.
- `FULL_SCOPE_ONLY` nghĩa nạp khi thao tác yêu cầu cả scope; nếu nó mang decisive constraint của node local thì constraint phải là context dependency bắt buộc. Không dùng policy để giấu điều kiện quyết định khỏi local read.

`claim_status_refs` trỏ nhãn nguyên bản trong source, không copy enum “CANON” lên toàn node nhiều trạng thái. Nếu node chứa nhiều status material, giữ theo span hoặc đọc cả node với nhãn nguyên văn; không bắt phân mảnh một claim một file.

Ví dụ binding shadow có bytes thật của60 tại baseline:

```json
{
  "kind": "READ_CURRENT",
  "artifact_ref": {
    "path": "60_MC4_IDENTITY_CURRENT.md",
    "sha256": "2B11C4846788A607B311854E0667E2A918F55E07F648A9DC70ED0C3A8187B088",
    "selector": {"kind": "WHOLE_FILE"}
  },
  "import_scope": "MC4 identity và boundaries đã ghi trong source",
  "assessment": "SHADOW_EXAMPLE_ONLY"
}
```

Đây là **mảnh ví dụ**, không phải Binding đầy đủ để production validator chấp nhận: chưa có binding_id/decision_refs/record registration. Nó minh họa cách không bịa approval. Muốn active phải hoàn tất các trường và review cần thiết.

## 5. Typed edges

```text
Edge {
  edge_id: ID;
  from: NodeOrModuleOrInterfaceRef;
  to: Ref;
  kind: edge-kind;
  purpose: nonempty string;
  condition: Condition;
  evidence_refs: EvidenceRef[1..n];
  review: Review;
}
Condition = ALWAYS | {task_family_in: string[]} | {all: Condition[]}
            | {any: Condition[]} | {not: Condition}
```

Không có tùy ý chạy code. Predicate chỉ dùng task features đã xác định ở route stage; chưa xác định cho kết quả UNKNOWN, không false. Khi UNKNOWN, nạp dependency nếu an toàn/khả thi; nếu không đủ để kết luận applicability thì block nhánh đó.

| Kind | Read closure | Reverse impact | Cycle policy |
|---|---|---|---|
| REQUIRES_EVIDENCE | Bắt buộc khi condition phù hợp/chưa loại được | Có, bắc cầu | SCC đọc được, visited set |
| REQUIRES_CONTROL | Tương tự, payload là control | Có | SCC chỉ nếu tương thích; conflict không được hòa trộn |
| CONSUMES_INTERFACE | Nạp các facet liên quan và context | Có | Xử lý như read graph |
| SUMMARIZES | Summary phải nạp owner khi cần premise chi tiết | Có, invalidate review | Không cấp authority ngược |
| DERIVED_FROM | Không tự nạp build inputs vào reasoning | Có cho build/output | DAG; cycle là lỗi |
| CITES_HISTORY | Chỉ provenance task rõ | Review impact có phạm vi | Không thành current evidence |
| SUPERSEDES | Không thăng source lịch sử; dùng xác định scope hiện hành | Có | DAG theo scope/epoch; không tự latest-wins |
| ISSUE_AFFECTS | Nạp open state material | Có | Cho phép backlink, không auto-resolve |

`EXPOSES` có thể suy từ interface participants và module-owned list; không cần ghi cạnh dư ở cả hai nơi. `CONTROLS_SOURCE_SCOPE` là scope declaration, không biến thành lore `GOVERNS`. Quan hệ lore như `DEPENDS_ON` chỉ ở source, không import vào read graph nếu chưa có evidence review rằng phải đọc.

## 6. Interface record đa phía

```text
Interface {
  interface_id: ID;
  metadata_owner: ModuleRef;
  participants: ModuleRef[2..n];
  description: navigation-only string;
  scope_refs: ScopeRef[];
  facets: [{facet_id, controlling_source_refs, authority_evidence,
            status_ref, unresolved_issue_refs}];
  read_requires: Edge[];
  review: Review;
}
```

Nếu facet ownership chưa xác lập: `authority_evidence.state=UNVERIFIED`, sources là candidates có nhãn, không tự dùng chúng làm owner. Interface record **không có authoritative `what_crosses`, lore relation/direction/actor quyền hạn do metadata author tự điền**. Các nội dung đó nằm ở controlling source refs; optional display summary mang `SUMMARIZES` và reviewed digest.

Ví dụ mapping đề xuất cho relic access: source chính70§10, context70§9/11, global consumer10, issueAF-ML-006. Không dùng form để suy singular seal relic thuộc toàn bộ plural catalogue. Ví dụ AF–TE: event từ70§16, status limitation từ30 boundary, operation từ70§17, unresolved issues007/008. Có thể ba module nguồn cùng tham gia một record nhưng mỗi facet vẫn giữ source authority hiện có.

## 7. Issue và decision

```text
Issue {
  issue_id: existing stable ID;
  metadata_owner: ModuleRef;
  raw_type_state: exact source label;
  kind: UNKNOWN | CONFLICT | QUESTION | PROPOSAL | OTHER_PRESERVED;
  workflow_state: OPEN | DEFERRED | RESOLVED | SUPERSEDED;
  source_record_ref: EvidenceRef;
  affects: Ref[];
  blocking_scope: task/scope predicate;
  resolution_ref: EvidenceRef | null;
}
Decision {
  decision_id: ID;
  evidence_ref: EvidenceRef | UNVERIFIED record;
  scope: ScopeRef[];
  accepted_delta: source reference;
  supersedes: scoped Ref[];
  carried_open_issues: IssueRef[];
  verification_refs: Ref[];
}
```

Không đổi AF-OPEN/ML/AV/CX IDs trong migration. `raw_type_state` bắt buộc giữ nguyên khi map enum. `RESOLVED` phải có resolution source; importing metadata không tạo quyết định resolve. `DEFERRED` cần căn cứ hoãn; “không biết” không tự là “đã quyết định hoãn”. Local unknown chưa thành issue ID vẫn phải được node context nạp, không ép tạo hàng nghìn issue giả để đủ schema.

## 8. Coverage, review và generated view

`Coverage = {scope_refs, task_family, assessment, sufficient_for, limitations, evidence_refs, reviewed_source_revision}`. `assessment`: `UNASSESSED`, `BOUNDED_SUPPORT`, `INSUFFICIENT_FOR_TASK`. Không dùng COMPLETE hoặc total-world OPERABLE. `BOUNDED_SUPPORT` không override thiếu premise của request cụ thể.

`Review = {state, reviewed_refs, reviewer_decision_ref, scope, invalidated_by}`. State `UNASSESSED` cho shadow/full-file fallback; `REVIEWED` cần scope/task family và digests. Nếu chưa có người chấp nhận dependency map, ghi UNASSESSED thay vì giả kiểm đầy đủ.

`View = {role, materialization:GENERATED, generated_from_refs, generator_ref, schema_version, output_sha256, review_refs?}`. Mỗi source/recipe/schema thay đổi phải invalidate view đúng dependency. Hash chỉ bắt bytes/revision; paraphrase đúng nghĩa cần review. Navigation view không phải authority claim; generated canon có authority từ decisions riêng.

## 9. Những validation bắt buộc

1. Parse/schema/version/feature negotiation; duplicate keys, IDs, path collision và root containment.
2. Mọi active registered pointer resolve đúng digest; mọi active source trong accepted release có binding; proposal/untracked file không tự active.
3. Selector/cardinality/context coverage; không đọc excerpt stale hoặc bỏ preamble chưa phân loại.
4. Edge target/type/condition; closure visited; phân biệt read SCC và forbidden derivation/supersession cycle.
5. Scope uniqueness/partition và evidence; ambiguous overlap không giải quyết bằng thứ tự list.
6. Issue refs/resolution refs/tombstones; active required consumer không trỏ retired node chưa remap.
7. Derived dependency fingerprint/generator version; validate sau generation; output deterministic.
8. Activation approval và compatibility controls/schema/snapshot; no mixed generation.

Các kiểm1–8 vẫn không chứng minh completeness ngữ nghĩa của edge metadata. Cổng reviewed-evidence và semantic differential tests ở09 là bắt buộc trước node activation.
