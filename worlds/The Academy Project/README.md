# The Academy — chỉ mục nguồn

**Vai trò:** chỉ mục đường dẫn trong repository. Vị trí thư mục giúp tra cứu, không tự xác lập quan hệ `CONTAINS`, `DEPENDS_ON`, thẩm quyền canon hoặc tính portable của một engine. Đọc [xác nhận tác giả ngày 2026-09-28](The_Academy_Authorial_Decisions_2026-09-28.md) trước khi xử lý các nhãn nguồn đã được đính chính.

## Nền tảng và kiến trúc

- [Historical Influence Potential](01_HIP/Historical_Influence_Potential.md): cổng đánh giá mở; tiêu chí đến từ context.
- [V1.5 Architecture](02_ACADEMY_ARCHITECTURE/V1_5/The_Academy_V1_5_Architecture.md): nguồn kiến trúc V1.5 mặc định sau soft migration M7.
- [V1.5 Open Registry](02_ACADEMY_ARCHITECTURE/V1_5/The_Academy_V1_5_Open_Registry.md): giữ các vùng `UNKNOWN` / open; registry không phải danh sách việc bắt buộc phải lấp.
- [V2 Architecture](02_ACADEMY_ARCHITECTURE/V2/The_Academy_V2_Architecture.md): nguồn kiến trúc V2 mặc định.
- [Academy Revise / V2.5 branch](02_ACADEMY_ARCHITECTURE/BRANCHES/The_Academy_V2_5_Revise_Branch.md): working branch; không phải successor bắt buộc của V1.5/V2.
- [Baseline V1.5 cũ](02_ACADEMY_ARCHITECTURE/V1_5/The_Academy_V1_5_Architecture_Baseline_Anti_Drift.md) và [handoff V1.5](02_ACADEMY_ARCHITECTURE/V1_5/The_Academy_V1_5_Architecture_Handoff.md): nguồn reconstruction/provenance, không còn là đường đọc mặc định.
- [Lust Working Draft](03_V1_5_INSTITUTIONAL_ENGINES/Lust/Lust_Working_Draft.md): engine thuộc V1.5; vai trò institutional cụ thể còn theo giới hạn của nguồn.

## Narrative engines và interface

- [Sloth Engine Working Draft](04_NARRATIVE_ENGINES/Sloth/Sloth_Engine_Working_Draft.md) cùng [Accommodation](04_NARRATIVE_ENGINES/Sloth/Sloth_Accommodation_Working_Draft.md), [Graze](04_NARRATIVE_ENGINES/Sloth/Sloth_Graze_Doctrine_Working_Draft.md) và [The Gun](04_NARRATIVE_ENGINES/Sloth/Sloth_The_Gun_Working_Draft.md). Mode V2 được tác giả xác nhận; phần Working/Placeholder vẫn giữ nhãn trong nguồn. [Bản Sloth ngắn](source_archive/Sloth/Sloth_Working_Draft.md) là nguồn lưu trữ.
- [Wrath Working Draft](04_NARRATIVE_ENGINES/Wrath/Wrath_Working_Draft.md): hybrid Engine/Entity, mode V2; phần gắn với The Tainted Cosmos chưa được tách khỏi nguồn.
- [Chaos v3](04_NARRATIVE_ENGINES/Chaos/Chaos_Engine_Canon_Specification_v3.md): bản chính thức của composite Chaos, mode V2. [Bản `updated`](source_archive/Chaos/Chaos_Engine_Canon_Specification_updated.md) được giữ để đối chiếu provenance.
- [Greed Engine Core v0.2](04_NARRATIVE_ENGINES/Greed/Greed_Narrative_Engine_Core_v0.2_Working_Draft.md), [Ring interface](04_NARRATIVE_ENGINES/Greed/Ring_Interface_v0.1_Working_Draft.md) và [hồ sơ triển khai Greed II](08_LORE_IMPLEMENTATIONS/Greed_II/Greed_II_Implementation_v0.1_Working_Draft.md): các bản working có phạm vi khác nhau. [Bản hợp nhất Greed II](source_archive/Greed/Greed_II_Core_Interfaces_Consolidated.md) vẫn lưu để đối chiếu nguồn.

## Provenance và quy tắc đọc

