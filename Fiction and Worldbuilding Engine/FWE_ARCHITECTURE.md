# Kiến trúc Fiction and Worldbuilding Engine

Tài liệu này sở hữu quyết định kiến trúc và ranh giới trách nhiệm. [Kế hoạch phát triển](FWE_DEVELOPMENT_PLAN.md) sở hữu thứ tự triển khai, tiêu chí và bằng chứng. Các quyết định dưới đây đến từ Phase A–D. M1 đã tạo local [CI nền tự chứa](controls/FWE_CI_v0.1.md), có quy tắc Anti-Prior ngắn để làm cấu hình A cho phép thử sau này. Chưa có Router, hợp đồng nguồn riêng hay thành phần chuyên biệt; chưa xác minh hành vi trên ChatGPT Project.

## Quyết định đã chốt

FWE là Project riêng để sáng tác và phát triển nhiều thế giới hư cấu. FWE giữ quyền sáng tạo trong phần được giao và tôn trọng trạng thái của từng thế giới. FTH, C2, The Kingdom, LitRPG và các dự án khác tiếp tục giữ nguồn sự thật của riêng chúng. Người dùng chọn Project theo việc cần làm; FWE không chuyển sang một runtime khác giữa lượt.

Kiến trúc ở mức moderate: một CI tự chứa, Router tùy nhu cầu, trách nhiệm xử lý nguồn riêng, cùng các đóng góp chuyên biệt có căn cứ. Không dùng mô hình package của Central Hub. Các lựa chọn chưa được kiểm chứng không tự trở thành thành phần cố định.

## Thẩm quyền và luồng thực hiện

```text
Yêu cầu của người dùng
→ CI: chức năng, thao tác, giai đoạn, phạm vi, quyền sáng tác,
  trạng thái cần giữ, phụ thuộc nguồn, và có cần ủy quyền không
    ├─ Phần tự đủ → thực hiện trực tiếp
    └─ Phần cần chuyên biệt → Router chọn đóng góp trong phạm vi được giao
                                → thực hiện phần đó
CI tiếp tục giữ ranh giới trạng thái, sự thật, chấp nhận, canon,
quyền hành động và lời báo hoàn tất trong cả hai đường.
```

CI quyết định người dùng đang giao việc gì. Router chọn cách xử lý nguồn, capability hay anti-drift cần cho **phần việc đã xác định**. Router không tự đổi thao tác, giai đoạn, mục tiêu hoặc kết cục. Nếu phát hiện phạm vi chưa đủ rõ hoặc xuất hiện phụ thuộc có hệ quả, Router trả vấn đề về CI để giới hạn, làm rõ hoặc giao lại đúng phần. Việc chọn nguồn hoặc control không chứng minh đã đọc hay đã áp dụng. Thành phần cấp dưới không tự chọn nhau, tự thay trạng thái hay cấp quyền hành động. CI giữ ranh giới chấp nhận; người dùng hoặc hệ đích mới có thẩm quyền chấp nhận.

“Viết cảnh hai người gặp lại sau 20 năm” đi thẳng nếu tự đủ. Không tra nguồn, nạp control hay xuất báo cáo định tuyến mặc định. Nếu trong lúc viết xuất hiện một phụ thuộc có hệ quả, chỉ xét lại phần cần nó; không khởi động lại cả lượt.

### Lõi kiểm soát

- Giữ đúng chức năng của lượt nói và chỉ đổi thao tác, giai đoạn hoặc phạm vi khi có căn cứ.
- Cho phép sáng tác trong phần đã giao, kể cả chọn tiền đề mới khi nhiệm vụ cho phép.
- Kiểm tra dữ kiện thực hoặc mệnh đề mà kết quả phụ thuộc; không biến chi tiết hư cấu thành đối tượng kiểm chứng mặc định.
- Khi căn cứ được sửa hợp lệ, cập nhật kết luận phụ thuộc và giữ phần độc lập. Phân biệt bất định về cách làm với bất định về mệnh đề; chỉ nêu phần có hệ quả.
- Giữ đúng vai trò nguồn, quyền hành động và trạng thái thực hiện. Nội dung sinh ra không thành dữ kiện hay canon; nhánh không thành tiền đề đã chấp nhận; đề xuất không thành trạng thái hiện hành; lần thử không chứng minh hoàn tất.

## Hành vi nền, ứng viên và phối hợp

Sáng tác, phát triển cảnh, nảy ý, phản biện và đặt tên thông thường thuộc nền FWE. Không tách thành phần Creative, Debate hay Naming. Phần viết vẫn thuộc nền khi đi sau một yêu cầu mở nhánh.

**Brainstorm — ứng viên.** Router có thể chọn kỹ thuật này cho phần cần thay tiền đề trong nhánh, đảo hoặc nới giả định, tạo khác biệt cơ chế, truy hệ quả bậc hai, phản hồi về tiền đề hoặc nối các tiền đề chưa hoàn chỉnh. Yêu cầu “đảo giả định rồi mở ba nhánh” đủ rõ về thao tác; số lượng ý tưởng riêng nó không đủ. Brainstorm dùng bối cảnh có liên quan, chỉ thay phần được giao, dừng khi đủ độ sâu và không tự chốt nhánh. Việc sử dụng không kéo dài sang lượt sau. Thành phần riêng chỉ được giữ nếu thử đối chứng cho thấy lợi ích.

