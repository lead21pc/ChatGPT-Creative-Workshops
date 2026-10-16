# Repository Context Gate

Before analyzing, planning, reviewing, or modifying this repository, read [SYSTEM_CONTEXT.md](./SYSTEM_CONTEXT.md) first.

Treat it as repository-level context for interpreting the authoring model, project boundaries, control architecture, evidence states, and the relationship between repository-visible state and live ChatGPT Project runtime.

It does **not** override:
- the user's explicit task instructions;
- more specific project-local control files;
- project-declared source authority;
- canon decisions made by the author.

After reading SYSTEM_CONTEXT.md, continue with the smallest relevant project-specific source set for the task. Do not generalize one paracosm's architecture to another.

## Kiểm tra trước khi thiết kế CI và Router

Trước khi tạo mới CI, Router hoặc thành phần anti-drift/kiểm soát dưới `llm-controls`, hoặc thiết kế lại đáng kể một thành phần hiện có trong phạm vi đó, phải đọc rationale thiết kế liên quan. Với dòng ChatGPT Project Global Native, tài liệu bắt buộc gồm [DESIGN_RATIONALE.md](<./llm-controls/global-instructions/ChatGPT Project Global Native/DESIGN_RATIONALE.md>). Trước triển khai, đối chiếu đề xuất với các quy tắc về chủ sở hữu trách nhiệm và mức sửa đổi đủ dùng trong rationale.

Rationale là tham chiếu thiết kế bắt buộc, không phải thẩm quyền bất biến; nó không ghi đè chỉ dẫn hiện tại của người dùng, kiến trúc mới hơn đã được chấp thuận, trạng thái repository thực tế hoặc các kiểm soát có ưu tiên cao hơn.
