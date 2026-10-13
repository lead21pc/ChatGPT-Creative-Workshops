# Pilot selector từ metadata hiện có — source 70

Ngày: 2026-10-02. **Selector: 4 PASS, 4 PARTIAL, 0 FAIL. Answerer: 8 PASS, 0 FAIL, 0 INCONCLUSIVE.** Không có lượt nào tự tin bỏ FULL: cả 8 đều `CONFIDENCE=MEDIUM`, `NEED_FULL_FALLBACK=YES`.

Kết quả cho thấy metadata hiện có giúp tìm evidence cần thiết trong bộ câu hỏi này. **Chưa chứng minh metadata đủ để selector tự xác nhận selection hoàn chỉnh hoặc cho phép bỏ FULL_FILE.** Không suy kết quả này thành yêu cầu thêm metadata hay đổi production.

## Thiết kế và bảo toàn context

- Giữ đúng 8 câu của pilot trước; không thêm câu.
- Mỗi câu dùng một Selector A mới và một Answerer B mới, `fork_turns=none`: tổng cộng 16 lượt thực tế. Các agent không thấy lịch sử chat, câu trả lời trước hoặc oracle.
- A chỉ đọc `sN.txt`: câu hỏi, nguyên văn metadata hiện có và danh sách heading/subheading theo thứ tự nguồn. Metadata được trích từ header source 70 và các dòng áp dụng cho 70 trong index. Không thêm summary hoặc quan hệ dependency.
- Metadata đã cấp được lưu trong `selector-metadata.txt`: 4.266 ký tự. Phần index dùng các dòng 1–5, 16, 38, 157–158 của bản hiện tại; header dùng dòng 1–15 của source 70. Có giữ nguyên `Load mode: FULL_FILE`.
- B chỉ đọc `bN.txt`: câu hỏi và nguyên văn section A chọn, cùng instruction evidence boundary của pilot trước. Không cấp index/header, lý do lựa chọn, confidence, fallback flag, oracle hoặc đáp án FULL cho B.
- Không thực hiện FULL fallback trong lượt B: yêu cầu thiết kế cấm B nhận FULL. Vì vậy đây là đo chất lượng của candidate selection, **không phải** một workflow fallback đã chạy end-to-end.
- Liệt kê parent heading trong SELECT được hiểu là chọn toàn bộ parent và các child. Những child được liệt kê kèm parent không làm evidence bị lặp. Ví dụ câu 7 chọn parent §6 nên B nhận cả §6.1, §6.2, UNKNOWN và §6.3; đây không phải evaluator tự thêm qualifier.
- Trích từ heading đến trước heading cùng cấp hoặc cao hơn, giữ nguyên nội dung; chuẩn hóa xuống dòng khi đặt vào prompt. Không tự thêm UNKNOWN sibling. Câu 3 chọn riêng §6.3 nên không lấy nội dung §7.
- Evaluator đọc FULL để đặt oracle, kiểm lựa chọn và chấm câu trả lời. Oracle và tiêu chí được ghi trước khi chạy trong `protocol-before-runs.md`. `source70-evaluator-only.txt` là bản nguồn riêng cho evaluator; A/B không được đọc file này.
- Cùng cấu hình model kế thừa; không có tên model chính xác hoặc sampling parameters để báo cáo. Một lượt/câu, không đo tần suất production.
- Trích đoạn đáp án thực tế dùng để chấm nằm trong `OBSERVATIONS.md`. Báo cáo tóm tắt câu trả lời; trích đoạn không phải transcript đầy đủ.

## SELECTOR RESULTS

Ký hiệu § trong báo cáo là số section đã có trong nguồn, không phải ID mới. MISSED xét evidence quyết định; UNNECESSARY xét nội dung không cần cho mức câu hỏi này sau khi evaluator đọc FULL. Không phạt một section bổ trợ hợp lý; PARTIAL ở các case mở quá nhiều phần không thêm evidence quyết định, không phải lỗi lore hoặc lựa chọn nguy hiểm.

