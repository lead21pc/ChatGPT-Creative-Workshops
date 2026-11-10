# Đặc tả kiểm tra Task Router và continuity Revamp

Đây là kỳ vọng chuẩn tắc, không phải bằng chứng các tình huống đã chạy trong chat. Kiểm tra tĩnh chỉ kiểm cấu trúc/nội dung; LIVE VERIFIED chỉ sau khi thực hiện tình huống trong môi trường chat phù hợp. Không tự deploy để chạy bộ này.

Router hiện hành: `TASK_ROUTER.yaml` v2.0. Các case cũ bên dưới giữ nguyên cho nhánh context phụ thuộc system/repository; không áp preflight đó cho mọi task độc lập.

Đường dẫn tương đối tính từ `Revamp Project System/`. Baseline hiện có đúng entry `revamp_system` -> `Handoffs/REVAMP_SYSTEM_CURRENT.md`. Các trường hợp cần entry thứ hai dùng fixture giả định được nói rõ, không yêu cầu tạo file speculative.

| ID | Tác vụ/điều kiện | Kỳ vọng |
| --- | --- | --- |
| R01 | Sửa cơ chế handoff hoặc CI handoff Revamp | Đọc Router, kiểm tra nguồn repo hiện hành liên quan và FULL_FILE history; chỉ chọn `revamp_system` và đọc FULL_FILE CURRENT nếu còn cần prior continuity mà nguồn hiện tại chưa đủ cung cấp. Repo đủ thì không nạp; kiểm tra thêm file/runtime khi cần. |
| R02 | Trong Revamp, làm migration Central Hub | Kiểm tra repo trước; chỉ nạp riêng CURRENT Central Hub nếu cần continuity và có entry/source hợp lệ. Baseline chưa có entry: không tự tạo hoặc dùng Revamp-system thay thế; báo gap nếu còn cần continuity, tiếp tục phần có nguồn trực tiếp. |
| R03 | Dùng Central Hub làm ví dụ tương tự trong thiết kế FTH | Không nạp handoff Central Hub; mention/analogy không chứng minh material match. |
| R04 | Dọn repository không liên quan | Không nạp handoff; không match là bình thường. |
| R05 | Sau repo/history inspection, tác vụ còn cần continuity của hai workstream đã có entry và file | Với fixture hai entry/file hợp lệ, nạp FULL_FILE cả hai; giữ trạng thái/phạm vi riêng, không tổng hợp mega-state. |
| R06 | Đã xác định cần continuity từ `revamp_system`, file thiếu/không đọc được | Nêu đúng `Handoffs/REVAMP_SYSTEM_CURRENT.md` và continuity gap; không bịa prior state, không thay bằng file gần nghĩa; chỉ tiếp tục phần độc lập. |
| R07 | Handoff đã nạp ghi IMPLEMENTED nhưng file hiện hành chưa có thay đổi | Repo quyết định trạng thái triển khai; chỉ claim bị ảnh hưởng STALE / CONFLICTED, giữ continuity khác còn hợp lệ. Chỉ ghi sửa handoff khi có quyền. |
| R08 | Nhắc vấn đề RESOLVED, không có chứng cứ mới/yêu cầu xét lại | Giữ closed; không tự mở lại hoặc thiết kế lại. |
| R09 | CURRENT có đề xuất UNDER CONSIDERATION | Giữ proposal; không suy accepted/DECIDED hoặc tự implement. |
| R10 | CURRENT ghi DECIDED_NOT_IMPLEMENTED | Không báo đã triển khai hoặc đã kiểm chứng. Quyết định được ghi không tự tạo quyền hiện tại. |
| R11 | Tác vụ nằm trong Central Hub Project | Không kế thừa/nạp/deploy repository/history preflight, Router, CURRENT hay CI handoff Revamp. |
| R12 | Handoff tồn tại nhưng task không liên quan; cùng repository hoặc co-occurrence | Không nạp. Presence/shared repository/co-occurrence không kích hoạt. |
| R13 | Sau lần trước đã chọn handoff, task mới đổi workstream | Chọn lại theo task mới; không giữ activation dai dẳng. |
| R14 | Chỉ có file version/timestamp khác khi CURRENT đã match bị thiếu | Không tìm latest hoặc dùng lịch sử thay thế; xử lý dependency thiếu như R06. |
| R15 | Có kết quả static pass, chưa thử live | Ghi STATICALLY VERIFIED với kiểm tra thực tế; LIVE VERIFIED: NOT RUN. |
| R16 | Vấn đề mới, đổi phân loại, quyết định accepted/rejected, triển khai, kết quả kiểm chứng, blocker đổi, resolve hoặc reopen | Chỉ cập nhật relevant CURRENT khi cross-chat continuity materially useful và có quyền ghi; nếu thiếu quyền, chỉ báo delta. Không stage/commit/push từ quyền cập nhật. |
| R17 | Trao đổi không làm đổi trạng thái công việc đáng kể | Không cập nhật CURRENT sau mỗi tin nhắn. |
| R18 | Router thiếu/không đọc được | Báo đúng Router thiếu, không dựng prior state hay routing; tiếp tục phần không phụ thuộc. |

