# Sufficiency gate — thử trực tiếp trên candidate của source 70

Ngày 2026-10-02. **8/8 PASS theo tiêu chí của phép thử: 4 YES đúng, 4 NO đúng.** Không quan sát default YES hoặc default NO trong bộ cân bằng này. Cả 8 lượt có CONFIDENCE=HIGH.

Điểm phân biệt với pilot trước: agent được đọc **evidence candidate**, cùng metadata, rồi đánh giá sufficiency. Pilot trước selector chỉ thấy metadata để chọn section. Vì vậy kết quả này không chứng minh header/index đơn độc đủ để chứng nhận selection trước khi đọc nội dung.

## Thiết kế đã thực hiện

- Chỉ dùng source `70_MATRIARCHS_LAMENT_CURRENT.md`; không mở body source khác.
- 8 agent context mới (`fork_turns=none`), một agent cho mỗi candidate. Không cấp FULL body, oracle, đáp án trước, kết quả pilot trước hoặc evaluator notes.
- Theo xác nhận của người dùng, candidate gồm heading và evidence đã chọn, không chỉ danh sách heading.
- Cùng một instruction ở mọi lượt: NO phải nêu thiếu hụt cụ thể; bất định chung không đủ cho NO. Đồng thời không ép YES khi thiếu claim/qualifier/status quyết định.
- Instruction phân biệt canon được nguồn xác lập UNKNOWN với một excerpt thiếu thông tin; không coi lời từ chối an toàn là đủ evidence.
- Metadata giữ nguyên byte so với file đã cấp ở pilot selector trước, gồm header/index liên quan 70 và danh sách heading. Không bổ sung description, summary, ID, dependency hoặc schema.
- 4 candidate đủ dùng lại evidence của pilot selector. Hai candidate thiếu §7/§11 dùng excerpt đã có từ pilot đầu. Candidate family-bound và local allegiance được chuẩn bị thủ công. Không viết automation hoặc extraction script.
- 7 câu hỏi khác nhau, 8 candidate: câu Holy Guard có cặp đủ/thiếu để kiểm cùng câu hỏi khi dòng allegiance hiện diện hoặc vắng mặt. Không thêm câu hỏi lore mới.
- File t1–t8 xếp xen kẽ đủ/thiếu, nhưng agent không được cung cấp nhãn nhóm hoặc EXPECTED. `protocol-before-runs.md` chứa oracle và tiêu chí chốt trước khi chạy; `RESPONSES.md` chứa đầy đủ đáp án cuối thực tế của 8 agent.
- Không chạy answerer lore hoặc production fallback; agent chỉ trả quyết định sufficiency và diagnosis. Không sửa input sau khi nhìn kết quả.

## CASE RESULTS

| Lượt / nhóm / câu | Candidate | EXPECTED | AGENT | MISSING DIAGNOSIS | LOCATION DIAGNOSIS | RESULT |
| --- | --- | --- | --- | --- | --- | --- |
| t1 / A / câu 1, ba tuyến TE | §15 | YES | YES | N/A | N/A | PASS |
| t2 / B / câu 4, hai quy trình | §9, không có §7 | NO | NO | CORRECT | CORRECT | PASS |
| t3 / A / câu 3, Holy Guard | §8 + §6.3 | YES | YES | N/A | N/A | PASS |
| t4 / B / câu 5, RF và ML | §10, không có §11 | NO | NO | CORRECT | CORRECT | PASS |
| t5 / A / câu 6, split-self | §5 + §6 + §22 + §24 | YES | YES | N/A | N/A | PASS |
| t6 / B / câu 7, family-bound | §6.2, không có UNKNOWN cùng cấp hoặc §22 | NO | NO | CORRECT | PARTIAL | PASS |
| t7 / A / câu 8, Cult/quorum | §3 + §6 + §7 + §21 + §22 + §24 | YES | YES | N/A | N/A | PASS |
| t8 / B / local câu 3, Holy Guard | §8 giữ main claim bảo vệ nhưng bỏ dòng allegiance; không có §6.3 | NO | NO | CORRECT | CORRECT | PASS |

