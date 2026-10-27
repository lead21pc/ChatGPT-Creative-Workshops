# Revamp Project System — Current Handoff

HANDOFF_ID: REVAMP_SYSTEM
FILENAME: REVAMP_SYSTEM_CURRENT.md
STATUS: ACTIVE
SCOPE: Revamp-system CI and local cross-chat workstream handoff mechanism only.
UPDATED: 2026-10-28

## 1. Established current state

- USER-PROVIDED STATE: nhiều chat Revamp dùng chung repository; reasoning/quyết định nằm phân tán trong hội thoại. Đây là nguồn mô tả vấn đề vận hành, chưa phải hành vi được tái hiện trong thử nghiệm nhiều chat.
- OBSERVED: baseline trước implementation là local `main`, HEAD `07380ce14c0ef6e13310d579929932c2a8eb7ce6`, working tree sạch. Đây là mốc lịch sử tác vụ, không phải khẳng định HEAD hiện tại; kiểm tra Git để biết trạng thái mới nhất.
- DECIDED: người dùng chấp thuận promote v2.1 thành ACTIVE ngày 2026-10-18, archive predecessor, commit và push lên main. Đó là quyền push của đợt xuất bản cũ, không phải quyền push thường trực; chính sách stage/commit local hiện hành được cập nhật theo quyết định 2026-10-28 dưới đây.
- IMPLEMENTED: v2.1 ACTIVE là CI hiện hành trong repository, có control handoff ở 4A; một Router YAML, một CURRENT này, một mẫu dùng lại và một đặc tả kiểm tra tuyến. v2.0 đã chuyển byte-exact vào `Project CI/Source_Archive/`, là predecessor không hoạt động; chỉ dùng lại khi người dùng yêu cầu rõ. Core ChatGPT 8.9 và output-language override được giữ. Trạng thái cài đặt live Project chưa được xác minh.
- DECIDED / IMPLEMENTED (2026-10-28): implementation local được cho phép có thể stage và commit các thay đổi đúng phạm vi sau kiểm chứng, không cần lệnh thứ hai; branch, tag và push vẫn cần quyền riêng. PUSH cần lệnh người dùng riêng; COMMIT != PUSH. Quyền audit/design/proposal hay chỉ nhận template/cập nhật CURRENT không tự cấp quyền implementation hoặc mở rộng phạm vi.
- IMPLEMENTED (2026-10-28): §2 thêm `FAILURE DETECTION != DEBUG AUTHORIZATION`: ngừng dùng đường phụ thuộc tiền đề không hợp lệ, giữ đường đó làm bằng chứng, chỉ tiếp tục từ trạng thái hiện hành đủ dùng khi an toàn, nếu không nêu blocker. Đã bỏ câu quyền Git lặp ở §4A; rút wording ẩn dụ ở §14 theo audit. Không thêm recovery framework hoặc control vào Central Hub. LIVE VERIFIED: NOT RUN.
- STATICALLY VERIFIED (2026-10-28): CI dài 7.985 ký tự gồm newline cuối; hai câu §2 đúng wording được duyệt và xuất hiện một lần, quyền push/branch/tag vẫn tách riêng, §4A giữ ranh giới Central Hub, §5–§6 không đổi. Kiểm tra UTF-8/newline/whitespace và `git diff --check` đạt. Template, history và route test không đổi; quyền chỉ nhận template/cập nhật CURRENT vẫn không tự cho phép implementation hay commit. LIVE VERIFIED: NOT RUN.
- IMPLEMENTED (local, 2026-10-24): Router `version: "1.1"`, `status: "active"`, giữ tên `HANDOFF_ROUTER.yaml`. Thứ tự: Router → nguồn repo hiện hành liên quan/đối chiếu quyết định và triển khai → FULL_FILE history → chọn/đọc CURRENT liên quan → kiểm tra thêm file/runtime khi cần. Repository preflight trỏ `https://github.com/lead21pc/chatgpt-ci-worldbuilding`, mặc định main; khi làm local phải dùng working tree hiện tại và phân biệt trạng thái local/remote. Trước khi trình bày phương án, chỉ rõ điều đã đáp ứng, gap hoặc conflict cùng source anchor; không đề xuất lại điều đã được chấp thuận như ý tưởng mới. Thiếu truy cập/chứng cứ phải báo thiếu và hoãn kết luận phụ thuộc. Bản Router chưa đánh số được lưu byte-exact tại `Project CI/Source_Archive/HANDOFF_ROUTER_pre_v1.1.yaml`; CI 4A và template giữ nguyên. LIVE VERIFIED: NOT RUN.
- STATICALLY VERIFIED (2026-10-24, Router v1.1): YAML parse đạt, không anchor/alias/merge key/custom tag hoặc kiểu dữ liệu mơ hồ; entry CURRENT, selection và failure behavior cũ giữ nguyên. Đường dẫn preflight/CURRENT tồn tại; CI/template giữ nguyên byte, CI 7.990 ký tự. Đặc tả giữ 18 tình huống route + 7 historical preflight + 6 template, thêm 4 repository preflight; đã review tính nhất quán, chưa chạy live. Router predecessor trong archive có SHA-256 `e9104429bcf90ece8a951238021d07753064d5299ecd1ceae221bbfec280d0dd`, trùng trước thay thế. History mục 10–11 đã đồng bộ repository trước history; nội dung lịch sử khác không đổi. Whitespace trong phạm vi đạt; chỉ thay đổi file Revamp, Central Hub và project khác không đổi. LIVE VERIFIED: NOT RUN.
- STATICALLY VERIFIED (2026-10-18): CI v2.1 trong giới hạn 8.000 ký tự, giữ 14 section gốc và thêm 4A; core ChatGPT 8.9, language override, các invariant và YAML default vẫn có. Hash SHA-256 v2.0 trong archive là `33c8035c231a76332f616a656f113d51a6c49a2acd60dbd81e11e0fffaaf6a85`, trùng trước chuyển. Router parse được bằng PyYAML, không anchor/alias/custom tag; đúng một entry trỏ đến một CURRENT có thật. Template/CURRENT có đủ 10 mục; đặc tả có 18 tình huống route và 6 tình huống template. UTF-8, EOF và whitespace đạt. Đây là kiểm tra cấu trúc cùng review nội dung, không phải 24 lần chạy hành vi. LIVE VERIFIED: NOT RUN.

