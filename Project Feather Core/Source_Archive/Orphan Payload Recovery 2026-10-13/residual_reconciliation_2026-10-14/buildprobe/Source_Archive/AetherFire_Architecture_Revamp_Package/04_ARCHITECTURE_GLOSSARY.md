# AetherFire — Glossary kiến trúc nguồn và điều khiển

> **Trạng thái:** `PROPOSAL`
>
> Mục tiêu: buộc ChatGPT, Codex và tài liệu dùng cùng một nghĩa.  
> Các mã trong backtick là **định danh thuật ngữ**, không phải từ thay thế cho giải thích.

---

# 1. Quy tắc dùng glossary

1. Nghĩa trong glossary chỉ áp cho **kiến trúc source/control**, không tự định nghĩa ontology lore.
2. Khi prior kỹ thuật chung xung đột với glossary này, glossary thắng trong scope kiến trúc AetherFire.
3. Không dùng hai thuật ngữ khác nhau cho cùng một primitive nếu không cần.
4. Không dùng một thuật ngữ cho hai graph type khác nhau.
5. Mỗi thuật ngữ kỹ thuật lần đầu trong một tài liệu nên có nghĩa rõ, không chỉ có nhãn.

---

# 2. Thuật ngữ cốt lõi

## Mô-đun nguồn — `SOURCE_MODULE`

Một đơn vị tài liệu có identity, phạm vi authority, lifecycle và local routing riêng.

Không đồng nghĩa:

```text
file
lore subsystem
institution
faction
```

Một file có thể tạm chứa nhiều module cũ trong migration, nhưng kiến trúc đích cố gắng đưa ownership về một module rõ.

---

## Miền — `DOMAIN`

Phạm vi chủ đề/chức năng được dùng để định tuyến.

`DOMAIN` là khái niệm phân loại.

`MODULE` là đơn vị sở hữu tài liệu.

```text
DOMAIN != MODULE
```

---

## Nút nguồn — `SOURCE_NODE`

Đơn vị định tuyến ổn định bên trong module.

Một node phải đủ nguyên vẹn về nghĩa để được đọc độc lập cùng dependency của nó.

```text
NODE != HEADING
NODE != LINE RANGE
```

Heading có thể là vị trí hiển thị của node.

---

## Giao diện — `INTERFACE`

Boundary nơi hai hoặc nhiều module trao đổi trạng thái, quyền, thông tin, resource hoặc relation đã xác lập.

```text
INTERFACE != CONTAINMENT
```

---

## Hợp đồng giao diện — `INTERFACE_CONTRACT`

Bản mô tả source-level cho một interface:

```text
participants
what crosses
relation type
controller/authority
constraints
truth state
coverage
issue hooks
```

Không phải API phần mềm.

---

## Registry kiến trúc — `ARCHITECTURE_REGISTRY`

Nguồn cấu trúc dùng để biết module nào tồn tại, ở đâu và liên kết thế nào.

```text
REGISTRY != CANON
REGISTRY != WORLD BIBLE
```

Registry không có quyền tạo lore.

---

## Chỉ mục cục bộ — `LOCAL_ROUTING_INDEX`

Bảng node trong một module.

Nó giúp Router nhảy tới node và tính closure.

```text
LOCAL INDEX != GLOBAL REGISTRY
```

---

## Chế độ xem dẫn xuất — `DERIVED_VIEW`

File/tài liệu được sinh hoặc kiểm tra từ source cấu trúc khác để con người/model đọc nhanh.

Ví dụ mục tiêu tương lai:

```text
00
92
```

```text
DERIVED VIEW != AUTHORITY SOURCE
```

---

# 3. Authority và truth

## Thẩm quyền nguồn — `SOURCE_AUTHORITY`

Quy tắc quyết định source nào có quyền kiểm soát một claim trong một scope.

Không đồng nghĩa quyền lực trong lore.

---

## Phạm vi kiểm soát — `AUTHORITY_SCOPE`

Phần source mà module/file có quyền làm nguồn hiện hành.