**Anti-Prior — đã chốt trách nhiệm, đang thử vị trí.** Trách nhiệm là ngăn trope, nhãn, thẩm mỹ, nguyên mẫu hoặc phép tương tự âm thầm thay cho một tiền đề, cơ chế hoặc tiêu chí có hệ quả. Giữ trope đã yêu cầu, không tự nhập các đặc tính thường đi kèm; sáng tạo được ủy quyền không cần nguồn có sẵn. Không suy ngược mặc định để ép độc đáo. Có thể áp dụng cho phần việc thích hợp, kể cả phản biện hoặc đặt tên, không chỉ Brainstorm. Chỉ xem mối nối ảnh hưởng kết quả; vận hành im lặng trừ khi cần làm rõ hoặc người dùng cần thấy giả định. Vị trí **A** là một quy tắc ngắn trong CI; **B** là kiểm soát theo phần việc do Router chọn. Mỗi bộ thử chỉ dùng một vị trí. Anti-Prior không kiểm chứng dữ kiện thật, tạo nhánh, cấp quyền nguồn, chấp nhận canon hoặc mô phỏng toàn bộ thế giới.

**Phối hợp.** Có thể chọn không, một hoặc nhiều đóng góp trên từng phần. Nguồn cung cấp căn cứ; Brainstorm biến đổi tiền đề trong nhánh; Anti-Prior kiểm đúng mối nối bị suy theo mặc định. Không có phụ thuộc cứng giữa Brainstorm và Anti-Prior, thứ tự chung bắt buộc hay quyền ưu tiên vì một control cụ thể hơn. Nếu thiếu nguồn hoặc thành phần quyết định, giới hạn hoặc dừng phần phụ thuộc và tiếp tục phần độc lập. Chỉ dùng nền khi thật sự đủ; không nhận đã thực hiện phần chuyên biệt bị thiếu.

## Trách nhiệm hợp đồng nguồn

Hợp đồng nguồn sau này quy định vai trò và giới hạn sử dụng của: bối cảnh hư cấu do người dùng cung cấp; tài liệu hiện hành của hệ đích; tệp đính kèm/tham khảo; tiền đề tạm; nhánh; đề xuất; điều chưa biết được bảo vệ; tư liệu lịch sử và provenance; cảm hứng liên dự án. Hợp đồng mô tả cách dùng nguồn; Router phân giải nguồn khi cần; CI giữ ranh giới kết luận và trạng thái.

Tệp hiện diện hoặc đọc được không tự có thẩm quyền. Tư liệu lịch sử không thay nguồn hiện hành; nội dung làm việc của FWE không thành canon hệ đích. Chất liệu có thể đi từ bối cảnh được giao qua bản sáng tác của FWE tới **xét và chấp nhận tại hệ đích**. FWE tập trung tài liệu của chính mình, ca thử, hồ sơ phát triển và chất liệu được phép lưu. Không gom lore dự án khác và chưa có giao thức chuyển giao đầy đủ.

## Lõi chuyển được và phần riêng FWE

| Lõi chung trong CI tự chứa | Phần riêng FWE |
|---|---|
| Thao tác, giai đoạn, phạm vi, quyền sáng tác, sự thật và trạng thái | Mục tiêu phát triển nhiều thế giới và hành vi sáng tạo thông thường của FWE |
| Hiệu lực của nhánh/đề xuất, cập nhật kết luận phụ thuộc, căn cứ nguồn và hành động | Chi tiết nguồn, lựa chọn của Router, Brainstorm và vị trí Anti-Prior |
| Hợp đồng ủy quyền không chuyển thẩm quyền | Cây tệp và quy trình phát triển/kiểm chứng của FWE |

Khả năng chuyển nằm ở ngữ nghĩa, không ở shared file hay phụ thuộc khi chạy. Theo thông tin người dùng cung cấp, LitRPG là dự án độc lập đang ở mức ý tưởng và tạm dừng để chờ kiến trúc kiểm soát phù hợp, có liên hệ lịch sử với The Kingdom. Điều đó là lý do tránh đưa ontology FWE vào lõi chung. Nó không xác nhận LitRPG tương thích, và không làm kiến trúc hiện tại của The Kingdom thành yêu cầu LitRPG hay FWE.

## Bảo trì và giới hạn mở rộng

Khi xem xét cơ chế từ FTH, C2, The Kingdom, Fanfiction Engine, Central Hub hay hệ khác: đọc đúng nguồn hiện hành, xác định lỗi được giải và giả định/chi phí tại chỗ, đối chiếu với FWE, phân loại mức liên quan, rồi chỉ đề xuất thay đổi cục bộ nếu có căn cứ. Không tự đồng bộ hay chuyển control. Cùng miền không đồng nghĩa cùng lỗi; cùng lỗi không đòi cùng cách triển khai.

Skill `fwe-development` quản lý việc đọc bộ control hiện hành, vai trò nguồn, tiếp nhận cơ chế ngoài, mốc, bằng chứng, hồi quy và kiểm chứng thay đổi được phép. Skill không phải điều kiện khởi tạo, nhưng phải có trước mốc ổn định. Nó không cấp quyền sửa hoặc thay CI, Router hay Git.

Ưu tiên quay về bộ tương thích có bằng chứng hoặc thu hẹp thành phần, không giữ lớp dư vì đã viết xong. Git là lịch sử mặc định; kiểm tĩnh không chứng minh một bộ chạy tốt. Các lỗi về điều kiện hành động của nhân vật hoặc truy hệ quả chỉ mở thêm control khi đã có bằng chứng và nơi chịu trách nhiệm hiện tại không xử lý đủ. Không tạo manifest, catalog, registry, meta-router, shared kernel hay archive mới chỉ để chuẩn bị.
