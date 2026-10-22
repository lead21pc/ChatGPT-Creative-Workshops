# Fanfiction Engine — Source Router v1.1

**Trạng thái:** router nguồn hiện hành trong repository sau soft migration M7. Việc môi trường ChatGPT Project tự nạp file này vẫn `UNVERIFIED`.  
**Vai trò:** chọn nguồn gần nhất đủ trả lời theo domain và loại yêu cầu.  
**Không làm:** không tạo canon, không giữ bản sao của canon engine-specific, không lấp `UNKNOWN`, không cấp capability hoặc authority.

Đọc trước:

1. [Fanfiction Engine Current Repository State](Fanfiction_Engine_Current_State.md) để biết nguồn hiện hành;
2. [Fanfiction Engine Anti-Drift Kernel](../../12_ANTI_DRIFT/Fanfiction_Engine_Anti_Drift_Kernel.md) khi câu hỏi có nguy cơ drift kiến trúc;
3. nguồn scoped gần nhất đủ cho yêu cầu.

Fanfiction Engine là toàn hệ; The Academy là platform nội bộ. Institutional Causality và Narrative Engine Causality là hai miền dùng độc lập hoặc kết hợp theo configuration, không phải pipeline bắt buộc. Nhãn lịch sử V1.5/V2 và V2.5 được ánh xạ tại Current State; Academy Revise vẫn là working branch.

## 1. Nguyên tắc routing

```text
REQUEST
→ determine operation/domain
→ read current-state pointer if authority matters
→ apply Fanfiction Engine anti-drift boundary
→ open smallest sufficient scoped source
→ expand only when a relation/provenance/UNKNOWN requires it
```

```text
ROUTER SELECTS SOURCES
ROUTER DOES NOT DEFINE THEIR CONTENT
```

Tên file, số version, vị trí thư mục và việc cùng xuất hiện không tự xác lập thẩm quyền, hierarchy, dependency hoặc canon.

## 2. Chọn nguồn theo domain

| Domain / yêu cầu | Nguồn bắt đầu | Mở thêm khi cần |
| --- | --- | --- |
| Trạng thái hiện hành của repository, source nào đang active | [Current State](Fanfiction_Engine_Current_State.md) | Nguồn được Current State trỏ tới |
| Ranh giới chống drift chung của Fanfiction Engine | [Fanfiction Engine Anti-Drift Kernel](../../12_ANTI_DRIFT/Fanfiction_Engine_Anti_Drift_Kernel.md) | Source scoped nếu cần fact cụ thể |
| HIP, tiêu chí đánh giá, target | [Historical Influence Potential](../../01_HIP/Historical_Influence_Potential.md) | Institutional Causality hoặc engine source nếu context yêu cầu |
| Institutional Causality, recruitment, cohort, institution, teaching, graduation | [Institutional Causality Architecture](../../02_FANFICTION_ENGINE_ARCHITECTURE/INSTITUTIONAL_CAUSALITY/Institutional_Causality_Architecture.md) | [Institutional Causality Open Registry](../../02_FANFICTION_ENGINE_ARCHITECTURE/INSTITUTIONAL_CAUSALITY/Institutional_Causality_Open_Registry.md), Handoff, legacy source |
| Institutional Causality unknown/open boundaries | [Institutional Causality Open Registry](../../02_FANFICTION_ENGINE_ARCHITECTURE/INSTITUTIONAL_CAUSALITY/Institutional_Causality_Open_Registry.md) | Source gốc được registry/provenance trỏ tới |
| Narrative Engine Causality, Host Fiction, World Bible, target, Local Realization | [Narrative Engine Causality Architecture](../../02_FANFICTION_ENGINE_ARCHITECTURE/NARRATIVE_ENGINE_CAUSALITY/Narrative_Engine_Causality_Architecture.md) | [Core Design Philosophy](<../Narrative Engine — Core Design Philosophy.md>) và engine source |
| Academy Revise | [Academy Revise Branch](../../02_FANFICTION_ENGINE_ARCHITECTURE/BRANCHES/Academy_Revise_Branch.md) | Institutional Causality/Narrative Engine Causality Architecture để kiểm tra input boundary |
| Greed / Ring | [Greed Core v0.2](../../04_NARRATIVE_ENGINES/Greed/Greed_Narrative_Engine_Core_v0.2_Working_Draft.md) | [Ring Interface](../../04_NARRATIVE_ENGINES/Greed/Ring_Interface_v0.1_Working_Draft.md), Greed II implementation, archive source |
| Sloth | [Sloth Engine](../../04_NARRATIVE_ENGINES/Sloth/Sloth_Engine_Working_Draft.md) | Accommodation/Graze/The Gun khi cơ chế đó liên quan |
| Wrath | [Wrath Working Draft](../../04_NARRATIVE_ENGINES/Wrath/Wrath_Working_Draft.md) | Chỉ tách engine/entity/host-specific state theo chính source |
| Chaos | [Chaos v3](../../04_NARRATIVE_ENGINES/Chaos/Chaos_Engine_Canon_Specification_v3.md) | Archive `updated` chỉ khi cần provenance |
| Lust | [Lust Working Draft](../../03_INSTITUTIONAL_ENGINES/Lust/Lust_Working_Draft.md) | Institutional Causality Architecture khi câu hỏi liên quan institutional context |
| Greed II hoặc implementation cụ thể | [Greed II Implementation](../../08_LORE_IMPLEMENTATIONS/Greed_II/Greed_II_Implementation_v0.1_Working_Draft.md) | Engine source để phân biệt implementation với invariant |
| Lịch sử hình thành / genealogy | [Engine Genealogy](../../06_ENGINE_GENEALOGY/engine_genealogy_and_development_updated.md) | Current architecture để tránh genealogy → hierarchy |
| Nguồn cũ / superseded / mâu thuẫn lịch sử | [source_archive](../../source_archive/README.md) | Nguồn hiện hành tương ứng |
| Workflow nhiều paracosm | [multi-paracosm hub workflow](../multi_paracosm_hub_workflow.md) | Chỉ khi yêu cầu thực sự đi qua nhiều paracosm |

