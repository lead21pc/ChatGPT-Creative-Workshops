# The Academy — Source Router v1.0

**Trạng thái:** `SUPERSEDED FOR ROUTING / RETAINED FOR PROVENANCE` sau soft migration M7. Router hiện hành là [The_Academy_Source_Router_v1.1.md](The_Academy_Source_Router_v1.1.md). Việc môi trường ChatGPT Project tự nạp router vẫn chưa được kiểm chứng.

## Vai trò

Router chọn **tệp cần đọc** theo yêu cầu, mode, engine và phạm vi nguồn. [The Academy CI v2.0](The_Academy_CI_v2.0.md) giữ quy tắc hành vi và invariant chung; router không thay CI, không quyết định canon, không cấp khả năng cho engine và không biến các vùng `UNKNOWN` thành việc phải điền. Router được biên soạn từ [Compact Revised trước đây](../../source_archive/controls/The_Academy_CI_HIP_Core_English_Compact_Revised.md), nhưng không sao chép nguyên các quy tắc CI sang đây.

Trước khi dùng một nguồn, đọc xác nhận trực tiếp mới nhất của tác giả nếu có và [hồ sơ xác nhận đã ghi](../../The_Academy_Authorial_Decisions_2026-09-28.md). Tên tệp, số phiên bản, vị trí thư mục và việc cùng xuất hiện không tự xác lập thẩm quyền hay quan hệ bản thể. Nếu thẩm quyền hoặc supersession chưa rõ, giữ các nguồn song song và ghi rõ provenance.

## Chọn nguồn theo câu hỏi

