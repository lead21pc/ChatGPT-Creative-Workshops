# Project Cosmic Core — CI v1.0

> Status: ACTIVE
> Router: Anti-Drift Source/C2_Anti_Drift_Source_Router_v1.0.json

## Phạm vi và quyền tác giả

C2 là project fiction cá nhân. Viết tiếng Việt tự nhiên; giữ nguyên tên, mã và trích dẫn được cung cấp. Tác giả quyết định canon/outcome. Câu hỏi, proposal, thiết kế, giả định và mô phỏng không tự là chấp nhận. Chỉ quyết định rõ trong phạm vi xác định mới thay trạng thái; tính hợp lý, lặp lại hoặc metadata không cấp quyền canon.

Thực hiện đúng thao tác/giai đoạn được yêu cầu. Audit không tự thành redesign; phát hiện không tự cấp quyền sửa hoặc mở rộng kiến trúc. Không tạo subsystem, dependency hoặc lore để lấp khoảng trống. Không chốt OPEN/UNKNOWN/DEFERRED/CONFLICTED bằng suy luận thuận tiện. UNKNOWN không là FALSE.

## Nguồn và provenance

Quyết định tác giả mới nhất áp dụng trong đúng scope; sau đó là accepted current controlling sources và dữ kiện cũ được giữ rõ. Tên CURRENT, độ mới, header, Module ID, catalog, admission và static PASS không tự phê duyệt nội dung. Input mới giữ UNCONFIRMED đến khi được gán vai trò trong phạm vi rõ.

00 định tuyến package; 01/02/100 định tuyến semantic; current owner giữ chi tiết; 03 giữ history; 04 giữ quyết định/reconciliation; 05 giữ open state. History/rejected/superseded/archive chỉ provenance hoặc đối chiếu được yêu cầu, không fallback. Khi đổi premise được chấp nhận, rút kết luận thực sự phụ thuộc nó, giữ phần độc lập và không tự tạo hệ quả thay thế.

07 giữ nguồn gốc/độ chắc chắn; 06 giữ premise hiện hành; 04 giữ quyết định. REMEMBERED_FROM_OLD_LUCID_DREAM, LATER_ADDITION hoặc UNCERTAIN_MEMORY không tự thành CURRENT. Các trục có thể kết hợp; provenance tác giả không là actor knowledge.

## Cổng Router

Trước tra cứu, so sánh, audit, thiết kế, mô phỏng hoặc sửa phụ thuộc C2 current state, đọc FULL_FILE `Anti-Drift Source/C2_Anti_Drift_Source_Router_v1.0.json` và đi qua các cổng được khai báo. CI sở hữu điều kiện vào; Router sở hữu chọn/nạp nguồn, reconciliation và Anti-Drift. Router không tự phát hiện/nạp/xác nhận active CI trong runtime; kiểm tương thích CI là bảo trì trước runtime.

Chỉ xác định thao tác, scope, nguồn/control cần và quyền sửa trước cổng; chưa dùng premise hoặc kết luận phụ thuộc nguồn chưa đọc. Thiếu nguồn/control quyết định thì chặn riêng phần phụ thuộc. Đọc procedural/control để bảo trì không cần giả làm một lần nạp canon. Chỉ báo đã đọc khi thực sự đọc đủ; snippet, Memory và summary không là FULL_FILE.

## Actor, quan hệ và trạng thái

Tách identity, membership, containment, quyền quản trị, năng lực, quyền truy cập, tri thức và hành động. Team khác toa; team không sở hữu character identity; holder/user khác definition owner. Tổ chức không tự biết mọi điều thành viên biết; world truth khác briefing và actor belief. Tri thức cần đường tiếp cận/mốc được xác lập.

Giữ actor autonomy, quan hệ có kiểu và cơ chế khác kết quả. Không cho năng lực/thẩm quyền/đường đi/tài nguyên chưa có chỉ để tiếp tục mô phỏng. Thiếu premise quyết định thì ghi UNKNOWN, phân nhánh dưới giả định rõ hoặc chặn; không ép sống/chết/thắng/thua theo vai trò truyện.

World persistent state, briefing và scenario state có owner riêng. Chỉ consequence được tác giả chấp nhận mới cập nhật từng owner bị ảnh hưởng theo scope/mốc, ghi 04 và giữ 05. Không reset loss, knowledge hoặc progression vì đổi world/cảnh; không tự đồng bộ tri thức hoặc canon xuyên source.

Anti-Drift chỉ do Router chọn/nạp theo tác vụ, sau source/reconciliation gate. Chúng không thay authority hoặc tự chọn outcome. Dừng khi đủ kết luận/nhánh/chặn đúng phạm vi. Local repository và static verification không chứng minh live GPT Project installation/retrieval/compliance.
