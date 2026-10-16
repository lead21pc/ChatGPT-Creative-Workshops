# Cơ sở thiết kế ChatGPT Project Global Native

## 1. Mục đích và phạm vi

Tài liệu này giải thích vì sao dòng ChatGPT Project Global Native được tạo, trách nhiệm nào cần được bảo toàn và khi nào một mở rộng kiến trúc thực sự cần thiết. Đối tượng đọc là người bảo trì và các phiên Codex/LLM tạo hoặc thiết kế lại CI, Router hay thành phần kiểm soát liên quan.

Đây là tài liệu tham chiếu thiết kế bắt buộc theo `AGENTS.md` ở root, không phải một CI chạy trong ChatGPT, một tầng định tuyến hay một bộ kiểm tra tự động. Nội dung giải thích lựa chọn thiết kế; tệp CI hiện tại cho biết câu chữ thực sự được đặc tả. Chỉ dẫn hiện tại của người dùng, kiến trúc mới hơn đã được chấp thuận, trạng thái repository thực tế và các kiểm soát có ưu tiên cao hơn không bị tài liệu này ghi đè.

```text
MORE CAPACITY != MORE POLICY
DECOMPRESSION BEFORE EXTENSION
AVAILABLE SPACE != REQUIRED COMPLEXITY
```

## 2. Ranh giới thế hệ đến v9.0

Ba mốc có vai trò khác nhau:

| Mốc | Môi trường thiết kế | Ý nghĩa |
| --- | --- | --- |
| v6.2 | Go/Free, ngân sách hẹp khoảng 1.500 ký tự | Về thực chất là thế hệ nguyên bản cuối của kiến trúc nhỏ trước khi các bản sau tiếp nhận chưng cất từ kiến trúc lớn hơn |
| v8.9 | Plus normal-chat, ngân sách khoảng 5.000 ký tự | Điểm trưởng thành của dòng Plus nén sát giới hạn, với ba bất biến có trách nhiệm riêng |
| v9.0 | Project, ngân sách thiết kế dưới 8.000 ký tự | Khởi đầu dòng Project-native, dùng dung lượng để làm rõ những phân biệt vốn bị nén |

Lịch sử ghi nhận v6.3 converted được chưng cất từ v7.3. Vì vậy, số phiên bản không tự xác định thứ tự thời gian, nguồn gốc ngữ nghĩa hay môi trường triển khai. v8.9 vẫn là baseline Plus normal-chat; v9.0 mở một dòng triển khai song song, không làm cho v8.9 tự động mất hiệu lực.

Ranh giới mới đến từ môi trường triển khai và khả năng diễn đạt điều kiện rõ hơn:

```text
normal-chat khoảng 5k → cần nén nhiều trách nhiệm liên quan
Project với ngân sách lớn hơn → có thể giải nén các phân biệt quan trọng
                              → không phát sinh nghĩa vụ thêm chính sách
```

Các ngân sách trên là bối cảnh thiết kế do tác giả xác định. 8.000 là trần, không phải mục tiêu phải lấp đầy. Một số phiên bản lớn hơn không tự tạo lý do để thay kiến trúc, đổi thuật ngữ hoặc viết lại quy tắc đang phù hợp. Mục tiêu không phải tối đa hóa độ phủ bằng mọi giá.

## 3. Điều v8.9 làm đúng: trách nhiệm có chủ sở hữu

Điểm cần giữ là loại quyết định mà từng phần quản lý, không phải tính bất biến của tiêu đề hay cách chia đoạn.

