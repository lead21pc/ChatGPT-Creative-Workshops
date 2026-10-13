# Rủi ro bổ sung và những điểm cần sửa trong proposal

Trạng thái: **PROPOSAL**. Các lỗi tiềm tàng của kiến trúc đích được ghi `INFERENCE`, không giả thành lỗi runtime đã xảy ra. Những failure mã hiện hành đã tái hiện nằm ở02.

## R-01 — Node ID chứa owner làm split phá tính ổn định

- **Severity:** `SCALING_RISK`; **evidence:** proposal03§3.2 dùng `AF.UNDIE:WHITE_EXIT`, §13/02§13 muốn giữ Node ID khi chuyển module.
- **Cơ chế hiện tại:** dependency bám path; proposal chuyển sang namespace owner nhưng chưa giải thích di chuyển owner.
- **Trigger/failure/impact:** split owner → phải đổi ID hoặc để namespace nói sai owner; alias dây chuyền làm reverse impact và external citation khó kiểm.
- **Guardrail:** “stable ID” bằng lời chưa quy định identity versus ownership. Không được rename ID chỉ vì đổi domain.
- **Hướng chung / xử lý cục bộ:** ID bất biến độc lập owner, tên gợi nhớ chỉ alias; owner là trường riêng. Giữ tombstone lịch sử; one-to-many split bắt consumer chọn successor theo scope, không tự redirect tất cả.
- **Rủi ro migration:** ID cũ đã được dùng trong chat/export không thể xóa alias theo thời hạn tùy ý; lưu mapping vĩnh viễn trong lịch sử release.

## R-02 — Interface registry có thể thành canon thứ hai và điểm tranh chấp tập trung

- **Severity:** `SCALING_RISK`; **evidence:** proposal02§4/06§3 nói registry không lore nhưng record chứa relation, direction, CANON và what-crosses; ví dụ có hai controlling nodes.
- **Cơ chế hiện tại:**70 sở hữu nội bộ ML;30 sở hữu status;40 sở hữu cross-world; giao diện có nhiều mặt, không nhất thiết một owner cho toàn thế giới.
- **Trigger/failure/impact:** sửa relation trong registry mà source chưa đổi → ai thắng? Registry global mọi interface cũng tăng O(E) và merge conflict.
- **Guardrail:** lời cấm registry tạo canon mâu thuẫn với duplicated asserted payload nếu không có reference semantics.
- **Hướng chung / xử lý cục bộ:** interface metadata nằm một nơi được chỉ định, chỉ tham chiếu các scope/claim được source kiểm soát. Ownership theo mặt của contract; hỗ trợ ≥3 participants; không suy quyền lực lore từ vị trí metadata. Global interface map là derived index.
- **Rủi ro migration:** chọn metadata owner là quyết định tài liệu; không được đổi source authority hoặc xác lập quan hệ lore chưa chốt để điền form.

## R-03 — Nhãn OPERABLE/DEEP dễ tạo tự tin sai

- **Severity:** `SCALING_RISK`; **evidence:** proposal06 ví dụ ML=OPERABLE;70§22 còn full Creed/constitution UNKNOWN;60 có identity rõ nhưng switching chưa chốt.
- **Cơ chế hiện tại:** prose chỉ ra giới hạn; proposal muốn một cấp coverage tổng quát cho module.
- **Trigger/failure/impact:** model dùng OPERABLE để chạy tác vụ ngoài phạm vi đủ nguồn, hoặc dùng PARTIAL để block cả câu tra cứu đủ evidence.
- **Guardrail:** coverage≠truth đúng nhưng chưa đủ; enum hỗ trợ task cũng chỉ mô tả, không chứng nhận mọi input.
- **Hướng chung / xử lý cục bộ:** coverage theo scope và task family, kèm limitations, review revision; tính đủ bằng chứng phải quyết lại trên request cụ thể. `UNASSESSED` khác `UNSUPPORTED`; field không có không nghĩa nội bộ không tồn tại.
- **Rủi ro migration:** không suy coverage từ độ dài hoặc tỷ lệ UNKNOWN; không chuẩn hóa DEFERRED thành mức coverage.

## R-04 — Trộn materialization, authority và trạng thái nội dung

