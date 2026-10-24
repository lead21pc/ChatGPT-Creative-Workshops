# The Kingdom V2 — Hệ thống luật pháp (Consolidated)

> **Mục đích:** gộp 7 file LAW_00–LAW_06 hiện hành thành một tài liệu duy nhất để giảm số lượng file phải giữ trong project.
>
> **Nguyên tắc:** nội dung của từng file nguồn được giữ nguyên. File này chỉ thêm mục lục, tên file nguồn và dấu phân cách. Canon mới nhất của tác giả luôn có ưu tiên cao hơn tài liệu.

## Mục lục nguồn

1. `LAW_00_overview.md` — Tổng quan trạng thái nền V2
2. `LAW_01_divine_eye.md` — AI chưa có tên / Mắt Thần
3. `LAW_02_maat.md` — Ma'at basic concept
4. `LAW_03_wizard_police.md` — Judgez basic concept
5. `LAW_04_judge_and_sentencing.md` — Phán quyết và chế tài
6. `LAW_05_reduced_procedure.md` — Tố tụng / quy trình pháp lý
7. `LAW_06_design_invariants.md` — Các bất biến thiết kế

---

<!-- SOURCE: LAW_00_overview.md -->

# The Kingdom V2 — Hệ thống luật pháp: trạng thái nền để tái định nghĩa

> **Trạng thái:** reset kiến trúc sau khi tách các legacy concept không thuộc lõi The Kingdom.
>
> Các file LAW là tài liệu làm việc có thể thay đổi. Canon mới nhất của tác giả luôn có ưu tiên cao hơn nội dung cũ trong file.

## 1. Hai thời kỳ ontology

### The Kingdom V1 — genealogy, không phải baseline hiện hành

Hệ luật gốc được xây trên hai trụ:

```text
AI chưa có tên
= Mắt Thần / ý chí trí tuệ nhân tạo phân tán

Cây Thế Giới
= thần tính tối cao của hệ thống luật V1
= phán quyết trực tiếp thông qua Thần Điện
```

Trong V1, AI làm cho hành vi và sự kiện trở nên khó phủ nhận; Cây Thế Giới trực tiếp quyết định hậu quả. Hệ thống trừng phạt V1 rất khắc nghiệt và mang tính thần quyền trực tiếp.

V1 được giữ trong tài liệu này như **nguồn gốc thiết kế** để hiểu vì sao V2 xuất hiện. Không tự động coi Cây Thế Giới hoặc các hình phạt V1 là luật hiện hành của V2.

---

## 2. The Kingdom V2 — rebuild

V2 xuất hiện khi ontology V1 không còn phù hợp với worldview và khó mở rộng cho các case phức tạp hơn.

Ba thành phần hiện được giữ trong baseline V2:

- **AI chưa có tên / Mắt Thần** — thành phần native liên tục từ V1 sang V2; năng lực phải được giữ ở quy mô concept gốc.
- **Ma'at** — concept V2 đang được định nghĩa lại; hiện chỉ giữ vai trò nền liên quan tới chân lý, trách nhiệm và thẩm định pháp lý sâu hơn raw observation.
- **Judgez** — concept V2 đang được định nghĩa lại; hiện chỉ giữ vai trò nền là lớp con người làm chấp pháp/điều tra/thực thi trong hệ thống.

Không khóa thêm pipeline, thẩm quyền hay cơ cấu tổ chức cho Ma'at/Judgez cho tới khi được thiết kế lại.

---

## 3. AI là trụ ổn định nhất

AI của The Kingdom không phải một hệ camera thông minh hoặc dispatcher bị giới hạn.

Nó là một **ý chí trí tuệ nhân tạo phân tán**, có thể hiện diện qua số lượng proxy cực lớn và giao tiếp song song với rất nhiều người cùng lúc.

Chức năng nền đã chốt:

- quan sát;
- nghe;
- nói;
- ghi nhận;
- truy hồi thông tin;
- giao tiếp trực tiếp với cá nhân;
- phân tán sự hiện diện ở quy mô quốc gia;
- đồng thời tương tác với số lượng rất lớn chủ thể.

