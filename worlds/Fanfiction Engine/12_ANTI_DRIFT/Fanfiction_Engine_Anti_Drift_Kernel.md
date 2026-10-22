# Fanfiction Engine — Anti-Drift Kernel

**Trạng thái:** tài liệu kiểm soát cách đọc Fanfiction Engine trong repository.\
**Phạm vi:** bảo vệ ranh giới kiến trúc và trạng thái tri thức; không tạo canon, không thay engine specification, không thay CI.

## 0. Quy tắc sử dụng

Kernel này không phải world bible, không phải bản tóm tắt toàn bộ Fanfiction Engine và không phải nguồn để điền các khoảng trống.

Khi nguồn cụ thể của engine, mode, implementation hoặc xác nhận tác giả nói rõ hơn, dùng nguồn đó trong đúng phạm vi của nó.

## 1. Thẩm quyền và trạng thái tri thức

- Chỉ tác giả/người dùng xác nhận mới thay đổi canon.
- Xác nhận mới có phạm vi rõ ưu tiên hơn nguồn cũ trong đúng phạm vi đó.
- Draft vẫn là draft cho đến khi được xác nhận.
- Xung đột chưa có supersession phải giữ provenance thay vì tự hợp nhất.

```text
UNKNOWN ≠ EMPTY
UNKNOWN ≠ PERMISSION TO INVENT

WORKING ≠ CANON
PROPOSAL ≠ CANON

EXISTENCE-ONLY
≠ REFERENCE DATA
```

Một chi tiết chỉ được xác nhận là đã tồn tại không tự cung cấp cơ chế, tiêu chí, phân bố, outcome hoặc dữ liệu để suy rộng.

## 2. Bản sắc Fanfiction Engine và The Academy platform

Fanfiction Engine là toàn hệ fanfiction/daydream simulation. The Academy là platform nội bộ hợp thức hóa các chuyển tiếp xuyên fiction/reality theo source/configuration; platform không đồng nhất với project.

```text
FANFICTION ENGINE != THE ACADEMY PLATFORM
```

Historical Influence Potential (HIP) là cổng đánh giá mở dùng tiêu chí từ context.

```text
HIP
≠ universal score
≠ power scale
≠ morality scale
≠ protagonist marker
≠ guaranteed historical change
```

Institutional Causality (legacy: V1.5) là miền nhân quả thể chế của Fanfiction Engine, dùng The Academy và các causal filters theo source; không xoay quanh một protagonist hoặc full school arc bắt buộc.

```text
RETURN TO ORIGIN
= TERMINUS OF THE DOCUMENTED FULL PRE-GRAD CONFIGURATION
```

Narrative Engine Causality (legacy: V2) là miền formalization/application của Narrative Engine theo Host Fiction, World Bible, target và context. Nó có thể chạy không cần graduate hoặc toàn bộ Institutional Causality.

```text
Narrative Engine
≠ story
≠ trope
≠ prompt
≠ fixed plot
≠ one specific implementation
```

Institutional Causality có thể chạy không cần Narrative Engine Causality; hai miền có thể kết hợp theo source/configuration. Sự kết hợp không tự tạo dependency hoặc thứ tự bắt buộc.

```text
Institutional Causality ≠ deprecated because Narrative Engine Causality exists
Narrative Engine Causality ≠ authority to redefine Institutional Causality retroactively
COMPOSITION != REQUIRED SEQUENCE
LEGACY VERSION NUMBER / GENEALOGY != CURRENT HIERARCHY
```

## 3. Quan hệ và cấu trúc

Mặc định dùng các node độc lập và quan hệ có loại khi source xác nhận.

```text
INTERACTION ≠ CONTAINMENT
CO-OCCURRENCE ≠ DEPENDENCY
TEMPORARY COMPOSITION ≠ PERMANENT COUPLING
REPEATED USE TOGETHER ≠ SUBSYSTEM STATUS
GENEALOGY ≠ CURRENT HIERARCHY
PRESENTATION ORDER ≠ ONTOLOGY
FILE LOCATION ≠ ONTOLOGY
IMPLEMENTATION ≠ ENGINE
```