- **Severity:** `BREAKPOINT_SOON`; **evidence:** current10–80 đều generated;50:6 giữ cả DESIGN INTENT/PROPOSAL; proposal04 có một enum truth gồm CANON,DEFERRED,SUPERSEDED và tuyên bố derived!=authority.
- **Cơ chế hiện tại:** gói sinh canon có authority đã chỉ định, trong đó từng mệnh đề có trạng thái riêng.00/92 là view không sở hữu canon.
- **Trigger/failure/impact:** áp blanket rule → loại current canon khỏi authority hoặc thăng toàn nội dung module CURRENT thành CANON.
- **Guardrail:** Router phân biệt role và claim; schema mới phải giữ phân biệt đó thay vì một boolean canon.
- **Hướng chung / xử lý cục bộ:** tách `role`, `materialization`, `lifecycle`, `claim_status_ref`, `issue_state`, `coverage`; raw source label được giữ nguyên. Metadata status chỉ trỏ evidence, không được sửa truth trực tiếp.
- **Rủi ro migration:** chuyển enum có thể làm mất `CANON / DESIGN INTENT`, `SEALED`, `UNDER CONSTRUCTION`; bảo toàn nguyên văn trước, mapping chỉ sau review.

## R-05 — Snapshot phải ngăn race đọc nguồn và hash nguồn

- **Severity:** `SCALING_RISK`; **evidence:** builder đọc source:181–209 rồi hash lại filesystem:1572; AR-02 đã xác nhận ghi từng phần.
- **Cơ chế hiện tại:** chưa khóa bytes input giữa read và hash.
- **Trigger/failure/impact:** người khác đổi source sau lần đọc trước lần hash → output từ bytesA nhưng manifest ghi hashB; hai branch cùng transfer authority có thể merge text sạch mà scope bị trùng.
- **Guardrail:** isolated rebuild về sau có thể phát hiện, không ngăn reader thấy generation trộn. Git commit không đồng nghĩa working tree bất biến.
- **Hướng chung / xử lý cục bộ:** build từ snapshot riêng và hash chính bytes đã đọc; writer kiểm base revision còn đúng; merge validate full graph, IDs, decision refs; reader pin snapshot cả lượt.
- **Rủi ro migration:** lock chỉ trong một máy không bảo vệ ChatGPT upload; bundle phải tự chứa generation identity và reject hỗn hợp. Chưa tái hiện race đa tiến trình, đây là suy luận từ đường code.

## R-06 — Graph lớn thật không biến mất bằng registry

- **Severity:** `SCALING_RISK`; **evidence:** các ranh giới RF, status, timeline có nhiều consumer; `closure_probe.json` tổng hợp high-fanout có8,001 node ảnh hưởng và dense80 có6,320 edge.
- **Cơ chế hiện tại:** full-read; proposal nói “minimum closure” nhưng chưa đặt hợp đồng khi vượt budget.
- **Trigger/failure/impact:** một premise chung thay đổi → affected closure gần toàn bộ gói; cắt sau N node sẽ bỏ consumer và nói sai đã đủ.
- **Guardrail:** blast-radius enum là mô tả, không phải completeness proof; optional edge không được dùng làm lối thoát khỏi dependency thật.
- **Hướng chung / xử lý cục bộ:** O(V+E) graph validation, O(Vc+Ec) traversal sau khi có index; chỉ load controls global thật sự bắt buộc. Vượt budget thì chia công việc với receipt tổng hợp hoặc block kết luận phụ thuộc; không thả edge.
- **Rủi ro migration:** graph inferred từ mọi mention tạo giả fanout; benchmark tổng hợp không chứng minh token cost hay correctness của LLM ở80 module.

## R-07 — Hash node đúng nhưng closure ngữ nghĩa sai

- **Severity:** `SCALING_RISK`; **evidence:**70 có unknown/quarantine tách khỏi đoạn cơ chế;80§4 và§10 giữ authority/current-stage unknown;50 có header hạn chế suy từ narrator sang năng lực.
- **Cơ chế hiện tại:** full-file giữ được các điều kiện ngoài đoạn; proposal node closure mới chưa có chứng cứ phân đoạn đủ.
- **Trigger/failure/impact:** index bỏ mandatory header, negation, issue hoặc exception ở node khác → validator ID/hash pass, answer sai.
- **Guardrail:** schema chỉ xác nhận những edge đã khai báo, không biết edge chưa khai báo. Full-read một module cũng chưa chữa thiếu candidate module.
- **Hướng chung / xử lý cục bộ:** segmentation review phủ toàn file, mandatory context inheritance, decisive-evidence oracle và negative fixtures; chưa review thì full affected module/domain. Search là candidate discovery, không là authority hoặc đủ closure.
- **Rủi ro migration:** claims “closure proven” phải giới hạn thành closure đúng theo metadata đã review tại snapshot, kèm giới hạn ngữ nghĩa; không chứng minh tuyệt đối đã hiểu thế giới.

