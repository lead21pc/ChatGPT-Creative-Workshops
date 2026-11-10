---
name: revamp-system-maintenance
description: Audit, thiết kế và bảo trì Revamp Project System, gồm CI, Task Router, AT_R và continuity. Kiểm tra semantic contract của base trước thay đổi control. Không dùng cho tác vụ do Revamp hỗ trợ nhưng không bảo trì chính Revamp, hoặc áp kiến trúc Revamp lên project khác.
---

# Bảo trì Revamp System

## Phạm vi và nguồn hiện hành

Đây là quy trình bảo trì, không phải runtime CI và không cấp quyền. Giữ đúng yêu cầu audit/design/implementation hiện tại; audit hoặc proposal không cho phép sửa. Quyền implementation đã cấp trong phiên vẫn có hiệu lực trong đúng scope.

Tìm repository chứa target; đọc `SYSTEM_CONTEXT.md`, `AGENTS.md`, rồi nguồn local hiện hành. Điểm vào là `Project CI/CHANGELOG.md` và CI active mà nó dẫn tới; không suy active từ số phiên bản lớn nhất. Đọc đầy đủ CI trước khi phân tích control. Với task phụ thuộc hệ thống, đọc `Project CI/Revamp Project System/TASK_ROUTER.yaml`, nguồn trực tiếp và FULL_FILE `HISTORY_AND_WHAT_NOT_TO_DO.md`; chỉ đọc CURRENT khi còn cần prior continuity hoặc task yêu cầu cập nhật nó. Không thay local state mới hơn bằng remote snapshot.

Đọc Global CI và rationale đầy đủ khi dùng chúng làm nguồn thiết kế/migration; rationale hiện hành nằm ở `llm-controls/global-instructions/ChatGPT Project Global Native/DESIGN_RATIONALE.md`. Kiểm tra constraint dung lượng từ nguồn hiện hành. Ưu tiên rule có tác dụng điều khiển hơn metadata; metadata không chứng minh tích hợp core, deployment hay live pass.

## Base semantics preflight

Bắt buộc trước khi tiếp tục task liên quan CI, Router, control architecture, inheritance, base/based on/governs/supplement, kế thừa hoặc migration từ Global CI. Xác định semantic contract bằng nội dung đầy đủ và luồng dependency thực tế: ai sở hữu control, control nằm ở đâu, cần nạp gì để vận hành. Không suy nghĩa chỉ từ keyword hoặc grep.

Đối với Revamp:

- `BASE = DESIGN SOURCE / LINEAGE`: invariant và core logic cần thiết được tích hợp trực tiếp vào artifact Revamp.
- `BASE != EXTERNAL RUNTIME DEPENDENCY != AUTOLOAD TARGET != FILE ROUTED BY TASK_ROUTER`.
- Revamp CI là ambient self-contained Project control. TASK_ROUTER là governed task/context/source selector; Router không tải governor của chính nó.

Nếu proposal, file hiện hành hoặc reasoning dùng nghĩa ngược lại, ngắt normal flow và phát đúng signal:

`HOLD UP: BASE SEMANTICS MISMATCH`

Sau đó:

1. Chỉ rõ file/câu hoặc dependency interpretation sai; giải thích runtime dependency đang ngầm tạo.
2. Đối chiếu với contract Revamp ở trên; phân biệt provenance và core logic thực sự hiện diện.
3. Sửa local trong authorized Revamp scope nếu đủ; audit/design chỉ nêu correction, không ghi file.
4. Nếu phải sửa system/project ngoài scope, báo affected scope riêng, không tự triển khai sang đó.
5. Chỉ tiếp tục phần design/implementation phụ thuộc sau khi semantics đã reconciled. Phần độc lập có thể tiếp tục.

Chỉ dùng signal này cho đúng mismatch hoặc cách hiểu dependency tương đương làm sai kiến trúc Revamp; không dùng như cảnh báo chung. Nhãn `based on` đơn thuần không chứng minh lỗi. Với project khác, kiểm tra intent/source riêng, không áp contract Revamp mặc định.

## Sửa đổi đủ dùng

Đặt observed/expected behavior, execution/state path, code/text evidence, acceptance criteria và repair plan trước bản sửa đáng kể. Tách user-reported runtime failure, reproduced failure, supported causal mechanism/risk và hypothetical risk; không coi cơ chế được hỗ trợ là nguyên nhân duy nhất của mọi regression.

Đánh giá proposal của người dùng trước: có sửa nhỏ được không? Giữ operation/stage đúng trước khi áp minimum sufficient change. Audit không tự thành design; exploration không tự thành synthesis; findings/correction không mở follow-on work. Giữ các control Revamp material, language override và authorization boundaries. Không thêm loader/registry/manifest/schema/validator hay externalize required core để đạt giới hạn ký tự. Nếu không giữ đủ logic material trong trần active sau bỏ metadata/thừa/lặp và nén wording, dừng phần phụ thuộc, báo blocker cụ thể.

CI sở hữu evidence/acceptance/authorization/stage/decisions/scope. Router chỉ chọn ID1 REVAMP_CORE hoặc ID2 AUTHORING và context/source; AT_R sở hữu bounded authoring, không execution. Handoff chỉ nối continuity, không evidence/permission. Giữ repo/history/conditional CURRENT và Central Hub isolation hiện hành. Cập nhật CURRENT chỉ khi material change + continuity hữu ích + authorized write scope, theo HANDOFF_TEMPLATE.md; không ghi sau mọi task.

Dùng `ci-behavior-engineering` cho điều tra/thiết kế/kiểm thử hành vi chuyên sâu; skill này không thay thế nó. `project-git-workflow` sở hữu baseline/scope/staging/commit. Không tạo branch/worktree chỉ vì task mới. Khi promote successor, dùng `artifact-source-archive`, lưu predecessor byte-exact và sửa active references trong scope. Không archive nguồn Global dùng chung chỉ vì Revamp đổi lineage.

## Kiểm chứng và bàn giao

Kiểm tra trực tiếp: nếu chỉ dán CI vào Project Instructions, required core có hiện diện đủ không? Nếu không, quay lại mismatch gate. Bỏ metadata ngoài tên/version/status không được làm mất control; kiểm provenance ở repository docs.

Đối chiếu trách nhiệm core với nguồn thiết kế, giữ override Revamp có chủ đích. Chạy test hiện có thích hợp ở `Project CI/Revamp Project System/tests/`, kiểm Router parse/conservative format, paths, giới hạn ký tự, UTF-8/BOM/LF/whitespace/diff và hash archive. Không sửa kỳ vọng test để che regression. Test cấu trúc không chứng minh model chọn đúng thao tác hoặc đọc source.

Dùng ca thuận, ca chống và ablation có liên quan khi kiểm hành vi; giữ model/cấu hình/context tương đương, ghi input/output và phạm vi bằng chứng. Chưa chạy thì ghi NOT RUN; không gọi một review đặc tả là live test. Báo file sửa, semantics trước/sau, trách nhiệm giữ/tích hợp, kiểm tra thực chạy, live/UNKNOWN còn lại và local commit nếu có. Không push/deploy/cài CI/skill hay sửa project khác nếu chưa được yêu cầu riêng.
