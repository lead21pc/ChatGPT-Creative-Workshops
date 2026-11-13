---
name: c2-canon-integration
description: Kiểm định và nhập delta lore của Project Cosmic Core (C2) vào nguồn hiện hành trong repository local. Đối chiếu mệnh đề, phân định nguồn có thẩm quyền, giữ xung đột và phần chưa chốt, rồi kiểm chứng phần nhập được tác giả cho phép. Dành cho công việc nguồn phía Codex.
---

# Kiểm định và nhập canon C2

ChatGPT Project phát triển và suy luận về lore theo C2 CI, Router, Anti-Drift và các nguồn được nạp. Skill này bắt đầu khi kết quả phiên hoặc tài liệu lore mới được đưa cho Codex để đối chiếu với nguồn C2 được duy trì cục bộ. CI giữ quy tắc hành vi và quyền canon, Router giữ cổng và định tuyến nguồn lúc chạy, Anti-Drift giữ quy tắc diễn giải. Skill chỉ điều phối kiểm định delta, chọn nơi ghi, cập nhật được phép và kiểm chứng baseline local.

Kích hoạt khi được yêu cầu audit, so sánh, phân loại, hòa giải hoặc nhập một delta, đầu ra phiên hay tệp lore mới của C2. Tác vụ thuần Git, kiến trúc chung, tra cứu lore thông thường và thảo luận chỉ trong Project nằm ngoài phạm vi. Brainstorm cần đối chiếu canon có thể dùng nguồn hiện hành cho phần đối chiếu. Giữ kết quả ở mức đề xuất cho tới khi tác giả chấp nhận và cho phép nhập.

## DELTA_AUDIT

Chế độ chỉ đọc. Dùng khi được yêu cầu kiểm định, so sánh, phân loại hoặc đề xuất nhập.

1. Xác định và đọc toàn bộ delta. Xác minh vai trò của nó từ nội dung và yêu cầu, kể cả khi tên tệp có chữ canon hoặc nằm trong thư mục nhận đầu vào. Prototype, lịch sử và ghi chú thiết kế giữ vai trò tương ứng. Delta là vật chứa mệnh đề để xét, chưa có quyền tự thay nguồn hiện hành. Tách thành mệnh đề hoặc nhóm cùng một quyết định. Giữ phần tác giả đã chốt tách khỏi suy luận, khả năng và đề xuất.
2. Kiểm chính delta trước khi so canon. Khi có liên quan, rà mâu thuẫn nội tại, đổi nghĩa thuật ngữ hoặc phạm vi, niên đại, nhân quả, tri thức, thẩm quyền và điều kiện chuyển trạng thái. Kiểm theo tiền đề hư cấu được cung cấp. Chỉ ra chỗ đề xuất bị trình bày như sự kiện hoặc kết luận vượt quá tiền đề.
3. Dùng working tree C2 hiện tại. Đọc README và hợp đồng nguồn trong chỉ mục hiện hành. Với kết luận phụ thuộc canon C2, đọc đầy đủ chỉ mục và sổ vấn đề mở từ cùng trạng thái gói. Dùng danh mục khi cần tìm nguồn, xác nhận ánh xạ và đọc đầy đủ các nguồn quyết định theo header và phạm vi thẩm quyền. Mở hồ sơ hòa giải khi xung đột, xuất xứ, thay thế, quyền ưu tiên hoặc chuyển thẩm quyền có thể đổi kết quả. Lịch sử và archive phục vụ truy nguyên hoặc đối chiếu được yêu cầu. Thiếu căn cứ quyết định thì nêu phần bị chặn.
4. So từng nhóm với baseline theo đối tượng, nghĩa, phạm vi, thời điểm, điều kiện và lớp canon. Phân loại theo quy ước hiện hành bên dưới, xác định nơi ghi thích hợp và nêu quyết định còn thiếu. Báo gọn mệnh đề, bằng chứng hiện hành, trạng thái, nguồn đích và cách xử lý đề xuất. Gộp các mệnh đề có cùng quyết định và chỉ đặt ID khi giúp đối chiếu. Dừng ở đề xuất.

### Phân loại và chọn nguồn

- `CURRENT` áp dụng cho mệnh đề đã có hiệu lực trong baseline hoặc đã được tác giả chấp nhận vào baseline đúng phạm vi. Mệnh đề mới tương thích vẫn cần được chấp nhận.
- `CONFLICTED` áp dụng khi các mệnh đề thực sự bất tương thích trong cùng nghĩa, phạm vi, thời điểm và lớp canon, và còn cần phân xử. Thiếu thông tin là `UNKNOWN` khi chưa đủ căn cứ kết luận.
- `DEFERRED` cần quyết định hoãn rõ ràng. Giữ `OPEN` và `UNKNOWN` theo hồ sơ hiện hành khi chưa có quyết định đó.
- Giữ riêng loại vấn đề, trạng thái chấp nhận hoặc xử lý và xuất xứ. Dùng quy ước đang có trong hòa giải, sổ vấn đề mở và provenance. `PROPOSAL` giữ vai trò đề xuất, `RESOLVED` cần căn cứ giải quyết, `SUPERSEDED` cần xác định phần đã bị thay thế có thẩm quyền. Xuất xứ hoặc mức chắc chắn tự nó không cấp quyền canon.

