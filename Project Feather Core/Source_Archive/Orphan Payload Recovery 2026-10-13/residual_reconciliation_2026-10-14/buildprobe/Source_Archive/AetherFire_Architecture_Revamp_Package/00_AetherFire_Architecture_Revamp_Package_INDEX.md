# AetherFire — Gói đề xuất tái kiến trúc nguồn và CI

> **Trạng thái:** `PROPOSAL / ARCHITECTURE AUDIT`  
> **Không phải:** canon, world bible, retcon, thay đổi source authority, hoặc quyết định triển khai đã được chấp nhận.  
> **Mục tiêu:** xử lý tận gốc vấn đề AetherFire tăng nhanh theo chiều rộng trong khi độ sâu cập nhật giữa các miền không đồng đều; giảm tải đọc, giảm drift, giảm duplication và làm kiến trúc có thể mở rộng bằng mô-đun mà không phải đập đi xây lại.
>
> **Phạm vi bằng chứng của gói này:** các source/control file hiện có trong Project ở thời điểm tạo gói, đặc biệt Router v3.2, `00`, `10`–`70`, `90`–`92`, các anti-drift overlay và mô hình hub. Những file được source hiện tại tham chiếu nhưng không có trong gói làm việc này được coi là **cần Codex xác minh trong repository**, không bị kết luận là đã mất.

---

## 1. Tại sao cần một đợt tái kiến trúc cấp hệ thống

Vấn đề hiện tại không còn chỉ là “file dài”.

AetherFire đang đi vào trạng thái:

```text
độ rộng lore / số miền / số giao diện
tăng nhanh hơn
độ sâu cập nhật và khả năng đồng bộ từng miền
```

Nếu tiếp tục kiến trúc hiện tại:

```text
thêm miền
→ thêm file
→ thêm route
→ thêm UNKNOWN
→ thêm cross-domain dependency
→ thêm reconciliation
→ thêm anti-drift applicability
→ tăng số nguồn phải đọc

nhưng

không có:
- chuẩn mô-đun chung;
- registry cấu trúc duy nhất;
- dependency graph có thể kiểm tra;
- coverage model;
- reverse-impact analysis;
- validation tự động;
- quy trình split/merge module ổn định.
```

Điểm gãy không phải “hết chỗ lưu lore”.

Điểm gãy là:

```text
chi phí chứng minh một câu trả lời đúng
+
chi phí chứng minh một thay đổi không làm drift
>
chi phí tạo lore mới
```

Khi đó Project trở thành hệ thống khó duy trì dù canon vẫn có chất lượng cao.

---

## 2. Luận điểm kiến trúc trung tâm

Chuyển từ mô hình:

```text
FILE-CENTRIC CLOSED PACKAGE
```

sang:

```text
OPEN MODULAR SOURCE GRAPH
```

với các nguyên tắc:

```text
CI
→ quản lý luật nền và invariant

Router
→ tính toán tập nguồn cần đọc

Registry
→ mô tả topology của source, không chứa canon

Module
→ sở hữu canon/control trong phạm vi rõ ràng

Node
→ đơn vị định tuyến ổn định trong module

Interface
→ hợp đồng giao tiếp giữa các module

Issue / Reconciliation
→ trạng thái và provenance riêng

Derived View
→ chỉ mục/tổng hợp được sinh hoặc kiểm tra từ registry

Validator
→ phát hiện drift cấu trúc trước khi model phải tự suy
```

Không dùng một “mega-index” mới để thay thế một monolith cũ.

---

## 3. Các tài liệu trong gói

1. `01_ARCHITECTURE_PAIN_AND_BREAKPOINT_AUDIT.md`  
   Kiểm toán pain point, breakpoint và bằng chứng cụ thể trong cấu trúc hiện tại.

2. `02_GLOBAL_INTEGRATED_SOLUTION_ARCHITECTURE.md`  
   Kiến trúc đích toàn cục và cách các giải pháp phối hợp với nhau.

3. `03_MODULAR_EXPANSION_FRAMEWORK.md`  
   Khung mô-đun dùng lâu dài khi lore, hệ thống và kiểu kiến trúc mới tiếp tục được thêm vào.

4. `04_ARCHITECTURE_GLOSSARY.md`  
   Bộ thuật ngữ chuẩn để ChatGPT, Codex và tài liệu không tự dùng prior quen thuộc rồi hiểu sai quan hệ.

