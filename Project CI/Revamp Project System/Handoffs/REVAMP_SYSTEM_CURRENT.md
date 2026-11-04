# Revamp Project System — Current Handoff

HANDOFF_ID: REVAMP_SYSTEM
FILENAME: REVAMP_SYSTEM_CURRENT.md
STATUS: ACTIVE
SCOPE: Revamp-system CI, two task paths and bounded authoring/continuity contracts only.
UPDATED: 2026-11-05

## 1. Established current state

- DECIDED / IMPLEMENTED (2026-11-05, receipt workstream): AT_R giữ toàn bộ wording control bằng tiếng Anh và tiêu chí context selection của correction local `60e68e7`. Bổ sung completeness cho task artifact so với state/premise handoff: giữ mọi material distinction cần để continuation không drift, không tối thiểu hóa fact count. Receipt tùy nhu cầu ghi state chuyển/distinctions giữ/context cố ý bỏ, gap khi material; không thay body, không là proof/validator/authority. OPEN/PROVISIONAL/UNKNOWN và provenance phải giữ khi material; mechanisms không nhập/rút gọn đổi nghĩa; REJECTED chỉ giữ khi omission tạo nguy cơ drift thực tế. Không receipt bắt buộc cho prompt đơn giản.
- STATICALLY VERIFIED (2026-11-05, receipt workstream): 8/8 test cấu trúc/contract Revamp đạt; review tĩnh H01 bounded Codex task, H02 premise continuation, H03 no receipt needed đạt theo contract. So sánh với HEAD xác nhận toàn văn AT_R ngoài section receipt mới giữ nguyên và template chỉ thêm đoạn vị trí tùy nhu cầu; 10 mục cũ còn nguyên. UTF-8/LF/không BOM/trailing whitespace, English control trong AT_R, diff scope/check đạt. CI/Router không sửa. LIVE VERIFIED: NOT RUN.
- IMPLEMENTED (2026-11-05): HANDOFF_TEMPLATE cho phép receipt không đánh số sau 10 mục hiện có, không bắt buộc field hay làm CURRENT cũ mất hợp lệ. AT_R sở hữu authoring/compression; template sở hữu vị trí trong persisted CURRENT. CI v2.5, Router v2.0, hai-ID model, điều kiện nạp/ghi CURRENT và Central Hub boundary giữ nguyên. Không có parser, registry, schema, validator, lifecycle hoặc subsystem mới. Case H01–H03 thêm vào đặc tả; không phải live model runs. Quyền tác vụ chỉ local implementation/verified commit; không push/deploy.

- DECIDED / IMPLEMENTED (2026-11-05): CI v2.5 ACTIVE, TASK_ROUTER v2.0 ACTIVE thay HANDOFF_ROUTER v1.1. CI là authority duy nhất; Router chỉ chọn task/context/source. ID1 REVAMP_CORE mặc định cho direct work, gồm analysis/creative/worldbuilding/brainstorm và implementation có quyền; ID2 AUTHORING qua singleton AT_R.md khi output chính là prompt/enhanced prompt/downstream brief/bounded handoff artifact. Preparation cho một prompt nằm trong ID2; context từ turn trước không tạo composition. Task mơ hồ thì hỏi deliverable, không suy execution/quyền. Không thêm registry, composition hoặc kiến trúc Central Hub.
- IMPLEMENTED (2026-11-05): task độc lập làm trực tiếp; task phụ thuộc repository/system đi repo → FULL_FILE history → chỉ needed FULL_FILE CURRENT khi còn thiếu continuity. Áp điều kiện này cho cả hai ID. Giữ selection, failure handling, repo/runtime precedence, scoped stale claims và Central Hub isolation cũ. CURRENT chỉ cập nhật khi material change + materially useful cross-chat continuity + authorized write scope, theo HANDOFF_TEMPLATE. AUTHORING != EXECUTION; giữ Codex decision handoff, không nâng state/authorization. Các mốc v2.4/v1.1 bên dưới là lịch sử workstream, không là active pins mới.

