# Sloth — OPEN_STATE

**Vai trò:** sở hữu danh sách/trạng thái chưa chốt; không phải TODO list và không cấp quyền tự hoàn thiện.
**Trạng thái nguồn:** Working Draft; các mục Stable giữ đúng phạm vi của nguồn. Tái cấu trúc tài liệu không nâng canon, Working, Placeholder hoặc UNKNOWN. Các mô tả signature là cách đọc phân tích bám nguồn, không là quyết định canon mới.

Đọc theo nhu cầu: [identity/signature](ENGINE_CORE.md), [ranh giới Host](HOST_CONTRACT.md), [vận hành](RUNTIME.md), [vùng mở](OPEN_STATE.md), [kiểm chứng bằng bản viết](WRITING_VALIDATION.md). Đây là vai trò tài liệu, không phải các bước thực thi engine.


# 12. Working / Placeholder

## Working

- Core Drive cuối cùng.
- Mô hình Authority.
- Định nghĩa chính xác của Seat.
- Formal meaning của “dứt nợ”.
- Quan hệ giữa Authority và regression.
- Quy tắc Graze chi tiết.
- Timing model.
- Cơ chế cụ thể của The Gun.

## Placeholder

- Trigger conditions của Accommodation.
- Authority hierarchy.
- Compatibility với từng loại fiction.
- Ammunition concept.
- Cross-fiction implementation của The Gun.
- Edge cases khi Regressor không được một authority rõ ràng “cho phép”.
- Operation pipeline chi tiết hơn.


## Vùng mở riêng của Accommodation

# Placeholder

-   Operation flow.
-   Trigger conditions.
-   Authority hierarchy.
-   Compatibility với các fiction khác.


## Vùng mở riêng của Graze

## Future Development

-   Movement rules
-   Timing model
-   Interaction with Accountability
-   Interaction with Accommodation


## Vùng mở riêng của The_Gun

## Future Development

-   Ammunition concept
-   Symbolic meaning
-   Cross-fiction implementations


## Phân loại độ mở và giới hạn của việc phân loại

- `UNKNOWN`/`OPEN`: giữ đúng vấn đề nguồn đã nêu; nếu nguồn không nói rõ là chưa externalize hay cố ý để mở, nguyên nhân vẫn **chưa xác định**. Không tự gán “unknown by design” cho từng cơ chế.
- `Working` / `Working Interpretation`: diễn giải đang làm việc, không nâng thành stable.
- `Placeholder` / `Future Development`: nhãn chưa chốt của nguồn, không phải requirement hoặc cam kết phải hoàn thiện.
- Portability/host-compatibility, câu hỏi nội bộ engine và quan hệ implementation giữ riêng đúng phạm vi câu hỏi; một câu trả lời ở host này không tự giải host khác.
- Cơ chế nối output với ongoing Host progression, nếu chưa có nguồn cụ thể, vẫn UNKNOWN tại HOST_CONTRACT; yêu cầu integrity không tự externalize cơ chế.

Các đoạn runtime/core cần nhắc Working/UNKNOWN tại chỗ để tránh nâng trạng thái vẫn giữ qualifier. OPEN_STATE sở hữu việc tra cứu trạng thái, không xóa qualifier khỏi nơi dùng cơ chế.


Core Drive/Authority/Seat được giữ ở ENGINE_CORE với chính nhãn Working của nguồn. Accountability tiếp tục mang nhãn Counter của cơ chế riêng; task này không thực hiện quyết định đổi phân loại.
