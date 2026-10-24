# The Kingdom — Luật Ngoại Nhân & World Tree — Current Handoff

HANDOFF_ID: TK-FOREIGN-JUSTICE-WORLDTREE
FILENAME: THE_KINGDOM_FOREIGN_JUSTICE_CURRENT.md
STATUS: ACTIVE
SCOPE: Tái thiết kế hệ luật áp dụng cho người ngoại quốc bị bắt trong Mẫu quốc, vai trò AI–Ma'at–Judgez–World Tree, hệ trừng phạt đối ngoại, bảo mật Rift/Dungeon, Giàn Hỏa Kiếp và biểu tượng thần quyền của World Tree. Không bao gồm luật dành cho người nội quốc.
UPDATED: 2026-10-25

## 1. Established current state

### FJ-01 — Baseline LAW V2 hiện có
STATUS: OBSERVED

Current state:
- File `THE_KINGDOM_LAW_V2_CONSOLIDATED.md` hiện giữ trạng thái reset:
  - AI chưa có tên / Mắt Thần là lõi native liên tục từ V1 sang V2 và không được nerf thành camera/dispatcher.
  - Ma'at đang ở tầng basic, chưa khóa ontology, đầu ra hay quy trình.
  - Judgez đang ở tầng basic, chưa khóa quyền phán quyết, cấu trúc tổ chức hay mô hình hoạt động.
  - World Tree và hình phạt V1 được ghi như genealogy, chưa phải luật V2 hiện hành.
  - Zetta/Guild và hệ sinh thái liên quan đã bị loại khỏi LAW V2.
- File hiện có chưa phản ánh thiết kế Luật Ngoại Nhân mới trong phần cuối cuộc trò chuyện.

Evidence / source anchors:
- `THE_KINGDOM_LAW_V2_CONSOLIDATED.md`
  - `LAW_00_overview.md`
  - `LAW_01_divine_eye.md`
  - `LAW_02_maat.md`
  - `LAW_03_wizard_police.md`
  - `LAW_04_judge_and_sentencing.md`
  - `LAW_05_reduced_procedure.md`
  - `LAW_06_design_invariants.md`

### FJ-02 — AI phải giữ đúng năng lực concept gốc
STATUS: DECIDED

Current state:
- AI là một ý chí trí tuệ nhân tạo phân tán quy mô quốc gia.
- Có thể quan sát, nghe, nói, ghi nhận, truy hồi và duy trì số lượng rất lớn tương tác/proxy đồng thời.
- Không được giảm năng lực AI chỉ để tạo việc cho Judgez hoặc các tầng hành chính.
- Năng lực nhận thức rộng không tự động đồng nghĩa AI có toàn bộ thẩm quyền pháp lý.
- Vai trò gốc trong luật: giúp người vi phạm/phạm nhân không thể đơn giản phủ nhận hành vi đã được xác lập; AI có thể trực tiếp trình bày factual record cho người liên quan.

Evidence / source anchors:
- `THE_KINGDOM_LAW_V2_CONSOLIDATED.md` → `LAW_01_divine_eye.md`, `LAW_06_design_invariants.md`

### FJ-03 — Luật hiện đang thiết kế là luật riêng cho người ngoại quốc
STATUS: DECIDED

Current state:
- Hệ luật/trừng phạt đang thiết kế chỉ áp dụng cho người ngoại quốc.
- Luật dành cho người nội quốc là một hệ khác và sẽ thiết kế sau.
- Không được dùng hệ Luật Ngoại Nhân hiện tại làm mặc định cho công dân/cư dân nội quốc.

Next:
- Khi externalize thành LAW, cần tách rõ phạm vi chủ thể ngay ở đầu tài liệu.

### FJ-04 — Chỉ áp dụng khi người ngoại quốc bị bắt
STATUS: DECIDED

Current state:
- Luật Ngoại Nhân này chỉ áp dụng với người đã bị Mẫu quốc bắt giữ.
- Không tự suy từ việc xác định được người giật dây ở bên ngoài thành người đó đã trở thành bị cáo/phạm nhân trong cùng thủ tục.

Consequence:
- Biện pháp đối với người giật dây bên ngoài phải được đặt ở nhánh khác nếu sau này được chốt.

### FJ-05 — Rift/Dungeon phải vẫn là bí mật quân sự
STATUS: DECIDED

