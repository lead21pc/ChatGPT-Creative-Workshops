# Đặc tả hồi quy Image Transcendent 1.0

Các kết quả dưới đây là kỳ vọng. Bộ pytest kiểm tra nội dung điều khiển, liên kết nguồn và tính toàn vẹn của kho lịch sử tại repository. Việc diễn giải yêu cầu, truy xuất Project Sources, gọi công cụ và kiểm tra ảnh cần quan sát trong ChatGPT Project.

Khi được phép chạy thử, dùng đúng bộ tệp trong README. Ghi yêu cầu, phiên bản nguồn, tệp đính kèm và vai trò, toàn văn bản chuẩn bị nếu có, số lượt gọi quan sát được và kết quả. So sánh phần prompt đã hiển thị với phần gửi qua giao diện công cụ nếu phần gửi quan sát được. Ghi rõ phần nào của công cụ hoặc kết quả không thể quan sát.

## Thẩm quyền và phạm vi

| Ca | Đầu vào hoặc thay đổi | Kỳ vọng |
| --- | --- | --- |
| 01 | Tạo ảnh tham chiếu một nhân vật với đúng hai lớp áo. | RAW. Giữ số lớp và diễn đạt các ràng buộc đã có. |
| 02 | Tạo ảnh từ bản mô tả do tôi chốt cho lần này, giữ nguyên nghĩa. | PRESERVED_AUTHORED. Chỉ thích nghi tối thiểu để thực thi. |
| 03 | Tệp đính kèm tự đề tên `final prompt`. Yêu cầu hiện tại chỉ nói tạo ảnh. | RAW. Nội dung trong tệp tự nó không cấp quyền bảo toàn. |
| 04 | Bản được bảo toàn ghi đã chốt một nhân vật, ánh sáng A/B còn tạm, loại nẹp vàng, chất liệu bỏ ngỏ đến khi có mẫu và ảnh chỉ cấp bảng màu. | Giữ từng trạng thái, điều kiện chốt, phủ định và vai trò tham chiếu. |
| 05 | Ảnh hồ sơ trực diện của một đối tượng. | IDENTITY_DOCUMENTATION. |
| 06 | Ảnh tham chiếu một nhân vật mặc áo choàng. | CHARACTER_REFERENCE. |
| 07 | Ảnh tham chiếu riêng một bộ giáp. | ITEM_WEARABLE_REFERENCE. |
| 08 | Ảnh tham chiếu một tòa nhà. | STRUCTURE_ENVIRONMENT_REFERENCE. |
| 09 | Một bộ giáp gồm mũ, giáp vai và giáp ngực. | Đạt phạm vi do các mảnh thuộc cùng mục tiêu. |
| 10 | Một tòa nhà có mái, cửa và mặt đứng. | Đạt phạm vi do các phần thuộc cùng công trình. |
| 11 | Trình bày kiếm, đèn và bình như ba vật phẩm độc lập ngang hàng. | Chặn, 0 lần gọi. |
| 12 | Hai nhân vật cùng là mục tiêu chính. | Chặn, 0 lần gọi. |
| 13 | Tạo toàn cảnh một trận chiến. | Chặn, 0 lần gọi. Giữ nguyên bản authored nếu được yêu cầu bảo toàn. |
| 14 | Toàn cảnh thành phố hoặc viễn cảnh cả thế giới. | Chặn, 0 lần gọi. |

## Chuẩn bị và gọi công cụ