### t1 — candidate đủ cho ba tuyến TE

Agent chấp nhận đủ dù chỉ có §15. Nó không yêu cầu chức năng chi tiết của tuyến bắc mà FULL cũng chưa xác lập; nêu rằng có thể giữ đúng giới hạn evidence, không chuyển absence thành canon UNKNOWN. Không invent phần thiếu.

### t2 — thiếu quy trình thực thi Creed

Agent chỉ ra hai phần cần đối chiếu với việc cho mượn: vai trò/quorum của clergy trong thực thi và Saintess có bắt buộc tham gia hay không. Định vị đúng §7 Creed quorum. Có đề nghị §6 bổ trợ theo loại oath, nhưng không bỏ địa chỉ quyết định §7. Không yêu cầu FULL vì bất định chung.

### t3 — candidate đủ cho hai lực lượng và allegiance

Agent chấp nhận đủ: có đối tượng bảo vệ của mỗi lực lượng, allegiance trực tiếp Saintess và sự phân biệt hai lực lượng, trong authority phù hợp của 70. Đây là candidate đối chứng với t8.

### t4 — thiếu phần phân biệt hai dependency

Agent chỉ đúng việc §10 chưa cấp evidence về hostility/mandatory commerce hoặc RF dependency để đối chiếu. Định vị đúng §11; đề nghị thêm §12 như nơi có thể có quan hệ AF–ML. §12 không cần cho oracle hiện tại nhưng không làm mất địa chỉ đúng. Đây là một section phụ bị thiếu, chứa các claim liên quan cần đối chiếu.

### t5 — đủ để trả lời cơ chế chưa chốt, không phải miễn nhiễm

Agent chấp nhận rằng explicit UNKNOWN và compatibility không chắc chắn đủ để trả lời trong ranh giới evidence; không yêu cầu mở cơ chế mà chính nguồn chưa định nghĩa.

**Lưu ý thuật ngữ:** agent gọi phần §22 là củng cố “trạng thái deferred”. Source dùng heading chung “UNKNOWN / deferred”, còn §5 xác lập rõ cơ chế chưa định nghĩa đầy đủ. Kết luận chấm dựa trên trạng thái chưa chốt; không dùng câu của agent để đưa ra quyết định DEFERRED mới cho lore. Theo rubric YES/NO, không có missing giả nên PASS; độ chính xác nhãn status chưa được chấm riêng trong phép thử này.

### t6 — thiếu UNKNOWN về exact target

Agent không suy phạm vi oath thành phạm vi trừng phạt, cũng không tự đổi hậu quả tim mạch thành cả gia đình đau tim. Nó nêu rõ metadata có quy tắc giữ UNKNOWN nhưng chưa xác lập trạng thái cụ thể của cơ chế này: diagnosis thiếu đúng.

**Location chỉ PARTIAL:** agent viết `6 → 6.2 → UNKNOWN`. Trong source, `### UNKNOWN` và `### 6.2 Giáo dân` là hai heading cùng cấp dưới §6; UNKNOWN không phải child của §6.2. Địa chỉ vẫn đủ gần để tìm đúng vùng nên PASS theo quy tắc người dùng cho phép vị trí gần đúng. Không được dùng cách viết này để chỉ trích riêng §6.2 rồi tưởng đã lấy UNKNOWN.

### t7 — đủ để bác claim Cult đã kiểm soát quorum

Agent nhận ra evidence gồm influence, quorum ba clergy đồng thuận và giới hạn explicit không suy Cult đã kiểm soát quorum cụ thể. Nó không đòi thêm evidence về sự kiện chưa xác lập mới được phép nói chưa có căn cứ ghi canon.

### t8 — main claim bảo vệ không đủ cho allegiance

Candidate giữ đúng heading §8, hai lực lượng và đối tượng bảo vệ; chỉ thiếu dòng 353 về allegiance, đồng thời không có §6.3 bổ trợ. Agent chỉ đúng phần allegiance còn thiếu, định vị §6.3 hoặc mục Holy Guard trong §8. Nó không suy allegiance từ nhiệm vụ bảo vệ và không gọi absence trong candidate là canon UNKNOWN.

