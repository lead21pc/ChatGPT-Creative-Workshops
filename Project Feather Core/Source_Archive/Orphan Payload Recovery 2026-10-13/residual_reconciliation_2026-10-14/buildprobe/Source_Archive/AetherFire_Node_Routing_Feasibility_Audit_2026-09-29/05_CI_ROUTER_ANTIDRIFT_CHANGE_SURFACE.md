# 05 — Bề mặt thay đổi CI, Router và anti-drift

> Bản chỉ dẫn cho **yêu cầu triển khai riêng trong tương lai**. Không sửa các file được nêu trong lượt audit này. Các số dòng chỉ đúng với snapshot local tại HEAD/audit date; cần diff lại bản Project đã cài trước activation.

## CI trong Project instructions

`AetherFire CI/AetherFire_CI_version_v2.6.md` là bản tham chiếu local, không phải nơi live Project tự lấy CI. Khi chuẩn bị activation, phải xem/copy bản instruction setting thực tế và đối chiếu byte/ngữ nghĩa.

| Vị trí tham chiếu | Contract hiện hành | Thay đổi tối thiểu cần đề xuất |
| --- | --- | --- |
| Dòng 29–31, Canon Source Gate | Đọc Router trước; `PROMPT_ROUTE_ONLY` chỉ xác định scope/source | Giữ nguyên thứ tự và lệnh không kết luận khi route. Không chuyển các invariant này sang file metadata. |
| Dòng 33 | Router sở hữu source authority/load order/truth status; excerpt/hit/summary không phải read | Giữ phần authority; mở một ngoại lệ **rất hẹp** cho reviewed `NODE_OR_FULL` closure được đọc thật theo contract Router. Excerpt rời, search hit và backend summary vẫn không phải read. Nếu không xác minh được closure, full-file hoặc blocked. |
| Dòng 1–28 và các invariant còn lại | Ngôn ngữ, discourse, provisionality, không suy canon | Không có nhu cầu sửa cho node routing. |

Không thể chỉ đổi Router: CI dòng 33 hiện phủ định trực tiếp việc coi một node excerpt là đọc đủ. Mọi thay đổi CI phải được cài lại vào Project instructions bằng yêu cầu riêng; sửa bản `.md` trong repo không kích hoạt nó.

## Router v3.2 bản tham chiếu

| Vị trí | Contract hiện hành | Thay đổi đề xuất |
| --- | --- | --- |
| Header dòng 5–7 và mục 1 dòng 11–47 | Runtime tự resolve CI file numeric latest | Với **live Project**: nhận CI đang cài ở instruction setting là active; bỏ live-discovery assumption. Nếu repo tooling vẫn cần numeric resolver, để ở Track C, không đặt vào đường live Project. |
| Luồng dòng 51–67 | `PROMPT_ROUTE_ONLY → resolve CI → 00 → 92 → current → 91 → new source → reconcile → overlay → execution` | Bỏ bước live CI discovery; giữ mọi gate khác. Thêm quyết định load mode **sau** file/domain selection, trước khi kết luận source read hoàn thành. |
| Dòng 69–79 | Route chỉ nhận diện, không lập premise | Giữ nguyên. Index/node selection không được thành câu trả lời. |
| Dòng 81 | Mọi routed file đọc hoàn toàn | Mặc định `FULL_FILE`; ngoại lệ `NODE_OR_FULL` chỉ khi bắt buộc đọc mandatory header + index + node + closure `REQUIRES`, semantic mapping đã review và Project retrieval được kiểm chứng. Node read không phải generic excerpt; bất kỳ phần không chắc quay về full current file. |
| Dòng 83–85 | Block khi decisive source thiếu; partial chỉ cho secondary gap | Giữ ý nghĩa. Không được biến “node không resolve” thành `SOURCE_LOAD_PARTIAL` nếu full file cũng không đọc được. |
| Dòng 89–132 | Authority order, old-canon quarantine | Giữ nguyên; mode không thay source priority hoặc status. |
| Dòng 137–155 | Bảng domain→file; `00/92` bắt buộc; `91` evidence theo issue | Bổ sung mode bên cạnh file, không thay domain owner. `00/92` full. Với `91`, phase đầu vẫn full; record mode sau review. `92` hook mới phải còn filename để fallback. |
| Dòng 159–187 | Resolve overlay version/status và dependency; load sau source gate | Giữ `FULL_FILE` cho toàn bộ active overlays; không thêm node contract vào overlay. |
| Dòng 191–225 | Reconciliation và pre-response check | Thêm check “closure đã đọc thật, semantic review còn hiệu lực, fallback đã chạy nếu nghi ngờ”; pre-response live CI check phải nói instruction setting identity, không numeric repo file. Giữ mọi điều cấm old-canon revival/UNKNOWN promotion. |

`60` không có hàng trong domain table hiện tại dù là current MC4 file. Cần thêm tuyến rõ `MC4/Academy identity → 60`, cùng cross-domain `40/10` theo scope. Đây là **validation gap đã thấy**, độc lập với việc node hóa.

## Anti-drift overlays

Không đổi phase đầu. Giữ nguyên header type/scope/authority, activation, open/stop và dependency. Năm active overlays được đọc trong audit: `Economy…v1.1`, `Modular…v1.0`, `Mortality…v1.1`, `Total_War…v1.1`, `Worldbuilding…v1.1`. Router hiện nạp overlay sau source/reconciliation, chỉ nếu task thuộc scope, và resolve dependency transitively. Cắt overlay có thể bỏ mất stopping rule hoặc scope caveat; chưa có bottleneck được chứng minh để trả giá đó.

## `00`, `92`, builder và package

Nếu thêm cột `load mode` vào `00`, nó chỉ là gợi ý đường đọc, không trao authority cho node. Giữ toàn bộ semantic/supersession context `00`. Với `92`, hook nên ghi **cả filename lẫn node ID tùy chọn**: `Read 20_STATUS_CIVIL_LABOR_CURRENT.md; preferred node AFN-...; fallback full file`. Hook không làm thay `91` evidence. Vì `00–92` là generated views, mọi activation bền qua rebuild cần thay đổi chỗ sinh trong builder/source mapping và kiểm output shadow. Tác vụ này không được phép chạy builder trên project thật; Track B atomic publication vẫn tách riêng.

## Hành vi cũ phải giữ

Route trước, đọc nguồn thật, đối chiếu `UNKNOWN/OPEN/DEFERRED/CONFLICTED`, nạp overlay sau gate, rồi mới execution; latest explicit user confirmation theo scope giữ precedence; source mới vẫn unconfirmed; design history không lên canon; file/overlay thiếu thì block đúng kết luận; cross-domain task đọc mọi owner có ảnh hưởng. Không có câu nào trong proposal này cấp phép canon mutation.