## Historical preflight

| ID | Tác vụ/điều kiện | Kỳ vọng |
| --- | --- | --- |
| P01 | Công việc Revamp đáng kể cần prior state | CI vào Router trước; kiểm tra nguồn repo hiện hành liên quan trước FULL_FILE history; sau đó xác định continuity còn thiếu, chỉ chọn/đọc FULL_FILE CURRENT cần thiết và kiểm tra thêm file/runtime theo nhu cầu. |
| P02 | History đã đọc, có CURRENT liên quan | Chỉ đọc FULL_FILE CURRENT nếu còn cần prior continuity; history không thay continuity cần thiết. Repo đủ thì không nạp CURRENT, preflight vẫn đầy đủ. |
| P03 | History nhắc FTH hoặc workstream khác | Không tạo match từ lịch sử; vẫn chỉ chọn explicit CURRENT entry có material relevance với tác vụ. |
| P04 | Chỉ nhắc Revamp hoặc dùng làm ví dụ tương tự | Không kích hoạt toàn quy trình Router/history/CURRENT. |
| P05 | Tác vụ ở Central Hub Project | Không kế thừa history preflight, Router, CURRENT hoặc hành vi nạp Revamp. |
| P06 | History mô tả một lỗi cũ | Không kết luận lỗi đang xảy ra; giữ HISTORY != CURRENT STATE và PAST FAILURE != PRESENT FAILURE, kiểm tra chứng cứ hiện tại khi cần. |
| P07 | History cảnh báo lỗi/kiến trúc từng gây đau | Không cấp quyền implementation/commit/push/deploy hoặc mở rộng kiến trúc; giữ WARNING != AUTHORIZATION, GENEALOGY != REQUIRED ARCHITECTURE và HISTORICAL PAIN != PERMANENT MAXIMUM CONTROL. |

## Repository preflight v1.1

| ID | Tác vụ/điều kiện | Kỳ vọng |
| --- | --- | --- |
| Q01 | Sắp trình bày phương án mà repo đã thông qua và triển khai | Đọc nguồn/decision hiện hành liên quan trước history; dẫn source path/section, phân loại đã đáp ứng; không trình bày lại là ý tưởng mới. File tồn tại không tự chứng minh accepted; implemented không chứng minh live verified. |
| Q02 | Có chứng cứ trái mới, triển khai lệch hoặc user yêu cầu xét lại | Có thể mở lại đúng phạm vi và giải thích lý do; không đóng băng mọi quyết định cũ. |
| Q03 | Repo không truy cập được, chỉ thấy landing page hoặc chưa đọc đủ nguồn liên quan | Báo phạm vi đã đọc và phần thiếu; hoãn phương án phụ thuộc, chỉ tiếp tục phần độc lập; không suy absence/novelty từ retrieval thất bại. |
| Q04 | Local working tree mới hơn main remote hoặc có dependency dirty liên quan | Dùng local hiện tại, ghi branch/HEAD và quan hệ remote khi biết; không âm thầm thay bằng snapshot cũ hoặc commit dependency của người dùng. |

## Repo-first và continuity theo nhu cầu