Current state:
- Rift/Dungeon là bí mật cấp quân sự.
- Bên ngoài chỉ nên biết người bị kết án chịu **lao động khổ sai**.
- Bên ngoài không được có đủ dữ kiện để xác định Rift/Dungeon thực chất là gì, ở đâu, vận hành ra sao hoặc liên hệ thế nào với hạ tầng quân sự.
- Thiết kế phải cho phép hình phạt có tính răn đe công khai trong khi bản chất nơi thi hành vẫn bị che giấu.

Design constraint:
- Không để việc “bị kết án” vô tình cấp cho phạm nhân quyền quan sát một cơ sở quân sự mà người bình thường không được biết.

### FJ-06 — Mở cửa để giao lưu văn hóa không tạo nghĩa vụ nhượng bộ
STATUS: DECIDED

Current state:
- Chính sách mở cửa vì giao lưu văn hóa không đồng nghĩa Mẫu quốc phải mềm luật, nhượng bộ hoặc chấp nhận bị lợi dụng.
- Mọi phân tích sau phải tránh giả định rằng Mẫu quốc cần thiện chí bên ngoài đến mức phải hy sinh deterrence hoặc quyền tự đặt luật.
- Giao lưu là mục tiêu chính sách; kiểm soát tiếp cận và trừng phạt hành vi vi phạm có thể cùng tồn tại.

Evidence / source anchors:
- `the_kingdom_dia_chinh_tri_dmz_quan_he_quoc_te.md`
- `THE_KINGDOM_LAW_V2_CONSOLIDATED.md`

### FJ-07 — Phong cách ngôn ngữ cho workstream này
STATUS: DECIDED

Current state:
- Hạn chế jargon.
- Nếu có từ tiếng Việt truyền đạt đủ nghĩa thì dùng tiếng Việt.
- Chỉ giữ từ tiếng Anh khi không có thay thế gọn/chính xác hoặc đó là tên riêng/thuật ngữ đã khóa như `World Tree`, `Ma'at`, `Judgez`, `Rift/Dungeon`, `Chain Soul Destruction`.

### WT-01 — World Tree phải đọc được như thần quyền đối với người ngoài
STATUS: DECIDED

Current state:
- World Tree được đưa trở lại bàn thiết kế theo hướng biểu tượng phải truyền đạt được:
  - thần tính;
  - quyền tối cao;
  - quyền lập trật tự;
  - quyền xác lập công lý;
  - nguồn authority mang tính thần quyền.
- Biểu tượng phải đủ rõ để người ngoài nhìn vào có thể hiểu đây không chỉ là “một cây thiêng” mà là một biểu tượng của quyền cai trị/phán quyết.

Constraints:
- Không nhập nhằng biểu tượng của World Tree với Ma'at.
- Cân/lông nên được giữ cho Ma'at nếu tiếp tục dùng, thay vì biến mọi biểu tượng công lý thành thuộc tính của World Tree.
- Không biến World Tree thành hình người chỉ để mượn ngôn ngữ biểu tượng của vua/thần.

### WT-02 — Hướng hình ảnh hiện tại
STATUS: IMPLEMENTED, NOT ACCEPTED AS FINAL

Current state:
- Đã tạo nhiều prototype hình ảnh World Tree trong cuộc trò chuyện.
- Sau phản hồi, hướng hiện tại đã:
  - giảm tính đối xứng máy móc;
  - làm cây trông tự nhiên hơn;
  - giữ quầng sáng/thần quang phía sau;
  - bỏ ngai vàng khỏi prototype gần nhất.
- User đã yêu cầu rõ **xóa ngai vàng**.
- Prototype gần nhất không còn ngai vàng, nhưng chưa có xác nhận rằng đây là thiết kế cuối.

Current prototype asset:
- `a_dramatic_high_fantasy_scene_a_gigantic_ancient.png`

Unsettled visual elements:
- biểu tượng tròn trên thân cây;
- hình gia huy riêng;
- hình biểu trưng dùng trên cờ, huy hiệu, con dấu;
- mức độ giữ quầng sáng và các vòng ký hiệu phía sau;
- ngôn ngữ hình học cuối cùng của biểu tượng thần quyền.

## 2. Active problems

### AP-01 — Phải thiết kế lại Ma'at và Judgez mà không nerf AI
Problem:
- AI đã đủ mạnh để làm nhiều việc điều tra/thông tin.
- Judgez và Ma'at chỉ có lý do tồn tại nếu giải những bài toán AI không nên hoặc không thể tự quyết bằng quyền lực pháp lý.

