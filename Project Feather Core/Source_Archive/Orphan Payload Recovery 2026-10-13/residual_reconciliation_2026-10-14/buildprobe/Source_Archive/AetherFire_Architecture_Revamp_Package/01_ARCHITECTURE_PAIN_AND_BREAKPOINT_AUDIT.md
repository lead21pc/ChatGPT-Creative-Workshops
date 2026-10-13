# AetherFire — Kiểm toán pain point và breakpoint kiến trúc hiện tại

> **Trạng thái:** `ARCHITECTURE AUDIT / PROPOSAL BASIS`  
> **Không thay đổi canon.**
>
> Mục tiêu của tài liệu này là chỉ thẳng những chỗ sẽ gãy khi lore tiếp tục phình theo chiều rộng nhưng độ sâu cập nhật không theo kịp.

---

# 1. Bằng chứng cấu trúc hiện tại

## 1.1 Kích thước source không đồng đều rất mạnh

Kiểm kê file trong gói Project hiện tại:

| File | Số dòng xấp xỉ | Số heading |
|---|---:|---:|
| `10_WORLD_INSTITUTIONS_GEOPOLITICS_CURRENT.md` | 2122 | 132 |
| `20_STATUS_CIVIL_LABOR_CURRENT.md` | 1592 | 76 |
| `30_UNDIE_SYSTEM_CURRENT.md` | 4154 | 179 |
| `40_METAFICTION_CANON_TIMELINE_CURRENT.md` | 1537 | 76 |
| `50_NARRATORS_POV_AND_HUMOR_CURRENT.md` | 1063 | 47 |
| `60_MC4_IDENTITY_CURRENT.md` | 68 | 7 |
| `70_MATRIARCHS_LAMENT_CURRENT.md` | 873 | 55 |
| `90_DESIGN_HISTORY_AND_RECONSIDERATIONS.md` | 4060 | 206 |
| `91_RECONCILIATION_RECORD.md` | 613 | 51 |
| `92_OPEN_ISSUES_CURRENT.md` | 92 | 9 |

Đây không phải lỗi tự thân.

Nó chứng minh một điều quan trọng:

```text
CURRENT
≠
SAME COVERAGE DEPTH
```

`60` là current source nhưng rất mỏng; `30` là current source nhưng cực sâu.

Kiến trúc hiện tại không có metadata đủ rõ để Router biết khác biệt này.

---

## 1.2 `00` đã chậm hơn topology hiện tại

`00_AETHERFIRE_CONSOLIDATION_INDEX.md` ghi:

```text
latest integration: 2026-09-12
```

và danh sách current-domain chính vẫn tập trung ở:

```text
10
20
30
40
50
```

Trong khi:

```text
60_MC4_IDENTITY_CURRENT.md
70_MATRIARCHS_LAMENT_CURRENT.md
```

đã tồn tại, còn `92` đã mở rộng routing tới RF, Academy, MC4, cross-world và ML vào ngày 2026-09-16.

Pain point:

```text
global view
≠
current topology
```

Đây là dấu hiệu của **registry drift**.

---

## 1.3 Authority split đã xảy ra nhưng content split chưa sạch

`90` ghi rõ:

```text
70 controls internal Matriarch's Lament canon
10 retains only global/cross-domain interface
```

Nhưng `10` hiện vẫn chứa một block lớn:

```text
## Matriarch's Lament — Current Regional Canon
```

với nội dung trùng đáng kể với `70`.

Kiểm tra tĩnh trên gói hiện tại tìm thấy khoảng:

```text
240 dòng nội dung khác nhau trùng chính xác
≈ hơn 10.000 ký tự
```

giữa `10` và `70`.

Đây là breakpoint thực tế:

```text
authority split
+
content duplication
→ future divergence almost guaranteed
```

Một trong hai file sẽ được sửa trước file kia.

Sau đó model phải tự quyết cái nào mới hơn hoặc phải vào reconciliation để cứu.

---

## 1.4 Router đã biết một route mà gói hiện tại không có

Router v3.2 đăng ký:

```text
80_STABLE_AVIATION_RF_AIRSPACE_CURRENT.md
```

nhưng file đó không xuất hiện trong gói Project hiện được cung cấp cho lần audit này.

Không kết luận file đã mất khỏi repository.

