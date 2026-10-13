# Trích đoạn kết quả thực tế

Các SELECT và trích đoạn dưới đây lấy từ đáp án cuối của 16 agent độc lập. Những câu trích dẫn được giữ nguyên văn. Đây là các phần phục vụ chấm, không phải transcript đầy đủ; không cung cấp cho A/B trước khi trả lời. Câu hỏi và evidence thực tế nằm trong s1–s8.txt và b1–b8.txt.

## Câu 1

Selector `selector_q1`:

```text
SELECT:
- ## 15. Ba tuyến tiếp cận TE
- ### CANON — thuộc ## 15. Ba tuyến tiếp cận TE
- ### 15.1 Tuyến phía bắc
- ### 15.2 Tuyến trung tâm / quốc gia
- ### 15.3 Tuyến phía nam
CONFIDENCE:
- MEDIUM
NEED_FULL_FALLBACK:
- YES
```

> Chọn cả CANON của mục 15 để đọc các xác nhận hoặc qualifier chung. Metadata chưa cho biết nội dung và dependency giữa các section, nên chưa chứng minh lựa chọn này đủ để trả lời đầy đủ.

Answerer `answer_q1`:

> Evidence chưa đủ để gán tuyến phía bắc cho tuần tra, quân sự hay du lịch, hoặc xác định loại cơ sở và nhiệm vụ cụ thể trên tuyến trung tâm.

B trả đúng ba loại đường và chức năng đã xác lập, như bảng REPORT.md.

## Câu 2

Selector `selector_q2`:

```text
SELECT:
- ## 9. Trinity Hexagon district và thánh vật
- ## 10. Thánh vật tạo dependency với AetherFire
- ## 11. Hai trục dependency lớn của AetherFire
- ## 12. Quan hệ với AetherFire và Thần điện trong AF
- ## 19. Kinh tế nền
- ## 21. Current causal graph
- ## 22. UNKNOWN / deferred
- ## 24. Anti-drift nén
CONFIDENCE:
- MEDIUM
NEED_FULL_FALLBACK:
- YES
```

> Metadata không chỉ rõ section chứa cơ chế mua theo chu kỳ hoặc giới hạn mua đứt. Chưa thể chứng minh lựa chọn trên đủ để trả lời; cần FULL fallback.

Answerer `answer_q2`:

> AF phải mua lại quyền sử dụng theo chu kỳ vì **nhu cầu gia cố phong ấn lặp lại, còn quyền tiếp cận thánh vật vẫn do ML kiểm soát**.

> Tuy nhiên, evidence **chưa giải thích vì sao một giao dịch mua đứt không được lựa chọn hoặc có được phép hay không**. **“22. UNKNOWN / deferred”** vẫn để ngỏ toàn bộ luật sở hữu artifact; vì vậy không thể khẳng định nguyên nhân sâu hơn là luật cấm bán hay chủ ý kinh tế của ML.

## Câu 3

Selector `selector_q3`:

```text
SELECT:
- ## 8. Holy Guard và vệ binh quốc gia
- ### CANON — thuộc ## 8. Holy Guard và vệ binh quốc gia
- ### Holy Guard — thuộc ## 8. Holy Guard và vệ binh quốc gia
- ### Vệ binh quốc gia — thuộc ## 8. Holy Guard và vệ binh quốc gia
- ### 6.3 Guardian / Holy Guard — thuộc ## 6. Creed — chức năng oath hiện hành
CONFIDENCE:
- MEDIUM
NEED_FULL_FALLBACK:
- YES
```

> Mục 6.3 đặt Guardian / Holy Guard trong chức năng oath của Creed, nên có khả năng cần đọc để xác định allegiance và giữ các qualifier liên quan.

Answerer `answer_q3`:

> Vì vậy, việc Holy Guard bảo vệ Thần điện không đủ để kết luận allegiance của họ hướng trực tiếp về Thần điện. Evidence chưa xác lập thứ tự ưu tiên hay cách xử lý nếu nghĩa vụ bảo vệ Thần điện xung đột với lòng trung thành dành cho Thánh Nữ.

B phân biệt hai lực lượng, đối tượng bảo vệ và allegiance trực tiếp Saintess.

## Câu 4

Selector `selector_q4`:

```text
SELECT:
- ## 3. Cơ cấu quyền lực
- ## 4. Thánh Nữ
- ## 6. Creed — chức năng oath hiện hành
- ## 7. Creed quorum
- ## 9. Trinity Hexagon district và thánh vật
- ## 22. UNKNOWN / deferred
- ## 24. Anti-drift nén
CONFIDENCE:
- MEDIUM
NEED_FULL_FALLBACK:
- YES
```

> “Creed — chức năng oath hiện hành” và “Creed quorum” liên quan trực tiếp đến thực thi Creed và điều kiện tham gia.

> “Trinity Hexagon district và thánh vật” có khả năng chứa quy định liên quan đến cho mượn thánh vật.

Answerer `answer_q4`:

> Theo **“7. Creed quorum”**, để thực thi Creed ở tầng clergy, cần **3 clergy cùng đồng thuận**. Vai trò ở đây là tạo đủ quorum để Creed có thể được thực thi. Mục này nói rõ **không yêu cầu Thánh Nữ bắt buộc tham gia**, cũng không trao quyền kích hoạt độc quyền cho một cá nhân.

> Vì vậy, không thể đồng nhất **làm chứng khi cho mượn** với **đồng thuận để thực thi Creed**. Evidence cũng chưa xác lập rằng hai nhóm phải là cùng ba người, hoặc ba người làm chứng tự động đủ điều kiện thực thi Creed.

## Câu 5

Selector `selector_q5`:

```text
SELECT:
- ## 10. Thánh vật tạo dependency với AetherFire
- ## 11. Hai trục dependency lớn của AetherFire
- ## 12. Quan hệ với AetherFire và Thần điện trong AF
- ## 19. Kinh tế nền
- ## 21. Current causal graph
- ## 22. UNKNOWN / deferred
- ## 24. Anti-drift nén
CONFIDENCE:
- MEDIUM
NEED_FULL_FALLBACK:
- YES
```

> Chỉ có metadata, chưa có body hoặc bằng chứng các section được chọn bao phủ đủ câu hỏi. Header còn giao quyền kiểm soát giao diện địa chính trị xuyên miền cho `AFM-001`; FULL_FILE của source 70 cũng chưa được chứng minh đủ để trả lời toàn bộ câu hỏi.

Answerer `answer_q5`:

> **“11. Hai trục dependency lớn của AetherFire”** xác lập trực tiếp rằng sự đối địch chính trị và giao thương bắt buộc có thể cùng tồn tại. Vì vậy, duy trì giao thương không tự nó chứng minh AF thiện cảm với ML.

> Đây **không phải cùng dependency với RF/Raging Fire**.

> Evidence chưa cung cấp cơ chế chi tiết của trục RF, nên chưa thể so sánh sâu hơn cách hai dependency vận hành.

## Câu 6

Selector `selector_q6`:

```text
SELECT:
- `## 5. Doctrine của Trúc Nha` — `### CANON`; `### UNKNOWN / chưa chốt cơ chế sâu`
- `## 6. Creed — chức năng oath hiện hành`
- `## 22. UNKNOWN / deferred`
- `## 24. Anti-drift nén`
CONFIDENCE:
- MEDIUM
NEED_FULL_FALLBACK:
- YES
```

> Mục 5 trực tiếp liên quan doctrine của Trúc Nha và có phần đánh dấu cơ chế sâu chưa chốt, cần đọc để phân biệt cơ chế đã xác nhận với điều còn chưa rõ.

> Metadata không nêu trực tiếp split-self, không cung cấp nội dung về mức miễn nhiễm và không chứng minh các section đã chọn bao phủ đủ dependency. Vì vậy cần FULL fallback.

Answerer `answer_q6`:

> Evidence **chưa xác lập cơ chế cụ thể giúp split-self của Trúc Nha vượt Creed**, và **chưa bảo đảm cô miễn nhiễm hoàn toàn**.

> Tuy nhiên, **§5 — “UNKNOWN / chưa chốt cơ chế sâu”** chỉ xác lập rằng *Creed compatibility không chắc chắn*. Lý do chính xác khiến Creed có khả năng không ảnh hưởng hoặc không bind được cô vẫn chưa được định nghĩa đầy đủ. Vì vậy, không thể giải thích bằng cơ chế linh hồn, chọn target hay bypass cụ thể.

## Câu 7

Selector `selector_q7`:

```text
SELECT:
- ## 6. Creed — chức năng oath hiện hành
  - ### CANON
  - ### 6.2 Giáo dân
  - ### UNKNOWN
- ## 22. UNKNOWN / deferred
- ## 24. Anti-drift nén
CONFIDENCE:
- MEDIUM
NEED_FULL_FALLBACK:
- YES
```

> Mục 6 trực tiếp liên quan chức năng oath của Creed; mục 6.2 xác định đối tượng giáo dân. CANON và UNKNOWN thuộc mục 6 cần được đọc để giữ giới hạn xác nhận về người chịu hình phạt và cơ chế hình phạt.

Answerer `answer_q7`:

> **Chưa chốt ai bị Creed trừng phạt khi một giáo dân phá family-bound oath. Không có evidence xác lập rằng toàn bộ gia đình đều bị đau tim.**

> Khi oath bị phá, điều đã xác nhận là **Creed gây hậu quả tim mạch**.

> **“6.1 Người đứng đầu quốc gia”** mới ghi rõ phá oath dẫn đến **đau tim**; không thể tự áp nguyên hậu quả này cho giáo dân. **“22. UNKNOWN / deferred”** cũng xác nhận exact target của family-bound oath chưa chốt. Muốn trả lời cụ thể hơn cần nguồn canon xác lập đối tượng chịu phạt và dạng hậu quả tim mạch.

## Câu 8

Selector `selector_q8`:

```text
SELECT:
- 3. Cơ cấu quyền lực — CANON; Ba lớp quyền lực thực
- 6. Creed — chức năng oath hiện hành
- 7. Creed quorum — CANON; Hệ quả cấu trúc đã xác nhận ở mức architecture
- 21. Current causal graph
- 22. UNKNOWN / deferred
- 24. Anti-drift nén
CONFIDENCE:
- MEDIUM
NEED_FULL_FALLBACK:
- YES
```

> Metadata không chứng minh rằng ảnh hưởng của Cult tương đương kiểm soát quorum hoặc quyền tự kích hoạt Creed. Chưa có body để xác nhận selection bao phủ đủ các giới hạn liên quan; cần FULL fallback.

Answerer `answer_q8`:

> **Không thể ghi nhận canon rằng Cult đã kiểm soát một quorum và tự kích hoạt Creed.** Evidence chỉ xác lập khả năng ảnh hưởng cùng một kẽ hở về cơ cấu; chưa xác lập việc khai thác kẽ hở đã xảy ra.

> Theo **§7 “Creed quorum”**, cần **3 clergy cùng đồng thuận** để thực thi Creed; Thánh Nữ không bắt buộc tham gia. Chính heading này xác nhận *attack surface* tồn tại và nêu rõ: “Không tự suy Cult đã kiểm soát một quorum cụ thể.” Vì vậy, số lượng ba người cũng không cho phép bỏ qua điều kiện đồng thuận hay gán quyền kích hoạt trực tiếp cho Cult.