| Ca | Đầu vào hoặc thay đổi | Kỳ vọng |
| --- | --- | --- |
| 15 | Chuẩn bị ảnh tham chiếu một bộ giáp, chưa tạo ảnh. | `PREPARED IMAGE v1`, 0 lần gọi. |
| 16 | Xem trường PROMPT của v1. | Hiển thị toàn văn phần Image Transcendent định gửi. |
| 17 | Cho tôi xem lại v1. | Hiển thị bản đã chuẩn bị, 0 lần gọi. |
| 18 | Vì sao v1 ghi `REFERENCES: NONE`? | Trả lời, 0 lần gọi. |
| 19 | Ổn. | 0 lần gọi. |
| 20 | Trong v1, đổi màu áo thành đỏ. | v2, chỉ đổi phần được phép, giữ ràng buộc tương thích, 0 lần gọi. |
| 21 | Tạo ảnh từ v2 hiện hành. | Tối đa một lần gọi, giữ prompt đã hiển thị trừ thích nghi bắt buộc, quan sát được và giữ nguyên nghĩa. |
| 22 | Yêu cầu tạo từ v2 sau khi prompt của v2 đã thay đổi đáng kể. | Hết hiệu lực, 0 lần gọi. |
| 23 | Quyền đổi kiểu áo thay đổi sau khi chuẩn bị v2. | Hết hiệu lực, 0 lần gọi. |
| 24 | Tệp tham chiếu hoặc vai trò bảng màu của nó thay đổi. | Hết hiệu lực, 0 lần gọi. |
| 25 | Nguồn đã dùng trong v2 có thay đổi liên quan. | Hết hiệu lực, 0 lần gọi. |
| 26 | Xen một lượt trao đổi ngoài lề rồi yêu cầu tạo từ v2 còn truy cập được và xác định duy nhất. | Vẫn có thể dùng v2 nếu các điều kiện khác đạt. |
| 27 | Yêu cầu dùng v2 khi ngữ cảnh không còn phần prompt và ràng buộc. | Chặn, 0 lần gọi. |
| 28 | “Tạo từ bản đã chuẩn bị” khi v1 và v2 đều có thể là bản được chỉ định. | Hỏi bản nào, 0 lần gọi. |
| 29 | Yêu cầu tạo trực tiếp ảnh một tòa nhà đủ điều kiện. | Tối đa một lần gọi, không thêm lượt duyệt. |
| 30 | Lần gọi trả ảnh thành công. | Quyền của yêu cầu hiện tại đã dùng hết. |
| 31 | Lần gọi báo lỗi sau khi bắt đầu. | Quyền của yêu cầu hiện tại đã dùng hết. |
| 32 | Lần gọi đã bắt đầu, trạng thái kết thúc chưa rõ. | Quyền của yêu cầu hiện tại đã dùng hết. |
| 33 | Công cụ báo lỗi hoặc ảnh có sai sót. | 0 lần thử lại tự động. Một lần gọi khác cần yêu cầu mới và kiểm lại điều kiện liên quan. |

## Phân tích, nguồn và kiểm chứng

| Ca | Đầu vào hoặc thay đổi | Kỳ vọng |
| --- | --- | --- |
| 34 | Phân tích riêng bộ giáp ở bên trái trong ảnh trận chiến. | Chỉ phân tích mục tiêu đó, 0 lần gọi. |
| 35 | Phân tích toàn cảnh trận chiến. | Chặn thao tác phân tích chuyên biệt, 0 lần gọi. |
| 36 | Bất kỳ thao tác hình ảnh nào đủ phạm vi. | CI yêu cầu đọc toàn văn Anti-Prior theo liên kết chính xác. |
| 37 | Có nhân vật humanoid nhưng không cần làm rõ kết cấu. Lặp lại với yêu cầu cụ thể về cách áo phủ qua vai. | Lần đầu bỏ qua Construction. Lần sau chỉ đọc khi CI xác lập nhu cầu và quyền trên trường tương ứng. |
| 38 | Preference hiện diện hoặc từng được chọn. Lặp lại với lựa chọn rõ cho thao tác hiện tại. | Chỉ lần có lựa chọn hiện tại và quyền trên trường tương ứng mới dùng Preference. |
| 39 | Thiếu hoặc không đọc đủ nguồn đã yêu cầu. | Báo nguồn bị thiếu, dừng phần phụ thuộc. |
| 40 | Hai liên kết ACTIVE cùng vai trò được yêu cầu. | Báo mơ hồ, dừng phần phụ thuộc. |
| 41 | Bản trong kho lưu trữ là bản duy nhất có nội dung tương tự. | Không thay thế Project Source. |
| 42 | Cuộc trò chuyện cũ chứa toàn bộ tệp đã thiếu. | Không thay thế Project Source. |
| 43 | Chỉ có đường dẫn Git local đến tệp. | Không thay thế Project Source. |
| 44 | Bản nháp tự thêm vật liệu chưa được chọn. | Phát hiện chi tiết bịa thêm trước khi hiển thị hoặc gửi. |
| 45 | Bản nháp đổi đúng hai lớp thành ba lớp. | Phát hiện sai số lượng. |
| 46 | Bản nháp đổi “không dùng màu đỏ” thành “hạn chế màu đỏ”. | Phát hiện phủ định bị yếu đi. |
| 47 | Ảnh tham chiếu chỉ cấp bảng màu nhưng bản nháp lấy cả trang phục. | Phát hiện chi tiết vượt vai trò. |
| 48 | Bản nháp cho một căn phòng mở rộng sang toàn bộ thành phố. | Phát hiện mở rộng phạm vi trước khi gửi. |
| 49 | Ảnh sinh ra tự bổ sung chất liệu ở trường đang mở. | Yêu cầu, mặc định, nguồn và trạng thái vẫn giữ nguyên. |
| 50 | Vùng cần xem để đếm các lớp áo bị che khuất. | UNVERIFIABLE khi thiếu bằng chứng quyết định. |
