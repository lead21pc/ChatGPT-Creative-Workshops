# ImageT subordinate — bảo toàn prompt

SPEC: REVIEWED_TEXT. LIVE: NOT RUN.

| Case | Input or state | Expected routing or prompt behavior |
| --- | --- | --- |
| No template | Manifest says `optional_absent`; no active template supplied | Skip template and process current prompt. |
| Missing active template | Manifest says `active`; template cannot be loaded | Stop and identify the missing template. |
| Conflicting inventory | Manifest says absent; active template appears | Stop for inconsistent release inventory. |
| Clear override | Template sets a blue coat; current prompt explicitly asks for a red coat | Use red coat; retain unrelated compatible template fields. |
| Ambiguous hard conflict | Template locks two arms; current prompt implies a different anatomy without clear override intent | Ask about anatomy before generation. |
| Negative without count | Current prompt says "not five fingers" | Keep that negative; do not infer exactly four fingers. |
| Nonhuman subject | Current prompt asks for a landscape | Do not apply body, clothing, beauty, or attraction criteria. |
| Local edit | Change only one object in an existing image | Preserve all other visible regions as far as the tool permits. |
| Hidden hard field | Required count is obscured in the output | Mark UNVERIFIABLE, not PASS. |

## Post-image verification regressions

| Case | Visible/runtime state | Expected verification behavior |
| --- | --- | --- |
| Open completion | An intentionally OPEN field receives a visible generator completion | Treat it as generator completion only; do not call it user-required and do not fail merely because it is present. |
| Open completion conflicts elsewhere | That OPEN completion visibly violates a separate applicable hard constraint | Fail only the independent violated constraint; the field does not become forbidden or a new default. |
| Visible output plus failure indicator | A visible image exists while the platform also reports generation failure or uncertain execution | Visible constraints may be checked from the image, but do not report clean execution success. |
| Result after completed call | A generation submission occurred and a later result is failed or uncertain | Prior approval remains consumed under Ready Gate; post-image verification does not restore it. |
| Retry after failed/uncertain result | The result is failed or uncertain | No silent retry; another call requires the normal fresh route/snapshot/approval path. |

Thêm: manifest/controller/router mismatch hoặc module thiếu/corrupt -> chặn phần ảnh, không archive fallback; preference có mặt/inactive -> không kích hoạt; ANALYZE chỉ phân tích; retry phải đọc lại nguồn và khóa hiện tại. Ready Gate v1.0 là dependency active/required cho mọi generation call, được manifest pin và router resolve; thiếu/unreadable/sai hash/version/compatibility phải dừng generation, không embedded fallback. Controller v1.1 chỉ delegation. Kiểm R01–R22 và X01 trong READY_GATE_TEST_CASES.md.

Kiểm local bằng python -B -m unittest discover -s tests -v từ root Central Hub; oracle chỉ mô phỏng inventory, không gọi model/tool. Khi thử live riêng, ghi input, sources thực nạp, prompt hiển thị, payload nếu quan sát được, ảnh và constraint thấy được.