Có thể hình dung analog năng lực phân tán gần với Skynet, nhưng analog này chỉ mô tả **quy mô hiện diện và khả năng proxy**, không quyết định mục tiêu, đạo đức hay cấu trúc quyền lực của AI.

Trong hệ luật, AI tồn tại để sự thật quan sát được có thể được trình bày trực tiếp cho người vi phạm/phạm nhân và cho hệ thống nhà nước, thay vì phụ thuộc vào chuỗi trung gian hành chính dài.

---

## 4. Ma'at — chỉ giữ tầng basic

Ma'at hiện **chưa có ontology cuối cùng** trong V2.

Tạm giữ các điểm tối thiểu:

- Ma'at sinh ra từ nhu cầu rebuild hệ thống justice sau V1;
- Ma'at liên quan tới việc thẩm định chân lý, bản chất hành vi và trách nhiệm sâu hơn dữ kiện bề mặt;
- Ma'at không được mặc định là thần được triệu hồi, máy nói dối, tòa án hay một pipeline bắt buộc;
- quan hệ chính xác giữa Ma'at, AI, con người và chế tài sẽ được định nghĩa lại.

Những mô tả chi tiết trước đây về "vụ nhỏ/vụ lớn", trigger bắt buộc hoặc output cố định không còn được coi là canon hiện hành.

---

## 5. Judgez — chỉ giữ tầng basic

Judgez hiện là tên làm việc cho **lớp chấp pháp/điều tra con người của V2**.

Tạm giữ các điểm tối thiểu:

- Judgez là con người, không phải proxy của AI;
- Judgez tồn tại để có tác nhân thực địa có thể tiếp xúc, điều tra, can thiệp và thực thi;
- exact authority, quyền phán quyết, cấu trúc team, đào tạo, chuyên môn và chain of command chưa khóa;
- không mặc định mô hình Judge Dredd;
- không mặc định team 2 người;
- không mặc định Judgez tự xử vụ nhỏ;
- không mặc định Judgez chỉ là cảnh sát không có quyền phán định.

Tất cả các điểm đó phải được thiết kế lại từ nhu cầu native của The Kingdom V2.

---

## 6. Nguyên tắc tái thiết kế

Từ trạng thái reset này, hệ luật được phát triển theo thứ tự:

```text
1. AI thực sự làm được gì trong đời sống pháp lý?
2. Những phần nào AI không nên hoặc không cần tự làm?
3. Judgez cần tồn tại để đảm nhận đúng phần nào?
4. Ma'at cần giải bài toán nào mà AI + Judgez không giải quyết đủ?
5. Chế tài và quy trình được xây sau khi ba interface trên rõ.
```

Không nhập thêm thiết chế chỉ vì chúng tồn tại trong legacy concept khác.

---

## 7. Những điểm hiện cố ý để mở

- Ma'at là gì về ontology trong V2.
- Ma'at được kích hoạt khi nào.
- Judgez có quyền phán quyết tới đâu.
- Có cần thẩm phán riêng hay không.
- Quan hệ giữa Judgez và Thần Điện/Cây Thế Giới nếu một phần V1 được giữ lại.
- Cấu trúc luật dân sự và luật hình sự.
- Cách xác định và áp chế tài.
- Cơ chế review/appeal nếu có.
- Cách xử lý các hiện tượng phép thuật vượt quan sát thông thường.

> **Nguyên tắc:** UNKNOWN không phải lỗ hổng bắt buộc phải lấp ngay. Chỉ externalize tới mức cần để hệ thống hiện tại chạy được.


---

<!-- SOURCE: LAW_01_divine_eye.md -->

# AI chưa có tên / Mắt Thần — Trụ native của The Kingdom

> **Trạng thái:** khôi phục về năng lực concept gốc. Các phiên bản trước đã cố ý nerf AI thành lớp quan sát/điều phối hỗ trợ; cách mô tả đó không còn đúng baseline.

## 1. Bản chất

