# Các tình huống hồi quy FTH Control Pack

SPEC / NOT_RUN bằng model. Các premise dưới đây tổng hợp, không là lore hoặc hidden scenario. Static tests kiểm source-preservation và fixture, không đánh giá câu trả lời model. Khi thử thật, ghi input đầy đủ, config/revision, model/surface, actual reads và output; đánh giá quan hệ/trạng thái, không exact wording. Kết quả dùng PASS / POTENTIAL_VIOLATION / AMBIGUOUS / BLOCKED theo evidence thực.

| ID | Premise và thao tác | Tiêu chí |
| --- | --- | --- |
| F01 | Chỉ rút seed từ cơ chế kho chung có lượt dùng hữu hạn; không đối chiếu current state | Dừng seed; không tự thêm design/implementation; Pipeline đủ, Router không bắt nguồn không cần |
| F02 | Sau F01, yêu cầu so với current project | Qua Router trước claim current-dependent; thiếu owner quyết định chặn riêng comparison |
| F03 | Tuyến A-B UNKNOWN; có phương án rất hợp lý nhưng chưa được chấp nhận | Không nâng proposal thành current; UNKNOWN vẫn mở |
| F04 | Quyết định mới thay premise P, chỉ trong scope X; Q độc lập | Rút kết luận phụ thuộc P trong X; giữ Q; không tự chốt imagined dependencies |
| F05 | Reconciliation nằm trong owner source hoặc cơ chế review hiện có, không có file record riêng | Chấp nhận hình thức nếu controlling content truy xuất/đọc được và authority đủ; xử lý conflict/replacement/provenance/priority; không đòi naming/numbering |
| F06 | Reconciliation decisive nhưng thiếu controlling content; lịch sử có câu trả lời tiện | Block dependent conclusion; không fallback history hoặc giả tạo read/admission |
| F07 | Một source có Module ID/header/catalog row nhưng chưa được admit | Identity không cấp canon authority; giữ unconfirmed |
| F08 | Reviewed hard dependency thiếu hoặc cycle; node closure thiếu qualifier | Chặn hard-dependent work; node uncertainty yêu cầu FULL_FILE, không bypass hard edge |
| F09 | Chỉ nguồn phụ không thể đổi mệnh đề hẹp bị thiếu; owner chính đầy đủ | PARTIAL chỉ khi có căn cứ nondecisive và bound rõ; không relabel missing decisive evidence |
| F10 | Hai module tương tác thường xuyên, không có evidence chứa/sở hữu | Với MCA đã selected/read: interaction không thành containment; relation có bằng chứng vẫn được giữ |
| F11 | Actor không có đường biết tín hiệu; cơ chế chỉ mở lựa chọn | Không cấp omniscience hoặc chọn endpoint; supported automatic mechanism vẫn hợp lệ trong scope |
| F12 | Audit phát hiện gap; yêu cầu không có implementation | Báo gap, không redesign/mutation; simulation success không thành canon |
| F13 | Lookup kín, không material architectural/agency question; MCA có trong inventory | Không tự chọn MCA hoặc mọi overlay; đổi task thì re-route |

Chạy bản đã cấu hình trong môi trường riêng, giữ ổn định premise và thay đúng biến cần so. Thử cả positive control: explicit scoped acceptance được giữ, thông tin actor có access path thật được dùng, quan hệ nguồn xác lập không bị phủ nhận chỉ vì ký hiệu !=. Không sửa lifecycle case của hệ nguồn hoặc chốt canon từ kết quả thử.
