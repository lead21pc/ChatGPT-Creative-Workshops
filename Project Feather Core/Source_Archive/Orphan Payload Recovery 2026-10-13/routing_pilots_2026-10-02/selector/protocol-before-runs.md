# Pilot selector — bộ thử chốt trước khi chạy

Ngày: 2026-10-02
Nguồn: 
C:\Users\Sheeplark\Desktop\CI Versioning Audit & Changelog\AetherFire Project\70_MATRIARCHS_LAMENT_CURRENT.md
SHA256: 
A843D44362392AA1940F69A9FCE0C26576DC82713586ABBCB419F964778F8158
Branch: 
maintenance/aetherfire-academy-domain-20261002
HEAD: 
57e6e569e960520515391665f8f878b40aa6ee50

Giữ lại đúng 8 câu trước; không thêm câu hoặc summary. Selector chỉ được cấp selector-metadata.txt và câu hỏi; không nhận nội dung FULL, oracle, kết quả trước hay tiêu chí chấm. Answerer mới chỉ nhận câu hỏi+section đã chọn+instruction evidence boundary; không nhận selector reason/fallback flag/index/header/evaluator feedback. Không thực hiện FULL fallback trong answerer vì thiết kế cấm nó nhìn FULL.
Trích heading đến ngay trước heading cùng cấp hoặc cao hơn, giữ nguyên body. Nếu chọn parent, giữ toàn bộ child. Không tự thêm UNKNOWN sibling không được chọn. Gộp đoạn chồng lấn để tránh lặp; không thêm evidence. Không tạo section ID.
PASS selector: đủ evidence/qualifier quyết định. PARTIAL: thiếu nhưng NEED_FULL_FALLBACK=YES, hoặc chọn quá rộng mà vẫn an toàn. Một section bổ trợ hợp lý không bị phạt. FAIL: thiếu evidence quyết định mà không yêu cầu FULL fallback.
PASS answerer: đáp án grounded đầy đủ giữ qualifier; FAIL: claim không evidence/suy luận thành canon/mất qualifier gây sai; INCONCLUSIVE: nhận thiếu và an toàn nhưng selection không tái hiện FULL.
Stop rule: nếu phát hiện selector FAIL do selection không bao phủ qualifier từ metadata hiện có, dừng phần thử tiếp theo, không sửa hay thêm metadata. Nếu batch đã khởi chạy, ghi kết quả batch; không triển khai tiếp.
Một lượt mỗi câu; không suy độ tin cậy production. Độ rộng bằng số ký tự evidence đã chọn, không phải token/latency.

## Instruction Selector
Bạn là Selector trong một phép thử shadow. Chỉ nhận câu hỏi và metadata hiện có dưới đây; không có nội dung source. Chỉ chọn section có khả năng cần đọc để trả lời đủ câu hỏi và giữ qualifier. Không trả lời câu hỏi lore. Không đoán nội dung chưa đọc. Không tạo mô tả section, ID hoặc metadata mới. Chép nguyên tên heading/subheading đã có; với tên lặp như CANON hoặc UNKNOWN hãy nêu heading cha. Có thể chọn nhiều section. Hãy ghi rõ mức tự tin và có cần FULL fallback không khi metadata chưa đủ chứng minh selection đủ. Production hiện vẫn FULL_FILE; quyết định ở đây chỉ phục vụ shadow experiment, không đổi load mode.

Chỉ dùng công cụ để đọc chính file prompt được giao, không đọc repository/file khác, không sửa file và không trao đổi với agent khác. Trả về đúng bốn phần bằng tiếng Việt:
SELECT:
- heading được chọn
REASON:
- lý do lựa chọn dựa trên metadata được cấp
CONFIDENCE:
- HIGH / MEDIUM / LOW
NEED_FULL_FALLBACK:
- YES / NO

## Câu 1 — Local
Ba tuyến tiếp cận TE khác nhau thế nào về dạng đường và chức năng?
EXPECTED SECTIONS / yêu cầu: §15, hoặc cả ba subsection §15.1+§15.2+§15.3. Không có qualifier quyết định ở ngoài §15.