## 3. Quy tắc theo loại yêu cầu

### Giải thích

Đọc source scoped gần nhất và giữ nguyên trạng thái canon/working/unknown.

### Audit

Đọc architecture/kernel trước, sau đó source scoped và provenance cần thiết.

Không biến finding thành redesign nếu user chỉ yêu cầu audit.

### Mô phỏng

Đọc engine source + host/world rules + target/context.

Không preselect open outcome.

### Đối chiếu version/provenance

Đọc Current State + source hiện hành + archive/genealogy cần thiết.

```text
NEWER FILE
≠ AUTOMATIC SUPERSESSION
```

Supersession phải có xác nhận.

### Thiết kế / proposal

Đọc current architecture và open boundary liên quan trước.

Proposal phải được giữ là proposal cho đến khi tác giả xác nhận.

## 4. Ranh giới nguồn

### Institutional Causality

Trong cấu hình đầy đủ đã externalize, return to origin kết thúc runtime thể chế trước tốt nghiệp; các causal filters riêng không bắt buộc đi hết school arc.

Không dùng operation hậu return của cấu hình đó để viết ngược ràng buộc của miền thể chế trước tốt nghiệp.

### Narrative Engine Causality

Narrative Engine Causality Architecture là nguồn architecture; engine-specific source vẫn quyết định cơ chế của từng engine. Application không cần graduate hoặc toàn bộ Institutional Causality; chỉ dùng host/source/configuration cho phép.

### Academy Revise

Academy Revise là working branch; nhãn lịch sử V2.5 không xác lập giai đoạn thứ ba, successor hoặc thống nhất tự động.

### Genealogy

Genealogy mô tả lịch sử hình thành.

```text
GENEALOGY ≠ CURRENT HIERARCHY
```

### Archive

Archive giữ provenance.

```text
ARCHIVED
≠ FALSE
≠ ACTIVE BY DEFAULT
```

## 5. Quy trình tối thiểu

1. Xác định operation: giải thích, audit, mô phỏng, đối chiếu, thiết kế hay continuation.
2. Xác định domain: HIP, Institutional Causality, Narrative Engine Causality, Academy Revise, engine, implementation, genealogy hoặc archive.
3. Nếu authority/current status quan trọng, đọc Current State.
4. Đọc source scoped gần nhất.
5. Mở thêm source chỉ khi một relation, conflict, host rule hoặc provenance thực sự cần kiểm tra.
6. Giữ `UNKNOWN`, `OPEN`, working và proposal đúng trạng thái.
7. Không suy hierarchy/dependency/capability từ file placement hoặc co-occurrence.

## 6. Không nhân bản state engine-specific

Router v1.1 cố ý không chứa bảng kiểu:

```text
Greed Governor = ...
Chaos official = ...
Sloth mode = ...
```

Các fact hiện hành thuộc Current State và nguồn engine/xác nhận tương ứng.

Điều này cho phép source engine thay đổi mà không phải sửa Router nếu đường routing không đổi.

## 7. Final rule

```text
ROUTE TO THE NEAREST SUFFICIENT SOURCE.

DO NOT TURN THE ROUTER INTO A SECOND CANON.
```
