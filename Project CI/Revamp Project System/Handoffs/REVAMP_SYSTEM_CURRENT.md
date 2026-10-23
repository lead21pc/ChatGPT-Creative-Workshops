# Revamp Project System — Current Handoff

HANDOFF_ID: REVAMP_SYSTEM
FILENAME: REVAMP_SYSTEM_CURRENT.md
STATUS: ACTIVE
SCOPE: Revamp-system CI and local cross-chat workstream handoff mechanism only.
UPDATED: 2026-10-24

## 1. Established current state

- USER-PROVIDED STATE: nhiều chat Revamp dùng chung repository; reasoning/quyết định nằm phân tán trong hội thoại. Đây là nguồn mô tả vấn đề vận hành, chưa phải hành vi được tái hiện trong thử nghiệm nhiều chat.
- OBSERVED: baseline trước implementation là local `main`, HEAD `07380ce14c0ef6e13310d579929932c2a8eb7ce6`, working tree sạch. Đây là mốc lịch sử tác vụ, không phải khẳng định HEAD hiện tại; kiểm tra Git để biết trạng thái mới nhất.
- DECIDED: người dùng chấp thuận promote v2.1 thành ACTIVE ngày 2026-10-18, archive predecessor, commit và push lên main. Quyền này dành cho đợt xuất bản này, không phải quyền thường trực cho chat sau.
- IMPLEMENTED: v2.1 ACTIVE là CI hiện hành trong repository, có control handoff ở 4A; một Router YAML, một CURRENT này, một mẫu dùng lại và một đặc tả kiểm tra tuyến. v2.0 đã chuyển byte-exact vào `Project CI/Source_Archive/`, là predecessor không hoạt động; chỉ dùng lại khi người dùng yêu cầu rõ. Core ChatGPT 8.9 và output-language override được giữ. Trạng thái cài đặt live Project chưa được xác minh.
- IMPLEMENTED (local, 2026-10-23): Router có block `historical_preflight`; substantive Revamp work đọc Router trước, rồi FULL_FILE `HISTORY_AND_WHAT_NOT_TO_DO.md`, rồi chọn/đọc CURRENT liên quan, sau đó kiểm tra file/runtime theo nhu cầu. History chỉ cung cấp bối cảnh lỗi lịch sử và tư thế phòng ngừa; không tạo match, thẩm quyền hay quyền triển khai. CI 4A và template không cần đổi. File history do người dùng đặt sẵn đúng đích; đã sửa hẹp thứ tự đọc ở mục 10–11 vì bản cung cấp ghi history trước Router, trái yêu cầu tích hợp. Các phần lịch sử khác giữ nguyên. LIVE VERIFIED: NOT RUN; không commit/push/deploy trong đợt tích hợp này.
- STATICALLY VERIFIED (2026-10-24): YAML parse đạt, không anchor/alias/merge key/custom tag hoặc kiểu dữ liệu mơ hồ; entry CURRENT, selection và failure behavior cũ giữ nguyên. Mọi đường dẫn tham chiếu tồn tại; CI/template giữ nguyên byte, CI 7.990 ký tự. Đặc tả giữ 18 tình huống route + 6 template và thêm 7 preflight; đã review tính nhất quán, chưa chạy live. Đảo đúng hai sửa đổi thứ tự trong history khôi phục SHA-256 bản cung cấp `3e183bd80db31ee5a8c59e4ac4f5d22149de45f77d90accd9f444d807514fc02`, xác nhận không sửa phần còn lại. Kiểm tra whitespace trong phạm vi đạt; chỉ thay đổi file Revamp, Central Hub và project khác không đổi. LIVE VERIFIED: NOT RUN.
- STATICALLY VERIFIED (2026-10-18): CI v2.1 trong giới hạn 8.000 ký tự, giữ 14 section gốc và thêm 4A; core ChatGPT 8.9, language override, các invariant và YAML default vẫn có. Hash SHA-256 v2.0 trong archive là `33c8035c231a76332f616a656f113d51a6c49a2acd60dbd81e11e0fffaaf6a85`, trùng trước chuyển. Router parse được bằng PyYAML, không anchor/alias/custom tag; đúng một entry trỏ đến một CURRENT có thật. Template/CURRENT có đủ 10 mục; đặc tả có 18 tình huống route và 6 tình huống template. UTF-8, EOF và whitespace đạt. Đây là kiểm tra cấu trúc cùng review nội dung, không phải 24 lần chạy hành vi. LIVE VERIFIED: NOT RUN.

