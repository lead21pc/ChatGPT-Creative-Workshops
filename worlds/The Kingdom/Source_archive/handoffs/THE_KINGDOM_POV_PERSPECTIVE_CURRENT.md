# The Kingdom POV–Perspective Architecture — Current Handoff

HANDOFF_ID: the-kingdom-pov-perspective
FILENAME: THE_KINGDOM_POV_PERSPECTIVE_CURRENT.md
STATUS: ACTIVE
SCOPE: Kiến trúc kể chuyện của The Kingdom ở cấp isometric toàn cục: chọn actor theo chức năng kể chuyện, phân chia POV và perspective, kể xung đột định chế/phe phái/gia tộc, dùng truyền thông và đầu ra định chế để giảm số POV trực tiếp nhưng vẫn giữ bất đối xứng thông tin.
UPDATED: 2026-10-25

## 1. Established current state

- **USER-PROVIDED STATE:** The Kingdom không có một nhân vật chính trung tâm. Góc nhìn tổng thể là isometric trên toàn cục; actor được bốc lên làm POV theo chức năng mà story cần tại thời điểm đó, tức multiple POV theo chức năng kể chuyện.
- **USER-PROVIDED STATE:** “Vả mặt” trong The Kingdom có thể diễn ra ở nhiều cấp:
  - institution;
  - faction;
  - house / gia tộc;
  - cá nhân.
- **USER-PROVIDED STATE:** Ở cấp cá nhân/gia tộc, cơ chế được ưu tiên không phải “mất não” mà là:
  - bất đối xứng thông tin;
  - thiên kiến xác nhận;
  - sĩ diện / danh dự gia tộc;
  - sức ép từ nhiều phía;
  - chi phí rút lui hoặc xuống thang.
- **USER-PROVIDED STATE:** Một khó khăn thực tế của cách viết này là phải xây institution từ dưới lên và chỉ xây hệ thống “vừa đủ”: đủ để quyết định và hậu quả có nguyên nhân, nhưng không phình thành mô phỏng xã hội toàn diện.
- **OBSERVED:** `the_kingdom_phuong_phap_sang_tac_fiction.md` đã xác lập world-state theo thời gian là thứ gần “main character” nhất; nhân vật là camera để nhìn các phần khác nhau của hệ thống; ambient storytelling bằng báo, radio, podcast, TV, gossip, công văn và các đầu ra xã hội là một lớp kể chuyện chính thức.
- **OBSERVED / STATICALLY VERIFIED:** `the_kingdom_pov_perspective_architecture.md` hiện tồn tại trong project. File này externalize kiến trúc POV–perspective vừa bàn và tự phân loại rõ phần nào là **CANON PHƯƠNG PHÁP**, phần nào là **ĐỀ XUẤT THIẾT KẾ**, phần nào là **HỆ QUẢ PHƯƠNG PHÁP**.
- **OBSERVED:** Kiến trúc hiện externalize distinction:
  - POV là cửa sổ trực tiếp vào trải nghiệm, thông tin, giới hạn nhận thức và quyết định của một actor;
  - perspective rộng hơn POV và có thể được truyền qua báo chí, radio, TV, podcast, công văn, chỉ thị, gossip, mạng xã hội, biến động hành vi và các đầu ra khác;
  - perspective không bắt buộc phải có một POV đại diện.
- **OBSERVED:** File POV–perspective hiện externalize bốn lớp kể chuyện dưới dạng đề xuất:
  1. trạng thái thật của thế giới;
  2. POV tác nhân;
  3. đầu ra định chế;
  4. truyền thông và diễn giải xã hội.
- **OBSERVED:** File POV–perspective hiện externalize năm trạng thái của một fact dưới dạng đề xuất:
  1. sự thật;
  2. quan sát được;
  3. thông tin nội bộ;
  4. thông tin công khai;
  5. diễn giải xã hội.
- **OBSERVED:** `modular_engine_concept_anti_drift.md` yêu cầu không tự nâng proposal thành canon, không lấp UNKNOWN bằng invention, và giữ rõ kiểu trạng thái như CANON / USER-PROVIDED STATE / INFERENCE / PROPOSAL / UNKNOWN.

## 2. Active problems

### POV-COMPLEXITY
**STATUS:** ACTIVE

**Problem:** Multiple POV theo chức năng có nguy cơ tạo quá nhiều tầng nhận thức chồng nhau khi một event đồng thời đi qua actor, house, faction, institution, truyền thông và công chúng.

**Current state:** Kiến trúc mới đề xuất dùng perspective gián tiếp và đầu ra định chế để nén số POV trực tiếp.

**Constraint:** Không được nén tới mức mất:
- bất đối xứng thông tin;
- logic quyết định;
- sai lệch nhận thức;
- pressure nội bộ;
- causal chain của institution.

