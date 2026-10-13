# Giải thích đề xuất Router 4.0

Trạng thái: bản thiết kế để đọc và góp ý, chưa được cài đặt. CI 3.0 hiện có bản đề xuất trong kho nhưng chưa được xác nhận là nội dung đang cài trong ChatGPT Project; mọi phần phụ thuộc vào nó vẫn là PENDING CI 3.0 CONTRACT. Bộ mặc định v2.6/Router 3.2 không thay đổi.

## Module Gate là gì?

Đó là cửa kiểm tra trước khi mô hình dùng một tệp nguồn để trả lời. Nó hỏi: câu hỏi này liên quan module nào, module ấy có đúng vai trò và phạm vi không, ai giữ quyền quyết định phần nội dung đang hỏi, có module khác bắt buộc phải đọc không, và đã đọc đủ nguồn chưa. Qua cửa này không có nghĩa nội dung đã đúng hay đã thành canon.

Router 3.2 có bảng định tuyến theo tên miền và tệp được viết sẵn. Nếu về sau thêm một faction hay institution mới, bảng ấy sẽ phình ra. Router 4.0 đề xuất để nguồn tự khai báo phạm vi bằng header và để một catalog trong 00 giúp tìm ra nó. Router core chỉ cần hiểu cách kiểm tra module, không cần biết trước tên mọi faction.

## Header và catalog làm gì?

Header là vài dòng Markdown ở đầu tệp, ghi mã module, vai trò, phạm vi và ranh giới chủ sở hữu. Nó giống nhãn trên bìa hồ sơ: giúp tìm và tránh đọc nhầm, nhưng không tự cấp quyền canon. Một tệp lịch sử tự viết rằng nó là canon vẫn phải bị đối chiếu với quyết định của người dùng và gói nguồn hiện hành.

Catalog là danh sách tệp được sinh từ các header đã kiểm tra. Vì chưa biết ChatGPT Project có thể tự liệt kê mọi tệp hay không, Router cần một danh sách mở đầu để biết nên mở header nào. Đề xuất đặt danh sách ấy trong 00, vốn đã được đọc đầu lượt. 00 vẫn giữ các ranh giới ngữ nghĩa hiện có; catalog chỉ giúp tìm đường, không thay nội dung nguồn hoặc nắm quyền của module.

Nếu tệp mới xuất hiện mà catalog chưa cập nhật, Router không được giả vờ rằng mình đã thấy hết nguồn. Tệp ấy có thể được đọc như nguồn mới chưa xác nhận khi người dùng chỉ rõ, nhưng sự hiện diện của nó không làm nó thành canon.

## Hai loại phụ thuộc khác nhau thế nào?

MODULE_REQUIRES nói rằng, với một loại câu hỏi cụ thể, đọc module A mà thiếu cả module B thì không đủ. NODE_REQUIRES hẹp hơn: một đoạn nội dung cụ thể cần thêm đoạn khác để không bỏ mất tiền đề quyết định. Cùng nhắc một nhân vật, cùng sự kiện hay nằm gần nhau không tạo ra bất kỳ phụ thuộc nào. Cạnh phụ thuộc phải có lý do và được xem lại.

## Đọc một đoạn có an toàn không?

Mặc định vẫn đọc nguyên tệp. Chỉ khi một module đã được rà soát và ChatGPT Project thật sự lấy được phần bối cảnh bắt buộc, chỉ mục cục bộ, đoạn đích và toàn bộ đoạn phụ thuộc thì mới có thể thử đọc theo node. Thiếu một mảnh, chỉ nhận được trích đoạn tìm kiếm, hoặc không chứng minh được phạm vi đã đọc thì quay về đọc nguyên tệp. Nếu tệp quyết định cũng không lấy được, phải dừng kết luận phụ thuộc vào nó. Các overlay anti-drift vẫn đọc nguyên tệp.

## Thêm faction mới sẽ xảy ra chuyện gì?

Nguồn mới được viết với header hợp lệ, được người dùng chấp nhận vào đúng vai trò, được thêm vào catalog sinh lại và kiểm tra cùng gói nguồn. Sau đó câu hỏi liên quan có thể dẫn Router tới nguồn mới; câu hỏi không liên quan không phải tải nó. Router core không cần sửa chỉ vì có thêm faction, institution, region, actor hay subsystem. Quan hệ tương tác giữa chúng không buộc chúng vào cây cha-con.

## Khi nào phải sửa Router?

Không cần sửa Router khi chỉ thêm module theo hợp đồng đã duyệt, đổi đường dẫn nhưng giữ mã định danh, hoặc cập nhật catalog và các liên kết phụ thuộc đã được rà soát. Cần xem lại Router khi thay nghĩa quyền hạn nguồn, thêm kiểu đọc mới, đổi cách khám phá tệp, hoặc thay chính quy tắc Module Gate. Những thay đổi đó là kiến trúc, không phải thêm một mục vào danh sách.

Trước khi dùng thật, cần một thử nghiệm riêng trong ChatGPT Project để xem backend có trả đủ nguồn và mô hình có giữ đúng quyền hạn, trạng thái chưa biết và các ngoại lệ hay không. Tám tài liệu này là đề xuất; chúng không tự kích hoạt CI 3.0 hay Router 4.0.
