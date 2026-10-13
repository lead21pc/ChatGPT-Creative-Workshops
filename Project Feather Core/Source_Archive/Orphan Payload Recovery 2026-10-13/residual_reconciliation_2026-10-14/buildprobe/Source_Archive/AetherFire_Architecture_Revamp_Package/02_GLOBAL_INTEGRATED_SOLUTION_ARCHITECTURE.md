# AetherFire — Đề xuất kiến trúc giải pháp toàn cục

> **Trạng thái:** `PROPOSAL`
>
> Mục tiêu: giải quyết routing, coverage, dependency, duplication, reconciliation, CI và module growth bằng **một kiến trúc thống nhất**, không bằng các bản vá độc lập.

---

# 1. Kiến trúc đích

Đề xuất mô hình:

```text
                    ┌─────────────────────┐
                    │      CI KERNEL      │
                    │ authority/invariant │
                    └──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐
                    │       ROUTER        │
                    │ task → read closure │
                    └──────────┬──────────┘
                               │
                 ┌─────────────▼─────────────┐
                 │ ARCHITECTURE REGISTRY     │
                 │ module inventory/topology │
                 └───────┬─────────┬─────────┘
                         │         │
              ┌──────────▼───┐ ┌───▼────────────┐
              │ SOURCE MODULE │ │ INTERFACE      │
              │ local nodes   │ │ CONTRACTS      │
              └──────┬───────┘ └──────┬─────────┘
                     │                │
              ┌──────▼────────────────▼──────┐
              │ ISSUE / RECONCILIATION STATE │
              └──────────────┬───────────────┘
                             │
                  ┌──────────▼──────────┐
                  │ REASONING OVERLAYS  │
                  └──────────┬──────────┘
                             │
                  ┌──────────▼──────────┐
                  │ PROMPT EXECUTION    │
                  └─────────────────────┘

Derived views:
registry/state
→ 00 / 92 / maps / reports

Validation:
all layers
→ structural checks
```

---

# 2. Các lớp và trách nhiệm

## Lớp A — CI kernel

CI chỉ giữ quy tắc không được thay đổi theo inventory:

```text
authorship
source authority
truth status
canon mutation authority
route-before-execute
module/interface discipline
UNKNOWN discipline
old-canon quarantine
validation requirement
```

CI không liệt kê từng domain.

---

## Lớp B — Architecture Registry

Registry trả lời:

```text
module nào tồn tại?
module ID là gì?
path hiện tại ở đâu?
module type gì?
authority scope ở đâu?
coverage tổng quát thế nào?
local routing index ở đâu?
interface nào được expose?
overlay nào có thể áp dụng?
schema version nào?
```

Registry **không chứa lore**.

Registry **không resolve canon**.

---

## Lớp C — Source Module

Mỗi module là đơn vị sở hữu nội dung.

Một module có:

```text
stable Module ID
authority boundary
local routing index
stable Node IDs
public interfaces
internal nodes
dependencies
coverage metadata
open-issue hooks
```

Không ép mỗi module cùng kích thước.

---

## Lớp D — Interface Contract

Cross-domain relation không được quản bằng copy-paste.

Một interface record có một identity duy nhất:

```text
Interface ID
endpoint A
endpoint B
relation type
direction
payload / what crosses
authority / controller
truth status
coverage
open issue hooks
controlling source nodes
```

Các module chỉ tham chiếu interface.

---

## Lớp E — Issue/Reconciliation state

Tách:

```text
CURRENT LORE
≠
OPEN STATE
≠
CONFLICT EVIDENCE
≠
DESIGN HISTORY
```

`92` nên là view của active issues.

`91` nên dần trở thành summary/index của các reconciliation record có ID ổn định.

---

## Lớp F — Overlays

Overlay là module điều khiển reasoning.

Overlay cũng phải có:

```text
Overlay ID
activation conditions
dependencies
conflicts
mandatory nodes
on-demand nodes
stop conditions
```

Không full-read overlay mặc định nếu architecture mới đã cho phép node closure an toàn.

---

## Lớp G — Derived Views

Ví dụ:

```text
00_AETHERFIRE_CONSOLIDATION_INDEX.md
92_OPEN_ISSUES_CURRENT.md
architecture maps
module inventory reports
```

Các view này:

```text
human/model friendly
but
not independent source of truth
```

---

## Lớp H — Validator / Build step

Validator kiểm tra:

