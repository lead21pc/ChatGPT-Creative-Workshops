# FTH Control Pack 0.1.0

Control stack có thể thích nghi, trích từ Project Feather Core (FTH), dành cho project dài hạn gặp source-authority drift, tự lấp UNKNOWN, nâng proposal thành state, trộn module/domain hoặc authoring vượt điểm dừng. CI ở đây là Custom Instructions.

Pack không chứa lore/canon/world-state FTH, không là world template, engine bắt tổ chức thế giới giống FTH hoặc phần mềm tự thực thi. Project nhỏ chưa gặp các failure này thường chưa cần cả stack. Người chỉ muốn học nguyên tắc có thể đọc README mà không cài.

## Fork/Copy what?

| Nhu cầu | File cần lấy |
| --- | --- |
| Chỉ đọc nguyên tắc | README này |
| Giữ thao tác và source gate | [CI](controls/project-instructions.md) + [Router](controls/source-router.yaml), cấu hình nguồn của bạn |
| Seed/primitives/comparison/localization có điểm dừng | Thêm [Pipeline](controls/authoring-pipeline.md); đây là cấu hình khuyến nghị để dùng đầy đủ các thao tác công bố |
| Quan hệ/module/agency | Thêm [MCA tùy chọn](optional/modular-concept-architecture_v1.0.md) khi thật sự cần |
| Chỉ thử/đánh giá | [Các tình huống hồi quy](tests/SCENARIOS.md), không cài chúng như control |

CI yêu cầu Pipeline cho matching transformation. Nếu chỉ copy CI + Router, thiếu Pipeline chặn riêng biến đổi phụ thuộc; không tuyên bố cấu hình đó có đầy đủ authoring. Router mẫu khai MCA: có thể giữ file để chỉ nạp khi đúng scope, hoặc bỏ entry khi chủ động không nhận capability này. Để entry mà thiếu file phải chặn phần MCA-dependent. Các overlay chuyên biệt khác không được đóng gói hoặc được baseline/MCA thay thế tương đương.

## Quick Start

1. Lưu bộ chỉ dẫn/binding đang dùng để rollback. Chọn CI và output language; CI tự chứa logic, không yêu cầu Global CI cũ.
2. Thay các placeholder dưới đây trong bản copy; chọn exact Router/Pipeline paths theo tên/vị trí thật bạn sẽ cài. Không sửa control FTH nguồn.
3. Khai discovery/index, current unresolved-state, reconciliation và source ownership theo cơ chế bạn đã dùng. Vai trò có thể cùng một tài liệu, phân tán ở owner hoặc qua cơ chế review có nội dung truy xuất được. Không bắt tên, numbering hay file riêng tương đương 00/92/91. Chưa có cơ chế phù hợp thì khai gap và chặn tác vụ phụ thuộc; không giả tạo empty accepted source.
4. Chỉ thêm control cần thiết. Cài CI vào instruction context; cung cấp Router/Pipeline và optional control ở vị trí đã khai. Các file là chỉ dẫn cho model, không tự truy xuất hoặc thực thi YAML.
5. Kiểm placeholder, YAML và thử các ca hồi quy trước khi dùng. Xác minh source ownership/admission, nội dung thực đọc và scope; copy/upload không chứng minh những điều đó.
6. Thử workload thật trong project nhận, ghi revision/model/surface, actual reads và kết quả. So fresh chat với chat dài; không dùng PASS của hệ nguồn thay cho test này.

## Bắt buộc tùy chỉnh

Các token `{{NAME}}` chỉ là chỗ thay văn bản, không phải schema hoặc biến được runtime tự nội suy. Thay tất cả trước khi cài; giữ quoting YAML hợp lệ nếu giá trị có dấu hai chấm, dấu nháy hoặc ký tự đặc biệt và parse lại sau khi sửa; đường dẫn control trong CI phải khớp file thật, các paths/bindings khác phải khớp deployment của bạn.

