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


Thêm: manifest/controller/router mismatch hoặc module thiếu/corrupt -> chặn phần ảnh, không archive fallback; preference có mặt/inactive -> không kích hoạt; ANALYZE chỉ phân tích; retry phải đọc lại nguồn và khóa hiện tại. Ready Gate active cho mọi generation call, kiểm trong READY_GATE_TEST_CASES.md.

Kiểm local bằng python -B -m unittest discover -s tests -v từ root Central Hub; oracle chỉ mô phỏng inventory, không gọi model/tool. Khi thử live riêng, ghi input, sources thực nạp, prompt hiển thị, payload nếu quan sát được, ảnh và constraint thấy được.