Không tạo quan hệ chỉ để graph trông đầy đủ hơn.

## 4. Bất đối xứng engine

Greed, Sloth, Wrath, Chaos, Lust và các engine tương lai không bắt buộc dùng cùng kiến trúc nội bộ.

Không ép mọi engine vào một mẫu kiểu:

```text
Governor
+ Catalyst
+ Counter
+ Doctrine
+ Tool
```

Một primitive hoặc cơ chế có ở một engine không cấp primitive hoặc cơ chế đó cho engine khác.

Một actor, host, weapon, interface hoặc implementation cụ thể không tự trở thành identity phổ quát của engine.

Composite chỉ tồn tại khi source xác nhận quan hệ hợp thành; nhiều engine cùng tác động lên một HIP không tự tạo composite hoặc dependency.

## 5. Agency, thông tin và authority

Engine có thể thay đổi điều kiện, áp lực, exposure, option space hoặc quan hệ. Điều đó không tự quyết định lựa chọn và outcome của actor/HIP.

```text
POWER ≠ AUTHORITY
ACCESS ≠ KNOWLEDGE
ABILITY ≠ AUTHORIZATION
INTENT ≠ EXECUTION
PRESSURE ≠ PREDETERMINED OUTCOME
```

Actor chỉ được dùng thông tin, quyền và khả năng mà source hoặc simulation state cho phép.

Không cho actor đọc hidden canon, future, author intent hoặc toàn bộ engine architecture nếu không có đường truy cập hợp lệ.

## 6. Failure modes đặc thù Fanfiction Engine

### 6.1. School-prior collapse

Không tự ép Institutional Causality về mô hình trường học thông thường:

```text
Academy
→ faculty
→ department
→ course
→ linear student progression
```

nếu source chưa xác nhận.

### 6.2. HIP metric collapse

Không lấy một bộ tiêu chí cụ thể, một nhóm HIP hoặc một lớp target làm định nghĩa phổ quát của HIP.

### 6.3. Faction-name collapse

Tên domain hoặc faction không tự chứng minh một Narrative Engine hoàn chỉnh.

### 6.4. Department explosion

Không biến mọi specialization hoặc component thành faction/engine.

### 6.5. One-template-for-all-engines

Không dùng cấu trúc của Greed, Sloth, Wrath, Chaos hoặc Lust làm schema bắt buộc cho engine khác.

### 6.6. Narrative Engine Causality back-defines Institutional Causality

Không suy rằng formalization muộn của Narrative Engine Causality cho biết Institutional Causality "thật ra phải là gì".

### 6.7. Implementation → universal invariant

Greed II, The Tainted Cosmos, Ring, The Gun hoặc một host-specific realization không tự trở thành invariant của engine nếu source không nói vậy.

### 6.8. Graduate population → fabricated dataset

Việc nhiều graduate từng tồn tại không cho phép dựng demographic, success rate, trajectory hoặc example outcome chưa externalize.

### 6.9. Legacy lore → current ontology

Legacy lore chỉ được dùng đúng trạng thái và phạm vi của nguồn.

### 6.10. UNKNOWN → standard content

Không tự lấp vùng mở bằng prior về school fiction, Seven Deadly Sins, worldbuilding, game design hoặc software architecture.

## 7. Quy tắc cuối

Giản lược câu chữ khi cần, nhưng không giản lược quan hệ đến mức làm sai kiến trúc.

Khi dữ kiện thiếu:

```text
preserve UNKNOWN
→ inspect scoped source
→ state minimum assumption only if needed
→ label proposal explicitly
```

Không tạo ontology chỉ để tài liệu trông hoàn chỉnh.