| Câu | EXPECTED SECTIONS | SELECTED SECTIONS | MISSED | UNNECESSARY / phần dư | RESULT |
| --- | --- | --- | --- | --- | --- |
| 1 | §15 hoặc đủ §15.1–15.3 | §15, CANON và §15.1–15.3 | Không | Parent/child lặp trong SELECT, gộp khi trích; không thêm evidence | PASS |
| 2 | §10; §9/§22 bổ trợ hợp lý | §9, §10, §11, §12, §19, §21, §22, §24 | Không | §12, §19, §21, §24 không cần cho cơ chế cấp quyền theo chu kỳ; §11 là bối cảnh dependency | PARTIAL |
| 3 | §8; §6.3 bổ trợ hợp lý | §8 cùng CANON/Holy Guard/Vệ binh quốc gia; §6.3 | Không | Một subsection bổ trợ trực tiếp allegiance, không phạt | PASS |
| 4 | §9 + §7 | §3, §4, §6, §7, §9, §22, §24 | Không | §3/§4/§6 có thể giúp định hướng vai trò, nhưng không cần để phân biệt hai quy trình; §22/§24 không thêm quy tắc quyết định | PARTIAL |
| 5 | §11 đủ mức hỏi; §10+§11 là lựa chọn đầy đủ tự nhiên | §10, §11, §12, §19, §21, §22, §24 | Không | §12, §19 và các phần tóm tắt/UNKNOWN không cần cho hai trục dependency đã được §11 nêu trực tiếp | PARTIAL |
| 6 | §5; hoặc §20 + §22 | §5 (CANON + UNKNOWN cơ chế sâu), §6, §22, §24 | Không | §6 trực tiếp đối chiếu chức năng Creed, §22 giữ UNKNOWN; §24 là phần kiểm giới hạn bổ trợ. Chưa tối ưu, nhưng lựa chọn có lý do sát câu hỏi | PASS |
| 7 | §6; hoặc §6.2 + UNKNOWN trong §6 | §6 (CANON, §6.2, UNKNOWN được liệt kê kèm parent), §22, §24 | Không | §22 trực tiếp kiểm exact target UNKNOWN; §24 bổ trợ anti-drift. Parent §6 còn có các oath khác, không làm mất qualifier | PASS |
| 8 | §7; §3 bổ trợ hợp lý | §3, §6, §7, §21, §22, §24 | Không | §6, §21, §22, §24 không cần để xác định quorum đồng thuận và giới hạn không suy Cult đã kiểm soát quorum | PARTIAL |

### Lý do của từng lựa chọn

1. A khớp heading “Ba tuyến tiếp cận TE”, đọc đủ cả ba tuyến và CANON chung. Không chỉ lấy một heading khớp từ khóa.
2. A chọn rộng các heading relic/dependency/quan hệ/kinh tế và các phần tóm tắt, chưa chỉ ra được phần nào đủ cho cơ chế định kỳ. An toàn nhưng dư rõ nhất ở một câu local.
3. A chọn section so sánh hai lực lượng và bổ sung oath của Holy Guard. Đây là nối subsection có lý do trực tiếp, không tự thêm quan hệ từ body chưa đọc.
4. A chọn cả “Trinity Hexagon district và thánh vật” lẫn “Creed quorum”, không mắc bẫy chỉ đọc nơi có thánh vật hoặc con số ba. Đọc thêm nhiều phần quyền lực và giới hạn.
5. A chọn cả “Thánh vật tạo dependency” và “Hai trục dependency”, đồng thời cảnh giác authority xuyên miền trong header. Tuy nhiên còn kéo thêm kinh tế, leak và nhiều tóm tắt. Chỉ cần trả lời mức tóm tắt trong 70; không đọc owner file khác.
6. A nhận ra heading “UNKNOWN / chưa chốt cơ chế sâu” dưới doctrine có thể quyết định câu hỏi bypass. Nó không thấy từ split-self trong metadata, nhưng vẫn chọn đúng phần qualifier. Không nhận body hoặc oracle trước.
7. A chủ động chọn cả CANON và UNKNOWN trong Creed, cùng UNKNOWN/deferred. Tránh lỗi trích riêng §6.2 rồi bỏ sibling UNKNOWN.
8. A chọn section quorum và cơ cấu quyền lực, đồng thời yêu cầu đối chiếu các giới hạn. Không chọn mỗi “Current causal graph” có từ khóa đúng.

### Confidence và fallback

Cả 8 lượt đều MEDIUM / YES. Các lý do đều nêu metadata chưa chứng minh đủ điều kiện hoặc qualifier. Câu 5 còn lưu ý header giao geopolitical interface cho AFM-001 và FULL của 70 cũng chưa chắc đủ cho chi tiết xuyên miền.

