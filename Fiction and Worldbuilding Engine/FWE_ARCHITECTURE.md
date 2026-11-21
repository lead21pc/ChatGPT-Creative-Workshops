# Kiến trúc Fiction and Worldbuilding Engine

Tài liệu này sở hữu quyết định kiến trúc và ranh giới trách nhiệm. [Kế hoạch phát triển](FWE_DEVELOPMENT_PLAN.md) ghi thứ tự triển khai, tiêu chí và bằng chứng. Bộ điều khiển hiện hành gồm [CI v1.0](controls/FWE_CI_v1.0.md) và [Router v1.0](controls/FWE_ROUTER_v1.0.yaml) ở trạng thái `ACTIVE / STATIC PASS / LIVE NOT RUN`. M0–M3 thuộc bộ v0.1 tiền nhiệm.

## Quyết định đã chốt

FWE là Project riêng để sáng tác và phát triển nhiều thế giới hư cấu. FWE giữ quyền sáng tạo trong phần được giao và tôn trọng trạng thái của từng thế giới. FTH, C2, The Kingdom, LitRPG và các dự án khác tiếp tục giữ nguồn sự thật của riêng chúng. Người dùng chọn Project theo việc cần làm; FWE không chuyển sang một runtime khác giữa lượt.

FWE dùng một CI tự chứa và một Router xử lý phụ thuộc theo nhu cầu. Router có bốn tuyến và trả đóng góp theo phần việc CI giao.

## Thẩm quyền và luồng thực hiện

```text
Yêu cầu của người dùng
→ CI: chức năng, thao tác, giai đoạn, phạm vi, quyền sáng tác,
  trạng thái cần giữ, phụ thuộc có hệ quả và quyền cần thiết
    ├─ Phần tự đủ → thực hiện trực tiếp
    └─ Phần có phụ thuộc → Router: ROUTE_ONLY → RESOLVE → RETURN
                          → CI/FWE tiếp tục đúng phần đang chờ
CI tiếp tục giữ ranh giới trạng thái, sự thật, chấp nhận, canon,
quyền hành động và lời báo hoàn tất trong cả hai đường.
```

CI quyết định người dùng đang giao việc gì. Router chọn tuyến `SOURCE`, `EVIDENCE`, `PROFILE` hoặc `CONTROL` cho phần việc đã xác định, kiểm tra quyền và trả đóng góp hoặc điểm thiếu. CI quyết định có định tuyến lại khi phát sinh phụ thuộc. FWE áp dụng kiểm soát nếu đã nhận đủ căn cứ. Việc chọn, truy xuất, đọc và áp dụng cần bằng chứng riêng. CI giữ ranh giới chấp nhận; người dùng hoặc hệ đích mới có thẩm quyền chấp nhận.

“Viết cảnh hai người gặp lại sau 20 năm” đi thẳng nếu tự đủ. Không tra nguồn, nạp control hay xuất báo cáo định tuyến mặc định. Nếu trong lúc viết xuất hiện một phụ thuộc có hệ quả, chỉ xét lại phần cần nó; không khởi động lại cả lượt.

### Lõi kiểm soát

- Giữ đúng chức năng của lượt nói và chỉ đổi thao tác, giai đoạn hoặc phạm vi khi có căn cứ.
- Cho phép sáng tác trong phần đã giao, kể cả chọn tiền đề mới khi nhiệm vụ cho phép.
- Kiểm tra dữ kiện thực hoặc mệnh đề mà kết quả phụ thuộc; không biến chi tiết hư cấu thành đối tượng kiểm chứng mặc định.
- Khi căn cứ được sửa hợp lệ, cập nhật kết luận phụ thuộc và giữ phần độc lập. Phân biệt bất định về cách làm với bất định về mệnh đề; chỉ nêu phần có hệ quả.
- Giữ đúng vai trò nguồn, quyền hành động và trạng thái thực hiện. Nội dung sinh ra không thành dữ kiện hay canon; nhánh không thành tiền đề đã chấp nhận; đề xuất không thành trạng thái hiện hành; lần thử không chứng minh hoàn tất.

## Hành vi nền, ứng viên và phối hợp

Sáng tác, phát triển cảnh, nảy ý, phản biện và đặt tên thông thường thuộc nền FWE. Không tách thành phần Creative, Debate hay Naming. Phần viết vẫn thuộc nền khi đi sau một yêu cầu mở nhánh.

