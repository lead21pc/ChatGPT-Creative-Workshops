---
name: central-hub-maintenance
description: Tra cứu, audit và bảo trì control, module, pipeline và candidate của Central Hub; kiểm tra trách nhiệm, phụ thuộc, promotion và bằng chứng kiểm chứng. Không dùng chỉ vì đang ở thư mục Hub, cho tác vụ thuần Git hoặc để thực hiện nghiên cứu/tạo ảnh thông thường qua AIS/ImageT.
---

# Bảo trì Central Hub

Skill hướng dẫn Codex đọc và bảo trì Central Hub. Kiến trúc và trạng thái hiện hành do nguồn Hub xác lập; skill không là runtime control, Router, Catalog hoặc bản sao cấu hình active. Không áp kiến trúc Hub cho FTH hay các paracosm khác.

## Xác định phạm vi và nguồn hiện hành

Mặc định tra cứu hẹp khi người dùng chỉ hỏi. Audit hoặc thiết kế chỉ đọc; chỉ sửa khi tác vụ cho phép triển khai. Xác định mục tiêu, phạm vi đọc/ghi và điều kiện hoàn tất; không biến phát hiện thành quyền tự sửa hoặc promotion.

Tìm repository chứa target từ working tree hiện tại. Vị trí đã biết là `C:/Users/Sheeplark/Desktop/CI Versioning Audit & Changelog/Central Hub`, chỉ dùng làm gợi ý khi không có target rõ. Không chuyển sang checkout khác để né trạng thái local; nếu không xác định được nguồn, báo thiếu và hỏi phần cần thiết.

Đọc `SYSTEM_CONTEXT.md` ở repository root và các `AGENTS.md` áp dụng trước khi phân tích. Bắt đầu từ `Central Hub/README.md`, lần theo tham chiếu tới bộ CI, Router, Architecture và root Package Catalog hiện hành. Chỉ đọc phần cần cho câu hỏi; khi audit hoặc sửa quan hệ giữa các tầng, đọc các định nghĩa liên quan trong bộ đó. Tiếp tục tới module, pipeline, manifest, candidate và tests được tham chiếu trực tiếp. Đọc rationale mà nguồn áp dụng yêu cầu trước khi thiết kế control liên quan.

Không chọn phiên bản theo tên file, số lớn nhất, ngày sửa hoặc sự hiện diện. Đối chiếu status, binding, tham chiếu và quyết định đã chấp nhận. Nếu nguồn hiện hành lệch nhau, chỉ rõ điểm lệch; không tự coi README, file mới hơn hay candidate là thẩm quyền thắng. Skill không giữ danh sách phiên bản active, package count, Library locator hoặc kết quả live riêng.

## Chọn chủ sở hữu trước khi sửa

Dùng các ranh giới sau để định hướng, rồi kiểm lại hợp đồng hiện hành trong nguồn:

- Hub CI giữ operation, stage, truth/state, quyền hành động, nhu cầu kiểm chứng và cách giải thích.
- Router chọn/composition package theo phạm vi và kiểm tra phụ thuộc/đọc nguồn; Catalog khai báo inventory và binding.
- Architecture giữ hợp đồng kỹ thuật dùng chung; module giữ hành vi chuyên biệt theo role và scope.
- Hub chọn entrypoint pipeline; AIS/ImageT giữ thủ tục và phụ thuộc nội bộ của mình. Đọc nội bộ khi cần bảo trì pipeline, không chuyển trách nhiệm đó lên Hub.
- Platform/tool thực hiện truy xuất và thao tác thực tế; chỉ dẫn mô tả hành vi không chứng minh công cụ đã chạy.

Đối chiếu đề xuất với hành vi đang có và failure/yêu cầu cụ thể. Ưu tiên sửa tại chủ sở hữu hiện có; chỉ thêm thành phần khi trách nhiệm cần thiết chưa biểu đạt được bằng cơ chế đang dùng. Không suy ra role từ prefix, quan hệ ngữ nghĩa từ thư mục, hoặc hard dependency từ một chỗ nhắc tên. Kiểm Refines/Complements/Requires theo khai báo thực, không tự biến refinement thành replacement, autoload hoặc thứ tự ưu tiên.

