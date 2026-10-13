# 03 — Kiến trúc đích tối thiểu để thử nghiệm

> Chỉ là proposal. Mọi block Markdown dưới đây minh họa cú pháp để đánh giá, không phải nội dung canon hay bản thay thế CI/Router.

## Runtime-required sau khi được duyệt và kích hoạt riêng

1. **CI trong Project instructions** vẫn giữ toàn bộ invariant và source gate. Chỉ contract về “read” được mở rộng có điều kiện: `FULL_FILE` mặc định; `NODE_OR_FULL` chỉ được coi là read khi header, local index, node đích và closure `REQUIRES` đều thật sự truy xuất được và hợp lệ. Không thể bỏ CI instruction hoặc chuyển gate sang metadata.
2. **Router Markdown** tách route selection khỏi execution như hiện tại. Mỗi file có mode `FULL_FILE`, `NODE_OR_FULL`, hoặc về sau `RECORD_OR_FULL`. Không có mode thì `FULL_FILE`. Router đọc `00` và `92` full, chọn current domain, kiểm status/conflict, chọn overlay đầy đủ, rồi execution. Nó không chọn CI file cho live Project; CI đã ở instruction setting.
3. **Current-domain file** vẫn là một Markdown Project-native source. Với file pilot, thêm một vùng đầu gồm mandatory runtime context và local routing index, rồi đặt routing marker ở đầu mỗi nhóm semantic đã review. Nội dung canon ở các nhóm giữ nguyên trong thử nghiệm shadow; marker/index là lớp điều hướng, không cấp authority mới.
4. **Fallback có thứ tự:** node selector/closure hợp lệ và runtime thực sự đọc được → dùng node; bất cứ nghi ngờ nào về mapping, qualifier, status hoặc retrieval → đọc full current file; file quyết định thiếu/không đọc được → `SOURCE_LOAD_BLOCKED`. `SOURCE_LOAD_PARTIAL` vẫn chỉ dành cho gap thứ cấp không đổi được kết luận giới hạn.

```markdown
# 80_STABLE_AVIATION_RF_AIRSPACE_CURRENT.md

> Runtime role: CURRENT CANON
> Domain/owner: aviation và RF airspace trong phạm vi file này
> Boundary: sovereignty ≠ ATC ≠ aviation economy
> Load mode: NODE_OR_FULL   <!-- chỉ sau activation riêng -->

## LOCAL ROUTING INDEX
| Node ID | Scope | REQUIRES | Issue/record hook |
| --- | --- | --- | --- |
| AFN-80-... | ... | ... | AF-AV-... / 91 record nếu thật sự quyết định |

## Existing section
> Routing ID: AFN-80-...
...existing content...
```

**Mandatory header** phải chứa role/owner, current-versus-history boundary, priority/supersession có tác động toàn file, cross-domain owner và load-mode contract. Nó không phải bản sao thu nhỏ của toàn file. Trong `10`, global “latest priority” kéo dài khoảng dòng 19–279; trong `30`, cập nhật visual ở khoảng dòng 2206, 3046 và 3719. Nếu không thể gói đúng và được duyệt bằng một header ngắn, file đó giữ `FULL_FILE`. Header/index chính nó cũng cần được truy xuất thực tế, không chỉ được model đoán qua tên file.

**Semantic node** là một nhóm mệnh đề đủ dùng cho một lớp câu hỏi; không phải mỗi heading một node. Node ID ổn định qua build nếu ý nghĩa không đổi; khi boundary/meaning đổi, reviewer phải sửa ID/index và các hook. Không tự cắt tại heading nếu exception nằm nơi khác. `REQUIRES` chỉ ghi khi thiếu target làm premise của conclusion không đủ; có thể trỏ node cùng file hoặc file khác, nhưng cross-file edge cần review chủ sở hữu và trạng thái. Nếu không chắc, dùng `REVIEW_REQUIRED` trong quy trình review, không phát hành edge giả; runtime dùng full file.

## Local-tooling-only

- Parser/validator chạy trên shadow copy/fixture để kiểm ID, span, index, dangling `REQUIRES`, duplicate, stale content mapping và file fallback. Không được là dependency của Project runtime.
- Bảng coverage, content hashes, source generation ID và diff giữa full-file/node closure phục vụ kiểm thử; không phải source authority.
- Builder hiện tạo `00–92` bằng ghi trực tiếp trong `build_consolidation.ps1` (ví dụ các write ở khoảng dòng 393, 716–1570). Nếu có activation, thay đổi lâu bền phải đi qua nguồn sinh/template hoặc bước build được chứng minh giữ marker/index; sửa tay generated file sẽ mất ở rebuild. Đây là ràng buộc bền vững của Track A với builder, **không** bắt phase 1 giải toàn bộ atomic publication của Track B.

## Future / deferred

- `90` history clusters, `91` record-mode, anti-drift node mode và reverse-impact/mutation graph chờ phép thử riêng.
- Runtime JSON/YAML registry, global node database, service và giao thức retrieval mới không có trong kiến trúc tối thiểu.
- Builder/package atomicity, resolver chọn `DRAFT`, manifest integrity là Track B/C độc lập; chỉ được nối vào activation nếu phát hiện dependency trực tiếp tới tính bền của index hoặc source generation.

## Quy tắc đọc tối thiểu

```text
User yêu cầu full audit hoặc mutation rộng                         → FULL_FILE
Index/header/node/REQUIRES không resolve hay chưa semantic review  → FULL_FILE
Authority conflict, qualifier ngoài closure, task lan rộng        → FULL_FILE
Project retrieval không chứng minh được node đủ                    → FULL_FILE
Full current file không sẵn hoặc không đọc được                    → SOURCE_LOAD_BLOCKED
```

Lựa chọn “đọc ít” chỉ xảy ra sau khi tất cả gate trên đều qua. Không có trạng thái “node lỗi nhưng vẫn suy bằng excerpt”.
