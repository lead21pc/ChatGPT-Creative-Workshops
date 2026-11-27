# Yêu cầu tạo hoặc cập nhật handoff CURRENT cho Revamp

Dùng trạng thái công việc đã phục hồi theo quy trình trong skill để trình bày đúng một bản full CURRENT hoàn chỉnh dạng Markdown, sẵn sàng lưu dưới tên `<WORKSTREAM>_CURRENT.md` tại đích bên ngoài gói skill đã được xác định và cho phép. Nếu yêu cầu chỉ là dựng nội dung, trả toàn văn, không trả outline, chỉ dẫn, patch hay tóm tắt hội thoại. Yêu cầu tạo file thật, trả delta hoặc ghi vào một đích cụ thể áp dụng quy tắc giao đầu ra trong skill và quyền của yêu cầu hiện tại. Việc nhận mẫu này không tự cấp quyền tạo hoặc ghi file, thay cấu hình kích hoạt, stage, commit, push hay deploy.

Xác định workstream thực tế cần nối tiếp: một luồng công việc có phạm vi rõ, không phải một chat. Nếu cuộc trò chuyện bao gồm nhiều luồng độc lập và không xác định được luồng chính từ yêu cầu hiện tại, hỏi một câu tập trung để chọn một luồng trước khi xuất file; không gộp thành trạng thái toàn project. Dùng tên file viết hoa, dấu gạch dưới, hậu tố `_CURRENT.md`, cùng HANDOFF_ID ổn định, dễ đọc. Nếu có file CURRENT trước đó do người dùng cung cấp, giữ tên file và ID khi workstream vẫn như cũ.

Trình bày trạng thái công việc đã phục hồi có ý nghĩa để tiếp tục: trạng thái đã thiết lập, vấn đề đang mở, việc còn thiếu/bị chặn, phương án đang cân nhắc, quyết định chưa hoàn thành, trạng thái triển khai/kiểm chứng, kết quả đã đóng, xung đột và unknown. Không kể diễn tiến theo thời gian, không ghi “user said”, “assistant said” hoặc “then we discussed”, trừ khi tác giả/thẩm quyền của một quyết định thực sự quan trọng. HANDOFF != CHAT SUMMARY; WORKSTREAM != CHAT.

Giữ nguyên mức chứng cứ và trạng thái, dùng nhãn khi cần:

- USER-PROVIDED STATE: trạng thái do người dùng cung cấp; không biến thành quan sát trực tiếp.
- OBSERVED: điều đã trực tiếp quan sát, kèm nguồn và phạm vi.
- DECIDED: chỉ khi người dùng thực sự chấp thuận quyết định; không suy từ đề xuất của assistant, im lặng hay tiếp tục trao đổi.
- IMPLEMENTED: đã sửa thực tế; không dùng cho kế hoạch chưa thực hiện.
- STATICALLY VERIFIED và LIVE VERIFIED: phân biệt kiểm tra file/cấu trúc với kiểm chứng hành vi chạy thật; ghi kiểm tra nào đã chạy, kết quả và giới hạn.
- UNDER CONSIDERATION, BLOCKED, UNKNOWN, RESOLVED, STALE / CONFLICTED: giữ đúng trạng thái, không tự nâng cấp.

DECIDED != IMPLEMENTED; IMPLEMENTED != VERIFIED; STATIC VERIFIED != LIVE VERIFIED; PROPOSAL != ACCEPTED; RESOLVED != IMMUTABLE. Kiểm tra chưa chạy phải ghi NOT RUN. Không dựng lại dữ kiện, quyết định, nguồn, ngày tháng hoặc kết quả không có trong hội thoại/nguồn đã đọc. Nếu ngày hiện tại không biết, ghi UNKNOWN.

Khi kết xuất full CURRENT từ CURRENT có sẵn, đọc đầy đủ bản cũ, coi đó là trạng thái trước và trình bày bản thay thế hoàn chỉnh với các thay đổi đáng kể có chứng cứ. Khi người dùng chỉ cần delta, áp dụng cách giao delta trong skill. Giữ thông tin còn hợp lệ; không âm thầm giữ hoặc hòa giải thông tin mâu thuẫn. Nêu phần STALE / CONFLICTED, nguồn mâu thuẫn và phần cần xác minh; file/runtime vừa kiểm tra quyết định trạng thái triển khai quan sát được. Không đánh dấu xung đột đã giải quyết nếu chưa có chứng cứ.

