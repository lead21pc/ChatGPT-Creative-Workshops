# Quyết định kiến trúc còn mở

Trạng thái: **PROPOSAL / chưa có quyết định của người dùng**. Không mục nào trong file này là câu hỏi canon đang được giải quyết; các issue `UNKNOWN / OPEN / DEFERRED / CONFLICTED` của lore giữ nguyên. Các phương án dưới đây đủ cụ thể để chốt trước khi triển khai từng giai đoạn của08.

| ID | Quyết định cần chốt | Khuyến nghị và căn cứ | Nếu chọn khác / cổng liên quan |
|---|---|---|---|
| D01 | Baseline cho migration: GitHub `main` hay chuỗi local HEAD? | Pin một commit và liệt kê riêng các local-only delta cần đưa vào. `main=67fef7f…`; localHEAD=`f4b7780…` khác ở11 đường dẫn AetherFire. | Không lấy local-only làm published canon. Cần trước P1/P2. |
| D02 | Activation mới explicit descriptor hay giữ highest eligible numeric? | Dùng explicit release descriptor sau khi shadow chứng minh parity. Probe DRAFT2.99 cho thấy runner hiện khác Router. | Nếu giữ auto-latest, phải có một resolver eligibility chung và compatibility check; rủi ro kích hoạt file mới bằng vị trí cao hơn. Cần trước P6. |
| D03 | Format metadata và canonical hash? | JSON strict, UTF-8, duplicate-key rejection; Markdown giữ làm nội dung. Repository đã có JSON/Python/PowerShell. | YAML cần parser/version và scalar semantics; mọi format phải pin canonicalization. Cần trước P2/P3. |
| D04 | Ai là editing owner cho curated literals? | Map theo từng output/source/decision, rồi chuyển sang Markdown editable theo đợt, giữ archive byte-exact. AR-04 cho thấy5 nguồn chỉ được read/presence-check. | Giữ trong builder lâu hơn vẫn có thể, nhưng node schema phải biểu diễn rõ; không chuyển ownership bằng copy tự động. Cần trước P4. |
| D05 | ID stable và alias khi split? | Opaque immutable ID, owner/path riêng; tombstone không tái dùng. Node một→nhiều yêu cầu consumer review. | ID kiểu `AF.UNDIE:WHITE_EXIT` dễ vỡ khi chuyển owner. Cần trước P3/P5. |
| D06 | Interface record có được chứa claim lore? | Chỉ giữ navigation, controlling facet refs, unresolved state; không copy truth/direction thành canon độc lập. | Nếu cho authoritative payload, phải có quyết định chuyển authority với nguồn, conflict/rollback model mới. Cần trước P3. |
| D07 | Scope và coverage đủ hẹp ở mức nào? | Khai báo theo task family + scope, giữ UNASSESSED mặc định; bắt review trước node activation. | Enum OPERABLE chung module có thể gây false confidence. Cần trước P5. |
| D08 | Cách phát hành nhiều file theo một snapshot? | Git commit-pinned bundle cho repository; local/export generation bất biến + active pointer, reader pin từ đầu lượt. | Nếu target không hỗ trợ atomic pointer/upload, cần quy tắc block mixed generation và handoff thủ công. Cần trước P6/P8. |
| D09 | `00/92` đổi vai trò lúc nào? | Chỉ sau source map/issue records đã đối chiếu hai chiều và generation deterministic; giữ generated canon10–80 có authority theo quyết định hiện tại. | Chuyển92 sớm có thể mất issue seed hoặc raw status; không sửa trực tiếp output generated. Cần trước P7. |
| D10 | `90/91` có cần split ngay? | Chưa. Dùng route-by-section/ID khóa revision và đo task cost, update collision, provenance retrieval. | Split chỉ vì4,000/640 dòng tạo fragmentation; nếu concurrency tăng, shard records theo owner/ID. Đánh giá ở P9. |
| D11 | Verifier có vào repository không và package baseline lỗi xử lý thế nào? | Version tool cùng repo; xử lý archive unlisted bằng quyết định admission rõ trước khi tuyên bố package PASS. | Chỉ regenerate manifest để hết lỗi có thể hợp lệ sau khi phân loại file, nhưng không là bằng chứng canon import. Cần trước P2. |
| D12 | Điều kiện để chạy semantic/live regression? | Giữ9 case DRAFT; chọn bounded task classes/prompt/evidence oracle và phê duyệt riêng theo README. | Structural pass không thể thay runtime result; nếu không có môi trường live, chỉ bật shadow/read-only với giới hạn rõ. Cần trước P6/P8. |
| D13 | Chi phí và ngưỡng full-read fallback? | Bắt full-read khi metadata chưa review, scope rộng, stale, missing edge hoặc semantic mismatch; nếu quá lớn thì chia với receipt hoặc block. | Không dùng hard cap N node để tuyên bố closure complete. Cần trước P5/P6. |
| D14 | Rollback/supersession publication? | Whole compatible release về source, controls, schema, metadata và views; commit/revert hoặc bundle pointer. | Rollback một file generated lẻ có thể hồi sinh premise cũ hoặc làm issue lệch. Cần trước P8. |

## Thứ tự quyết định tối thiểu

Trước khi viết validator production: D01, D03, D05, D07, D11. Trước khi chuyển editing owner: D04, D06, D09. Trước khi bật Router mới: D02, D08, D12, D13. Trước mutation transaction: D14 cùng toàn bộ căn cứ authority/scope còn material.

Các lựa chọn này có thể được duyệt từng nhóm. Đồng ý D03 về JSON không đồng nghĩa chấp nhận schema05 toàn bộ, chuyển source authority, nâng phiên bản CI hoặc publish. Nếu một lựa chọn đổi, cập nhật chính thiết kế/acceptance liên quan rồi mới triển khai; không khớp schema bằng cách sửa canon để có dữ liệu đẹp.

## Giới hạn của kết luận 10 lần

Kiến trúc04 có thể biểu diễn thêm module mà không mở rộng CI/Router cho từng domain **nếu** nguồn mới vẫn dùng các primitive đọc, authority, interface, issue, history và decision đã nêu. Không có bảo đảm mọi future world system sẽ vừa khít. Một feature mới thật sự thay nghĩa quyền nguồn, thời gian/lớp canon hay điều kiện nạp sẽ cần schema/control review có version, nhưng đó là evolution có giới hạn thay vì dựng lại toàn repository. Graph dày thật thì chi phí review tăng theo quan hệ thật; không nên che bằng registry hoặc AI search.