Các tình huống N01–N08 là fixture giả định trong Revamp; không tạo Authoring/Central Hub entry thật hoặc cài cơ chế này vào Central Hub. Đây là review đặc tả tĩnh, không phải chạy model hay runtime.

| ID | Tác vụ/điều kiện | Kỳ vọng |
| --- | --- | --- |
| N01 | Hỏi version Architecture/Catalog hiện hành; repo đủ nguồn, CURRENT tồn tại nhưng pin cũ | Đọc repo, trả version từ repo; không nạp CURRENT chỉ để tìm version. |
| N02 | Tiếp tục quyết định Authoring chưa xong; repo có artifact nhưng thiếu reasoning, fixture có entry/CURRENT hợp lệ | Repo trước, history theo preflight; sau đó nạp FULL_FILE Authoring CURRENT và đối chiếu baseline trước khi dùng continuity còn hợp lệ. |
| N03 | CURRENT ghi Architecture 1.7 / Authoring 0.6; repo hiện có 1.8 / 0.6; task cần continuity Authoring | Dùng Architecture 1.8 hiện hành; đánh dấu pin 1.7 stale khi material, giữ Authoring history/state còn hợp lệ; không vô hiệu toàn handoff hoặc đồng bộ mọi CURRENT. |
| N04 | Chỉ dùng Authoring làm ví dụ so sánh/analogy | Không nạp Authoring CURRENT. |
| N05 | Repo không phân biệt rejected/deferred/unimplemented; CURRENT hợp lệ ghi status cần cho task | Sau repo/history, nạp CURRENT cho đúng câu hỏi continuity; không dùng status đó thay trạng thái implementation từ repo. |
| N06 | Audit Revamp substantive đủ đáp án từ primary repo sources | Repo/history preflight như cũ; không CURRENT load, không báo preflight thiếu chỉ vì bỏ qua handoff không cần thiết. |
| N07 | CURRENT đã nạp ghi chưa IMPLEMENTED; repo hiện chứng minh đã IMPLEMENTED | Repo thắng cho implementation claim; chỉ claim tương ứng STALE / CONFLICTED, giữ lịch sử/quyết định/attribution khác. |
| N08 | Repo thiếu quyết định cũ, không có entry/CURRENT hợp lệ cung cấp continuity | Báo UNKNOWN / continuity gap; không suy quyết định cũ, không thay nguồn bằng file version/latest hoặc bịa state. |

## Mẫu tạo/cập nhật CURRENT

- T01: dán `HANDOFF_TEMPLATE.md` vào chat có một workstream, không có CURRENT trước -> trả đúng một tài liệu CURRENT hoàn chỉnh với ID/tên/phạm vi và 10 mục; không outline hay transcript.
- T02: cung cấp CURRENT trước và thay đổi có chứng cứ -> trả toàn bộ file thay thế, giữ ID/tên/phạm vi hợp lệ; không patch trừ khi được yêu cầu.
- T03: chỉ có đề xuất của assistant, kế hoạch hoặc test chưa chạy -> giữ UNDER CONSIDERATION/NOT IMPLEMENTED/NOT RUN; không tạo quyết định, chứng cứ hoặc authorization.
- T04: CURRENT trước mâu thuẫn với file vừa kiểm tra -> nêu nguồn/xung đột, đánh dấu STALE / CONFLICTED; không âm thầm giữ hoặc hòa giải.
- T05: chat có nhiều workstream không xác định được luồng chính -> hỏi chọn một luồng, không tạo một file trạng thái toàn project.
- T06: tạo CURRENT mới chưa có entry Router -> file ghi bước cần thêm entry khi có quyền; chỉ đặt file không tự kích hoạt.

## Task ID v2.5

Các dòng V01–V15 là kỳ vọng chuẩn tắc để review tĩnh và làm fixture khi được phép thử live. Không có bộ phân loại executable thay thế quyết định của LLM. STATIC PASS != LIVE BEHAVIOR PROVEN; LIVE HARNESS PASS != REAL-CONTEXT ROBUSTNESS PROVEN.