- STATICALLY VERIFIED (2026-11-05): 8 kiểm tra tự động cấu trúc/contract đạt bằng `python -B -m unittest discover -s "Revamp Project System/tests" -p "test_*.py" -v`; YAML parse/token conservative, đúng hai ID/owner/path, CI 7.984 ký tự, UTF-8/LF/không BOM/trailing whitespace đạt. So sánh trực tiếp trước archive xác nhận CI §1–§4 và §5–§14 nguyên nội dung; Router selection/failure/CURRENT và preflight giữ nguyên ngoài delta scope/role/version. Review đặc tả 43 case cũ + 15 case mới; R16 được giới hạn thêm điều kiện useful continuity theo quyết định v2.5. Không phải 58 lượt chạy model.
- ARCHIVED byte-exact (2026-11-05): CI v2.4 SHA-256 `753dbbea1185b2e71063ba9a8d2f3df8a44398e6653091f235d641c12a07b5b8`; HANDOFF_ROUTER v1.1 SHA-256 `0f1a83d5791d62fded820aa48df49ee5ad0bd8d68e20483ace5a23ab517e411b`. Checker trước chuyển trả PASS_SHARED, dùng đúng Source_Archive chung; hash trước/sau khớp. Hai predecessor không còn active. LIVE VERIFIED: NOT RUN; không deploy hoặc push. Kiểm tra diff toàn repo gặp `Filename too long` tại archive FTH ngoài phạm vi; kiểm tra diff trong Project CI đạt, không sửa file ngoài scope. Kết quả Git/commit tra trực tiếp trong repository.

- DECIDED / IMPLEMENTED (2026-11-03): repo-first inspection vẫn là bước chính; sau repo/history chỉ nạp FULL_FILE CURRENT khi còn cần prior workstream continuity mà nguồn hiện tại chưa đủ cung cấp. WORKSTREAM RELEVANCE != HANDOFF NECESSITY. Handoff là bounded continuity, không phải global repository snapshot; pin shared version là mốc workstream, không là current-stack authority vĩnh viễn. Repo/runtime hiện hành quyết định implementation/artifact state; chỉ claim bị ảnh hưởng STALE / CONFLICTED, giữ rationale/quyết định/verification attribution còn hợp lệ. STALE SHARED VERSION PIN != STALE ENTIRE HANDOFF; không đồng bộ mọi CURRENT khi subsystem khác nâng shared stack.
- STATICALLY VERIFIED (2026-11-03): YAML parse và kiểm tra token đạt, không anchor/alias/merge key/custom tag; entry, repository_preflight, history ordering, authorization và Central Hub boundary giữ nguyên. Router giữ v1.1; CI v2.4 giữ nguyên. Review tĩnh 18 route + 7 history + 4 repository-preflight + 6 template + 8 continuity cases (43 tổng) đạt theo phạm vi đặc tả; không phải chạy live. UTF-8/LF/không BOM/trailing whitespace và `git diff --check` đạt. LIVE VERIFIED: NOT RUN. Commit của delta này: tra `git log -1 --format=%H -- "Project CI/Revamp Project System/HANDOFF_ROUTER.yaml"`; hash không nhúng vào chính snapshot commit.

- DECIDED / IMPLEMENTED (2026-11-01): theo thay đổi đã được người dùng duyệt, v2.4 được promote trực tiếp ACTIVE, thay v2.3; không tạo candidate stage. §2: yêu cầu prompt Codex là decision handoff cho scope/quyết định đã chốt, chỉ mở lại phần có concrete blocker. §6: `CANDIDATE != REQUIRED STAGE`, baseline được duyệt có thể promote trực tiếp. §8: giữ known-correct path khi thử replacement, không giả định incumbent cho kiến trúc mới. Governing base vẫn là ChatGPT Project Global Native 9.0; các control khác giữ nguyên.
- STATICALLY VERIFIED (2026-11-01): v2.4 có 7.978 ký tự gồm newline cuối, đủ 14 section và §4A; chỉ ba đoạn được duyệt cùng version/ngày adoption thay đổi. Hai invariant mới xuất hiện đúng một lần; authorization, stage/commit policy, failure recovery và Central Hub boundary giữ nguyên. Rà soát văn bản A–F đạt; đây không phải sáu lần chạy live. UTF-8/LF/newline cuối, không BOM/trailing whitespace và `git diff --check` đạt. v2.3 được archive byte-exact, SHA-256 `a04a6d276fe299c019311518090dd997880f6744279080fa53a947a4a5a856ce`. LIVE VERIFIED: NOT RUN.

