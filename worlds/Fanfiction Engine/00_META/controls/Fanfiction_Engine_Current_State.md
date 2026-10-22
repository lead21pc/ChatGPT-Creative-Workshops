# Fanfiction Engine — Current Repository State

**Trạng thái:** snapshot điều hướng hiện hành của repository sau soft migration M7.\
**Vai trò:** chỉ ra nguồn mặc định cần đọc. File này không tự tạo canon và không thắng nguồn scoped nếu có xung đột.

## 0. Tên hiện hành và phạm vi

| Hạng mục | Tên hiện hành | Nhãn lịch sử |
| --- | --- | --- |
| Toàn project/hệ mô phỏng | Fanfiction Engine | The Academy Project |
| Platform nội bộ | The Academy | Giữ tên platform |
| Miền nhân quả thể chế | Institutional Causality | V1.5 |
| Miền formalization/application của Narrative Engine | Narrative Engine Causality | V2 |
| Working branch | Academy Revise | V2.5 |

```text
FANFICTION ENGINE != THE ACADEMY PLATFORM
INSTITUTIONAL CAUSALITY CAN RUN WITHOUT NARRATIVE ENGINE CAUSALITY
NARRATIVE ENGINE CAUSALITY CAN RUN WITHOUT FULL INSTITUTIONAL CAUSALITY
COMPOSITION != REQUIRED SEQUENCE
LEGACY VERSION NUMBER != CURRENT HIERARCHY
```

Hai miền là hai operational halves của cùng Fanfiction Engine, có thể dùng độc lập và kết hợp theo source/configuration. Narrative Engine Causality không cần graduate của Institutional Causality. Chi tiết chưa externalize tiếp tục là `UNKNOWN`.

[WHAT_IS_FANFICTION_ENGINE.md](../../WHAT_IS_FANFICTION_ENGINE.md) giải thích mục đích và ranh giới project/platform. Các tên cũ trong genealogy, quyết định có ngày tháng và archive là provenance, không phải tên project/domain hiện hành. Control versions CI v2.0 và Router v1.1 vẫn giữ nguyên.

## 1. Lớp điều khiển

- CI hiện hành: [Fanfiction_Engine_CI_v2.0.md](Fanfiction_Engine_CI_v2.0.md)
- Router hiện hành: [Fanfiction_Engine_Source_Router_v1.1.md](Fanfiction_Engine_Source_Router_v1.1.md)
- Anti-drift kernel của Fanfiction Engine: [Fanfiction_Engine_Anti_Drift_Kernel.md](../../12_ANTI_DRIFT/Fanfiction_Engine_Anti_Drift_Kernel.md)

Trạng thái nạp CI/router/kernel vào ChatGPT Project runtime vẫn `UNVERIFIED`.

## 2. Kiến trúc Fanfiction Engine

### Institutional Causality

Nguồn kiến trúc mặc định:

- [Institutional_Causality_Architecture.md](../../02_FANFICTION_ENGINE_ARCHITECTURE/INSTITUTIONAL_CAUSALITY/Institutional_Causality_Architecture.md)
- [Institutional_Causality_Open_Registry.md](../../02_FANFICTION_ENGINE_ARCHITECTURE/INSTITUTIONAL_CAUSALITY/Institutional_Causality_Open_Registry.md)

Nguồn reconstruction/provenance vẫn giữ:

- [The_Academy_V1_5_Architecture_Baseline_Anti_Drift.md](../../02_FANFICTION_ENGINE_ARCHITECTURE/INSTITUTIONAL_CAUSALITY/The_Academy_V1_5_Architecture_Baseline_Anti_Drift.md)
- [The_Academy_V1_5_Architecture_Handoff.md](../../02_FANFICTION_ENGINE_ARCHITECTURE/INSTITUTIONAL_CAUSALITY/The_Academy_V1_5_Architecture_Handoff.md)

Institutional Causality dùng các thành phần thể chế và tương tác HIP-HIP như causal filters theo source. Trong cấu hình đầy đủ đã externalize, return to origin kết thúc runtime thể chế trước tốt nghiệp; không phải mọi cách dùng đều cần một full school narrative. The Academy platform cùng miền này có thể giải thích historical absence/timeline skip trong configuration phù hợp mà không tự điền cơ chế chưa có nguồn.