| Placeholder | Phải khai gì |
| --- | --- |
| `{{PROJECT_NAME}}` | Tên project, không phải tên quốc gia/module mặc định |
| `{{OUTPUT_LANGUAGE}}` | Ngôn ngữ/phong cách trả lời của bạn |
| `{{SOURCE_ROUTER_PATH}}` | Vị trí/tên exact Router đã cấu hình |
| `{{AUTHORING_PIPELINE_PATH}}` | Vị trí/tên exact Pipeline đã cấu hình |
| `{{PROJECT_INSTRUCTIONS_PATH}}` | Bản CI tương thích; maintenance reference, không CI discovery runtime |
| `{{DISCOVERY_BINDING}}` | Owner/path/mechanism cho discovery/index khi applicable |
| `{{OPEN_STATE_BINDING}}` | Owner/path/mechanism cho current unresolved state khi applicable |
| `{{RECONCILIATION_BINDING}}` | Owner/path/mechanism xử lý conflict, supersession/replacement, provenance, priority/authority khi quyết định task |
| `{{SOURCE_OWNERSHIP}}` | Nguồn/owner nào có thẩm quyền trong scope nào và cách xác lập admission; metadata không tự cấp quyền |
| `{{SOURCE_STORAGE_BINDING}}` | Nơi truy xuất và thứ tự nguồn được chấp nhận, nếu có; không tự suy fallback |
| `{{OPTIONAL_CONTROL_DIRECTORY}}` | Thư mục control trực tiếp, ví dụ vị trí bản copy của optional/ |

PRESERVE RECONCILIATION ROLE != REQUIRE FTH FILE STRUCTURE.

Reconciliation không phải quyền model tự hòa giải: phải giữ quyết định/phạm vi thay thế, provenance và xung đột chưa giải quyết. Đọc controlling content đầy đủ khi material. Binding được điền không chứng minh source admission hoặc FULL_FILE. Thiếu căn cứ quyết định chặn phần phụ thuộc; tác vụ độc lập vẫn tiếp tục. Discovery không cần catalogue mới nếu nguồn hiện có đủ; không bịa Module ID cho nguồn legacy.

Thuật ngữ canon/state có thể đổi cho project nhận nếu giữ rõ ai được chấp nhận điều gì, scope nào; proposal, inference, hypothetical, UNKNOWN, DEFERRED và CONFLICTED không tự chuyển trạng thái. `A != B` chặn suy diễn tự động, không cấm quan hệ đã có bằng chứng. NODE_OR_FULL chỉ dùng với reviewed closure truy xuất được; mặc định FULL_FILE.

## Cách kiểm tra

Trong thư mục bản copy đã cấu hình, chạy lệnh này. Nó báo file còn token và trả exit code khác 0; đây chỉ là phép dò token, không xác minh semantics/binding:

```powershell
python -c "from pathlib import Path; import re,sys; paths=[*Path('controls').rglob('*'),*Path('optional').rglob('*')]; bad=[str(p) for p in paths if p.is_file() and re.search(r'\{\{[A-Z_]+\}\}',p.read_text(encoding='utf-8'))]; print('Unresolved placeholders:',bad); sys.exit(bool(bad))"
```

Parse YAML bằng PyYAML nếu có sẵn; sau đó dùng [SCENARIOS](tests/SCENARIOS.md) để kiểm behavior, không so exact wording. Bộ kiểm tự động của repository nguồn được mô tả ở PACKAGING.md; archive độc lập không cần bộ đó để đọc/copy hoặc thử thủ công. Giữ proposal khác canon; không để regression test tự phê duyệt world-state.

## Rollback

Gỡ chỉ dẫn/binding đã thêm và chủ động khôi phục bộ CI/Router/nguồn tương thích đã lưu. Không sửa hoặc xóa dữ liệu thế giới. Thiếu nguồn lúc chạy không tự kích hoạt rollback/history fallback. Dừng workload phụ thuộc cho tới khi xác minh lại bộ cũ.

## Xuất xứ, giới hạn và license

Trích từ repository `lead21pc/chatgpt-ci-worldbuilding`, source revision `7dd8ce9ceae77b09b6e20f0c686f41f9b1945807`: CI 3.4, Router 5.0, Pipeline 1.1, MCA 1.2. Đây là projection riêng, không runtime migration. MCA giữ reasoning body; chỉ đổi hook/peer references và metadata. Không kèm Economy, Total War, Undie, RP, lore/canon sources, characters, chronology, reconciliation contents hay archive.

Xem [release notes](RELEASE_NOTES.md) để biết hashes và evidence. SOURCE-DERIVED, STATICALLY VERIFIED, REGRESSION VERIFIED, PACKAGING VERIFIED và LIVE VERIFIED là các lớp riêng. Các ca văn bản chưa chạy model không phải behavioral PASS. Không có live portability trên project khác được xác nhận; EXTRACTED SUCCESSFULLY != LIVE VERIFIED ON ANOTHER PROJECT.

Pack thuộc [MIT License](LICENSE); giữ copyright/license khi phân phối bản sao. Đây là tài nguyên độc lập, không là sản phẩm OpenAI chính thức hoặc bảo đảm model tuân thủ.