Nhưng về kiến trúc, điều này chứng minh rằng:

```text
router inventory
có thể lệch
physical source inventory
```

Nếu không có validator, lỗi chỉ xuất hiện khi task thực sự route vào domain đó.

---

## 1.5 Router v3.2 bắt full-read theo file

Quy tắc hiện tại:

```text
routed file
→ read completely
```

Điều này rất an toàn khi package nhỏ.

Với source 4.000+ dòng và cross-domain task:

```text
1 local question
→ multiple full-file reads
→ context amplification
```

Khi lore rộng thêm, chi phí đọc tăng theo số domain chạm vào, không theo kích thước thật của câu hỏi.

---

# 2. Pain point và breakpoint

## BP-01 — Full-read amplification

### Pain point

Router dùng file làm đơn vị nhỏ nhất.

### Breakpoint

Khi một câu hỏi chỉ cần 2–3 cơ chế nhưng chạm 4 domain:

```text
task-local evidence
<<
loaded evidence
```

Context bị tiêu vào nội dung không thể thay đổi kết luận.

### Hệ quả

- model mất budget cho reasoning;
- xác suất bỏ sót điều quyết định trong biển text tăng;
- càng thêm source càng chậm;
- module lớn bị “phạt” vì độ sâu của chính nó.

### Mức độ

`BREAKPOINT NOW`

---

## BP-02 — Global index trở thành snapshot, không còn là topology sống

### Pain point

`00` vừa là index đọc cho model, vừa là snapshot hợp nhất.

### Breakpoint

Khi module được thêm nhanh hơn index được cập nhật.

### Hệ quả

- module tồn tại nhưng không được route;
- module mới phải dựa vào `92` hoặc Router riêng lẻ;
- nhiều control view có topology khác nhau.

### Mức độ

`BREAKPOINT NOW`

---

## BP-03 — Authority split nhưng canon text vẫn duplicate

### Pain point

Tách quyền kiểm soát file nhưng vẫn copy nguyên block lore sang file cha.

### Breakpoint

Lần chỉnh sửa đầu tiên chỉ xảy ra ở một copy.

### Hệ quả

```text
same claim
→ two current-looking locations
→ divergent wording
→ reconciliation debt
```

### Mức độ

`BREAKPOINT NOW`

---

## BP-04 — Không có một registry cấu trúc duy nhất

Hiện thông tin routing nằm rải ở:

```text
CI
Router
00
92
header từng file
91
90
```

Mỗi lớp giữ một phần.

### Breakpoint

Một module mới cần sửa quá nhiều nơi bằng tay.

### Hệ quả

- quên đăng ký;
- stale route;
- ghost route;
- authority boundary và routing boundary lệch nhau.

### Mức độ

`BREAKPOINT NOW`

---

## BP-05 — Coverage blindness

### Pain point

Không có metadata chuẩn cho biết một domain/node hiện được mô tả tới mức nào.

### Ví dụ cấu trúc

```text
60 ≈ 68 dòng
30 ≈ 4154 dòng
```

Cả hai đều là current source.

### Breakpoint

Model thấy:

```text
CURRENT
```

và dễ mặc định rằng cả hai có khả năng trả lời cùng độ sâu.

### Hệ quả

- hỏi sâu vào module mỏng → SOURCE_LOAD_BLOCKED;
- model dễ dùng prior để lấp;
- user cảm giác “đã có source mà sao vẫn thiếu”.

### Mức độ

`BREAKPOINT SOON`

---

## BP-06 — Domain bucket quá rộng

`10` hiện gánh đồng thời:

```text
world
state
institutions
geopolitics
foreign relations
RF
Academy
một phần ML
nhiều strategic interface
```

### Breakpoint

Các subdomain có tốc độ thay đổi khác nhau.

### Hệ quả

- file cha trở thành monolith;
- local edit có blast radius lớn;
- split sau này rất tốn vì dependency đã dính vào file name thay vì module ID.

### Mức độ

`BREAKPOINT SOON`

---

## BP-07 — Không có quy tắc split/merge module

Hiện việc tách `70` ra khỏi `10` đã xảy ra.

Nhưng kiến trúc chưa định nghĩa chung:

```text
khi nào phải split?
split cái gì?
ai giữ cross-domain interface?
file cũ trở thành gì?
cách tránh duplicate?
```