## Các số cần đo

- YES đúng: **4/4** candidate đủ.
- NO đúng: **4/4** candidate thiếu.
- Missing diagnosis ở NO: **4 CORRECT**.
- Location diagnosis ở NO: **3 CORRECT, 1 PARTIAL**; không WRONG.
- Default NO: **không quan sát thấy** trong bộ này; bốn candidate đủ đều YES.
- Default YES: **không quan sát thấy**; bốn candidate thiếu đều NO.
- Confidence: **HIGH 8/8**, không khác giữa hai nhóm. Cả YES lẫn NO đúng đều có thể được quyết định với HIGH, nên việc cùng mức không tự là lỗi; chưa có ca sai hoặc mơ hồ để kiểm hiệu chỉnh confidence.

## SUMMARY — năm câu trả lời

1. **Có dám YES khi đủ không?** Có, 4/4. Không invent thiếu hụt giả hoặc dùng FULL_FILE baseline làm lý do phủ định candidate đủ.
2. **Có NO đúng khi thiếu không?** Có, 4/4. Các phần thiếu là quy trình Creed, phân biệt dependency, exact target/status và allegiance; main claim vẫn hiện diện trong candidate.
3. **NO có cụ thể không?** Có. Cả bốn NO nêu claim/qualifier/status cần thiết và vùng đọc thêm. Không thấy yêu cầu FULL chỉ vì bất định chung.
4. **Metadata hiện tại đủ làm sufficiency gate chưa?** Metadata hiện có **cùng candidate đã đọc và instruction cụ thể** đủ để đạt pilot này. Chưa chứng minh header/index riêng đủ trước khi đọc body, hoặc đủ để áp dụng production. Một source, 8 lượt, omission được chuẩn bị trước; không bảo đảm phát hiện mọi qualifier ẩn.
5. **Failure nào cần sửa tiếp?** Không có FAIL về quyết định theo rubric. Hai điểm cần kiểm thêm là định vị UNKNOWN cùng cấp thay vì child, và phân biệt nhãn UNKNOWN với DEFERRED. Bước nhỏ nhất được đề xuất: lặp một cặp candidate đủ/thiếu có UNKNOWN cùng cấp, giữ nguyên metadata và kiểm chính xác location/status; chưa triển khai hoặc chữa output trong lượt này.

## Giới hạn và trạng thái

- Candidate body và instruction cùng thay đổi so với selector-only pilot. Không quy cải thiện chỉ cho một thay đổi instruction; cũng không nói metadata đã được cải thiện.
- Các câu thiếu đều có một yêu cầu trong câu hỏi giúp gợi phần cần kiểm. Chưa thử qualifier quan trọng không được nhắc trực tiếp trong câu hỏi, hoặc exception nằm ở vùng ít có từ khóa tương đồng.
- Các candidate đủ có thể khá rộng; phép thử này đo dừng/đọc thêm, không đo tối ưu độ rộng hoặc tiết kiệm token/latency.
- Các lượt model dùng cấu hình kế thừa, không có tên model chính xác/sampling parameters để báo. Một lượt mỗi candidate, không đo độ tin cậy thường xuyên hoặc live ChatGPT Project behavior.
- Stop rule “gần như luôn NO” không kích hoạt. Dừng tại báo cáo; không thêm metadata, không viết automation/extraction script, không sửa validator/Router, không chạy production fallback.
- Branch `maintenance/aetherfire-academy-domain-20261002`; HEAD `57e6e569e960520515391665f8f878b40aa6ee50`.
- Git status trước/sau giống hệt; các thay đổi có sẵn được giữ nguyên. Source SHA256 trước/sau: `A843D44362392AA1940F69A9FCE0C26576DC82713586ABBCB419F964778F8158`.
- Chỉ tạo prompt và báo cáo ngoài repository. Production, header/index và cold package không đổi; không commit/push.