## 2. Active problems

ID: REVAMP-HANDOFF-01
STATUS: USER-PROVIDED STATE; LOCAL IMPLEMENTATION COMPLETED; LIVE VERIFICATION NOT RUN
Problem: trạng thái công việc phân mảnh giữa nhiều chat có thể khiến chat sau tìm lại vấn đề cũ, bỏ sót việc chưa xong hoặc nhầm quyết định với triển khai.
Current state: cơ chế local đã được viết; chưa chứng minh nó giảm lỗi trong live chat.
Next: chỉ khi được phép cài thử, dùng các tình huống trong đặc tả route để kiểm chứng hành vi thật.

## 3. Outstanding / blocked

- LIVE VERIFIED: NOT RUN. Việc cài CI/Router/CURRENT vào ChatGPT Project và thử chuyển việc giữa chat chưa được xác minh; promotion repository không chứng minh deployment.
- Không có blocker local được thiết lập. Quyền commit/push từng cấp cho đợt promotion 2026-10-18 là lịch sử; chính sách stage/commit hiện hành theo §2, còn push vẫn cần lệnh riêng. Không có quyền push hoặc deploy trong đợt sửa ngày 2026-10-28.
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

Thứ tự trong history mục 10–11 đã đồng bộ với Router v1.1: vào Router, kiểm tra repo hiện hành trước history, rồi CURRENT. Đây là sửa tính tương thích chỉ dẫn, không phải kiểm chứng lại các sự kiện lịch sử được kể trong file.

## 8. Relevant source anchors

Đường dẫn tính từ repository root:

- `SYSTEM_CONTEXT.md`: mục 11–12, phân biệt repository/live runtime và lớp chứng cứ; đã đọc đầy đủ.
- `AGENTS.md`: repository context gate; đã đọc đầy đủ. Chỉ dẫn AGENTS do người dùng cung cấp trong chat thêm ranh giới shared local working state và proposal review.
- `Project CI/Source_Archive/Revamp_Project_System_CI_v2.0.md`: predecessor byte-exact để provenance/rollback; không phải nguồn hiện hành hay fallback mặc định. Các bản Revamp cũ hơn đã ở cùng archive; không sửa chúng.
- `llm-controls/global-instructions/ChatGPT Plus+ Era/chatgpt v8.9.txt`: governing core đã đọc đầy đủ; không sửa trong tác vụ này.
- `Project CI/Revamp_Project_System_CI_v2.1.md`: CI ACTIVE trong repository; 4A CROSS-CHAT HANDOFF.
- `Project CI/Revamp Project System/HANDOFF_ROUTER.yaml`: Router v1.1 ACTIVE; repository preflight trước history; một entry CURRENT `revamp_system`.
- `Project CI/Revamp Project System/HISTORY_AND_WHAT_NOT_TO_DO.md`: bối cảnh lỗi lịch sử/phòng ngừa; đọc FULL_FILE sau Router, trước CURRENT. HISTORY != CURRENT STATE; PAST FAILURE != PRESENT FAILURE; WARNING != AUTHORIZATION; GENEALOGY != REQUIRED ARCHITECTURE; HISTORICAL PAIN != PERMANENT MAXIMUM CONTROL.
- `Project CI/Revamp Project System/HANDOFF_TEMPLATE.md`: tạo mới hoặc thay thế toàn bộ CURRENT từ trạng thái có chứng cứ trong chat.
- `Project CI/Revamp Project System/tests/HANDOFF_ROUTE_TEST_CASES.md`: đặc tả chuẩn tắc; không phải log thử nghiệm live.

## 9. Next-entry guidance

Với tác vụ substantive Revamp, đọc Router trước, kiểm tra nguồn hiện hành liên quan trong repo được chỉ định và đối chiếu quyết định/triển khai, rồi FULL_FILE history trước mọi khôi phục CURRENT; sau đó chỉ chọn/đọc FULL_FILE CURRENT liên quan. Đối chiếu thêm các state/decision từ CURRENT với source hiện tại trước khi trình bày phương án. Không coi giải pháp đã chấp thuận là đề xuất mới; chỉ mở lại khi có chứng cứ trái mới, triển khai lệch hoặc người dùng yêu cầu. History không thay CURRENT hoặc tạo match. Xác nhận quyền, dùng local working tree khi tác vụ phụ thuộc local; giữ trạng thái các workstream riêng. Không match thì không nạp handoff khác. Chỉ nhắc Revamp không kích hoạt quy trình; Central Hub không kế thừa repository/history preflight hoặc cơ chế Revamp.

Khi có thay đổi đáng kể, cập nhật đúng CURRENT trong phạm vi quyền ghi; nếu chưa có quyền, báo delta đề xuất. CI ACTIVE là quyết định người dùng, không phải kết quả suy từ kiểm tra tĩnh. Không báo LIVE VERIFIED chỉ từ kết quả tĩnh hoặc publication Git. CURRENT FILE = ACTIVE HANDOFF; Git giữ lịch sử.

## 10. Explicit exclusions

- Central Hub không kế thừa Router, quy tắc CI handoff, CURRENT hoặc hành vi nạp của Revamp. Revamp có thể biết công việc Central Hub khi có nguồn phù hợp; cơ chế vẫn chỉ ở Revamp.
- Không phải global memory, transcript archive, trạng thái toàn repository hoặc snapshot từng chat. WORKSTREAM != CHAT; HANDOFF != CHAT SUMMARY.
- Không manifest/registry/schema/state engine, bộ chọn latest-version, router chọn router, hay lớp quản lý cập nhật.
- Handoff không tự cấp quyền implementation. Khi implementation local được cho phép, stage/commit thay đổi đã kiểm chứng trong phạm vi theo §2; branch/tag/push vẫn cần quyền riêng. Không deploy, tạo worktree hoặc sửa kiến trúc Project khác chỉ từ việc tiếp nhận handoff.