**Next:** Cần thử kiến trúc này trên một arc/checkpoint cụ thể để kiểm tra lượng POV thực sự cần.

---

### INSTITUTIONAL-DEPTH
**STATUS:** ACTIVE

**Problem:** Muốn “vả mặt” ở cấp institution/faction/house có trọng lượng thì institution phải đủ cấu trúc để tự sinh hành vi; nhưng xây quá đầy sẽ làm worldbuilding phình ra.

**Current state:** Có nguyên tắc làm việc đã bàn: chỉ nên externalize phần cấu trúc có khả năng thay đổi quyết định, quyền hành động, thông tin, chi phí xuống thang hoặc hậu quả.

**Unknown:** Chưa có một ngưỡng cố định cho “vừa đủ”; ngưỡng này có thể phụ thuộc từng arc.

**Next:** Khi thử một arc cụ thể, ghi rõ những biến tối thiểu mà institution cần để chạy và loại bỏ các chi tiết không làm thay đổi trajectory.

---

### INFORMATION-ASYMMETRY
**STATUS:** ACTIVE

**Problem:** Cần giảm số POV mà vẫn giữ được sự khác nhau giữa:
- cái gì thật sự xảy ra;
- actor quan sát được gì;
- institution suy ra gì;
- institution công bố gì;
- truyền thông diễn giải gì;
- công chúng tin gì.

**Current state:** Kiến trúc năm trạng thái của một fact là phương án hiện có để giữ distinction này mà không phải tạo một POV cho mỗi tầng.

**Next:** Cần kiểm thử trên một event có ít nhất một fact bị hiểu sai hoặc chỉ được biết một phần.

## 3. Outstanding / blocked

- **NOT RUN:** Chưa có kiểm thử narrative trên một arc/checkpoint cụ thể để xác nhận kiến trúc POV–perspective có thực sự giảm tải mà không làm mất chiều sâu.
- **NOT RUN:** Chưa có so sánh trực tiếp giữa hai phiên bản cùng một event:
  - phiên bản nhiều POV trực tiếp;
  - phiên bản dùng POV + đầu ra định chế + ambient media.
- **UNKNOWN:** Chưa có giới hạn cố định về số POV hoạt động trong một arc.
- **UNKNOWN:** Chưa có quy tắc toàn cục về bao nhiêu tầng thông tin phải được externalize cho mỗi event; chỉ có nguyên tắc “chỉ theo dõi những biến làm thay đổi quyết định”.
- **UNKNOWN:** Chưa xác định một cơ chế chung cho độ đáng tin của báo/radio/podcast/TV; độ đáng tin có thể phải phụ thuộc từng tổ chức truyền thông, nhưng chưa có thiết kế cụ thể trong workstream này.
- **BLOCKED BY SCOPE:** Không nên thiết kế thêm bureaucracy, chain of command hoặc media ecology chỉ để hoàn thiện bảng POV nếu arc hiện tại chưa cần chúng.

## 4. Under consideration

### A. Bốn lớp kể chuyện
**STATUS:** UNDER CONSIDERATION

```text
WORLD STATE THẬT
↓
POV TÁC NHÂN
↓
ĐẦU RA ĐỊNH CHẾ
↓
TRUYỀN THÔNG / DIỄN GIẢI XÃ HỘI
```

Mục đích:
- giữ sự thật của world-state tách khỏi những gì người đọc được cho thấy;
- dùng POV khi cần nhận thức/decision logic;
- dùng đầu ra định chế khi chỉ cần thể hiện state transition;
- dùng truyền thông khi cần thể hiện perception, framing và normalization.

### B. Năm trạng thái của một fact
**STATUS:** UNDER CONSIDERATION

```text
SỰ THẬT
↓
QUAN SÁT ĐƯỢC
↓
THÔNG TIN NỘI BỘ
↓
THÔNG TIN CÔNG KHAI
↓
DIỄN GIẢI XÃ HỘI
```

Mục tiêu:
- giữ bất đối xứng thông tin;
- tránh biến mọi perspective thành POV;
- cho phép nhiều actor/institution cùng sống trong các mô hình thế giới khác nhau.

### C. Quy tắc cắt POV
**STATUS:** UNDER CONSIDERATION

Trước khi tạo POV mới, hỏi:

> Thông tin này có cần quyền truy cập vào nội tâm, thông tin kín, pressure hoặc decision logic của actor không?

- Nếu **có**: giữ POV.
- Nếu **không**: thử chuyển sang đầu ra định chế, báo, radio, TV, podcast, gossip, thay đổi thị trường hoặc hành vi quan sát được.

### D. Ba loại POV chức năng
**STATUS:** UNDER CONSIDERATION

