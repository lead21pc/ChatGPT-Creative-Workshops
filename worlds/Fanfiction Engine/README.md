# Fanfiction Engine — chỉ mục nguồn

**Vai trò:** chỉ mục đường dẫn trong repository. Vị trí thư mục giúp tra cứu, không tự xác lập quan hệ `CONTAINS`, `DEPENDS_ON`, thẩm quyền canon hoặc tính portable của một engine. Đọc [xác nhận tác giả ngày 2026-09-28](The_Academy_Authorial_Decisions_2026-09-28.md) trước khi xử lý các nhãn nguồn đã được đính chính.

**Bắt đầu từ:** [định hướng / Project Core](WHAT_IS_FANFICTION_ENGINE.md) cho bản sắc và quan hệ cấp project; [Current State](00_META/controls/Fanfiction_Engine_Current_State.md) cho con trỏ active, mapping tên và trạng thái; [Router](00_META/controls/Fanfiction_Engine_Source_Router_v1.1.md) cho đường đọc theo yêu cầu. Tên hiện hành là Fanfiction Engine; đây là tên đã có trên current tree trước task này.

## Nền tảng và kiến trúc

- [Historical Influence Potential](01_HIP/Historical_Influence_Potential.md): cổng đánh giá mở; tiêu chí đến từ context.
- [Institutional Causality Architecture](02_FANFICTION_ENGINE_ARCHITECTURE/INSTITUTIONAL_CAUSALITY/Institutional_Causality_Architecture.md): nguồn kiến trúc Institutional Causality mặc định sau soft migration M7.
- [Institutional Causality Open Registry](02_FANFICTION_ENGINE_ARCHITECTURE/INSTITUTIONAL_CAUSALITY/Institutional_Causality_Open_Registry.md): giữ các vùng `UNKNOWN` / open; registry không phải danh sách việc bắt buộc phải lấp.
- [Narrative Engine Causality Architecture](02_FANFICTION_ENGINE_ARCHITECTURE/NARRATIVE_ENGINE_CAUSALITY/Narrative_Engine_Causality_Architecture.md): nguồn kiến trúc Narrative Engine Causality mặc định.
- [Academy Revise branch](02_FANFICTION_ENGINE_ARCHITECTURE/BRANCHES/Academy_Revise_Branch.md): `PAUSED WORKING BRANCH` theo chỉ dẫn tác giả trong lần project-control revamp; nội dung nhánh giữ nguyên, không phải successor bắt buộc của Institutional Causality/Narrative Engine Causality.
- [Baseline V1.5 cũ](02_FANFICTION_ENGINE_ARCHITECTURE/INSTITUTIONAL_CAUSALITY/The_Academy_V1_5_Architecture_Baseline_Anti_Drift.md) và [handoff V1.5](02_FANFICTION_ENGINE_ARCHITECTURE/INSTITUTIONAL_CAUSALITY/The_Academy_V1_5_Architecture_Handoff.md): nguồn reconstruction/provenance, không còn là đường đọc mặc định.
- [Lust Working Draft](03_INSTITUTIONAL_ENGINES/Lust/Lust_Working_Draft.md): engine thuộc Institutional Causality; vai trò institutional cụ thể còn theo giới hạn của nguồn.

## Narrative engines và interface

Mỗi package dùng `ENGINE_CORE.md`, `HOST_CONTRACT.md`, `RUNTIME.md`, `OPEN_STATE.md` và `WRITING_VALIDATION.md` theo vai trò tài liệu; đây không phải shared causal schema. Các link dưới đây vào owner active; nguồn cũ giữ tại chỗ với nhãn provenance, nội dung gốc không đổi.