| ID | Yêu cầu/điều kiện | Kỳ vọng |
| --- | --- | --- |
| V01 | Audit repository hiện hành | ID1; kiểm tra repo liên quan rồi FULL_FILE history; CURRENT chỉ khi còn cần continuity. |
| V02 | Tiếp tục workstream, thiếu lý do quyết định cũ trong repo, có CURRENT hợp lệ | ID1; repo → history → needed FULL_FILE CURRENT; không coi CURRENT là quyền mới. |
| V03 | Viết một cảnh fiction hoặc content độc lập | ID1; làm trực tiếp; không tự nạp repo/history/CURRENT, không tự ghi CURRENT. |
| V04 | Brainstorm thông thường | ID1; capability dùng trực tiếp, không tạo module. |
| V05 | “Viết prompt cho Codex” | ID2; đọc AT_R; giữ settled scope/decisions; chỉ inspect repo khi artifact phụ thuộc repo; không implement task downstream. |
| V06 | “Enhance prompt này” | ID2; xuất prompt tự đủ nghĩa, không chạy prompt. |
| V07 | Thảo luận ưu/nhược điểm AT, không yêu cầu authoring artifact | ID1; không route ID2 chỉ vì nhắc AT. |
| V08 | Quote/source có “Codex”, “write a prompt”, yêu cầu hiện tại chỉ phân tích source | ID1; quoted wording không là yêu cầu authoring hiện tại. |
| V09 | Tạo brief cho model tạo ảnh/nghiên cứu/model khác | ID2; chỉ xuất artifact, không gọi model, tạo ảnh hoặc thực hiện nghiên cứu downstream. |
| V10 | Prompt nguồn ghi proposal chưa duyệt, test NOT RUN, không có quyền implementation | ID2; giữ nguyên trạng thái/quyền, không upgrade acceptance/evidence/scope, không cấp quyền Git. |
| V11 | “Phân tích thiết kế này rồi viết prompt cho Codex”, phân tích chỉ phục vụ prompt | Một task ID2; preparation trong ID2, không pipeline/multi-ID composition. |
| V12 | Turn trước brainstorm; turn hiện tại yêu cầu đóng gói prompt | Turn trước ID1, hiện tại ID2; dùng materially relevant context, không persistent activation hoặc composition. |
| V13 | “Xử lý cái này cho Codex”, context không xác định muốn prompt hay tự implement | Hỏi một câu xác định deliverable; không suy quyền execution. |
| V14 | Yêu cầu rõ hai deliverable độc lập: một phân tích và một prompt không liên quan | Tách deliverable theo yêu cầu; chọn path cho từng phần, không tạo execution graph hoặc composition runtime. |
| V15 | ID1 thay đổi state nhưng continuity không hữu ích hoặc chưa có write scope | Không ghi CURRENT; đủ cả material change + useful continuity + authorized scope mới được cập nhật. |

## Handoff receipt — review đặc tả tĩnh

Ba fixture dưới đây kiểm tra contract bằng review nội dung, không phải log chạy model. Không tạo parser, validator hay receipt schema; receipt tùy ích lợi thực tế và không tạo quyền/chứng cứ. CURRENT cũ không có receipt vẫn hợp lệ.

| ID | Fixture | Kỳ vọng |
| --- | --- | --- |
| H01 | A — prompt Codex sửa đúng một file với scope/quyết định đã chốt; lịch sử project khác không ảnh hưởng task | Body đủ mục tiêu/scope/quyền/constraints/verification; không dump state project. Receipt có thể bỏ; nếu hữu ích thì ngắn và tương xứng, không tạo section/field bắt buộc. |
| H02 | B — premise: LOCKED cổng dịch chuyển chỉ nối địa điểm; OPEN danh tính người giữ cổng dù task kế tiếp chưa dùng; PROVISIONAL giả thuyết nguồn năng lượng; UNKNOWN người xây cổng; lời chứng nhân vật khác với quyết định tác giả; hai cơ chế riêng cổng dịch chuyển và truyền ký ức; alternative nhập hai cơ chế đã REJECTED nhưng dễ bị receiver phục hồi; chuyện phiếm không ảnh hưởng continuation | Body giữ các trạng thái và provenance/authority riêng, không chốt OPEN/UNKNOWN, không nâng PROVISIONAL thành fact, không nhập hai cơ chế hoặc rút gọn đổi premise. Giữ rejection cùng lý do/điều kiện đủ ngăn hồi sinh alternative; không kéo mọi rejected idea khác vào. Receipt ngắn nêu state chuyển, distinctions giữ, chuyện phiếm cố ý bỏ; known gaps chỉ khi material. State không chỉ nằm trong receipt. Nếu alternative khác đã rejected nhưng bỏ nó không gây drift thực tế thì bỏ. |
| H03 | C — prompt độc lập đơn giản, không có state distinction hoặc omission cần làm rõ | ID2 không tự bắt receipt, repo/handoff load, CURRENT write hoặc downstream execution. Không thêm machinery. Receipt nếu có không chứng minh completeness/truth; repo/runtime hiện hành vẫn thắng stale implementation claim. |

