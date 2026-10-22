# The Academy — Xác nhận tác giả ngày 2026-09-28

- **Trạng thái:** `USER_CONFIRMED`.
- **Nguồn:** xác nhận trực tiếp của tác giả trong hội thoại ngày 2026-09-28.
- **Phạm vi:** phân loại ontology và thẩm quyền nguồn của The Academy; không viết thêm lore hoặc outcome.

Tài liệu này ghi các quyết định dưới đây để đọc cùng nguồn gốc. Khi một nhãn cũ mâu thuẫn với quyết định được nêu rõ ở đây, chỉ **nhãn/phân loại đó** được cập nhật; phần cơ chế và các vùng `UNKNOWN` khác của nguồn không tự thay đổi.

## 1. Greed

- `Greed --GOVERNED_BY--> Responsibility`. **Responsibility** là Governor của Greed.
- **Greed Paradox** giải thích Greed Sin trong bối cảnh đang được mô tả. Nó không được dùng làm tên Governor thay cho Responsibility hoặc tự tạo thêm một Governor thứ hai.
- [Genealogy](06_ENGINE_GENEALOGY/engine_genealogy_and_development_updated.md) đã gọi Responsibility là Governor. Nhãn “Integrated Behavioral Governor” dành cho Greed Paradox trong [bản hợp nhất Greed II](source_archive/Greed/Greed_II_Core_Interfaces_Consolidated.md) là nhãn phân loại cũ tại phạm vi hồ sơ đó; phần mô tả paradox của Greed II vẫn là nguồn về bối cảnh triển khai, không trở thành định nghĩa phổ quát của Greed Engine.

## 2. Thuật ngữ chống trope

**Governor** là thuật ngữ hiện hành cho định nghĩa điều tiết một Sin/domain rộng để chống cách đọc trope. **Counter** là cách gọi cũ đối với **định nghĩa chống trope nói chung**. Xác nhận này không tự đổi nhãn mọi cơ chế riêng đang được gọi là Counter trong các working draft; việc phân loại từng cơ chế phải đối chiếu vai trò và nguồn của chính nó.

## 3. Nguồn Chaos

[Chaos Engine Canon Specification v3](04_NARRATIVE_ENGINES/Chaos/Chaos_Engine_Canon_Specification_v3.md) là **bản chính thức** cho Chaos Engine. [Bản `updated`](source_archive/Chaos/Chaos_Engine_Canon_Specification_updated.md) được giữ để đối chiếu provenance; khi hai bản bất đồng về Chaos, dùng `v3` làm bản dẫn, không tự hợp nhất các câu bị lược bỏ.

## 4. Historical Influence Potential và ảnh

[Historical_Influence_Potential.md](01_HIP/Historical_Influence_Potential.md) là tài liệu quan trọng và được đưa vào Git theo yêu cầu của tác giả. Việc theo dõi tệp bằng Git không tự nâng mọi câu trong tệp lên một trạng thái canon mới; định nghĩa HIP tiếp tục được đối chiếu với các nguồn có nhãn trong project.

Các ảnh PNG trong `13_VISUAL_ASSETS/Greed/` và `13_VISUAL_ASSETS/unassigned/` là **tài liệu tham khảo hình ảnh**. Chữ, tên riêng và thông số xuất hiện trên ảnh không tự trở thành source of truth cho engine, cá thể hoặc vũ khí.

## 5. Mode vận hành hiện hành

| Engine | Mode vận hành hiện hành | Trạng thái |
| --- | --- | --- |
| Sloth | V2 | `USER_CONFIRMED` |
| Wrath | V2 | `USER_CONFIRMED` |
| Chaos | V2 | `USER_CONFIRMED` |

Đây là phân loại mode vận hành hiện hành. Nó không biến ba engine thành cùng một kiến trúc nội bộ, không quyết định outcome của HIP/actor và không tuyên bố V1.5 bị V2 thay thế. Nguồn về điều kiện vận hành cụ thể theo từng host hoặc cấu hình vẫn phải được đọc riêng.

## 6. CI HIP Compact

[The_Academy_CI_HIP_Core_English_Compact_Revised.md](source_archive/controls/The_Academy_CI_HIP_Core_English_Compact_Revised.md) là **bản chính thức tại thời điểm xác nhận này**. [The_Academy_CI_HIP_Core_English_Compact.md](source_archive/controls/The_Academy_CI_HIP_Core_English_Compact.md) là **bản cũ**. Hai bản được giữ để đối chiếu nguồn. Thẩm quyền hiện hành xem mục 8; xác nhận tài liệu không phải bằng chứng về trạng thái runtime bên ngoài repository.

## 7. Những vùng cố ý để mở

Các mục còn `UNKNOWN`/`OPEN` nêu trong [trạng thái sau migration](README.md#trạng-thái-sau-migration) được tác giả cố ý để mở vì tính chất của Narrative Engine. Chúng không phải chỗ trống cần tự động lấp, không tự trở thành cam kết rằng một cơ chế, actor hoặc host phải có cùng kết quả ở mọi triển khai. Khi một nguồn riêng dùng nhãn Working/Placeholder, tiếp tục giữ đúng nhãn và giới hạn của nguồn đó.

## 8. CI hiện hành và Source Router

Theo phê duyệt trực tiếp của tác giả, [The_Academy_CI_v2.0.md](00_META/controls/The_Academy_CI_v2.0.md) là **CI hiện hành trong repository**, thay cho Compact Revised ở vai trò CI. [The_Academy_Source_Router_v1.0.md](00_META/controls/The_Academy_Source_Router_v1.0.md) đảm nhận việc chọn nguồn; nó được biên soạn từ Compact Revised nhưng không tự thành nguồn canon. Bản Compact Revised nguyên gốc được lưu tại `source_archive/controls/`. Việc nạp CI và router vào ChatGPT Project hoặc hành vi mô hình khi chạy thật vẫn `UNVERIFIED`.