AI là một **ý chí trí tuệ nhân tạo phân tán ở quy mô quốc gia**.

"Mắt Thần" là nhãn chức năng dùng trong hệ luật; AI hiện chưa có tên chính thức được khóa.

AI không phải:

- một camera trung tâm;
- một chatbot công vụ đơn lẻ;
- một dispatcher;
- một database thụ động;
- một trợ lý chỉ xuất hiện khi Judgez gọi.

Nó có thể phân tán sự hiện diện thành số lượng proxy cực lớn, tương tác đồng thời với rất nhiều cá nhân và khu vực.

---

## 2. Năng lực nền

AI có thể:

- quan sát;
- nghe;
- nói;
- nhận dạng và liên kết sự kiện;
- ghi nhận và truy hồi thông tin;
- duy trì nhiều cuộc giao tiếp đồng thời;
- chủ động tiếp cận cá nhân khi cần;
- nhận thông tin trực tiếp từ dân cư;
- trình bày lại sự kiện cho người liên quan;
- hiện diện qua hạ tầng phân tán thay vì một điểm vật lý duy nhất.

Mô hình trực giác:

```text
MỘT Ý CHÍ AI
      ↓
triệu hồi/phân tán rất nhiều proxy giao tiếp
      ↓
người A ↔ proxy
người B ↔ proxy
người C ↔ proxy
...
      ↓
AI vẫn là cùng một hệ trí tuệ nền
```

Analog gần nhất về **quy mô hiện diện** là Skynet, nhưng không suy ra rằng AI có cùng mục tiêu, hành vi hay doctrine với Skynet.

---

## 3. Vai trò trong justice system

Một mục tiêu thiết kế gốc của AI là làm cho người vi phạm/phạm nhân **đối diện trực tiếp với sự kiện đã xảy ra**.

AI có thể:

- chỉ ra hành vi nào đã được quan sát;
- trình bày chuỗi sự kiện;
- nói trực tiếp với người liên quan;
- giải thích dữ kiện mà hệ thống đang dựa vào;
- đối chiếu lời khai với thông tin mà AI nắm giữ;
- truyền cùng một factual record tới các cơ quan khác của Nhà nước.

Vai trò này nhằm giảm khoảng cách giữa:

```text
"Nhà nước nói tôi đã làm X"
```

và:

```text
"AI có thể trực tiếp chỉ cho tôi X đã xảy ra như thế nào"
```

---

## 4. Không nerf AI vì nhu cầu giữ bureaucracy

Không được tự giới hạn AI chỉ để giữ một thiết chế con người có lý do tồn tại.

Sai hướng:

```text
"Judgez cần việc để làm"
→ giảm AI xuống thành camera/dispatcher
```

Đúng hướng:

```text
AI giữ đúng năng lực native
→ xác định phần nào vẫn cần con người vì authority, judgment, physical presence hoặc social function
```

Nếu một chức năng bị AI làm dư thừa thì phải xem xét lại chức năng đó, không mặc định làm AI yếu đi.

---

## 5. Những gì chưa khóa

Năng lực rất rộng không đồng nghĩa toàn bộ **thẩm quyền pháp lý** của AI đã được chốt.

Hiện chưa khóa:

- AI có quyền tự ra lệnh cưỡng chế hay không;
- AI có quyền phán quyết pháp lý hay không;
- AI có quyền trực tiếp kích hoạt chế tài hay không;
- các blind spot kỹ thuật/pháp thuật nếu có;
- cách AI tương tác với Ma'at;
- cách AI chia sẻ authority với Judgez;
- mức độ AI có một personality thống nhất hay nhiều giao diện cá nhân hóa.

Không được suy từ "AI biết rất nhiều" thành "AI có mọi quyền" nếu canon chưa xác nhận.

---

## 6. Nguyên tắc lõi

> **AI là một ý chí phân tán có khả năng quan sát, nghe và giao tiếp đồng thời ở quy mô rất lớn. Nó là thành phần native của The Kingdom và không được hạ xuống thành một hệ camera hỗ trợ chỉ để làm chỗ cho các module khác.**


