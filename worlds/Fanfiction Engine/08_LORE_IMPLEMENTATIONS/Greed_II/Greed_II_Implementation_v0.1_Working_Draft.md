# Greed II — Hồ sơ triển khai v0.1 (Working Draft)

## 0. Trạng thái và ranh giới

**Trạng thái:** Bản tách thông tin từ [Greed_II_Core_Interfaces_Consolidated.md](../../source_archive/Greed/Greed_II_Core_Interfaces_Consolidated.md); không tự xác nhận canon mới.

Tài liệu này giữ các dữ kiện về **Greed II như một cá thể, vũ khí và bối cảnh vận hành cụ thể**. Cơ chế Greed ở mức Narrative Engine được trình bày riêng tại [Greed Core v0.2](../../04_NARRATIVE_ENGINES/Greed/Greed_Narrative_Engine_Core_v0.2_Working_Draft.md); quy trình Ring tại [Ring interface](../../04_NARRATIVE_ENGINES/Greed/Ring_Interface_v0.1_Working_Draft.md), với [the ring.txt](../../source_archive/Greed/the%20ring.txt) là nguồn gốc để đối chiếu.

Tách hồ sơ cá thể khỏi hồ sơ engine là thay đổi **cách tổ chức tài liệu**. Quan hệ bản thể chính xác giữa Greed II và Greed Narrative Engine, kể cả khả năng engine chạy không cần Greed II, vẫn là `UNKNOWN`.

## 1. Greed II — danh tính và năng lực

Theo bản hợp nhất, Greed II không phải Greed I. Greed II bắt đầu là backup avatar của Greed I; sau khi Greed I bị phản bội và thất bại, avatar phát triển ý chí độc lập. Greed I chấp nhận cho cá thể đó kế thừa vị trí rồi kết thúc cycle trước. Greed II vì vậy được mô tả như một cá thể độc lập, không chỉ là bản sao.

Năng lực tự thân được ghi là pháp sư hạng ba, không chủ yếu là chiến binh, kiếm sĩ hay kỵ sĩ. Phần lớn sức mạnh chiến đấu đến từ hệ vũ khí và Five Servants. Greed II thường tránh giao chiến và leo thang, chỉ đánh khi cần.

Đây là đặc tính của **Greed II**; không dùng cấp pháp sư, tiểu sử hoặc sở thích chiến đấu của cá thể này làm định nghĩa Greed Narrative Engine.

## 2. Greed Axe / Five Servants

Lõi vũ khí là gia đình năm người trở thành hệ vũ khí phục vụ Greed II sau một biến cố lớn:

| Thành viên | Ghi nhận trong nguồn |
| --- | --- |
| Cha, mẹ | Tương đối thoải mái khi ở cạnh Greed II. |
| Con cả, con thứ, con út | Thường tranh cãi, kể cả khi chiến đấu. |

Họ giữ ý chí riêng, không phải trang bị vô tri. Sự bất hòa làm giảm hiệu quả hợp nhất, hiệu suất chiến đấu và độ kết dính của True Form. Đây là lỗi cơ học của **hệ vũ khí Five Servants**, chưa phải failure mode phổ quát của Greed Engine.

Bản hợp nhất gắn hệ vũ khí với các chủ đề trách nhiệm, trải nghiệm, kế thừa, gia đình, kết nối và hợp nhất. Đó là thematic core của vũ khí trong bản triển khai này, không tự động là bộ tiêu chí của Greed Narrative Engine.

Vũ khí ban đầu là **Divine Halberd**. Sau khi hợp nhất với Greed II và Five Servants, phương thức tồn tại của nó thay đổi. Các form là các biểu hiện của cùng một thực thể, **không phải các nấc tiến hóa**; True Form trở về dạng Divine Halberd ban đầu.

## 3. Các dạng vũ khí được ghi nhận

| Dạng | Kích hoạt, hình thái và chức năng |
| --- | --- |
| **Open Form** | Rìu bổ củi thông thường; trạng thái nghỉ, không biểu hiện sức mạnh nổi bật. |
| **Form 1 — Astaroth** | Greed II hy sinh máu làm môi giới; rìu tay một lưỡi với họa tiết đầu lâu. Càng giết càng mạnh; là dạng chiến đấu thường dùng. `Astaroth` là battle name, không phải True Name, và gia đình vũ khí không đặc biệt thích tên này. |
| **Form 2 — Ampte** | Battle call `Rage On`; Greed II hy sinh nửa mana. Rìu chiến cán dài, hình cong để tích động lượng, thuộc tính Fire. Khi đủ động lượng có thể triệu hồi Fire Spirit King cho đòn AOE; đây là dạng thiên về bùng nổ. `Ampte` là battle name, không phải True Name, và gia đình vũ khí không đặc biệt thích tên này. |
| **Form 3 — True Form** | Greed II hy sinh nửa sinh mệnh và toàn bộ mana. Vũ khí trở về Divine Halberd nguyên thủy, thuộc tính Astral chứ không phải Fire. Có Astral Wraith Horse mang giáp đầy đủ và một nữ rider theo thiết kế heavy cavalry. Greed II, vũ khí, servants, rider và mount hợp nhất thành một trạng thái chiến đấu; bản hợp nhất dùng phép so sánh “Oversoul-like”. True Name chưa được chốt trong bộ nguồn được hợp nhất. |

