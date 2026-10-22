# Greed — Narrative Engine Core v0.2 (Working Draft)

## Trạng thái và nguồn

Bản này tiếp nối [v0.1](../../source_archive/Greed/Greed_Narrative_Engine_Core_v0.1_Working_Draft.md) để ghi nhận quyết định trực tiếp của tác giả về Governor. Đây là bản tổ chức cơ chế, không tự xác lập canon cho các vùng chưa rõ. [Xác nhận tác giả](../../The_Academy_Authorial_Decisions_2026-09-28.md) có thẩm quyền đối với cách phân loại `Responsibility` và `Greed Paradox`; [bản hợp nhất Greed II](../../source_archive/Greed/Greed_II_Core_Interfaces_Consolidated.md) và [nguồn Ring](../../source_archive/Greed/the%20ring.txt) lưu mô tả gốc.

## Phạm vi engine

Greed là một Narrative Engine có **Governor là Responsibility**: đã tham điều gì thì phải có trách nhiệm đến cùng với điều đó. Governor này giữ Greed khỏi cách đọc trope chỉ xoay quanh tích trữ hoặc chiếm đoạt; nó không định trước kết quả của một câu chuyện, mức trách nhiệm cụ thể của mọi host, hay phương thức thực thi ngoài nguồn hiện có.

Trong cấu hình đã được ghi nhận, [Ring interface](Ring_Interface_v0.1_Working_Draft.md) vận hành cùng Greed: trao cơ hội và lợi ích cho người nhận, cho trải nghiệm và lựa chọn tích lũy qua phần lớn cuộc đời, rồi đặt ra yêu cầu tự nguyện trao trả. Quan hệ cơ chế này được ghi nhận; tính bắt buộc của vật thể Ring trong mọi cấu hình, khả năng chạy độc lập và tính portable sang host khác vẫn là `UNKNOWN`.

**Greed Paradox** giải thích Sin Greed trong bối cảnh Greed II: Greed II muốn được trao, nhưng sự từ chối cũng mở ra cuộc giao chiến mà cá thể ấy khao khát. Nó không phải tên Governor và không tự thành invariant của mọi Greed Engine. Tiểu sử Greed I/II, tư cách nhân viên The Academy, Founder, KPI và Greed Axe/Five Servants thuộc [hồ sơ triển khai Greed II](../../08_LORE_IMPLEMENTATIONS/Greed_II/Greed_II_Implementation_v0.1_Working_Draft.md).

## Chu trình được ghi nhận

```text
chọn người nhận phù hợp [tiêu chí: UNKNOWN]
→ trao Ring và lợi ích [chi tiết: UNKNOWN]
→ sống cùng Ring trong phần lớn cuộc đời; lựa chọn và trải nghiệm phát sinh
→ Greed yêu cầu trao trả
→ tự nguyện tháo và trao trả?
    CÓ   → chu trình Ring khép theo điều kiện tự nguyện
    KHÔNG → giao chiến
             Greed thắng → Ring bị phá hủy, không thu hồi bằng vũ lực
             kết quả khác → UNKNOWN
```

Trải nghiệm của người nhận là thứ Greed thu nhận theo nguồn. Thành công, thất bại và lựa chọn của người nhận không được định sẵn. `the ring.txt` có bước “Đạt được thành công”, trong khi bản hợp nhất ghi cả thành công và thất bại; bản này không biến thành công thành điều kiện bắt buộc.

## Ranh giới chưa chốt

- Tiêu chí chọn người nhận, cơ chế và lợi ích Ring, giới hạn sức mạnh, nguồn gốc, số lượng Ring và cách Greed thu nhận trải nghiệm.
- Kết quả khi người nhận từ chối nhưng Greed không thắng; cách Governor vận hành ngoài cấu hình đang được mô tả.
- Sự phụ thuộc bản thể giữa Greed Engine, Greed II, Ring và host; tính portable của mỗi thành phần.
- `Infinite Rings` là giả định ở lớp Greed Paradox trong bản hợp nhất, trong khi nguồn Ring để số lượng là placeholder; chưa nâng thành canon ổn định.
- Ring được gọi là chất xúc tác **cho một cuộc đời** trong nguồn; nhãn đó không tự chứng minh Ring là một `Catalyst` theo ontology chung của project.