## 2. Active problems

ID: REVAMP-HANDOFF-01
STATUS: USER-PROVIDED STATE; LOCAL IMPLEMENTATION COMPLETED; LIVE VERIFICATION NOT RUN
Problem: trạng thái công việc phân mảnh giữa nhiều chat có thể khiến chat sau tìm lại vấn đề cũ, bỏ sót việc chưa xong hoặc nhầm quyết định với triển khai.
Current state: cơ chế local đã được viết; chưa chứng minh nó giảm lỗi trong live chat.
Next: chỉ khi được phép cài thử, dùng các tình huống trong đặc tả route để kiểm chứng hành vi thật.

## 3. Outstanding / blocked

- LIVE VERIFIED: NOT RUN. Việc cài CI/Router/CURRENT vào ChatGPT Project và thử chuyển việc giữa chat chưa được xác minh; promotion repository không chứng minh deployment.
- Không có blocker local được thiết lập. Commit/push được người dùng cho phép cho đợt promotion này; xác minh kết quả thực tế qua Git commit và remote refs. Không có quyền deploy trong yêu cầu này.
- Chưa đủ nguồn authoritative để tạo CURRENT cho Central Hub hoặc workstream khác; không tạo file suy đoán.

## 4. Under consideration

None currently established. Không có phương án mới nào được ghi thành accepted chỉ vì xuất hiện trong đề xuất.

## 5. Decided but not completed

Không có quyết định thiết kế còn thiếu triển khai được thiết lập. Cơ chế local và promotion ACTIVE đã IMPLEMENTED. Publication đã được cho phép; kết quả commit/push phải kiểm tra trong Git, không suy từ handoff. Kiểm chứng live chưa chạy, nằm ở mục 3; không biến nó thành quyết định deploy mới. RECORDED DECISION != NEW AUTHORIZATION.

## 6. Resolved / closed

ID: REVAMP-HANDOFF-LOCAL
STATUS: RESOLVED (local artifact gap); IMPLEMENTED; STATICALLY VERIFIED; LIVE VERIFIED: NOT RUN
Problem: chưa có artifact local cho việc chọn và tiếp nhận handoff theo workstream.
Resolution: bộ file local tối thiểu đã được tạo. Chỉ đóng phần thiếu artifact; không đóng vấn đề hiệu quả vận hành live.
Evidence: các file trong mục 8; kiểm tra cấu trúc và review nội dung nêu tại mục 1. `git diff --check -- "Project CI"` được dùng để giữ kiểm tra trong phạm vi. Lần kiểm tra toàn repo gặp đường dẫn archive FTH quá dài; không sửa các file ngoài phạm vi để xử lý lỗi này.
Reopen only if: chứng cứ mới mâu thuẫn, nội dung triển khai lệch yêu cầu hoặc người dùng yêu cầu xét lại.

## 7. Conflicts / stale state

Không có xung đột được thiết lập khi khởi tạo. Khi file/runtime đã kiểm tra mâu thuẫn với handoff, báo rõ và đánh dấu phần ảnh hưởng STALE / CONFLICTED; file/runtime quyết định trạng thái triển khai quan sát được. Ngày UPDATED không tự chứng minh độ mới của từng mục.

Xung đột thứ tự trong bản history cung cấp đã được sửa local ở mục 10–11: Router là entrypoint, history là nguồn đầu tiên sau Router và trước CURRENT. Đây là sửa tính tương thích chỉ dẫn, không phải kiểm chứng lại các sự kiện lịch sử được kể trong file.