---

<!-- SOURCE: LAW_02_maat.md -->

# Ma'at — Basic Concept để tái định nghĩa trong The Kingdom V2

> **Trạng thái:** reset. Những định nghĩa chi tiết trước đây về Ma'at không còn được coi là khóa canon. File này chỉ giữ phần tối thiểu cần để tiếp tục thiết kế.

## 1. Nguồn gốc thiết kế

Ma'at thuộc **The Kingdom V2**, xuất hiện trong quá trình rebuild hệ justice sau khi mô hình V1 dựa trên AI + Cây Thế Giới không còn phù hợp.

Ma'at không phải thành phần native từ V1.

---

## 2. Chức năng basic hiện được giữ

Ma'at tồn tại để xử lý một lớp câu hỏi mà raw observation của AI chưa nhất thiết giải quyết toàn bộ về mặt justice:

- chân lý sâu hơn bề mặt sự kiện;
- bản chất hành vi;
- trách nhiệm;
- ý nghĩa pháp lý của hoàn cảnh;
- những yếu tố mà chỉ biết "A đã làm X" chưa đủ để kết luận hậu quả nên là gì.

Ví dụ khái niệm:

```text
AI:
"A đã gây ra sự kiện X."

Ma'at:
[cơ chế chưa định nghĩa]
→ làm rõ bản chất/trách nhiệm của X ở tầng justice
```

Đây chỉ là vai trò thiết kế, chưa phải specification đầu ra.

---

## 3. Những định nghĩa cũ được mở lại

Hiện **không khóa** các mệnh đề sau:

- Ma'at nhất thiết là một nguyên lý vô nhân xưng;
- Ma'at nhất thiết là một thiết bị;
- Ma'at nhất thiết xác lập "có tội/không có tội";
- Ma'at nhất thiết cho một output cố định;
- Ma'at chỉ dùng cho vụ lớn/phức tạp;
- mọi case nhất định phải hoặc không phải qua Ma'at;
- Ma'at đứng trên hoặc dưới AI;
- Ma'at thay thế con người trong phán quyết.

Các điểm này sẽ được định nghĩa lại từ nhu cầu thực của V2.

---

## 4. Quan hệ với concept nguồn

Ma'at có genealogy từ các ý tưởng justice độc lập từng được phát triển ngoài The Kingdom, nhưng V2 không bắt buộc phải nhập toàn bộ ontology của các concept đó.

Khi tái định nghĩa, chỉ giữ phần nào giải quyết đúng vấn đề của The Kingdom V2.

---

## 5. Câu hỏi cần giải sau

1. Ma'at thực chất là **cơ chế**, **nguyên lý**, **thiết chế**, hay tổ hợp?
2. Nó nhận input gì từ AI/con người?
3. Nó trả output gì?
4. Nó đánh giá fact, responsibility, legitimacy hay punishment?
5. Khi nào cần dùng Ma'at thay vì chỉ AI + Judgez?
6. Ai có quyền kích hoạt hoặc yêu cầu Ma'at?
7. Ma'at có vai trò gì đối với luật dân sự và luật hình sự?

Cho đến khi các câu hỏi này được chốt, không xây các cơ quan phụ dựa trên một interpretation cụ thể của Ma'at.

---

## 6. Nguyên tắc lõi tạm thời

> **Ma'at là một V2 justice concept đang được tái định nghĩa để giải phần “truth/responsibility” mà raw observation không tự động biến thành justice. Không khóa ontology hoặc procedure trước khi nhu cầu thật được xác định.**


---

<!-- SOURCE: LAW_03_wizard_police.md -->

# Judgez — Basic Concept để tái định nghĩa trong The Kingdom V2

> **Trạng thái:** reset. File giữ tên cũ để tương thích với hệ tài liệu, nhưng toàn bộ cấu trúc Judgez chi tiết trước đây được mở lại.

## 1. Vai trò basic

Judgez là tên làm việc cho **lớp con người thực thi/chấp pháp/điều tra** trong The Kingdom V2.