Current state:
- Chưa có kiến trúc cuối cùng được chốt.
- Một proposal đã được đưa ra:
  - AI = factual record / memory / communication.
  - Judgez = con người tại hiện trường, cưỡng chế, điều tra thực địa, một phần judgment nếu được phép.
  - Ma'at = xác lập responsibility/trách nhiệm sâu hơn việc chỉ biết “A đã làm X”.
  - Luật = ánh xạ responsibility sang hậu quả.
- Proposal này chưa được người dùng xác nhận là canon.

Need:
- Xác định Ma'at là gì về ontology.
- Xác định Judgez có quyền gì.
- Xác định khi nào Ma'at bắt buộc.
- Xác định World Tree tham gia ở đâu mà không làm V2 quay lại mô hình V1 toàn diện.

### AP-02 — Tái nhập World Tree mà không tái nhập toàn bộ V1
Problem:
- World Tree V1 từng là tyrant/cold truth và trực tiếp phán punishment.
- V2 sinh ra một phần vì mô hình `truth confirmed → divine punishment` không còn phù hợp.
- Workstream hiện lại muốn dùng World Tree cho deterrence đối ngoại.

Need:
- Chốt World Tree là:
  - authority tuyên án;
  - authority xác lập chủ quyền pháp lý;
  - executor;
  - biểu tượng thần quyền;
  - hay tổ hợp.
- Không tự giả định Tree tiếp tục xử luật nội quốc.
- Không tự biến World Tree thành Ma'at thứ hai.

### AP-03 — Che Rift/Dungeon nhưng vẫn giữ tính răn đe
Problem:
- Hình phạt phải được biết tới như lao động khổ sai.
- Nơi thi hành thật là bí mật quân sự.
- Cần ngăn phạm nhân, nhân viên ngoại quốc hoặc quan sát viên suy ra cấu trúc Rift/Dungeon qua thông tin phái sinh.

Need:
- Thiết kế giao diện công khai:
  - tên pháp lý công khai;
  - cách chuyển phạm nhân;
  - thông tin nào được công bố;
  - điều kiện liên lạc/thăm gặp nếu có.
- Thiết kế vùng lao động sao cho quan sát từ bên trong không đủ lộ ontology/hạ tầng quân sự.
- Quyết định có cần lọc ký ức tuyệt mật khi mãn án hay không; chưa chốt.

Evidence / source anchors:
- `the_kingdom_he_thong_phan_gian_va_kiem_soat_tri_thuc.md`

### AP-04 — Giàn Hỏa Kiếp phải vừa công khai vừa vận hành được
Problem:
- V1 dùng thời gian cực dài, gây nguy cơ tắc bộ phận thi hành án nếu giữ nguyên.
- Mục tiêu mới là deterrence công khai với người ngoài.

Current state:
- User đề xuất rút xuống **1 tuần**.
- Yêu cầu công khai đã rõ:
  - giàn phải lộ thiên;
  - người bên ngoài phải có thể quan sát;
  - người bên ngoài phải có thể ghi nhận/ghi hình.
- Chưa chốt:
  - 1 tuần có phải con số cuối cùng hay chỉ là proposal;
  - vị trí chính xác;
  - số lượng vị trí thi hành song song;
  - cơ chế giữ phạm nhân sống;
  - trạng thái linh hồn;
  - thủ tục kết thúc án và tử vong;
  - quyền quan sát của báo chí/ngoại giao/thiết bị nước ngoài.

### AP-05 — Chain Soul Destruction
Problem:
- Luật Ngoại Nhân chỉ áp dụng cho người bị bắt.
- Người giật dây ở ngoài có thể có liên hệ trực tiếp với hành vi nhưng chưa nằm trong custody.

Current state:
- `Chain Soul Destruction` đang được cân nhắc như một biện pháp đối với người giật dây có liên quan.
- Chưa chốt nó là:
  - hình phạt pháp lý;
  - phản kích;
  - biện pháp an ninh;
  - quyền chiến tranh;
  - hay một loại chế tài thần quyền riêng.

Need:
- Nếu giữ, phải tách rõ khỏi thủ tục xử người đã bị bắt để không làm luật tự mâu thuẫn.
- Phải định nghĩa ngưỡng liên hệ/trách nhiệm đủ mạnh để tránh “chain” lan sang người chỉ biết, người sơ suất hoặc người có liên hệ yếu.

