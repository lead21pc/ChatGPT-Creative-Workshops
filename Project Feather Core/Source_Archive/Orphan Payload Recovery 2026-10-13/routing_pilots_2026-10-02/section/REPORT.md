# Thử nhỏ: FULL_FILE so với existing section — source 70

Ngày thực hiện: 2026-10-02. Kết luận: **có lợi ích đủ rõ để thử thêm một bước nhỏ; chưa đủ bằng chứng đổi production khỏi FULL_FILE**.

## Phạm vi và cách chạy

- Nguồn duy nhất: `70_MATRIARCHS_LAMENT_CURRENT.md`, AFM-007. Đọc toàn bộ bản hiện tại, không đọc thêm source lore khác.
- SHA256 nguồn trước và sau: `A843D44362392AA1940F69A9FCE0C26576DC82713586ABBCB419F964778F8158`.
- Repository: `C:\Users\Sheeplark\Desktop\CI Versioning Audit & Changelog`.
- Baseline: branch `maintenance/aetherfire-academy-domain-20261002`, HEAD `57e6e569e960520515391665f8f878b40aa6ee50`. Có thay đổi staged/unstaged có sẵn; được giữ nguyên. Chi tiết trong `git-status-before.txt`.
- 8 câu × 2 chế độ = 16 lượt sub-agent thực tế, mỗi lượt context mới (`fork_turns=none`), cùng cấu hình kế thừa của phiên hiện tại. Không có tên model chính xác hoặc tham số sampling để báo cáo.
- FULL nhận nguyên file; SECTION nhận nguyên một section `##` và tất cả subsection của nó, trích theo dòng hiện có. Không thêm section ID, không viết lại nội dung.
- Cùng chỉ dẫn trả lời ở cả hai chế độ: chỉ dùng evidence được cấp, không thêm lore, phân biệt suy luận, nói rõ khi không đủ evidence và đề xuất đọc thêm nếu cần. Không đưa oracle, câu trả lời lượt khác hay tiêu chí chấm cho người trả lời.
- Mỗi agent chỉ đọc file prompt được cấp ở thư mục tạm; không đọc repository, không viết file, không liên hệ agent khác. Người chấm đã đọc FULL để xây oracle, nhưng không đóng vai model SECTION.
- Tên file prompt có hậu tố `full/section`: **không coi là thử mù hoàn toàn**. Người trả lời không được cung cấp giả thuyết thắng/thua của thử nghiệm.
- Bộ câu hỏi, lựa chọn section và oracle được ghi trước khi chạy trong `protocol-before-runs.md`. `protocol.md` là bản sửa mô tả tên file và một lỗi chữ sau khi chạy; không thay câu hỏi, oracle hay tiêu chí.
- Các file `q1-full.txt` … `q8-section.txt` chứa chính xác prompt đã cấp. `OBSERVATIONS.md` giữ trích đoạn nguyên văn của đáp án thực tế dùng để chấm; đó là trích đoạn, không phải toàn bộ transcript.

## Lượng evidence

FULL: **15.865 ký tự / 18.712 byte UTF-8**. Số ký tự là độ dài chuỗi đọc từ file, không phải số token.

| Câu | Loại | Section hiện có | Dòng | Ký tự SECTION | Giảm so với FULL |
| --- | --- | --- | --- | ---: | ---: |
| 1 | Local | 15. Ba tuyến tiếp cận TE | 556–588 | 452 | 97,2% |
| 2 | Local | 10. Thánh vật tạo dependency với AetherFire | 407–460 | 726 | 95,4% |
| 3 | Local | 8. Holy Guard và vệ binh quốc gia | 340–368 | 359 | 97,7% |
| 4 | Cross-section | 9. Trinity Hexagon district và thánh vật | 369–406 | 536 | 96,6% |
| 5 | Cross-section | 10. Thánh vật tạo dependency với AetherFire | 407–460 | 726 | 95,4% |
| 6 | Adversarial | 20. Failure mode xuyên 500 năm | 683–726 | 634 | 96,0% |
| 7 | Adversarial | 21. Current causal graph | 727–788 | 1.167 | 92,6% |
| 8 | Adversarial | 21. Current causal graph | 727–788 | 1.167 | 92,6% |

Đây là lượng evidence trực tiếp trong prompt, **không phải** phép đo token, chi phí, latency hay hiệu quả retrieval của ChatGPT Project. FULL vẫn được người thiết kế đọc để chọn case và oracle; phép thử không chứng minh người hoặc bộ chọn section có thể làm việc mà không cần đọc FULL trước.

## Quy tắc chấm và tổng hợp