## R-08 — Schema mới, điều kiện unknown và cycle cần fail có phạm vi

- **Severity:** `SCALING_RISK`; **evidence:** đề xuất version1.x, mixed lifecycle SPLITTING/MERGING, conditional overlays; current references qua lại giữa10/70/80.
- **Cơ chế hiện tại:** prose resolution không có type checker. Một cycle trong read refs có thể hợp lệ; cycle derivation/supersession thường không hợp lệ.
- **Trigger/failure/impact:** bỏ qua field/edge type lạ hoặc coi condition UNKNOWN là false → thiếu evidence; block mọi cycle → loại cả dependency hai chiều hợp lệ.
- **Guardrail:** numeric version không chứng minh compatible features.
- **Hướng chung / xử lý cục bộ:** pin supported schema major/minor+required features; unknown semantic field/edge bắt block; condition TRUE/FALSE/UNKNOWN, UNKNOWN load conservatively hoặc block nhánh phụ thuộc. Phân tích SCC theo graph type; không recursion vô hạn.
- **Rủi ro migration:** mixed schema trong một release chỉ được phép có adapter đã duyệt cho từng record; không đoán. SPLITTING là trạng thái transaction chưa publish, không là module active nửa chừng.

## R-09 — Registry lỗi không cho phép quay về canon cũ hoặc bypass authority

- **Severity:** `SCALING_RISK`; **evidence:** proposal05§9 đề xuất fallback full-file; current Router§4 cấm old-canon fallback.
- **Cơ chế hiện tại:** authority được chứng minh qua controls/index; registry đích sẽ gánh đường dẫn tới owner.
- **Trigger/failure/impact:** registry mất/stale và agent lấy cache cũ/archive → phục hồi nội dung superseded hoặc làm mutation sai owner.
- **Guardrail:** có file canon recoverable không có nghĩa đang được phép dùng nó làm hiện hành.
- **Hướng chung / xử lý cục bộ:** bundle có source map/authority receipt độc lập với cache; fallback chỉ đọc nếu current snapshot và authority vẫn chứng minh được. Mất cả root descriptor thì block conclusion, chỉ tiếp tục filesystem audit không canon.
- **Rủi ro migration:** khôi phục snapshot cũ để so sánh phải mang nhãn historical; rollback canonical activation cần quyết định rõ, không chỉ đổi symlink.

## R-10 — Đường dẫn, IDs và summaries có lỗi mà diff sạch không thấy

- **Severity:** `SCALING_RISK`; **evidence:** repo Windows, filenames có Unicode/spaces; proposal đưa Module/Node IDs mới và alias; current .gitattributes bảo toàn bytes Markdown.
- **Cơ chế hiện tại:** path strings/heading anchors, chưa có chính sách portable identity và aliases.
- **Trigger/failure/impact:** hai branch cấp cùng ID, case-only path collision, Unicode-normalization alias hoặc selector trỏ nhầm heading → integrity có thể đúng từng file nhưng binding sai.
- **Guardrail:** Git merge sạch không kiểm semantic uniqueness. Dò string duplication cũng không bắt paraphrase stale.
- **Hướng chung / xử lý cục bộ:** ID ASCII bất biến, UUID được kiểm uniqueness; path relative có chuẩn slash, kiểm canonical containment/casefold collisions và không tự sửa source Unicode. Hash raw bytes; canonicalization metadata riêng có version.
- **Rủi ro migration:** tự normalize tên/nội dung archive vi phạm byte preservation; chỉ validate và báo trước khi rename có duyệt.

## Những phần của proposal nên giữ và nên bỏ

Giữ: identity độc lập path; registry hỗ trợ discovery; metadata node theo module; truth/coverage tách; reverse impact; full-read fallback; migration shadow; tránh split90/91 quá sớm.

Sửa: một interface không nhất thiết hai phía; ID không mã hóa owner; thay “OPERABLE toàn module” bằng khả năng theo scope/task; phân biệt generated canon với generated navigation; issue source phải thật sự có owner, không cho sửa92 rồi builder ghi đè.

Bỏ khỏi giai đoạn đầu: global registry giữ payload lore của mọi interface; orphan registry riêng; enum budget dùng như quyền cắt closure; management changelog lặp toàn Git/91; việc ép lập node cho từng heading; di chuyển toàn folder; dịch toàn bộ lore thành database. Một record quyết định kiến trúc chỉ cần khi có trade-off/migration khó phục hồi từ diff.
