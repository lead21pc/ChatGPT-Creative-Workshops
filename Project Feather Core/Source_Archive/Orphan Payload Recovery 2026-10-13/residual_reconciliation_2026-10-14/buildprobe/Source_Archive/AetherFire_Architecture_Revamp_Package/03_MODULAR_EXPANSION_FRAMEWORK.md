# AetherFire — Khung mở rộng mô-đun dài hạn

> **Trạng thái:** `PROPOSAL`
>
> Mục tiêu: định nghĩa một contract chung để AetherFire có thể tiếp tục thêm lore, subsystem, quốc gia, engine, overlay và kiến trúc mới mà không phải sửa toàn bộ control layer.

---

# 1. Primitive kiến trúc

Khung chỉ cần một số primitive ổn định:

```text
MODULE
NODE
INTERFACE
DEPENDENCY
ISSUE
RECONCILIATION
VIEW
OVERLAY
REGISTRY
SCHEMA
```

Không thêm primitive mới nếu chỉ là biến thể nội dung.

---

# 2. Module contract

Mỗi module phải khai báo tối thiểu:

```yaml
module_id:
module_type:
path:
authority_scope:
schema_version:
coverage:
local_index:
public_interfaces:
required_modules:
optional_modules:
status:
```

Đây là metadata tài liệu, không phải canon.

---

# 3. Stable identity

## 3.1 Module ID

Module ID không phụ thuộc filename.

Ví dụ proposal:

```text
AF.WORLD
AF.STATUS
AF.UNDIE
AF.METAFICTION
AF.NARRATION
AF.MC4
AF.ML
AF.AVIATION
CTRL.ROUTER
CTRL.MODULAR
CTRL.WORLDLOGIC
```

Tên chính xác có thể đổi trước khi triển khai.

## 3.2 Node ID

Node ID thuộc namespace của module:

```text
AF.UNDIE:WHITE_EXIT
AF.STATUS:CIVIL_ENTRY
AF.ML:CREED_QUORUM
```

Node ID không chứa line number.

## 3.3 Interface ID

Cross-module interface:

```text
IF:AF_ML:RELIC_ACCESS
IF:AF_UNDIE:STATUS_TRANSITION
```

Một interface có một ID duy nhất dù hai module cùng tham gia.

---

# 4. Local routing index

Mỗi module dài phải có:

```markdown
## LOCAL ROUTING INDEX
```

Schema đề xuất:

| Field | Ý nghĩa |
|---|---|
| `Node ID` | định danh ổn định |
| `Scope` | nội dung node |
| `Load Policy` | cách tải |
| `Requires` | dependency nội bộ |
| `Cross Requires` | dependency module khác |
| `Exposes` | interface/public contract |
| `Issue Hooks` | open/conflict liên quan |
| `Coverage` | độ phủ |
| `Authority Note` | boundary cần giữ |

Load policy tối thiểu:

```text
ALWAYS
ON_DEMAND
FULL_SCOPE_ONLY
```

---

# 5. Dependency types

Không dùng một từ `dependency` cho mọi edge.

Đề xuất structural edge types:

```text
REQUIRES
OPTIONALLY_USES
EXPOSES
CONSUMES_INTERFACE
CONTROLS_SOURCE_SCOPE
DERIVES_VIEW_FROM
SUPERSEDES
REFERS_TO_HISTORY
RECONCILES
CONSTRAINS
```

Lore relation types vẫn do ontology riêng kiểm soát.

Không chuyển structural edge thành lore edge.

---

# 6. Dependency closure

Pseudo-runtime:

```text
requested nodes
→ add ALWAYS nodes
→ expand REQUIRES
→ expand Cross Requires
→ add interface contracts
→ add active issue hooks
→ add reconciliation evidence if needed
→ add overlay closure
→ validate
```

Cycle:

```text
valid declared cycle
→ load each node once

unknown/unresolvable cycle
→ FULL_READ_FALLBACK or BLOCK
```

---

# 7. Coverage taxonomy

Coverage không phải truth status.

Đề xuất:

```text
REGISTERED
BOUNDARY_ONLY
PARTIAL
OPERABLE
DEEP
```

Có thể thêm:

```text
DEFERRED_COVERAGE
```

nhưng chỉ nếu thật cần.

## Rule

```text
DEEP
!=
MORE CANON AUTHORITY

BOUNDARY_ONLY
!=
FALSE INTERNAL STATE

PARTIAL
!=
PERMISSION TO FILL
```

---

# 8. Task capability declaration

Một module có thể khai báo task classes nó hỗ trợ.

Ví dụ:

```yaml
supports:
  - factual_lookup
  - bounded_analysis

does_not_yet_support:
  - full_operational_simulation
  - quantitative_model
```

Đây là cách xử lý domain mỏng mà không bắt user đào sâu ngay.

---

# 9. Interface contract

Một interface phải đủ mô tả boundary, không cần mô tả toàn module.

Schema:

```yaml
interface_id:
participants:
relation_type:
direction:
controlling_nodes:
what_crosses:
authority:
information_path:
constraints:
failure_behavior:
truth_status:
coverage:
issue_hooks:
```

Chỉ field có ý nghĩa với interface mới cần populated.

Không invent field content để đủ form.

---

# 10. Interface ownership

Cross-domain relation không thuộc độc quyền một bên nếu relation thực sự là boundary chung.

Pattern:

```text
Module A internals
Module B internals
Interface X between A/B
```

Module A/B có thể summary X.

Nhưng controlling interface record chỉ có một.

---

# 11. Module lifecycle

Đề xuất trạng thái tài liệu:

```text
PROPOSED
REGISTERED
CURRENT
SPLITTING
MERGING
SUPERSEDED
RETIRED
ARCHIVED
```

Không trộn với canon truth status.

Ví dụ:

```text
module status = CURRENT
node truth = UNKNOWN
```

hoàn toàn hợp lệ.

---

# 12. Split criteria

Một module nên được cân nhắc split khi có từ hai dấu hiệu mạnh trở lên:

```text
1. có authority scope độc lập;
2. có tốc độ cập nhật độc lập;
3. task thường xuyên chỉ cần một phần;
4. phần đó có public interface riêng;
5. full-read cost đã cao;
6. phần đó có reconciliation/open issues độc lập;
7. content bắt đầu duplicate sang file khác;
8. team/model phải tạo nhiều exception routing.
```

Không dùng số dòng làm trigger duy nhất.

---

# 13. Merge criteria

Chỉ merge nếu:

```text
same authority
same lifecycle
same change cadence
same boundary
separation creates no independent routing value
```

Không merge chỉ vì thường co-occur.

---

# 14. Module addition protocol

Khi thêm architecture/module mới:

```text
STEP 1 — assign Module ID
STEP 2 — declare authority scope
STEP 3 — declare coverage
STEP 4 — define local nodes
STEP 5 — declare public interfaces
STEP 6 — declare dependencies
STEP 7 — register open/unknown state
STEP 8 — run structural validator
STEP 9 — regenerate views
STEP 10 — only then enable runtime routing
```

CI không cần sửa nếu primitive cũ đủ.

---

# 15. Module removal protocol

Không xóa route trực tiếp.

```text
CURRENT
→ SUPERSEDED/RETIRED
→ redirect dependencies
→ validate no active consumers
→ archive
```

Nếu còn consumer:

```text
REMOVAL_BLOCKED
```

---

# 16. Module rename protocol

Rename path không đổi identity:

```text
Module ID stable
path changes
registry updates
```

Không bắt toàn Project sửa dependency nếu dependency dùng Module ID.

---

# 17. Change transaction

Mọi structural/canon mutation lớn:

```text
PREPARE
→ identify controlling node
→ determine blast radius

LOAD
→ compute affected closure

CHANGE
→ edit only authoritative owner

RECONCILE
→ update conflict/open state

VALIDATE
→ structural + source checks

BUILD
→ regenerate derived views

REPORT
→ unresolved consequences
```

Không “sửa xong rồi search xem còn gì vỡ”.

---

# 18. Blast radius

Dùng bốn mức:

```text
LOCAL
BOUNDED_CROSS_MODULE
STRUCTURAL
GLOBAL
```

### `LOCAL`

Không đổi interface.

### `BOUNDED_CROSS_MODULE`

Đổi một hoặc vài interface đã biết.

### `STRUCTURAL`

Đổi authority, module boundary, schema hoặc dependency contract.

### `GLOBAL`

Đổi CI kernel/source authority/truth semantics.

---

# 19. Full-read fallback

Node routing không phải tôn giáo.

Bắt full-read khi:

```text
domain-wide audit
whole-module rewrite
structural mutation
unproven closure
stale local index
missing dependency
conflicting authority
unknown interface ownership
reconciliation requires whole context
user explicitly requests full read
```

---

# 20. Validation rules

## Registration

```text
every CURRENT module registered
every registered path resolves
```

## Node

```text
unique Node ID
marker exists
dependency resolves
```

## Interface

```text
endpoint exists
controller exists
no duplicate controlling record
```

## Authority

```text
no two current modules claim same exclusive scope
unless explicit shared contract exists
```

## View

```text
derived view matches registry generation state
```

## Issue

```text
active issue references valid module/node/interface
```

## Supersession

```text
target exists
active consumer remapped or explicitly blocked
```

---

# 21. Architecture schema version

Đề xuất:

```text
ARCH_SCHEMA_VERSION = 1
```

Router và CI khai báo compatible range.

Ví dụ:

```text
Router v4
supports Architecture Schema 1.x
```

Nếu schema không tương thích:

```text
STRUCTURE_LOAD_BLOCKED
```

Không tự đoán.

---

# 22. Derived view policy

Derived view phải có metadata:

```text
generated_from
schema_version
generated_at
registry_revision
```

Nếu manual edit được cho phép:

```text
manual section
```

phải tách khỏi generated section.

Tốt hơn:

```text
generated file = no manual truth edits
```

---

# 23. Không ép module đồng hình

Một module lore có thể khác overlay.

Nhưng cùng contract tối thiểu:

```text
identity
scope
interfaces
dependencies
coverage
routing
lifecycle
```

Nội bộ vẫn tự do.

---

# 24. Tương thích với nguyên tắc modular hiện có

Khung này giữ nguyên:

```text
INTERACTION != CONTAINMENT
SHARED CONTRACT != SHARED IMPLEMENTATION
GENEALOGY != CURRENT HIERARCHY
POWER != AUTHORITY
```

và mở rộng chúng sang document architecture:

```text
SAME FILE != SAME MODULE
SAME MODULE != SAME LORE ENTITY
ROUTED_TOGETHER != DEPENDENCY
SUMMARY COPY != AUTHORITY
CURRENT != COMPLETE
INDEX != SOURCE
REGISTRY != CANON
```

---

# 25. Mục tiêu cuối

Khi Project gấp 5–10 lần hiện tại:

```text
add module
→ register
→ connect interfaces
→ validate
```

không phải:

```text
add module
→ edit CI
→ edit Router
→ edit global index
→ edit open file
→ copy summary vào world file
→ manually search every dependency
→ hope nothing drifted
```
