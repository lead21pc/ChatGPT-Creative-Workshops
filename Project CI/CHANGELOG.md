# Changelog — Revamp Project System CI

Cập nhật ngày 2026-11-01. Phạm vi: dòng Revamp CI và các thay đổi trực tiếp của cơ chế handoff đi kèm.

Ngày commit được quy về UTC+07:00. Ngày nhập hoặc khôi phục file vào Git không chứng minh ngày tạo, ngày chấp thuận hay ngày cài vào ChatGPT Project. Các bản trong `Source_Archive` chỉ được đọc để đối chiếu lịch sử theo yêu cầu làm changelog; chúng không trở thành nguồn điều khiển hiện hành.

## Trạng thái hiện hành

- CI: [Revamp_Project_System_CI_v2.4.md](Revamp_Project_System_CI_v2.4.md), `ACTIVE` trong repository; governing base là ChatGPT Project Global Native 9.0.
- Handoff Router: [HANDOFF_ROUTER.yaml](<Revamp Project System/HANDOFF_ROUTER.yaml>), v1.1, `active`.
- Trạng thái tiếp nối và bằng chứng kiểm chứng được ghi tại [REVAMP_SYSTEM_CURRENT.md](<Revamp Project System/Handoffs/REVAMP_SYSTEM_CURRENT.md>).
- `LIVE VERIFIED: NOT RUN` theo CURRENT. Promotion, commit và kiểm tra tĩnh không chứng minh cài đặt hoặc hành vi live. Changelog này ghi lịch sử, không cấp quyền hay thay CURRENT.

## 2026-11-01 — CI v2.4: chuyển quyết định sang Codex và promotion trực tiếp

- Người dùng duyệt promotion trực tiếp v2.4 ACTIVE; không tạo candidate stage. Governing base vẫn là ChatGPT Project Global Native 9.0.
- §2 coi yêu cầu prompt Codex là decision handoff: mang scope/quyết định đã chốt sang prompt, chỉ mở lại phần bị concrete blocker.
- §6 giữ exploration chưa chốt ở trạng thái provisional và thêm `CANDIDATE != REQUIRED STAGE`; baseline được người dùng duyệt có thể promote trực tiếp.
- §8 giữ đường known-correct khi thử bản thay thế, không dựng incumbent hoặc đường candidate giả cho kiến trúc mới.
- Chỉ thay đúng ba đoạn đã duyệt cùng version/ngày adoption; lưu v2.3 byte-exact trong `Source_Archive` và cập nhật CURRENT. v2.4 dài 7.978 ký tự gồm newline cuối; kiểm tra tĩnh A–F và định dạng đạt. LIVE VERIFIED: NOT RUN.

## 2026-10-29 — CI v2.3: chuyển governing base sang Global Native 9.0

Commit: `34e250c` — `Promote Revamp CI v2.3 to Global Native 9.0`.

- Chuyển base từ ChatGPT 8.9 sang ChatGPT Project Global Native 9.0; cập nhật version và ngày adoption.
- Giữ nguyên toàn bộ nội dung từ §1 đến cuối so với v2.2, gồm quyền stage/commit local, quy tắc tiền đề sai và handoff. Đây là thay đổi base được kế thừa; không phải bằng chứng hành vi tổng thể của hai base giống nhau.
- Lưu v2.2 byte-exact trong `Source_Archive`; cập nhật CURRENT cho v2.3 `ACTIVE`.
- Bằng chứng đã ghi trong CURRENT: 7.992 ký tự gồm newline cuối, đủ 14 section và §4A, kiểm tra UTF-8/LF/whitespace và đường dẫn đạt; live chưa chạy.

## 2026-10-28 — CI v2.2: quyền commit local và xử lý tiền đề sai

Commits: `c8a98d1` — sửa nội dung trên file v2.1 lúc đó; `7c20340` — tách thành v2.2 và bảo toàn v2.1 trước sửa.

