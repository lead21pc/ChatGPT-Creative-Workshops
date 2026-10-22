# Greed — Narrative Engine Core v0.1 (Working Draft)

## 0. Trạng thái và phạm vi

**Trạng thái:** Bản tách tài liệu đang xét; không tự nâng nội dung nguồn thành canon mới hoặc tuyên bố thay thế hai tệp nguồn.

Tài liệu này mô tả **Greed như một Narrative Engine** ở mức cơ chế. Nó không dùng tiểu sử Greed I/II, vai trò nhân viên The Academy, Five Servants hay Greed Axe làm định nghĩa của engine. Các dữ kiện đó thuộc hồ sơ triển khai `Greed_II_Implementation_v0.1_Working_Draft.md`.

Nguồn đối chiếu được giữ nguyên:

- `Greed_II_Core_Interfaces_Consolidated.md`: bản hợp nhất working draft, đặc biệt các mục 8 và 11–18.
- `the ring.txt`: nguồn working draft mô tả chi tiết quy trình Ring.

**Ranh giới:** Việc tách tài liệu không chứng minh Greed Engine có thể chạy thiếu Greed II, không chứng minh Ring có thể chạy độc lập, và không thiết lập tính portable sang host khác. Các quan hệ đó vẫn là `UNKNOWN`.

## 1. Cơ chế đang có nguồn mô tả

Trong cấu hình được hai nguồn trên mô tả, **quy trình Ring là giao diện vận hành gắn với Greed**. Ring tạo cơ hội và lợi ích cho một người nhận, tạo điều kiện để lựa chọn và trải nghiệm tích lũy qua phần lớn cuộc đời họ. Greed quan sát/thu nhận trải nghiệm đó và đến lúc kết thúc yêu cầu người nhận tự nguyện tháo Ring, trao trả.

Nguồn gọi Ring là công cụ tạo trải nghiệm, phép thử và chất xúc tác; nó không được mô tả như phần thưởng hay mục tiêu thu gom vật thể. Kết quả lịch sử, mức thành công của người nhận và lựa chọn cuối cùng không được xác định trước bởi mô tả cơ chế này.

Đây là **cơ chế hiện được ghi nhận**, chưa phải tuyên bố rằng mọi triển khai tương lai của Greed đều bắt buộc giữ cùng vật thể, actor hoặc host.

## 2. Quy trình và các nhánh đã được mô tả

```text
chọn người nhận phù hợp [tiêu chí: UNKNOWN]
→ trao Ring [điều kiện tiếp nhận: UNKNOWN]
→ người nhận sống cùng Ring trong phần lớn cuộc đời
→ lợi ích, lựa chọn và trải nghiệm phát sinh
→ Greed đến yêu cầu trao trả
→ người nhận tự nguyện tháo Ring và trao trả?
    CÓ  → chu trình Ring hoàn tất theo điều kiện trả tự nguyện
    KHÔNG → Greed giao chiến
              Greed thắng → Ring bị Greed phá hủy, không thu hồi
              kết quả khác → UNKNOWN
```

**Điều kiện hoàn tất** là sự tự nguyện trao trả. Nhánh dùng vũ lực không được viết thành “thu hồi thành công”: nguồn nói Ring bị phá hủy **nếu Greed thắng**. Nguồn chưa xác định kết quả khi Greed thua hoặc giao chiến không kết thúc theo nhánh đó.

`the ring.txt` có bước “Đạt được thành công”, còn bản hợp nhất mô tả cả thành công, thất bại và lựa chọn. Bản tách này không biến thành công thành kết quả bắt buộc; ý nghĩa chính xác của bước đó cần được người tạo xác nhận.

## 3. Đầu ra và giới hạn suy luận

- **Đầu ra được mô tả:** trải nghiệm độc nhất của người nhận và lựa chọn của họ khi được yêu cầu buông Ring. Nguồn nói Greed thu nhận trải nghiệm trong thời gian người nhận giữ Ring; cách ghi nhận/truyền/giới hạn của quá trình này chưa được mô tả.
- **Lợi ích Ring:** nguồn đặt **yêu cầu thiết kế** rằng lợi ích phải đủ sức thay đổi đời người nhận và tạo lựa chọn có ý nghĩa, nhưng không áp đảo đến mức làm mất giá trị phép thử. Loại lợi ích, cơ chế và giới hạn sức mạnh vẫn là placeholder; yêu cầu này chưa chứng minh một Ring cụ thể đã đạt mức đó.
- **Phép thử:** khả năng tự nguyện buông lợi ích sau thời gian dài. Câu “sở hữu chính mình” trong nguồn là cách diễn giải triết lý; tài liệu này không biến nó thành thước đo kỹ thuật hoặc tiêu chí HIP.
- **Người nhận:** nguồn hiện nói về một con người. Khả năng áp dụng cho đối tượng khác là `UNKNOWN`.
- **HIP:** hai nguồn này không đặt tiêu chí HIP cho việc chọn người nhận. “Phù hợp” không tự định nghĩa thành một nhóm HIP hay một điểm số.

## 4. Greed Paradox: ranh giới giữa engine và Greed II

Bản hợp nhất mô tả Greed II muốn **được trao** hơn là chiếm lấy; việc tự nguyện trả Ring hoàn tất trách nhiệm, còn sự từ chối mở ra trận đấu mà Greed II đồng thời khao khát. Đó là áp lực hành vi được ghi trong cấu hình hiện tại.

**[PROPOSAL — chưa phải invariant canon của engine]** Có thể dùng mâu thuẫn `muốn nhận sự trao trả tự nguyện ↔ muốn đối diện sự từ chối` làm trục phân tích Greed Narrative Engine. Cần người tạo xác nhận trước khi khẳng định mọi triển khai Greed đều có cùng ham muốn, vai trò nhân viên/Avatar, hoặc cùng cách giải quyết bằng chiến đấu.

Các chi tiết Founder, KPI của nhân viên, khả năng người nhận gần mức demigod và Five Servants thuộc ngữ cảnh Greed II; chúng không được dùng làm điều kiện phổ quát của cơ chế Ring.

## 5. Trạng thái chưa chốt

- Tiêu chí chọn người nhận và điều kiện họ nhận Ring.
- Nguồn gốc, số lượng, lợi ích chính xác, cơ chế thu nhận trải nghiệm và giới hạn của Ring.
- Kết quả khi người nhận từ chối nhưng Greed không thắng.
- Điều kiện vận hành Greed Engine ngoài cấu hình Greed II đang được mô tả.
- Ring vật thể có bắt buộc trong mọi host hay không; điều kiện tương thích với host.
- Greed Paradox của Greed II có phải invariant của Narrative Engine hay không.
- Mệnh đề **Infinite Rings**: bản hợp nhất ghi đây là giả định ở lớp Paradox, còn `the ring.txt` để số lượng Ring là placeholder. Không tự nâng thành canon ổn định.

## 6. Quy tắc đọc cùng hồ sơ triển khai

`Greed_II_Implementation_v0.1_Working_Draft.md` lưu các đặc tính của Greed II, vũ khí và bối cảnh cụ thể. Chúng có thể tham gia quy trình Ring trong bản triển khai đang ghi, nhưng sự có mặt cùng nhau không tự chứng minh chúng là thành phần bắt buộc của mọi Greed Narrative Engine. Khi cần quy trình Ring chi tiết, đối chiếu `the ring.txt` thay vì suy ra từ mô tả vũ khí.