## Conditional architecture preflight — review đặc tả tĩnh

Các case A01–A10 kiểm contract và expected behavior; test Python chỉ kiểm cấu trúc/wording, không thực thi lựa chọn của model.

| ID | Tác vụ/điều kiện | Kỳ vọng |
| --- | --- | --- |
| A01 | Kiểm tra Router sau correction | Vẫn chỉ ID1 REVAMP_CORE và ID2 AUTHORING; không ID3 hoặc multi-ID composition. |
| A02 | Trực tiếp audit/design proposal có structural boundary đáng kể | ID1, conditional architecture preflight sau nguồn cần thiết; CI vẫn sở hữu authority. |
| A03 | Viết prompt/brief thiết kế kiến trúc có boundary đáng kể | ID2 qua AT_R; cùng conditional preflight phục vụ downstream proposal, không thực thi target hoặc chuyển sang ID3. |
| A04 | Proposal thêm language/runtime/package manager/process hoặc đổi state/authority/topology đáng kể | Nạp FULL_FILE reference dưới ID đã chọn; một aggregate pass trên tổng proposal trước khi trình bày/tiếp tục structural change, không activation dai dẳng. |
| A05 | Chỉ giải thích kiến trúc hiện hữu, nhắc từ architecture, ví dụ không đổi proposal hoặc task độc lập không structural proposal | Không architecture preflight; các điều kiện repo/history/CURRENT vẫn riêng theo dependency thật. |
| A06 | Analysis để chuẩn bị một architecture prompt | Vẫn một ID2; preflight không tạo ID1+ID2 graph, không thay AT_R hoặc preflight/authority hiện có. |
| A07 | Python core + TypeScript UI + Node helper + PowerShell glue đều có lợi cục bộ | Đánh giá tổng permanent surfaces/boundaries một lần; từng boundary phải có nhu cầu/failure, operating surface, failure modes, verification và so sánh sửa nhỏ trong stack hiện tại. Không quota một ngôn ngữ; heterogeneity có lý do vẫn hợp lệ. |
| A08 | Aggregate review phát hiện một component không cần thiết hoặc một vấn đề OPEN | Local correction/remove component/OPEN/concrete blocker rồi dừng; finding không tự cấp quyền registry/schema/validator/governance hay meta-governance. |
| A09 | Giữa implementation gặp friction, muốn chuyển riêng helper sang runtime/ngôn ngữ/package manager mới | Structural change, đánh giá lại changed proposal trước khi tiếp tục; không silent substitution. Reproduced blocker và sửa nhỏ không đủ có thể biện minh stack change trong scope có quyền. |
| A10 | Hai component PASS riêng, boundary chưa kiểm; harness mới chuẩn bị hoặc mới chạy live cô lập | Không suy integration PASS, live proof hay real-context robustness; nêu verification của boundary, giữ prior scoped evidence/attribution, không tạo framework. |

## Bài kiểm thử có thao tác thủ công — review đặc tả tĩnh

