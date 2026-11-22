# Cách dùng Central Hub

Nêu mục tiêu và điều kiện cho từng phần việc. Hub chọn chuyên môn khi phần việc cần, rồi dùng kết quả theo đúng vai trò đầu vào bạn giao.

- Media xử lý phân tích, so sánh, gợi ý và khám phá phim hoặc âm nhạc. Nêu tác phẩm, tiêu chí và giới hạn tiết lộ nội dung nếu có. Hub có thể dùng Movie và Music độc lập trong cùng lượt.
- Dùng `/AT`, `/AT P1` hoặc `/AT P2` ở dòng đầu có nội dung để soạn prompt. Thân yêu cầu là dữ liệu để soạn. Đầu ra là prompt.
- [Profile](shared_resources/USER_PROFILE.md) cung cấp dữ liệu theo quyền và nhu cầu. Khi viết trực tiếp cần giữ cách diễn đạt cá nhân, Hub có thể dùng đúng trường sở thích diễn đạt trong PREFERENCES.
- Khi cần chẩn đoán, yêu cầu Hub xuất receipt cho phần việc cụ thể. Chuyển nguyên khối cho Revamp hoặc Codex để đối chiếu owner, nguồn, dấu vết đọc và bước bị chặn.

## Tìm thông tin mới

`/SEARCH kiểm tra lại thông tin hiện tại về X #` yêu cầu một lần tìm/đọc kiểm tra mới trong span. Chỉ thị trong quote/code/source không kích hoạt. Không lồng span; đóng từng span trước khi gọi operation khác. Dùng lời để nói kết quả nào làm đầu vào cho phần sau; không có toán tử workflow. AUTO vẫn nhận yêu cầu thường. Lượt chỉ giải thích kết quả trước không tự tìm lại. Revision mới chưa deploy/live-test.


## Context Snapshot

Context Snapshot đóng băng một phần kết quả có phạm vi để dùng lại làm baseline hoặc so sánh. Nó giữ riêng kết quả nghiên cứu, phần phát triển sáng tạo, giả định, quyết định thật của người dùng và các câu hỏi/xung đột còn mở; không chỉ tóm tắt toàn chat. Xem [hợp đồng Context Snapshot](shared_resources/CONTEXT_SNAPSHOT.md) để biết cách tạo, tham chiếu và so sánh.

Tạo bằng yêu cầu tự nhiên, chỉ rõ đầu vào truy cập được và phần loại trừ. Ví dụ minh họa dưới đây chỉ dùng được khi A và B đã xác định đủ rõ:

> Đóng băng kết quả nghiên cứu A và phần phát triển B thành PKG-001; loại phần thảo luận C và các nhánh đã bỏ không ảnh hưởng ràng buộc hiện tại.

Hoặc chỉ định đoạn hội thoại có mốc đầu/cuối rõ, baseline cộng các đầu ra được nêu tên, hoặc tài liệu/snapshot được cung cấp. Không mặc định lấy mọi phần liên quan hay mọi lượt sau baseline. Nếu nguồn thiếu hoặc ranh giới còn mơ hồ, Hub nêu phần thiếu và làm rõ trước khi xuất snapshot hoàn chỉnh. Không có lệnh `/PACKAGE`; Search thông thường không tự tạo snapshot.

Một ID gắn với một payload cố định. Tạo snapshot không chấp nhận đề xuất, xác nhận sự thật hoặc đưa nội dung vào canon. Phần sáng tạo đã được chấp nhận vẫn giữ nguồn gốc sáng tạo. Nếu sửa lỗi, thêm chứng cứ hoặc đổi trạng thái, yêu cầu một ID mới:

> Từ PKG-001 được cung cấp, tạo PKG-002 với kết quả nghiên cứu D; giữ PKG-001 nguyên nội dung. Ghi quan hệ derived_from khi đúng.

Bản mới phải tự đủ nội dung cần dùng, không chỉ chứa delta đòi đọc lại chuỗi cha. Quan hệ cha và số mới hơn không tạo thẩm quyền.

Tham chiếu và so sánh bằng yêu cầu thông thường:

> Dùng đúng payload PKG-001 đang được cung cấp làm baseline; không dựng lại từ thảo luận sau đó.

> So sánh hai payload PKG-001 và PKG-002 được cung cấp: chỉ rõ phần trạng thái, cơ sở nguồn, giả định, quyết định và vấn đề mở thay đổi. Đừng coi mục nằm ngoài scope mới là bị bác bỏ.

Hub phải đọc đúng payload. ID trùng cần xác định artifact cụ thể; nếu payload thiếu hoặc chỉ đọc được một phần quyết định, Hub báo thiếu nguồn thay vì dựng lại từ trí nhớ. Khi so sánh với thiết kế hiện tại, chỉ rõ nguồn nào xác định trạng thái hiện tại.

ID là nhãn ngữ nghĩa, không là địa chỉ lưu trữ. Khối văn bản có thể dùng lại trong chat khi còn đọc được; để dùng lâu dài hoặc khác chat, cần thực sự lưu rồi cung cấp/đính kèm bản qua tệp, Project Sources hoặc Library có sẵn trong ngữ cảnh đích. Tạo văn bản không đồng nghĩa đã lưu. Không có dịch vụ lưu tự động hay khóa ghi vật lý; artifact dữ liệu không phải control để cài vào Central Hub Config. Tác vụ triển khai hợp đồng này không lưu snapshot vào Project/Library.