Với đề xuất từ Revamp hoặc chat khác, dùng `ACCEPT`, `ACCEPT WITH LOCAL CORRECTION` hoặc `RETURN FOR REPLAN` dựa trên nguồn thực tế. Nêu bằng chứng cho phần xung đột và phương án sửa đủ dùng; thiết kế lại ngoài phạm vi được duyệt vẫn cần người dùng quyết định.

## Thực hiện thay đổi được duyệt

Dùng `project-git-workflow` cho baseline repository, phân loại dirty state, phạm vi ghi, staging và commit đúng file task-owned. Giữ nguyên thay đổi ngoài phạm vi. Audit chỉ đọc không stage/commit. Quyền triển khai local không tự cho phép push, PR hoặc thao tác Project/Library.

Trước sửa, xác định thay đổi nằm ở core, package/module, pipeline hay candidate; lần theo các tham chiếu và bên sử dụng trực tiếp bị ảnh hưởng. Chỉ mở rộng đọc theo phụ thuộc cần thiết. Không sửa tất cả các tầng chỉ để chúng trông đồng bộ.

Giữ candidate ngoài active cho tới khi có quyết định promotion đúng phạm vi. Khi được duyệt promotion/migration, kiểm bản được chọn, identity/role/version, binding, phụ thuộc, tham chiếu và các giả định tests/docs chịu tác động. Không tự tạo Registry, Catalog cục bộ, manifest hoặc Router mới nếu cơ chế hiện có đủ dùng. Không suy từ commit hoặc Catalog membership ra runtime activation.

Nếu tạo successor thay thế artifact cũ, dùng `artifact-source-archive` cho cơ chế archive và kiểm byte-exact predecessor trước khi báo hoàn tất. Candidate song song hoặc sửa tại chỗ không tự cần archive. Không đọc archive để làm nguồn active/fallback; chỉ đọc lịch sử khi người dùng yêu cầu cụ thể. Cài hoặc cập nhật Project/Library là hành động riêng, cần được cho phép trong tác vụ; không báo đã triển khai chỉ từ thay đổi repository.

Runtime control/config dùng ngôn ngữ do hợp đồng Hub hiện hành quy định; không áp quy tắc đó lên ghi chú dành cho người đọc, trích dẫn hoặc nội dung người dùng. Trả lời người dùng bằng tiếng Việt theo chỉ dẫn áp dụng.

## Kiểm chứng và báo cáo

Chọn kiểm tra từ nội dung thay đổi: parse YAML/metadata khi sửa cấu hình, kiểm tham chiếu/binding/hash khi chúng chịu tác động, và các ca hợp đồng/hồi quy liên quan trong `Central Hub/tests/` hoặc tests do pipeline sở hữu. Khi thay đổi hợp đồng dùng chung, chạy bộ hồi quy Hub có liên quan rộng hơn. Không tạo tests chỉ khớp câu chữ của skill; không chạy kiểm tra toàn repository cho một tra cứu hẹp.

Đọc lại đầu ra thực tế và diff; kiểm cả điều được đổi và ràng buộc cần giữ. Với artifact văn bản, kiểm UTF-8, BOM, line endings, whitespace và `git diff --check` trong phạm vi ghi; giữ quy tắc byte-exact nơi có yêu cầu. Sửa fixture hoặc kỳ vọng chỉ khi hợp đồng mới đã được duyệt, không để che failure.

Tách bằng chứng repository/static, mô phỏng/fixture, UI quan sát, người dùng báo cáo và live được tái hiện. `SEARCH HIT != FULL READ`, `SELECTED != EXECUTED`, `STATIC PASS != LIVE PASS`, `REPOSITORY ACTIVE != PROJECT DEPLOYED`. Khi thiếu bằng chứng quyết định, giữ UNKNOWN và chặn phần phụ thuộc cần nó; tiếp tục phần độc lập có đủ căn cứ.

Báo ngắn gọn thay đổi/kết luận, nguồn hoặc file liên quan, kiểm chứng đã thực hiện và phần chưa kiểm chứng. Nếu chưa thể xác minh runtime, nêu thao tác tái hiện và kết quả cần quan sát phù hợp với thay đổi; không tự chạy live test ngoài quyền tác vụ. Tách local commit khỏi push và khỏi cài đặt runtime.