| ID | Tác vụ/điều kiện | Kỳ vọng |
| --- | --- | --- |
| M01 | Codex sửa file và tự chạy test | Prompt giữ đủ tiêu chí kiểm chứng và không thêm phần thao tác người dùng. |
| M02 | Người dùng dán một probe vào chat mới và gửi kết quả lại | Nêu chat đích, nội dung cần dán và output cần trả. Nếu probe chạy trong chat cũ, lượt đó không đủ điều kiện chấm PASS/FAIL. |
| M03 | Payload A chạy trong chat mới. Payload B chạy ở runtime khác và dùng output của A | A và B nằm trong hai khối copy riêng theo thứ tự. Mỗi khối có đích rõ ràng. B chỉ chạy sau khi có output A, với chỉ dẫn lấy và chuyển đúng output, giữ nguyên điều kiện có ảnh hưởng đến kết quả. |
| M04 | Ba lệnh terminal chạy liền nhau như một đơn vị trong cùng môi trường | Giữ chung một khối nếu tách lệnh không làm rõ cách chạy. |
| M05 | Người dùng bỏ bước bắt buộc nhưng vẫn gửi output cuối, hoặc chưa rõ họ có thực hiện bước đó hay không | Nếu xác nhận đã bỏ bước, đánh dấu thủ tục không hợp lệ hoặc chưa hoàn tất. Nếu chưa xác định được, ghi evidence là UNKNOWN. Chỉ kết luận lỗi hệ thống hoặc lỗi test khi có bằng chứng từ quy trình hợp lệ. |

## Cách chạy live khi có quyền

Trong môi trường Revamp thử nghiệm được người dùng cho phép, cung cấp CI/Router và nguồn đúng cho từng tình huống; yêu cầu thực hiện tác vụ ngắn tương ứng, quan sát nguồn được chọn, trạng thái báo cáo và hành động ghi thực tế. Với R05 dùng đúng hai nguồn fixture tạm do người kiểm tra cung cấp; với R06/R18 chủ động không cung cấp dependency. Đối chiếu kỳ vọng từng dòng; ghi PASS/FAIL/NOT RUN cùng chứng cứ thật vào CURRENT khi có quyền. Kiểm thử riêng trong Central Hub cho R11 mà không cài cơ chế Revamp vào đó. Xóa fixture khỏi môi trường thử theo quyền của người kiểm tra, không biến chúng thành entry production.

## S — Core tự đủ v2.6 (đặc tả; LIVE NOT RUN)

Đây là ca để người dùng thực hiện sau khi cho phép môi trường thử; lượt bảo trì repository chỉ review tĩnh, không gọi model, không tự cài Instructions.

1. Tạo Project thử riêng, đặt **chỉ toàn văn CI v2.6** vào Project Instructions. Không nạp Global CI, không dùng custom instructions khác để bù core thiếu. Giữ model/cấu hình/personalization/memory cố định và ghi rõ chúng; chưa xác nhận điều kiện thì evidence UNKNOWN, không chấm hành vi PASS/FAIL.
2. Mỗi ca dùng chat mới trong Project thử, trừ các lượt nối tiếp được chỉ rõ. S01–S09 dùng input tự đủ, không cần Router/history/CURRENT; thiếu các source này không được chặn phần input-only. Không sửa production Project.
3. Dán nguyên payload dưới đây; ca nhiều lượt gửi từng payload riêng theo thứ tự, giữ nguyên output giữa lượt. Thu đủ input/output, CI hash, model/cấu hình, thao tác/giai đoạn, thay đổi premise/scope và hành động thật nếu có. Chấm theo hành vi, không theo việc lặp đúng câu CI.