### Breakpoint

Mỗi lần module phình sẽ được xử lý theo cách ad hoc.

### Hệ quả

Project tích lũy nhiều kiểu split khác nhau và Router phải biết từng ngoại lệ.

### Mức độ

`BREAKPOINT SOON`

---

## BP-08 — Cross-domain interface explosion

Thêm một domain không chỉ thêm một file.

Nó tạo interface với domain cũ.

Nếu `n` module tương tác dày:

```text
potential cross-module relations
≈ O(n²)
```

Không phải mọi cặp đều có relation, nhưng tốc độ tăng vẫn cao hơn số module.

### Hệ quả

- UNKNOWN tăng ở boundary;
- open issue tăng nhanh;
- reconciliation tăng nhanh;
- một update local có impact ngoài dự kiến.

### Mức độ

`CORE SCALING RISK`

---

## BP-09 — Không có forward dependency graph đủ máy đọc

Router yêu cầu:

```text
accepted premise change
→ propagate dependent conclusions
```

Nhưng dependency chủ yếu nằm trong prose.

### Breakpoint

Khi một node có nhiều downstream consumer.

### Hệ quả

Model không thể chứng minh nó đã tìm hết dependency.

### Mức độ

`CORE SCALING RISK`

---

## BP-10 — Không có reverse-impact graph

Forward dependency trả lời:

```text
A cần B
```

Nhưng canon mutation cần:

```text
ai đang cần A?
```

### Breakpoint

Một premise đổi nhưng downstream conclusion còn sót.

### Hệ quả

```text
new premise
+
old dependent conclusion
→ latent contradiction
```

### Mức độ

`CORE SCALING RISK`

---

## BP-11 — `92` có nguy cơ trở thành monolith của mọi thiếu sót

`92` hiện rất hiệu quả vì gọn.

Nhưng khi lore rộng:

```text
local unknown
+
cross-domain unknown
+
deferred
+
conflict
+
proposal
→ one central table
```

### Breakpoint

`92` phình đến mức chính nó cần routing.

### Hệ quả

- một compact register trở thành global database bằng Markdown;
- merge conflict tăng;
- khó chia ownership.

### Mức độ

`BREAKPOINT LATER, HIGH PROBABILITY`

---

## BP-12 — `91` có nguy cơ trở thành monolith provenance

`91` vừa giữ:

```text
integration addenda
reconciliation summary
conflict register
evidence trail
priority reasoning
```

### Breakpoint

Số lần retcon/refactor tăng theo tuổi Project.

### Hệ quả

- provenance càng ngày càng khó route;
- conflict cũ và mới sống chung;
- task cục bộ phải vào một historical ledger lớn.

### Mức độ

`BREAKPOINT LATER`

---

## BP-13 — `90` đã là monolith lịch sử

`90` khoảng 4.000 dòng và hơn 200 heading.

Nó đã chứa:

```text
history
genealogy
reconsideration
analysis
retired design
surviving legacy
current notes
```

### Breakpoint

Khi thêm nhiều domain và nhiều vòng refactor.

### Hệ quả

History trở thành nơi “cái gì cũng từng có”.

Nếu Router vào đây không có node routing tốt, nguy cơ old-canon bias tăng dù quarantine vẫn tồn tại.

### Mức độ

`BREAKPOINT NOW FOR PROVENANCE TASKS`

---

## BP-14 — Generated view và hand-maintained view chưa có contract

`00` và `92` tự mô tả là generated/control view.

Nhưng kiến trúc chưa cho thấy trong gói hiện tại:

```text
generator nào?
source registry nào?
validation nào?
hash/version nào?
```

### Breakpoint

View không còn đồng bộ với source sinh ra nó.

### Hệ quả

“generated” trở thành nhãn quy trình thay vì thuộc tính có thể kiểm chứng.

### Mức độ

`BREAKPOINT NOW`

---

## BP-15 — Không có registration integrity check

Không thấy một bước bắt buộc kiểu:

```text
new *_CURRENT.md detected
→ registered?
→ authority declared?
→ index updated?
→ open issue hook valid?
→ router can reach it?
```

### Hệ quả

Module mới có thể tồn tại nhưng không tham gia runtime.

### Mức độ

`BREAKPOINT NOW`

---

## BP-16 — Không có stale-index detection