Hành vi đó giữ an toàn, nhưng **không chứng minh fallback được dùng có chọn lọc**: A yêu cầu FULL ngay cả hai câu rất hẹp mà oracle xác nhận selection đủ. Không có lượt NO để kiểm tính tự tin khi lựa chọn đủ. Không gọi 8/8 YES là độ chính xác phát hiện thiếu context 100%.

## ANSWER RESULTS

| Câu | Kết luận của B | Qualifier giữ/mất | Hallucination | RESULT |
| --- | --- | --- | --- | --- |
| 1 | Bắc đường mòn sát núi lửa; trung tâm đường quốc gia ML+TE, cơ sở chính thức; nam thô sơ chủ yếu logistics | Giữ: không tự gán chức năng quân sự/du lịch hoặc nhiệm vụ cụ thể | Không quan sát thấy | PASS |
| 2 | Relic tiêu hao rồi tái tạo; AF cần phong ấn định kỳ, ML giữ quyền cấp phép; AF mua quyền mỗi chu kỳ | Giữ: không giải thích được vì sao không chọn mua đứt, ownership law chưa đầy đủ; không bịa luật cấm bán/động cơ ML | Không quan sát thấy | PASS |
| 3 | Hai lực lượng riêng; Holy Guard bảo vệ Temple+Saintess, allegiance Saintess; National Guard bảo vệ quốc gia/chính quyền | Giữ: bảo vệ Temple không đồng nghĩa allegiance Temple; cách xử lý xung đột chưa xác lập | Không quan sát thấy | PASS |
| 4 | Linh mục làm chứng trong cho mượn khác vai trò clergy đồng thuận thực thi; Saintess không bắt buộc tham gia thực thi | Giữ: ít nhất ba người làm chứng khác quorum ba người đồng thuận; không chứng minh cùng nhân sự/làm chứng tự tạo quorum | Không quan sát thấy | PASS |
| 5 | AF duy trì thương mại do quyền dùng relic định kỳ dù đối địch; RF và ML là hai trục khác nhau | Giữ: không đồng nhất RF/firewall/bloodline với relic access; cơ chế RF sâu chưa được cấp | Không quan sát thấy | PASS |
| 6 | Cơ chế split-self vượt Creed chưa xác lập đầy đủ; không bảo đảm miễn nhiễm | Giữ: compatibility không chắc chắn, không tự tạo linh hồn/target/bypass; exact mechanism UNKNOWN | Không quan sát thấy | PASS |
| 7 | Có hậu quả tim mạch, exact target UNKNOWN; không suy cả gia đình đau tim | Giữ: phân biệt hậu quả tim mạch giáo dân với đau tim Head of State, phạm vi oath khác đối tượng chịu phạt | Không quan sát thấy | PASS |
| 8 | Không ghi canon Cult đã chiếm quorum/tự kích hoạt; chỉ có influence và attack surface | Giữ: ba clergy cùng đồng thuận; influence không chứng minh control, nguy cơ không phải sự kiện đã xảy ra | Không quan sát thấy | PASS |

So với pilot trước, ba câu từng INCONCLUSIVE (4, 5, 7) đều trả lời đầy đủ hơn khi selection tự tìm được evidence phụ. Đây là quan sát giữa hai lượt khác nhau, **không phải** so sánh có kiểm soát để quy toàn bộ cải thiện cho selector: số section được cấp tăng và model mỗi lượt có biến thiên.

## Độ rộng lựa chọn

FULL dài 15.865 ký tự. Chỉ tính union nội dung section cấp cho B, không tính lặp parent/child:

| Câu | Ký tự evidence B | Tỷ lệ FULL | Section/dòng đã trích |
| --- | ---: | ---: | --- |
| 1 | 452 | 2,8% | 556–588 |
| 2 | 5.436 | 34,3% | 369–539; 669–682; 727–810; 832–880 |
| 3 | 529 | 3,3% | 286–296; 340–368 |
| 4 | 5.142 | 32,4% | 99–186; 230–339; 369–406; 789–810; 832–880 |
| 5 | 4.899 | 30,9% | 407–539; 669–682; 727–810; 832–880 |
| 6 | 3.421 | 21,6% | 187–296; 789–810; 832–880 |
| 7 | 2.538 | 16,0% | 230–296; 789–810; 832–880 |
| 8 | 5.143 | 32,4% | 99–149; 230–339; 727–810; 832–880 |

Median 26,2%, trung bình 21,7%, lớn nhất 34,3%. Không có câu nào nhận nửa file, nhưng 4/8 câu nhận hơn 30%, kể cả câu local về relic chỉ cần §10 (726 ký tự trong pilot trước).