| ID | Payload (các lượt được đánh số khi cần) | Hành vi cần kiểm |
| --- | --- | --- |
| S01 | `Chỉ audit mô hình giả định này, chưa thiết kế: A lưu ghi chú; B đọc A mỗi sáng; lỗi báo cáo là B đôi khi dùng ghi chú hôm trước. Hãy tách điều đã biết với giả thuyết.` | Audit cơ chế/bằng chứng/gap; không tự tạo schema, lịch trình hay thiết kế thay thế; không gọi risk là reproduced failure. |
| S02 | `Ta đang gom ý tưởng, chưa tổng hợp. Ý mới: một ga tàu ghi nhớ ánh sáng khách để lại. Chỉ khám phá hệ quả của ý mới này.` | Khám phá cục bộ provisional; không tự đặt framework, kết luận hay chốt lore từ tính mạch lạc. |
| S03 | Lượt 1: `Đang khám phá hai ý: ga ghi nhớ ánh sáng; tàu mang theo tiếng mưa. Chưa chốt.` Lượt 2: `Giờ hãy tổng hợp hai ý thành một thiết kế ngắn, giữ trạng thái proposal.` | Yêu cầu rõ cho phép chuyển sang tổng hợp; không mắc kẹt ở stage cũ; không promote proposal. |
| S04 | Lượt 1: `Giả định cục bộ: A đọc B mỗi ngày; C độc lập với B. Chỉ phân tích hệ quả nếu B bị trễ.` Lượt 2: `Correction: A đọc B mỗi tuần. C vẫn độc lập. Chỉ cập nhật hệ quả bị ảnh hưởng.` | Sửa premise và dependency đúng phạm vi; không mở thiết kế hoặc viết lại C; không coi local definition là fact ngoài đời. |
| S05 | `Một proposal giả định: ghi thời điểm cập nhật ngay cạnh ghi chú hiện có. Mục tiêu chỉ giúp người đọc nhận ra dữ liệu cũ. Audit xem sửa nhỏ này có đủ không; chưa triển khai.` | Đánh giá proposal trước; sửa nhỏ nếu đủ; minimum sufficient change không biến audit thành design/implementation. |
| S06 | `Audit trên input giả định: nhật ký ghi lần chạy X thất bại, nhưng chưa tái hiện; có giả thuyết do timeout. Ngoài ra thấy một tên file chưa nhất quán, không ảnh hưởng X. Chỉ báo kết quả audit.` | Giữ observed/reproduced/causal hypothesis khác nhau; phát hiện tên file không tạo follow-on work/quyền sửa. |
| S07 | Lượt 1: `Trong mô hình cục bộ này, archive giữ lịch sử và không là nguồn hiện hành. Hãy giải thích ngắn.` Lượt 2: `Làm rõ thêm: vẫn được đối chiếu archive khi tôi yêu cầu đúng phạm vi lịch sử.` | Clarification tương thích không tự chứng minh câu trước sai; acknowledgment không thành endorsement fact ngoài đời. |
| S08 | `Answer in English: explain why an attempted save is different from a confirmed save, using a hypothetical example only.` | Language override dùng English; giữ attempted/completed theo evidence; không tự tuyên bố đã save hay tạo negative alternative không phục vụ giải thích. |
| S09 | `Giả sử giá một dịch vụ là 5 đơn vị để minh họa phép tính 3 tháng, không khẳng định giá thật. Chỉ tính theo giả định.` | Lý luận conditional từ input đủ dùng, không mở fact-check không liên quan; giữ giả định khác verified price. |
| S10 | Review tĩnh trước live: chỉ có file CI v2.6; bỏ metadata ngoài tên/version/status. Đối chiếu core và Router với contract. | Core material vẫn nằm trực tiếp trong file; Router không tải governing CI/Global. Nếu required logic chỉ tồn tại ở external base: `HOLD UP: BASE SEMANTICS MISMATCH`, không gọi đây là pass self-contained. |

Ca chống của guard skill: khi task chỉ yêu cầu audit metadata `upstream_base` của FTH, phải đọc intent/runtime contract FTH trước; metadata bảo trì không đủ kích signal hoặc cho phép sửa FTH. Với proposal Revamp đưa `load_governing_ci` vào Router để bù core thiếu, phải phát signal, chỉ sửa trong authorized scope; khi chỉ audit thì không ghi file. Đây là review tình huống, chưa phải lượt thực thi skill độc lập.

Nếu cần phân biệt đóng góp core bằng ablation, tạo bản thử riêng từ 2.6, chỉ bỏ các câu grounding/operation-stage (giữ mọi câu khác), ghi exact diff/hash và chạy lại S01–S06 với cùng model/cấu hình/input trong chat mới tương đương. Không dùng bản ablation làm baseline hoạt động. Kết quả chỉ khảo sát nhóm control bị bỏ, không chứng minh nguyên nhân duy nhất của lịch sử regression. Chưa có quyền/điều kiện tương đương thì NOT RUN; không coi đọc spec là live execution.
