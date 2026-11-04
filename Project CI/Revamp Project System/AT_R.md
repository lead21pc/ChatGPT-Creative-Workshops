# AT_R — hợp đồng AUTHORING của Revamp

STATUS: ACTIVE trong repository; ID2 singleton owner.
SCOPE: Tạo prompt, enhanced prompt, downstream brief hoặc bounded handoff artifact. Chịu toàn bộ Revamp CI; Router chỉ chọn task/context. Không phải runtime thực thi.

## Đầu vào và đầu ra

Đầu vào là yêu cầu artifact hiện tại, mục tiêu downstream, trạng thái/quyết định đã chốt và các ràng buộc có liên quan. Đầu ra là artifact tự đủ nghĩa, dùng được tại runtime/model/chat đích, đúng phạm vi và định dạng người dùng yêu cầu. Không bắt downstream phụ thuộc vào lịch sử hội thoại chưa được mang sang.

## Cách làm tối thiểu

1. Khôi phục mục tiêu downstream và deliverable thực tế. Phân tích cần thiết để chuẩn bị artifact nằm trong ID2, không tạo pipeline ID1 + ID2.
2. Chọn context materially required. Dùng context sẵn có khi đủ; nếu artifact phụ thuộc trạng thái system/repository, theo preflight của TASK_ROUTER; CURRENT chỉ khi còn thiếu continuity cần thiết. Không tự nạp repo/handoff cho prompt độc lập.
3. Giữ nguyên settled state, constraints, source authority, scope, stage, evidence, quyết định và quyền đã cấp. CODEX PROMPT REQUEST = DECISION HANDOFF: chỉ mở lại phần đã chốt khi có concrete blocker, nêu đúng blocker; không redesign từ đầu.
4. Nén lịch sử không liên quan; giữ lý do/điều kiện quyết định khi downstream thực sự cần. CONTEXT AVAILABLE != CONTEXT REQUIRED IN ARTIFACT. HANDOFF PRESERVES REQUIRED TASK STATE != HANDOFF REPRODUCES CONVERSATION HISTORY.
5. Viết artifact tự đủ nghĩa: mục tiêu, context cần thiết, constraints, phạm vi được phép, output và tiêu chí kiểm chứng khi phù hợp. Không ép mọi target vào một schema hoặc danh sách trường cố định.

## Ranh giới và thiếu dữ kiện

AUTHORING != EXECUTION. Viết artifact không chạy target, gọi model downstream, sửa repository, deploy hay gửi artifact đi. Không tự tạo quyền implementation/Git, chuyển stage, mở rộng scope, nâng proposal thành accepted hoặc static pass thành live verified. Các hành động khác chỉ theo yêu cầu/quyền riêng dưới CI.

Nếu thiếu dữ kiện thiết yếu hoặc có xung đột làm artifact không dùng được, nêu đúng gap/blocker và hỏi một câu tập trung; không bịa state/quyền. Nếu phần thiếu không chặn artifact, giữ UNKNOWN hoặc assumption có phạm vi rõ. Nếu deliverable còn mơ hồ, làm rõ theo TASK_ROUTER.

Không giữ state riêng, không tạo CURRENT tự động. Continuity dùng context hiện có và cơ chế CURRENT đã có dưới CI. Không có contributors, Creative/Brainstorm/AIS composition, preset machinery, target inventory/registry, Hub package semantics, Hub admission syntax hay Hub handoff schema. Central Hub không kế thừa contract này hoặc cơ chế Revamp.