### AP-06 — Gia huy / biểu tượng World Tree
Problem:
- Cần một biểu tượng có thể dùng được ở nhiều mức:
  - thần điện;
  - cờ;
  - con dấu;
  - gia huy/huy hiệu;
  - biểu tượng pháp quyền;
  - kiến trúc.
- Không nên phụ thuộc vào một tranh minh họa quá chi tiết.

Need:
- Thiết kế một silhouette đơn giản, nhận diện tốt ở kích thước nhỏ.
- Chốt quan hệ giữa:
  - cây;
  - quầng sáng;
  - vương miện/tán cây;
  - vòng quyền lực;
  - quyền trượng hoặc dấu authority;
  - rễ.
- Không dùng ngai vàng trong hướng hiện tại.
- Không dùng cân/lông nếu muốn giữ chúng riêng cho Ma'at.

## 3. Outstanding / blocked

### OUT-01 — Luật nội quốc
STATUS: BLOCKED BY SCOPE

- Cố ý chưa thiết kế.
- Luật nội quốc phải là workstream riêng hoặc phase sau.
- Không được lấp khoảng trống này bằng Luật Ngoại Nhân.

### OUT-02 — Mức phạt cụ thể
STATUS: UNKNOWN

Chưa chốt đầy đủ:
- thế nào là vi phạm nhẹ;
- thế nào là mức đủ để lao động khổ sai;
- tội nào tới tử hình;
- các mức thời hạn;
- quyền kháng nghị/review nếu có;
- mức discretion của Judgez;
- vai trò bắt buộc hay tùy chọn của Ma'at.

### OUT-03 — Authority cuối cùng
STATUS: UNKNOWN

Chưa chốt ai có quyền cuối:
- Judgez;
- Ma'at;
- World Tree;
- một cơ quan pháp lý khác;
- hay một cấu trúc kết hợp.

### OUT-04 — Cập nhật file LAW
STATUS: NOT RUN

- Chưa cập nhật `THE_KINGDOM_LAW_V2_CONSOLIDATED.md` với Luật Ngoại Nhân, World Tree tái thiết kế, Rift secrecy, Giàn Hỏa Kiếp 1 tuần hoặc Chain Soul Destruction.
- Không có kiểm tra tĩnh sau cập nhật vì cập nhật chưa được thực hiện.
- Không có LIVE VERIFIED; đây là worldbuilding/document state, không phải runtime.

## 4. Under consideration

### UC-01 — Kiến trúc trách nhiệm
STATUS: UNDER CONSIDERATION

Proposal hiện có:

```text
AI
→ xác lập factual record

Judgez
→ bắt giữ / bảo vệ / can thiệp / điều tra thực địa

Ma'at
→ xác lập responsibility khi fact chưa đủ để quyết justice

World Tree
→ xác lập hoặc thực thi authority thần quyền đối với ngoại nhân

Law
→ xác định hậu quả/chế tài
```

Không được coi pipeline này là canon cho tới khi được chốt.

### UC-02 — Ma'at như lớp responsibility
STATUS: UNDER CONSIDERATION

- Ma'at không nên chỉ lặp lại fact mà AI đã biết.
- Hướng đề xuất là đánh giá:
  - agency;
  - intent;
  - coercion;
  - causation;
  - responsibility;
  - justification.
- Output chưa được chốt.
- Chưa chốt Ma'at là nguyên lý, thiết chế, cơ chế, thần tính hay tổ hợp.

### UC-03 — Judgez như đại diện pháp quyền tại hiện trường
STATUS: UNDER CONSIDERATION

- Hướng đề xuất:
  - quyền can thiệp bảo vệ;
  - quyền điều tra thực địa;
  - quyền cưỡng chế;
  - có thể có judgment giới hạn ở việc nhẹ/reversible.
- Không chốt mô hình Judge Dredd.
- Không chốt team 2 người.
- Không chốt quyền xử án nặng.

### UC-04 — Giàn Hỏa Kiếp 1 tuần
STATUS: UNDER CONSIDERATION

- User đề xuất 1 tuần để tránh tắc bộ phận thi hành án.
- Yêu cầu công khai/lộ thiên là hướng mạnh hiện tại.
- Con số 1 tuần chưa được ghi nhận là quyết định cuối cùng.

### UC-05 — Chain Soul Destruction đối với người giật dây
STATUS: UNDER CONSIDERATION

- Có thể dùng với người đứng ngoài nếu trách nhiệm/liên hệ đủ mạnh.
- Chưa chốt điều kiện kích hoạt, bản chất pháp lý hay phạm vi lan truyền.