5. `05_CI_REVAMP_PROPOSAL.md`  
   Đề xuất nâng CI theo hướng kernel ổn định + registry/module động; khuyến nghị major-version bump.

6. `06_MANAGEMENT_FILE_SUITE_PROPOSAL.md`  
   Đề xuất bộ file/quy trình quản lý tối thiểu cần thêm và những file không nên tạo.

7. `07_CODEX_DEEP_ARCHITECTURE_AUDIT_AND_REVAMP_PROMPT.md`  
   Prompt cấp cao để Codex audit repository thật, tìm thêm rủi ro ngoài danh sách này và chuẩn bị triển khai.

---

## 4. Thứ tự đọc khuyến nghị

```text
01 Audit
↓
02 Kiến trúc đích
↓
03 Khung mô-đun
↓
04 Glossary
↓
05 CI
↓
06 File quản lý
↓
07 Prompt Codex
```

Không nên triển khai `NODE_ROUTING` riêng trước rồi mới nghĩ về registry, coverage và validation.

Nếu làm như vậy, hệ thống chỉ chuyển từ:

```text
đọc quá nhiều
```

sang:

```text
đọc ít hơn nhưng không chứng minh được đã đọc đủ
```

---

## 5. Quyết định lớn được đề xuất

### Quyết định A — Major revamp thay vì vá nối tiếp

Đề xuất xem thay đổi này là một lần thay hợp đồng kiến trúc và cân nhắc:

```text
AetherFire CI v3.0
Source Router v4.0
Architecture Schema v1
```

Tên/version cuối cùng do user quyết định.

Lý do: thay đổi này sửa semantics của routing, module registration, derived views, dependency closure và canon-mutation impact. Đây không còn là chỉnh nhỏ.

### Quyết định B — CI không được liệt kê inventory của thế giới

CI phải biết:

```text
cách route
cách xác định authority
cách xử lý UNKNOWN
cách module tương tác
cách kiểm tra mutation
```

CI không nên phải biết:

```text
hiện có 10 / 20 / 30 / 40 / 50 / 60 / 70 / 80 nào
```

Inventory thuộc registry.

### Quyết định C — Mỗi module tự sở hữu node của nó

Không xây global node registry chứa từng section của toàn Project.

Global registry chỉ cần biết module và interface chính.

Node map thuộc module.

### Quyết định D — Cross-domain relation phải có nơi sở hữu

Quan hệ chéo không được tồn tại bằng cách copy cùng một lore block vào hai file.

Phải có:

```text
one controlling interface record
+
module-local references / summaries
```

### Quyết định E — `00` và `92` nên là derived view

Các file này hữu ích cho con người/model.

Nhưng nếu chúng vừa là generated view vừa được bảo trì thủ công như authority-like index, chúng sẽ drift.

Đề xuất:

```text
registry / issue records
→ generate or validate
→ 00 / 92
```

### Quyết định F — Coverage khác Truth Status

Một node có thể:

```text
CANON + INTERFACE_ONLY
CANON + DEEP
UNKNOWN + DEEP_ANALYSIS
PROPOSAL + DETAILED
```

Không được dùng độ dài source để suy độ chắc chắn.

---

## 6. Tiêu chí thành công

Tái kiến trúc đạt mục tiêu khi:

```text
thêm một module mới
≠ sửa CI

thêm một module mới
≈
register module
+ define authority boundary
+ define public interfaces
+ define local nodes
+ validate
```

và:

```text
sửa một node
→ biết các dependency trực tiếp
→ biết interface nào bị ảnh hưởng
→ biết open issue nào liên quan
→ biết khi nào phải full-read
```

và:

```text
một câu hỏi cục bộ
→ không phải đọc cả domain file dài

một audit toàn miền
→ vẫn bắt buộc full-read
```

và:

```text
generated view stale
→ validator phát hiện
```

thay vì model phải đoán.

---

## 7. Điều tuyệt đối không làm

```text
- Không biến registry thành canon.
- Không dùng coverage để điền UNKNOWN.
- Không split source chỉ để file ngắn.
- Không tạo một registry cho mỗi loại quan hệ nhỏ.
- Không copy canon để “tiện đọc”.
- Không cho CI biết danh sách domain cụ thể nếu registry có thể cung cấp.
- Không cho Router tự suy dependency từ từ khóa.
- Không dùng line number làm định danh ổn định.
- Không để generated view trở thành nguồn authority thứ hai.
- Không biến proposal kiến trúc thành thay đổi canon.
```