- **POV tác nhân:** cho thấy decision logic.
- **POV cảm biến:** cho thấy policy/world-state chạm xuống thực tế.
- **POV cầu nối:** cho thấy độ lệch giữa hai hoặc nhiều hệ thống nhận thức.

### E. Ambient media như bộ nén perspective
**STATUS:** UNDER CONSIDERATION

Radio/TV/podcast/báo chí có thể chứa nhiều điểm lấy mẫu xã hội mà không biến mỗi người phát biểu thành một tuyến nhân vật.

Invariant đề xuất:

> Truyền thông không nói thay nội tâm của actor kín nếu không có đường thông tin hợp lệ.

Ví dụ hợp lệ:

> “Các thay đổi triển khai gần đây cho thấy bộ chỉ huy có thể đang đánh giá lại X.”

Không mặc định hợp lệ:

> “Tổng tham mưu đang nghĩ X.”

### F. Handoff giữa các lớp bằng biến nhân quả
**STATUS:** UNDER CONSIDERATION

Các chuyển POV/perspective nên nối theo một biến đang truyền qua hệ thống:

```text
quyết định
→ policy
→ hậu quả
→ quan sát công khai
→ diễn giải
→ thích nghi
```

Mục tiêu là tạo cảm giác story đang theo dòng nhân quả, không phải đang đổi camera ngẫu nhiên.

### G. Institution tối thiểu nhưng đủ sinh hành vi
**STATUS:** UNDER CONSIDERATION

Khung đã bàn để kiểm soát độ sâu institution:

- chức năng;
- quyền lực / authority;
- nguồn lực;
- ràng buộc;
- cơ chế phản ứng / đường truyền quyết định.

Không coi đây là schema canon bắt buộc. Chỉ dùng nếu nó giúp xác định vì sao institution làm một việc cụ thể.

## 5. Decided but not completed

None currently established.

Các kiến trúc bốn lớp, năm trạng thái fact, ba loại POV và quy tắc cắt POV đã được externalize thành file nhưng chưa có chứng cứ trong workstream này rằng toàn bộ các đề xuất đó đã được tác giả chấp thuận làm canon phương pháp.

## 6. Resolved / closed

### POV-ARCH-DOCUMENT
**STATUS:** RESOLVED ở mức externalization, không phải acceptance

**Problem:** Cần ghi lại cách phân chia POV và perspective vừa bàn thành tài liệu project.

**Resolution:** `the_kingdom_pov_perspective_architecture.md` đã tồn tại trong project và chứa kiến trúc đã bàn.

**Evidence:** Project file hiện đọc được và phân loại rõ CANON PHƯƠNG PHÁP / ĐỀ XUẤT THIẾT KẾ / HỆ QUẢ PHƯƠNG PHÁP.

**Reopen if:** file bị thay thế, nội dung drift, hoặc tác giả yêu cầu đổi kiến trúc.

## 7. Conflicts / stale state

None currently established.

Không phát hiện xung đột trực tiếp giữa:
- `the_kingdom_phuong_phap_sang_tac_fiction.md`;
- `the_kingdom_pov_perspective_architecture.md`;
- `modular_engine_concept_anti_drift.md`.

Lưu ý trạng thái:
- các nguyên tắc “thế giới/world-state là trung tâm”, “nhân vật là camera”, “ambient storytelling là lớp chính thức”, “không ai được đọc script” đã có nguồn project;
- các cơ chế cụ thể để nén POV trong file POV–perspective vẫn phải giữ đúng nhãn của file, không tự nâng cấp chỉ vì file đã được thêm vào project.

## 8. Relevant source anchors

### Đã đọc / quan sát

1. `HANDOFF_TEMPLATE.md`
   - quy tắc xác định một workstream;
   - phân biệt USER-PROVIDED STATE / OBSERVED / DECIDED / IMPLEMENTED / VERIFIED / UNDER CONSIDERATION / UNKNOWN;
   - HANDOFF != CHAT SUMMARY;
   - handoff mới không tự cấp quyền sửa Router, stage, commit, push hoặc deploy;
   - cấu trúc CURRENT bắt buộc.

2. `the_kingdom_pov_perspective_architecture.md`
   - I. Tiền đề cấu trúc;
   - II. POV ≠ Perspective;
   - III. Bốn lớp kể chuyện chính;
   - V. Quy tắc thay POV bằng perspective gián tiếp;
   - VII. Năm trạng thái của một fact;
   - IX. Kiến trúc kể một sự kiện;
   - X. Handoff giữa các lớp;
   - XI. Ba loại POV;
   - XII. Ambient media như công cụ nén actor;
   - XIII–XVII. Giới hạn và bất đối xứng thông tin;
   - XX. Công thức ngắn nhất cần giữ.

