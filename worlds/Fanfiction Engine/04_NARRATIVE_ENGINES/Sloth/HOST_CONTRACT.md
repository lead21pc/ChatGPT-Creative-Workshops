# Sloth — HOST_CONTRACT

**Vai trò:** sở hữu ranh giới Host ↔ engine ↔ tiến trình Host đang tiếp tục; không thay luật Host hoặc định nghĩa runtime bên trong.
**Trạng thái nguồn:** Working Draft; các mục Stable giữ đúng phạm vi của nguồn. Tái cấu trúc tài liệu không nâng canon, Working, Placeholder hoặc UNKNOWN. Các mô tả signature là cách đọc phân tích bám nguồn, không là quyết định canon mới.

Đọc theo nhu cầu: [identity/signature](ENGINE_CORE.md), [ranh giới Host](HOST_CONTRACT.md), [vận hành](RUNTIME.md), [vùng mở](OPEN_STATE.md), [kiểm chứng bằng bản viết](WRITING_VALIDATION.md). Đây là vai trò tài liệu, không phải các bước thực thi engine.

## Ranh giới đọc/áp dụng — yêu cầu integrity của task

Đây là ràng buộc áp dụng do tác giả yêu cầu trong lần restructuring, không phải chứng cứ một run đã diễn ra hoặc một cơ chế tích hợp mới.

### Host input cần đối chiếu

Điều kiện regression/tồn tại ngoài tiến trình thường, authority cho phép nếu Host có, trạng thái nghĩa vụ, thông tin và agency của Regressor. Không áp một cơ chế World Will cho mọi Host.

### Thẩm quyền Host được giữ

Metaphysics, lịch sử, quan hệ xã hội, canon constraints, actor knowledge, quyền và khả năng có nguồn tiếp tục có thẩm quyền trong phạm vi của Host. Không rewrite Host để engine chạy; không biến vocabulary/claim của engine thành capability đã thực thi.

### Permission và local realization

Accommodation là cách diễn giải interface đã có nguồn, không cho phép rewrite cơ chế hồi quy của Host. Authority/Seat là Working; The Gun không tự cấp sức mạnh xuyên host.

Thay đổi cách biểu đạt/local realization chỉ được xem xét khi tương thích nguồn Host và identity ở ENGINE_CORE; sự cho phép thay chi tiết cụ thể chưa có nguồn vẫn UNKNOWN. Nếu không tương thích, giữ bất tương thích hoặc nêu giả định có nhãn, không âm thầm sửa engine/Host.

### Parallel progression

Nghĩa vụ, xử lý Regressor và hệ quả phải tương tác với tiến trình của Host. Sơ đồ duty discharged → rest không xóa Host progression; state tái nhập, timing và tác động regression lên timeline cụ thể: UNKNOWN.

```text
HOST RULES REMAIN AUTHORITATIVE WITHIN THEIR SCOPE
HOST ADAPTATION != ENGINE IDENTITY LOSS
ENGINE OUTPUT != REPLACEMENT HOST TIMELINE
```

Một scene chưa đi đến đủ hệ quả chỉ cho evidence trong phạm vi đã viết. Không xem thiếu đoạn tiếp diễn là bằng chứng Host đã dừng hoặc đã tiếp tục đúng.

## Các khối nguồn giữ nguyên phạm vi
