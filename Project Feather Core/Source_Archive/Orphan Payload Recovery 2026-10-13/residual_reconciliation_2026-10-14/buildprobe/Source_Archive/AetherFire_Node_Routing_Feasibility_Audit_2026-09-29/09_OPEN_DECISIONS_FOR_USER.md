# 09 — Những quyết định còn cần người dùng

> Audit không tự chọn default cho các quyết định dưới đây. Các chi tiết như tên ID, số node cụ thể, định dạng bảng hoặc ngưỡng closure là việc thiết kế/thử nghiệm, **không** đẩy sang người dùng. Không cần trả lời những mục này để hoàn tất audit hiện tại.

| Vấn đề cần quyết định sau khi có bằng chứng | Phương án A | Phương án B | Đánh đổi; chưa chọn mặc định |
| --- | --- | --- | --- |
| Có cho phép **một đợt shadow Project thật** với bản CI/Router/source thử nghiệm riêng không? | Có, giữ bộ hiện hành để đối chứng và chỉ thử trong không gian shadow được kiểm | Chỉ kiểm local, không chạy Project shadow | A mới xác minh được runtime retrieval/behavior nhưng cần quản lý snapshot và thời gian; B ít thao tác hơn nhưng node mode phải ở trạng thái `UNVERIFIED_RUNTIME`, không thể kích hoạt có cơ sở. |
| Tiêu chí chấp nhận khi paired test có lỗi semantic | Đặt ngưỡng **zero critical error** về authority/truth status và yêu cầu đủ case qua review | Chấp nhận một mức sai lệch đã được nêu rõ với phạm vi giới hạn | A nghiêm hơn, có thể giữ full-file lâu; B tối ưu sớm hơn nhưng có nguy cơ false canon/UNKNOWN resolution. Audit đề nghị ưu tiên an toàn, song không tự chốt ngưỡng chính sách thay người dùng. |
| Sau pilot, phạm vi kích hoạt đầu tiên nên là gì? | Chỉ một domain/prompt class đã qua test (ví dụ aviation `80`) | Nhiều domain đã qua test cùng một lần | A dễ rollback và quy trách nhiệm; B giảm số lần phát hành nhưng blast radius lớn hơn. Không tự kích hoạt lựa chọn nào. |
| Khi `90` có nội dung `CURRENT CANON` đan với genealogy, có muốn đầu tư history-cluster routing ở phase sau không? | Review status từng cluster rồi thử `RECORD_OR_FULL`/history node với anti-revival oracle | Giữ `90` full-file lâu dài | A có thể giảm read cho provenance task nhưng tốn review và dễ sai authority; B đơn giản và an toàn hơn, còn chi phí context chưa đo được. |

Các câu hỏi này **không phải yêu cầu cho phép sửa runtime trong lượt hiện tại**. P0–P2 trên bản sao có thể chuẩn bị trong một yêu cầu tương lai; mọi cài đặt vào Project instructions, Router, anti-drift hoặc source hiện hành vẫn cần task triển khai riêng đúng phạm vi người dùng chọn.