Một index có thể đúng lúc tạo nhưng sai sau hai tuần.

Nếu không có:

```text
schema version
source fingerprint
module revision
validation
```

thì model không biết index còn tin được không.

### Mức độ

`CORE CONTROL GAP`

---

## BP-17 — Không có interface contract

Cross-domain lore thường được mô tả trong prose của hai phía.

### Pain point

Không có record chuẩn trả lời:

```text
what crosses?
who controls?
which module owns the relation?
which nodes are endpoints?
what is known vs unknown?
```

### Breakpoint

Hai domain mô tả cùng relation theo granularity khác nhau.

### Mức độ

`CORE SCALING RISK`

---

## BP-18 — “Module” chưa phải contract tài liệu

Anti-drift đã định nghĩa module về reasoning rất tốt.

Nhưng source package chưa có chuẩn file/module bắt buộc:

```text
identity
authority scope
public interfaces
dependencies
coverage
local nodes
change policy
```

### Hệ quả

Mỗi module mới có style riêng.

### Mức độ

`CORE SCALING RISK`

---

## BP-19 — Namespace kiến trúc chưa chuẩn

Các từ sau dễ bị dùng chồng:

```text
source
index
domain
module
section
node
current
controlling
generated
dependency
interface
authority
priority
```

### Breakpoint

ChatGPT/Codex dùng prior phần mềm hoặc prior văn bản khác nhau rồi áp sai.

### Hệ quả

- `dependency` bị hiểu thành containment;
- `index` bị hiểu thành authority;
- `current` bị hiểu thành complete;
- `generated` bị hiểu thành automatically fresh.

### Mức độ

`BREAKPOINT SOON`

---

## BP-20 — Kiểu quan hệ của lore và kiểu quan hệ của tài liệu dễ bị trộn

Ví dụ:

```text
file A controls domain B
```

là quan hệ tài liệu.

Nó không có nghĩa:

```text
lore entity A governs lore entity B
```

Khi kiến trúc phình, nếu không tách namespace:

```text
DOCUMENT_GRAPH
LORE_GRAPH
AUTHORITY_GRAPH
DEPENDENCY_GRAPH
```

model rất dễ suy sai.

### Mức độ

`HIGH DRIFT RISK`

---

## BP-21 — Control overlay có thể lặp lại chính bệnh của canon source

Các overlay hiện đã dài từ khoảng 500 đến hơn 1.000 dòng.

Nếu mỗi overlay tiếp tục phình:

```text
node routing cho canon
+
full-read overlay
→ bottleneck chuyển chỗ
```

### Mức độ

`BREAKPOINT SOON`

---

## BP-22 — Overlay dependency chưa có validator

Router có dependency đặc biệt giữa Mortality, Modular Architecture và Total War.

Khi số overlay tăng:

```text
overlay A requires B
B conditionally requires C
C conflicts with D
```

không có graph validator sẽ tạo dependency cycle hoặc load thừa.

### Mức độ

`FUTURE CONTROL RISK`

---

## BP-23 — Không có compatibility contract giữa schema version và CI/Router

Nếu local index schema thay đổi:

```text
Router cũ đọc index mới thế nào?
CI cũ hiểu coverage field mới ra sao?
```

Hiện chưa có versioned architecture schema độc lập.

### Mức độ

`BREAKPOINT AT FIRST MAJOR REVAMP`

---

## BP-24 — Không có transaction cho canon mutation

Hiện user có thể xác nhận một thay đổi.

Router có nguyên tắc propagate.

Nhưng không có workflow dữ liệu kiểu:

```text
PRE-IMPACT
→ EDIT
→ RECONCILE
→ VALIDATE
→ REGENERATE VIEWS
→ POST-IMPACT CHECK
```

### Hệ quả

Mutation hợp lệ về authority vẫn có thể để lại source package không đồng bộ.

### Mức độ

`CORE MAINTENANCE RISK`

---

## BP-25 — Không có orphan registry

Project đã có khái niệm “orphaned” trong prose.

Nhưng không có nơi tập trung cho:

```text
relation mất parent
source split nhưng edge chưa remap
route cũ bị retire
dependency cũ không còn owner
```

### Hệ quả

Orphan tồn tại đến khi một task tình cờ đụng vào.

### Mức độ

`BREAKPOINT LATER`

---