### Narrative Engine Causality

Nguồn kiến trúc mặc định:

- [Narrative_Engine_Causality_Architecture.md](../../02_FANFICTION_ENGINE_ARCHITECTURE/NARRATIVE_ENGINE_CAUSALITY/Narrative_Engine_Causality_Architecture.md)

Narrative Engine Causality formalize/áp dụng engine theo host rules và target/context; application có thể chạy không cần toàn bộ Institutional Causality.

Nguồn phương pháp nền:

- [Narrative Engine — Core Design Philosophy.md](../Narrative%20Engine%20%E2%80%94%20Core%20Design%20Philosophy.md)

### Academy Revise

Nguồn working branch:

- [Academy_Revise_Branch.md](../../02_FANFICTION_ENGINE_ARCHITECTURE/BRANCHES/Academy_Revise_Branch.md)

```text
ACADEMY REVISE
= WORKING BRANCH
≠ AUTOMATIC SUCCESSOR
≠ CURRENT ONTOLOGY BY VERSION NUMBER
```

## 3. HIP

Nguồn chính:

- [Historical_Influence_Potential.md](../../01_HIP/Historical_Influence_Potential.md)

HIP là cổng đánh giá mở; tiêu chí đến từ context và HIP không tự bảo đảm outcome lịch sử.

## 4. Engine và miền vận hành đã được xác nhận

| Hạng mục | Trạng thái hiện hành | Nguồn dẫn |
| --- | --- | --- |
| Chaos | Canon Specification v3 là bản chính thức | [Chaos v3](../../04_NARRATIVE_ENGINES/Chaos/Chaos_Engine_Canon_Specification_v3.md) |
| Sloth | Mode Narrative Engine Causality | [Authorial Decisions](../../The_Academy_Authorial_Decisions_2026-09-28.md) |
| Wrath | Mode Narrative Engine Causality | [Authorial Decisions](../../The_Academy_Authorial_Decisions_2026-09-28.md) |
| Chaos | Mode Narrative Engine Causality | [Authorial Decisions](../../The_Academy_Authorial_Decisions_2026-09-28.md) |
| Lust | Thuộc Institutional Causality; chi tiết institutional role/interface/authority còn source-bound | [Lust Working Draft](../../03_INSTITUTIONAL_ENGINES/Lust/Lust_Working_Draft.md) |
| Greed Governor | Responsibility | [Authorial Decisions](../../The_Academy_Authorial_Decisions_2026-09-28.md) |

Các nhãn này ánh xạ các xác nhận legacy V2/V1.5 sang tên hiện hành; hồ sơ xác nhận có ngày tháng vẫn giữ nguyên cách gọi cũ. Chúng không cấp cùng architecture, capability hoặc authority cho engine khác; không tự gán mode cho Greed hoặc future engine.

## 5. Provenance và nguồn cũ

- [M6 Semantic Migration Audit](../The_Academy_M6_Semantic_Migration_Audit.md) ghi gate trước soft migration.
- [engine genealogy](../../06_ENGINE_GENEALOGY/engine_genealogy_and_development_updated.md) mô tả lịch sử hình thành; genealogy không tự tạo current hierarchy.
- [source_archive](../../source_archive/README.md) giữ nguồn cũ và bản nháp để truy vết.
- [The_Academy_Authorial_Decisions_2026-09-28.md](../../The_Academy_Authorial_Decisions_2026-09-28.md) ghi các xác nhận tác giả đã externalize tại thời điểm đó.
- [Source Router v1.0](The_Academy_Source_Router_v1.0.md) được giữ để đối chiếu provenance sau khi v1.1 trở thành router hiện hành.

## 6. Quy tắc đọc snapshot

Nếu file này và nguồn được liên kết bất đồng:

```text
repair CURRENT STATE
≠ use CURRENT STATE to override scoped source
```

Snapshot tồn tại để giảm chi phí tìm nguồn, không phải để tạo thêm một tầng thẩm quyền.
