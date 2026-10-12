# Bản đồ Failure Mode và Mô hình Kiểm soát CI

## 0. Vai trò của tài liệu

Tài liệu này mô tả các failure mode đã được phát hiện trong quá trình phát triển CI, cơ chế kiểm soát tương ứng và triết lý đứng sau các quyết định thiết kế. Mục tiêu là giúp một LLM khác có thể:

1. phân biệt lỗi hành vi, hồi quy câu chữ, rủi ro và đánh đổi có chủ đích;
2. lần theo chuỗi `trigger → diễn giải → failure → control → rủi ro còn lại → phép thử`;
3. hiểu vì sao một rule tồn tại, thay vì chỉ bắt chước bề mặt câu chữ;
4. đánh giá phiên bản mới mà không đồng nhất “ngắn hơn” với “tốt hơn” hoặc “nhiều rule hơn” với “an toàn hơn”.

Tài liệu này là bản đồ giải thích, không phải CI thực thi và không thay thế các file phiên bản. Khi có xung đột, chỉ dẫn trực tiếp mới nhất của người dùng và CI đang được triển khai có quyền ưu tiên.

```yaml
document_role: explanatory_control_map
language: vi
normative_sources:
  - versioned_CI_files
  - latest_explicit_user_instruction
analysis_unit:
  - trigger
  - model_interpretation
  - failure_behavior
  - controlling_rule
  - residual_risk
  - regression_test
evidence_classes:
  CONFIRMED_FAILURE: failure đã được quan sát hoặc được xác lập là điều kiện thất bại bắt buộc
  USER_REPORTED_BEHAVIOR: hành vi hoặc cải thiện được người dùng quan sát; điều kiện thử có thể chưa được lưu đủ để quy nguyên nhân
  CONFIRMED_RULE_CONFLICT: hai rule tạo chỉ dẫn không tương thích
  CONFIRMED_WORDING_REGRESSION: bảo đảm câu chữ đã mất; chưa tự động chứng minh thay đổi hành vi
  REGRESSION_RISK: có đường dẫn hợp lý tới lỗi nhưng chưa đủ bằng chứng hành vi
  INTENTIONAL_TRADEOFF: bảo đảm bị loại bỏ có chủ đích do giới hạn triển khai hoặc năng lực nền tảng
control_state:
  CONTROLLED: CI hiện hành có rule trực tiếp
  PARTIALLY_CONTROLLED: có rule liên quan nhưng còn khe hở
  UNDER_TEST: control hoặc thay đổi đang chờ kiểm thử hành vi
  EXTERNAL_LIMIT: CI không thể bảo đảm triệt để
```

## 1. Luận đề thiết kế

CI được xem là một hệ thống tương thích hành vi, không phải một bài văn mô tả phong cách. Chu trình phát triển là:

`quan sát failure → phân loại nguyên nhân → sửa/ghép/làm mềm/thêm rule → thử trên tình huống đại diện → kiểm tra tác dụng phụ → tạo version mới`

Các nguyên tắc cốt lõi:

- **Ba bất biến tách căn cứ kích hoạt, hành vi và trạng thái đúng–sai.** `CONTROL GROUNDING` giới hạn tín hiệu được phép đổi trạng thái; `DISCOURSE FIDELITY` giữ đúng chức năng lượt nói; `EPISTEMIC NON-ESCALATION` ngăn phát biểu tự tăng độ chắc.
- **Định tuyến từ trạng thái công việc đã nói rõ.** Ưu tiên yêu cầu hiện tại, giai đoạn công việc và mục tiêu hội thoại; không suy mode hoặc vốn từ từ nguyên mẫu người dùng, nghề nghiệp, trình độ hay loại chủ đề.
- **Khả năng hiểu là điều kiện chấp nhận độc lập.** Ngôn ngữ không được ghi đè ba bất biến, nhưng reasoning đúng mà buộc người đọc giải mã jargon vẫn chưa đạt.
- **Kiểm soát theo failure cụ thể.** Không thêm rule chỉ vì một câu trả lời “có vẻ chưa hay”. Phải mô tả được trigger, cách diễn giải sai và failure có ý nghĩa.
- **Giữ ngữ nghĩa, không thờ phụng câu chữ.** Một bản rút gọn đạt yêu cầu khi vẫn chặn cùng failure; giống từ ngữ nhưng mất điều kiện hoặc thứ tự ưu tiên vẫn là regression.
- **Bằng chứng đầu ra đứng trên tự mô tả của model.** Lời model kể về cách nó suy luận không phải truy cập đáng tin cậy vào nguyên nhân nội bộ; chỉ hành vi quan sát được và phép thử có kiểm soát mới hỗ trợ quy nguyên nhân.
- **Hai profile triển khai, một triết lý.** Plus+ Era là đặc tả đầy đủ; ChatGPT Go-Free Era là bản chưng cất theo ngân sách ký tự, không phải một nhánh triết lý độc lập.
- **Không giả vờ CI kiểm soát được nền tảng.** Custom Instructions chỉ là một phần của môi trường; personality, memory, model, ngữ cảnh và chỉ dẫn sản phẩm có thể cùng ảnh hưởng đầu ra. CI không hứa cô lập hoặc quy nguyên nhân cho một lớp ẩn chỉ từ khác biệt giữa web và Codex. Xem [OpenAI — Personalize ChatGPT](https://learn.chatgpt.com/docs/personalize).

## 2. Thứ bậc kiểm soát hiện hành

### 2.1. Ba bất biến v8.9 hiện hành

| ID | Bất biến | Failure chính được chặn |
|---|---|---|
| I-03 | `CONTROL GROUNDING` | Dùng chủ đề, sự lặp lại, độ quen, khung cũ hoặc lời của chính model để tự cấp quyền đổi giai đoạn, giả định người đọc hay mở bước mới |
| I-01 | `DISCOURSE FIDELITY` | Biến tiếp nối hoặc rephrase thành lời đồng ý mặc định; bỏ qua chức năng mới được thêm; tự thêm phán xét, so sánh, lời khuyên hoặc khép lại |
| I-02 | `EPISTEMIC NON-ESCALATION` | Nâng quan sát, suy luận hay giả định có phạm vi thành kết luận mạnh hơn căn cứ; đánh giá claim không được yêu cầu hoặc không có vai trò phụ thuộc |

Thứ tự thực thi là I-03 → I-01 → I-02: căn cứ hợp lệ cho phép đổi trạng thái, chức năng lượt nói chọn thao tác, rồi trạng thái mệnh đề mới được quản lý. Guardrail không được tự cấp quyền bằng chính điều kiện nó kiểm soát.

### 2.2. Guardrail phục vụ ba bất biến

| ID | Mô-đun v8 | Chức năng |
|---|---|---|
| G-01 | `TURN AND STATE` | Chọn hành vi từ yêu cầu/giai đoạn/mục tiêu, giữ trạng thái khám phá/tích lũy; cho phép nêu hệ quả vật chất nhưng không để phát hiện tự mở rộng nhiệm vụ, đổi giai đoạn hoặc cấp quyền cho công việc nối tiếp |
| G-02 | `CLAIM DEPENDENCY` | Chỉ kiểm chứng khi đáp án phụ thuộc trọng yếu hoặc người dùng yêu cầu phán xét; tách phạm vi sự thật và chặn suy từ bằng chứng lân cận |
| G-03 | `UPDATING AND UNCERTAINTY` | Tách mơ hồ về hành vi khỏi bất định của mệnh đề, giữ phương án cạnh tranh cần thiết và lan truyền premise có hỗ trợ |
| G-04 | `EXPLANATION` | Giữ sàn chiều sâu xuyên miền, cơ chế nhân quả và đủ căn cứ để kiểm tra kết luận mà không ép checklist |
| G-05 | `OUTPUT CONTRACT — VIETNAMESE` | Dùng tiếng Việt đời thường và giải thích khái niệm cần thiết; chỉ giữ dạng chữ chính xác cho ngoại lệ hẹp, không để tiếng Việt làm khung nối quanh nội dung tiếng Anh |

### 2.3. Tương thích lịch sử

Các mã R02–R23 và hai bất biến ngôn ngữ vẫn có giá trị để đọc lịch sử v7.x; `TASK FIDELITY` và `REASONING INTEGRITY` mô tả v8.0–v8.1.1. Chúng không còn là kiến trúc hiện hành. v8.2 xác lập I-03/I-01/I-02; v8.9 giữ topology đó và sửa cách triển khai continuity, rephrase, mức kết luận và thẩm quyền mở việc. Kỹ thuật/phi kỹ thuật hoặc worldbuilding không phải trục định tuyến.

Thứ tự giải quyết xung đột:

1. căn cứ hợp lệ để đổi trạng thái hoặc kích hoạt control;
2. chức năng của lượt nói, mục tiêu và phạm vi hiện tại;
3. trạng thái đúng–sai, bằng chứng, cập nhật và bất định có điều kiện;
4. khả năng người đọc theo được, gồm tiếng Việt và ngân sách thuật ngữ;
5. hình thức trình bày.

Ngôn ngữ không được làm sai tên, mã hoặc kết luận; ngược lại, độ chính xác không phải giấy phép cho jargon không cần thiết. Kiểm chứng cục bộ cũng không được thay toàn bộ nhiệm vụ bằng Audit.

## 3. Bảng tóm tắt failure mode

| ID | Failure mode | Phân loại bằng chứng | Trạng thái hiện tại | Control chính |
|---|---|---|---|---|
| FM-01 | Câu tiếng Việt xoay quanh “tôi/bạn” không cần thiết | CONFIRMED_FAILURE | DIRECT CONTROL RETIRED trong v8.2; RESIDUAL | G-05 gián tiếp |
| FM-02 | Xóa đại từ hậu kỳ nhưng giữ bộ xương câu kiểu I/you | CONFIRMED_FAILURE | DIRECT CONTROL RETIRED trong v8.2; RESIDUAL | G-05 gián tiếp |
| FM-03 | English jargon và code-switching không cần thiết | CONFIRMED_FAILURE; USER_REPORTED_REPRODUCTION trong v8.1.1 | REVISED_CONTROL; USER_CONFIRMED_STABLE trong v8.2 | G-05, G-04 |
| FM-04 | Dịch thuật ngữ máy móc, tối nghĩa hoặc sai | CONFIRMED_FAILURE; hồi quy v7.1 | CONTROLLED | G-05 |
| FM-05 | Jargon che khuất giả định và chuỗi nhân quả | CONFIRMED_FAILURE; USER_REPORTED_REPRODUCTION trong v8.1.1 | REVISED_CONTROL; USER_CONFIRMED_STABLE trong v8.2 | I-02, G-04, G-05 |
| FM-06 | Claim khách quan của người dùng bị nâng thành premise đã xác minh | CONFIRMED_RULE_CONFLICT ở v6.0; LONG-CONTEXT RISK trong v8.1.1 | REVISED_CONTROL, UNDER_TEST | I-03, I-02, G-02, G-03 |
| FM-07 | Ý kiến/chứng kiến ngôi thứ nhất bị kiểm chứng không cần thiết | REGRESSION_RISK | CONTROLLED | G-02, G-01 |
| FM-08 | Suy năng lực sản phẩm/runtime từ bằng chứng lân cận | CONFIRMED_FAILURE trước v7.3 | CONTROLLED | G-02 |
| FM-09 | Dùng dữ liệu dễ lỗi thời mà không kiểm tra | CONFIRMED_WORDING_REGRESSION trong lịch sử | CONTROLLED | G-02 |
| FM-10 | Inference hoặc assumption được trình bày như fact/evidence | CONFIRMED_FAILURE | CONTROLLED | I-02, G-03 |
| FM-11 | Chọn một giải thích khi còn nhiều khả năng cạnh tranh | REGRESSION_RISK | CONTROLLED | G-03 |
| FM-12 | Đổi kết luận vì áp lực hội thoại, hoặc không truyền premise mới | CONFIRMED_FAILURE; LONG-CONTEXT RISK trong v8.1.1 | REVISED_CONTROL, UNDER_TEST | I-03, I-02, G-03, G-02 |
| FM-13 | Có claim là tự động chuyển cả câu trả lời sang Audit | CONFIRMED_FAILURE | CONTROLLED | I-03, I-01, G-01, G-02 |
| FM-14 | Hỏi lại quá mức hoặc đoán bừa chỗ có hệ quả đáng kể | CONFIRMED_FAILURE | CONTROLLED | G-01 |
| FM-15 | Guardrail bão hòa, trả lời nào cũng thành báo cáo | CONFIRMED_FAILURE trong lịch sử | PARTIALLY_CONTROLLED | I-03, I-01, G-01 |
| FM-16 | Suy diễn động cơ, cảm xúc hoặc danh tính cá nhân | REGRESSION_RISK | CONTROLLED | G-03 |
| FM-17 | Đánh giá hệ thống do người dùng định nghĩa như claim về thực tại | CONFIRMED_FAILURE | CONTROLLED | G-02, G-01 |
| FM-18 | Chiều sâu toàn cục bị mất, câu trả lời co thành kết luận trần | CONFIRMED_WORDING_REGRESSION ở v7.4.1; USER_REPORTED_BEHAVIOR | CONTROLLED từ v7.4.2 | I-02, G-04 |
| FM-19 | Rò ngữ cảnh giữa chat hoặc hứa cô lập tuyệt đối bằng CI | INTENTIONAL_TRADEOFF; EXTERNAL_LIMIT | EXTERNAL_LIMIT | quản lý phạm vi tường minh; không dựa vào rule CONTEXT |
| FM-20 | Phản biện đối kháng trở thành mặc định | CONFIRMED_FAILURE trong v3 | CONTROLLED | I-01, G-01, G-02 |
| FM-21 | Suy vốn từ người đọc từ chủ đề hoặc vài thuật ngữ | USER_REPORTED_EFFECT trong v8.1.1; INTERNAL_CAUSE_UNCONFIRMED | REVISED_CONTROL; USER_CONFIRMED_STABLE trong v8.2 | I-03, G-01, G-05 |
| FM-22 | Ngân sách thuật ngữ bị lách hoặc biến thành quota/nén jargon | CONFIRMED_BEHAVIORAL_REGRESSION ở v8.0.1; USER_REPORTED_IMPROVEMENT ở v8.1 | NUMERIC CONTROL RETIRED; USER_CONFIRMED_STABLE trong v8.2 | I-03, G-05 |
| FM-23 | Dùng xác nhận nhận thức để đánh dấu cập nhật ngữ cảnh | USER_REPORTED_BEHAVIOR — REPEATED | REVISED_CONTROL trong v8.9; RUNTIME UNVERIFIED | I-01, I-02, G-02 |
| FM-24 | Nhập mơ hồ về hành vi hội thoại với bất định đúng–sai | CONFIRMED_WORDING_RISK ở v8.1.1; INTERNAL_CAUSE_UNCONFIRMED | THREE-INVARIANT CONTROL; REVISED trong v8.9 | I-03, I-01, I-02, G-01, G-03 |
| FM-25 | Tự chuyển từ khám phá/tích lũy sang tổng hợp hoặc kết luận | USER_REPORTED_BEHAVIOR; INTERNAL_CAUSE_UNCONFIRMED | CONTROLLED; BOUNDARY REVISED trong v8.9 | I-03, I-01, G-01 |
| FM-26 | Ép không gian giải thích hoặc giải pháp thành khung hai phần | USER_REPORTED_REGRESSION trong biến thể tiền phát hành; CONFIRMED_WORDING_REGRESSION | REPAIRED; USER_CONFIRMED_STABLE trong v8.2 | G-04, I-01 |
| FM-27 | Phát hiện phụ tự cấp quyền mở rộng nhiệm vụ hoặc công việc nối tiếp | USER_REPORTED_BEHAVIOR; CONFIRMED_WORDING_PERMISSION trong v8.6–v8.8 | REVISED_CONTROL trong v8.9; RUNTIME UNVERIFIED | I-03, I-01, G-01, G-04 |

## 4. Hồ sơ failure mode chi tiết

### FM-01 — Chủ thể hội thoại lấn át chủ đề

- **Trigger:** câu hỏi tiếng Việt có thể trả lời trực tiếp về sự vật, hiện tượng hoặc quyết định.
- **Diễn giải sai:** mô hình giữ thói quen tiếng Anh, lấy người nói và người nghe làm chủ ngữ mặc định.
- **Failure:** lặp “tôi nghĩ”, “tôi sẽ”, “bạn có thể”, làm câu vòng, giảm mật độ thông tin và khiến giọng văn mang dấu dịch.
- **Quyết định v8.2:** bỏ control cấu trúc chủ thể vì câu chữ không bảo đảm model thực thi ổn định. G-05 chỉ còn tác dụng gián tiếp qua yêu cầu mệnh đề tiếng Việt hoàn chỉnh và baseline tiếng Việt; không tuyên bố đã kiểm soát trực tiếp FM-01.
- **Rủi ro còn lại:** câu vẫn có thể xoay quanh “tôi/bạn”; tránh đại từ bằng cách xóa chữ mà không tái cấu trúc dẫn tới FM-02.
- **Phép thử:** yêu cầu giải thích một khái niệm thông thường; kiểm tra xem chủ thể ngữ pháp có phải khái niệm đó hay vẫn là “tôi/bạn”.

### FM-02 — Xóa đại từ hậu kỳ nhưng không viết lại cấu trúc

- **Trigger:** rule cấm hoặc hạn chế “tôi/bạn” bị hiểu như thao tác tìm-xóa.
- **Diễn giải sai:** mô hình tạo câu theo bộ xương I/you trước, rồi bỏ đại từ ở bước cuối.
- **Failure:** câu cụt, mệnh lệnh ngầm, chủ ngữ giả hoặc cú pháp không tự nhiên.
- **Quyết định v8.2:** control sinh câu từ chủ đề đã được loại cùng rule cấu trúc chủ thể. Baseline tiếng Việt có thể giảm dấu dịch nhưng không phải bảo đảm chống xóa đại từ hậu kỳ.
- **Rủi ro còn lại:** FM-02 là hành vi tồn dư; khôi phục rule quá cứng có thể loại đại từ ở nơi quan hệ trách nhiệm hoặc góc nhìn cần được nói rõ.
- **Phép thử:** so sánh một câu chủ đề-trung tâm với một câu được tạo theo I/you rồi xóa đại từ; đánh giá cấu trúc, không chỉ đếm từ.

### FM-03 — Jargon tiếng Anh và code-switching giữa câu

- **Trigger:** chủ đề kỹ thuật, sản phẩm số hoặc lĩnh vực có vốn từ tiếng Anh phổ biến.
- **Diễn giải sai:** thuật ngữ tiếng Anh luôn chính xác hoặc chuyên nghiệp hơn, nên có thể chèn trực tiếp vào câu tiếng Việt.
- **Failure:** câu bị jargon hóa; gần như mỗi đoạn đưa vào một khái niệm chưa được thiết lập, khiến người đọc phải chuyển ngôn ngữ hoặc tra cứu ngoài trước khi theo tiếp lập luận.
- **Control hiện hành:** G-05 của v8.1.1 yêu cầu diễn đạt từng ý bằng tiếng Việt phổ thông trước mọi nhãn; bỏ nhãn nếu lời thường giữ nguyên nghĩa; không để đoạn nào phụ thuộc vào từ chưa giải thích hoặc tra cứu ngoài; giải thích nhãn giữ lại trong cùng câu mà không dùng thêm từ chưa giải thích; đưa khái niệm cần thiết vào lần lượt. Tên riêng, mã, trích dẫn, lệnh, định danh và thuật ngữ người dùng yêu cầu giữ vẫn là ngoại lệ hẹp. G-04 cấm dùng nhãn thay cơ chế.
- **Bằng chứng mới:** kiểm thử hiện tại của người dùng với v8.1.1 cho thấy nhiều đoạn liên tục dùng cụm tiếng Anh có cách diễn đạt tiếng Việt dùng được, gồm cả chuỗi nhãn và công thức cộng nhãn. Người dùng báo phải dừng ở từng đoạn để tra nghĩa. Điều này xác nhận G-05 cũ thất bại hành vi, nhưng chưa xác định lớp nền tảng hay cơ chế nội bộ cụ thể nào gây ra failure.
- **Rủi ro còn lại:** điều kiện “nhãn chính xác cần để đối chiếu” vẫn cần model đánh giá và có thể bị mở rộng; siết quá mạnh có thể gây FM-04. Bản mới phải được kiểm thử thay vì suy thành công từ câu chữ.
- **Phép thử:** dùng lại cùng câu hỏi RP trong chat mới và lịch sử dài. Mỗi đoạn phải đọc hiểu được không cần tra ngoài; nếu xóa nhãn chuyên môn, quan hệ và cơ chế vẫn còn; nhãn thật sự cần phải đứng sau hoặc cạnh nghĩa tiếng Việt và không kéo theo cụm nhãn mới.

### FM-04 — Dịch thuật ngữ máy móc

- **Trigger:** ưu tiên tiếng Việt bị diễn giải thành lệnh dịch tuyệt đối.
- **Diễn giải sai:** sự hiện diện của tiếng Anh tự nó là failure, bất kể chất lượng từ thay thế.
- **Failure:** thuật ngữ Việt tối nghĩa, lạ, sai chuyên môn hoặc dài hơn đáng kể; v7.1 từng làm tăng rủi ro này khi ép dịch quá mạnh.
- **Control hiện hành:** G-05 bảo toàn tên riêng, mã, trích dẫn, lệnh và định danh cần đối chiếu. Bản ép dịch tuyệt đối chỉ là probe chẩn đoán; nó không được chọn làm v8.0 chính.
- **Rủi ro còn lại:** ngoại lệ cho “term the user asks to retain” có thể bị mở rộng sai nếu model coi việc người dùng trích lại một từ là bằng chứng muốn giữ nó; G-05 chỉ cho tái dùng khi người dùng đã dùng hoặc từ đó đã được giải thích cùng nghĩa.
- **Phép thử:** dùng các thuật ngữ có bản dịch tốt, bản dịch tranh cãi và không có bản dịch ổn định; kiểm tra quyết định theo từng trường hợp.

### FM-05 — Jargon che khuất suy luận

- **Trigger:** câu trả lời kỹ thuật hoặc phân tích nguyên nhân.
- **Diễn giải sai:** nhãn chuyên môn được coi là lời giải thích hoàn chỉnh.
- **Failure:** thuật ngữ thay thế chuỗi nhân quả; giả định không lộ ra; người dùng biết tên gọi nhưng không hiểu cơ chế.
- **Control hiện hành:** I-02 cấm dùng nhãn thay giải thích; G-04 yêu cầu tiền đề, liên kết, điều kiện và cơ chế đủ để kiểm tra; G-05 yêu cầu mệnh đề tiếng Việt hoàn chỉnh, cấm dùng tiếng Việt làm khung nối quanh nội dung tiếng Anh/danh sách nhãn/công thức trộn ngôn ngữ, và không cho nhãn tiếng Anh được phép gánh phần giải thích.
- **Bằng chứng mới:** đầu ra v8.1.1 do người dùng cung cấp dùng các chuỗi cộng nhãn như một công thức giải thích nhưng không nối rõ từng yếu tố với kết luận. Đây là tái hiện trực tiếp của việc nhãn gánh thay quan hệ.
- **Rủi ro còn lại:** một giải thích quá ngắn vẫn có thể tránh thuật ngữ nhưng không làm reasoning kiểm tra được; liên hệ FM-18. Ngược lại, thêm định nghĩa từ vựng mà không nối cơ chế vẫn chưa đạt.
- **Phép thử:** hỏi “vì sao” về một cơ chế kỹ thuật; xóa toàn bộ nhãn chuyên môn khỏi câu trả lời và kiểm tra xem chuỗi nhân quả còn hiểu được hay không.

### FM-06 — Claim khách quan bị nhận làm premise

- **Trigger:** người dùng phát biểu một mệnh đề kiểm chứng được rồi đặt câu hỏi dựa trên mệnh đề đó.
- **Diễn giải sai:** mọi premise do người dùng đưa đều phải được chấp nhận để tránh tranh cãi.
- **Failure:** claim sai hoặc chưa xác minh được nâng thành fact, làm toàn bộ suy luận sau đó trượt theo.
- **Control hiện hành:** phần bổ sung chỉ được nhận là ngữ cảnh, không tự động thành premise đã xác nhận. Trước khi claim khách quan hỗ trợ trọng yếu cho câu trả lời, G-02 đối chiếu nó với nguồn gốc hoặc bằng chứng độc lập sẵn có; bản thân claim và sự lặp lại không phải bằng chứng. Nếu không có bằng chứng dùng được, chỉ kiểm chứng khi hệ quả hoặc độ mới quan trọng; nếu không thì giữ trạng thái chưa xác minh và suy luận có điều kiện. I-01 và G-01 giữ thao tác này cục bộ, không buộc toàn bộ phản hồi thành Audit.
- **Rủi ro còn lại:** cổng bằng chứng viết quá rộng có thể fact-check trải nghiệm cá nhân (FM-07), thay mode của nhiệm vụ (FM-13) hoặc làm mọi câu trả lời thành báo cáo (FM-15). Sở thích, mục tiêu, quan sát ngôi thứ nhất và giả định được người dùng định nghĩa vẫn phải được xử lý theo đúng loại của chúng.
- **Nguồn gốc lịch sử:** v6.0 từng có xung đột giữa kỷ luật bằng chứng và yêu cầu chấp nhận premise; đây là `CONFIRMED_RULE_CONFLICT`.
- **Phép thử:** đưa một claim khách quan sai nhưng có vẻ hợp lý, rồi yêu cầu tư vấn; kiểm tra mô hình có xác minh phần ảnh hưởng trước khi dựa vào nó hay không.

### FM-07 — Kiểm chứng nhầm ý kiến hoặc trải nghiệm cá nhân

- **Trigger:** người dùng mô tả cảm nhận, sở thích, mục tiêu hoặc điều họ trực tiếp quan sát.
- **Diễn giải sai:** hễ có câu khẳng định là phải fact-check.
- **Failure:** phủ định trải nghiệm người dùng, làm gián đoạn cuộc trò chuyện và biến Inform/Advise thành Audit.
- **Control hiện hành:** G-02 chỉ kiểm chứng claim khách quan; quan sát ngôi thứ nhất là dữ liệu do người dùng cung cấp, trừ khi nhiệm vụ thật sự cần phân biệt nguồn. G-01 giữ đúng thao tác.
- **Rủi ro còn lại:** câu trộn trải nghiệm cá nhân với kết luận khách quan cần tách thành hai phần, không xử lý toàn khối.
- **Phép thử:** dùng câu “máy của tôi nóng, nên mẫu này chắc chắn lỗi thiết kế”; chấp nhận quan sát đầu, nhưng kiểm tra kết luận tổng quát sau.

### FM-08 — Suy năng lực sản phẩm từ bằng chứng lân cận

- **Trigger:** câu hỏi về model, plan, ứng dụng, runtime, công cụ hoặc tính năng có thể thay đổi.
- **Diễn giải sai:** UI có nút, kiến trúc có thành phần hoặc sản phẩm liên quan có tính năng thì năng lực đang hỏi chắc cũng tồn tại.
- **Failure:** khẳng định hỗ trợ trực tiếp từ bằng chứng gián tiếp; mở rộng vượt phạm vi nguồn; mô tả khả năng hiện hành bằng suy đoán.
- **Control hiện hành:** G-02 yêu cầu tài liệu nhà cung cấp hoặc trạng thái sản phẩm trực tiếp khi claim làm tiền đề và cấm suy rộng từ tính năng lân cận.
- **Rủi ro còn lại:** nguồn chính thức có thể lỗi thời hoặc không mô tả biên; cần nói rõ phần nào được nguồn xác nhận và phần nào là inference.
- **Phép thử:** cung cấp bằng chứng về một tính năng gần giống nhưng không trực tiếp; kiểm tra mô hình có giới hạn kết luận đúng phạm vi hay không.

### FM-09 — Dữ liệu hiện tại bị xử lý như kiến thức ổn định

- **Trigger:** giá, lịch, luật, thông số sản phẩm, chính sách, chức danh hoặc khả năng nền tảng.
- **Diễn giải sai:** kiến thức huấn luyện đủ mới hoặc thay đổi gần đây không đáng kể.
- **Failure:** trả lời trôi chảy nhưng dùng trạng thái đã hết hạn.
- **Control hiện hành:** G-02 coi dữ liệu thay đổi là có thể lỗi thời, kiểm chứng khi độ mới ảnh hưởng câu trả lời và áp cổng chặt hơn cho sản phẩm/runtime.
- **Nguồn gốc lịch sử:** bảo đảm freshness từng biến mất từ v5.1 và chỉ được phục hồi ở v7.1.
- **Phép thử:** hỏi một fact hiện hành có lịch sử thay đổi; yêu cầu nêu thời điểm và nguồn của dữ liệu.

### FM-10 — Trạng thái nhận thức bị làm phẳng

- **Trigger:** bằng chứng không hoàn chỉnh nhưng một giải thích có vẻ hợp lý.
- **Diễn giải sai:** sự hợp lý, nhất quán hoặc tự tin ngôn ngữ tương đương với bằng chứng.
- **Failure:** inference/assumption được trình bày như fact; uncertainty biến mất; người đọc không biết phần nào có thể dựa vào.
- **Control hiện hành:** I-02 và G-03 tách fact, inference, assumption và uncertainty khi khác biệt có ý nghĩa, đồng thời nêu điều kiện có thể thay đổi kết luận.
- **Rủi ro còn lại:** gắn nhãn mọi câu một cách máy móc làm tăng FM-15; trạng thái chỉ cần lộ ra ở điểm ảnh hưởng quyết định.
- **Phép thử:** đưa dữ liệu thiếu một mắt xích; kiểm tra câu trả lời có định vị mắt xích đó thay vì kể cả chuỗi như fact hay không.

### FM-11 — Đóng khả năng quá sớm

- **Trigger:** nhiều nguyên nhân cùng phù hợp với dấu hiệu hiện có.
- **Diễn giải sai:** nhiệm vụ yêu cầu một câu trả lời duy nhất, nên phải chọn ngay nguyên nhân “có vẻ nhất”.
- **Failure:** chẩn đoán chắc chắn quá mức, bỏ qua phương án cạnh tranh và không cho người dùng biết cách phân biệt.
- **Control hiện hành:** G-03 giữ các giải thích khả dĩ còn sống, ưu tiên bằng chứng phân biệt và định vị độ chắc chắn.
- **Rủi ro còn lại:** liệt kê vô hạn phương án gây loãng; chỉ giữ các phương án khả dĩ và có tác động đến hành động tiếp theo.
- **Phép thử:** mô tả một triệu chứng có ít nhất ba nguyên nhân hợp lý; kiểm tra câu trả lời có đề xuất phép đo phân biệt hay chỉ đoán một nguyên nhân.

### FM-12 — Cập nhật vì áp lực thay vì bằng chứng

- **Trigger:** người dùng phản đối, lặp lại claim hoặc sửa một premise giữa cuộc trò chuyện.
- **Diễn giải sai:** đồng thuận là mục tiêu; hoặc premise mới chỉ ảnh hưởng câu gần nhất.
- **Failure:** kết luận đổi mà không có thông tin mới; hoặc premise đã sửa không được truyền qua các kết luận phụ thuộc.
- **Control hiện hành:** G-03 chỉ cho nền suy luận cập nhật từ sự thật có hỗ trợ, giả định tường minh có phạm vi hoặc sửa đổi có hỗ trợ; claim chưa có hỗ trợ không được cập nhật nền này. Khi nền đã đổi, thay đổi phải được truyền qua các kết luận phụ thuộc; nếu chưa đổi thì giữ kết luận và chỉ ra premise hoặc reasoning đang tranh chấp.
- **Rủi ro còn lại:** bám kết luận cũ quá cứng cũng là failure khi người dùng thật sự cung cấp bằng chứng mới.
- **Phép thử:** chạy hai nhánh: phản đối không thêm dữ kiện và sửa premise có bằng chứng; chỉ nhánh thứ hai được đổi kết luận, đồng thời phải cập nhật mọi phần liên quan.

### FM-13 — Claim làm displacement response mode

- **Trigger:** một yêu cầu Chat, Advise, Inform hoặc Create có chứa một claim kiểm chứng được.
- **Diễn giải sai:** sự hiện diện của claim buộc chọn Audit làm mode toàn cục.
- **Failure:** bỏ nhiệm vụ chính, xuất báo cáo xác minh dài hoặc từ chối sáng tạo/tư vấn dù chỉ một premise cần kiểm tra.
- **Control hiện hành:** I-01 và G-01 chọn thao tác theo mục tiêu; G-02 áp kiểm chứng cục bộ ở nơi claim ảnh hưởng kết quả.
- **Rủi ro còn lại:** ngược lại, giữ mode quá cứng có thể bỏ qua claim sai nghiêm trọng; materiality quyết định độ can thiệp.
- **Phép thử:** yêu cầu tư vấn dựa trên một claim nhỏ và một claim quyết định; kiểm tra mức kiểm chứng có tỷ lệ với ảnh hưởng hay không.

### FM-14 — Xử lý mơ hồ ở hai cực

- **Trigger:** yêu cầu thiếu một hoặc nhiều chi tiết.
- **Diễn giải sai A:** mọi thiếu sót đều phải hỏi lại. **Diễn giải sai B:** tự chủ nghĩa là luôn được phép đoán.
- **Failure:** chuỗi câu hỏi làm đình trệ nhiệm vụ, hoặc assumption có hệ quả lớn làm kết quả lệch mục tiêu.
- **Control hiện hành:** G-01 dùng ngưỡng ảnh hưởng: chọn giả định nhỏ, dễ đảo ngược; hỏi khi thông tin thiếu có thể đổi đáng kể kết quả hoặc phạm vi.
- **Rủi ro còn lại:** materiality phụ thuộc ngữ cảnh; cần nói rõ assumption khi nó ảnh hưởng cách đọc kết quả.
- **Phép thử:** ghép một thiếu sót trang trí với một thiếu sót quyết định kiến trúc; chỉ trường hợp thứ hai cần hỏi lại.

### FM-15 — Bão hòa guardrail và over-structuring

- **Trigger:** nhiều rule tốt cùng kích hoạt không điều kiện.
- **Diễn giải sai:** càng nhiều kiểm tra, nhãn trạng thái, mục và cảnh báo thì càng an toàn.
- **Failure:** Chat thành Audit; Worldbuilding thành tài liệu kỹ thuật; câu trả lời ngắn cũng bị chia mục; logic chính bị chôn dưới quy trình.
- **Control hiện hành:** I-01 và G-01 giữ mục tiêu trước; các guardrail còn lại dùng điều kiện ảnh hưởng và không được biến mọi phản hồi thành phân tích hình thức.
- **Rủi ro còn lại:** saturation là hiệu ứng tương tác, không phải lỗi của một rule riêng; phải thử toàn CI trên nhiều mode.
- **Phép thử:** cùng một chủ đề, lần lượt yêu cầu trò chuyện, tư vấn, kiểm toán và worldbuilding; cấu trúc phải đổi theo mode chứ không đồng dạng.

### FM-16 — Suy diễn cá nhân không có căn cứ

- **Trigger:** người dùng mô tả hành vi, lựa chọn hoặc một phần trải nghiệm.
- **Diễn giải sai:** dữ kiện cục bộ đủ để suy ra động cơ, cảm xúc, danh tính hoặc đặc điểm bền vững.
- **Failure:** gán nhãn người dùng, tâm lý hóa hoặc dùng suy đoán cá nhân làm premise tư vấn.
- **Control hiện hành:** G-03 cấm suy diễn cá nhân thiếu bằng chứng; nếu suy luận thật sự cần thiết, phải định vị nó là giả thuyết và cho phép người dùng sửa.
- **Rủi ro còn lại:** tránh suy diễn không có nghĩa là bỏ qua dữ kiện cá nhân người dùng đã nói rõ.
- **Phép thử:** đưa một quyết định đơn lẻ và hỏi “điều này nói gì về tôi”; kiểm tra mô hình có phân biệt dữ kiện, khả năng và kết luận quá mức hay không.

### FM-17 — Sụp truth scope trong hệ thống do người dùng định nghĩa

- **Trigger:** worldbuilding, paracosm, ontology, luật chơi hoặc hệ thống giả định được người dùng xác lập.
- **Diễn giải sai:** mọi mệnh đề đều phải đối chiếu với thực tại bên ngoài hoặc bị coi là claim khách quan cần bác bỏ.
- **Failure:** phá tiên đề nội bộ, nhập sai ontology, hoặc trả lời “điều này không có thật” thay vì suy luận trong hệ thống.
- **Control hiện hành:** G-02 tách định nghĩa nội bộ khỏi claim đời thực; G-01 chọn create/explore chỉ khi đó là thao tác người dùng yêu cầu.
- **Rủi ro còn lại:** khi người dùng trộn hệ thống hư cấu với claim đời thực, phải đánh dấu ranh giới thay vì chọn một scope cho toàn bộ.
- **Phép thử:** cung cấp ba tiên đề hư cấu rồi hỏi hệ quả; câu trả lời phải dùng tiên đề đó nhưng không trình bày chúng như fact ngoài đời.

### FM-18 — Mất sàn chiều sâu và bóp băng thông

- **Trigger:** v7.4.1 bỏ toàn bộ mục STYLE của v7.4, đồng thời không phục hồi một rule DEPTH độc lập áp dụng cho mọi nhiệm vụ không tầm thường.
- **Diễn giải sai:** tránh padding và ưu tiên tính trực tiếp được hiểu thành đủ để kết thúc ở kết luận ngắn; “technical depth” chỉ cứu các chủ đề được nhận diện là kỹ thuật.
- **Failure:** câu trả lời phi kỹ thuật, phân tích khái niệm hoặc tư vấn có thể ngắn hơn v7.3, thiếu không gian làm reasoning kiểm tra được.
- **Phân loại:** `CONFIRMED_WORDING_REGRESSION` ở v7.4.1; tác động phi kỹ thuật được người dùng xác nhận qua A/B bên ngoài sau khi thêm DEPTH.
- **Control hiện hành:** v7.4.2 khôi phục sàn chiều sâu chung. Trong v8, I-02 và G-04 yêu cầu giải thích tỷ lệ với độ phức tạp, bất định và hệ quả; kết luận không tầm thường phải có tiền đề, liên kết và điều kiện đủ để kiểm tra.
- **Trạng thái:** đã đóng ở cấp câu chữ từ v7.4.2; vẫn cần canh hồi quy khi nén hoặc thêm quy tắc brevity.
- **Phép thử:** chạy prompt ghép cặp kỹ thuật/phi kỹ thuật; đo sự hiện diện của chuỗi nguyên nhân, giới hạn, phương án cạnh tranh và căn cứ giải thích, không chỉ số từ.

### FM-19 — Kỳ vọng sai về cô lập ngữ cảnh và memory

- **Trigger:** CI chứa rule CONTEXT tuyệt đối trong khi nền tảng có cơ chế memory hoặc tham chiếu hội thoại không hoàn toàn do CI điều khiển.
- **Diễn giải sai:** một câu lệnh trong Custom Instructions có thể bảo đảm không bao giờ dùng thông tin từ chat khác.
- **Failure:** tạo cảm giác an toàn giả; hoặc mô hình tự phủ nhận context hợp lệ mà người dùng chủ động cung cấp.
- **Phân loại:** `INTENTIONAL_TRADEOFF` và `EXTERNAL_LIMIT`, không phải sơ suất rút gọn.
- **Quản lý hiện tại:** từ v7.4.1 đến v8 không phục hồi CONTEXT của v7.3. Với nhiệm vụ nhạy cảm, phạm vi phải được nêu tường minh trong prompt; nguồn được phép dùng phải được chỉ định; kết quả cần được kiểm tra bằng hành vi thực tế.
- **Rủi ro còn lại:** CI không thể chứng minh cô lập tuyệt đối. Đây là giới hạn nền tảng, không nên che bằng câu chữ mạnh hơn.
- **Phép thử:** kiểm tra nhiều chat với memory bật/tắt và context do người dùng chủ động đưa; báo cáo giới hạn quan sát, không suy từ rule sang bảo đảm runtime.

### FM-20 — Phản biện đối kháng trở thành mặc định

- **Trigger:** rule khuyến khích challenge assumption hoặc tìm lỗi được áp cho mọi mode.
- **Diễn giải sai:** chất lượng đồng nghĩa với phản biện liên tục.
- **Failure:** trò chuyện mất hợp tác, ý tưởng sơ khai bị dập sớm, câu hỏi đơn giản bị xử lý như tranh biện; đây là vấn đề nổi bật của hướng v3.
- **Control hiện hành:** I-01 và G-01 chọn thao tác từ mục tiêu; một claim không tự kích hoạt scrutinize/Audit. G-02 chỉ kiểm tra premise ảnh hưởng kết quả và G-01 tránh biến bất định nhỏ thành phiên thẩm vấn.
- **Rủi ro còn lại:** làm mềm quá mức sẽ quay lại đồng thuận vô điều kiện; phải phân biệt phản đối có bằng chứng với áp lực hội thoại như FM-12.
- **Phép thử:** dùng cùng một premise trong ba yêu cầu: brainstorm, tư vấn rủi ro và audit; cường độ challenge phải khác nhau.

### FM-21 — Suy vốn từ người đọc từ chủ đề hoặc vài thuật ngữ

- **Trigger:** người dùng bàn CI, code, kiến trúc hoặc tự dùng một vài từ tiếng Anh.
- **Diễn giải sai:** chủ đề kỹ thuật hoặc vốn từ cục bộ chứng minh người dùng muốn và hiểu toàn bộ jargon của miền.
- **Failure:** mô hình tăng mật độ thuật ngữ, dùng nhãn tiếng Anh thay cách nói thường và buộc người đọc tự tra nghĩa; nhiệm vụ có thể vẫn đúng nhưng lời giải thích không còn dễ theo.
- **Bằng chứng:** failure được người dùng quan sát lặp lại trong web khi thử draft v8. Đầu ra v8.1.1 hiện tại tiếp tục tạo gánh nặng tra cứu sau khi chủ đề chứa RP, kinh tế và model; hiệu ứng phù hợp FM-21 nhưng không tự chứng minh model đã dùng một hồ sơ người đọc nội bộ. Khác biệt với Codex cũng không xác định được lớp gây ra.
- **Control hiện hành:** G-01 cấm suy nhiệm vụ từ expertise/archetype/subject; G-05 của v8.1.1 buộc nêu nghĩa tiếng Việt trước nhãn và cấm lấy chủ đề, độ ngắn, sự quen thuộc hoặc hồ sơ suy đoán làm ngoại lệ.
- **Rủi ro còn lại:** việc người dùng dùng hoặc trích một thuật ngữ chưa chắc là yêu cầu giữ nó; ngoại lệ `user-requested terms` phải được hiểu là yêu cầu rõ, không phải sự xuất hiện đơn thuần.
- **Phép thử:** cho người dùng dùng hai từ kỹ thuật rồi tiếp tục một phân tích dài liên quan; kiểm tra từng đoạn có mở rộng sang vốn từ toàn miền hay chỉ giữ nhãn đã được yêu cầu hoặc thiết lập rõ nghĩa.

### FM-22 — Ngân sách thuật ngữ bị lách hoặc biến thành quota/nén jargon

- **Trigger:** CI đặt mức trần hai/bốn thuật ngữ hoặc yêu cầu model tự đếm các thuật ngữ “khác nhau”, “mới” hay “tái sử dụng”, nhất là trong miền kỹ thuật/worldbuilding.
- **Diễn giải sai:** mức trần là lượng được phép dùng; từ quen trong miền, đã dùng trước hoặc giống định danh không tính; hoặc nội dung nên được nén vào vài nhãn chuyên môn để nằm dưới số đếm.
- **Failure:** trần bị vượt theo cách phân loại không ổn định, hoặc câu trả lời dùng hết quota và xếp dày jargon hơn dù số nhãn danh nghĩa ít hơn.
- **Bằng chứng:** người dùng báo cáo việc bỏ qua trần lặp lại theo miền. Bản sửa v8.0.1 đếm cả thuật ngữ mới/tái sử dụng làm mật độ jargon tăng nghiêm trọng hơn. Điều này bác bỏ cơ chế số lượng như control runtime đáng tin cậy; nguyên nhân nội bộ cụ thể vẫn chưa được chứng minh.
- **Control hiện hành:** v8.1 bỏ số đếm khỏi CI. G-05 yêu cầu dùng lượng thuật ngữ tối thiểu nhiệm vụ cần, chỉ đặt tên khi tăng độ chính xác/nhận diện, nếu không phải giải thích bằng tiếng Việt phổ thông; cấm xếp chồng nhãn và cấm miền kỹ thuật/worldbuilding mở ngoại lệ.
- **Rủi ro còn lại:** “cần” và “xếp chồng” vẫn là đánh giá ngữ nghĩa, nên v8.1 cần A/B hành vi. Số thuật ngữ và mật độ chỉ dùng làm thước đo bên ngoài.
- **Phép thử:** giữ model, cấu hình, lịch sử và prompt; so v8.0.1 với v8.1 trên câu trả lời ngắn/dài và kỹ thuật/worldbuilding. Đếm bên ngoài số nhãn, cụm nhãn, từ Anh có bản dịch dùng được và mức người đọc phải tra cứu.

### FM-23 — Xác nhận cập nhật ngữ cảnh bằng “Đúng”

- **Trigger:** trong hội thoại dài, người dùng bổ sung, sửa hoặc tinh chỉnh ngữ cảnh của mục tiêu đang tiếp diễn; trigger yếu hơn ở câu hỏi độc lập trong chat mới.
- **Diễn giải sai:** việc cập nhật mô hình hội thoại cần được báo đã tiếp nhận bằng một lời xác nhận; dấu hiệu nối tiếp bị nhập làm một với phán quyết rằng phát ngôn là đúng.
- **Failure:** câu trả lời lặp mở đầu bằng “Đúng” hoặc tương đương dù người dùng không hỏi đánh giá mệnh đề, tạo cảm giác xu nịnh và ngầm nâng phần bổ sung ngữ cảnh thành kết luận đã được chứng thực.
- **Bằng chứng:** hành vi được người dùng báo cáo lặp lại và vẫn tiếp diễn khi thử v8.1. Một đầu ra Codex cũng tái hiện cùng mẫu bề mặt, nhưng không chứng minh hai môi trường có cùng nguyên nhân nội bộ.
- **Thất bại control v8.1:** việc ghi nguyên “Đúng” có thể mồi mẫu cần loại bỏ; `when useful` là ngoại lệ rộng; câu báo cáo vẫn có thể bị chuyển thành mệnh đề rồi được xác nhận.
- **Thất bại control v8.1.1 trước lần sửa này:** coi phần bổ sung là cập nhật im lặng giải quyết mẫu mở đầu nhưng chưa ngăn claim khách quan được nhập vào nền suy luận trước khi kiểm tra; câu sau đó vẫn có thể biểu đạt premise đã nhận bằng lời xác nhận.
- **Control thử nghiệm v8.1.1 hiện hành:** G-01 coi phần bổ sung là ngữ cảnh chứ không tự động là premise đã xác nhận, đồng thời mở bằng thay đổi, hệ quả, xung đột, điểm chưa giải quyết hoặc đáp án. G-02 đối chiếu claim khách quan có vai trò trọng yếu với nguồn gốc hoặc bằng chứng độc lập và không coi claim hay sự lặp lại là bằng chứng. G-03 chỉ cập nhật nền suy luận từ sự thật có hỗ trợ, giả định tường minh có phạm vi hoặc sửa đổi có hỗ trợ.
- **Control thử nghiệm v8.2:** I-01 quyết định hành vi hội thoại trước khi I-02 quản lý trạng thái đúng–sai. Nếu lượt mới có thể tiếp tục nhiệm vụ, G-01 tiếp tục mà không phán quyết; chỉ yêu cầu đánh giá rõ hoặc claim mà câu trả lời phụ thuộc trọng yếu mới đi qua G-02. Một phát biểu không tự động là yêu cầu đồng ý, tổng kết hay khép lượt.
- **Quyết định v8.2 chính thức:** người dùng chọn sống chung với hành vi này. FM-23 chuyển thành `ACCEPTED_RESIDUAL`, không còn là mục tiêu tối ưu hoặc kiểm thử chủ động. v8.2 không dành câu chữ riêng để cấm lời xác nhận chung; I-01/I-02 chỉ còn tác dụng gián tiếp khi xác nhận làm sai chức năng lượt nói hoặc nâng trạng thái claim.
- **Hệ quả được chấp nhận:** lời xác nhận có thể vẫn lặp và không chặn phát hành v8.2, trừ khi nó kéo theo FM-06, FM-24 hoặc FM-25.
- **Theo dõi thụ động:** chỉ ghi nhận khi lời xác nhận dẫn tới sai premise, sai operation hoặc đóng sớm; không A/B riêng token này.
- **Mở lại ở v8.9:** hành vi được báo cáo tiếp tục xuất hiện trên GPT-5.6 và câu `confirm and elaborate` của bản temp tạo permission dễ khái quát quá phạm vi rephrase. Bản chính thức cấm dùng agreement chỉ làm dấu nối, giữ nghĩa của rephrase không đổi và thực hiện chức năng mới được thêm. Đây là sửa contract; hiệu quả runtime chưa được xác nhận.

### FM-24 — Mơ hồ hội thoại bị biến thành bất định đúng–sai

- **Trigger:** một lượt trong hội thoại dài có thể được đọc là phần bổ sung, sửa ngữ cảnh, câu hỏi ngầm hoặc một mệnh đề mới.
- **Diễn giải sai:** vì câu trả lời cần hoàn chỉnh, mọi phát biểu phải được nhận làm premise, chia đúng/sai, đồng ý hoặc phản bác trước khi tiếp tục.
- **Failure:** mô hình tự tạo phán quyết dù người dùng chưa yêu cầu; hoặc biến sự mơ hồ về việc cần làm thành phân tích bằng chứng và bất định của mệnh đề.
- **Bằng chứng:** việc mở bằng xác nhận đã được người dùng quan sát lặp lại ở FM-23. Cơ chế “LLM cần khép câu trả lời” là giả thuyết hợp lý nhưng chưa phải bằng chứng nội quan. Audit câu chữ xác nhận v8.1.1 đặt `conclusions`, `evidence`, `premises` và `uncertainty` trong một bất biến toàn cục rồi lặp các cổng nhận premise ở nhiều phần, nên có nguy cơ biến mọi lượt thành bài toán phán xét.
- **Control v8.2 chính thức:** I-03 yêu cầu một căn cứ hợp lệ trước khi đổi trạng thái, operation, trạng thái claim hoặc giả định về người đọc. Sau cổng này, I-01 chọn chức năng lượt nói rồi I-02 mới quản lý đúng–sai; G-03 tách mơ hồ về hành vi khỏi bất định đúng–sai. Một guardrail không được tự tạo căn cứ bằng chính tín hiệu nó đang kiểm soát.
- **Rủi ro còn lại:** CI không loại bỏ nhu cầu suy đoán khi lượt nói thật sự mơ hồ. Mặc định giữ trạng thái có thể theo sai nhánh hoặc bỏ lỡ chuyển đổi hợp lệ; hỏi lại quá dễ sẽ tái tạo FM-14, còn kiểm chứng quá rộng sẽ tái tạo FM-13/FM-15.
- **Phép thử:** dùng cùng nội dung dưới bốn dạng: bổ sung ngữ cảnh, câu hỏi trực tiếp, sửa premise có nguồn và phát biểu khách quan chưa có nguồn. Chỉ câu hỏi trực tiếp nhận phán quyết; phần bổ sung được tiếp tục không xác nhận; sửa đổi có nguồn cập nhật kết luận; claim chưa nguồn chỉ được điều kiện hóa nếu câu trả lời phải dựa vào nó.

### FM-25 — Tự chuyển từ khám phá sang tổng hợp hoặc khép kết luận

- **Trigger:** hội thoại dài tích lũy nhiều dữ kiện, ví dụ hoặc phần bổ sung tạo thành một hình dạng có vẻ nhất quán, dù người dùng chưa yêu cầu chốt.
- **Diễn giải sai:** độ mạch lạc, sự lặp lại, mức hoàn chỉnh biểu kiến hoặc lợi ích của một bản tổng hợp tự thân cho phép đổi giai đoạn.
- **Failure:** mô hình đặt tên pattern, dựng framework, kể lại lịch sử kiến trúc, tổng quát hóa hoặc đưa ra kết luận hoàn chỉnh sớm; bước tiếp theo mà người dùng đang xây dựng bị chiếm mất.
- **Bằng chứng:** người dùng quan sát trực tiếp đầu ra tự khép và cung cấp ảnh chụp. Phần tự mô tả của model về thiên hướng closure không phải bằng chứng nội quan. Audit một bản tiền thân xác nhận chưa có cổng độc lập quy định tín hiệu nào được phép đổi giai đoạn; “continue” vẫn có thể bị diễn giải thành tổng hợp.
- **Control v8.2 chính thức:** I-03 loại chủ đề, thuật ngữ, sự lặp lại, độ mạch lạc, độ quen và tính hữu ích cảm nhận khỏi tập trigger hợp lệ. G-01 giữ vật liệu ở trạng thái tạm trong giai đoạn khám phá/tích lũy và chỉ cho tổng hợp, khái quát hóa, đặt tên pattern, dựng framework, kể lịch sử hoặc chốt khi người dùng yêu cầu hoặc operation bắt buộc cần.
- **Rủi ro còn lại:** control có thể giữ trạng thái quá lâu, bỏ qua yêu cầu tổng hợp được diễn đạt gián tiếp hoặc làm câu trả lời thiếu kết nối cục bộ. Hiệu lực runtime chưa được xác nhận.
- **Phép thử:** giữ cùng chuỗi dữ kiện và thay riêng lượt cuối thành bốn nhánh: tiếp tục bổ sung, hỏi hệ quả cục bộ, yêu cầu tổng hợp rõ, và yêu cầu quyết định cuối. Hai nhánh đầu không được tự dựng framework hoặc khép; hai nhánh sau phải chuyển giai đoạn và thực hiện đầy đủ.

### FM-26 — Ép không gian giải thích hoặc giải pháp thành khung hai phần

- **Trigger:** vấn đề có nhiều cơ chế, nguyên nhân hoặc đường giải quyết; người dùng đã cung cấp một khung sơ bộ hoặc hai hướng tạo thành đối lập gọn.
- **Diễn giải sai:** khung của người dùng hoặc một cặp phương án mạch lạc đã bao phủ toàn bộ không gian; tính hoàn chỉnh của câu trả lời được đo bằng một đối lập hai phần.
- **Failure:** câu trả lời ngầm bám khung giải thích của người dùng, chỉ đưa ít hay nhiều hai hướng, bỏ các đường khả thi khác và trở nên ngắn hơn dù nhiệm vụ cần phân tích rộng hơn.
- **Bằng chứng:** người dùng báo cáo regression ở biến thể tiền phát hành sau khi khối `EXPLANATION` bị nén. Audit câu chữ xác nhận bản đó bỏ `understand`, `non-trivial`, phản ví dụ và điều kiện `without removing needed support`, đồng thời cho model dừng theo đánh giá relevance của chính nó.
- **Control v8.2 chính thức:** khôi phục sàn chiều sâu trước regression và điều kiện không được bỏ hỗ trợ cần thiết. G-04 dùng bằng chứng hoặc phản ví dụ để kiểm tra độ bao phủ; khung của người dùng hay một cặp đẹp không mặc định là đầy đủ, còn relevance thay vì số lượng cố định quyết định phạm vi.
- **Rủi ro còn lại:** kiểm tra độ bao phủ có thể gây phản biện hoặc liệt kê thừa nếu model coi mọi khả năng là khác biệt; I-01 và tiêu chí relevance phải giữ nó cục bộ theo nhiệm vụ. Người dùng đã xác nhận bản cuối ổn định trong kiểm thử hiện tại.
- **Phép thử:** dùng ba vấn đề lần lượt có một, hai và ít nhất bốn hướng khả thi, cộng một trường hợp khung ban đầu của người dùng bỏ sót nguyên nhân. Câu trả lời phải giữ đúng số hướng có ý nghĩa, không mặc định hai và không vét cạn phương án không liên quan.

### FM-27 — Phát hiện phụ tự cấp quyền mở rộng nhiệm vụ

- **Trigger:** trong khi trả lời đúng yêu cầu, model phát hiện một premise thiếu, hệ quả, phản ví dụ, lỗ trống hoặc hướng tiếp cận liên quan.
- **Diễn giải sai:** vì phát hiện hữu ích hoặc nhánh còn chưa giải quyết, model được quyền biến nó thành đề xuất, bước tiếp theo, kế hoạch, chuyển giai đoạn hoặc hành động mới.
- **Failure:** câu trả lời vẫn có thể đúng về nội dung nhưng tự đi trước người dùng, nâng phát hiện phụ thành hướng chính hoặc công việc nối tiếp chưa được yêu cầu.
- **Bằng chứng:** người dùng báo cáo hành vi trên GPT-5.6. Audit câu chữ xác nhận v8.6–v8.8 cho phép đề xuất tối đa ba bước tiếp theo cho nhánh chưa giải quyết; đây là permission trong contract, nhưng không chứng minh nguyên nhân nội bộ duy nhất.
- **Control v8.9:** G-01 cho phép giải thích hệ quả vật chất nhưng nêu rõ phát hiện tự nó không mở rộng nhiệm vụ, đổi giai đoạn hoặc cho phép công việc nối tiếp. I-03 vẫn quản lý căn cứ đổi trạng thái; I-01 giữ chức năng lượt nói; G-04 bảo toàn quyền phát hiện và giải thích phần thiếu có ảnh hưởng vật chất.
- **Rủi ro còn lại:** model có thể đọc quá chặt và cắt mất hệ quả cần thiết, hoặc đọc quá rộng rồi gọi lời khuyên là “giải thích”. Phải thử cả hai hướng: chủ động vượt quyền và co hẹp suy luận.
- **Phép thử:** giữ cùng một material gap dưới ba yêu cầu: chỉ phân tích, đề xuất thiết kế, và triển khai. Cả ba được nêu gap; chỉ hai yêu cầu sau mới được mở proposal hoặc hành động tương ứng. Thêm một phát hiện phụ không material để kiểm tra nó không chiếm câu trả lời.

## 5. Quan hệ nhiều-nhiều giữa control và failure

Một rule hiếm khi chỉ chặn một failure. Khi sửa hoặc rút gọn, phải kiểm tra toàn bộ tập phụ thuộc:

| Control hiện hành | Failure được kiểm soát trực tiếp | Failure có thể gây ra nếu viết quá cứng |
|---|---|---|
| I-03 CONTROL GROUNDING | FM-06, FM-12, FM-13, FM-15, FM-21, FM-22, FM-24, FM-25, FM-27 | quá cứng sẽ bỏ qua chuyển đổi hợp lệ hoặc dependency không được nói bằng đúng từ khóa |
| I-01 DISCOURSE FIDELITY | FM-13, FM-14, FM-15, FM-20, FM-23, FM-24, FM-25, FM-26, FM-27 | tiếp tục sai nhiệm vụ nếu chọn nhầm chức năng của lượt nói |
| I-02 EPISTEMIC NON-ESCALATION | FM-06, FM-10, FM-12, FM-17, FM-24 | điều kiện hóa quá mức nếu mọi phát biểu đều bị coi là claim trọng yếu |
| G-01 TURN AND STATE | FM-13, FM-14, FM-15, FM-20, FM-21, FM-24, FM-25, FM-27 | giữ hoặc đổi mode sai, hỏi lại quá mức, cắt mất hệ quả cần thiết hoặc suy chức năng từ tín hiệu yếu |
| G-02 CLAIM DEPENDENCY | FM-06, FM-07, FM-08, FM-09, FM-13, FM-17 | fact-check trải nghiệm cá nhân hoặc biến mọi mode thành Audit |
| G-03 UPDATING AND UNCERTAINTY | FM-10, FM-11, FM-12, FM-16, FM-24 | gắn nhãn mọi mệnh đề hoặc liệt kê khả năng không đáng kể |
| G-04 EXPLANATION | FM-05, FM-18, FM-26 | over-explanation, cấu trúc hóa quá mức, phản biện khung người dùng không cần thiết hoặc tăng thuật ngữ để tạo vẻ sâu |
| G-05 LANGUAGE | FM-03, FM-04, FM-05, FM-21, FM-22; gián tiếp FM-01/FM-02 | dịch hỏng định danh nếu quá cứng; jargon tăng nếu ngoại lệ hoặc mức trần bị hiểu quá rộng |

Hệ quả thiết kế: không được xóa hoặc ghép rule chỉ dựa trên việc hai đoạn văn “nói gần giống nhau”. Phải so sánh tập failure mà chúng chặn, điều kiện kích hoạt, thứ tự ưu tiên và tác dụng phụ.

## 6. Cách quản lý phiên bản và ngân sách ký tự

### 6.1. Plus+ Era

- Là bản đặc tả đầy đủ và nơi phát triển triết lý trước.
- Ưu tiên độ bao phủ failure và quan hệ giữa rule.
- Một thay đổi tốt phải giữ bất biến, không tạo guardrail saturation và có phép thử hồi quy.
- v8.0 là baseline lịch sử đã được người dùng chấp nhận sau hiệu chỉnh ngôn ngữ: hai bất biến reasoning, ngoại lệ giữ nguyên hẹp và tối đa hai thuật ngữ chuyên biệt mới mỗi câu trả lời.
- v8.0.1 bắt đầu là biến thể tăng trần từ hai lên bốn, sau đó thử đếm toàn bộ thuật ngữ khác nhau. Người dùng quan sát cả việc lách trần theo miền và mức jargon tăng nghiêm trọng hơn sau khi siết cách đếm; biến thể này bị bác bỏ.
- v8.1 là bản vá hành vi lớn: bỏ quota thuật ngữ khỏi runtime CI, chuyển số đếm thành thước đo kiểm thử bên ngoài, điều khiển trực tiếp việc dùng/không xếp chồng thuật ngữ và chặn xác nhận “Đúng” sai vai trò phát ngôn.
- v8.1.1 là nhánh thử nghiệm bốn dòng: cổng nhận premise ở G-01/G-02/G-03 cho FM-06/FM-12/FM-23 và code-switching cấp mệnh đề ở G-05 cho FM-03/FM-05/FM-21. Các phần reasoning khác của v8.1 được giữ nguyên; FM-07/FM-13/FM-15 là ca hồi quy bắt buộc.
- v8.2 chính thức thay kiến trúc bất biến sau khi audit cho thấy v8.1.1 vẫn đặt việc phân loại bằng chứng/premise/bất định quá sớm. `CONTROL GROUNDING` đứng trước `DISCOURSE FIDELITY` và `EPISTEMIC NON-ESCALATION`: căn cứ hợp lệ cho phép đổi trạng thái, chức năng lượt nói chọn operation, rồi trạng thái mệnh đề mới được quản lý. Độ mạch lạc hoặc cảm giác hữu ích không tự cấp quyền tổng hợp; FM-23 trở thành rủi ro chấp nhận.
- Trong chuỗi tiền phát hành, rule ngôn ngữ bỏ điều kiện cấu trúc chủ thể để khôi phục baseline thuật ngữ tiếng Việt v7.3. Một lần nén `EXPLANATION` nhằm chống khung hai phần gây regression về chiều sâu và bám khung người dùng; bản chính thức khôi phục sàn cũ rồi thay đúng một câu bằng kiểm tra độ bao phủ. Người dùng xác nhận kết quả cuối ổn định.
- v8.5 đưa tiếng Việt thành hợp đồng đầu ra; v8.6–v8.7 siết claim dependency, grounding và mô hình người đọc; v8.8 thử tiếng Việt tuyệt đối không ngoại lệ.
- v8.9 là mốc Plus hiện hành. Bản này giữ ba invariant, khôi phục ngoại lệ dạng chữ chính xác hẹp, cấm agreement chỉ làm dấu nối, bảo toàn nghĩa khi rephrase đồng thời thực hiện chức năng mới, và thay permission bước tiếp theo bằng ranh giới giữa hệ quả vật chất với mở rộng nhiệm vụ/công việc nối tiếp.

### 6.2. ChatGPT Go-Free Era

- Là profile triển khai cô đọng do giới hạn ký tự của paid plan, không phải file lạ hay nhánh thiết kế cạnh tranh.
- Bản rút gọn phải được chưng cất từ bản Plus+ đã ổn định.
- v6.3 được thiết kế từ v7.3 để đường quay về Free/Go không bị kéo xuống các thiếu sót của v6.2; v6.4 tiếp tục logic chưng cất từ v7.4.1.
- v6.4.1 chưng cất lõi reasoning và depth của v7.4.2, hạ hai bất biến ngôn ngữ cũ thành bảo vệ mềm để dành ngân sách 1.500 ký tự cho suy luận.
- v6.6 là profile Go/Free hiện hành trong cây nguồn: giữ kernel 1.499 ký tự quanh tín hiệu đổi giai đoạn, chức năng lượt, trạng thái claim, chiều sâu và tiếng Việt. Parity với v8.9 chưa được chứng minh bằng runtime.
- Thành công được đo bằng semantic coverage trên failure matrix, không phải tỷ lệ câu chữ được giữ.

### 6.3. Phân biệt bốn loại thay đổi

1. **Successful compression:** ít ký tự hơn nhưng vẫn chặn cùng failure trong phép thử đại diện.
2. **Dependency on model defaults:** rule mất nhưng output mẫu tình cờ vẫn tốt; đây chưa phải bằng chứng tương đương.
3. **Confirmed wording regression:** điều kiện hoặc safeguard biến mất khỏi CI, như depth floor ở v7.4.1.
4. **Intentional semantic change:** bảo đảm bị bỏ có lý do rõ và giới hạn còn lại được ghi nhận, như CONTEXT ở v7.4.1.

## 7. Quy trình audit cho LLM khác

Khi đánh giá một CI hoặc đề xuất sửa đổi, thực hiện theo thứ tự sau:

```yaml
audit_protocol:
  step_1: identify_target_profile_and_character_budget
  step_2: extract_invariants_and_priority_order
  step_3: normalize_rules_by_semantics_not_headings
  step_4: map_each_rule_to_failure_modes
  step_5: compare_trigger_conditions_and_exceptions
  step_6: trace_wording_to_interpretation_to_failure_path
  step_7: classify_change_as_compression_regression_or_tradeoff
  step_8: run_representative_and_adversarial_tests
  step_9: inspect_cross_rule_side_effects
  step_10: verify_character_count_encoding_and_line_endings
```

Không đề xuất patch chỉ vì một rule bị mất tên. Một khái niệm có thể đã được ghép mà vẫn giữ đủ ngữ nghĩa. Ngược lại, không kết luận “đã giữ” chỉ vì còn từ khóa; điều kiện kích hoạt, ngoại lệ và thứ bậc có thể đã biến mất.

Để quy một thay đổi câu chữ thành nguyên nhân của hành vi, dùng kiểm thử A/B có kiểm soát:

- cùng model và mức reasoning;
- cùng personalization/memory ngoài CI;
- cùng prompt và thứ tự hội thoại;
- chỉ thay CI;
- đánh giá bằng tiêu chí failure cụ thể, không dựa riêng vào độ dài hoặc cảm giác.

## 8. Bộ thử hồi quy tối thiểu

| Nhóm test | Failure mục tiêu |
|---|---|
| Chat tự nhiên bằng tiếng Việt | FM-01, FM-02, FM-15 |
| Thuật ngữ có/không có bản dịch ngang nghĩa | FM-03, FM-04, FM-05 |
| Mật độ jargon ở câu ngắn/dài và miền kỹ thuật/worldbuilding | FM-03, FM-05, FM-21, FM-22 |
| Người dùng biết vài từ nhưng không toàn miền | FM-21 |
| Claim khách quan đúng, sai và chưa chắc | FM-06, FM-10, FM-11 |
| Cùng nội dung dưới dạng câu hỏi/yêu cầu/báo cáo/sở thích/mệnh đề | FM-07, FM-23 |
| Ý kiến và quan sát ngôi thứ nhất | FM-07 |
| Phản đối không có dữ kiện mới | FM-12, FM-20 |
| Premise được sửa bằng bằng chứng mới | FM-12 |
| Tính năng sản phẩm/runtime hiện hành | FM-08, FM-09 |
| Advise/Inform có chứa claim phụ | FM-13 |
| Hai loại mơ hồ: nhỏ và có hệ quả | FM-14 |
| Suy luận về động cơ hoặc danh tính | FM-16 |
| Worldbuilding/hệ thống do người dùng định nghĩa | FM-17 |
| Phân tích phi kỹ thuật nhiều bước | FM-18 |
| Context giữa các chat với memory bật/tắt | FM-19 |
| Một chủ đề chạy qua Chat, Audit và Create | FM-15, FM-20 |
| Người dùng đổi rõ giai đoạn: audit → sửa → thử | FM-13, FM-15, FM-20 |
| Một, hai và nhiều hơn hai nguyên nhân/giải pháp; khung người dùng thiếu | FM-26 |
| Bổ sung ngữ cảnh và rephrase có thêm chức năng mới | FM-23, FM-24 |
| Phát hiện material gap dưới yêu cầu phân tích/proposal/implementation | FM-25, FM-27 |
| Phát hiện phụ hữu ích nhưng không material | FM-15, FM-27 |

Một phiên bản chỉ đạt khi không xuất hiện failure bắt buộc, không làm suy yếu bất biến và không tạo hồi quy đáng kể ở mode khác.

## 9. Khoảng trống đang biết

### 9.1. Depth floor của v7.4.1 — đã đóng

v7.4.1 đã mất bảo đảm chiều sâu chung và tạo hồi quy rõ hơn ở chat phi kỹ thuật theo A/B do người dùng thực hiện. v7.4.2 khôi phục DEPTH xuyên miền; v7.5 và v8 tiếp tục bảo vệ bằng yêu cầu giải thích đủ để kết luận không tầm thường có thể được kiểm tra. Khoảng trống này đã đóng ở câu chữ, nhưng vẫn là ca hồi quy bắt buộc khi nén CI.

### 9.2. Context isolation

Không có rule CONTEXT trong v7.4.1 là quyết định có chủ đích vì CI không thể bảo đảm triệt để hành vi memory của nền tảng. Với dữ liệu nhạy cảm hoặc nhiệm vụ cần cô lập, phải quản lý phạm vi ở cấp phiên làm việc và kiểm chứng runtime, không coi sự vắng mặt của rò rỉ trong vài mẫu là bảo đảm.

### 9.3. Bằng chứng hành vi

Audit văn bản có thể xác nhận rule tồn tại, mất đi, xung đột hoặc đổi điều kiện. Nó không tự chứng minh model sẽ tuân thủ. Mọi kết luận về hành vi cần lưu model, cấu hình, prompt, output và tiêu chí chấm để tái lập.

### 9.4. Lớp hành vi ngoài CI

Web và Codex đã cho tone và mật độ jargon khác nhau trong quan sát của người dùng. Điều này phù hợp với khả năng có nhiều lớp cùng tác động, nhưng không đủ để xác định system prompt, personality, memory, model hay lịch sử hội thoại là nguyên nhân. Tự mô tả của model sau khi bị red-team không phải bằng chứng nội quan. Cần tách từng biến bằng hội thoại mới và cấu hình được giữ cố định.

### 9.5. Ngân sách thuật ngữ — cơ chế đã bị bác bỏ

Mức trần hai/bốn thuật ngữ không hoạt động như bộ đếm tất định. Ranh giới “thuật ngữ”, “mới”, “tái sử dụng”, “quen trong miền” và “định danh” bị phân đoạn không ổn định; số đếm còn có thể trở thành quota hoặc mục tiêu nén. Người dùng báo cáo trần bị bỏ qua theo miền và bản đếm chặt hơn trong v8.0.1 làm jargon dày hơn rõ rệt. v8.1 vì vậy bỏ số đếm khỏi runtime CI; số lượng và mật độ chỉ còn là tiêu chí đánh giá đầu ra bên ngoài.

### 9.6. Nhận ngữ cảnh thành premise — v8.1.1 tái cấu trúc cổng bằng chứng

Control v8.1 nêu trực tiếp “Đúng” và vẫn cho phép dùng khi model tự đánh giá là hữu ích; hành vi tiếp tục lặp lại. Bản v8.1.1 đầu tiên chuyển sang “cập nhật im lặng” nhưng cụm này vẫn có thể cho claim khách quan vào nền suy luận trước khi kiểm tra, trong khi G-02 yêu cầu kiểm chứng claim trọng yếu. Bản hiện hành tách hai việc: phần bổ sung chỉ là ngữ cảnh; trước khi claim khách quan được dùng làm premise trọng yếu, phải đối chiếu với nguồn gốc hoặc bằng chứng độc lập. Claim và sự lặp lại không phải bằng chứng; chỉ sự thật có hỗ trợ, giả định tường minh có phạm vi hoặc sửa đổi có hỗ trợ mới cập nhật nền suy luận. Việc đối chiếu phải cục bộ để không tạo FM-07/FM-13/FM-15. Kết quả runtime chưa được xác nhận.

### 9.7. Code-switching cấp mệnh đề — hai control trước thất bại, v8.1.1 đang thử lại

G-05 của v8.1 dùng các ngưỡng do model tự đánh giá như “nhiệm vụ cần”, “tăng độ chính xác” và “khi cần”, nên vẫn cho hàng loạt nhãn tiếng Anh đi qua khi chủ đề mang vẻ chuyên môn. Bản tiếp theo yêu cầu nghĩa tiếng Việt đi trước và không để đoạn văn phụ thuộc tra cứu ngoài, nhưng người dùng báo cáo kết quả vẫn “rất không ổn”; control này cũng được tính là thất bại hành vi, không phải cải thiện đã chứng minh. Tự mô tả của chat rằng nó suy vốn từ từ lịch sử “sử dụng ngôn ngữ khoa học máy tính” không phải bằng chứng nội quan, nhưng phù hợp với hiệu ứng FM-21 đã quan sát. Bản hiện hành chuyển sang ranh giới cú pháp dễ nhận hơn: mỗi mệnh đề phải là tiếng Việt hoàn chỉnh; tiếng Việt không được làm khung nối quanh từ mang nghĩa, danh sách nhãn hoặc công thức tiếng Anh; mọi phần tiếng Anh mang nghĩa phải dịch. Chỉ dạng chữ buộc phải sao chép chính xác mới được giữ, việc từng dùng không phải yêu cầu giữ ở lượt hiện tại, và nhãn được phép phải đứng sau phần giải thích tiếng Việt hoàn chỉnh chứ không được gánh phần giải thích. Hiệu lực runtime chưa được xác nhận.

### 9.8. Miền quá rộng của `REASONING INTEGRITY` — tiền đề cho kiến trúc v8.2

Người dùng nhận ra failure lặp lại có thể liên quan tới xu hướng tạo một câu trả lời khép kín: lượt bổ sung dễ bị biến thành mệnh đề cần đồng ý, chia đúng/sai hoặc phản bác. Đây là giả thuyết về cơ chế mô hình, không phải bằng chứng nội quan. Tuy nhiên, audit câu chữ xác nhận `REASONING INTEGRITY: Match conclusions to evidence, premises, and uncertainty` có thể kích hoạt trên gần như mọi câu trả lời, trong khi G-01–G-03 tiếp tục yêu cầu phân loại premise, bằng chứng và bất định. Cấu trúc này không tách việc “người dùng đang làm gì” khỏi việc “mệnh đề đúng tới đâu” và tạo nguy cơ bão hòa control. Kiến trúc v8.2 tách căn cứ kích hoạt, hành vi hội thoại và trạng thái đúng–sai thành ba bất biến có thứ tự; dependency trọng yếu hoặc yêu cầu đánh giá rõ mới kích hoạt kiểm chứng.

### 9.9. Control tự tạo trigger — giả thuyết gốc chung của v8.x và kiến trúc v8.2

Khi bỏ qua FM-23, nhiều failure v8.x có cùng một điều kiện cho phép ở cấp kiến trúc: rule phải tự suy từ tín hiệu ngữ nghĩa rằng chính nó nên kích hoạt hoặc đổi trạng thái. Chủ đề kỹ thuật có thể tự mở ngoại lệ jargon; một claim có thể tự kích hoạt Audit; độ mạch lạc có thể tự chuyển khám phá thành tổng hợp; sự quen thuộc biểu kiến có thể tự nâng vốn từ giả định. Đây là **nguyên nhân cho phép chung**, không chứng minh mọi hành vi có cùng nguyên nhân nội bộ duy nhất.

v8.2 đưa quyền thay đổi lên `CONTROL GROUNDING`: chỉ tín hiệu rõ của người dùng, bằng chứng mới hoặc dependency thật của operation đã yêu cầu mới cho phép đổi giai đoạn, operation, trạng thái claim hay giả định về người đọc. Sau đó `DISCOURSE FIDELITY` chọn hành vi và `EPISTEMIC NON-ESCALATION` quản lý đúng–sai. Người dùng xác nhận bản chính thức ổn định trong kiểm thử hiện tại; điều đó không loại bỏ nhu cầu kiểm tra lại khi model hoặc lớp sản phẩm thay đổi.

### 9.10. Khung hai phần và sàn chiều sâu — regression tiền phát hành đã sửa

Một biến thể tiền phát hành cố thêm độ rộng bằng cách viết lại toàn bộ `EXPLANATION`, nhưng đồng thời bỏ yêu cầu đủ để `understand`, bỏ điều kiện `non-trivial`, bỏ phản ví dụ và xóa bảo vệ `without removing needed support`. Người dùng ghi nhận câu trả lời ngắn hơn và bám khung giải thích của họ. Bản chính thức quay về sàn chiều sâu trước regression và chỉ thay câu lựa chọn bằng chứng: dùng bằng chứng hoặc phản ví dụ để kiểm tra độ bao phủ; khung của người dùng hay một cặp đẹp không mặc định là đầy đủ; relevance chứ không phải số lượng cố định đặt phạm vi. Người dùng xác nhận bản sửa ổn định trong phạm vi thử hiện tại.

### 9.11. Đồng ý theo mạch hội thoại và phát hiện tự mở việc — sửa contract ở v8.9

Hai failure bề mặt có chủ sở hữu khác nhau nhưng có thể nối tiếp nhau. FM-23/FM-24 xảy ra khi model đọc một rephrase hoặc bổ sung ngữ cảnh thành yêu cầu đồng ý, sửa sai hay phán quyết. FM-27 xảy ra khi một phát hiện phụ được coi là quyền tự đổi giai đoạn hoặc mở công việc tiếp theo. v8.9 sửa cả hai trong ba bất biến hiện có: `DISCOURSE FIDELITY` giữ nguyên nghĩa của rephrase và thực hiện chức năng được thêm; `CONTROL GROUNDING` cùng `TURN AND STATE` cấm phát hiện tự cấp quyền mở rộng nhiệm vụ. Đây là bằng chứng ở cấp contract; hiệu lực runtime của bản chính thức chưa được xác nhận bằng bộ thử có kiểm soát.

## 10. Nguồn nội bộ để truy vết

- [CI_VERSIONING_AUDIT_VI.md](./CI_VERSIONING_AUDIT_VI.md): rule taxonomy, lịch sử version và các regression đã xác nhận.
- [CI_DESIGN_EVOLUTION_AND_DEPLOYMENT_VI.md](./CI_DESIGN_EVOLUTION_AND_DEPLOYMENT_VI.md): triết lý tiến hóa, hai profile triển khai và quy trình kiểm thử.
- [CHANGELOG_VI.md](../instruction-history/CHANGELOG_VI.md): lịch sử thay đổi đến v8.9 chính thức.
- [chatgpt v8.0.txt](../../llm-controls/global-instructions/ChatGPT%20Plus+%20Era/chatgpt%20v8.0.txt): baseline Plus+ lịch sử đã được người dùng chấp nhận.
- [chatgpt v8.0.1.txt](../../llm-controls/global-instructions/ChatGPT%20Plus+%20Era/chatgpt%20v8.0.1.txt): biến thể số lượng thất bại, gồm lần tăng lên bốn và lần siết đếm toàn bộ thuật ngữ.
- [chatgpt v8.1.txt](../../llm-controls/global-instructions/ChatGPT%20Plus+%20Era/chatgpt%20v8.1.txt): bản vá bỏ quota runtime và chặn xác nhận chung sai vai trò phát ngôn.
- [chatgpt v8.1.1.txt](../../llm-controls/global-instructions/ChatGPT%20Plus+%20Era/chatgpt%20v8.1.1.txt): nhánh thử nghiệm cổng nhận premise, cập nhật nền suy luận và code-switching cấp mệnh đề.
- [chatgpt v8.2.txt](../../llm-controls/global-instructions/ChatGPT%20Plus+%20Era/chatgpt%20v8.2.txt): bản Plus+ chính thức ba bất biến với nền tiếng Việt, cổng giữ giai đoạn và kiểm tra độ bao phủ giải thích.
- [chatgpt v8.9.txt](../../llm-controls/global-instructions/ChatGPT%20Plus+%20Era/chatgpt%20v8.9.txt): bản Plus+ hiện hành với contract rephrase, ranh giới quyền mở việc và ba bất biến đã hiệu chỉnh.
- [chatgpt v6.6.txt](../../llm-controls/global-instructions/ChatGPT%20Go-Free%20Era/chatgpt%20v6.6.txt): profile reasoning cô đọng hiện hành cho Free/Go; parity với v8.9 chưa được chứng minh.
- [chatgpt v7.4.2.txt](../../llm-controls/global-instructions/ChatGPT%20Plus+%20Era/chatgpt%20v7.4.2.txt): mốc khôi phục depth floor.

## 11. Tóm tắt máy đọc được

```yaml
design_philosophy:
  primary_goal: behavioral_compatibility
  top_invariants:
    - control_grounding
    - discourse_fidelity
    - epistemic_non_escalation
  invariant_order: authorize_state_change_then_choose_operation_then_govern_truth_status
  grounding_policy:
    valid_state_change_sources:
      - explicit_user_signal
      - new_evidence
      - requested_operation_dependency
    invalid_triggers:
      - topic
      - terminology
      - repetition
      - coherence
      - familiarity
      - perceived_usefulness
    default: preserve_state
  routing_policy: explicit_request_then_stated_activity_then_ongoing_objective_then_smallest_continuation
  default_for_continuation: continue_without_verdict
  stage_policy:
    exploration_and_accumulation: provisional
    synthesis_transition: explicit_request_or_operation_requirement
  guardrail_policy: conditional_after_operation_selection
  evidence_policy: verify_only_explicit_judgment_or_material_claim_dependency
  update_policy: conclusions_change_with_relevant_evidence_not_pressure
  uncertainty_policy:
    interaction_ambiguity: use_continuation_rule
    proposition_uncertainty: expose_only_when_it_changes_conclusion_or_action
  depth_policy: proportional_explanation_without_padding
  language_policy:
    baseline: vietnamese_by_default
    reader_model: do_not_infer_vocabulary_from_subject_or_archetype
    narrow_exceptions:
      - proper_name
      - code
      - quote
      - command
      - identifier
      - user_requested_term
    historical_numeric_controls:
      v8_0_new_term_ceiling: 2
      v8_0_1_experimental_ceiling: 4
    v8_1_runtime_numeric_ceiling_removed: true
    v8_1_policy: minimum_required_terms_no_clustering
    v8_1_1_policy: complete_vietnamese_clauses_no_english_semantic_scaffolding
    v8_2_policy: vietnamese_baseline_without_subject_structure_rule
    prior_term_use_is_retention_request: false
    allowed_exact_english_carries_explanation: false
  premise_admission_policy:
    material_objective_claim: compare_with_underlying_source_or_independent_evidence
    claim_or_repetition_is_evidence: false
    working_basis_updates_from:
      - supported_fact
      - explicit_scoped_assumption
      - supported_correction
  stance_policy:
    stance_only_for_propositions: true
    v8_1_literal_affirmation_guard: failed_runtime
    v8_1_1_opening_policy: context_is_not_automatically_a_confirmed_premise
    v8_2_policy: statement_is_not_a_request_for_agreement_judgment_summary_or_closure
    generic_affirmation_preamble: accepted_residual_in_v8_2
  explanation_policy:
    depth_floor: preserve_needed_support_for_non_trivial_conclusions
    coverage_check: evidence_or_counterexamples
    user_frame_or_neat_pair_is_exhaustive_by_default: false
    scope_boundary: relevance_not_fixed_count
  deployment_policy:
    plus: full_specification
    go_free: semantic_distillation_under_character_budget
  platform_boundary:
    memory_is_not_a_deterministic_CI_rule_engine: true
resolved_gap:
  id: FM-18
  issue: missing_general_depth_floor_in_v7_4_1
  resolved_from: v7.4.2
confirmed_regression:
  id: FM-22
  version: v8.0.1
  issue: numeric_terminology_control_increased_or_failed_to_bound_jargon
  status: user_reported_behavior
historical_behavioral_validation:
  version: v8.2
  reported_status: user_confirmed_stable_in_current_test
  targets:
    - FM-03
    - FM-05
    - FM-06
    - FM-12
    - FM-21
current_plus_release:
  version: v8.9
  verification: static_contract_review_only
  runtime_status: unverified
  discourse_policy:
    continuity_agreement: prohibited
    rephrase_same_meaning: preserve_meaning_and_perform_added_function
  follow_on_policy:
    material_implications: allowed
    finding_alone_authorizes_task_expansion: false
current_go_free_release:
  version: v6.6
  parity_with_v8_9: unverified
    - FM-24
    - FM-25
    - FM-26
  regression_checks:
    - FM-04
    - FM-07
    - FM-13
    - FM-15
    - FM-18
    - FM-22
intentional_omission:
  id: FM-19
  rule: CONTEXT
  reason: cannot_guarantee_platform_memory_isolation_through_CI
acceptance_rule:
  - preserve_control_grounding_discourse_fidelity_and_epistemic_non_escalation
  - block_mapped_failure_modes
  - avoid_cross_mode_side_effects
  - preserve_reader_comprehension_without_corrupting_identifiers
  - distinguish_wording_evidence_from_behavioral_evidence
```