```text
module registration
file existence
Node ID uniqueness
dependency resolution
interface endpoints
authority duplication
stale derived views
schema version
cycles
orphan records
supersession links
coverage metadata
```

---

# 3. Một giải pháp cho từng pain point nhưng dùng chung kiến trúc

| Pain point | Giải pháp cục bộ | Cơ chế chung |
|---|---|---|
| full-file read | node routing | local routing index + dependency closure |
| stale `00` | regenerate/validate | derived-view pipeline |
| duplicate `10`/`70` | one owner + interface summary | module authority + interface contract |
| missing route | registration validation | architecture registry |
| uneven detail | coverage metadata | shared coverage taxonomy |
| domain monolith | split by authority/change cadence | module lifecycle |
| cross-domain growth | explicit interface records | interface registry |
| mutation impact | reverse dependency | graph validation |
| `92` growth | source issue records + generated view | issue state layer |
| `91` growth | reconciliation records by ID | provenance layer |
| `90` growth | historical modules/shards later | history registry |
| overlay growth | overlay nodes | same module framework |
| glossary drift | shared glossary | schema terminology |
| CI coupling | inventory-free CI | registry-driven runtime |
| stale node map | validator | build pipeline |
| orphan relation | orphan check | interface/dependency graph |
| rename/split breakage | stable IDs | identity != path |

Không có giải pháp nào ở bảng trên cần một architecture riêng.

---

# 4. Nguồn sự thật tối thiểu

Để tránh fragmentation, chỉ nên có rất ít nguồn cấu trúc có quyền khai báo.

## 4.1 Canon truth

Do current canon module sở hữu.

## 4.2 Structural truth

Do:

```text
Architecture Registry
+
module-local manifest/index
+
Interface Registry
```

sở hữu.

## 4.3 Open-state truth

Do issue records/reconciliation state sở hữu.

## 4.4 Derived views

Không sở hữu truth.

---

# 5. Giải quyết duplication `10` ↔ `70`

Pattern đích:

```text
10
→ AF-global interface to ML
→ references Interface IDs

70
→ ML internals

Interface Registry
→ AF ↔ ML contracts
```

Không:

```text
10 contains copy of 70
```

Nếu một global source cần context:

```text
summary
+ Interface ID
+ controlling Module ID
```

không copy full section.

---

# 6. Giải quyết `00`

`00` nên được định nghĩa lại là:

```text
DERIVED GLOBAL SOURCE MAP
```

Nó hiển thị:

```text
module
scope
path
authority
coverage
major interfaces
active/open counts
```

Nhưng các trường này được lấy từ registry.

Nếu `00` khác registry:

```text
VALIDATION FAIL
```

Không để model chọn cái nó thích.

---

# 7. Giải quyết `92`

Đề xuất:

```text
issue records
→ generate active issue view
→ 92
```

Mỗi issue có:

```text
Issue ID
state
scope
affected Module IDs
affected Node IDs
Interface IDs
evidence/reconciliation refs
blocking level
user-resolution requirement
```

`92` vẫn gọn, vì nó là view.

---

# 8. Giải quyết `91`

Không cần split ngay lập tức.

Giai đoạn đầu:

```text
91 stays
+
add stable reconciliation IDs
+
route by ID/node
```

Khi vượt threshold:

```text
Reconciliation/
  REC-....md
  REC-....md

91
→ generated summary/index
```

Không phân mảnh sớm.

---

# 9. Giải quyết `90`

Không cần lập tức cắt 4.000 dòng thành hàng chục file.

Trước tiên:

```text
node-index 90
+
classify history scopes
+
link historical nodes to current Module IDs
```

Chỉ split khi:

```text
independent history branch
+
independent update cadence
+
repeated local provenance requests
```

---

# 10. Coverage model

Đề xuất coverage độc lập truth status:

```text
REGISTERED
BOUNDARY_ONLY
PARTIAL
OPERABLE
DEEP
```

Ý nghĩa:

### `REGISTERED`

Biết module/node tồn tại, chưa đủ vận hành.

### `BOUNDARY_ONLY`

Biết interface và phạm vi; nội bộ chưa đủ.

### `PARTIAL`

Một số cơ chế đã xác lập nhưng task class còn bị giới hạn.

### `OPERABLE`

Đủ để chạy các task bình thường trong scope đã công bố.

### `DEEP`

