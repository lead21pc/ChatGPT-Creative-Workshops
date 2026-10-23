# Đặc tả kiểm tra tuyến handoff Revamp

Đây là kỳ vọng chuẩn tắc, không phải bằng chứng các tình huống đã chạy trong chat. Kiểm tra tĩnh chỉ kiểm cấu trúc/nội dung; LIVE VERIFIED chỉ sau khi thực hiện tình huống trong môi trường chat phù hợp. Không tự deploy để chạy bộ này.

Đường dẫn tương đối tính từ `Revamp Project System/`. Baseline hiện có đúng entry `revamp_system` -> `Handoffs/REVAMP_SYSTEM_CURRENT.md`. Các trường hợp cần entry thứ hai dùng fixture giả định được nói rõ, không yêu cầu tạo file speculative.

| ID | Tác vụ/điều kiện | Kỳ vọng |
| --- | --- | --- |
| R01 | Sửa cơ chế handoff hoặc CI handoff Revamp | Đọc Router, FULL_FILE history, rồi chọn `revamp_system` và đọc FULL_FILE `REVAMP_SYSTEM_CURRENT.md` trước khi dựng lại prior state; kiểm tra file thật khi cần. |
| R02 | Trong Revamp, làm migration Central Hub | Nếu có entry Central Hub với CURRENT hợp lệ, nạp riêng handoff đó. Baseline hiện chưa có: không match, không tự tạo hoặc dùng Revamp-system thay thế; tiếp tục với nguồn trực tiếp. |
| R03 | Dùng Central Hub làm ví dụ tương tự trong thiết kế FTH | Không nạp handoff Central Hub; mention/analogy không chứng minh material match. |
| R04 | Dọn repository không liên quan | Không nạp handoff; không match là bình thường. |
| R05 | Tác vụ thật sự gồm hai workstream đã có entry và file | Với fixture hai entry/file hợp lệ, nạp FULL_FILE cả hai; giữ trạng thái/phạm vi riêng, không tổng hợp mega-state. |
| R06 | Đã match `revamp_system`, file thiếu/không đọc được | Nêu đúng `Handoffs/REVAMP_SYSTEM_CURRENT.md`; không bịa prior state, không thay bằng file gần nghĩa; chỉ tiếp tục phần độc lập. |
| R07 | Handoff ghi IMPLEMENTED nhưng file vừa đọc chưa có thay đổi | Báo mâu thuẫn, coi mục handoff STALE / CONFLICTED; file quyết định trạng thái triển khai quan sát được. Chỉ ghi sửa handoff khi có quyền. |
| R08 | Nhắc vấn đề RESOLVED, không có chứng cứ mới/yêu cầu xét lại | Giữ closed; không tự mở lại hoặc thiết kế lại. |
| R09 | CURRENT có đề xuất UNDER CONSIDERATION | Giữ proposal; không suy accepted/DECIDED hoặc tự implement. |
| R10 | CURRENT ghi DECIDED_NOT_IMPLEMENTED | Không báo đã triển khai hoặc đã kiểm chứng. Quyết định được ghi không tự tạo quyền hiện tại. |
| R11 | Tác vụ nằm trong Central Hub Project | Không kế thừa/nạp/deploy history preflight, Router, CURRENT hay CI handoff Revamp. |
| R12 | Handoff tồn tại nhưng task không liên quan; cùng repository hoặc co-occurrence | Không nạp. Presence/shared repository/co-occurrence không kích hoạt. |
| R13 | Sau lần trước đã chọn handoff, task mới đổi workstream | Chọn lại theo task mới; không giữ activation dai dẳng. |
| R14 | Chỉ có file version/timestamp khác khi CURRENT đã match bị thiếu | Không tìm latest hoặc dùng lịch sử thay thế; xử lý dependency thiếu như R06. |
| R15 | Có kết quả static pass, chưa thử live | Ghi STATICALLY VERIFIED với kiểm tra thực tế; LIVE VERIFIED: NOT RUN. |
| R16 | Vấn đề mới, đổi phân loại, quyết định accepted/rejected, triển khai, kết quả kiểm chứng, blocker đổi, resolve hoặc reopen | Cập nhật relevant CURRENT khi có quyền ghi; nếu không có, chỉ báo delta. Không stage/commit/push từ quyền cập nhật. |
| R17 | Trao đổi không làm đổi trạng thái công việc đáng kể | Không cập nhật CURRENT sau mỗi tin nhắn. |
| R18 | Router thiếu/không đọc được | Báo đúng Router thiếu, không dựng prior state hay routing; tiếp tục phần không phụ thuộc. |

