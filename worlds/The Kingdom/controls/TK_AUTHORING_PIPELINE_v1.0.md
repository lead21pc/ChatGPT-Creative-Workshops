# The Kingdom Authoring Pipeline v1.0

Status: ACTIVE
Version: 1.0
Role: AUTHORING_PROCEDURE

## Phạm vi và quyền

Điều khiển phép chuyển đổi được yêu cầu và điểm dừng, không sở hữu canon, lựa chọn nguồn, truth status hoặc kết quả actor. CI giữ thao tác/giai đoạn và quyền vào Router; Router giữ discovery/owner/nạp/đối chiếu/chọn overlay. Pipeline chỉ khai báo thông tin cần và biến đổi material được phép. Tác vụ The Kingdom không tự thu hẹp thành Hyperborea; giữ đúng quốc gia/miền/thời điểm/phạm vi mà yêu cầu xác lập. Không giữ state ngoài ngữ cảnh task.

## Chọn phép biến đổi

Chỉ kích hoạt khi chức năng yêu cầu có biến đổi, không từ keyword. Tra cứu hoặc audit đơn thuần không tự thành thiết kế. Dùng trực tiếp seed/primitives đã đủ; không bắt đi qua mọi bước để đủ sơ đồ.

| Yêu cầu | Phép làm và điểm dừng |
| --- | --- |
| Triết xuất chat/note/handoff | Tách claim, căn cứ và status; dừng ở current-state extraction, chưa nhập canon |
| Source cũ trộn nhiều lớp | Tách primitives/qualifier/current/history/proposal/unknown; không một old file = một new owner |
| Seed/functional abstraction | Bỏ implementation không thiết yếu, giữ intent và quan hệ quyết định; dừng seed |
| Phân rã primitive | Chỉ tách chức năng/điều kiện/thẩm quyền/nguồn lực/quan hệ/state/transition có giá trị; không lấp slot |
| Author decision | Đề xuất delta đúng scope và các owner chịu tác động; không chấp nhận hệ quả suy diễn kèm theo |
| Checkpoint idea | Đề xuất breakpoint, pre-state, direct delta/resulting boundary, gap; chưa thành checkpoint lịch sử |
| Interval material / event | Đề xuất transition trong interval, affected owner, thông tin khả dụng, hệ quả chưa rõ; không tự dựng hai năm |
| So sánh với current | Đối chiếu relevant owner; báo tương thích/xung đột/phụ thuộc; không tự sửa |
| IRL localization | Baseline @ time → divergence đã biết → actor state @ T; dừng ứng dụng/đề xuất có điều kiện |
| Di chuyển legacy owner | Triết xuất → kiểm coverage/status/link → archive byte-exact; không dùng archive phục hồi lore |
| Quyết định accepted → implementation proposal | Đề xuất thay đổi file/delta/kiểm tra đúng scope; chưa triển khai nếu chỉ yêu cầu proposal |
| Triển khai đã được yêu cầu rõ | Thực hiện scope đã cho, kiểm chứng, báo giới hạn; không suy thêm commit/push/deploy |

EXTRACTION != CANON INTEGRATION; DESIGN != IMPLEMENTATION; SIMULATION != TIMELINE HISTORY. A seed không chỉ là bản tóm tắt: giữ lõi chức năng/nhân quả; không genericize đến mất ý nghĩa. Không reverse-define seed từ implementation ưa thích. Quan hệ cần nhưng chưa có vẫn UNKNOWN.

## Handoff sớm vào Router

Trước phép biến đổi đầu tiên cần current state, nêu information need và vào Router, có thể trước seed hoặc trong comparison. Không cố nạp toàn project; không dùng dữ liệu ngoài làm authority. Input mới có thể là premise, requirement, correction hoặc proposal, không gom chung thành fact. Khi scope/thời điểm/owner mở rộng, route lại phần phụ thuộc trước khi dùng. Pipeline không chọn nguồn thay một premise bị chặn.

Router đã nạp/reconcile xong mới tiếp tục phần có căn cứ và các overlay nó chọn. Thiếu Pipeline chặn đúng transformation; thiếu nguồn/control chặn bước phụ thuộc; phần độc lập vẫn tiếp tục. Conditional design premise không giả làm current fact để vượt cổng bị chặn.

## Kiểm trước khi dừng

Giữ terminology, qualifiers và epistemic status; không viết lore prose thay tài liệu mô phỏng khi không yêu cầu. Comparison không tự xin repair; compatibility không là acceptance; accepted premise không chấp nhận dependency tưởng tượng. Proposal phải nêu vấn đề, giả định, delta và phạm vi nếu được chấp nhận. Không thêm simulation, hệ quả bậc hai, alternative hoặc kế hoạch nhập nếu yêu cầu không cần. Dừng đúng sản phẩm đã yêu cầu.
