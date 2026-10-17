# Yêu cầu tạo hoặc cập nhật handoff CURRENT cho Revamp

Hãy dùng trạng thái công việc được chứng minh trong cuộc trò chuyện này để tạo đúng một file `<WORKSTREAM>_CURRENT.md` hoàn chỉnh, sẵn sàng lưu vào `Project CI/Revamp Project System/Handoffs/`. Trả về toàn bộ nội dung Markdown của file, không trả outline, hướng dẫn viết file, patch hoặc bản tóm tắt hội thoại. Không ghi file, sửa Router, stage, commit, push hay deploy chỉ vì nhận mẫu này; việc tạo nội dung không cấp quyền thực hiện những hành động đó.

Xác định workstream thực tế cần nối tiếp: một luồng công việc có phạm vi rõ, không phải một chat. Nếu cuộc trò chuyện bao gồm nhiều luồng độc lập và không xác định được luồng chính từ yêu cầu hiện tại, hỏi một câu tập trung để chọn một luồng trước khi xuất file; không gộp thành trạng thái toàn project. Dùng tên file viết hoa, dấu gạch dưới, hậu tố `_CURRENT.md`, cùng HANDOFF_ID ổn định, dễ đọc. Nếu có file CURRENT trước đó do người dùng cung cấp, giữ tên file và ID khi workstream vẫn như cũ.

Chỉ trích xuất trạng thái công việc có ý nghĩa để tiếp tục: trạng thái đã thiết lập, vấn đề đang mở, việc còn thiếu/bị chặn, phương án đang cân nhắc, quyết định chưa hoàn thành, trạng thái triển khai/kiểm chứng, kết quả đã đóng, xung đột và unknown. Không kể diễn tiến theo thời gian, không ghi “user said”, “assistant said” hoặc “then we discussed”, trừ khi tác giả/thẩm quyền của một quyết định thực sự quan trọng. HANDOFF != CHAT SUMMARY; WORKSTREAM != CHAT.

Giữ nguyên mức chứng cứ và trạng thái, dùng nhãn khi cần:

- USER-PROVIDED STATE: trạng thái do người dùng cung cấp; không biến thành quan sát trực tiếp.
- OBSERVED: điều đã trực tiếp quan sát, kèm nguồn và phạm vi.
- DECIDED: chỉ khi người dùng thực sự chấp thuận quyết định; không suy từ đề xuất của assistant, im lặng hay tiếp tục trao đổi.
- IMPLEMENTED: đã sửa thực tế; không dùng cho kế hoạch chưa thực hiện.
- STATICALLY VERIFIED và LIVE VERIFIED: phân biệt kiểm tra file/cấu trúc với kiểm chứng hành vi chạy thật; ghi kiểm tra nào đã chạy, kết quả và giới hạn.
- UNDER CONSIDERATION, BLOCKED, UNKNOWN, RESOLVED, STALE / CONFLICTED: giữ đúng trạng thái, không tự nâng cấp.

DECIDED != IMPLEMENTED; IMPLEMENTED != VERIFIED; STATIC VERIFIED != LIVE VERIFIED; PROPOSAL != ACCEPTED; RESOLVED != IMMUTABLE. Kiểm tra chưa chạy phải ghi NOT RUN. Không dựng lại dữ kiện, quyết định, nguồn, ngày tháng hoặc kết quả không có trong hội thoại/nguồn đã đọc. Nếu ngày hiện tại không biết, ghi UNKNOWN.

Nếu người dùng cung cấp CURRENT hiện có: đọc đầy đủ, coi đó là trạng thái trước, kết hợp các thay đổi đáng kể có chứng cứ trong chat và trả file thay thế hoàn chỉnh. Giữ thông tin còn hợp lệ; không âm thầm giữ hoặc hòa giải thông tin mâu thuẫn. Nêu phần STALE / CONFLICTED, nguồn mâu thuẫn và phần cần xác minh; file/runtime vừa kiểm tra quyết định trạng thái triển khai quan sát được. Không đánh dấu xung đột đã giải quyết nếu chưa có chứng cứ.

Handoff chỉ nối tiếp công việc, ghi quyết định/trạng thái và dẫn tới nguồn. Nó không thay thế kiểm tra file/runtime hiện tại, không là chứng cứ sự thật bên ngoài và không cấp quyền triển khai, commit, push hay deploy. RECORDED DECISION != NEW AUTHORIZATION; LOCAL CHANGE != COMMIT != PUSH. Yêu cầu hiện tại kiểm soát nhiệm vụ/quyền hạn; file/runtime kiểm soát trạng thái thực tế; handoff ghi trạng thái công việc trước đó.

Giữ vấn đề đã giải quyết thật ngắn: vấn đề, cách giải quyết, chứng cứ, điều kiện mở lại. Chỉ mở lại khi chứng cứ mới mâu thuẫn, triển khai hiện tại lệch hoặc người dùng yêu cầu xét lại. Không biến mục đã đóng thành kho lịch sử; Git giữ lịch sử. Chỉ cập nhật khi trạng thái công việc thay đổi đáng kể, không sau mỗi tin nhắn.

Ghi các đường dẫn/section/ID nguồn đã được thiết lập; phân biệt nguồn đã đọc với nguồn chỉ được nhắc tới. Không bịa anchor hoặc tự đọc chat khác. Hướng dẫn lần vào tiếp theo phải đủ để xác định việc cần làm, nguồn cần kiểm tra và giới hạn quyền; không ngầm cho phép bắt đầu implementation. Với file mới chưa có entry trong Router, ghi rõ cần thêm entry phù hợp khi được phép, để thao tác đặt file vào Handoffs không bị hiểu thành tự kích hoạt. HANDOFF PRESENCE != ACTIVATION; MENTION != MATCH.

Central Hub không nhận Router, quy tắc handoff Revamp, file CURRENT hay hành vi nạp xuyên chat. Revamp có thể ghi công việc liên quan Central Hub, nhưng file đó vẫn nằm trong Revamp. Ghi ranh giới này trong phần loại trừ khi liên quan.

Dùng cấu trúc sau cho file hoàn chỉnh. Điền nội dung thực tế; mục không có dữ kiện ghi “None currently established.”. Không để placeholder và không bịa dữ kiện để lấp mục.

```markdown
# <Workstream> — Current Handoff

HANDOFF_ID: <stable readable id>
FILENAME: <WORKSTREAM>_CURRENT.md
STATUS: ACTIVE
SCOPE: <bounded workstream scope>
UPDATED: <known current date or UNKNOWN>

## 1. Established current state

## 2. Active problems

## 3. Outstanding / blocked

## 4. Under consideration

## 5. Decided but not completed

## 6. Resolved / closed

## 7. Conflicts / stale state

## 8. Relevant source anchors

## 9. Next-entry guidance

## 10. Explicit exclusions
```

Chỉ dùng ID cho mục cụ thể khi giúp nối tiếp công việc. Khi hữu ích, ghi ngắn: ID, STATUS, SCOPE, Problem, Current state, Evidence / source anchors, Next. STATUS: ACTIVE của tài liệu chỉ cho biết đây là handoff hiện hành; không chứng minh CI đã được cài, quyết định đã triển khai hoặc nội dung đã LIVE VERIFIED.
