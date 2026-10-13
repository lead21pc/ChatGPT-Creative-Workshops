# AetherFire — Đề xuất bộ file quản lý tối thiểu

> **Trạng thái:** `PROPOSAL`
>
> Mục tiêu: thêm đủ file để scale, nhưng không tạo một lớp “management lore” khổng lồ.

---

# 1. Nguyên tắc

Không tạo một file quản lý cho mỗi vấn đề.

Đề xuất chỉ có **ba source cấu trúc mới thật sự cần thiết**, còn phần lớn thông tin ở local module.

```text
1. ARCHITECTURE_REGISTRY
2. INTERFACE_REGISTRY
3. ARCHITECTURE_CHANGE_LOG
```

Các view như `00/92` được sinh hoặc validate từ chúng và source hiện tại.

---

# 2. File 1 — `ARCHITECTURE_REGISTRY.yaml`

## Vai trò

Inventory của module/control source.

Không chứa canon.

Schema mẫu:

```yaml
schema_version: 1

modules:
  - module_id: AF.WORLD
    path: 10_WORLD_INSTITUTIONS_GEOPOLITICS_CURRENT.md
    type: current_canon
    status: CURRENT
    authority_scope:
      - global_state
      - cross_domain_geopolitics
    coverage: PARTIAL
    local_index: embedded
    exposes:
      - IF.AF_ML
      - IF.AF_RF
    requires: []

  - module_id: AF.ML
    path: 70_MATRIARCHS_LAMENT_CURRENT.md
    type: current_canon
    status: CURRENT
    authority_scope:
      - matriarchs_lament_internal
    coverage: OPERABLE
    local_index: embedded
```

## Không chứa

```text
full node list của mọi module
full lore
open issue prose
reconciliation evidence
```

Node list thuộc local index của module.

---

# 3. File 2 — `INTERFACE_REGISTRY.yaml`

## Tại sao cần riêng

Cross-domain relation là nơi complexity tăng nhanh nhất.

Nếu để relation nằm trong cả hai module:

```text
duplication
```

Nếu để trong một module bất kỳ:

```text
ownership bias
```

Dedicated interface registry giải quyết boundary.

Schema mẫu:

```yaml
schema_version: 1

interfaces:
  - interface_id: IF.AF_ML.RELIC_ACCESS
    participants:
      - AF.WORLD
      - AF.ML
    relation_type: DEPENDS_ON
    direction: ML_TO_AF_ACCESS
    controlling_nodes:
      - AF.ML:RELIC_ACCESS
      - AF.WORLD:SEAL_DEPENDENCY
    truth_status: CANON
    coverage: PARTIAL
    issue_hooks:
      - AF-ML-006
```

Registry này ghi **contract**, không copy lore chi tiết.

---

# 4. File 3 — `ARCHITECTURE_CHANGE_LOG.md`

## Vai trò

Ghi structural migration:

```text
module split
module merge
path rename
authority transfer
schema change
registry migration
derived-view regeneration
```

Không dùng để ghi canon history.

Format:

```text
CHANGE-ID
date
type
before
after
affected module IDs
validation result
rollback reference
```

Điều này tách:

```text
architecture history
≠
design history
≠
canon reconciliation
```

---

# 5. Những file nên giữ nhưng đổi vai trò

## `00_AETHERFIRE_CONSOLIDATION_INDEX.md`

Đổi thành:

```text
generated global source map
```

Nguồn:

```text
Architecture Registry
+ module headers
```

Không hand-maintain inventory độc lập.

---

## `92_OPEN_ISSUES_CURRENT.md`

Giữ vì cực hữu ích cho runtime.

Nhưng:

```text
generate/validate
from active issue records
```

Nếu chưa có issue registry riêng, có thể tạm tiếp tục dùng `92` làm authoritative issue register trong migration.

Không tạo issue database mới ngay nếu chưa cần.

---

## `91_RECONCILIATION_RECORD.md`

Giữ trong giai đoạn đầu.

Thêm ID ổn định.

Chỉ split khi size/traffic thật sự vượt threshold.

---

## `90_DESIGN_HISTORY_AND_RECONSIDERATIONS.md`