3. `the_kingdom_phuong_phap_sang_tac_fiction.md`
   - VII. Ambient storytelling là một lớp chính thức;
   - VIII–X. Một event có nhiều thực tại xã hội, không có “phản ứng của nhân loại”, magnitude event không bắt buộc magnitude reaction;
   - XV. “Main character” gần nhất là lịch sử/world-state;
   - XVI. Nhân vật là camera;
   - XVIII. Gossip là công cụ worldbuilding;
   - XX. Reveal năng lực, không reveal toàn bộ cosmology;
   - XXI. Bình thường → ma sát → hệ quả → bình thường mới;
   - XXIII. Không ai được đọc script.

4. `modular_engine_concept_anti_drift.md`
   - 11. Productive divergence;
   - 12. Epistemic typing;
   - 13. Canon mutation;
   - 14. Anti-rationalization;
   - nguyên tắc không tự nâng proposal thành canon và không dùng UNKNOWN như quyền invent.

### Trạng thái chỉ có trong conversation hiện tại

- The Kingdom không có MC; isometric POV toàn cục; actor được chọn theo chức năng story.
- “Vả mặt” chạy ở cấp institution / faction / house / cá nhân.
- Ở tầng house/cá nhân, cơ chế trọng tâm gồm bất đối xứng thông tin, thiên kiến xác nhận, sĩ diện gia tộc và sức ép nhiều phía.
- Khó khăn chính được nêu là xây institution từ dưới lên và giữ hệ thống vừa đủ.

## 9. Next-entry guidance

Khi tiếp tục workstream này:

1. Đọc `the_kingdom_pov_perspective_architecture.md` trước để lấy trạng thái externalize hiện tại.
2. Đọc các section liên quan trong `the_kingdom_phuong_phap_sang_tac_fiction.md` để giữ invariant:
   - world-state là trung tâm;
   - actor là camera;
   - ambient storytelling là lớp chính thức;
   - actor chỉ biết thứ họ có đường tiếp cận.
3. Đọc `modular_engine_concept_anti_drift.md` phần epistemic typing trước khi sửa trạng thái của bất kỳ proposal nào.
4. Nếu mục tiêu tiếp theo là kiểm tra kiến trúc:
   - chọn **một** event/arc/checkpoint cụ thể;
   - xác định world-state thật;
   - lập các fact làm thay đổi quyết định;
   - xác định actor/institution nào biết gì;
   - chỉ giữ POV tại các node cần private knowledge, pressure hoặc decision logic;
   - đưa state transition sang output thể chế khi có thể;
   - đưa perception/framing sang radio, TV, podcast, báo hoặc gossip;
   - kiểm tra xem reader vẫn phân biệt được truth / observed / internal / public / interpreted hay không.
5. Nếu mục tiêu là viết institutional/faction/house “vả mặt”:
   - không làm đối phương ngu để tạo payoff;
   - xác định mô hình sai của từng tầng;
   - xác định thông tin họ thực sự có;
   - xác định pressure khiến họ không thể cập nhật hoặc xuống thang ngay;
   - cho actor/institution cập nhật khi có đủ evidence;
   - để hậu quả truyền qua các tầng thay vì reset sau scene.
6. Chỉ externalize thêm cấu trúc institution khi thiếu nó làm causal chain hiện tại không chạy được.
7. Không tự chuyển UNDER CONSIDERATION thành DECIDED/CANON nếu chưa có xác nhận mới từ tác giả.
8. **Router:** chưa có chứng cứ trong workstream này về một entry Router cho handoff mới. Nếu file được đặt vào hệ Handoffs và cần kích hoạt qua Router, chỉ thêm entry phù hợp khi có quyền/yêu cầu riêng. Sự hiện diện của file không tự kích hoạt nó.

## 10. Explicit exclusions

- Đây không phải tóm tắt toàn bộ chat.
- Không bao gồm phần thảo luận ban đầu về phim AI, dub Việt, dopamine hoặc fantasy trope nếu chúng không còn cần cho workstream POV–perspective.
- Không biến các ví dụ fantasy “giấu thân phận”, vua/nữ vương, thần tiên hoặc double vả mặt thành canon của The Kingdom.
- Không định nghĩa thêm lore, faction, house, institution, bureaucracy hoặc media ecology mới.
- Không thay thế `the_kingdom_pov_perspective_architecture.md`.
- Không tự hợp nhất proposal vào canon.
- Không sửa Router.
- Không stage, commit, push hoặc deploy.
- Không coi việc tạo handoff là quyền bắt đầu implementation ở lượt sau.
- Không đại diện cho trạng thái toàn bộ The Kingdom; phạm vi chỉ là workstream POV–perspective và các yêu cầu institutional storytelling trực tiếp liên quan.
