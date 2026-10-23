# Greed — HOST_CONTRACT

**Vai trò:** sở hữu ranh giới Host ↔ engine ↔ tiến trình Host đang tiếp tục; không thay luật Host hoặc định nghĩa runtime bên trong.
**Trạng thái nguồn:** Working Draft v0.2; Governor theo xác nhận tác giả. Tái cấu trúc tài liệu không nâng canon, Working, Placeholder hoặc UNKNOWN. Các mô tả signature là cách đọc phân tích bám nguồn, không là quyết định canon mới.

Đọc theo nhu cầu: [identity/signature](ENGINE_CORE.md), [ranh giới Host](HOST_CONTRACT.md), [vận hành](RUNTIME.md), [vùng mở](OPEN_STATE.md), [kiểm chứng bằng bản viết](WRITING_VALIDATION.md). Đây là vai trò tài liệu, không phải các bước thực thi engine.

## Ranh giới đọc/áp dụng — yêu cầu integrity của task

Đây là ràng buộc áp dụng do tác giả yêu cầu trong lần restructuring, không phải chứng cứ một run đã diễn ra hoặc một cơ chế tích hợp mới.

### Host input cần đối chiếu

State/đời sống của người nhận con người trong cấu hình Ring; lợi ích, lựa chọn, trải nghiệm, yêu cầu tự nguyện trao trả và nhánh giao chiến theo RUNTIME. Tiêu chí chọn, năng lực thực thi và cách Greed thu nhận trải nghiệm chưa chốt.

### Thẩm quyền Host được giữ

Metaphysics, lịch sử, quan hệ xã hội, canon constraints, actor knowledge, quyền và khả năng có nguồn tiếp tục có thẩm quyền trong phạm vi của Host. Không rewrite Host để engine chạy; không biến vocabulary/claim của engine thành capability đã thực thi.

### Permission và local realization

Lợi ích/cơ hội và phép thử trao trả là cơ chế đã có nguồn; không bảo đảm thành công hoặc tự nguyện trả. Không nhập tiểu sử, việc làm, Axe/Five Servants của Greed II vào universal engine.

Thay đổi cách biểu đạt/local realization chỉ được xem xét khi tương thích nguồn Host và identity ở ENGINE_CORE; sự cho phép thay chi tiết cụ thể chưa có nguồn vẫn UNKNOWN. Nếu không tương thích, giữ bất tương thích hoặc nêu giả định có nhãn, không âm thầm sửa engine/Host.

### Parallel progression

Hệ quả lựa chọn/trao trả/giao chiến phải được writer đặt vào diễn tiến Host đang tiếp tục. Cơ chế tích hợp state, lịch tái xuất và compatibility xuyên host cụ thể: UNKNOWN.

```text
HOST RULES REMAIN AUTHORITATIVE WITHIN THEIR SCOPE
HOST ADAPTATION != ENGINE IDENTITY LOSS
ENGINE OUTPUT != REPLACEMENT HOST TIMELINE
```

Một scene chưa đi đến đủ hệ quả chỉ cho evidence trong phạm vi đã viết. Không xem thiếu đoạn tiếp diễn là bằng chứng Host đã dừng hoặc đã tiếp tục đúng.

## Các khối nguồn giữ nguyên phạm vi



Trong cấu hình đã được ghi nhận, [Ring interface](COMPONENTS/Ring.md) vận hành cùng Greed: trao cơ hội và lợi ích cho người nhận, cho trải nghiệm và lựa chọn tích lũy qua phần lớn cuộc đời, rồi đặt ra yêu cầu tự nguyện trao trả. Quan hệ cơ chế này được ghi nhận; tính bắt buộc của vật thể Ring trong mọi cấu hình, khả năng chạy độc lập và tính portable sang host khác vẫn là `UNKNOWN`.

**Greed Paradox** giải thích Sin Greed trong bối cảnh Greed II: Greed II muốn được trao, nhưng sự từ chối cũng mở ra cuộc giao chiến mà cá thể ấy khao khát. Nó không phải tên Governor và không tự thành invariant của mọi Greed Engine. Tiểu sử Greed I/II, tư cách nhân viên The Academy, Founder, KPI và Greed Axe/Five Servants thuộc [hồ sơ triển khai Greed II](<../../08_LORE_IMPLEMENTATIONS/Greed_II/Greed_II_Implementation_v0.1_Working_Draft.md>).