- DECIDED / IMPLEMENTED (2026-10-31): theo yêu cầu người dùng, đã đổi tên repository GitHub thành `lead21pc/ChatGPT-Creative-Workshops`; API xác nhận canonical URL `https://github.com/lead21pc/ChatGPT-Creative-Workshops`, giữ repository ID `1361687313`. Đã đổi `origin` local sang HTTPS `.git` tương ứng và Router `repository_preflight.url` sang canonical URL; cập nhật sáu liên kết release hiện hành trong README root và `distribution/README.md`. Router vẫn v1.1, chỉ đổi endpoint; thứ tự nạp, entry và ranh giới Central Hub giữ nguyên. Các mốc lịch sử/provenance vẫn giữ tên cũ khi mô tả trạng thái trước rename. Không có quyền push trong tác vụ này. LIVE VERIFIED: NOT RUN.
- STATICALLY VERIFIED (2026-10-31): Router parse YAML đạt, so sánh với baseline xác nhận chỉ URL thay đổi; version và ranh giới Central Hub giữ nguyên. `git diff --check` đạt. Lần truy cập URL mới trước thao tác rename trả `Repository not found`; đó là kết quả trước rename, không phải trạng thái truy cập hiện hành. Xác minh GitHub repository không phải kiểm chứng runtime ChatGPT Project.

- DECIDED / IMPLEMENTED (2026-10-30): người dùng chấp thuận đặt `FAILURE_ENTRY_MODES.md` ở gốc `Revamp Project System/`, giữ nội dung nguồn `D:\FAILURE_ENTRY_MODES.md`. Đây là reference so sánh Case 1/2/1.5; entry mode không xác định nguyên nhân, mức nghiêm trọng hoặc trạng thái chứng cứ. History §8 có liên kết đọc tùy nhu cầu; không thêm mandatory preflight, Router entry hoặc control. CI v2.3 và Router giữ nguyên. Kiểm chứng live: NOT RUN; thêm file trong repository không chứng minh live deployment.

- USER-PROVIDED STATE: nhiều chat Revamp dùng chung repository; reasoning/quyết định nằm phân tán trong hội thoại. Đây là nguồn mô tả vấn đề vận hành, chưa phải hành vi được tái hiện trong thử nghiệm nhiều chat.
- OBSERVED: baseline trước implementation là local `main`, HEAD `07380ce14c0ef6e13310d579929932c2a8eb7ce6`, working tree sạch. Đây là mốc lịch sử tác vụ, không phải khẳng định HEAD hiện tại; kiểm tra Git để biết trạng thái mới nhất.
- DECIDED: người dùng chấp thuận promote v2.1 thành ACTIVE ngày 2026-10-18, archive predecessor, commit và push lên main. Đó là quyền push của đợt xuất bản cũ, không phải quyền push thường trực; chính sách stage/commit local hiện hành được cập nhật theo quyết định 2026-10-28 dưới đây.
- DECIDED / IMPLEMENTED (2026-10-29): người dùng chấp thuận audit `ACCEPT` và promote v2.3 thành ACTIVE với governing base ChatGPT Project Global Native 9.0. Nội dung hành vi §1–§14 được giữ nguyên từ v2.2; chỉ metadata version/status/base thay đổi. v2.2 được lưu byte-exact trong `Project CI/Source_Archive/` làm predecessor không hoạt động; v2.1 và v2.0 vẫn ở archive. Chỉ dùng predecessor đã lưu khi người dùng yêu cầu rõ. Trạng thái cài đặt live Project chưa được xác minh; repository promotion không chứng minh live deployment.
- STATICALLY VERIFIED (2026-10-29): v2.3 dài 7.992 ký tự gồm newline cuối; đủ 14 section và §4A, phần từ §1 đến cuối khớp v2.2 byte-for-byte, base là ChatGPT Project Global Native 9.0 và không còn governing-base reference tới ChatGPT 8.9. UTF-8, LF, newline cuối, không BOM/trailing whitespace đạt. Bản archive v2.2 có SHA-256 `43e9ac6c17790e11cfe581b29a7a9679aafe543a4743f93b603f0cc87a6b3eba`, trùng bản active trước promotion. Router/CURRENT paths còn hợp lệ; `git diff --check` trong phạm vi đạt. LIVE VERIFIED: NOT RUN.
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
- Không có blocker local được thiết lập. Quyền push từng cấp cho các đợt publication cũ là lịch sử; chính sách stage/commit hiện hành theo §2, còn push vẫn cần lệnh riêng. Đợt rebase ngày 2026-10-29 không có quyền push hoặc deploy.
- Chưa đủ nguồn authoritative để tạo CURRENT cho Central Hub hoặc workstream khác; không tạo file suy đoán.