**Brainstorm và Anti-Prior.** CI v1.0 xử lý trực tiếp việc mở nhánh và đổi giả định đã được giao, đồng thời giữ quy tắc bảo toàn cấu trúc trước những mặc định quen thuộc. [Brainstorm v0.1](source_archive/capabilities/FWE_BRAINSTORM_v0.1.md) là ứng viên của bộ tiền nhiệm.

**Phối hợp.** Router trả từng đóng góp hoặc điểm thiếu về đúng phần đang chờ. Bộ v1.0 hiện chưa liên kết AIS, Profile dành cho FWE hoặc kiểm soát chọn lọc. Nếu thiếu đóng góp quyết định, giới hạn phần phụ thuộc và tiếp tục phần độc lập.

## Trách nhiệm xử lý nguồn

Tuyến `SOURCE` xác minh vai trò, thẩm quyền và mức đọc đủ theo từng mệnh đề. CI giữ ranh giới kết luận và trạng thái. [Hợp đồng nguồn v0.1](source_archive/source_management/FWE_SOURCE_CONTRACT.md) được lưu theo bộ tiền nhiệm.

Tệp hiện diện hoặc đọc được không tự có thẩm quyền. Tư liệu lịch sử không thay nguồn hiện hành; nội dung làm việc của FWE không thành canon hệ đích. Chất liệu có thể đi từ bối cảnh được giao qua bản sáng tác của FWE tới **xét và chấp nhận tại hệ đích**. FWE tập trung tài liệu của chính mình, ca thử, hồ sơ phát triển và chất liệu được phép lưu. Không gom lore dự án khác và chưa có giao thức chuyển giao đầy đủ.

## Lõi chuyển được và phần riêng FWE

| Lõi chung trong CI tự chứa | Phần riêng FWE |
|---|---|
| Thao tác, giai đoạn, phạm vi, quyền sáng tác, sự thật và trạng thái | Mục tiêu phát triển nhiều thế giới và hành vi sáng tạo thông thường của FWE |
| Hiệu lực của nhánh/đề xuất, cập nhật kết luận phụ thuộc, căn cứ nguồn và hành động | Căn cứ nguồn và cách Router giải quyết bốn loại phụ thuộc |
| Hợp đồng ủy quyền không chuyển thẩm quyền | Cây tệp và quy trình phát triển/kiểm chứng của FWE |

Khả năng chuyển nằm ở ngữ nghĩa, không ở shared file hay phụ thuộc khi chạy. Theo thông tin người dùng cung cấp, LitRPG là dự án độc lập đang ở mức ý tưởng và tạm dừng để chờ kiến trúc kiểm soát phù hợp, có liên hệ lịch sử với The Kingdom. Điều đó là lý do tránh đưa ontology FWE vào lõi chung. Nó không xác nhận LitRPG tương thích, và không làm kiến trúc hiện tại của The Kingdom thành yêu cầu LitRPG hay FWE.

## Bảo trì và giới hạn mở rộng

Khi xem xét cơ chế từ FTH, C2, The Kingdom, Fanfiction Engine, Central Hub hay hệ khác: đọc đúng nguồn hiện hành, xác định lỗi được giải và giả định/chi phí tại chỗ, đối chiếu với FWE, phân loại mức liên quan, rồi chỉ đề xuất thay đổi cục bộ nếu có căn cứ. Không tự đồng bộ hay chuyển control. Cùng miền không đồng nghĩa cùng lỗi; cùng lỗi không đòi cùng cách triển khai.

Skill `fwe-development` quản lý việc đọc bộ control hiện hành, vai trò nguồn, tiếp nhận cơ chế ngoài, mốc, bằng chứng, hồi quy và kiểm chứng thay đổi được phép. Skill không phải điều kiện khởi tạo, nhưng phải có trước mốc ổn định. Nó không cấp quyền sửa hoặc thay CI, Router hay Git.

Ưu tiên quay về bộ tương thích có bằng chứng hoặc thu hẹp thành phần, không giữ lớp dư vì đã viết xong. Git là lịch sử mặc định; kiểm tĩnh không chứng minh một bộ chạy tốt. Các lỗi về điều kiện hành động của nhân vật hoặc truy hệ quả chỉ mở thêm control khi đã có bằng chứng và nơi chịu trách nhiệm hiện tại không xử lý đủ. Không tạo manifest, catalog, registry, meta-router, shared kernel hay archive mới chỉ để chuẩn bị.