- §2 cho phép implementation local đã được cấp quyền stage và commit thay đổi đúng phạm vi sau kiểm chứng. Branch, tag và push vẫn cần quyền riêng; audit/design/proposal không tự cấp quyền implementation.
- Thêm `FAILURE DETECTION != DEBUG AUTHORIZATION`: ngừng dùng đường phụ thuộc tiền đề không hợp lệ, giữ làm bằng chứng; tiếp tục từ trạng thái hiện hành đủ dùng khi an toàn, nếu không báo blocker.
- Bỏ câu quyền Git lặp ở §4A; rút phần ẩn dụ ở §14. Không thêm recovery framework.
- Phát hành v2.2 `ACTIVE`, tiếp tục dùng ChatGPT 8.9; archive giữ v2.1 trước đợt sửa, không phải bản trung gian đã sửa dưới tên v2.1.
- Bằng chứng đã ghi trong CURRENT: 7.985 ký tự, wording được duyệt xuất hiện đúng một lần, §5–§6 giữ nguyên, kiểm tra định dạng đạt; live chưa chạy.

## 2026-10-24 — Router v1.1: kiểm tra repository trước khôi phục trạng thái

Commit: `12a9a25` — `Promote Revamp handoff router v1.1 with repository preflight`.

- Thêm repository preflight: đọc nguồn hiện hành liên quan, đối chiếu quyết định đã chấp thuận và phần đã triển khai trước khi đề xuất; làm local phải dùng working tree hiện tại, kể cả dependency dirty có liên quan.
- Thứ tự đọc trở thành Router → nguồn repository hiện hành → history đầy đủ → CURRENT phù hợp → kiểm tra thêm file/runtime khi cần.
- Phân biệt điều đã đáp ứng, gap và conflict với source anchor; không trình bày lại giải pháp đã chấp thuận như ý tưởng mới. Thiếu chứng cứ thì hoãn kết luận phụ thuộc.
- Đánh số Router v1.1, lưu predecessor tại `Source_Archive/HANDOFF_ROUTER_pre_v1.1.yaml`; đồng bộ thứ tự trong history, CURRENT và đặc tả test. CI vẫn là v2.1; CI và template không đổi.
- CURRENT ghi YAML parse và kiểm tra cấu trúc đạt; thêm 4 tình huống repository preflight. Đây là đặc tả/review, không phải kết quả chạy live.

## 2026-10-24 — bổ sung historical preflight

Commit: `8ca2b6b` — `Integrate Revamp historical preflight before CURRENT recovery`.

- Thêm `HISTORY_AND_WHAT_NOT_TO_DO.md` và yêu cầu đọc đầy đủ trước khôi phục CURRENT trong công việc Revamp substantive.
- Ghi bối cảnh lỗi lịch sử, giới hạn chống mở rộng kiến trúc và ranh giới `HISTORY != CURRENT STATE`, `PAST FAILURE != PRESENT FAILURE`.
- Cập nhật Router, CURRENT và đặc tả test; không đổi version CI. Bước repository preflight được bổ sung ở commit tiếp theo cùng ngày.

## 2026-10-18 — CI v2.1: ACTIVE và handoff theo workstream

Commit: `2fed113` — `Promote Revamp CI v2.1 and add workstream handoff controls`.

- Chuyển từ v2.0 `PROPOSAL` sang v2.1 `ACTIVE` theo adoption; tiếp tục governing base ChatGPT 8.9.
- Thêm §4A `CROSS-CHAT HANDOFF`: chọn nguồn liên quan, đọc `FULL_FILE`, giữ trạng thái các workstream riêng; handoff không tự chứng minh trạng thái thực tế, acceptance hoặc authorization.
- Tạo Router, template, CURRENT đầu tiên và đặc tả route test. Cập nhật CURRENT khi có thay đổi đáng kể trong phạm vi được phép, không theo từng tin nhắn.
- Rút gọn wording để giữ giới hạn CI 8.000 ký tự; giữ 14 section gốc và các nguyên tắc evidence, minimum sufficient change, YAML default.
- Giới hạn cơ chế cho Revamp; Central Hub không kế thừa CI handoff, Router, CURRENT hay hành vi nạp này. Archive v2.0 byte-exact.
- CURRENT ghi kiểm tra cấu trúc đạt, gồm 18 tình huống route và 6 tình huống template trong đặc tả; không phải 24 lần chạy hành vi. Live chưa chạy.