### UC-06 — World Tree như thần quyền đối ngoại
STATUS: UNDER CONSIDERATION

- Hướng đang xét: World Tree quay lại chủ yếu trong Luật Ngoại Nhân, không mặc định quay lại làm judge của toàn xã hội.
- Mục đích:
  - deterrence;
  - thể hiện chủ quyền thần quyền;
  - tạo một authority mà người ngoài nhận diện được.
- Chưa chốt vị trí chính xác trong process.

## 5. Decided but not completed

### DC-01 — Tách phạm vi Luật Ngoại Nhân khỏi luật nội quốc
STATUS: DECIDED, NOT IMPLEMENTED IN LAW FILE

- Quyết định phạm vi đã có.
- Chưa externalize vào `THE_KINGDOM_LAW_V2_CONSOLIDATED.md`.

### DC-02 — Rift/Dungeon phải được che ở cấp quân sự
STATUS: DECIDED, NOT IMPLEMENTED IN LAW FILE

- Công chúng ngoài chỉ được biết đây là lao động khổ sai.
- Chưa có thiết kế interface/biện pháp bảo mật cuối cùng.

### DC-03 — World Tree không dùng ngai vàng trong hướng hình ảnh hiện tại
STATUS: DECIDED, IMPLEMENTED IN CURRENT PROTOTYPE

- Prototype gần nhất đã bỏ ngai.
- Chưa có gia huy/huy hiệu riêng được chốt.

## 6. Resolved / closed

### RS-01 — Zetta không thuộc LAW V2 hiện tại
STATUS: RESOLVED

Resolution:
- Zetta/Guild/closed-space architecture đã bị loại khỏi bộ LAW V2.
- Không đưa trở lại workstream này trừ khi có yêu cầu mới.

Evidence:
- `THE_KINGDOM_LAW_V2_CONSOLIDATED.md` → design invariants / reset architecture.

Reopen only if:
- người dùng chủ động yêu cầu nhập lại một chức năng cụ thể.

### RS-02 — Không nerf AI để bảo tồn bureaucracy
STATUS: RESOLVED

Resolution:
- AI phải giữ năng lực concept gốc.
- Các thiết chế khác phải chứng minh chức năng của mình dựa trên authority, judgment, hiện diện vật lý hoặc nhu cầu khác; không được tồn tại bằng cách làm AI yếu đi.

Evidence:
- `THE_KINGDOM_LAW_V2_CONSOLIDATED.md` → `LAW_01_divine_eye.md`, `LAW_06_design_invariants.md`.

Reopen only if:
- canon mới thay đổi năng lực AI.

### RS-03 — Ngai vàng trong thiết kế hình ảnh World Tree
STATUS: RESOLVED FOR CURRENT VISUAL DIRECTION

Resolution:
- User yêu cầu xóa ngai vàng.
- Prototype gần nhất đã bỏ ngai.

Reopen only if:
- user yêu cầu đưa ngai hoặc một cấu trúc tương đương trở lại.

## 7. Conflicts / stale state

### CF-01 — LAW file hiện tại vs hướng tái nhập World Tree
STATUS: STALE / CONFLICTED

Conflict:
- `THE_KINGDOM_LAW_V2_CONSOLIDATED.md` hiện ghi World Tree/punishment V1 chỉ là genealogy, không phải baseline V2.
- Workstream mới đang cân nhắc đưa World Tree và một phần punishment V1 trở lại **riêng cho người ngoại quốc**.

Required handling:
- Không âm thầm coi file cũ đã cập nhật.
- Khi được yêu cầu sửa LAW, phải ghi rõ đây là phạm vi foreign-only để tránh biến World Tree thành authority mặc định cho luật nội quốc.

### CF-02 — V1 Giàn Hỏa Kiếp 100 năm vs proposal 1 tuần
STATUS: STALE / UNDER CONSIDERATION

Conflict:
- V1 genealogy dùng thời gian cực dài.
- Hướng mới đề xuất 1 tuần vì lý do vận hành.

Required handling:
- Không dùng lại con số 100 năm như mặc định.
- Không gọi 1 tuần là canon cuối cùng cho tới khi chốt.

### CF-03 — Visual concept có ngai vs hướng hiện tại không ngai
STATUS: STALE

Conflict:
- Một số prototype trước dùng ngai/throne như biểu tượng quyền lực.
- User đã loại bỏ ngai khỏi hướng hiện tại.