| Thành phần | Quyết định sở hữu | Ranh giới cần giữ |
| --- | --- | --- |
| `OUTPUT CONTRACT` | Ngôn ngữ và cách diễn đạt đầu ra | Giữ tiếng Việt phổ thông, ngoại lệ dạng chữ chính xác hẹp và chiều sâu nội dung |
| `CONTROL GROUNDING` | Căn cứ cho đổi trạng thái, giả định về giai đoạn/người đọc và thẩm quyền của khung ngữ cảnh | Không chọn thao tác thay cho discourse và không tiếp quản kiểm chứng sự thật |
| `DISCOURSE FIDELITY` | Chức năng lượt nói: tiếp tục, yêu cầu, diễn đạt lại, sửa đổi và phần đánh giá cần thiết | Không dùng đồng ý để nối hội thoại; diễn đạt lại chỉ là sửa đổi khi nghĩa thay đổi |
| `EPISTEMIC NON-ESCALATION` | Mức kết luận được bằng chứng cho phép; quan sát, suy luận và giả định có phạm vi | Sự lặp lại hay phù hợp ngữ cảnh không làm tăng căn cứ |
| `TURN AND STATE` | Thao tác, giai đoạn, khám phá, mơ hồ, phạm vi hành động và dừng | Phát hiện không tự mở việc; giữ trạng thái không có nghĩa bỏ qua yêu cầu chuyển giai đoạn hợp lệ |
| `CLAIM DEPENDENCY` ở v8.9; `CLAIM STATE AND DEPENDENCY` ở v9.0 | Trạng thái phát biểu, cách sử dụng, xác nhận và điều kiện kiểm chứng; v9.0 nói rõ thêm báo cáo hành động | Ghi nhận hoặc dùng có điều kiện không xác lập sự thật; báo cáo cá nhân không tự thành mục tiêu kiểm chứng |
| `UPDATING AND UNCERTAINTY` | Cập nhật căn cứ, lan truyền đến kết luận phụ thuộc và bất định có hệ quả | Không biến mơ hồ về thao tác thành tranh luận đúng–sai; không suy hồ sơ rộng của người dùng |
| `EXPLANATION` | Hỗ trợ giải thích đủ để hiểu và đánh giá kết luận | Không cắt mất căn cứ cần thiết, áp số lượng mục cố định hoặc biến mọi trả lời thành báo cáo |

Thứ tự `grounding → discourse → epistemic` biểu thị quan hệ ràng buộc: cần căn cứ cho đổi trạng thái, chọn đúng thao tác rồi kết luận trong giới hạn hỗ trợ. Nó không phải mẫu ba bước phải xuất hiện trong đầu ra. Không kiểm soát nào được tự cấp quyền thông qua chính tín hiệu nó kiểm soát.

Các đoạn triển khai cụ thể hóa bất biến; chúng không phải các trung tâm quyền hạn cạnh tranh. Ví dụ, `TURN AND STATE` triển khai thao tác/phạm vi, còn `CLAIM STATE AND DEPENDENCY` triển khai cách đánh giá phát biểu được thao tác đó cần đến. Có phát biểu khách quan trong đầu vào không đồng nghĩa toàn bộ lượt phải chuyển sang kiểm toán.

## 4. Giải nén thay vì tạo thêm chủ sở hữu

v8.9 đặt nhiều điều kiện trong những đoạn rất ngắn. Đây là áp lực biểu đạt có thể thấy trong hiện vật gần 5k; không có nghĩa mọi câu ngắn đều sai hoặc mọi trách nhiệm gần nhau đều cần tách mô-đun.

v9.0 dùng thêm không gian ở các điểm sau:

| Phân biệt cần nói rõ | Vì sao hữu ích | Nơi tiếp tục sở hữu |
| --- | --- | --- |
| Chọn thao tác và giữ giai đoạn | Tránh hiểu giữ trạng thái thành mắc kẹt trong giai đoạn cũ | `TURN AND STATE` |
| Tiếp tục khám phá và chuyển sang tổng hợp theo yêu cầu | Độ mạch lạc không tự cho phép chốt; yêu cầu tổng hợp rõ lại là tín hiệu hợp lệ | `TURN AND STATE` |
| Trạng thái phát biểu, cách sử dụng và điều kiện kiểm chứng | Ngăn giả định thành sự thật mà không buộc tra cứu mọi đầu vào | `CLAIM STATE AND DEPENDENCY` |
| Đề xuất, mô phỏng, thử, kiểm tra và hoàn thành | Báo cáo hành động phải khớp sự kiện và mức thành công quan sát được | `CLAIM STATE AND DEPENDENCY` |
| Khác biệt thực tế và đánh đổi theo ưu tiên | So sánh phải phục vụ tiêu chí của yêu cầu, không áp một chính sách quyết định phổ quát | `TURN AND STATE` |

Quy tắc báo cáo hành động là bổ sung hẹp đã được duyệt, không phải một hệ thống thực thi mới. Nó không cấp quyền truy cập, khả năng chạy nền hay lưu giữ. Việc tích hợp so sánh cũng không tạo một `Decision Policy` cho mọi lượt.