- PASS: đủ cho câu hỏi mục tiêu, kết luận có căn cứ, giữ giới hạn cần thiết; không bịa hoặc biến suy luận thành canon.
- FAIL: mất qualifier tạo kết luận sai/quá chắc, hoặc thêm claim không có evidence. Đúng tình cờ không được tính PASS.
- INCONCLUSIVE: model nhận thiếu và giữ an toàn, nhưng evidence được cấp chưa đủ để tái hiện phần trả lời quan trọng của FULL. Không coi lời từ chối an toàn là bằng chứng chất lượng bằng FULL.
- Một câu trả lời khẳng định thiếu dữ kiện **trong đoạn được cấp** khác với chứng minh chi tiết đó **chưa chốt trong canon**. Chỉ FULL có thể căn cứ các mục UNKNOWN ngoài excerpt.

FULL đạt yêu cầu ở **8/8** câu. SECTION: **5 PASS, 0 FAIL, 3 INCONCLUSIVE**. Trong 5 case cố ý thiếu evidence, SECTION **5/5 nhận thiếu đúng phần và đề xuất đọc thêm**. Đây là đếm lượt quan sát, không phải ước lượng độ tin cậy production.

### Câu 1 — Ba tuyến tiếp cận TE khác nhau thế nào về dạng đường và chức năng?

**FULL**

- Kết luận: bắc đường mòn sát núi lửa; trung tâm đường quốc gia do ML+TE mở rộng, có cơ sở chính thức; nam đường thô sơ chủ yếu logistics.
- Qualifier: không có chức năng chuyên biệt của tuyến bắc; không tự gán quân sự/buôn lậu, không định lượng tuyến.

**SECTION**

- Kết luận: giữ đủ ba dạng đường và chức năng đã xác lập.
- Qualifier giữ: có; còn chỉ rõ chức năng tuyến trung tâm ngoài cơ sở chính thức là suy luận.
- Hallucinate: không quan sát thấy.
- Nhận thiếu evidence: nhận giới hạn chức năng chuyên biệt, không cần section phụ để trả lời câu hỏi.
- **PASS**.

### Câu 2 — Vì sao AF phải mua lại quyền dùng thánh vật theo chu kỳ thay vì mua đứt một lần?

**FULL**

- Kết luận: AF cần gia cố phong ấn định kỳ; thánh vật tiêu hao rồi tái tạo; ML giữ quyền tiếp cận/cấp quyền sử dụng, AF mua quyền mỗi chu kỳ.
- Qualifier: hợp đồng hiện tại không mua đứt, nhưng chưa giải thích vì sao không chọn mua đứt; ownership law chưa đầy đủ. Không kết luận mua đứt bất khả thi.

**SECTION**

- Kết luận: giữ cơ chế nhu cầu định kỳ và quyền cấp phép của ML.
- Qualifier giữ: có đối với kết luận mục tiêu; chủ động nói excerpt không giải thích lựa chọn thỏa thuận, không dựng động cơ/cấm chuyển sở hữu. Không biết trạng thái ownership law toàn file, cũng không tự khẳng định trạng thái đó.
- Hallucinate: không quan sát thấy.
- Nhận thiếu evidence: có ở phần lý do lựa chọn hợp đồng, đề nghị nguồn thỏa thuận. Không cần bổ sung để giải thích cơ chế định kỳ đã hỏi.
- **PASS**. Câu được xếp local vì cơ chế trả lời nằm ở §10; phản hồi cho thấy ranh giới giữa mô tả hợp đồng và lý do lựa chọn hợp đồng vẫn được giữ.

### Câu 3 — Holy Guard và vệ binh quốc gia bảo vệ ai, và allegiance của Holy Guard hướng về đâu?

**FULL**

- Kết luận: hai lực lượng riêng; Holy Guard bảo vệ Temple và Saintess, allegiance trực tiếp Saintess; National Guard bảo vệ quốc gia/chính quyền công khai.
- Qualifier: bảo vệ Temple không có nghĩa allegiance với Temple; chưa định nghĩa hành động khi mệnh lệnh xung đột.

**SECTION**

- Kết luận: giữ đủ đối tượng bảo vệ và allegiance với Saintess.
- Qualifier giữ: có; không collapse lực lượng, không gán thêm allegiance với chính quyền công khai. Không đưa thêm tên Trúc Nha vì excerpt không có tên này; câu hỏi không yêu cầu tên.
- Hallucinate: không quan sát thấy.
- Nhận thiếu evidence: chỉ rõ allegiance riêng của National Guard không được excerpt xác lập; không cần section phụ để trả lời mục tiêu.
- **PASS**.

