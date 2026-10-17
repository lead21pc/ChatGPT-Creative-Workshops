# Ready Gate active — 22 ca đặc tả

Ready Gate thuộc IMAGE_CONTROLLER_v1.0.md; không thay Hub instructions. SPEC: REVIEWED_TEXT; LIVE: NOT RUN. Đây là baseline active theo xác nhận người dùng, không cần lựa chọn thử nghiệm.

| ID | Event or input | Required outcome |
| --- | --- | --- |
| R01 | Request reaches prompt gate with a required material field unresolved | Stop for the decision; no Ready Gate pass and no tool call. |
| R02 | Valid request, no reply after Ready Gate | Numbered PENDING_APPROVAL; all five user-visible categories and exact question; zero calls. |
| R03 | YES/CÓ/ĐỒNG Ý clearly approves the current version | APPROVED; freshness check; one call with unchanged displayed prompt and approved inputs; no second confirmation. |
| R04 | NO/KHÔNG without changes | PENDING_APPROVAL, still unapproved; ask what to change; zero calls. |
| R05 | "Có, nhưng đổi màu sang xanh lá." | REVISION_REQUIRED; never submit old version; preserve other constraints; new route/gate/version. |
| R06 | "Không, thực ra tôi muốn hai hình vuông." | New version changes only the authorized count; zero calls until new approval. |
| R07 | After R05, approve the new version | Submit exactly the new version once; old approval has no effect. |
| R08 | "Có lẽ", emoji, quoted YES or uncertain approval target | Clarify; no approval inferred; zero calls. |
| R09 | Request or tool-facing prompt/options/references changes after approval, before submit | STALE or REVISION_REQUIRED; reroute/gate/new version; old approval invalid. |
| R10 | New unrelated image request follows approval | Previous approval never authorizes it; new Ready Gate required. |
| R11 | Context no longer identifies exact pending prompt | STALE; reconstruct through route and prompt gate; new confirmation. |
| R12 | Effective source version changes or a required source cannot be read | No call; route/resolve again, new Ready Gate only after source requirements pass. |
| R13 | ANALYZE only | Analysis only; no Ready Gate or image generation. |
| R14 | EDIT/VARIATION/CORRECT | Gate before each call; preserve outside delta and non-open fields. Ready display cannot broaden operation. |
| R15 | Retry with changed prompt | Route/gate/new version; require new approval. |
| R16 | Submission already occurred; retry uses same prompt | Approval was consumed; require new version/approval for another call. |
| R17 | User asks what one sentence means without revising | Answer without tool call; same unchanged pending version remains identifiable. |
| R18 | User explicitly approves an older version while a newer one is pending | No call; clarify current version. |
| R19 | Submission result uncertain | Report uncertainty; no silent retry; any retry needs a new approval. |
| R20 | Gate-passed prompt is shown or approved | Compare composed, displayed and submitted prompt when observable; no Ready-stage rewrite or post-approval polish. |
| R21 | Preference absent throughout | Ready Gate still works; preference additions category says none; M2 is not a prerequisite. |
| R22 | Prompt says "not five fingers", exact count not set | No inference of four; baseline negative handling survives. |


Dùng CREATE một hình vuông xanh dương trên nền trắng, không chữ/đối tượng khác; EDIT/CORRECT chỉ đổi màu vật trái trong ảnh hai vật; VARIATION chỉ đổi màu; ANALYZE mô tả, không tạo. Ca độc lập dùng chat mới; ca stale/retry dùng nhiều lượt.

Ghi model/ngày/control hashes, request/attachments/options, prompt hiển thị, reply, state, call count và payload nếu quan sát được. Phê duyệt phải đúng version và chỉ một call. Không nhìn thấy payload thì UNVERIFIABLE; prompt hiển thị không chứng minh payload backend. Các nhánh chưa duyệt phải zero calls. Đặc tả này không cấp quyền tạo ảnh.
