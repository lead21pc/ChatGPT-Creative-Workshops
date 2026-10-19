# Central Hub v1.1 — CREATIVE và BRAINSTORM Library singleton

Repository v1.1: ACTIVE. Project deployment: NOT_VERIFIED trong mốc local này. Không upload tự động, không stage/commit/push. Bộ promotion đã chấp nhận được sao chép vào root; chỉ cập nhật trạng thái repository, đường dẫn evidence record và mô tả số binding. Catalog chuyển hai singleton sang Library; thuật toán Router giữ nguyên.

TECHNICAL Library, AIS và ImageT giữ nguyên bindings. Trial trước có LIVE INTEGRATION PARTIAL theo báo cáo người dùng: các success path PASS, I08 UNVERIFIABLE. Không chạy lại I01–I10, không tạo failure injection. CREATIVE/BRAINSTORM Library hiện NOT_PERFORMED; kết quả legacy không là bằng chứng migration đã live.

## Hai file cần upload

Upload nguyên hai file sau vào **Library / Central Hub Config**, giữ filename:

- `library_modules/HUB-DOM-CREATIVE_v1.0.md`: HUB-DOM-CREATIVE / HUB-PKG-CREATIVE / DOMAIN_CONTROL / ACTIVE / 1.0.
- `library_modules/HUB-CAP-BRAINSTORM_v1.0.md`: HUB-CAP-BRAINSTORM / HUB-PKG-BRAINSTORM / CAPABILITY / ACTIVE / 1.0.

Đây là bản có header runtime, không phải source legacy cùng tên ngắn. Không upload lại TECHNICAL, không dùng trial wrapper. Phần thân của từng module giữ byte-exact sau H1 của source cũ. Không thêm Refines/Complements/Requires hoặc package-local Catalog.

## Thứ tự cài đặt thủ công

1. Lưu Project Instructions và source roster hiện đang dùng để rollback. Upload hai file trên vào đúng `Central Hub Config`; chưa coi upload là identity verification hoặc scoped application.
2. Resolve trong đúng root và đọc **FULL_FILE** từng object: đối chiếu Module ID, Package ID, Runtime role, Scope, Status ACTIVE, artifact Version 1.0 và đúng body. Không chấp nhận snippet/header-only hoặc identity mơ hồ. Ghi nhận `library_file_id` và Library `version_id` thực tế; không suy Library version_id từ artifact Version.
3. Trong `HUB_PACKAGE_CATALOG_v1.0.yaml` ở root, cập nhật riêng `location` của hai entry bằng identity đã quan sát: `library_file_id`, `library_version_id`, locator thật được root-bound nếu runtime cần; chuyển `resolution` từ UNRESOLVED thành RESOLVED và `verification` từ NOT_PERFORMED sang trạng thái đúng bằng chứng full-read vừa có. Không claim smoke PASS trước khi chạy. Null hiện tại là unresolved, không phải quyền search rộng hoặc dùng repository/source cũ. Nếu chưa xác lập exact identity thì dừng cài phần migration, giữ deployment đang dùng; không dùng Catalog chưa resolve để giả rằng package đã sẵn sàng.
4. **PROJECT INSTRUCTIONS:** toàn bộ nội dung root `HUB_CI_v1.1.md`.
5. **PROJECT SOURCES:** root `HUB_ROUTER_v1.1.yaml`, `HUB_ARCHITECTURE_v1.0.md`, `HUB_PACKAGE_CATALOG_v1.0.yaml` đã ghi nhận hai exact bindings. Thay core candidate/trial tương ứng, không để nhiều bộ core cùng làm authority. Giữ chính xác các nguồn pipeline sau:

   - `tool_pipelines/AIS/AIS_PIPELINE_v1.0.md`
   - `tool_pipelines/AIS/AIS_ROUTER_v1.1.yaml`
   - `tool_pipelines/ImageT/IMAGE_CONTROLLER_v1.1.md`
   - `tool_pipelines/ImageT/IMAGE_SOURCE_ROUTER.yaml`
   - `tool_pipelines/ImageT/manifest.yaml`
   - `tool_pipelines/ImageT/READY_GATE_v1.0.md`
   - `tool_pipelines/ImageT/IMAGE_ANTI_PRIOR.md`
   - `tool_pipelines/ImageT/config.md`

   Giữ tên source và nội dung hiện hành; pipeline tự resolve dependency. Không đổi preference inactive/direct-input-only.