Vì các chủ sở hữu hiện tại diễn đạt được những hành vi này, v9.0 không thêm lớp `NEUTRAL BEHAVIOR` hoặc các mục độc lập `Critical Independence`, `Execution Integrity`, `Choice / Comparison`. Dừng vẫn thuộc `TURN AND STATE`, không được tạo một quyền dừng thứ hai trong `EXPLANATION`.

## 5. Mẫu mở rộng gây lỗi và giới hạn bằng chứng

Khi yêu cầu tạo tài liệu này, tác giả báo cáo một mẫu lỗi lặp lại ở Project CI phát triển từ v8.9: dung lượng lớn hơn bị hiểu là chỗ để thêm chính sách, thay vì làm rõ trách nhiệm đã có. Báo cáo của tác giả là nguồn cho quan sát này; lượt khảo sát repository không tái hiện độc lập các lần mở rộng đó và không khẳng định mọi Project CI đều mắc lỗi.

```text
quy tắc toàn cục bị nén
→ chuyển sang nơi có nhiều ký tự hơn
→ coi phần dung lượng trống là nhu cầu thêm mục
→ viết lại trách nhiệm cũ dưới một tên mới
→ nhiều chủ sở hữu quyết định cùng một việc
→ thêm kiểm soát để xử lý sự chồng lấn
→ quản trị đệ quy / thiết kế quá mức
```

Các tên như Action Policy, Decision Policy, Evidence Policy, Source Policy, Planning Policy, Router hoặc anti-drift không tự chứng minh một trách nhiệm mới. Vấn đề xuất hiện khi nội dung thực tế của chúng tái tạo quyết định đã có chủ sở hữu. Một thành phần cùng tên vẫn có thể hợp lệ nếu nó giải quyết một trách nhiệm khác có căn cứ.

Từng quy tắc mới có thể trông hợp lý nhưng tổng thể kết hợp lại kém hơn: nhiều điều kiện kích hoạt cùng một quyết định, thứ tự áp dụng không rõ và mật độ ràng buộc tăng. Một quy tắc giữ giai đoạn có thể xung đột với quy tắc ép kiểm toán; một mục bằng chứng có thể bắt kiểm chứng cả đầu vào mà mục trạng thái coi là giả định cục bộ. Kết quả có thể là giữ giai đoạn quá lâu, phản biện sớm, kiểm chứng thừa hoặc thêm tầng phân xử để chữa tầng trước.

Các hệ quả này là rủi ro cấu trúc được suy ra từ cơ chế chồng lấn, không phải tất cả đã được đo trên v9.0. Tài liệu lịch sử riêng đã ghi nhận FM-13 (phát biểu ép chế độ kiểm toán), FM-20 (phản biện mặc định), FM-24 (nhập mơ hồ thao tác với bất định đúng–sai), FM-25 (tự chốt khi đang khám phá) và FM-27 (phát hiện phụ tự mở việc). Các ghi nhận đó hỗ trợ nhu cầu giữ ranh giới, không chứng minh dung lượng lớn hơn là nguyên nhân duy nhất.

## 6. Quy tắc trước khi thêm một thành phần

Trước khi thêm primitive, mục, chính sách, Router, anti-drift hoặc kiểm soát:

1. Nêu lỗi cụ thể hoặc yêu cầu chưa được đáp ứng; phân biệt nó với sở thích và giả thuyết.
2. Xác định quyết định đang bị ảnh hưởng và chủ sở hữu hiện tại.
3. Kiểm tra liệu làm rõ hoặc mở rộng cục bộ chủ sở hữu đó có giải quyết được vấn đề.
4. Chỉ thêm chủ sở hữu mới khi kiến trúc hiện có không thể diễn đạt hành vi cần thiết mà không ghép các trách nhiệm theo cách gây hại; giải thích vì sao sửa nhỏ hơn chưa đủ.

```text
NEW FAILURE → CHECK EXISTING OWNER → LOCAL EXTENSION → NEW PRIMITIVE ONLY IF REQUIRED
FORMAT CHANGE != ARCHITECTURE CHANGE
```

Đổi Markdown sang YAML, đổi tên tiêu đề hoặc tách một đoạn thành nhiều đoạn không tự tạo kiến trúc mới. Đánh giá phải theo đầu vào, quyết định và tác động thực tế. Không tạo thêm thành phần chống thiết kế quá mức chỉ để thực thi quy tắc này.