Nếu hai module claim exclusive authority cùng scope:

```text
AUTHORITY_CONFLICT
```

---

## Trạng thái chân trị — `TRUTH_STATUS`

Ví dụ:

```text
CANON
UNCONFIRMED
UNKNOWN
DEFERRED
CONFLICTED
PROPOSAL
HISTORICAL
SUPERSEDED
```

Không trộn với module lifecycle hoặc coverage.

---

## Trạng thái mô-đun — `MODULE_STATUS`

Ví dụ:

```text
PROPOSED
REGISTERED
CURRENT
SPLITTING
SUPERSEDED
RETIRED
ARCHIVED
```

Một module `CURRENT` vẫn có node `UNKNOWN`.

---

# 4. Coverage

## Độ phủ — `COVERAGE`

Mức độ source mô tả đủ sâu tới đâu trong scope.

Đề xuất:

```text
REGISTERED
BOUNDARY_ONLY
PARTIAL
OPERABLE
DEEP
```

```text
COVERAGE != TRUTH_STATUS
COVERAGE != AUTHORITY
COVERAGE != QUALITY SCORE
```

---

## Đủ vận hành — `OPERABLE`

Source đủ để thực hiện một nhóm task đã khai báo mà không phải invent missing mechanism quyết định.

Không có nghĩa complete.

---

## Chỉ đủ boundary — `BOUNDARY_ONLY`

Biết module tồn tại và biết cách nó nối ra ngoài, nhưng nội bộ chưa được mô tả đủ để simulation sâu.

---

# 5. Routing

## Định tuyến — `ROUTING`

Chọn module/node/control source cần đọc cho task.

Không phải reasoning conclusion.

---

## Bao đóng tải — `LOAD_CLOSURE`

Tập tối thiểu gồm:

```text
target nodes
+ mandatory nodes
+ dependencies
+ interface records
+ issue/reconciliation evidence
+ overlay dependencies
```

đủ để thực hiện task an toàn.

---

## Tải toàn phần dự phòng — `FULL_READ_FALLBACK`

Chuyển từ node closure sang full file/domain read khi không chứng minh được closure.

Đây là safety mechanism, không phải failure.

---

## Chính sách tải — `LOAD_POLICY`

Đề xuất:

```text
ALWAYS
ON_DEMAND
FULL_SCOPE_ONLY
```

---

# 6. Dependency

## Phụ thuộc bắt buộc — `REQUIRES`

A không thể được hiểu/thực thi đúng trong task scope nếu thiếu B.

Không suy `REQUIRES` chỉ từ việc cùng xuất hiện.

---

## Phụ thuộc tùy chọn — `OPTIONALLY_USES`

B có thể cải thiện task nhưng không quyết định closure tối thiểu.

---

## Phụ thuộc ngược — `REVERSE_DEPENDENCY`

Danh sách consumer của một node/interface.

Dùng cho impact analysis.

---

## Bán kính ảnh hưởng — `BLAST_RADIUS`

Phạm vi một thay đổi có thể ảnh hưởng:

```text
LOCAL
BOUNDED_CROSS_MODULE
STRUCTURAL
GLOBAL
```

---

# 7. Cross-domain state

## Vấn đề mở — `OPEN_ISSUE`

Một câu hỏi/quan hệ cần user hoặc source mới giải quyết.

Không phải canon negation.

---

## Không rõ — `UNKNOWN`

Thiếu dữ liệu canon cho claim.

```text
UNKNOWN != FALSE
UNKNOWN != PROPOSAL
```

---

## Trì hoãn — `DEFERRED`

Được cố ý không giải quyết trong scope hiện tại.

---

## Xung đột — `CONFLICTED`

Có claim cạnh tranh không thể cùng đúng trong cùng scope và chưa được authority giải quyết.

---

## Mồ côi — `ORPHANED`

Một node/interface/dependency mất controlling parent hoặc target sau retcon/split/remove.

```text
ORPHANED != RETIRED
```

---

