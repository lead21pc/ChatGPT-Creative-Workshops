# Greed — ENGINE_CORE

**Vai trò:** sở hữu identity, signature và ranh giới để engine vẫn là chính nó; không giữ full runtime hoặc lore summary.
**Trạng thái nguồn:** Working Draft v0.2; Governor theo xác nhận tác giả. Tái cấu trúc tài liệu không nâng canon, Working, Placeholder hoặc UNKNOWN. Các mô tả signature là cách đọc phân tích bám nguồn, không là quyết định canon mới.

Đọc theo nhu cầu: [identity/signature](ENGINE_CORE.md), [ranh giới Host](HOST_CONTRACT.md), [vận hành](RUNTIME.md), [vùng mở](OPEN_STATE.md), [kiểm chứng bằng bản viết](WRITING_VALIDATION.md). Đây là vai trò tài liệu, không phải các bước thực thi engine.


## Signature — cách đọc phân tích

- **Căng thẳng:** ham muốn phải mang trách nhiệm đến cùng; trong cấu hình Ring đã có nguồn, cơ hội sống và trải nghiệm kéo dài dẫn tới yêu cầu tự nguyện buông lợi ích.
- **Trọng lượng nội tại:** `Responsibility` là Governor đã được tác giả xác nhận; không xóa ham muốn, không áp đặt người nhận phải đạt thành công hoặc phải tự nguyện trả. Không nâng Greed Paradox của Greed II thành Governor thứ hai.
- **Externalization đã có nguồn:** [interface Ring](COMPONENTS/Ring.md); cơ chế host khác hoặc Greed không cần Ring chưa được chốt.
- **Hành vi nhận diện:** cơ hội/lợi ích → tích lũy trải nghiệm và lựa chọn → thử thách tự nguyện trao trả; không thể thay bằng tích trữ vật phẩm hoặc cưỡng đoạt mà giữ nguyên cấu hình này.

Đây là signature của cấu hình đã externalize, không chứng minh mọi Greed configuration bắt buộc có Ring. Bỏ Responsibility hoặc biến tự nguyện trao trả thành thu hồi cưỡng bức làm sai phần cơ chế đã ghi nhận; khả năng abstraction ngoài cấu hình này vẫn thuộc OPEN_STATE.

## Nguồn và provenance

Được phân bố từ [Greed_Narrative_Engine_Core_v0.2_Working_Draft.md](Greed_Narrative_Engine_Core_v0.2_Working_Draft.md). Bản đó giữ nguyên toàn bộ nội dung gốc dưới thông báo provenance; không còn là full specification hoạt động song song. Nội dung cơ chế hiện hành đọc ở các owner của package này. Canon/source authority không đổi chỉ vì đổi format.


## Trạng thái và nguồn

Bản này tiếp nối [v0.1](<../../source_archive/Greed/Greed_Narrative_Engine_Core_v0.1_Working_Draft.md>) để ghi nhận quyết định trực tiếp của tác giả về Governor. Đây là bản tổ chức cơ chế, không tự xác lập canon cho các vùng chưa rõ. [Xác nhận tác giả](<../../The_Academy_Authorial_Decisions_2026-09-28.md>) có thẩm quyền đối với cách phân loại `Responsibility` và `Greed Paradox`; [bản hợp nhất Greed II](<../../source_archive/Greed/Greed_II_Core_Interfaces_Consolidated.md>) và [nguồn Ring](<../../source_archive/Greed/the ring.txt>) lưu mô tả gốc.


## Phạm vi engine

Greed là một Narrative Engine có **Governor là Responsibility**: đã tham điều gì thì phải có trách nhiệm đến cùng với điều đó. Governor này giữ Greed khỏi cách đọc trope chỉ xoay quanh tích trữ hoặc chiếm đoạt; nó không định trước kết quả của một câu chuyện, mức trách nhiệm cụ thể của mọi host, hay phương thức thực thi ngoài nguồn hiện có.