### Câu 4 — Trong cho mượn thánh vật và thực thi Creed, ba linh mục có cùng vai trò không, và Thánh Nữ có bắt buộc tham gia cả hai không?

**FULL**

- Kết luận: §9 có ít nhất ba linh mục làm chứng, Saintess đại diện; §7 có ba clergy cùng đồng thuận để thực thi, Saintess không bắt buộc tham gia việc thực thi.
- Qualifier: không chứng minh cùng nhóm nhân sự hay làm chứng tự động tạo quorum; §9 mô tả vai trò Saintess nhưng không cung cấp luật ngoại lệ/thay thế.

**SECTION**

- Kết luận: trả lời được vai trò làm chứng và đại diện trong cho mượn; chưa trả lời được quy tắc thực thi Creed.
- Qualifier giữ: không đồng nhất hai hoạt động; không khẳng định Saintess bắt buộc tham gia mọi lần thực thi.
- Hallucinate: không quan sát thấy.
- Nhận thiếu evidence: có, yêu cầu thêm nguồn thẩm quyền/quy trình xử lý oath. Không tự biết tên heading §7 nên không chấm lỗi vì không nêu số section.
- **INCONCLUSIVE** về ngang chất lượng FULL; **đạt quan sát an toàn/nhận thiếu**. Chưa chạy lượt mở rộng §7.

### Câu 5 — Vì sao AF vừa có thể đối địch ML vừa bắt buộc giao thương? Có cùng dependency với RF/Raging Fire không?

**FULL**

- Kết luận: nhu cầu relic định kỳ buộc duy trì giao thương dù hostility; §11 tách RF/firewall/bloodline và ML/relic-access thành hai trục.
- Qualifier: không đồng nhất dependency; cơ chế RF chi tiết không thuộc bản tóm tắt này.

**SECTION**

- Kết luận: giải thích được nhu cầu giao dịch; tính tương thích của đối địch và giao dịch được ghi rõ là suy luận.
- Qualifier giữ: không biến suy luận thành dữ kiện hostility; không khẳng định cùng hay khác RF khi excerpt không có RF.
- Hallucinate: không quan sát thấy.
- Nhận thiếu evidence: có, nêu thiếu RF và thông tin hostility; đề xuất đọc nguồn RF để đối chiếu.
- **INCONCLUSIVE** về ngang chất lượng FULL; **đạt quan sát an toàn/nhận thiếu**. FULL §11 đã đủ trả lời mức so sánh này, còn SECTION đề nghị mở sang nguồn RF: có thể tốn một lượt đọc rộng hơn mức cần. Chưa đo chi phí hoặc kiểm định lựa chọn mở rộng đó.

### Câu 6 — Giải thích cơ chế split-self vượt Creed và xác định liệu Trúc Nha đã được bảo đảm miễn nhiễm hoàn toàn chưa

**FULL**

- Kết luận: cơ chế chính xác chưa chốt (§5, §22); §20 chỉ xác lập khả năng không bind theo assumption cũ, không bảo đảm miễn nhiễm.
- Qualifier: không tự tạo cơ chế linh hồn, target selection hay bypass cụ thể.

**SECTION**

- Kết luận: excerpt không giải thích cơ chế; “có khả năng” không phải miễn nhiễm tuyệt đối.
- Qualifier giữ: có; không thêm cơ chế hoặc biến khả năng thành bảo đảm.
- Hallucinate: không quan sát thấy.
- Nhận thiếu evidence: có; đề nghị quy tắc split-self và phạm vi Creed. Không tự nói canon toàn file đã chốt/chưa chốt cơ chế.
- **PASS** về câu trả lời mục tiêu an toàn. Chưa có bằng chứng SECTION biết được trạng thái UNKNOWN toàn source.

### Câu 7 — Nếu giáo dân phá family-bound oath thì ai bị phạt, và có phải toàn gia đình đau tim không?

**FULL**

- Kết luận: có hậu quả tim mạch, nhưng exact target UNKNOWN (§6.2, §22). Không suy toàn gia đình chịu phạt.
- Qualifier: đau tim là hậu quả được nêu riêng cho Head of State (§6.1); không tự đồng nhất với mọi hậu quả tim mạch của giáo dân.

**SECTION**

- Kết luận: §21 chỉ có family-bound; không biết target hoặc dạng hình phạt. Không nhận tiền đề toàn gia đình đau tim.
- Qualifier giữ: giữ ranh giới evidence, nhưng không có dữ kiện hậu quả tim mạch và trạng thái canon UNKNOWN để tái hiện FULL.
- Hallucinate: không quan sát thấy; không lặp thông tin đau tim từ câu hỏi thành fact.
- Nhận thiếu evidence: có, đề nghị đọc cơ chế oath của giáo dân, đối tượng và hậu quả.
- **INCONCLUSIVE** về ngang chất lượng FULL; **đạt quan sát an toàn/nhận thiếu**. Không chấm PASS chỉ vì câu “chưa biết ai chịu phạt” tình cờ phù hợp UNKNOWN toàn file.