Xác định thực thể và trạng thái trực tiếp được mô tả. Ưu tiên nguồn hiện hành có phạm vi bao quát mệnh đề đó. Chỉ theo dẫn chiếu khi nguồn kia có thể đổi kết luận hoặc nơi ghi. Chỉ đề xuất nguồn mới khi căn tính, trạng thái, vòng đời, ranh giới thẩm quyền hoặc định nghĩa dùng qua nhiều miền thực sự cần được duy trì riêng.

- Độ phức tạp, tần suất xuất hiện, tên riêng, mục tra cứu, heading và số tệp trống đều chưa đủ để tách nguồn. Một thực thể có thể thuộc phạm vi của nguồn hiện có.
- Danh mục chỉ dẫn đường. Dẫn chiếu không chuyển thẩm quyền và không tự tạo phụ thuộc. Ghi định nghĩa và quan hệ người giữ hoặc sử dụng theo nguồn thực sự quản từng mệnh đề.

## INTEGRATE

Chỉ ghi khi tác giả đã cho phép nhập phần được chấp nhận. Quyền audit và quyền nhập một phần không mở rộng sang phần còn lại, module mới, thay đổi kiến trúc hoặc control. Quyền tạo nhánh, tag, push và triển khai được xác định riêng.

1. Đọc lại toàn bộ delta và các nguồn hiện hành chịu tác động. Làm lại phần kiểm định cần thiết trên nội dung thực tế. Xác nhận lại phần được chấp nhận và phần còn mở, nhất là khi nguồn hoặc phạm vi đã đổi. Giữ phần còn mơ hồ ở trạng thái hiện có và chỉ tiếp tục phần độc lập đã rõ quyền.
2. Ghi mệnh đề đã được chấp nhận vào đúng nguồn, giữ nội dung ngoài phạm vi. Cập nhật danh mục khi đường tra cứu đổi, hòa giải khi có quyết định, thay thế hoặc chuyển thẩm quyền cần lưu, và sổ vấn đề mở khi trạng thái thực sự đổi. Chỉ thêm module khi việc duy trì riêng có căn cứ và tác giả đã chấp thuận. Giữ bản delta theo vai trò nguồn gốc của nó. Việc di chuyển hoặc lưu trữ bản gốc theo quyền và quy trình hiện hành của tác vụ.
3. Dùng README, manifest, builder và tests hiện hành cho phần bảo trì. Khi đổi admission, kiểm ánh xạ tường minh và điều kiện bảng module/tập dòng hash mà builder yêu cầu trước khi sinh lại metadata. Từ thư mục C2, dùng `python -B build_consolidation.py --write` khi cần đồng bộ vùng sinh tự động, rồi `python -B build_consolidation.py --check`. Dùng `python -B build_consolidation.py --check-router` khi hợp đồng định tuyến/control bị tác động hoặc workflow hiện hành yêu cầu. Chạy kiểm thử liên quan khi đổi admission hoặc hợp đồng được kiểm, dùng `python -B -m unittest discover -s tests -v` khi cần kiểm cả bộ.
4. Đọc lại nguồn đã ghi và vùng sinh tự động liên quan. So với quyết định, baseline trước sửa và các điểm còn mở. Kiểm nội dung thiếu, nội dung vượt quyền, thay đổi ngoài phạm vi và `git diff --check`. Báo riêng kết quả đối chiếu ngữ nghĩa, kết quả kiểm gói và điều còn mở. Chỉ báo baseline local đã cập nhật khi cả phần nội dung lẫn các kiểm tra áp dụng đều đạt. Kết quả cấu trúc không xác nhận nghĩa lore hoặc hành vi trong ChatGPT Project.

## Ví dụ cần đối chiếu lại với nguồn hiện hành

- `Os s5shi` là ví dụ câu chú riêng của Cosmic Mage `25_1`. Nếu ranh giới ấy vẫn đúng, giữ định nghĩa ở nguồn nhân vật và dẫn mục tra cứu về đó.
- Slot `25_3–25_5` thuộc Team 25 trong baseline đã kiểm. Chỉ đề xuất hồ sơ riêng khi có trạng thái nhân vật cần duy trì độc lập.
- Sự thật bền của World 1, điều được cấp trong briefing và sự kiện Campaign 01 thuộc các phạm vi riêng. Một sự kiện có thể dẫn đến nhiều cập nhật đã được chấp nhận, mỗi cập nhật ghi tại nguồn chịu tác động.
- Một sự kiện làm lộ thông tin chưa xác lập rằng Rongo đã tiếp nhận hoặc hiểu. Kiểm đường thông tin, chủ thể biết và mốc trước khi ghi tri thức tổ chức.