Handoff chỉ nối tiếp công việc, ghi quyết định/trạng thái và dẫn tới nguồn. Nó không thay thế kiểm tra file/runtime hiện tại, không là chứng cứ sự thật bên ngoài và không cấp quyền triển khai, commit, push hay deploy. RECORDED DECISION != NEW AUTHORIZATION; LOCAL CHANGE != COMMIT != PUSH. Yêu cầu hiện tại kiểm soát nhiệm vụ/quyền hạn; file/runtime kiểm soát trạng thái thực tế; handoff ghi trạng thái công việc trước đó.

CURRENT là continuity giới hạn theo workstream, không phải snapshot toàn repository. Ghi shared-stack version cùng mốc/phạm vi đã biết; pin đó không tự là version hiện hành vĩnh viễn. Lần vào sau theo quy trình chọn nguồn của skill: kiểm đích hiện hành trước, rồi chỉ đọc tài liệu lịch sử và trạng thái tiếp nối khi có nhu cầu tương ứng. Chỉ nạp CURRENT sau khi đã kiểm nguồn hiện hành và History theo điều kiện, nếu còn nhu cầu tiếp nối mà nguồn hiện hành chưa đáp ứng. Không cần đọc History trước để được đọc CURRENT. Pin shared version cũ chỉ làm stale claim bị ảnh hưởng, không xóa rationale, quyết định hay attribution còn hợp lệ; không cập nhật mọi handoff chỉ vì subsystem khác nâng shared stack.

Giữ vấn đề đã giải quyết thật ngắn: vấn đề, cách giải quyết, chứng cứ, điều kiện mở lại. Chỉ mở lại khi chứng cứ mới mâu thuẫn, triển khai hiện tại lệch hoặc người dùng yêu cầu xét lại. Không biến mục đã đóng thành kho lịch sử; dùng lịch sử phiên bản hiện có khi khả dụng, không giả định host có Git. Chỉ cập nhật khi trạng thái công việc thay đổi đáng kể, không sau mỗi tin nhắn.

Ghi các đường dẫn/section/ID nguồn đã được thiết lập; phân biệt nguồn đã đọc với nguồn chỉ được nhắc tới. Không bịa anchor hoặc tự đọc chat khác. Hướng dẫn lần vào tiếp theo phải đủ để xác định việc cần làm, nguồn cần kiểm tra và giới hạn quyền; không ngầm cho phép bắt đầu implementation. Ghi vị trí nguồn tiếp nối đã được thiết lập khi có ảnh hưởng. Việc tạo file không tự kích hoạt nó và không cấp quyền sửa cấu hình khám phá; nếu chưa xác định được vị trí hoặc thẩm quyền nguồn, ghi rõ khoảng trống. Mẫu này chỉ định dạng trạng thái, không sở hữu quy trình tìm nguồn, vòng đời, quyền ghi hoặc kích hoạt. HANDOFF PRESENCE != ACTIVATION; MENTION != MATCH.

Giữ các giới hạn của hệ thống đích và các luồng công việc độc lập. Theo dõi công việc về một hệ thống không tự cài skill, quy tắc tiếp nối hoặc hành vi nạp nguồn vào hệ thống đó. Không mang CURRENT từ repository trước hoặc từ thư mục skill đã cài sang đích khác. Ghi các ranh giới thực sự có liên quan trong phần loại trừ.

Giữ cấu trúc 10 mục dưới đây. Trong mục phù hợp, có thể gom chi tiết đã phục hồi về cùng chủ đề thành một khối, đặt trạng thái cạnh từng mệnh đề và dùng dẫn chiếu ngắn nếu cần nối qua mục khác. Đặt trạng thái cần để tiếp tục trong thân tài liệu. Điền nội dung thực tế; mục không có dữ kiện ghi “None currently established.”. Không để placeholder và không bịa dữ kiện để lấp mục.

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

Khi giúp kiểm tra phần state được chuyển giao và phần cố ý lược bỏ, có thể thêm một mục không đánh số `## Handoff Receipt` sau 10 mục trên; không bắt buộc cho mọi CURRENT và không làm mất tính hợp lệ của CURRENT cũ. Ghi thật ngắn state đã chuyển, distinction quan trọng được giữ, context cố ý không chuyển và gap material nếu có; không ép tên field hoặc cấu trúc con cố định. Body vẫn chứa state cần để tiếp tục; receipt không thay body, không lặp toàn bộ body và không chứng minh state đúng hoặc đầy đủ, cũng không cấp quyền. Quy trình phục hồi, phân loại, nén và giao đầu ra nằm trong skill; mẫu chỉ cung cấp vị trí receipt trong CURRENT, không đổi điều kiện ghi/nạp hoặc quyền hạn.
