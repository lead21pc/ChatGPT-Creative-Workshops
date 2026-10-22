# The Academy — M6 Semantic Migration Audit

**Trạng thái:** `PASS WITH CORRECTIONS APPLIED`.  
**Phạm vi:** đối chiếu bộ tài liệu tái cấu trúc M2–M5 với baseline/source hiện hành trước soft migration M7.  
**Mục tiêu:** phát hiện mất dữ kiện, nâng trạng thái tri thức, mạnh hóa relation hoặc đứt provenance.

## 1. Bộ nguồn được đối chiếu

Nguồn cũ / neo:

- `The_Academy_V1_5_Architecture_Baseline_Anti_Drift.md`
- `The_Academy_V1_5_Architecture_Handoff.md`
- `The_Academy_Authorial_Decisions_2026-09-28.md`
- `Narrative Engine — Core Design Philosophy.md`
- `The_Academy_CI_v2.0.md`
- `The_Academy_Source_Router_v1.0.md`

Nguồn mới:

- `The_Academy_Anti_Drift_Kernel.md`
- `The_Academy_Current_State.md`
- `The_Academy_V1_5_Architecture.md`
- `The_Academy_V1_5_Open_Registry.md`
- `The_Academy_V2_Architecture.md`
- `The_Academy_V2_5_Revise_Branch.md`
- `The_Academy_Source_Router_v1.1.md`

## 2. Gate A — mất canon / baseline fact

### Phát hiện ban đầu

Bản V1.5 Architecture đầu tiên đã rút gọn quá tay và làm mờ/mất ba nhóm dữ kiện:

1. cùng một world có thể được chọn qua nhiều recruitment cycle;
2. cấu hình sampling legacy chi tiết hơn con số `10 HIP/world`;
3. trường hợp external-project Greed + Lust cùng tiếp cận một HIP ở trạng thái existence-only.

Ngoài ra Wizard tower / protected forest chưa có nơi rõ trong bộ mới.

### Correction đã áp dụng

- phục hồi repeat-world recruitment như fact được phép dùng;
- phục hồi wording sampling legacy nhưng giữ rõ rằng nó không phải HIP definition;
- phục hồi Greed + Lust case với nhãn `EXISTENCE-ONLY`;
- thêm Wizard tower / protected forest vào Open Registry với trạng thái `LEGACY-LORE / AWAITING CONFIRMATION`.

### Kết quả

`PASS` sau correction.

## 3. Gate B — UNKNOWN bị nâng thành fact

Đã kiểm tra các nhóm:

- recruitment criteria/detection;
- repeat-world trigger;
- pass-recipient protocol;
- compensation implementation;
- cohort relation/lifetime;
- temporal ontology;
- institutional map;
- Teaching mechanism;
- Security authority/custody;
- curriculum/exam/placement;
- Lust interface;
- post-return handoff/concurrency.

Tất cả vẫn được giữ trong Open Registry dưới trạng thái mở.

```text
OPEN REGISTRY ≠ TODO LIST
UNKNOWN ≠ EMPTY
UNKNOWN ≠ PERMISSION TO INVENT
```

Kết quả: `PASS`.

## 4. Gate C — relation bị mạnh lên

Đã kiểm tra các failure mode:

```text
INTERACTION → CONTAINMENT
CO-OCCURRENCE → DEPENDENCY
MULTIPLE ENGINES → COMPOSITE
GENEALOGY → CURRENT HIERARCHY
IMPLEMENTATION → ENGINE IDENTITY
V2 → V1.5 DEFINITION
V2.5 → SUCCESSOR
```

Không có relation nào trong bộ mới được dùng để tự cấp các relation trên.

Academy Revise đã được tách thành `WORKING BRANCH`, loại bỏ hàm ý version ladder mặc định.

Kết quả: `PASS`.

## 5. Gate D — provenance bị đứt

Các nguồn mới đều dẫn ngược về baseline, handoff, authorial decisions, core philosophy hoặc source engine phù hợp.

Archive/genealogy tiếp tục được giữ nguyên.

Không có source cũ nào bị xóa trong M2–M6.

Kết quả: `PASS`.

## 6. Kiểm tra diff trước M7

So với `main`, branch trước khi ghi audit này:

- chỉ thêm file mới;
- không sửa hoặc xóa file cũ;
- baseline cũ và Router v1.0 vẫn còn nguyên.

Điều này bảo đảm safe fallback trước soft migration.

## 7. Kết luận M6

```text
SEMANTIC MIGRATION GATE: PASS

NO KNOWN CANON LOSS
NO UNKNOWN PROMOTION
NO RELATION STRENGTHENING
PROVENANCE PRESERVED
```

M7 được phép bắt đầu.

M7 chỉ đổi **default reading path / status pointers**. Nó không được xóa source cũ và không được dùng migration status như bằng chứng thay đổi canon.
