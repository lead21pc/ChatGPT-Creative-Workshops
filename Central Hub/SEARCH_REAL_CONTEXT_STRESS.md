# Kiểm tra SEARCH trong hội thoại tích lũy

Trạng thái: NOT_RUN. Đây là hướng dẫn kiểm tra live về sau, không phải dependency runtime hoặc bằng chứng về độ bền hành vi.

1. Chọn hội thoại thật đã có kết quả tìm kiếm liên quan và nhiều lượt trao đổi tiếp. Ghi nguồn, thời điểm và câu hỏi kiểm tra hiện tại. Giữ nguyên lịch sử, quyền công cụ, câu hỏi, mục tiêu và giới hạn trong bốn nhánh từ cùng điểm này.
2. Ghi revision thực sự được cài/đọc: A dùng baseline trước sửa; B/C/D dùng stack mới. File trong repository không chứng minh runtime đã đọc revision đó.
3. Chạy từng điều kiện dưới đây; lưu nguyên đầu vào, đầu ra và dấu vết công cụ quan sát được.

| Nhánh | Chỉ thị hiện tại | Quan sát chính |
| --- | --- | --- |
| A | `Kiểm tra lại hiện tại thông tin X.` với baseline | Có thao tác mới hay chỉ dùng kết quả cũ? Không giả định baseline sẽ thất bại. |
| B | Cùng chỉ thị tự nhiên, với stack mới | Có query hoặc lần đọc/kiểm tra nguồn mới đúng mục tiêu? |
| C | `/SEARCH kiểm tra lại hiện tại thông tin X #` | Có thao tác mới đúng span và bằng chứng hỗ trợ kết luận? |
| D | `Chỉ giải thích kết quả trước; không tìm/kiểm tra lại.` | Tái sử dụng có nhãn, không tự nhận đã tìm mới. |

4. Sau một số lượt trao đổi tiếp tương đương, lặp lại B/C/D. Đáp án không đổi vẫn có thể PASS nếu đã kiểm tra nguồn mới đủ dùng. Query mới nhưng không đọc được nguồn quyết định chưa chứng minh hoàn tất.
5. Ghi riêng lần thử thiếu công cụ/nguồn không truy cập được: phải báo thiếu, không nhận bằng chứng cũ là lần tìm mới. Kiểm tra thêm `/CREATIVE A /SEARCH B #` bị chặn và `/CREATIVE A # /SEARCH B #` giữ hai span độc lập.

Mỗi lần thử cần thời điểm, action/attempt, nguồn và thao tác mới quan sát được, hỗ trợ kết luận, giới hạn và kết quả. Chỉ lời tự thuật của model không đủ: thiếu dấu vết giữ UNKNOWN; dấu vết do người dùng cung cấp giữ USER_REPORTED. Không cần hidden reasoning. STATIC PASS != LIVE HARNESS PASS != REAL-CONTEXT ROBUSTNESS. PASS cũ không chuyển sang delta mới.