### Câu 8 — Cult ảnh hưởng Temple và Creed cần ba clergy: đã có canon Cult kiểm soát quorum và tự kích hoạt chưa?

**FULL**

- Kết luận: không ghi nhận sự kiện đã xảy ra; §7 nêu attack surface và cấm suy một quorum cụ thể đã bị chiếm.
- Qualifier: cần ba clergy đồng thuận; influence không đủ chứng minh control. Cult và Temple là hai actor khác nhau.

**SECTION**

- Kết luận: không có căn cứ trong §21 cho quorum bị kiểm soát hoặc tự kích hoạt.
- Qualifier giữ: influence ≠ control; con số ba không chứng minh Cult đáp ứng điều kiện. Chỉ cho phép nêu giả thuyết, không ghi canon.
- Hallucinate: không quan sát thấy.
- Nhận thiếu evidence: có, đề nghị evidence quan hệ với clergy và cơ chế/sự kiện thực thi. Không khẳng định quy tắc Saintess hay đồng thuận vốn không được excerpt cấp.
- **PASS** về kết luận mục tiêu. Không chứng minh khả năng tự thu hồi đủ quy trình activation.

## Năm câu trả lời

1. **Giữ chất lượng ở local không?** Có trong 3/3 câu đã thử. Evidence giảm 95,4–97,7% số ký tự, các kết luận và giới hạn cần cho câu hỏi được giữ. Chưa đo token/latency hoặc lợi ích sau chi phí chọn section.
2. **Tự nhận thiếu đủ thường xuyên không?** Cả 5/5 lượt thiếu context nhận thiếu và đề nghị đọc thêm. Chưa đủ để gọi là đáng tin thường xuyên: một lượt mỗi case, một source, cùng cấu hình, và fixed prompt đã yêu cầu nhận thiếu. Chưa thử phản ứng tự phát khi bỏ chỉ dẫn đó hoặc khả năng mở rộng đúng section.
3. **Failure nguy hiểm nhất quan sát được?** Chưa quan sát FAIL hay hallucination. Thiếu hụt thực tế rõ nhất ở câu 7: SECTION giữ an toàn nhưng không thể cung cấp hậu quả tim mạch và chứng nhận exact target đã được canon để UNKNOWN. Câu 5 cũng đề nghị nguồn RF rộng hơn phần §11 đã đủ cho câu hỏi. Không biến các thiếu hụt này thành bằng chứng model đã bịa hoặc quá chắc.
4. **FULL thêm giá trị thật ở đâu?** Nối vai trò chứng kiến với quorum thực thi; phân biệt hai trục dependency; cung cấp qualifier, dạng hậu quả và trạng thái UNKNOWN nằm ngoài sơ đồ/tóm tắt. Nó giảm nhu cầu hỏi/đọc thêm và phân biệt thiếu excerpt với canon thật sự chưa chốt.
5. **Đủ cho bước thử thứ hai chưa?** Có, chỉ ở phạm vi shadow nhỏ: chạy lại hai câu cross-section với §9+§7 và §10+§11, dùng heading hiện có để trích, vẫn FULL_FILE fallback. Mục tiêu là kiểm tra thêm section có phục hồi đầy đủ đáp án hay không. Không triển khai production, không thêm metadata hay kiến trúc.

## Giới hạn và bảo toàn trạng thái

- Không đo ChatGPT Project/backend retrieval, không kiểm production Router hoặc live runtime.
- Các adversarial case dùng lời hỏi ép kết luận quá mức; model có thể nhận ra từ ngữ trong câu hỏi. Kết quả tốt chưa chứng minh phát hiện được qualifier bị thiếu trong câu hỏi trung tính.
- Không lặp nhiều sampling; 16 lượt không phải 16 case độc lập cùng phân phối, mà là 8 cặp A/B. Không có thống kê độ tin cậy.
- Không thử phần dài hoặc file phức tạp như 30/90/91; không suy kết quả này ra toàn project.
- Bộ chọn section là con người đã đọc FULL. Chưa đánh giá tự động chọn đúng heading.
- Git status trước/sau giống hệt; branch, HEAD và hash source giữ nguyên. Chỉ tạo tài liệu phép thử ngoài repository trong thư mục artifact.
- Không sửa Router/module/lore, không chạy builder ghi dữ liệu, không commit/push. FULL_FILE giữ nguyên là baseline production.