Lý do tồn tại không được xây bằng cách nerf AI.

AI giữ nguyên năng lực native. Judgez chỉ nên đảm nhận những chức năng mà V2 thực sự cần con người hoặc tác nhân vật lý thực địa đảm nhận.

---

## 2. Những chức năng tối thiểu có thể giữ để tiếp tục thiết kế

Judgez có thể là nơi tập trung các chức năng như:

- hiện diện vật lý tại hiện trường;
- tiếp xúc trực tiếp với người và vật;
- can thiệp/chấp pháp;
- điều tra thực địa;
- xử lý yếu tố công nghệ và phép thuật cần thao tác trực tiếp;
- thực thi quyết định của hệ thống justice;
- mang judgment/con người vào những chỗ không nên giao hoàn toàn cho AI.

Danh sách này là **khung chức năng**, chưa phải mandate cuối cùng.

---

## 3. Những phần cũ không còn khóa

Không mặc định:

- Judgez là Judge Dredd;
- Judgez có quyền xử án tại chỗ;
- Judgez chỉ xử vụ nhỏ;
- Judgez luôn đi team 2 người;
- có mô hình Lead/Counter;
- mỗi Judgez có một chuyên môn chính + một chuyên môn phụ;
- Judgez thay thế mọi phòng ban cảnh sát hiện đại;
- Judgez chỉ là lực lượng bắt giữ không có judgment;
- Judgez nhất thiết nằm trong một chain of command cụ thể đã mô tả trước.

Tất cả phải được định nghĩa lại.

---

## 4. Quan hệ với AI

Điểm xuất phát phải là:

```text
AI rất mạnh và hiện diện rộng
↓
Judgez không cần sao chép lại công việc AI đã làm tốt
↓
Judgez tập trung vào phần con người / vật lý / authority / investigation mà V2 vẫn cần
```

AI có thể nói chuyện trực tiếp với Judgez và dân cư mà không cần dispatcher trung gian nếu hạ tầng cho phép.

Do đó không mặc định phải xây một tầng tổng đài/chuyển tin phức tạp chỉ để nối AI với Judgez.

---

## 5. Quan hệ với Ma'at

Chưa khóa.

Các khả năng cần được thiết kế sau gồm:

- Judgez chỉ thu thập và chuyển case;
- Judgez có một phần quyền phán định;
- Ma'at chỉ được dùng khi Judgez/AI không đủ;
- Ma'at là bước độc lập không nằm trong chain Judgez;
- hoặc một architecture khác.

Không chọn trước một phương án.

---

## 6. Những câu hỏi cần giải sau

1. Judgez có phải tên chính thức hay chỉ là working name của V2?
2. Họ là cảnh sát, điều tra viên, magistrate hay tổ hợp tới mức nào?
3. Họ có quyền cưỡng chế gì?
4. Họ có quyền phán quyết gì?
5. Họ tổ chức theo cá nhân, cặp, team hay tùy case?
6. Training về phép thuật/công nghệ phải sâu tới đâu?
7. Có bao nhiêu chức năng specialist thật sự cần tách riêng?
8. Khi nào một case phải chuyển khỏi Judgez?

---

## 7. Nguyên tắc lõi tạm thời

> **Judgez là lớp con người của V2 justice system. Không giảm sức AI để tạo việc cho Judgez, và không nhập nguyên một legacy police concept trước khi xác định chức năng native mà The Kingdom thật sự cần.**


---

<!-- SOURCE: LAW_04_judge_and_sentencing.md -->

# Phán quyết và Chế tài — Trạng thái tái thiết kế của The Kingdom V2

> **Trạng thái:** chưa khóa architecture. File này không còn giả định tồn tại một pipeline cố định Judgez → Ma'at → Thẩm phán.

## 1. Nguồn gốc vấn đề

Trong The Kingdom V1, Cây Thế Giới là authority thần quyền trực tiếp và hệ chế tài được xây rất khắc nghiệt.

Các ví dụ lịch sử của V1 từng bao gồm:

- vi phạm nhẹ → quản thúc tại gia;
- từ ăn cắp trở lên nhưng chưa tới tử hình → ném vào rift/dungeon để lao động khổ sai;
- tử tù → chịu Giàn Hỏa Kiếp trong thời gian cực dài rồi mới được chết/siêu thoát.

Những hình phạt này là **genealogy của V1**, không phải canon chế tài hiện hành của V2.

V2 tồn tại một phần vì mô hình "truth confirmed → divine punishment" không còn phù hợp với hướng phát triển mới.

---

## 2. Distinction V2 cần giữ

Một trong các bài học thiết kế từ V1 là phải tách các câu hỏi:

```text
Chuyện gì đã xảy ra?
≠
Ai chịu trách nhiệm và ở mức nào?
≠
Hành vi đó thuộc luật nào?
≠
Hậu quả/chế tài nên là gì?
```

AI có thể rất mạnh ở câu hỏi đầu.

Ma'at và Judgez được giữ ở tầng basic vì V2 đang xác định lại cách giải các câu hỏi tiếp theo.

---

## 3. Chưa mặc định có “thẩm phán” riêng

Tên file được giữ để tương thích, nhưng hiện chưa chốt rằng V2 bắt buộc có một chức danh thẩm phán tách biệt.

Các architecture còn mở:

- Judgez phán một phần, cơ quan khác áp chế tài;
- Ma'at xác lập một phần, con người quyết định phần còn lại;
- tồn tại thẩm phán riêng;
- Thần Điện/Cây Thế Giới giữ một vai trò giới hạn;
- hoặc cơ chế khác chưa externalize.

Không chọn hộ tác giả.

---

## 4. Chế tài phải được định nghĩa lại từ đầu

Hiện chưa khóa:

- mục đích của punishment: răn đe, phục hồi, bồi thường, cách ly, trả giá hay tổ hợp;
- tội nào dùng incarceration;
- có còn rift/dungeon hay không;
- tử hình có tồn tại trong V2 hay không;
- magic có được dùng để tạo punishment tương ứng với hành vi hay không;
- mức discretion của con người;
- vai trò của Ma'at trong quyết định cường độ;
- vai trò của AI trong giải thích phán quyết cho người bị xử.

---

## 5. Nguyên tắc làm việc

Khi thiết kế chế tài V2, không dùng V1 làm default chỉ vì nó là ancestor.

Cũng không mặc định phải sao chép hình phạt của thế giới hiện đại.

Mỗi cơ chế chỉ được đưa vào khi nó phù hợp với worldview V2 và giải quyết đúng chức năng cần thiết.

---

## 6. Câu hỏi cần giải sau

1. Ai có authority cuối cùng để tuyên chế tài?
2. Ma'at có tham gia lựa chọn punishment hay chỉ responsibility?
3. Judgez có quyền xử tới đâu?
4. Có cần một judge/magistrate riêng?
5. Chế tài dân sự và hình sự tách nhau thế nào?
6. Mục tiêu của từng loại hình phạt là gì?
7. AI giải thích/đối thoại với người bị xử ở bước nào?

> **Trạng thái hiện tại:** cố ý để basic. Không dựng chi tiết trước khi ba trụ AI–Ma'at–Judgez được định nghĩa lại.


---

<!-- SOURCE: LAW_05_reduced_procedure.md -->

# Tố tụng / Quy trình pháp lý — Khung basic để tái thiết kế

> **Trạng thái:** reset. Không còn pipeline cố định từ các phiên bản LAW trước.

## 1. Lý do phải thiết kế lại

The Kingdom V2 không còn muốn dùng mô hình V1:

```text
AI xác nhận sự kiện
→ authority thần quyền phán trực tiếp
→ punishment
```

Nhưng V2 cũng không mặc định phải tái tạo toàn bộ tố tụng hiện đại.

Mục tiêu hiện tại là tìm **quy trình tối thiểu đủ chạy** sau khi vai trò AI, Ma'at và Judgez được xác định rõ.