## 4. Under consideration

None currently established. Không có phương án mới nào được ghi thành accepted chỉ vì xuất hiện trong đề xuất.

## 5. Decided but not completed

Không có quyết định thiết kế còn thiếu triển khai được thiết lập. Baseline v2.5 local và promotion ACTIVE đã IMPLEMENTED. Tác vụ v2.5 cho phép commit local sau kiểm chứng; không cho push. Các quyền publication cũ không là quyền mới; kết quả commit/push phải kiểm tra trong Git, không suy từ handoff. Kiểm chứng live chưa chạy, nằm ở mục 3; không biến nó thành quyết định deploy mới. RECORDED DECISION != NEW AUTHORIZATION.

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

- `Project CI/Revamp Project System/FAILURE_ENTRY_MODES.md`: reference so sánh tình huống lỗi đi vào Revamp, đặc biệt Case 1.5; giải thích CI §2, không thay thế control, CURRENT hoặc phân loại chứng cứ §4.

Đường dẫn tính từ repository root:

- `SYSTEM_CONTEXT.md`: mục 11–12, phân biệt repository/live runtime và lớp chứng cứ; đã đọc đầy đủ.
- `AGENTS.md`: repository context gate; đã đọc đầy đủ. Chỉ dẫn AGENTS do người dùng cung cấp trong chat thêm ranh giới shared local working state và proposal review.
- `Project CI/Source_Archive/Revamp_Project_System_CI_v2.2.md`: predecessor byte-exact để provenance/rollback khi được yêu cầu; không phải nguồn hiện hành hay fallback mặc định. v2.1, v2.0 và các bản cũ hơn ở cùng archive.
- `llm-controls/global-instructions/ChatGPT Plus+ Era/chatgpt v8.9.txt`: governing core cũ của v2.2; đã đọc đầy đủ và không sửa trong tác vụ rebase.
- `llm-controls/global-instructions/ChatGPT Project Global Native/chatgpt v9.0.txt`: governing core hiện hành của v2.5, kế thừa từ v2.3/v2.4; không sửa trong đợt promotion này.
- `llm-controls/global-instructions/ChatGPT Project Global Native/DESIGN_RATIONALE.md`: rationale bắt buộc đã đọc đầy đủ; tham chiếu thiết kế, không phải bằng chứng live.
- `Project CI/Source_Archive/Revamp_Project_System_CI_v2.3.md`: predecessor không hoạt động, được lưu byte-exact khi promote v2.4; chỉ dùng cho provenance/rollback khi được yêu cầu.
- `Project CI/Revamp_Project_System_CI_v2.5.md`: CI ACTIVE; §4A task routing/continuity, giữ §2 Codex decision handoff/authorization/failure recovery và các section khác.
- `Project CI/Source_Archive/Revamp_Project_System_CI_v2.4.md` và `Project CI/Source_Archive/HANDOFF_ROUTER_v1.1.yaml`: predecessor không hoạt động, byte-exact; không dùng làm nguồn mặc định.
- `Project CI/Revamp Project System/AT_R.md`: singleton ID2, minimum authoring contract, không thực thi downstream.
- `Project CI/Revamp Project System/TASK_ROUTER.yaml`: Router v2.0 ACTIVE; ID1/ID2, conditional repository/history/CURRENT context; một CURRENT entry `revamp_system`.
- `Project CI/Revamp Project System/HISTORY_AND_WHAT_NOT_TO_DO.md`: bối cảnh lỗi lịch sử/phòng ngừa; đọc FULL_FILE sau Router, trước CURRENT. HISTORY != CURRENT STATE; PAST FAILURE != PRESENT FAILURE; WARNING != AUTHORIZATION; GENEALOGY != REQUIRED ARCHITECTURE; HISTORICAL PAIN != PERMANENT MAXIMUM CONTROL.
- `Project CI/Revamp Project System/HANDOFF_TEMPLATE.md`: tạo mới hoặc thay thế toàn bộ CURRENT từ trạng thái có chứng cứ trong chat.
- `Project CI/Revamp Project System/tests/HANDOFF_ROUTE_TEST_CASES.md`: 61 case đặc tả chuẩn tắc (58 baseline + H01–H03); không phải log thử nghiệm live.
- `Project CI/Revamp Project System/tests/test_task_router.py`: 8 kiểm tra cấu trúc/contract, không phải live harness hay classifier runtime.

