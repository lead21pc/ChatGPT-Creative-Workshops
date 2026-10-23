# Greed — OPEN_STATE

**Vai trò:** sở hữu danh sách/trạng thái chưa chốt; không phải TODO list và không cấp quyền tự hoàn thiện.
**Trạng thái nguồn:** Working Draft v0.2; Governor theo xác nhận tác giả. Tái cấu trúc tài liệu không nâng canon, Working, Placeholder hoặc UNKNOWN. Các mô tả signature là cách đọc phân tích bám nguồn, không là quyết định canon mới.

Đọc theo nhu cầu: [identity/signature](ENGINE_CORE.md), [ranh giới Host](HOST_CONTRACT.md), [vận hành](RUNTIME.md), [vùng mở](OPEN_STATE.md), [kiểm chứng bằng bản viết](WRITING_VALIDATION.md). Đây là vai trò tài liệu, không phải các bước thực thi engine.


## Ranh giới chưa chốt

- Tiêu chí chọn người nhận, cơ chế và lợi ích Ring, giới hạn sức mạnh, nguồn gốc, số lượng Ring và cách Greed thu nhận trải nghiệm.
- Kết quả khi người nhận từ chối nhưng Greed không thắng; cách Governor vận hành ngoài cấu hình đang được mô tả.
- Sự phụ thuộc bản thể giữa Greed Engine, Greed II, Ring và host; tính portable của mỗi thành phần.
- `Infinite Rings` là giả định ở lớp Greed Paradox trong bản hợp nhất, trong khi nguồn Ring để số lượng là placeholder; chưa nâng thành canon ổn định.
- Ring được gọi là chất xúc tác **cho một cuộc đời** trong nguồn; nhãn đó không tự chứng minh Ring là một `Catalyst` theo ontology chung của project.


## Giới hạn

- Nguồn gốc, cơ chế, giới hạn sức mạnh, lợi ích chính xác và số lượng Ring: placeholder.
- `Infinite Rings` xuất hiện trong nguồn Greed Paradox nhưng xung đột với placeholder về số lượng ở nguồn Ring; trạng thái ổn định chưa được chốt.
- Nguồn hiện mô tả người nhận là con người. Áp dụng cho đối tượng khác, host khác hoặc chạy Ring độc lập với Greed: `UNKNOWN`.
- Quan hệ giữa Ring và Governor `Responsibility` được giải thích trong [Greed Core](ENGINE_CORE.md); interface này không biến trách nhiệm thành một outcome bắt buộc của người nhận.


## Phân loại độ mở và giới hạn của việc phân loại

- `UNKNOWN`/`OPEN`: giữ đúng vấn đề nguồn đã nêu; nếu nguồn không nói rõ là chưa externalize hay cố ý để mở, nguyên nhân vẫn **chưa xác định**. Không tự gán “unknown by design” cho từng cơ chế.
- `Working` / `Working Interpretation`: diễn giải đang làm việc, không nâng thành stable.
- `Placeholder` / `Future Development`: nhãn chưa chốt của nguồn, không phải requirement hoặc cam kết phải hoàn thiện.
- Portability/host-compatibility, câu hỏi nội bộ engine và quan hệ implementation giữ riêng đúng phạm vi câu hỏi; một câu trả lời ở host này không tự giải host khác.
- Cơ chế nối output với ongoing Host progression, nếu chưa có nguồn cụ thể, vẫn UNKNOWN tại HOST_CONTRACT; yêu cầu integrity không tự externalize cơ chế.

Các đoạn runtime/core cần nhắc Working/UNKNOWN tại chỗ để tránh nâng trạng thái vẫn giữ qualifier. OPEN_STATE sở hữu việc tra cứu trạng thái, không xóa qualifier khỏi nơi dùng cơ chế.