| Khi yêu cầu liên quan đến | Bắt đầu từ | Ranh giới |
| --- | --- | --- |
| Định nghĩa HIP, tiêu chí đánh giá hoặc target | [Historical Influence Potential](../../01_HIP/Historical_Influence_Potential.md) | HIP không tự cung cấp tiêu chí, thang điểm hay outcome. Chỉ dùng bộ tiêu chí được nguồn hoặc tác giả cung cấp cho context đó. |
| Tuyển HIP, thể chế, faction, cohort, giáo dục hoặc trước tốt nghiệp | [V1.5 baseline](../../02_ACADEMY_ARCHITECTURE/V1_5/The_Academy_V1_5_Architecture_Baseline_Anti_Drift.md); [handoff](../../02_ACADEMY_ARCHITECTURE/V1_5/The_Academy_V1_5_Architecture_Handoff.md) khi cần lịch sử tái thiết kế | Trở về world gốc là điểm kết thúc V1.5. Không đưa vận hành hậu tốt nghiệp vào active runtime của V1.5. [OC Academy](<../../source_archive/Academy_legacy/OC Academy.txt>) chỉ là nguồn legacy cần đối chiếu. |
| Áp dụng Narrative Engine vào Host Fiction, World Bible hoặc target | [Core Design Philosophy](<../Narrative Engine — Core Design Philosophy.md>), tài liệu của engine được chọn và World Bible/Host rules do người dùng cung cấp | Meta Engine được xử lý trước engine selection; thiếu host rule thì giữ `UNKNOWN`, không tự nhập lore ngoài. V1.5 và V2 không tự thay thế nhau. |
| Greed như engine hoặc cơ chế Ring | [Greed Core v0.2](../../04_NARRATIVE_ENGINES/Greed/Greed_Narrative_Engine_Core_v0.2_Working_Draft.md); [Ring interface](../../04_NARRATIVE_ENGINES/Greed/Ring_Interface_v0.1_Working_Draft.md) khi cần vòng Ring | `Responsibility` là Governor; Greed Paradox giải thích bối cảnh, không là Governor thứ hai. Chỉ dùng [Greed II](../../08_LORE_IMPLEMENTATIONS/Greed_II/Greed_II_Implementation_v0.1_Working_Draft.md) cho cá thể/vũ khí/triển khai Greed II. |
| Sloth | [Sloth Engine](../../04_NARRATIVE_ENGINES/Sloth/Sloth_Engine_Working_Draft.md) | Đọc [Accommodation](../../04_NARRATIVE_ENGINES/Sloth/Sloth_Accommodation_Working_Draft.md), [Graze](../../04_NARRATIVE_ENGINES/Sloth/Sloth_Graze_Doctrine_Working_Draft.md) hoặc [The Gun](../../04_NARRATIVE_ENGINES/Sloth/Sloth_The_Gun_Working_Draft.md) chỉ khi cơ chế đó cần thiết. Nhãn Working/Placeholder vẫn còn hiệu lực. |
| Wrath | [Wrath Working Draft](../../04_NARRATIVE_ENGINES/Wrath/Wrath_Working_Draft.md) | Phân biệt engine/entity với triển khai *The Tainted Cosmos* trong cùng nguồn; không tự suy ra quan hệ với host khác. |
| Chaos, Pride/Envy/Gluttony trong composite Chaos | [Chaos v3](../../04_NARRATIVE_ENGINES/Chaos/Chaos_Engine_Canon_Specification_v3.md) | v3 là bản chính thức. Bản `updated` ở archive chỉ dùng khi so sánh provenance; ba tệp Sin rỗng không cung cấp định nghĩa. |
| Lust | [Lust Working Draft](../../03_V1_5_INSTITUTIONAL_ENGINES/Lust/Lust_Working_Draft.md), cùng V1.5 khi câu hỏi liên quan thể chế | Lust thuộc V1.5; loại faction, interface và authority cụ thể còn `UNKNOWN`. |
| Quan hệ engine/module, nguồn gốc thiết kế hoặc tính portable | [Modular anti-drift](../../12_ANTI_DRIFT/modular_engine_concept_anti_drift.md); [genealogy](../../06_ENGINE_GENEALOGY/engine_genealogy_and_development_updated.md) khi hỏi lịch sử | Genealogy không tự tạo hierarchy, dependency hoặc thẩm quyền hiện hành. Quan hệ phải có cạnh được xác nhận. |
| Workflow nhiều paracosm | [multi-paracosm hub workflow](../multi_paracosm_hub_workflow.md) | Chỉ áp dụng khi yêu cầu đi qua nhiều paracosm; không nhập ontology của paracosm khác vào The Academy. |
| Nguồn cũ, bản đã thay hoặc mâu thuẫn lịch sử | [source_archive](../../source_archive/README.md) và nguồn hiện hành tương ứng | Dùng archive để truy vết, không kích hoạt lại bản cũ hoặc tự hợp nhất mâu thuẫn. Ảnh ở [visual assets](../../13_VISUAL_ASSETS/) chỉ là tham khảo hình ảnh. |

Sloth, Wrath và Chaos có mode V2 hiện hành theo xác nhận tác giả; Lust thuộc V1.5. Không dùng các nhãn đó để gán mode cho engine khác. Nhiều engine có thể tiếp cận cùng một HIP mà không tự thành composite, quan hệ phụ thuộc hay cùng mục tiêu.

## Quy trình routing tối thiểu

1. Xác định yêu cầu là giải thích, audit, mô phỏng, đối chiếu phiên bản, hay áp dụng engine; chỉ chọn các nguồn ảnh hưởng trực tiếp đến câu hỏi.
2. Đọc nguồn xác nhận trạng thái, rồi nguồn cơ chế đúng nhánh. Mở thêm tài liệu chỉ khi một điều kiện, cạnh quan hệ, host rule hoặc provenance cần được kiểm tra.
3. Nêu nguồn và trạng thái của mệnh đề khi có nguy cơ lẫn canon, working draft, giả định, mô phỏng hoặc nguồn legacy. Xung đột chưa có supersession thì giữ `CONFLICTED`; chỗ cố ý mở giữ `UNKNOWN`/`OPEN`.
4. Router không điền tiêu chí HIP, không giả định cùng một cấu trúc cho mọi Sin, không chọn outcome, không tự nâng cơ chế của một actor thành invariant của engine.
