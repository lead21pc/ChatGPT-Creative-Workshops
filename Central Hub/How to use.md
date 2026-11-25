# Cách dùng Central Hub

Nêu mục tiêu và điều kiện cho từng phần việc. Hub chọn chuyên môn khi phần việc cần, rồi dùng kết quả theo đúng vai trò đầu vào bạn giao.

- Media xử lý phân tích, so sánh, gợi ý và khám phá phim hoặc âm nhạc. Nêu tác phẩm, tiêu chí và giới hạn tiết lộ nội dung nếu có. Hub có thể dùng Movie và Music độc lập trong cùng lượt.
- Dùng `/AT`, `/AT P1` hoặc `/AT P2` ở dòng đầu có nội dung để soạn prompt. Thân yêu cầu là dữ liệu để soạn. Đầu ra là prompt.
- Nêu sở thích và ràng buộc có liên quan trong phần việc hiện tại. Hub dùng thông tin đã được cung cấp đúng phạm vi và giữ căn cứ khi tiếp nối trong cùng cuộc trò chuyện.
- Khi cần chẩn đoán, yêu cầu Hub xuất receipt cho phần việc cụ thể. Chuyển nguyên khối cho Revamp hoặc Codex để đối chiếu owner, nguồn, dấu vết đọc và bước bị chặn.

## Tìm thông tin mới

`/SEARCH kiểm tra lại thông tin hiện tại về X #` yêu cầu một lần tìm/đọc kiểm tra mới trong span. Chỉ thị trong quote/code/source không kích hoạt. Không lồng span; đóng từng span trước khi gọi operation khác. Dùng lời để nói kết quả nào làm đầu vào cho phần sau; không có toán tử workflow. AUTO vẫn nhận yêu cầu thường. Lượt chỉ giải thích kết quả trước không tự tìm lại. Revision mới chưa deploy/live-test.