## 9. Next-entry guidance

Chọn ID theo deliverable hiện tại trong TASK_ROUTER; task độc lập làm trực tiếp, ID2 đọc AT_R và không chạy downstream. Với tác vụ phụ thuộc repository/system, đọc Router trước, kiểm tra nguồn repo hiện hành và đối chiếu quyết định/triển khai, rồi FULL_FILE history. Từ baseline đó, chỉ chọn/đọc FULL_FILE CURRENT nếu còn cần prior continuity mà nguồn hiện tại chưa đủ cung cấp; repo đủ thì không nạp, preflight vẫn hoàn tất. Đối chiếu CURRENT đã nạp với repo/runtime; pin shared-stack cũ không thay current version hoặc vô hiệu toàn handoff. Không coi giải pháp đã chấp thuận là đề xuất mới; chỉ mở lại khi có chứng cứ trái mới, triển khai lệch hoặc người dùng yêu cầu. History không thay CURRENT hoặc tạo match. Xác nhận quyền, dùng local working tree hiện hành; giữ các workstream riêng. Nếu continuity còn thiếu và không có nguồn hợp lệ, báo UNKNOWN/gap; không bịa state. Central Hub không kế thừa repository/history preflight hoặc cơ chế Revamp.

Chỉ khi state đổi đáng kể và cross-chat continuity materially useful, cập nhật đúng CURRENT trong phạm vi quyền ghi; nếu chưa có quyền, báo delta đề xuất. CI ACTIVE là quyết định người dùng, không phải kết quả suy từ kiểm tra tĩnh. Không báo LIVE VERIFIED chỉ từ kết quả tĩnh hoặc publication Git. CURRENT FILE = ACTIVE HANDOFF; Git giữ lịch sử.

## 10. Explicit exclusions

- Central Hub không kế thừa Router, quy tắc CI handoff, CURRENT hoặc hành vi nạp của Revamp. Revamp có thể biết công việc Central Hub khi có nguồn phù hợp; cơ chế vẫn chỉ ở Revamp.
- Không phải global memory, transcript archive, trạng thái toàn repository hoặc snapshot từng chat. WORKSTREAM != CHAT; HANDOFF != CHAT SUMMARY.
- Không manifest/registry/schema/state engine, bộ chọn latest-version, router chọn router, lớp quản lý cập nhật, multi-ID execution graph hoặc composition runtime. Không bắt đầu tối ưu sâu AT_R trong v2.5.
- Handoff không tự cấp quyền implementation. Khi implementation local được cho phép, stage/commit thay đổi đã kiểm chứng trong phạm vi theo §2; branch/tag/push vẫn cần quyền riêng. Không deploy, tạo worktree hoặc sửa kiến trúc Project khác chỉ từ việc tiếp nhận handoff.

## Handoff Receipt

- Đã chuyển: baseline hai-ID Revamp, contract receipt tối thiểu, owner AT_R/template và giới hạn kiểm chứng/authorization của workstream.
- Đã giữ: DECIDED khác IMPLEMENTED khác STATICALLY VERIFIED/LIVE VERIFIED; context omission khác quên state; receipt khác body/proof/authority; known gaps live trong mục 3 vẫn mở.
- Cố ý không chuyển: toàn văn predecessor archive, state chi tiết của project khác và transcript hội thoại; các phần này không cần để tiếp tục workstream receipt.
- Gap còn biết: chưa thử receipt trên model hoặc premise thật; không suy hiệu quả live từ contract/spec tĩnh.