## 2026-10-12 — CI v2.0: governing base ChatGPT 8.9

Commit: `68386b1` — `Add Revamp Project System CI v2.0`.

- Thêm v2.0 vào `Project CI`, trạng thái trong file là `PROPOSAL`.
- So với v1.1 được lưu, đổi version và governing-base references từ ChatGPT 8.9 temp sang ChatGPT 8.9; các quy tắc còn lại giữ nguyên.
- Giữ mô hình supplement kế thừa toàn bộ base, language override và YAML default.

## 2026-10-13 — khôi phục lineage vào archive

Commit: `40663bb` — `recover(project-ci): preserve current archive lineage`.

- Khôi phục bản Revamp không đánh số, v1.0 và v1.1 vào `Project CI/Source_Archive`, cùng một số artifact CI lịch sử khác.
- Đây là mốc bảo toàn lịch sử trong Git, không phải đợt phát hành hay bằng chứng các bản được tạo ngày 2026-10-13. Thứ tự mục changelog ưu tiên dòng phiên bản; mốc khôi phục này xảy ra sau commit thêm v2.0.

## v1.1 và v1.0 — các bản đề xuất lịch sử

Nguồn: các file lưu trong `Source_Archive`, được nhập tại `40663bb`. Chưa xác lập ngày tạo/adoption riêng từ các nguồn đã kiểm tra.

- **v1.1 so với v1.0:** thêm YAML default ở §5 cho Router/manifest/index/registry và machine config; dùng YAML bảo thủ, tránh anchor/alias, merge key, custom tag và cú pháp phụ thuộc parser. Không ép đổi prose hoặc live config chỉ để đồng nhất; không tạo schema/validator mới nếu thiếu lỗi cụ thể.
- **v1.0 so với bản không đánh số:** chuyển base từ ChatGPT 8.7 sang ChatGPT 8.9 temp với yêu cầu kế thừa đầy đủ; khai báo language override; làm rõ repository access chỉ cho inspection, target mặc định local và quyền branch/tag/commit/push tách riêng.
- Cả hai file đều khai báo `PROPOSAL`; việc có mặt trong archive không chứng minh từng được kích hoạt.

## 2026-09-30 — bản Revamp không đánh số, dựa trên ChatGPT 8.7

Commit: `568d42d` — `Add Project System CI revamp`.

- Thêm `Revamp Project System CI.md` với trạng thái `PROPOSAL`.
- Thiết lập 14 section: bảo toàn tác vụ/giai đoạn, đánh giá đề xuất người dùng trước, kiểm tra hệ thống thực tế, sửa đổi đủ dùng, tăng độ phức tạp theo bằng chứng, giữ phạm vi và hành vi đã kiểm chứng, tách kiến trúc lưu trữ khỏi ontology, tránh recursive governance.
- Phân biệt `OBSERVED FAILURE`, `REPRODUCED FAILURE`, `SUPPORTED RISK`, `HYPOTHETICAL FUTURE RISK`; cho phép exploration được yêu cầu nhưng không tự nâng proposal thành baseline.
- File hiện được bảo toàn tại `Source_Archive/Revamp Project System CI.md`. Ngày trên là ngày commit, không khẳng định ngày khởi thảo hoặc live adoption.

## Nguồn và giới hạn kiểm chứng

- Đối chiếu nội dung CI hiện hành, Router, history, CURRENT, các bản Revamp lưu và commit/diff liên quan trong Git local. Không suy trạng thái remote từ lịch sử local.
- Các kết quả kiểm tra tĩnh lịch sử ở trên là bằng chứng đã được CURRENT ghi nhận; tác vụ viết changelog không chạy lại toàn bộ kiểm tra cũ hay thử nghiệm live.
- Changelog không thay đổi CI, Router, CURRENT, artifact lưu hoặc trạng thái deployment; không tạo version CI mới.