# 8. History và supersession

## Lịch sử thiết kế — `DESIGN_HISTORY`

Provenance của thiết kế.

Không phải current baseline.

---

## Bị thay thế — `SUPERSEDED`

Claim/source từng có authority nhưng đã bị claim/source mới thay trong scope xác định.

---

## Nghỉ hẳn — `RETIRED`

Không còn là phần hoạt động hiện hành.

---

## Lưu trữ — `ARCHIVED`

Được giữ vì provenance/bytes/history nhưng không active.

---

# 9. Validation

## Xác thực cấu trúc — `STRUCTURAL_VALIDATION`

Kiểm tra:

```text
registration
path
IDs
dependencies
interfaces
authority
cycles
views
orphans
schema
```

Không kiểm chứng sự thật lore.

---

## Cũ lệch — `STALE`

Metadata/view không còn phản ánh source revision mà nó tuyên bố mô tả.

Không suy stale chỉ từ ngày file.

---

## Tham chiếu treo — `DANGLING_REFERENCE`

Reference trỏ tới ID/path không resolve trong active package/schema.

---

## Trùng authority — `AUTHORITY_DUPLICATION`

Hai source cùng tự nhận controlling authority cho cùng exclusive scope mà không có contract chia scope.

---

## Trùng nội dung — `CONTENT_DUPLICATION`

Cùng một block/claim được copy sang nhiều source.

Không phải lúc nào cũng sai, nhưng rất nguy hiểm nếu cả hai cùng current-looking.

---

# 10. Build và view

## Sinh lại — `REGENERATE`

Tạo lại derived view từ registry/state.

---

## Bản dựng cấu trúc — `STRUCTURE_BUILD`

Bước chạy validator + generator sau structural change.

Không phải compile phần mềm theo nghĩa bắt buộc.

---

## Phiên bản schema — `SCHEMA_VERSION`

Version của contract metadata.

Tách khỏi:

```text
CI version
Router version
canon revision
module revision
```

---

# 11. Mutation

## Giao dịch thay đổi — `CHANGE_TRANSACTION`

Chuỗi:

```text
impact
→ load
→ edit
→ reconcile
→ validate
→ regenerate
→ report
```

Mục tiêu là không để một canon change hợp lệ tạo package state lệch.

---

## Thay đổi cục bộ — `LOCAL_CHANGE`

Không đổi public interface hoặc authority.

---

## Thay đổi cấu trúc — `STRUCTURAL_CHANGE`

Đổi:

```text
module boundary
authority
interface contract
schema
dependency topology
```

---

# 12. Graph separation

Bắt buộc phân biệt:

```text
LORE_GRAPH
DOCUMENT_GRAPH
SOURCE_AUTHORITY_GRAPH
DEPENDENCY_GRAPH
INTERFACE_GRAPH
INFORMATION_GRAPH
DESIGN_GENEALOGY_GRAPH
```

Không chuyển edge giữa graph nếu không có bridge rõ.

---

# 13. Các từ dễ gây drift và cách dùng

## `source`

Không dùng một mình nếu có thể nói rõ:

```text
current canon source
control source
historical source
derived view
registry
```

## `index`

Phải nói rõ:

```text
global source map
local routing index
registry
```

## `current`

Chỉ có nghĩa hiện hành trong lifecycle/authority scope.

Không có nghĩa:

```text
complete
deep
globally controlling
```

## `controlling`

Phải kèm scope.

Không có “controlling file” vô hạn scope.

## `dependency`

Phải có edge type.

## `module`

Trong tài liệu kiến trúc này nghĩa là source/control module, trừ khi ghi rõ lore module.

---

# 14. Quy tắc cho ChatGPT/Codex

Khi gặp một từ có prior phổ biến nhưng glossary đã định nghĩa:

```text
use glossary meaning
```

Nếu source cũ dùng từ khác:

```text
do not silently normalize semantics
```

Hãy map rõ:

```text
legacy term
→ architecture term
```

nếu cần.

Không biến glossary thành canon.
