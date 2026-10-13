# AetherFire — Đề xuất revamp CI để đồng bộ kiến trúc mô-đun

> **Trạng thái:** `PROPOSAL`
>
> Khuyến nghị: cân nhắc **major version** thay vì vá minor nếu triển khai toàn bộ thay đổi này.

---

# 1. Tại sao CI hiện tại cần đổi vai trò

CI hiện tại rất mạnh ở:

```text
authorship
control grounding
source gate
truth status
anti-drift
canon mutation authority
simulation discipline
```

Đó là phần phải giữ.

Điểm không mở rộng tốt là khi CI/Router phải biết inventory cụ thể của Project.

Nếu mỗi module mới khiến phải sửa:

```text
CI
Router
00
92
overlay tables
```

thì control layer bị khóa vào snapshot của world.

---

# 2. Nguyên tắc CI mới

```text
CI GOVERNS THE RULES OF THE SYSTEM.
REGISTRY DESCRIBES THE CURRENT INVENTORY.
MODULES OWN CONTENT.
INTERFACES OWN CROSS-MODULE CONTRACTS.
VIEWS PRESENT DERIVED STATE.
```

CI không biết “AetherFire hiện có bao nhiêu quốc gia/file”.

CI biết “một module mới phải đăng ký thế nào”.

---

# 3. Đề xuất version

Nếu thực hiện:

```text
node routing
registry-backed topology
module contract
interface registry
coverage semantics
change transaction
generated views
structural validation
```

thì đây là breaking change đối với runtime contract.

Đề xuất cân nhắc:

```text
AetherFire CI v3.0
Source Router v4.0
Architecture Schema v1
```

Không bắt buộc tên/version này; mục đích là **không giả vờ đây chỉ là patch nhỏ**.

---

# 4. CI kernel nên giữ gì

CI kernel nên ngắn và khó thay đổi.

## 4.1 Authorship

```text
user controls canon/outcomes
```

## 4.2 Source authority

```text
explicit user decision
> current controlling canon
> preserved older canon
> unconfirmed
> inference
> proposal
```

## 4.3 Truth status

Giữ hệ:

```text
CANON
USER-PROVIDED STATE
UNCONFIRMED
HISTORICAL/SUPERSEDED
INFERENCE
PROPOSAL
HYPOTHETICAL
UNKNOWN
DEFERRED
CONFLICTED
UNVERIFIED
```

## 4.4 Stage discipline

```text
PROMPT_ROUTE_ONLY
PROMPT_EXECUTION
```

## 4.5 Module discipline

CI định nghĩa:

```text
Module ID
Node ID
Interface ID
Registry
Coverage
Schema compatibility
```

ở mức invariant.

Chi tiết schema nằm ngoài CI.

## 4.6 Canon mutation

Chỉ explicit user confirmation mutate canon.

Mutation structural/broad phải chạy impact analysis.

## 4.7 Validation

Nếu structural metadata không hợp lệ:

```text
fallback
or
block
```

không đoán.

---

# 5. Những gì nên đưa ra khỏi CI

## 5.1 Danh sách file/domain cụ thể

Không để CI phải ghi:

```text
10 → world
20 → status
...
```

Registry chịu trách nhiệm.

## 5.2 Danh sách overlay cụ thể

Có thể dùng:

```text
Overlay Registry
```

hoặc registry chung.

CI chỉ định nghĩa:

```text
load relevant overlays
resolve dependencies
specific beats generic inside declared scope
```

## 5.3 Glossary dài

CI chỉ pin:

```text
active architecture glossary
```

Glossary nằm file riêng.

## 5.4 Schema chi tiết

Không nhồi YAML field definitions vào CI.

---

# 6. Pipeline runtime CI vNext

```text
PHASE 0
resolve active CI + compatible architecture schema

PHASE 1 — ROUTE ONLY
classify operation
resolve module candidates from registry
validate registration
select target nodes/interfaces
identify canon mutation authority
form no conclusion

PHASE 2 — SOURCE CLOSURE
load mandatory nodes
expand dependencies
load interface contracts
load active issues/reconciliation evidence
validate closure
fallback to full read when required

PHASE 3 — CONTROL
resolve overlays
load overlay dependency closure

PHASE 4 — EXECUTION
answer / analyze / simulate / design

PHASE 5 — MUTATION ONLY IF AUTHORIZED
impact analysis
edit authoritative owner
reconcile
validate
regenerate views
report unresolved edges
```