Có độ chi tiết cao và nhiều failure/interface đã được mô hình hóa.

Không dùng:

```text
COMPLETE
```

vì lore sống gần như không bao giờ “complete” theo nghĩa tuyệt đối.

---

# 11. Read closure

Runtime mới:

```text
prompt
→ classify task
→ registry selects modules
→ load mandatory module nodes
→ select target nodes
→ expand dependencies
→ expand cross-module interfaces
→ load relevant open/conflict evidence
→ load overlay closure
→ validate closure
→ execute
```

Nếu closure không chứng minh được:

```text
FULL_READ_FALLBACK
```

Nếu source bắt buộc không có:

```text
SOURCE_LOAD_BLOCKED
```

---

# 12. Canon mutation transaction

Khi user xác nhận thay đổi canon:

```text
1. identify changed node
2. compute direct reverse dependencies
3. compute affected interfaces
4. classify blast radius
5. read required affected closure
6. edit controlling source only
7. update issue/reconciliation records
8. regenerate views
9. run validators
10. report unresolved downstream state
```

Blast-radius classes:

```text
LOCAL
BOUNDED_CROSS_MODULE
STRUCTURAL
GLOBAL
```

`STRUCTURAL` hoặc `GLOBAL` bắt buộc full affected-domain read.

---

# 13. Module split transaction

Khi một module quá lớn:

```text
old module
→ define split boundary
→ create new Module IDs
→ migrate nodes
→ preserve stable Node IDs where possible
→ replace copied cross-content with interfaces
→ update registry
→ update dependency endpoints
→ validate reverse dependencies
→ keep redirect/alias for migration window
→ remove alias after validation
```

Không split bằng cách copy rồi xóa dần.

---

# 14. Module merge transaction

Chỉ merge nếu:

```text
same authority scope
+
same change cadence
+
same lifecycle
+
same interface boundary
```

Không merge vì hai module thường được đọc cùng nhau.

---

# 15. Quy tắc thêm kiến trúc mới

Một loại architecture mới không được buộc sửa CI nếu nó có thể khai báo bằng module contract hiện tại.

Ví dụ:

```text
new military theater system
new religious subsystem
new aviation system
new magic economy
new cross-world mechanism
```

đều phải có thể:

```text
register
declare nodes
declare interfaces
declare dependencies
declare coverage
```

Nếu không thể, câu hỏi đầu tiên là:

```text
module schema thiếu primitive thật
hay
thiết kế mới đang cố bypass architecture?
```

Chỉ thay schema khi primitive mới thực sự không biểu diễn được.

---

# 16. Nguyên tắc chống phân mảnh

```text
MORE MODULES
!=
MORE GLOBAL CONTROL FILES
```

Mỗi module có local metadata.

Global layer chỉ giữ inventory và interface.

Không tạo global file cho từng loại node.

---

# 17. Lộ trình triển khai

## Giai đoạn 0 — Audit repo thật

- xác minh source tree;
- xác minh active CI;
- xác minh `80`;
- đo duplication;
- đo dangling refs;
- xác minh generated-view process.

## Giai đoạn 1 — Schema và glossary

- chốt thuật ngữ;
- chốt Module ID / Node ID / Interface ID;
- chốt coverage;
- chốt registry schema.

## Giai đoạn 2 — Shadow registry

- tạo registry nhưng chưa đổi runtime;
- map source hiện tại;
- validator chạy song song.

## Giai đoạn 3 — Node routing

- thêm local index;
- Router dùng closure;
- vẫn có full-read fallback mạnh.

## Giai đoạn 4 — Derived views

- `00/92` được sinh/kiểm tra từ registry/state.

## Giai đoạn 5 — Authority cleanup

- loại duplicate cross-domain blocks;
- đặc biệt các split đã xảy ra như `10`/`70`.

## Giai đoạn 6 — CI major revamp

- chuyển inventory khỏi CI/Router;
- runtime dùng registry.

## Giai đoạn 7 — Provenance scaling

- chỉ khi cần mới split `90/91`.

---

# 18. Tiêu chí không được hy sinh

```text
source authority
truth status
UNKNOWN preservation
old-canon quarantine
explicit user canon authority
typed relation discipline
actor information discipline
no hidden dependency
no silent reconciliation
```

Tái kiến trúc chỉ được làm runtime rẻ hơn và cấu trúc kiểm chứng tốt hơn.

Nó không được làm bằng chứng yếu đi.