Đó chưa phải tiết kiệm end-to-end: A còn nhận 4.266 ký tự metadata mỗi lượt, có thêm một lượt model và instruction/tool overhead. Không đo token, latency hay chi phí. Nếu làm đúng tất cả yêu cầu FULL fallback của A, workflow vẫn phải đọc FULL ở 8/8 câu; phần candidate trở thành chi phí bổ sung. Pilot này không thực thi workflow đó.

## SUMMARY — sáu câu trả lời

1. **Local có chọn đúng không?** Có: cả 3 selection bao phủ evidence cần và B trả lời PASS. Câu 2 chọn quá rộng nên selector PARTIAL; hai câu còn lại PASS.
2. **Có chọn đúng multi-section closure không?** Có trong hai case đối chiếu: chọn §9+§7 và §10+§11. Cũng chọn được qualifier UNKNOWN ở câu 6 và 7. Không mắc bẫy từ khóa ở bộ câu hỏi này. Đây là closure đủ theo oracle đọc FULL, không phải closure đã được metadata tự chứng nhận.
3. **Có nhận ra metadata chưa đủ không?** Có cảnh giác, YES ở 8/8. Chưa chứng minh biết phân biệt khi nào thật sự cần fallback; mẫu thể hiện một chính sách dè dặt gần như mặc định.
4. **Có chọn quá rộng không?** Có ở 4 câu, đặc biệt local relic chọn 8 section. Chưa tới nửa file; có xu hướng đọc thêm UNKNOWN, anti-drift và causal graph dù không phải mọi câu cần chúng.
5. **Failure cụ thể lớn nhất?** Không có FAIL về evidence hoặc answer. Hạn chế lớn nhất là không xác nhận được lúc nào selection đủ mà không cần FULL, cộng với đọc dư. Câu 5 cảnh giác authority đúng nhưng vẫn chưa định vị được mức hỏi mà tóm tắt trong 70 đủ trả lời. Không có căn cứ sửa metadata để chữa một lỗi bỏ qualifier chưa xảy ra.
6. **Đủ đáng thử automation extraction chưa?** Có **chỉ cho việc trích heading trong shadow**, vì selection hiện có đã đưa được đủ evidence cho B ở 8/8 câu. Chưa đủ để tự quyết định bỏ FULL hoặc chứng minh tiết kiệm thực tế. Bước nhỏ nhất được đề xuất, chưa triển khai: một script thử riêng nhận danh sách heading đã chọn ở câu 4 và 7, tự trích rồi đối chiếu nội dung với excerpt chuẩn của lượt này, kiểm boundary/dedup và giữ nguyên UNKNOWN; giữ FULL_FILE fallback. Không thêm IDs, summary, metadata hoặc loader.

## Giới hạn và trạng thái repository

- Chỉ dùng body source 70. Đọc SYSTEM_CONTEXT để tuân thủ context gate; index chỉ dùng metadata liên quan 70. Không đọc body source 30/90/91 hoặc owner file khác.
- Câu hỏi giữ nguyên từ pilot trước, gồm lời hỏi ép kết luận quá mức; chưa thử thêm câu trung tính hoặc nguồn khó. Metadata có các heading cảnh báo UNKNOWN/anti-drift sẵn nên có thể hỗ trợ hành vi thận trọng.
- Instruction A đã yêu cầu xét qualifier và fallback, B đã yêu cầu nói rõ thiếu evidence. Không gọi đây là hành vi tự phát ngoài instruction.
- Model/cấu hình chỉ một loại, một lượt mỗi case, không có đánh giá mù giữa nhiều evaluator.
- Stop rule không kích hoạt: không có selector FAIL. Không thêm metadata hoặc sửa production sau khi nhìn kết quả.
- Repository `C:\Users\Sheeplark\Desktop\CI Versioning Audit & Changelog`, branch `maintenance/aetherfire-academy-domain-20261002`, HEAD `57e6e569e960520515391665f8f878b40aa6ee50`.
- SHA256 source trước/sau: `A843D44362392AA1940F69A9FCE0C26576DC82713586ABBCB419F964778F8158`. Git status trước/sau giống hệt; các thay đổi có sẵn được giữ nguyên.
- Chỉ tạo artifact ngoài repository. Không sửa Router, header, source lore, tests hay cold package; không commit/push; không triển khai selective loading.
