# Chaos — OPEN_STATE

**Vai trò:** sở hữu danh sách/trạng thái chưa chốt; không phải TODO list và không cấp quyền tự hoàn thiện.
**Trạng thái nguồn:** nội dung canon theo specification v3 đã được xác nhận; các mục UNKNOWN vẫn mở. Tái cấu trúc tài liệu không nâng canon, Working, Placeholder hoặc UNKNOWN. Các mô tả signature là cách đọc phân tích bám nguồn, không là quyết định canon mới.

Đọc theo nhu cầu: [identity/signature](ENGINE_CORE.md), [ranh giới Host](HOST_CONTRACT.md), [vận hành](RUNTIME.md), [vùng mở](OPEN_STATE.md), [kiểm chứng bằng bản viết](WRITING_VALIDATION.md). Đây là vai trò tài liệu, không phải các bước thực thi engine.


# 15. Chưa khóa / UNKNOWN

Các phần sau chưa được xác định đầy đủ:

- Three Pengs được gán Upper / Middle / Lower Peng theo thứ tự nào.
- Ludopath kích hoạt dưới điều kiện chính xác nào.
- Catalyst có cần cả ba Peng cùng active hay không.
- Envy và Gluttony có thể trực tiếp xuất hiện ở frontend hay không.
- Pride có authority nội bộ lên hai Peng còn lại hay chỉ là interface biểu hiện.
- Volatility điều khiển chính xác:
  - reward value,
  - satisfaction threshold,
  - intensity,
  - continuation probability,
  - hay một biến khác.
- Điều kiện Chaos Engine chọn một HIP hoặc potential HIP làm target.
- Chaos Engine có thể tác động lên non-HIP hay không.
- Cơ chế formal để "xâm phạm HIP formation".
- HIP có thể chống, phục hồi hoặc chuyển hóa áp lực của Chaos Engine như thế nào.
- Failure state của Chaos Engine.
- Termination condition.
- Tool / Doctrine / Counter nếu Chaos Engine có các thành phần này.
- Mức portable sang từng loại host fiction.
- Authority / jurisdiction của Chaos Engine khi hoạt động xuyên host.
- Quan hệ formal giữa Chaos Engine và từng Executor của The Academy.
- Điều kiện xác định The Academy vận hành theo Institutional Causality, Narrative Engine Causality hay một configuration lai.
- Phạm vi authority trực tiếp của The Academy trong Institutional Causality so với backend authority trong Narrative Engine Causality.

---


## Phân loại độ mở và giới hạn của việc phân loại

- `UNKNOWN`/`OPEN`: giữ đúng vấn đề nguồn đã nêu; nếu nguồn không nói rõ là chưa externalize hay cố ý để mở, nguyên nhân vẫn **chưa xác định**. Không tự gán “unknown by design” cho từng cơ chế.
- `Working` / `Working Interpretation`: diễn giải đang làm việc, không nâng thành stable.
- `Placeholder` / `Future Development`: nhãn chưa chốt của nguồn, không phải requirement hoặc cam kết phải hoàn thiện.
- Portability/host-compatibility, câu hỏi nội bộ engine và quan hệ implementation giữ riêng đúng phạm vi câu hỏi; một câu trả lời ở host này không tự giải host khác.
- Cơ chế nối output với ongoing Host progression, nếu chưa có nguồn cụ thể, vẫn UNKNOWN tại HOST_CONTRACT; yêu cầu integrity không tự externalize cơ chế.

Các đoạn runtime/core cần nhắc Working/UNKNOWN tại chỗ để tránh nâng trạng thái vẫn giữ qualifier. OPEN_STATE sở hữu việc tra cứu trạng thái, không xóa qualifier khỏi nơi dùng cơ chế.
