# Fanfiction Engine — Current Repository State

**Vai trò:** snapshot con trỏ active, mapping tên và trạng thái. Giải thích quan hệ cấp project thuộc [tài liệu định hướng](../../WHAT_IS_FANFICTION_ENGINE.md); cơ chế thuộc nguồn scoped. Snapshot không tạo canon hoặc thắng nguồn/xác nhận có thẩm quyền.

## 0. Tên hiện hành và mapping lịch sử

| Hạng mục | Tên hiện hành | Nhãn lịch sử |
| --- | --- | --- |
| Toàn project | Fanfiction Engine | The Academy Project |
| Platform | The Academy | Giữ tên platform |
| Miền vận hành | Institutional Causality | V1.5 |
| Miền vận hành | Narrative Engine Causality | V2 |
| Nhánh nghiên cứu tạm dừng | Academy Revise | V2.5 |

## 1. Nguồn quản hiện hành

| Vai trò | Nguồn active |
| --- | --- |
| Định hướng / quan hệ cấp project | [WHAT_IS_FANFICTION_ENGINE.md](../../WHAT_IS_FANFICTION_ENGINE.md) |
| CI | [CI v2.0](Fanfiction_Engine_CI_v2.0.md) |
| Chọn nguồn | [Router v1.1](Fanfiction_Engine_Source_Router_v1.1.md) |
| Chống drift | [Anti-Drift Kernel](../../12_ANTI_DRIFT/Fanfiction_Engine_Anti_Drift_Kernel.md) |
| Điều hướng | [README](../../README.md) |

CI/Router được sửa tại chỗ trong lần project-control revamp; nhãn version được giữ nguyên, không tạo bản kế nhiệm. Trạng thái triển khai/nạp và hành vi ChatGPT Project vẫn `UNVERIFIED`.

## 2. Kiến trúc miền và trạng thái nhánh

| Phạm vi | Nguồn | Trạng thái / cách dùng |
| --- | --- | --- |
| Institutional Causality | [Architecture](../../02_FANFICTION_ENGINE_ARCHITECTURE/INSTITUTIONAL_CAUSALITY/Institutional_Causality_Architecture.md), [Open Registry](../../02_FANFICTION_ENGINE_ARCHITECTURE/INSTITUTIONAL_CAUSALITY/Institutional_Causality_Open_Registry.md) | Nguồn mặc định; vùng mở giữ nguyên |
| Narrative Engine Causality | [Architecture](../../02_FANFICTION_ENGINE_ARCHITECTURE/NARRATIVE_ENGINE_CAUSALITY/Narrative_Engine_Causality_Architecture.md) | Nguồn mặc định |
| HIP | [Historical Influence Potential](../../01_HIP/Historical_Influence_Potential.md) | Nguồn định nghĩa |
| Academy Revise | [Branch](../../02_FANFICTION_ENGINE_ARCHITECTURE/BRANCHES/Academy_Revise_Branch.md) | `PAUSED WORKING BRANCH` theo chỉ dẫn tác giả trong lần revamp này; nội dung vẫn read-only, không nâng thành kiến trúc hiện hành |
| Phương pháp | [Core Design Philosophy](<../Narrative Engine — Core Design Philosophy.md>) | Nguồn phương pháp, không thay source riêng của engine |

## 3. Trạng thái và con trỏ engine

| Hạng mục | Trạng thái / nguồn hiện hành |
| --- | --- |
| Chaos | [Package Chaos](../../04_NARRATIVE_ENGINES/Chaos/ENGINE_CORE.md), tái cấu trúc nội dung canon v3; bản v3 gốc giữ provenance tại đường cũ |
| Sloth, Wrath, Chaos | Mode Narrative Engine Causality; xem [xác nhận tác giả, mục 5](../../The_Academy_Authorial_Decisions_2026-09-28.md#5-mode-vận-hành-hiện-hành) với nhãn legacy V2 |
| Lust | [Working Draft](../../03_INSTITUTIONAL_ENGINES/Lust/Lust_Working_Draft.md); Institutional Causality |
| Greed / Ring | [Greed package](../../04_NARRATIVE_ENGINES/Greed/ENGINE_CORE.md), [Ring component](../../04_NARRATIVE_ENGINES/Greed/COMPONENTS/Ring.md); giữ Working/UNKNOWN; phân loại Governor theo [xác nhận tác giả](../../The_Academy_Authorial_Decisions_2026-09-28.md#1-greed) |
| Implementation Greed II | [Implementation v0.1](../../08_LORE_IMPLEMENTATIONS/Greed_II/Greed_II_Implementation_v0.1_Working_Draft.md); Working Draft |

Con trỏ package: [Sloth](../../04_NARRATIVE_ENGINES/Sloth/ENGINE_CORE.md), [Wrath](../../04_NARRATIVE_ENGINES/Wrath/ENGINE_CORE.md). Mỗi ENGINE_CORE dẫn tới HOST_CONTRACT, RUNTIME, OPEN_STATE và WRITING_VALIDATION. Tám nguồn cũ có thông báo provenance, không còn là owner active song song; archive không đổi. Writer validation: `NOT RUN`, không có runtime PASS từ migration.

Cơ chế, giới hạn và quan hệ riêng đọc ở nguồn; không suy mode hoặc trạng thái cho engine khác từ bảng này.

## 4. Provenance

- [Authorial Decisions 2026-09-28](../../The_Academy_Authorial_Decisions_2026-09-28.md): các xác nhận có phạm vi; giữ nguyên terminology/path lịch sử trong hồ sơ.
- [Genealogy](../../06_ENGINE_GENEALOGY/engine_genealogy_and_development_updated.md): lịch sử hình thành.
- [M6 Semantic Migration Audit](../The_Academy_M6_Semantic_Migration_Audit.md): hồ sơ migration lịch sử.
- [V1.5 baseline](../../02_FANFICTION_ENGINE_ARCHITECTURE/INSTITUTIONAL_CAUSALITY/The_Academy_V1_5_Architecture_Baseline_Anti_Drift.md), [handoff](../../02_FANFICTION_ENGINE_ARCHITECTURE/INSTITUTIONAL_CAUSALITY/The_Academy_V1_5_Architecture_Handoff.md): reconstruction/provenance, không là đường đọc mặc định.
- [Router v1.0](The_Academy_Source_Router_v1.0.md), [source_archive](../../source_archive/README.md): nguồn cũ để đối chiếu khi cần.

Nếu snapshot sai nguồn, sửa snapshot trong phạm vi được phép; không dùng snapshot để ghi đè nguồn scoped hoặc hồ sơ lịch sử.