- [Genealogy](06_ENGINE_GENEALOGY/engine_genealogy_and_development_updated.md) ghi quá trình hình thành; quan hệ lịch sử không tự thành phụ thuộc hiện hành.
- [Academy Anti-Drift Kernel](12_ANTI_DRIFT/The_Academy_Anti_Drift_Kernel.md) là kernel chống drift project-specific; [Modular anti-drift](12_ANTI_DRIFT/modular_engine_concept_anti_drift.md) vẫn giữ invariant tổng quát và provenance rộng hơn.
- [Narrative Engine — Core Design Philosophy](<00_META/Narrative Engine — Core Design Philosophy.md>) và [multi-paracosm hub workflow](00_META/multi_paracosm_hub_workflow.md) là tài liệu phương pháp; chúng không thay các xác nhận engine-specific.
- [Current State](00_META/controls/The_Academy_Current_State.md) là snapshot điều hướng; [CI v2.0](00_META/controls/The_Academy_CI_v2.0.md) là CI hiện hành; [Source Router v1.1](00_META/controls/The_Academy_Source_Router_v1.1.md) là router hiện hành. [Router v1.0](00_META/controls/The_Academy_Source_Router_v1.0.md) được giữ để đối chiếu provenance. Trạng thái nạp CI/router/kernel vào ChatGPT Project chưa được kiểm chứng.
- [OC Academy](<source_archive/Academy_legacy/OC Academy.txt>) là nguồn lore cũ; đối chiếu V1.5 Architecture, Open Registry và provenance phù hợp trước khi dùng làm ràng buộc hiện hành.
- [source_archive](source_archive/README.md) giữ nguồn cũ và bản nháp để truy xuất, không là chỉ mục nguồn hiện hành.
- Ảnh trong `13_VISUAL_ASSETS/Greed/` và `13_VISUAL_ASSETS/unassigned/` là tài liệu tham khảo hình ảnh theo xác nhận tác giả, không là nguồn chốt tên hoặc thông số.

## Trạng thái sau migration

Các thư mục rỗng mang tên cũ `The Academy`, `The Chaos Engine`, `The Greed Entropy Injector`, `The Lust Judgment Redemptions`, `The Sloth Regressors Hunter` và `The Wrath Forsaken` đã được dọn khỏi working tree. Git theo dõi tệp, không theo dõi thư mục rỗng; mục này ghi nhận bước dọn cuối cùng.

Những điểm dưới đây được tác giả **cố ý để mở** theo tính chất của Narrative Engine. Giữ nguyên `UNKNOWN`/`OPEN` và các nhãn Working/Placeholder của từng nguồn; không xem chúng là việc phải điền đủ để hoàn tất migration hoặc tự suy ra một đáp án chung cho mọi triển khai:

- **Greed/Ring:** tiêu chí chọn người nhận; nguồn gốc, số lượng, lợi ích và giới hạn Ring; kết quả khi Greed không thắng; khả năng engine hoặc Ring chạy với actor/host khác. `Infinite Rings` chưa được nâng từ giả định Paradox thành canon Ring. Xem [Greed Core](04_NARRATIVE_ENGINES/Greed/Greed_Narrative_Engine_Core_v0.2_Working_Draft.md) và [Ring interface](04_NARRATIVE_ENGINES/Greed/Ring_Interface_v0.1_Working_Draft.md).
- **Thuật ngữ:** quyết định `Counter → Governor` áp dụng cho định nghĩa chống trope nói chung; cách phân loại các cơ chế riêng vẫn cần đối chiếu. Ví dụ [Sloth draft](04_NARRATIVE_ENGINES/Sloth/Sloth_Engine_Working_Draft.md) còn gọi `Accountability` là Counter. Ring được nguồn gọi là chất xúc tác cho một cuộc đời; việc gán nó thành `Catalyst` formal của ontology chưa được xác nhận.
- **Sloth:** Core Drive cuối cùng, Authority/Seat, timing, Graze, The Gun và điều kiện Accommodation còn mang nhãn Working/Placeholder trong [nguồn](04_NARRATIVE_ENGINES/Sloth/Sloth_Engine_Working_Draft.md). Mode V2 hiện hành đã được tác giả xác nhận.
- **Wrath:** transition giữa hai quan hệ với The Academy, cơ chế giữa Lust/Wrath/MC và phần tách engine khỏi triển khai *The Tainted Cosmos* chưa được formal hóa trong [working draft](04_NARRATIVE_ENGINES/Wrath/Wrath_Working_Draft.md). Mode V2 hiện hành đã được tác giả xác nhận.
- **Chaos:** [v3](04_NARRATIVE_ENGINES/Chaos/Chaos_Engine_Canon_Specification_v3.md) là bản chính thức và mode V2 hiện hành đã được xác nhận; các điều kiện kích hoạt, giới hạn/termination, tính portable và điều kiện chọn V1.5/V2/cấu hình lai vẫn được chính v3 ghi `UNKNOWN / OPEN`.
