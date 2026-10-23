# Sloth — ENGINE_CORE

**Vai trò:** sở hữu identity, signature và ranh giới để engine vẫn là chính nó; không giữ full runtime hoặc lore summary.
**Trạng thái nguồn:** Working Draft; các mục Stable giữ đúng phạm vi của nguồn. Tái cấu trúc tài liệu không nâng canon, Working, Placeholder hoặc UNKNOWN. Các mô tả signature là cách đọc phân tích bám nguồn, không là quyết định canon mới.

Đọc theo nhu cầu: [identity/signature](ENGINE_CORE.md), [ranh giới Host](HOST_CONTRACT.md), [vận hành](RUNTIME.md), [vùng mở](OPEN_STATE.md), [kiểm chứng bằng bản viết](WRITING_VALIDATION.md). Đây là vai trò tài liệu, không phải các bước thực thi engine.


## Signature — cách đọc phân tích

- **Căng thẳng:** muốn dứt nghĩa vụ để trở về nghỉ nhưng vẫn phải xử lý lớp đối tượng liên tục được Entropy/Accommodation tạo điều kiện tồn tại.
- **Trọng lượng nội tại:** nguồn gọi `Accountability` là **Counter**: nghĩa vụ đã thuộc Sloth phải được hoàn tất; nó không biến Sloth thành chăm chỉ. Task này không tự đổi nhãn cơ chế riêng sang Governor.
- **Externalization:** Accommodation tương tác với điều kiện tồn tại của Regressor trong fiction; Graze và The Gun là phương thức/chi phí thực thi, không phải toàn bộ identity.
- **Hành vi nhận diện:** nghĩa vụ không thể bỏ mặc → tối thiểu hóa tương tác cần thiết → hoàn tất → quay lại nghỉ. Chỉ có một tay súng lười hoặc hiệu quả chưa đủ chứng minh signature.

Core Drive/Authority/Seat vẫn là Working. Checklist Stable ở trên giữ phân loại nguồn; cơ chế component do các file COMPONENTS sở hữu. Không dùng sơ đồ tích hợp như cam kết mọi host đều hỗ trợ hoặc như end-state narrative bắt buộc.

## Nguồn và provenance

Được phân bố từ [Sloth_Engine_Working_Draft.md](Sloth_Engine_Working_Draft.md). Bản đó giữ nguyên toàn bộ nội dung gốc dưới thông báo provenance; không còn là full specification hoạt động song song. Nội dung cơ chế hiện hành đọc ở các owner của package này. Canon/source authority không đổi chỉ vì đổi format.


# Sloth — Working Draft

## Trạng thái

Đây là concept đang được phát triển trong The Academy.

Lưu ý:

- Chỉ áp dụng định nghĩa nội bộ của project.
- Không dựa trên ý nghĩa truyền thống của Seven Deadly Sins.
- Sloth được xử lý như một Executor / narrative-engine module trong wrapper của The Academy.
- Các phần chưa chốt vẫn được giữ ở trạng thái Working Draft / Placeholder.

---


# 1. Vai trò

**Executor:** Sloth\
**Job hiện tại:** **Regressors Hunter**

Sloth không săn người yếu.

Đối tượng chính là các Regressor — một lớp HIP có khả năng thay đổi lịch sử ở quy mô lớn nhờ khả năng hồi quy, thử lại, tái tối ưu lựa chọn hoặc phủ quyết một trạng thái lịch sử đã xảy ra.

---


# 2. Core Drive — Working

Sloth không được xây như “lười biếng” theo nghĩa thông thường.

Core Drive hiện tại thiên về:

- giữ **Authority** của chính mình;
- không chấp nhận kẻ khác chiếm **Seat**;
- không chấp nhận quyền quyết định lịch sử bị chia sẻ;
- muốn hoàn tất nghĩa vụ càng nhanh càng tốt để “dứt nợ” và quay lại trạng thái không phải hành động.

Authority, Seat và “dứt nợ” hiện là các trục vận hành của Sloth, chưa phải định nghĩa cuối cùng đã khóa.

---


# 3. Paradox

The Academy là một **Entropy Engine**.

Entropy liên tục tạo điều kiện để các Regressor xuất hiện.

Điều đó tạo ra nghịch lý trực tiếp đối với Sloth:

- Regressor liên tục xâm phạm hoặc ngồi vào vị trí Authority mà Sloth xem là Seat của mình;
- chính Entropy Engine lại liên tục tạo điều kiện cho lớp đối tượng này tồn tại;
- Sloth muốn ngồi yên, nhưng càng có Regressor thì càng bị buộc phải đứng dậy xử lý;
- vì vậy sự tồn tại của Sloth bên trong một Entropy Engine tự nó đã là một paradox có thể được khai thác thành chức năng.

The Academy không loại bỏ paradox này.

Nó cung cấp **purpose**, **counter** và **catalyst** để biến paradox thành một operation có ích cho engine.

---


# 4. Counter — Accountability

**Accountability** là counter của Sloth.

Vai trò:

- không làm Sloth thay đổi bản chất;
- không biến Sloth thành “chăm chỉ”;
- buộc Sloth phải hoàn thành trách nhiệm của một Executor;
- ngăn khả năng bỏ mặc nghĩa vụ;
- biến paradox thành công việc có ích cho Entropy Engine.

Accountability tạo ràng buộc:

> Một khi nghĩa vụ đã thuộc về Sloth, nó phải được xử lý đến cùng.

Vì Sloth muốn thoát khỏi nghĩa vụ nhanh nhất có thể, counter này không triệt tiêu Sloth mà ép bản chất của Sloth tự tìm đường tối thiểu để hoàn thành công việc.

---


# 11. Stable Elements

## Stable

- Sloth là Executor của The Academy.
- Job: **Regressors Hunter**.
- Counter: **Accountability**.
- Catalyst: **Accommodation**.
- Doctrine: **Graze**.
- Tool: **The Gun**.
- Regressor là một lớp HIP rất cao.
- Graze tối thiểu hóa tương tác không cần thiết.
- The Gun phục vụ mục tiêu kết thúc nghĩa vụ nhanh nhất có thể.
- Accommodation tạo điều kiện cho lớp đối tượng mà Sloth phải săn.
- Sloth tồn tại như một paradox bên trong Entropy Engine.
- Accountability không sửa Sloth; nó buộc Sloth phải hoàn thành nghĩa vụ.

---