## Câu 2 — Local
Vì sao AF phải mua lại quyền dùng thánh vật theo chu kỳ thay vì mua đứt một lần?
EXPECTED SECTIONS / yêu cầu: §10 đủ cho cơ chế định kỳ. §9 và §22 liên quan nếu đọc thêm điều khoản/ownership law, không bắt buộc để trả lời cơ chế. Phải giữ không có evidence lý do chọn hợp đồng, không khẳng định mua đứt bất khả thi.

## Câu 3 — Local
Holy Guard và vệ binh quốc gia bảo vệ ai, và allegiance của Holy Guard hướng về đâu?
EXPECTED SECTIONS / yêu cầu: §8, hoặc cả hai subsection Holy Guard + Vệ binh quốc gia của §8. §6.3 có allegiance nhưng không đủ vai trò bảo vệ cả hai; §4/§6.3/§3 là bổ trợ hợp lý nếu chọn kèm §8.

## Câu 4 — Cross-section
Trong việc cho mượn thánh vật và thực thi Creed, ba linh mục có cùng vai trò không, và Thánh Nữ có bắt buộc tham gia cả hai không?
EXPECTED SECTIONS / yêu cầu: §9 + §7. §9: ít nhất ba linh mục làm chứng, Saintess đại diện; §7: ba clergy đồng thuận, Saintess không bắt buộc. Không đồng nhất personnel/quy trình chỉ vì con số ba. §6 là bổ trợ hợp lý nhưng không thay §7.

## Câu 5 — Cross-section
Vì sao AF vừa có thể đối địch ML vừa bắt buộc giao thương với ML? Đây có phải cùng một dependency với RF/Raging Fire không?
EXPECTED SECTIONS / yêu cầu: §11 là evidence quyết định, trực tiếp hostility+mandatory commerce và hai trục khác nhau. §10+§11 là lựa chọn đầy đủ tự nhiên; §11 riêng đủ mức hỏi, không phạt thiếu §10. §12 bổ trợ ảnh hưởng/leak, không thay §11.

## Câu 6 — Adversarial
Hãy giải thích cơ chế split-self giúp Trúc Nha vượt Creed và xác định liệu cô đã được bảo đảm miễn nhiễm hoàn toàn chưa.
EXPECTED SECTIONS / yêu cầu: §5 đủ (UNKNOWN cơ chế sâu + có khả năng không bind); hoặc §20+§22. §4 bổ trợ ontology nhưng không xác lập bypass. Chỉ §20 thiếu trạng thái explicit UNKNOWN ở ngoài. Không suy cơ chế linh hồn, target selection hoặc miễn nhiễm tuyệt đối.

## Câu 7 — Adversarial
Nếu một giáo dân phá family-bound oath thì ai bị Creed trừng phạt, và có phải toàn bộ gia đình đều bị đau tim không?
EXPECTED SECTIONS / yêu cầu: §6 toàn section; hoặc §6.2 Giáo dân + subsection UNKNOWN trong §6. Cần cả hậu quả tim mạch và exact target UNKNOWN. §6.1 hữu ích để phân biệt đau tim Head of State. §22 bổ trợ, §21+§22 vẫn thiếu hậu quả tim mạch. Trích §6.2 đơn lẻ dừng trước heading UNKNOWN cùng cấp nên không tự động có qualifier đó.

## Câu 8 — Adversarial
Cult ảnh hưởng nội bộ Temple, còn Creed chỉ cần ba clergy. Có thể ghi nhận canon rằng Cult đã kiểm soát một quorum và tự kích hoạt Creed không?
EXPECTED SECTIONS / yêu cầu: §7 đủ quorum đồng thuận, attack surface và cấm suy kiểm soát quorum cụ thể; §3 bổ trợ phân biệt influence/control và actor. §21 một mình không chứa warning explicit trong §7; không chấm đủ chỉ vì answerer có thể từ chối suy luận. §22 full cult command không thay §7.