- [Greed](04_NARRATIVE_ENGINES/Greed/ENGINE_CORE.md), [Ring](04_NARRATIVE_ENGINES/Greed/COMPONENTS/Ring.md), [Greed II implementation](08_LORE_IMPLEMENTATIONS/Greed_II/Greed_II_Implementation_v0.1_Working_Draft.md).
- [Sloth](04_NARRATIVE_ENGINES/Sloth/ENGINE_CORE.md), [Accommodation](04_NARRATIVE_ENGINES/Sloth/COMPONENTS/Accommodation.md), [Graze](04_NARRATIVE_ENGINES/Sloth/COMPONENTS/Graze.md), [The Gun](04_NARRATIVE_ENGINES/Sloth/COMPONENTS/The_Gun.md).
- [Wrath](04_NARRATIVE_ENGINES/Wrath/ENGINE_CORE.md); hybrid và boundary The Tainted Cosmos giữ tại HOST_CONTRACT của package, không tuyên bố portability.
- [Chaos](04_NARRATIVE_ENGINES/Chaos/ENGINE_CORE.md); package tổ chức lại nội dung canon v3, giữ Three Pengs/Ludopath nguyên cấu trúc. Bản v3 gốc giữ provenance tại đường cũ.

Writer validation của cả bốn package là protocol `NOT RUN`, chưa có writer-run evidence. Lust tiếp tục thuộc institutional side và không nằm trong migration này.

## Provenance và quy tắc đọc

- [Genealogy](06_ENGINE_GENEALOGY/engine_genealogy_and_development_updated.md) ghi quá trình hình thành; quan hệ lịch sử không tự thành phụ thuộc hiện hành.
- [Fanfiction Engine Anti-Drift Kernel](12_ANTI_DRIFT/Fanfiction_Engine_Anti_Drift_Kernel.md) là kernel chống drift project-specific; [Modular anti-drift](12_ANTI_DRIFT/modular_engine_concept_anti_drift.md) vẫn giữ invariant tổng quát và provenance rộng hơn.
- [Narrative Engine — Core Design Philosophy](<00_META/Narrative Engine — Core Design Philosophy.md>) và [multi-paracosm hub workflow](00_META/multi_paracosm_hub_workflow.md) là tài liệu phương pháp; chúng không thay các xác nhận engine-specific.
- [Current State](00_META/controls/Fanfiction_Engine_Current_State.md) là snapshot điều hướng; [CI v2.0](00_META/controls/Fanfiction_Engine_CI_v2.0.md) là CI hiện hành; [Source Router v1.1](00_META/controls/Fanfiction_Engine_Source_Router_v1.1.md) là router hiện hành. [Router v1.0](00_META/controls/The_Academy_Source_Router_v1.0.md) được giữ để đối chiếu provenance. Trạng thái nạp CI/router/kernel vào ChatGPT Project chưa được kiểm chứng.
- [OC Academy](<source_archive/Academy_legacy/OC Academy.txt>) là nguồn lore cũ; đối chiếu Institutional Causality Architecture, Open Registry và provenance phù hợp trước khi dùng làm ràng buộc hiện hành.
- [source_archive](source_archive/README.md) giữ nguồn cũ và bản nháp để truy xuất, không là chỉ mục nguồn hiện hành.
- Ảnh trong `13_VISUAL_ASSETS/Greed/` và `13_VISUAL_ASSETS/unassigned/` là tài liệu tham khảo hình ảnh theo xác nhận tác giả, không là nguồn chốt tên hoặc thông số.

## Trạng thái sau migration

Các thư mục rỗng mang tên cũ `The Academy`, `The Chaos Engine`, `The Greed Entropy Injector`, `The Lust Judgment Redemptions`, `The Sloth Regressors Hunter` và `The Wrath Forsaken` đã được dọn khỏi working tree. Git theo dõi tệp, không theo dõi thư mục rỗng; mục này ghi nhận bước dọn cuối cùng.

Các vùng `UNKNOWN`/`OPEN`, Working và Placeholder giữ nguyên trạng thái trong nguồn riêng; chúng không phải danh sách việc phải hoàn thiện. Tra cứu cơ chế và điểm mở qua các liên kết engine/interface ở trên; các đính chính nhãn đọc tại [Authorial Decisions](The_Academy_Authorial_Decisions_2026-09-28.md). README không giữ bản sao state hoặc cơ chế engine.
