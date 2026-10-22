# The Academy — Current Repository State

**Trạng thái:** snapshot điều hướng hiện hành của repository sau soft migration M7.  
**Vai trò:** chỉ ra nguồn mặc định cần đọc. File này không tự tạo canon và không thắng nguồn scoped nếu có xung đột.

## 1. Lớp điều khiển

- CI hiện hành: [The_Academy_CI_v2.0.md](The_Academy_CI_v2.0.md)
- Router hiện hành: [The_Academy_Source_Router_v1.1.md](The_Academy_Source_Router_v1.1.md)
- Anti-drift kernel của The Academy: [The_Academy_Anti_Drift_Kernel.md](../../12_ANTI_DRIFT/The_Academy_Anti_Drift_Kernel.md)

Trạng thái nạp CI/router/kernel vào ChatGPT Project runtime vẫn `UNVERIFIED`.

## 2. Kiến trúc The Academy

### V1.5

Nguồn kiến trúc mặc định:

- [The_Academy_V1_5_Architecture.md](../../02_ACADEMY_ARCHITECTURE/V1_5/The_Academy_V1_5_Architecture.md)
- [The_Academy_V1_5_Open_Registry.md](../../02_ACADEMY_ARCHITECTURE/V1_5/The_Academy_V1_5_Open_Registry.md)

Nguồn reconstruction/provenance vẫn giữ:

- [The_Academy_V1_5_Architecture_Baseline_Anti_Drift.md](../../02_ACADEMY_ARCHITECTURE/V1_5/The_Academy_V1_5_Architecture_Baseline_Anti_Drift.md)
- [The_Academy_V1_5_Architecture_Handoff.md](../../02_ACADEMY_ARCHITECTURE/V1_5/The_Academy_V1_5_Architecture_Handoff.md)

V1.5 vẫn là miền nhân quả thể chế trước tốt nghiệp và kết thúc ở return to origin.

### V2

Nguồn kiến trúc mặc định:

- [The_Academy_V2_Architecture.md](../../02_ACADEMY_ARCHITECTURE/V2/The_Academy_V2_Architecture.md)

Nguồn phương pháp nền:

- [Narrative Engine — Core Design Philosophy.md](../Narrative%20Engine%20%E2%80%94%20Core%20Design%20Philosophy.md)

### V2.5 / Academy Revise

Nguồn working branch:

- [The_Academy_V2_5_Revise_Branch.md](../../02_ACADEMY_ARCHITECTURE/BRANCHES/The_Academy_V2_5_Revise_Branch.md)

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

## 4. Engine và mode hiện đã xác nhận trong repository

| Hạng mục | Trạng thái hiện hành | Nguồn dẫn |
| --- | --- | --- |
| Chaos | Canon Specification v3 là bản chính thức | [Chaos v3](../../04_NARRATIVE_ENGINES/Chaos/Chaos_Engine_Canon_Specification_v3.md) |
| Sloth | Mode V2 | [Authorial Decisions](../../The_Academy_Authorial_Decisions_2026-09-28.md) |
| Wrath | Mode V2 | [Authorial Decisions](../../The_Academy_Authorial_Decisions_2026-09-28.md) |
| Chaos | Mode V2 | [Authorial Decisions](../../The_Academy_Authorial_Decisions_2026-09-28.md) |
| Lust | Thuộc V1.5; chi tiết institutional role/interface/authority còn source-bound | [Lust Working Draft](../../03_V1_5_INSTITUTIONAL_ENGINES/Lust/Lust_Working_Draft.md) |
| Greed Governor | Responsibility | [Authorial Decisions](../../The_Academy_Authorial_Decisions_2026-09-28.md) |

Các nhãn này không cấp cùng architecture, capability hoặc authority cho engine khác.

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