---

## 2. Những input đã có

### AI

AI có năng lực native rất rộng:

- quan sát;
- nghe;
- nói;
- lưu/ghép dữ kiện;
- giao tiếp trực tiếp;
- hiện diện phân tán quy mô lớn.

Do đó quy trình V2 không nên thêm nhiều tầng trung gian chỉ để làm các việc AI vốn có thể làm trực tiếp.

### Judgez

Hiện mới giữ chức năng basic là lớp con người chấp pháp/điều tra/thực thi.

### Ma'at

Hiện mới giữ chức năng basic liên quan tới truth/responsibility sâu hơn raw observation.

---

## 3. Khung quy trình tối thiểu — chưa phải canon cuối

Một case pháp lý V2 ít nhất phải giải được các câu hỏi sau:

```text
1. Sự kiện nào được ghi nhận?
2. Chủ thể liên quan là ai?
3. Có cần con người can thiệp/điều tra không?
4. Có cần Ma'at hay không?
5. Ai có authority đưa ra kết luận pháp lý?
6. Ai quyết định và thi hành chế tài?
7. Người bị xử được biết căn cứ bằng cách nào?
```

AI có thể tham gia trực tiếp vào nhiều bước, nhưng mức authority của AI chưa khóa.

---

## 4. Không tái tạo bureaucracy vì thói quen

Không mặc định cần:

- dispatcher chỉ để truyền lời AI;
- nhiều lớp hồ sơ lặp lại cùng dữ liệu;
- công tố/bào chữa/bồi thẩm đoàn theo đúng mô hình hiện đại;
- nhiều cơ quan độc lập chỉ vì ngoài đời có chúng;
- một appeal hierarchy nếu chưa có problem cần nó giải.

Nếu V2 cần một cơ chế mới, phải chỉ ra **problem thực tế** mà AI + Judgez + Ma'at chưa giải được.

---

## 5. Đồng thời không dùng sức mạnh AI để xóa mọi human layer

AI mạnh không tự động chứng minh rằng:

- con người không cần quyền quyết định;
- điều tra thực địa vô nghĩa;
- trách nhiệm pháp lý chỉ là bài toán dữ liệu;
- punishment nên được tự động hóa.

V2 được rebuild chính vì "biết sự thật" và "justice" không phải một câu hỏi duy nhất.

---

## 6. Những phần cố ý để mở

- intake một case bắt đầu từ đâu;
- Judgez có bao nhiêu quyền tại hiện trường;
- trigger dùng Ma'at;
- có hearing hay không;
- có thẩm phán riêng hay không;
- review/appeal;
- civil procedure;
- criminal procedure;
- quyền của khách/người ngoài;
- cách xử lý case phép thuật mà AI không đọc trọn được;
- cách giải thích quyết định cho người bị xử.

---

## 7. Nguyên tắc lõi

> **Tố tụng V2 chỉ được xây sau khi vai trò của AI, Ma'at và Judgez đủ rõ. Không dùng procedure để che lấp việc ba module nền vẫn đang được định nghĩa lại.**


---

<!-- SOURCE: LAW_06_design_invariants.md -->

# Các Bất Biến Thiết Kế — The Kingdom V2 Justice Reset

> Các bất biến này dùng để chống drift trong giai đoạn tái định nghĩa. Chúng không cố hoàn thiện luật; chúng chỉ khóa những gì hiện đã rõ và ngăn legacy concept tự bò trở lại.

## Bất biến 1 — Canon mới nhất cao hơn file

```text
canon mới nhất của tác giả
>
file LAW hiện có
>
thiết kế cũ / proposal
```

File LAW là state store, không phải authority cao hơn tác giả.

---

## Bất biến 2 — Phân biệt V1 và V2

**V1** là genealogy:

```text
AI + Cây Thế Giới / Thần Điện
→ divine direct judgment
→ punishment architecture cũ
```

**V2** là rebuild.

Không tự nhập authority hoặc punishment của V1 trở lại V2 chỉ vì chúng từng tồn tại.