## 8. Relevant source anchors

Đường dẫn tính từ repository root:

- `SYSTEM_CONTEXT.md`: mục 11–12, phân biệt repository/live runtime và lớp chứng cứ; đã đọc đầy đủ.
- `AGENTS.md`: repository context gate; đã đọc đầy đủ. Chỉ dẫn AGENTS do người dùng cung cấp trong chat thêm ranh giới shared local working state và proposal review.
- `Project CI/Source_Archive/Revamp_Project_System_CI_v2.0.md`: predecessor byte-exact để provenance/rollback; không phải nguồn hiện hành hay fallback mặc định. Các bản Revamp cũ hơn đã ở cùng archive; không sửa chúng.
- `llm-controls/global-instructions/ChatGPT Plus+ Era/chatgpt v8.9.txt`: governing core đã đọc đầy đủ; không sửa trong tác vụ này.
- `Project CI/Revamp_Project_System_CI_v2.1.md`: CI ACTIVE trong repository; 4A CROSS-CHAT HANDOFF.
- `Project CI/Revamp Project System/HANDOFF_ROUTER.yaml`: chọn handoff liên quan; một entry `revamp_system`.
- `Project CI/Revamp Project System/HISTORY_AND_WHAT_NOT_TO_DO.md`: bối cảnh lỗi lịch sử/phòng ngừa; đọc FULL_FILE sau Router, trước CURRENT. HISTORY != CURRENT STATE; PAST FAILURE != PRESENT FAILURE; WARNING != AUTHORIZATION; GENEALOGY != REQUIRED ARCHITECTURE; HISTORICAL PAIN != PERMANENT MAXIMUM CONTROL.
- `Project CI/Revamp Project System/HANDOFF_TEMPLATE.md`: tạo mới hoặc thay thế toàn bộ CURRENT từ trạng thái có chứng cứ trong chat.
- `Project CI/Revamp Project System/tests/HANDOFF_ROUTE_TEST_CASES.md`: đặc tả chuẩn tắc; không phải log thử nghiệm live.

## 9. Next-entry guidance

Với tác vụ substantive Revamp, đọc Router trước, rồi FULL_FILE history được Router chỉ định trước mọi khôi phục CURRENT; sau đó chỉ chọn/đọc FULL_FILE CURRENT liên quan. History không thay CURRENT hoặc tạo match. Xác nhận quyền và trạng thái local hiện tại; kiểm tra source thật cho phần phụ thuộc. Giữ trạng thái của workstream khác riêng. Nếu không có material match, tiếp tục workflow bình thường và không nạp handoff không liên quan. Chỉ nhắc Revamp không kích hoạt quy trình; Central Hub không kế thừa history preflight hoặc cơ chế Revamp.

Khi có thay đổi đáng kể, cập nhật đúng CURRENT trong phạm vi quyền ghi; nếu chưa có quyền, báo delta đề xuất. CI ACTIVE là quyết định người dùng, không phải kết quả suy từ kiểm tra tĩnh. Không báo LIVE VERIFIED chỉ từ kết quả tĩnh hoặc publication Git. CURRENT FILE = ACTIVE HANDOFF; Git giữ lịch sử.

## 10. Explicit exclusions

- Central Hub không kế thừa Router, quy tắc CI handoff, CURRENT hoặc hành vi nạp của Revamp. Revamp có thể biết công việc Central Hub khi có nguồn phù hợp; cơ chế vẫn chỉ ở Revamp.
- Không phải global memory, transcript archive, trạng thái toàn repository hoặc snapshot từng chat. WORKSTREAM != CHAT; HANDOFF != CHAT SUMMARY.
- Không manifest/registry/schema/state engine, bộ chọn latest-version, router chọn router, hay lớp quản lý cập nhật.
- Quyền stage/commit/push của đợt promotion này không cấp quyền thường trực. Không deploy, branch/tag/worktree hoặc sửa kiến trúc Project khác từ việc tiếp nhận handoff.
