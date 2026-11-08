# Kiểm thử Naming trong ngữ cảnh thật

REAL-CONTEXT STRESS: NOT RUN

Đặc tả này không là runtime control hoặc bằng chứng hành vi đã PASS. Dùng context thật của tác giả, giữ cùng context và mục tiêu cho baseline Concept/Anti-Prior và nhánh thêm Naming 1.0. Ghi đúng revision được cài/đọc, đầu vào, đầu ra thực, evidence được dùng, câu hỏi làm rõ và đánh giá tác giả; không điền kết quả từ fixture.

Baseline không có Naming dùng yêu cầu tự nhiên tương đương; nhánh Naming dùng span chính xác. Mỗi nhánh bắt đầu trong chat mới để tránh nhiễm kết quả. Kiểm tra thư viện/nguồn theo hợp đồng hiện hành trước khi chạy. Không suy nghĩa hoặc độ phổ biến chỉ từ đáp án mẫu.

| Ca | Yêu cầu cho nhánh Naming, sau khi cung cấp context thật | Tiêu chí quan sát |
| --- | --- | --- |
| N01 | `/NAME P2 Đề xuất 10 tên nam phương Tây cho setting hiện tại; tránh nhóm tên mặc định sáo mòn của model, giữ đúng vùng/thời kỳ đã giao. #` | Có lựa chọn hữu ích theo đánh giá tác giả; không bịa tần suất hoặc biến phổ biến thành sai. |
| N02 | `/NAME P2 Giữ hệ tên vừa xác định; tránh cliché, không tạo pseudo-language hoặc tên fantasy chỉ để nghe lạ. #` | Candidate vẫn trong hệ được giao; không đổi hệ tên để đạt novelty. Thử thêm hệ hư cấu do tác giả chủ động định nghĩa. |
| N03 | `/NAME Phân tích tên phiên âm Wang Ming khi chưa biết characters; giữ các khả năng mở. #` | Không chốt một written form/meaning duy nhất. Chỉ hỏi nếu cần quyết định material; không fabricate evidence. |
| N04 | `/NAME P3 Phân tích 夜神月; tách written form, reading, semantic units, liên tưởng và quan hệ fiction. #` | Các lớp được giữ riêng; claim factual dựa chứng cứ phù hợp hoặc nêu gap. Không tự suy tính cách. |
| N05 | `/NAME P3 Phân tích 太乙真人, chú ý semantic units và chức năng danh hiệu; không suy fiction role. #` | Không tự mặc định mỗi ký tự là một semantic unit; không nhảy cultural function sang role nhân vật. |
| N06 | `/NAME Tôi cố ý dùng tên đã cung cấp dù source meaning không khớp role nhân vật. Đánh giá cách dùng và giữ nguyên nhân vật. #` | Không sửa role/personality để cứu candidate; giữ quyết định tác giả. Thêm candidate khác vi phạm protected state để kiểm tra loại candidate thay vì sửa state. |
| N07 | `/NAME P2 Dùng evidence Hub đã cung cấp để kiểm tra fit; association thú vị trong báo cáo không là tiêu chí của tôi. #` | Không promote association thành criterion/symbolism/lore. Thử return có qualifier, conflict và UNKNOWN; chỉ relation phụ thuộc bị chặn. AIS return là đầu vào có provenance thật hoặc được đánh dấu mô phỏng, không bịa AIS execution. |
| N08 | `/NAME Đề xuất ba tên mới gồm hai âm tiết cho ba đảo trong hệ hư cấu tôi giao; không cần nghĩa. #` | Có kết quả ngay khi context đủ; không forced approval. Lặp với yêu cầu trình basis trước: phải dừng, nói invocation kết thúc, hướng dẫn span mới. |

Ở N08, lượt sau thử chỉ “đồng ý”: Naming không được chạy lại. Sau đó gọi `/NAME P2 Dùng basis vừa trình nhưng sửa ràng buộc đã nêu; tiếp tục. #`; phải cập nhật basis và không giữ preset từ lần gọi trước nếu bị bỏ ở call mới. Thêm câu hỏi có consequential ambiguity để quan sát một focused clarification.

Lặp một ca semantic bằng plain/P1/P2 để kiểm tra invariants không chỉ tồn tại ở P3. Với P3 yêu cầu cả distinctness bằng lời, không cần preset ghép. Kèm một span Creative/Brainstorm/Debate độc lập để kiểm tra không tự gọi hoặc làm lan scope; span lỗi Naming không chặn span độc lập hợp lệ.

Chỉ ghi PASS/FAIL sau khi quan sát output thật trong đúng scope. So sánh lỗi fit/semantic/state, chất lượng lựa chọn theo tiêu chí tác giả, số lượt hỏi không cần thiết và khả năng sửa basis. Static hoặc fixture pass không xác nhận Naming robust, Library retrieval, provenance recognition hay live routing.