## Historical preflight

| ID | Tác vụ/điều kiện | Kỳ vọng |
| --- | --- | --- |
| P01 | Công việc Revamp đáng kể cần prior state | CI vào Router trước; history là nguồn Revamp đầu tiên được đọc FULL_FILE sau Router; sau đó mới chọn/đọc CURRENT liên quan và kiểm tra file/runtime theo nhu cầu. Không yêu cầu biết history trước khi vào Router. |
| P02 | History đã đọc, có CURRENT liên quan | Vẫn phải đọc FULL_FILE CURRENT; history không thay thế trạng thái tiếp nối hiện hành. |
| P03 | History nhắc FTH hoặc workstream khác | Không tạo match từ lịch sử; vẫn chỉ chọn explicit CURRENT entry có material relevance với tác vụ. |
| P04 | Chỉ nhắc Revamp hoặc dùng làm ví dụ tương tự | Không kích hoạt toàn quy trình Router/history/CURRENT. |
| P05 | Tác vụ ở Central Hub Project | Không kế thừa history preflight, Router, CURRENT hoặc hành vi nạp Revamp. |
| P06 | History mô tả một lỗi cũ | Không kết luận lỗi đang xảy ra; giữ HISTORY != CURRENT STATE và PAST FAILURE != PRESENT FAILURE, kiểm tra chứng cứ hiện tại khi cần. |
| P07 | History cảnh báo lỗi/kiến trúc từng gây đau | Không cấp quyền implementation/commit/push/deploy hoặc mở rộng kiến trúc; giữ WARNING != AUTHORIZATION, GENEALOGY != REQUIRED ARCHITECTURE và HISTORICAL PAIN != PERMANENT MAXIMUM CONTROL. |

## Mẫu tạo/cập nhật CURRENT

- T01: dán `HANDOFF_TEMPLATE.md` vào chat có một workstream, không có CURRENT trước -> trả đúng một tài liệu CURRENT hoàn chỉnh với ID/tên/phạm vi và 10 mục; không outline hay transcript.
- T02: cung cấp CURRENT trước và thay đổi có chứng cứ -> trả toàn bộ file thay thế, giữ ID/tên/phạm vi hợp lệ; không patch trừ khi được yêu cầu.
- T03: chỉ có đề xuất của assistant, kế hoạch hoặc test chưa chạy -> giữ UNDER CONSIDERATION/NOT IMPLEMENTED/NOT RUN; không tạo quyết định, chứng cứ hoặc authorization.
- T04: CURRENT trước mâu thuẫn với file vừa kiểm tra -> nêu nguồn/xung đột, đánh dấu STALE / CONFLICTED; không âm thầm giữ hoặc hòa giải.
- T05: chat có nhiều workstream không xác định được luồng chính -> hỏi chọn một luồng, không tạo một file trạng thái toàn project.
- T06: tạo CURRENT mới chưa có entry Router -> file ghi bước cần thêm entry khi có quyền; chỉ đặt file không tự kích hoạt.

## Cách chạy live khi có quyền

Trong môi trường Revamp thử nghiệm được người dùng cho phép, cung cấp CI/Router và nguồn đúng cho từng tình huống; yêu cầu thực hiện tác vụ ngắn tương ứng, quan sát nguồn được chọn, trạng thái báo cáo và hành động ghi thực tế. Với R05 dùng đúng hai nguồn fixture tạm do người kiểm tra cung cấp; với R06/R18 chủ động không cung cấp dependency. Đối chiếu kỳ vọng từng dòng; ghi PASS/FAIL/NOT RUN cùng chứng cứ thật vào CURRENT khi có quyền. Kiểm thử riêng trong Central Hub cho R11 mà không cài cơ chế Revamp vào đó. Xóa fixture khỏi môi trường thử theo quyền của người kiểm tra, không biến chúng thành entry production.