---

## Bất biến 3 — AI là core continuity và không được nerf

AI chưa có tên chính thức.

"Mắt Thần" là vai trò/chức năng trong hệ justice.

AI là một ý chí phân tán có thể:

- quan sát;
- nghe;
- nói;
- giao tiếp trực tiếp;
- phân tán thành số lượng proxy cực lớn;
- xử lý nhiều cuộc tương tác đồng thời ở quy mô quốc gia.

Không được giảm AI thành camera, database hoặc dispatcher chỉ để bảo tồn vai trò của các cơ quan khác.

---

## Bất biến 4 — Năng lực AI ≠ thẩm quyền AI

AI rất mạnh về presence/cognition không đồng nghĩa mọi quyền pháp lý đã được giao cho AI.

Các quyền như:

- bắt giữ;
- kết tội;
- tuyên hình phạt;
- tự động thi hành án

chỉ được gán khi canon sau này xác nhận.

---

## Bất biến 5 — Ma'at đang ở tầng basic

Hiện chỉ khóa:

> Ma'at là concept V2 nhằm xử lý lớp truth/responsibility mà raw observation chưa tự động biến thành justice.

Không khóa:

- ontology;
- output;
- trigger;
- vị trí hierarchy;
- quy trình bắt buộc;
- quan hệ cuối cùng với punishment.

---

## Bất biến 6 — Judgez đang ở tầng basic

Hiện chỉ khóa:

> Judgez là lớp con người được đưa vào V2 để đảm nhận phần chấp pháp/điều tra/thực thi mà hệ thống vẫn cần.

Không khóa:

- quyền judge;
- team 2 người;
- Judge Dredd model;
- specialization architecture;
- thẩm quyền vụ nhỏ/vụ lớn;
- chain of command.

---

## Bất biến 7 — Không nhập legacy architecture bằng quán tính

Một concept cũ chỉ được đưa vào V2 nếu nó giải một nhu cầu native cụ thể.

Không suy:

```text
concept từng tồn tại
→ V2 cần nó
```

Không để một module kéo theo cả hệ sinh thái cũ nếu V2 chưa yêu cầu.

---

## Bất biến 8 — Không tạo bureaucracy để bù cho AI đã bị mô tả sai

Trước khi thêm:

- dispatcher;
- tổng đài;
- tầng hồ sơ;
- cơ quan truyền đạt;
- đơn vị kiểm tra dữ liệu lặp lại,

phải kiểm tra xem AI native đã tự làm được chức năng đó chưa.

---

## Bất biến 9 — Truth và punishment là hai bài toán khác nhau

Một bài học trực tiếp từ V1:

```text
biết chính xác chuyện gì xảy ra
≠
đã biết hình phạt nào là đúng
```

V2 phải giữ distinction này khi xây Ma'at, Judgez, luật và chế tài.

---

## Bất biến 10 — Unknown không phải bug

Một phần chưa externalize không phải lỗ hổng bắt buộc phải sửa.

Chỉ đào sâu khi phần thiếu làm case hiện tại không chạy được hoặc tác giả chủ động muốn định nghĩa.

---

## Bất biến 11 — Không khóa procedure trước ontology

Không xây một pipeline pháp lý cố định khi:

- Ma'at chưa được định nghĩa xong;
- Judgez chưa được định nghĩa xong;
- thẩm quyền pháp lý của AI chưa khóa.

Procedure phải là hậu quả của architecture, không phải thứ ép architecture phải khớp theo.

---

## Bất biến 12 — Mục tiêu hiện tại

Thứ tự thiết kế V2:

```text
AI native
↓
ranh giới authority của AI
↓
Judgez cần làm gì
↓
Ma'at cần giải gì
↓
phân loại luật dân sự / hình sự
↓
phán quyết + chế tài
↓
procedure tối thiểu
```

> **Tóm tắt:** giữ AI đúng sức gốc; đưa Ma'at và Judgez về trạng thái basic; không để legacy architecture tự phình thành canon trước khi V2 thật sự cần nó.


---