6. **LIBRARY:** giữ nguyên TECHNICAL ACTIVE/1.0, `library_file_id=libfile_bab7d55cd85c819198291acf135099fd`, Library version_id `1`; thêm hai object mới đã xác minh ở bước 2. Đây là ba singleton, mỗi package direct entrypoint.
7. Sau khi hai Library artifact đã FULL_FILE/identity verified, khi chuyển sang Catalog mới, **gỡ khỏi live Project Sources** `CREATIVE_v1.0.md` và `BRAINSTORM_v1.0.md`. Không để chúng làm fallback/authority song song. TECHNICAL source cũ tiếp tục không thuộc bộ v1.1. Không xóa repository copies hoặc gỡ nguồn không liên quan.
8. Chạy bốn smoke case dưới đây sau khi exact delegation và bindings đã cài. Không upload tài liệu này, tests, candidate snapshots hoặc result records như runtime controls.

## S01–S04 — chỉ chuẩn bị, NOT_RUN

| Case | Prompt | Kết quả cần quan sát |
| --- | --- | --- |
| S01 — BASELINE | Viết lại câu này thân thiện hơn: “Vui lòng gửi tài liệu trước 5 giờ chiều.” | Package set NONE; không specialization/pipeline không cần thiết. |
| S02 — CREATIVE | Viết cảnh ngắn hai người bạn gặp lại ở ga tàu, dùng hành động và nhịp câu để thể hiện khoảng cách giữa họ; chi tiết phải có chức năng, không giải thích trực tiếp cảm xúc. | HUB-PKG-CREATIVE / HUB-DOM-CREATIVE tự được chọn; exact Library module ACTIVE/1.0 trong Central Hub Config, FULL_FILE và đúng identity/header; không Project Source fallback. |
| S03 — BRAINSTORM | Với ý tưởng thành phố tồn tại nhờ giữ bí mật, đảo giả định thành bắt buộc công khai; phát triển ba nhánh khác cơ chế, mỗi nhánh có hệ quả bậc hai. | HUB-PKG-BRAINSTORM / HUB-CAP-BRAINSTORM tự được chọn; exact Library ACTIVE/1.0, FULL_FILE và đúng identity/header; không Project Source fallback. |
| S04 — CREATIVE + BRAINSTORM | Từ tiền đề thành phố vận hành bằng bí mật, phát triển ba nhánh song song bằng cách đảo hoặc nới giả định. Với mỗi nhánh, viết một cảnh ngắn có hành động, nhịp và chi tiết chức năng để cho thấy hệ quả bậc hai. Chưa chọn nhánh cuối. | Cả CREATIVE và BRAINSTORM từ Library, đọc đầy đủ đúng hai bound objects; đóng góp có scope, không winner-take-all. Không tự gọi AIS/ImageT. |

Ghi bằng chứng quan sát: CI/Router/Catalog thực dùng, package/module chọn, exact object/root, artifact Version so với Library version_id, FULL_FILE/has_more, header, binding location, hành vi trả lời và fallback attempt. Ghi PASS/FAIL/UNVERIFIABLE theo bằng chứng; route tự khai không đủ chứng minh read. Không yêu cầu hidden reasoning. Không thử controlled Library failure.

## Rollback có chủ đích

Nếu chưa chuyển deployment thì giữ nguyên bộ đang chạy. Nếu đã chuyển và cần quay về, khôi phục source roster/Instructions đã lưu. Để quay về đầy đủ v1.0: khôi phục root `HUB_CI_v1.0.md`, `HUB_ROUTER_v1.0.yaml`, các source `TECHNICAL_v1.0.md`, `CREATIVE_v1.0.md`, `BRAINSTORM_v1.0.md`; gỡ core v1.1 khỏi deployment; giữ AIS/ImageT hiện hành và Library objects nguyên trạng nhưng không được v1.0 chọn. ROLLBACK != FALLBACK. Không đổi Catalog sang legacy tự động khi Library lỗi.

Nguồn rollback v1.0/legacy hiện nằm byte-exact dưới `Source_archive/Central Hub legacy v1.0/`, giữ cấu trúc đường dẫn cũ bên trong. Khi người dùng chủ động rollback, lấy đúng file từ đó; không có đọc archive trong runtime. Receipt: `Source_archive/HUB_LEGACY_ARCHIVE_RECEIPT_2026-10-19.json`. Các đường dẫn source cũ nêu trong phần rollback là vị trí tương đối bên trong nhóm archive này.
