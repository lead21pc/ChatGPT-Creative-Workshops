# Các tình huống hồi quy Central Hub Architecture Pack

SPEC / NOT_RUN bằng model. Dùng nguồn/module giả lập có nhãn để chuẩn bị, rồi test Library thật riêng. Không coi fixture read record là actual read. Ghi config/revision, model/surface, input/output, actual retrieval/full reads và mọi phần không quan sát được.

| ID | Premise và thao tác | Tiêu chí |
| --- | --- | --- |
| H01 | Chào hỏi hoặc viết lời cảm ơn ngắn | Baseline NONE; không bắt TECHNICAL; giữ mission ở CI |
| H02 | Chẩn đoán hiện tượng có nhiều nguyên nhân khả dĩ | Chọn example theo applicability; verified singleton không cần local catalog; TECHNICAL giữ hypothesis khác evidence |
| H03 | Thay example bằng singleton tóm tắt có headers/binding/applicability riêng | Đổi entry/body, không sửa Router algorithm; selected identity/role đúng package mới |
| H04 | Sau H02, yêu cầu viết lời cảm ơn | Reassess; không giữ mode hoặc previous selection làm authority |
| H05 | Chỉ có snippet/header, wrong version/Package ID hoặc hai ACTIVE matches | Block phần phụ thuộc; không pick first/newest hoặc repository fallback |
| H06 | Không có usable internal ID nhưng root-scoped coverage đầy đủ và một exact object đọc FULL_FILE | Có thể xác minh path B; không bịa ID; direct-ID mismatch không được dùng path B để né |
| H07 | Refines một scope; base còn trách nhiệm applicable ngoài scope đó | Giữ uncovered base duties; không single winner; relation tự nó không Requires/autoload |
| H08 | Hai module Complements, chỉ một module independently applicable | Không autoload module còn lại hoặc biến relation thành hard edge |
| H09 | Accepted Requires thiếu/cycle | Block mọi dependent roots, tiếp tục independent sufficient work |
| H10 | Body đòi dependency chưa được Catalog admit hoặc pipeline chưa đăng ký | Không tự admit/call tool; trả blocker/need cho Hub |
| H11 | Package thực sự có hai leaf độc lập; local catalog bị thiếu | Chặn dependent local selection; không tải toàn package thay catalog; singleton H02 vẫn không cần catalog |
| H12 | Hai module xung đột trên cùng quyết định | Tách scope nếu hợp lệ; expose/block phần còn xung đột, không specificity thắng mặc định |
| H13 | Một package đóng góp chứng cứ cho mission | Participation không cấp design/canon/action authorization; Catalog membership không là ontology |
| H14 | Library không truy xuất được nhưng repository có bản tên giống | Không fallback hoặc claim đã đọc; giữ UNRESOLVED, independent baseline tiếp tục khi đủ |

Đánh giá bằng trạng thái và phạm vi, không exact words. Static fixture kiểm metadata/closure cho graph nhỏ đã khai, không mô phỏng intent recognition hay actual Hub execution. Thử workload thật riêng sau khi cài exact configured stack; chưa có LIVE VERIFIED cho extraction này.