## BP-26 — Không có tiêu chuẩn “đủ để chạy” cho module mỏng

Một module có thể được xác nhận tồn tại nhưng chưa đủ:

```text
authority
information
resource
transition
failure
interface
```

### Hệ quả

Model biết module tồn tại nhưng không biết loại task nào được phép thực thi trên nó.

### Mức độ

`COVERAGE GAP`

---

## BP-27 — Không có structural test suite

Hiện anti-drift kiểm tra reasoning rất tốt.

Nhưng thiếu kiểm tra package:

```text
duplicate Node ID
missing file
unregistered current source
dangling interface
unresolved dependency
duplicate controlling authority
stale generated view
cycle
orphan issue
invalid supersession target
```

### Mức độ

`BREAKPOINT NOW`

---

## BP-28 — Không có “blast-radius budget”

Một edit nhỏ có thể lan rộng.

Kiến trúc hiện tại không có chỉ báo:

```text
LOCAL
CROSS_MODULE_BOUNDED
STRUCTURAL
GLOBAL
```

### Hệ quả

Model có thể tưởng đang sửa local nhưng thực tế đổi contract của nhiều domain.

### Mức độ

`MUTATION RISK`

---

## BP-29 — Physical file name đang gánh quá nhiều identity

Dependency thường trỏ thẳng file.

Nếu module split hoặc rename:

```text
file identity changes
→ many routes break
```

Cần stable module ID và node ID tách khỏi path.

### Mức độ

`MIGRATION RISK`

---

## BP-30 — Sửa bằng cách tạo thêm nhiều file quản lý có thể làm vấn đề tệ hơn

Nếu phản ứng với mọi pain point bằng một file mới:

```text
routing registry
coverage registry
dependency registry
authority registry
issue registry
version registry
...
```

thì Project tạo “management lore” lớn ngang lore thật.

### Mức độ

`ANTI-SOLUTION RISK`

Giải pháp phải tối thiểu hóa số source-of-truth.

---

# 3. Breakpoint hệ thống khi lore tiếp tục rộng

Nếu không thay kiến trúc, chuỗi xấu nhất là:

```text
more modules
→ more boundaries
→ more partial coverage
→ more open interfaces
→ more duplicate summaries
→ more reconciliation
→ larger full-read sets
→ more context pressure
→ more missed dependencies
→ more corrective files
→ more routing complexity
→ more drift
```

Điểm nguy hiểm nhất:

```text
TOTAL DOCUMENTATION ↑
nhưng
PROVABLE LOCAL CONSISTENCY ↓
```

Tức là thêm tài liệu không còn đồng nghĩa tăng khả năng trả lời chính xác.

---

# 4. Những gì không nên làm

## 4.1 Không chỉ thêm mục lục

Mục lục giải quyết navigation.

Không giải quyết:

```text
authority
coverage
dependency
reverse impact
interface ownership
stale state
validation
```

## 4.2 Không chỉ chia file nhỏ hơn

File nhỏ nhưng dependency không khai báo:

```text
→ model phải search nhiều file hơn
```

Đó là fragmentation, không phải modularity.

## 4.3 Không tạo global mega-index chứa mọi node

Nó sẽ trở thành monolith mới.

## 4.4 Không bắt mọi module có cùng độ sâu

Mục tiêu là:

```text
uneven coverage
nhưng explicit
```

không phải:

```text
force every domain to become equally detailed
```

## 4.5 Không dùng AI search làm source authority

Search chỉ tìm candidate.

Authority vẫn do Router/CI/source contract quyết định.

---

# 5. Kết luận audit

Vấn đề cấp hệ thống hiện tại có thể nén thành:

```text
CURRENT ARCHITECTURE
= strong truth discipline
+ strong anti-drift discipline
+ weak structural registry
+ weak incremental scaling
+ weak machine-verifiable dependency
+ weak coverage representation
+ growing duplication / view drift risk
```

Điều đáng giữ là toàn bộ kỷ luật authority/UNKNOWN/quarantine hiện có.

Điều phải thay là:

```text
đơn vị quản lý:
FILE
→ MODULE + NODE + INTERFACE

topology:
hand-maintained multi-view
→ registry-backed

change:
edit then discover impact
→ impact-aware transaction

read:
whole routed file
→ canon-complete closure + safe fallback
```