Required handling:
- Prototype có ngai chỉ là lịch sử thiết kế, không phải visual baseline.

## 8. Relevant source anchors

### Sources read / established
- `HANDOFF_TEMPLATE.md`
  - quy tắc tạo CURRENT handoff; handoff không phải chat summary và không tự cấp quyền implementation.
- `THE_KINGDOM_LAW_V2_CONSOLIDATED.md`
  - baseline LAW V2 hiện có;
  - AI native;
  - Ma'at basic;
  - Judgez basic;
  - sentencing/procedure reset;
  - design invariants.
- `the_kingdom_language_religion_meta.md`
  - World Tree, thần tính và meta tôn giáo.
- `the_kingdom_he_thong_phan_gian_va_kiem_soat_tri_thuc.md`
  - kiểm soát derivative information, oath/curse và bí mật.
- `the_kingdom_dia_chinh_tri_dmz_quan_he_quoc_te.md`
  - DMZ, mở cửa, giao lưu văn hóa, nguyên tắc không mặc định nhượng bộ.
- `the_kingdom_POT_personal_terminal_watch.md`
  - POT là interface cá nhân nếu sau này cần xác định cách AI/nhà nước trực tiếp thông báo luật cho người dùng.
- `a_dramatic_high_fantasy_scene_a_gigantic_ancient.png`
  - prototype World Tree gần nhất, đã bỏ ngai vàng nhưng chưa được chốt final.

### Sources mentioned but not required for current handoff
- `modular_engine_concept_anti_drift.md`
  - dùng khi cần kiểm tra module boundaries / proposal vs canon.
- `the_kingdom_pov_perspective_architecture.md`
  - phương pháp kể chuyện; không phải luật nội bộ.

## 9. Next-entry guidance

1. Bắt đầu bằng việc đọc:
   - `THE_KINGDOM_FOREIGN_JUSTICE_CURRENT.md`;
   - `THE_KINGDOM_LAW_V2_CONSOLIDATED.md`.
2. Không giả định handoff đã cập nhật LAW file.
3. Nếu tiếp tục thiết kế ontology:
   - chốt vai trò Ma'at;
   - chốt quyền Judgez;
   - chốt vai trò pháp lý của World Tree trong phạm vi ngoại nhân;
   - sau đó mới dựng procedure.
4. Nếu tiếp tục hệ punishment:
   - xác định ngưỡng tội;
   - thiết kế interface công khai cho lao động khổ sai nhưng giữ Rift/Dungeon bí mật;
   - chốt thời gian/công suất/quan sát của Giàn Hỏa Kiếp;
   - tách Chain Soul Destruction khỏi thủ tục xử người bị bắt nếu nó áp lên actor bên ngoài.
5. Nếu tiếp tục visual World Tree:
   - dùng prototype không ngai làm baseline hình ảnh tạm;
   - thiết kế biểu tượng/gia huy đơn giản riêng;
   - tránh quay lại tính đối xứng quá máy móc;
   - tránh dùng cân/lông nếu chúng thuộc Ma'at.
6. Chỉ khi người dùng yêu cầu cập nhật LAW mới sửa `THE_KINGDOM_LAW_V2_CONSOLIDATED.md`.
7. Nếu file CURRENT này được đưa vào Revamp Router sau này, cần thêm entry phù hợp khi được phép. Sự hiện diện của handoff không tự kích hoạt Router hay triển khai.

## 10. Explicit exclusions

- Không thiết kế luật dành cho người nội quốc trong workstream này.
- Không nhập Zetta/Guild/Earth-0 legacy architecture vào LAW.
- Không coi các proposal Ma'at/Judgez/World Tree trong handoff là canon nếu chưa được chốt.
- Không coi prototype World Tree gần nhất là thiết kế cuối.
- Không tự quyết định mức án, tử hình, appeal/review hoặc authority cuối khi chưa có quyết định.
- Không tự biến mục tiêu giao lưu văn hóa thành nghĩa vụ nhượng bộ.
- Không mở rộng sang toàn project The Kingdom, địa chính trị, y tế, POV hoặc các workstream khác nếu không ảnh hưởng trực tiếp tới Luật Ngoại Nhân.
- Handoff này không cấp quyền sửa Router, commit, push, deploy hoặc tự cập nhật file LAW.
- Không đưa file này vào Central Hub; nếu dùng trong Revamp thì vẫn là handoff của Revamp.
