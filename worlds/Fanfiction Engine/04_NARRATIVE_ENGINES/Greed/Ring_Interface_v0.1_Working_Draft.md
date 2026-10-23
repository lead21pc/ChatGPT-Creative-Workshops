# Thông báo trạng thái nguồn — Greed

**Vai trò hiện tại:** provenance của cấu trúc tài liệu trước restructuring; không còn là full specification/component owner hoạt động song song. Nội dung canon/Working/Placeholder/UNKNOWN không bị phủ định hoặc nâng trạng thái.

**Owner hiện hành:** [nguồn thay thế về tổ chức tài liệu](COMPONENTS/Ring.md); [runtime](RUNTIME.md), [Host contract](HOST_CONTRACT.md), [open state](OPEN_STATE.md), [writer validation](WRITING_VALIDATION.md).

Toàn bộ nội dung gốc nằm nguyên byte bên dưới để giữ provenance và các liên kết từ nguồn đóng băng. Không chuyển/sửa archive theo hard freeze của task. Các mục genealogy/đối chiếu lịch sử bên dưới vẫn được đọc đúng phạm vi lịch sử, không là nguồn mặc định cho cơ chế active.

**SHA-256 của nội dung gốc:** `9f72fda14d0f457e819857092672d19c44e5d3fb5aff7150f57f872a3baeffcc`.

<!-- BEGIN PRESERVED ORIGINAL -->
# Ring — interface của Greed v0.1 (Working Draft)

## Trạng thái

Bản tách cơ chế từ [the ring.txt](../../source_archive/Greed/the%20ring.txt) và phần Ring của [bản hợp nhất Greed II](../../source_archive/Greed/Greed_II_Core_Interfaces_Consolidated.md). Hai nguồn được giữ trong `source_archive` để đối chiếu. Bản này không xác nhận một cơ chế hoặc outcome mới. Đọc cùng [Greed Engine Core v0.2](Greed_Narrative_Engine_Core_v0.2_Working_Draft.md).

## Vai trò và quy trình

Ring là công cụ tạo điều kiện cho trải nghiệm độc nhất của một con người; không chỉ là vật phẩm tăng sức mạnh, phần thưởng hoặc vật thể Greed muốn tích trữ. Nguồn gọi nó là cơ hội, phép thử và chất xúc tác cho một cuộc đời. Đây là mô tả chức năng trong cấu hình Greed hiện có, chưa phải phân loại `Catalyst` theo ontology chung.

1. Greed chọn một người phù hợp và trao Ring. Tiêu chí chọn và điều kiện tiếp nhận chưa được xác định.
2. Ring cho người nhận lợi ích trong phần lớn cuộc đời. Lợi ích cụ thể chưa được xác định; yêu cầu thiết kế của nguồn là đủ tạo thay đổi và lựa chọn có ý nghĩa nhưng không làm phép thử mất giá trị.
3. Trải nghiệm, lựa chọn, thành công và thất bại của người nhận phát sinh trong đời sống cùng Ring; Greed thu nhận trải nghiệm đó theo nguồn. Cách thu nhận chưa được mô tả.
4. Greed trở lại và yêu cầu người nhận **tự nguyện tháo Ring, trao trả**. Đây là điều kiện hoàn tất được nêu rõ.
5. Nếu người nhận từ chối, Greed giao chiến. Nếu Greed thắng, Greed phá hủy Ring thay vì lấy lại bằng vũ lực. Kết quả khi Greed không thắng là `UNKNOWN`.

Phép thử cuối cùng là người nhận có thể tự nguyện buông lợi ích sau thời gian dài hay không. Nó không phải phép đo ai mạnh, giàu hoặc thành công nhất. `the ring.txt` có bước “Đạt được thành công”; bản hợp nhất ghi cả thành công và thất bại, nên thành công không được đặt làm điều kiện bắt buộc của interface này.

## Giới hạn

- Nguồn gốc, cơ chế, giới hạn sức mạnh, lợi ích chính xác và số lượng Ring: placeholder.
- `Infinite Rings` xuất hiện trong nguồn Greed Paradox nhưng xung đột với placeholder về số lượng ở nguồn Ring; trạng thái ổn định chưa được chốt.
- Nguồn hiện mô tả người nhận là con người. Áp dụng cho đối tượng khác, host khác hoặc chạy Ring độc lập với Greed: `UNKNOWN`.
- Quan hệ giữa Ring và Governor `Responsibility` được giải thích trong [Greed Core](Greed_Narrative_Engine_Core_v0.2_Working_Draft.md); interface này không biến trách nhiệm thành một outcome bắt buộc của người nhận.