Chủ sở hữu hiện tại không phải bất khả thay thế. Nếu bằng chứng chỉ ra ranh giới hiện tại sai hoặc gây ghép trách nhiệm có hại, có thể chuyển trách nhiệm hoặc thiết kế lại trong phạm vi được phép. Khi thay đổi, cần chỉ rõ phần nào thay thế phần nào để tránh hai chủ sở hữu cùng tồn tại ngoài ý muốn.

## 7. Mở rộng theo lĩnh vực

Nền toàn cục quản lý hành vi chung; Project-specific CI có thể thêm trách nhiệm thực sự thuộc lĩnh vực như quy trình lập trình, xử lý canon/ontology, phương pháp nghiên cứu, sáng tạo phân kỳ hoặc cách dùng repository và công cụ chuyên biệt.

Một Project lập trình có thể quy định repository nào được sửa, kiểm thử nào cần chạy và điều kiện nghiệm thu. Việc có nhiệm vụ và hành động không tự biện minh cho một hệ thống kiểm soát phạm vi tổng quát thứ hai.

Một Project worldbuilding có thể xác định quyền quyết định canon, ontology và nguồn có thẩm quyền riêng. Nó chỉ mở rộng quy tắc trạng thái phát biểu khi mô hình sự thật hư cấu/cục bộ đòi hỏi một phân biệt mới, thay vì viết lại toàn bộ kỷ luật phát biểu chung.

Mở rộng nên nằm cạnh nền toàn cục với đầu vào và quyết định riêng. Không biến tên lĩnh vực thành lý do sao chép trách nhiệm. Các paracosm giữ độc lập; rationale này không áp ontology, nguồn có thẩm quyền hoặc Router của một thế giới cho thế giới khác.

## 8. Khi nào cần Router

Router phải giải quyết một vấn đề lựa chọn hoặc nạp cụ thể, không chỉ làm cho sơ đồ trông có tổ chức. Trước khi tạo, cần làm rõ:

- Lỗi định tuyến cụ thể là gì và vì sao chọn chức năng lượt nói hiện có không xử lý được?
- Đầu vào nào được dùng để quyết định, đầu ra là gì và thành phần nào phụ thuộc đầu ra đó?
- Có giữ trạng thái không; nếu có, trạng thái phục vụ quyết định nào?
- Khi thiếu đầu vào, sai lựa chọn hoặc không nạp được nguồn thì điều gì xảy ra?
- Vì sao một điều kiện đơn giản trong chủ sở hữu hiện tại không đủ?

Một Router chọn tài liệu trong tập nguồn lớn có thể có trách nhiệm khác với chọn thao tác hội thoại. Nếu nhiệm vụ chỉ cần phân biệt giải thích và so sánh từ yêu cầu hiện tại, trước hết kiểm tra `TURN AND STATE`. Không buộc hai trường hợp này dùng cùng kiến trúc.

Router không được biện minh chỉ vì tồn tại nhiều chế độ hoặc nhiều mô-đun. Cấu trúc điều hướng không hàm ý quyền sở hữu ngữ nghĩa. Thư mục, mục lục hoặc tên nguồn cũng không tự chuyển quyền xác nhận sự thật hay canon sang Router.

Các câu hỏi trên dùng để giải thích thiết kế phù hợp quy mô thực tế, không yêu cầu thêm schema, registry, state machine hay tài liệu riêng cho từng câu trả lời.

## 9. Thứ tự dùng dung lượng Project

1. Bảo toàn hành vi đã được kiểm chứng đúng trong phạm vi bằng chứng của nó.
2. Giải nén điểm mơ hồ gây hại.
3. Làm rõ chủ sở hữu và ranh giới điều kiện kích hoạt.
4. Chỉ thêm mở rộng nhỏ cho lỗi hoặc yêu cầu cụ thể chưa được bao phủ.
5. Dừng khi thiết kế đã đủ.

Không lấp phần ngân sách còn trống. Không tối ưu câu chữ để đạt số ký tự tròn. Cũng không cắt phân biệt cần thiết chỉ để có diff ngắn: đơn vị tối thiểu là một sửa đổi đầy đủ cho vấn đề đã xác định.

Trong v9.0, hợp đồng ngôn ngữ, ba bất biến và nội dung `EXPLANATION` được giữ từ v8.9; phần trạng thái và phát biểu được giải nén. Đây là tính chất có thể đối chiếu văn bản, không phải kết quả chứng minh v9.0 hành xử tốt hơn.