---

# 7. Router vNext phải trở thành inventory-agnostic

Router không giữ hard-coded table cho mọi domain.

Nó hỏi registry:

```text
task domain / entity / node
→ candidate modules
```

Sau đó dùng module metadata.

Hard-coded route chỉ dành cho:

```text
bootstrap controls
registry itself
emergency fallback
```

---

# 8. Compatibility contract

CI phải biết:

```text
supported Architecture Schema range
supported Router range
```

Ví dụ:

```text
CI v3.0
requires Architecture Schema 1.x
requires Router >= 4.0 < 5.0
```

Nếu incompatible:

```text
CONTROL_COMPATIBILITY_BLOCKED
```

Không dùng best guess.

---

# 9. Fallback khi registry hỏng

CI mới không được chết hoàn toàn chỉ vì registry lỗi.

Fallback:

```text
registry unavailable/stale
→ full-file source gate using declared controlling sources
→ architecture-sensitive mutation blocked
→ bounded read-only analysis may continue if source authority remains provable
```

Mục tiêu:

```text
registry improves routing
but
does not become single point of truth failure for canon
```

---

# 10. CI và coverage

CI phải ghi rõ:

```text
coverage is metadata
not truth
not authority
```

Nếu task yêu cầu độ sâu vượt coverage:

```text
BLOCK
or
conditional branch
```

Không fill.

---

# 11. CI và module addition

Một module mới hợp lệ khi:

```text
registered
authority scope declared
schema valid
interfaces declared
local node map valid
```

CI không sửa.

Đây là tiêu chí quan trọng nhất để tránh major rewrite lần nữa.

---

# 12. CI và architecture extension

Nếu một architecture mới xuất hiện:

```text
new module type
```

thì trước tiên thử biểu diễn bằng primitive hiện có.

Chỉ bump schema khi cần một primitive mới thật.

Không bump CI chỉ vì lore có loại subsystem mới.

---

# 13. CI và derived views

CI xác định:

```text
derived view cannot override source/registry
```

Nếu view stale:

```text
ignore for authority
regenerate/validate
```

---

# 14. CI và structural validation

Pre-response check nên thêm:

```text
- registry/schema compatible?
- required module registered?
- node closure proven?
- interface endpoints valid?
- active issue hooks loaded?
- derived view stale?
```

Nhưng tránh in ra toàn bộ checklist trong mọi câu trả lời.

---

# 15. CI và change transaction

Nếu user nói:

```text
"xác nhận canon"
```

không chỉ update một file.

CI yêu cầu:

```text
truth mutation
+
structural synchronization
```

Nếu user chỉ authorizes lore change nhưng không authorizes architecture rewrite:

```text
update controlling canon
mark structural follow-up
do not redesign architecture silently
```

---

# 16. Migration từ CI v2.x

## Bước 1 — Shadow mode

CI cũ vẫn active.

Registry mới chỉ audit.

## Bước 2 — Compare routing

Với cùng prompt:

```text
old full-file route
vs
new node closure
```

Kiểm tra new closure không bỏ mất decisive evidence.

## Bước 3 — Enable node route read-only

Không canon mutation qua new pipeline.

## Bước 4 — Enable mutation transaction

Sau regression pass.

## Bước 5 — retire old hard-coded routing

Chỉ khi:

```text
all current modules registered
all controlling scopes valid
views regenerated
tests pass
```

---

# 17. Regression tests bắt buộc

## Local factual

Một node, một module.

## Cross-domain

Nhiều module, bounded interface.

## Unknown

Không được biến thiếu source thành false.

## Conflict

Phải vào reconciliation.

## Old canon

Không fallback.

## Missing module

Phải block/fallback.

## Stale view

Không dùng view làm authority.

## Canon mutation

Phải tìm reverse impact.

## Module split

Old path alias không làm mất dependency.

## Overlay cycle

Phải detect.

---

# 18. Mục tiêu của CI vNext

Sau revamp:

```text
CI change frequency
<<
lore/module change frequency
```

Nếu cứ mỗi vài module lại phải sửa CI, kiến trúc chưa thành công.

CI phải trở thành **kernel ổn định**, không phải bản đồ thế giới.