Thiết kế nữ rider trong nguồn: giáp toàn thân, định hướng heavy cavalry, ảnh hưởng fantasy Đông Á, nhiều lớp lamellar và thiết kế thực dụng; không fanservice hay breast-shaped armor. Bảng màu True Form: Ash Black/Mud Gray chủ đạo, Blood Red gradient thứ cấp, Blue Astral Spark làm điểm nhấn.

Các vũ khí khi Five Servants tách ra mới ở mức **concept**, có thể thay đổi: cha và mẹ dùng Sickle and Chain; con cả Medium Sword; con thứ Slingshot; con út Karambit.

## 4. Paradox trong triển khai Greed II

Bản hợp nhất mô tả ham muốn của Greed II thiên về **muốn được người khác tự nguyện trao** hơn là đoạt lấy. Từ chối vì thế mang ý nghĩa bị bác bỏ, không chỉ là mất vật thể.

Trong quy trình Ring đang được mô tả, Greed II có hai áp lực đối lập:

- Với vai trò nhân viên The Academy, người nhận tự nguyện trả Ring là cách khép chu trình trách nhiệm và trải nghiệm; sự từ chối khiến trạng thái hoàn tất lý tưởng thất bại.
- Với tư cách Avatar of Greed, sự từ chối mở ra cuộc giao chiến với người mà Greed II đã theo dõi và góp phần nuôi dưỡng. Nguồn mô tả Greed II đồng thời khao khát trải nghiệm ấy.

Các cách nói “farmer who raises bosses”, người nhận có thể đạt mức gần demigod, và Founder quan sát paradox của chính Greed II đều thuộc **mô hình/bối cảnh cá thể trong bản hợp nhất**. Chúng không chứng minh mọi người nhận Ring sẽ mạnh như vậy hoặc Founder/KPI là thành phần bắt buộc của Greed Narrative Engine.

Mô hình **Infinite Rings → Infinite Responsibilities** cũng thuộc lớp Paradox đang chờ quyết định tích hợp. [the ring.txt](../../source_archive/Greed/the%20ring.txt) để số lượng Ring là placeholder; hồ sơ này không nâng Infinite Rings thành canon ổn định.

## 5. Quan hệ với cơ chế Ring

Greed II là người trao, quan sát và yêu cầu trả Ring trong cấu hình hiện được hai nguồn ghi lại. Nếu người nhận từ chối, nguồn mô tả Greed II giao chiến; **chỉ khi Greed II thắng** thì Ring bị chính Greed II phá hủy. Kết quả giao chiến khác là `UNKNOWN`.

Greed Axe có thể tham gia giải quyết nhánh giao chiến của Greed II, nhưng nguồn không xác lập Axe là điều kiện bắt buộc để Ring tạo trải nghiệm, để người nhận tự nguyện trả Ring, hoặc để mọi triển khai Greed Engine vận hành. Quy trình và giới hạn Ring được giữ tại [Ring interface](../../04_NARRATIVE_ENGINES/Greed/Ring_Interface_v0.1_Working_Draft.md), với [the ring.txt](../../source_archive/Greed/the%20ring.txt) và bản lõi engine để đối chiếu; hồ sơ này không lặp lại đặc tả Ring.

## 6. Ghi chú về quá trình thiết kế và phần chưa chốt

Bản hợp nhất mô tả quá trình thiết kế vũ khí bằng lặp lại concept, nhập vai/mô phỏng động tác vật lý tương tự, quan sát quán tính, bán kính vung, trọng tâm, chuyển động và cảm giác cầm, rồi điều chỉnh. Đây là **provenance thiết kế**, không phải quy tắc vận hành trong fiction.

Các phần chưa chốt trong bộ nguồn được hợp nhất gồm cosmology, Citadel, Seven Seats, lịch sử chi tiết và True Name cuối cùng của Form 3. Các tệp đặt tên xuất hiện ngoài ba nguồn mà bản hợp nhất đã chọn không được tự nhập vào bản tách này.

Việc chuyển paradox của Greed II thành invariant cho Greed Narrative Engine, hoặc xác định một actor khác có thể vận hành engine, cần xác nhận riêng của người tạo.