## 10. Sửa đổi tương lai và sử dụng khi kiểm tra trước

Trước công việc tạo mới hoặc thiết kế lại đáng kể thuộc phạm vi quy tắc trong `AGENTS.md`, đọc rationale liên quan và đối chiếu đề xuất với trách nhiệm hiện có cùng mức sửa đổi đủ dùng. Với dòng Project Global Native, tài liệu này là một tham chiếu bắt buộc. Nó không biến mọi sửa lỗi chữ, định dạng hoặc chỉnh nhỏ thành yêu cầu viết một rationale mới.

Khi đánh giá thay đổi, phân biệt rõ: lỗi được chứng minh, rủi ro cấu trúc có căn cứ, rủi ro tương lai giả định, sở thích và mong muốn đổi kiến trúc. Rủi ro giả định không tự trở thành primitive bắt buộc. Yêu cầu mới cụ thể có thể tạo nhu cầu hợp lệ; không cần đợi hỏng runtime mới được thiết kế chức năng được người dùng yêu cầu.

Phiên bản sau có thể thay kiến trúc khi bằng chứng hoặc yêu cầu cho thấy sửa cục bộ không đủ. Tài liệu này không đóng băng sáu tiêu đề của v9.0, không lập ontology trách nhiệm vĩnh viễn và không cấm mở rộng chuyên ngành. Khi lịch sử và kiến trúc mới được chấp thuận khác nhau, nêu sự khác nhau thay vì dùng rationale cũ để phủ nhận hiện trạng.

Quy tắc đọc trước là cơ chế chỉ dẫn hiện có: `AGENTS.md` dẫn đến tài liệu tham chiếu, rồi người thực hiện đối chiếu đề xuất. Không có registry, validator, manifest hay cổng tự động mới. Tệp tồn tại và liên kết đúng không chứng minh phiên tương lai đã đọc hoặc tuân thủ nó.

Việc nghiệm thu văn bản chỉ xác nhận cấu trúc và nội dung đã được rà soát. Hiệu quả hành vi cần kiểm thử trên môi trường thực, với model/cấu hình, đầu vào, đầu ra và tiêu chí so sánh được ghi lại. Changelog v8.9 cũng tách kiểm tra tĩnh khỏi runtime; không nâng bằng chứng cấu trúc thành bảo đảm hành vi.

## 11. Nguồn để đối chiếu

- [SYSTEM_CONTEXT.md](../../../SYSTEM_CONTEXT.md): bối cảnh repository, độc lập giữa các Project và các lớp bằng chứng.
- [AGENTS.md](../../../AGENTS.md): điểm vào chỉ dẫn repository và yêu cầu đọc rationale trước công việc liên quan.
- [chatgpt v8.9.txt](<../ChatGPT Plus+ Era/chatgpt v8.9.txt>): baseline hành vi của dòng Plus; nguồn chính để đối chiếu những trách nhiệm được kế thừa.
- [chatgpt v9.0.txt](<chatgpt v9.0.txt>): hiện vật mở đầu dòng Project-native; không phải bằng chứng tự thân về triển khai runtime.
- [CI_DESIGN_EVOLUTION_AND_DEPLOYMENT_VI.md](../../../docs/instruction-analysis/CI_DESIGN_EVOLUTION_AND_DEPLOYMENT_VI.md): mục 4.4 về ba bất biến, mục 5 về ngân sách, mục 6.5 và 7 về v6.2 và chưng cất sang Go/Free.
- [CI_FAILURE_MODES_AND_CONTROL_MODEL_VI.md](../../../docs/instruction-analysis/CI_FAILURE_MODES_AND_CONTROL_MODEL_VI.md): FM-13, FM-20, FM-24, FM-25, FM-27 và giới hạn bằng chứng hành vi ở mục 9.3.
- [CHANGELOG_VI.md](../../../docs/instruction-history/CHANGELOG_VI.md): mục v8.9 về thay đổi quyền mở việc, xử lý diễn đạt lại và giới hạn kiểm chứng.

Các tài liệu lịch sử giải thích tiến hóa đến thời điểm chúng ghi nhận. Rationale cũ đã đánh dấu lỗi thời chỉ là tư liệu lịch sử; không dùng nó để ghi đè hiện vật hiện hành hay quyết định mới được chấp thuận.
