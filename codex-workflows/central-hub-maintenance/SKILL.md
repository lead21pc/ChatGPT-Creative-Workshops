---
name: central-hub-maintenance
description: Tra cứu, audit và bảo trì control, module và pipeline Central Hub. Dùng cho thay đổi hợp đồng, phụ thuộc hoặc bằng chứng Hub. Không dùng cho tác vụ thuần Git hoặc sử dụng AIS/ImageT thông thường.
---

# Bảo trì Central Hub

## Nguồn, phạm vi và chủ sở hữu

Đọc SYSTEM_CONTEXT.md và AGENTS.md áp dụng. Từ Central Hub/README.md, lần theo binding hiện hành tới CI, Router, Architecture, Catalog và các phụ thuộc trực tiếp. Đối chiếu identity, role, status, version và body, không đoán theo tên file hay bản mới nhất. Đọc rationale được yêu cầu khi thiết kế control.

Hub CI giữ thao tác, giai đoạn, quyền, trạng thái và chuẩn kết luận. Router giữ lựa chọn theo scope, composition, closure, phân giải và lỗi đọc dùng chung. Catalog khai báo admission/binding. Architecture giữ hợp đồng kỹ thuật. Module giữ quyết định domain và trạng thái cục bộ, pipeline giữ thủ tục thực thi. Platform thực hiện truy xuất và gọi công cụ.

## ACTIVE-FIRST và NO CANDIDATE

Audit, thiết kế và proposal chỉ đọc. Đối chiếu đề xuất với working tree và phạm vi được giao. Với đề xuất từ Revamp hoặc nơi khác, dùng ACCEPT, ACCEPT WITH LOCAL CORRECTION hoặc RETURN FOR REPLAN. Giữ ngữ nghĩa và tiêu chí kiểm phù hợp, bỏ vòng tạo candidate và promotion của đề xuất. Quyền triển khai vẫn phải được cấp.

Khi đã được phép, sửa trực tiếp owner active, đồng bộ binding và tham chiếu chịu tác động, kiểm chứng rồi commit đúng phạm vi với project-git-workflow. Không yêu cầu phê duyệt promotion lần hai. Giữ một binding được chấp nhận, exact identity và kiểm phụ thuộc. Cài Project/Library và push cần quyền riêng.

Dùng Git làm lịch sử và rollback mặc định. Chỉ dùng archive riêng khi được yêu cầu, có dependency cụ thể, hoặc Git và bộ binding tương thích không đủ để khôi phục. Các archive hiện có là nguồn lịch sử, không dùng làm runtime fallback.

## Hợp đồng hiện hành

Control active chỉ chứa ngữ nghĩa và metadata cần để chọn, xác minh hoặc thực hiện hợp đồng hiện hành. Thay điều khoản đã lỗi thời tại owner. Ghi quan sát vào Central Hub/RUNTIME_EVIDENCE_CHANGELOG.md. Dùng tài liệu thiết kế/cài đặt hiện có khi cần giữ rationale hay hướng dẫn migration. README dẫn đến nguồn active. Git giữ diff và predecessor.

## Bằng chứng theo hành vi

Tra changelog trước khi kết luận một hành vi chưa được xác minh. Ghi hành vi, điều kiện, môi trường, kết quả, provenance và revision nếu biết. Phân biệt USER_CONFIRMED_LIVE_PASS, CODEX_REPRODUCED_LIVE, UI_OBSERVATION, kiểm tĩnh, fixture/mô phỏng và tài liệu nhà cung cấp. PASS người dùng xác nhận trực tiếp có giá trị trong môi trường và phạm vi đã thử.

Xét lại phần PASS bị tác động bởi thay đổi có thể đổi kết quả hoặc bằng chứng mới trái với kết quả trong cùng điều kiện. Giữ các PASS độc lập và bản ghi gốc. Kiểm riêng việc cài hoặc đọc exact object/body khi mệnh đề cần nó. Không yêu cầu xác nhận lại chỉ vì đổi version. Bằng chứng cũ không thay một lần tái hiện hiện tại đã được yêu cầu.

Tài liệu im lặng, thiếu hoặc chậm cập nhật không hạ quan sát live. Chỉ ghi mâu thuẫn nếu tài liệu khẳng định trái với quan sát trong cùng phạm vi. Giữ cả hai nguồn và giới hạn kết luận theo môi trường đã quan sát. Ghi một entry khi có bằng chứng mới và quyền ghi, cập nhật tóm tắt khi kết luận hiện hành đổi. Audit chỉ đề xuất delta khi có căn cứ mới.

## Hồi quy hiện hành theo phạm vi ảnh hưởng

Giữ kiểm hợp đồng hiện hành và lỗi còn tái diễn. Gộp ca trùng sau khi giữ đủ ca biên. Chuyển ca và helper còn dùng tới suite của owner trước khi bỏ test khóa candidate, promotion, revision hay migration đã hết nhiệm vụ. Kiểm imports trước khi bỏ file. Dùng Git cho test đã retire.

Domain-only chạy test owner. Đổi interface thêm consumer trực tiếp. Đổi hợp đồng chung chạy shared và consumer chịu ảnh hưởng. Full Hub suite dành cho thay đổi ngữ nghĩa CI, thuật toán routing/composition, mô hình admission, phân giải dùng rộng, context/state chung, topology lớn, dọn test nhiều owner hoặc yêu cầu rõ. Dọn lịch sử hay định dạng dùng kiểm tương xứng.

Kiểm parse, identity, binding, closure, hash và tham chiếu theo ảnh hưởng. Đọc diff, kiểm định dạng và báo giới hạn bằng chứng. Giữ quyền thao tác, ngôn ngữ runtime và quy tắc Git của tác vụ.