Giữ nguyên giai đoạn đầu.

Thêm node routing.

Không split chỉ vì file dài.

---

# 6. File không nên tạo ngay

Không tạo:

```text
NODE_REGISTRY_GLOBAL.yaml
COVERAGE_REGISTRY.yaml
DEPENDENCY_REGISTRY.yaml
AUTHORITY_REGISTRY.yaml
OVERLAY_DEPENDENCY_REGISTRY.yaml
```

nếu cùng dữ liệu đã có thể đặt ở:

```text
module local index
Architecture Registry
Interface Registry
```

Nếu tạo tất cả, consistency problem sẽ quay lại ở management layer.

---

# 7. Khi nào cần thêm Issue Registry riêng

Chỉ tạo:

```text
ISSUE_REGISTRY.yaml
```

khi `92` bắt đầu có một trong các dấu hiệu:

```text
> nhiều trăm active issues
frequent cross-module issue updates
automated query needed
manual merge conflict frequent
issue lifecycle needs machine validation
```

Trước đó:

```text
92 + stable IDs
```

đủ.

---

# 8. Khi nào cần split Reconciliation

Chỉ split `91` khi:

```text
route-by-ID vẫn không đủ
file read cost cao
multiple unrelated reconciliation streams
frequent concurrent edits
```

Đích:

```text
Reconciliation/
  REC-AF-....md

91_RECONCILIATION_RECORD.md
→ generated summary
```

Không thực hiện sớm.

---

# 9. Khi nào cần module manifest riêng

Ban đầu metadata module có thể nằm trong:

```text
Architecture Registry
+
header/local index trong source
```

Nếu module quá lớn hoặc được compose ở nhiều package:

```text
<module>.manifest.yaml
```

mới đáng cân nhắc.

---

# 10. Validator đề xuất

Không nhất thiết là file Markdown.

Nên có script:

```text
validate_architecture.py
```

hoặc công cụ tương đương.

Checks:

```text
CURRENT source not registered
registered path missing
duplicate Module ID
duplicate Node ID
unresolved node reference
invalid Interface endpoint
duplicate controlling scope
orphan dependency
cycle
stale derived view
schema mismatch
superseded module still active consumer
```

---

# 11. Generator đề xuất

Một script:

```text
build_architecture_views.py
```

có thể sinh/kiểm tra:

```text
00
92 summary sections
source map
interface map
validation report
```

Không sinh canon prose.

---

# 12. Generated file metadata

Mỗi generated view có:

```yaml
generated: true
generated_from:
schema_version:
registry_revision:
generated_at:
```

Nếu file bị sửa tay:

```text
validator warns
```

---

# 13. Directory layout — cân nhắc, không bắt buộc migrate ngay

Đích sạch có thể là:

```text
AetherFire Project/
├─ Current/
├─ Control/
│  ├─ CI/
│  ├─ Router/
│  └─ Overlays/
├─ Architecture/
│  ├─ ARCHITECTURE_REGISTRY.yaml
│  ├─ INTERFACE_REGISTRY.yaml
│  ├─ ARCHITECTURE_GLOSSARY.md
│  └─ ARCHITECTURE_CHANGE_LOG.md
├─ Derived/
│  ├─ 00_AETHERFIRE_CONSOLIDATION_INDEX.md
│  └─ 92_OPEN_ISSUES_CURRENT.md
├─ Reconciliation/
├─ History/
└─ Source_Archive/
```

Nhưng **không nên reorganize paths ngay ở migration đầu**.

Ổn định identity trước.

Di chuyển path sau.

---

# 14. Quy tắc tối thiểu để tránh fragmentation

```text
CANON CONTENT
→ module source

MODULE INVENTORY
→ architecture registry

CROSS-MODULE CONTRACT
→ interface registry

OPEN STATE
→ issue layer / 92

CONFLICT PROVENANCE
→ reconciliation

DESIGN HISTORY
→ 90/history

CONTROL RULE
→ CI/router/overlay

HUMAN READ MAP
→ derived view
```

Một loại thông tin chỉ nên có **một nơi sở hữu**.

Các nơi khác chỉ tham chiếu hoặc summary.
