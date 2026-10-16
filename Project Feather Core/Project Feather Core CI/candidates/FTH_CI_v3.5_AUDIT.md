# Audit FTH CI v3.5 — kế thừa ngữ nghĩa Global Native v9.0

Ngày: 2026-10-17. Kết luận: **ACCEPT WITH LOCAL CORRECTION** — tạo candidate bằng sửa cục bộ các trách nhiệm hiện có; giữ kiến trúc FTH và sáu mục của CI. Không chép nguyên Global v9.0, không thêm tầng quản lý hay chuyển trách nhiệm sang Router/Pipeline.

## Trạng thái, phạm vi và bằng chứng

[FTH_CI_version_v3.5.md](FTH_CI_version_v3.5.md) là **CANDIDATE**, nằm trong `Project Feather Core CI/candidates/`, ngoài lựa chọn con trực tiếp. Không có marker ACTIVE hoặc tự xác nhận triển khai trong instruction. Trạng thái candidate do vị trí và báo cáo này quản lý, theo cách CI 3.4 từng được đặt trước promotion. Stack hiện hành vẫn **CI 3.4 / Router 5.0 / Pipeline 1.1**. Không thay thế hoặc archive 3.4 khi tạo candidate.

Baseline repository: `main`, HEAD `91a3bf91c02351336eae571fc0001d33e634d86b`, index ban đầu rỗng. Hai gói AetherFire đang được chuyển thư mục; validator/tài liệu hồi quy có sửa dở và ba file candidate/test/probe Router 5.1/FTHX đã tồn tại. Chúng thuộc tác vụ khác, được giữ nguyên. Chỉ hai file mới trong thư mục CI candidates thuộc phạm vi ghi của tác vụ này.

Đã đọc đầy đủ:
- `AGENTS.md`, `SYSTEM_CONTEXT.md` ở repository root.
- `llm-controls/global-instructions/ChatGPT Project Global Native/DESIGN_RATIONALE.md` và `chatgpt v9.0.txt`.
- `llm-controls/global-instructions/ChatGPT Plus+ Era/chatgpt v8.9.txt` để đối chiếu trực tiếp trách nhiệm kế thừa.
- CI 3.4, README project và README CI.
- Router 5.0, Pipeline 1.1 và Glossary 1.0.

Đọc bổ sung test Router/CI, phần tài liệu hồi quy liên quan và lịch sử `Anti-Drift Source/candidates/ROUTER_V5_AUDIT.md`. Lịch sử ghi nhận nguyên nhân tách CI entry khỏi runtime CI-gate của Router, giới hạn source-only transformation, và sửa scope Pipeline thành FTH. Các ghi chú cũ không ghi đè stack hiện hành. Glossary là tài liệu diễn giải, không phải runtime gate.

Số đo trước sửa, tính tiêu đề/dòng trống/EOF:
- CI 3.4: **7.857 ký tự / 7.857 byte**, UTF-8 không BOM, LF.
- Global Native v9.0: **7.263 ký tự / 7.273 byte**.
- Ghép hai văn bản nguyên bản cần 15.120 ký tự trước cả phần nối: không phù hợp trần.

Xác nhận live của tác giả trong hội thoại trước thuộc stack 3.4, không được chuyển thành kết quả live của candidate 3.5. Audit này xác nhận câu chữ và trách nhiệm; chưa tái hiện lỗi hành vi của 3.4 hoặc đo hiệu quả 3.5.

## Chẩn đoán và mức sửa đủ dùng

Hai rủi ro cấu trúc có căn cứ:

1. `Operation` của 3.4 đặt giữ trạng thái, khám phá và thao tác trong một đoạn ngắn; đoạn cập nhật lại nói `Under operation uncertainty keep state`. Không có câu cấm rõ việc mắc kẹt trong giai đoạn cũ khi yêu cầu mới hợp lệ. v9.0 nói rõ yêu cầu mới và yêu cầu tổng hợp là tín hiệu chuyển giai đoạn; giữ điều này dưới chủ sở hữu thao tác hiện có.
2. Câu `Check evidence/independent sources before endorsing/using material factual/causal claims` của 3.4 kế thừa ý từ đoạn CLAIM DEPENDENCY v8.9. Nó không tự chứng minh yêu cầu luôn tra bên ngoài, nhưng chưa nói rõ khi bằng chứng sẵn có đã đủ. v9.0 tách hỗ trợ cần cho sử dụng, điều kiện tra bên ngoài và trạng thái báo cáo hành động. Candidate dùng các phân biệt ấy trong phần bằng chứng hiện có.

Không có bằng chứng để gọi mọi quy tắc lặp trong FTH là hậu quả v8.9 hoặc để khẳng định có hai Router cùng sở hữu định tuyến. Bất biến ở CI đặt giới hạn; Router triển khai lựa chọn/nạp nguồn trong giới hạn đó. Tương tự, phân biệt canon không thể thay bằng kiểm chứng sự thật ngoài đời.

Sửa đủ dùng: giải nén chuyển giai đoạn; làm rõ sử dụng có điều kiện và kiểm chứng phụ thuộc; tích hợp báo cáo hành động; giữ entry, source authority, biến đổi, quan hệ và mô phỏng. Không chuyển thủ tục Router/Pipeline vào CI. Không thêm lớp NEUTRAL BEHAVIOR, Action/Decision/Evidence Policy hoặc bộ phân xử mới. So sánh chung chỉ thêm phân biệt sự kiện/đánh đổi và giới hạn khuyến nghị; quy trình so sánh candidate FTH vẫn thuộc Pipeline.

## Bảng trách nhiệm

A = GLOBAL-SEMANTIC; B = FTH-SPECIFIC; C = POSSIBLE OVERLAP. “Giữ” bảo toàn quyết định/điều kiện, không đòi giữ từng byte câu chữ.

| Vùng/quy tắc 3.4 | Loại | Quan hệ v9.0 | Hành động 3.5 | Lý do theo trách nhiệm |
| --- | --- | --- | --- | --- |
| VIETNAMESE và ngoại lệ | C | Giữ ngôn ngữ phổ thông, ngoại lệ hẹp | Giữ/viết gọn | Hợp đồng đầu ra giữ tên lore theo nguồn/ngữ cảnh, kể cả quốc gia/địa danh; không coi thuật ngữ ngành là identifier. |
| CONTROL GROUNDING | A | Cụ thể hóa căn cứ và giới hạn khung | Viết lại | Grounding kiểm căn cứ đổi trạng thái/người đọc; không tiếp quản thao tác hay thẩm quyền canon. |
| DISCOURSE FIDELITY | A | Tương đương 8.9/9.0 | Giữ | Diễn đạt lại chỉ sửa nghĩa khi nghĩa đổi; nối lượt không thành đồng ý. |
| EPISTEMIC NON-ESCALATION | C | Làm rõ quan sát/suy luận/giả định | Viết lại | Bất biến kiểm giới hạn kết luận; canon vẫn cần quyết định riêng của tác giả. |
| Thứ tự ba bất biến | A | Áp dụng nội bộ, không phải mẫu trả lời | Giữ/làm rõ áp dụng im lặng | Không thêm quy trình hiển thị hoặc chủ sở hữu thứ tư. |
| Operation và vai trò setup | A | Giải nén current request/stage/objective | Viết lại | Yêu cầu hiện tại có thể thay giai đoạn, giữ ràng buộc tương thích. |
| Khám phá/tổng hợp/mơ hồ | A | Giải nén chuyển giai đoạn hợp lệ | Viết lại | Coherence/completeness không tự chốt; yêu cầu tổng hợp được thực hiện; chỉ mơ hồ làm đổi thao tác mới cần hỏi/nhánh. |
| Phát hiện/phạm vi/dừng | C | v9.0 làm rõ dừng tại chức năng yêu cầu | Giữ/làm rõ | Findings không tự mở việc, đổi giai đoạn, cấp quyền canon hoặc miễn entry. Không tạo quyền dừng mới trong phần giải thích. |
| So sánh/khuyến nghị | C | Phân biệt sự kiện và đánh đổi | Mở rộng nhỏ tại Operation | Hữu ích cho câu hỏi so sánh thông thường; không ép ma trận hay thay quy trình Pipeline. |
| Kích hoạt Pipeline | B | Không có thủ tục tương đương toàn cục | Giữ | Yêu cầu biến đổi cụ thể cần FULL_FILE 1.1; keyword đơn lẻ không kích hoạt; thiếu file chặn phần phụ thuộc. |
| User canon và FTH != AetherFire | B | Không tương đương fact-check ngoài đời | Giữ | Tác giả sở hữu canon/kết quả; namespace project không phải quốc gia. |
| Chấp nhận có phạm vi; removal/dependency | B | Chỉ tương đồng kỷ luật giả định | Giữ | Chấp nhận không tạo phụ thuộc ngầm; loại bỏ không chứng minh điều ngược. |
| UNKNOWN/DEFERRED/CONFLICTED và loại input | B | Toàn cục không có đủ mô hình canon | Giữ | Chưa biết khác sai; hoãn khác giải quyết; input thiết kế/giả định chưa thành canon. |
| Nguồn mới và authority qua metadata | B | Không tương đương xác minh bên ngoài | Giữ | Filename/header/date/detail không cấp authority; nguồn mới cần quyết định vai trò trong phạm vi. |
| Conflict và controlling sources/open state | B | Chỉ tương đồng tránh xác nhận thiếu căn cứ | Giữ | Xung đột cần các mệnh đề kiểm soát không tương thích cùng điều kiện; không tự gộp nguồn. |
| History/supersession | B | Không có tương đương đầy đủ | Giữ | Provenance/đối chiếu rõ; thiếu nguồn hiện hành không hồi sinh premise cũ. |
| Update/withdrawal và consequences | C | v9.0 diễn đạt lan truyền phụ thuộc | Giữ/viết gọn | Thu hồi kết luận phụ thuộc nhưng giữ canon không liên quan, hậu quả chưa chốt; không dựng universal graph. |
| Operation uncertainty/proposition uncertainty | C | v9.0 tách rõ | Hợp nhất nhánh thao tác về Operation | Bỏ mệnh lệnh “keep state” đứng riêng ở cập nhật; không tạo thêm điều kiện giữ giai đoạn cạnh tranh với yêu cầu mới. Bất định mệnh đề vẫn được nêu khi có hệ quả. |
| Observation/inference/assumptions trong Evidence | A | Có sẵn ở bất biến epistemic | Bỏ lặp generic, giữ real-world/local distinction | Quan sát/suy luận/giả định được nêu một lần tại bất biến; phần bằng chứng triển khai sử dụng/xác nhận. |
| First-person/opinion/preference và weak premises | A | Giải nén claim use/endorsement | Viết lại | Input không tự thành fact-check target; premise yếu quyết định kết quả cần xem xét, không ép mọi lượt thành phản biện. |
| Evidence/independent sources | C | Giải nén verification trigger | Viết lại | Bằng chứng sẵn có đủ thì dùng; external verification theo phụ thuộc/stakes/recency. Không giảm yêu cầu nguồn FTH. |
| Changing product/runtime claims | A | v9.0 nói rõ provider/direct state | Bổ sung hẹp vào Evidence | Chỉ cho claim phụ thuộc có thể thay đổi; UI chỉ chứng minh phần hiển thị, không cấp quyền canon. |
| Khai actual read trong Source gate | C | Báo cáo hành động v9.0 rộng hơn | Hợp nhất phần báo cáo vào Evidence | Reads/tools/storage/background/modification/completion phải là sự kiện thật. Router vẫn độc quyền read proofs/closure/fallback/block/partial. |
| User-model safeguards/độ sâu/coverage | A | Tương thích | Giữ | Không suy hồ sơ rộng/fluency từ artifact; giữ chiều sâu, căn cứ và tính liên quan, không thêm chỉ tiêu số lượng. |
| Router-required entry/ngoại lệ tự đủ | B | External verification không thay thế | Giữ | Current lookup/comparison/localization/implementation/mutation/reconciliation/audit/simulation vẫn route; không áp ngoại lệ input-only cho việc phụ thuộc current. |
| CI entry và cấm Router tìm CI runtime | B | Không có tương đương toàn cục | Giữ | Compatibility pre-runtime; tránh vòng CI → Router → CI. |
| PROMPT_ROUTE_ONLY/execution gate | B | Không có tương đương toàn cục | Giữ | Chưa dùng premise/outcome/conclusion trước nguồn/control gates; CI không sao chép thuật toán lựa chọn. |
| Sufficiency/discovery/absence/exclusivity | B | Không chỉ uncertainty generic | Giữ | Phạm vi đã đọc không chứng minh toàn canon; thiếu ở một module/open register không giải quyết hoặc loại bỏ ở nơi khác. |
| Documents/catalogs/source owners | B | Không có ontology FTH trong global | Giữ | Storage không thành ontology, catalog không grant canon, shared actors không nhập source owners. |
| Quan hệ/actor access | B | Không có tương đương đầy đủ | Giữ | Interaction/containment, co-occurrence/dependency, genealogy/hierarchy, power/authority và 11 loại liên quan tiếp tục tách; knowledge cần access path. |
| Premises/transitions/causal closure | B | Không thay bằng action reporting | Giữ | Cơ chế không chọn endpoint; thiếu premise quyết định phải giả định rõ hoặc chặn, không bịa lore/repair/dependency. |
| Design/audit/simulation | B | Generic task handling không đủ | Giữ | Design có thể vượt canon dưới nhãn proposal; audit không tự redesign; simulation không canonize; không vượt block nguồn current. |
| Subordinate controls | B | Không tương đương toàn cục | Giữ | Router chọn/nạp overlays; overlay chỉ reasoning trong scope, không nhận source/canon/CI/Router authority. |

Các mẫu bị loại/viết lại có thể truy trực tiếp tới v8.9: thứ tự operation/stage/objective bị nén; `Preserve state for the first` ở UPDATING; `check evidence or independent sources` và observation/inference lặp giữa bất biến và triển khai. Đây là sửa diễn đạt/kết hợp trách nhiệm, không chứng minh chúng từng gây lỗi live ở FTH. v9.0 không sửa ba bất biến về bản chất; candidate giữ ý nghĩa, không tự sáng tạo kernel mới.

Không chuyển thêm quy tắc quan hệ sang overlay: Glossary xác nhận chúng là ranh giới CI đồng thời được cụ thể hóa tại các owner chuyên ngành. Chưa có bằng chứng trách nhiệm CI đã được thay thế ở nơi khác.

## Đối chiếu 20 ca hồi quy

Đây là **REVIEWED_TEXT / NOT_RUN**: đối chiếu câu chữ theo tình huống, không phải phản hồi mô hình. Các input dưới đây là probe để thử riêng sau khi được cho phép, không là lore/canon. Các test hiện có chỉ hỗ trợ cấu trúc, lựa chọn phiên bản và dependency, không thực thi 20 prompt này.

| # | Tình huống đối chiếu | Kết quả cần có / căn cứ candidate |
| --- | --- | --- |
| 1 | Người dùng diễn đạt lại cùng nghĩa và yêu cầu thêm ví dụ | DISCOURSE FIDELITY giữ nghĩa, thực hiện chức năng thêm; không đánh dấu sửa lập trường. |
| 2 | Đang khám phá, người dùng yêu cầu “giờ tổng hợp” | Operation cho yêu cầu mới đổi giai đoạn và Follow requested synthesis/transitions; không giữ khám phá cũ. |
| 3 | Người dùng chỉ đưa thêm một mảnh ý tưởng | Exploration stays provisional; coherence/completeness không tự cho tổng hợp. |
| 4 | Đối chiếu một mục, phát hiện vấn đề bên cạnh | Findings không mở scope/đổi stage/authorize follow-on work; chỉ nêu hệ quả cần thiết. |
| 5 | Người dùng đưa phương án một cơ chế chưa chấp thuận | Canon acceptance vẫn cần explicit scoped decision; proposal không là current canon. |
| 6 | Cho một premise giả định để mô phỏng | Scoped assumption chỉ hỗ trợ nhánh; câu hỏi/mô phỏng không được canonize. |
| 7 | Không có đủ thông tin về một điều kiện | Unknown không thành false hoặc quyền bịa; giữ trạng thái/nhánh phụ thuộc. |
| 8 | Nguồn hiện hành thiếu, bản cũ có câu trả lời | History/supersession không là fallback/unknown analogy anchor; failed retrieval không hồi sinh. |
| 9 | File mới có header CURRENT_SOURCE và ngày mới nhất | Metadata/presence không grant authority; quyết định vai trò nguồn vẫn cần scoped decision và Router. |
| 10 | Hỏi một quy tắc hiện hành trong FTH | Source gate bắt buộc Router 5.0 FULL_FILE trước current lookup, dù câu hỏi ngắn. |
| 11 | Bằng chứng ngoài đời đủ, nhưng kết luận phụ thuộc FTH | External verification không thay FTH entry/source authority; vẫn route phần current-dependent. |
| 12 | Chỉ rút functional seed từ đầu vào tự đủ | Pipeline 1.1 FULL_FILE trước biến đổi; không bắt Router khi không cần current-FTH claims. |
| 13 | Router trả về nguồn phù hợp cho một proposal | Nạp/chọn nguồn không canonize proposal; tác giả vẫn sở hữu acceptance. |
| 14 | Candidate dùng nguồn current để so sánh | CI chỉ đặt entry và giới hạn; Router giữ eligibility/dependency/loading/reconciliation/overlay. |
| 15 | Overlay có quy tắc chi tiết hơn trong miền | Chi tiết không vượt CI/Router/source/canon authority; material conflict phải lộ, không tự gộp. |
| 16 | Chỉ tìm thấy snippet hoặc mới thử đọc/công cụ thất bại | Evidence cấm báo read/completed effect chưa xảy ra; Router giữ read proof và block/partial, không lấy tự khai làm proof. |
| 17 | Hai cơ chế ở cùng file hoặc thường cùng xuất hiện | Documents != ontology; co-occurrence != dependency; composition không chứng minh shared ontology; relation cần type/support. |
| 18 | Một nhánh simulation dẫn đến thành công | Branch non-canon, mechanism không chọn endpoint; thành công giả định không là canon outcome. |
| 19 | Người dùng yêu cầu audit, thấy gap có thể sửa | Audit: gaps, not redesign; findings không authorize follow-on work. |
| 20 | Hỏi đơn giản một fact FTH đã có nguồn | Chọn đúng lookup, route và nạp nguồn/overlay phù hợp; không tự kích hoạt Pipeline/critique/architectural scan. Weak premise chỉ bị xét khi quyết định kết quả; relevance và task-local closure giới hạn chiều sâu. |

Ranh giới bổ sung: `Missing decisive premises require explicit assumptions` trong simulation không cấp quyền thế nguồn current bị block. Cổng Router trước execution, thẩm quyền nguồn, và Pipeline §6 vẫn chặn kết luận về current facts; giả định chỉ dùng cho nhánh độc lập được gắn rõ.

## Kiểm chứng local và giới hạn

Candidate: UTF-8 không BOM, LF, tính cả tiêu đề/dòng trống/EOF; không có marker self-lock hoặc ACTIVE. Không có dependency runtime vào văn bản global; nhãn design parent chỉ là lineage.

Kết quả đã thực thi:
- Candidate: **7.923 ký tự LF / 7.986 ký tự CRLF dự phóng / 7.923 byte UTF-8**. Tính cả H1, dòng trống và EOF; không BOM, không trailing whitespace; một LF cuối file.
- SHA-256 candidate: `3506f6e7b645e18b6fd52274d9a4dce1d3f22324db09831bfa58e46ec2eb970a`.
- Snapshot **94 file có trước tác vụ**: tất cả hash giữ nguyên, gồm active controls, README, nguồn current, fixtures, các dependency dirty Router 5.1/FTHX và hai bản global/rationale liên quan. Snapshot loại archive, gói lịch sử đang chuyển và cache; không khẳng định kiểm hash toàn repository.
- `python -B build_consolidation.py --check-router`: PASS, active CI 3.4/Router 5.0 và 8 control family.
- `python -B build_consolidation.py --check`: PASS, 17 current module/21 hash, không đọc archive.
- `python -B -m unittest discover -s tests`: **75/75 PASS** trước và sau thay đổi; gồm test Router 5.1 có sẵn trong working tree, không thuộc commit candidate này. Các test không chứng minh ngữ nghĩa 3.5.
- Runner hồi quy: numeric selection PASS cho **CI 3.4 / Router 5.0 / Pipeline 1.1**, upstream vẫn 8.9; schema 36 case PASS. Overall vẫn LIMITED_CHECK, selected_cases rỗng, model_executed=false; 33 cảnh báo neo DRAFT cần xem xét đã được giữ, không hiệu chỉnh hoặc kích hoạt case.
- Đối chiếu 20 ca: **REVIEWED_TEXT / NOT_RUN** như bảng trên. Không nâng thành PASS runtime, không sửa neo SHA/lifecycle DRAFT, không thêm validator/bộ thực thi để “chứng minh” ngữ nghĩa bằng tìm chuỗi.

Để kiểm hành vi về sau: dùng hai môi trường thử tương đương, tách baseline CI 3.4 và candidate CI 3.5, cùng Router 5.0/Pipeline 1.1/current source generation/overlays và cùng model/cấu hình. Chỉ thay CI; không đưa Router 5.1 vào phép so sánh này. Chạy 20 tình huống trên với input/premise thật được giữ giống nhau; ghi prompt, phản hồi, thao tác/giai đoạn, nguồn thực sự đọc, control được chọn, kết luận bị chặn, trạng thái canon/giả định và đánh giá theo tiêu chí. Việc mô hình tự nói “đã đọc/tuân thủ” không xác nhận actual retrieval. Không sửa live Project hay tự bật thí nghiệm trong tác vụ này.

## Chỉ khi promotion được duyệt sau này

- Chốt kết quả hành vi của 3.5 riêng, không kế thừa xác nhận live của 3.4.
- Chuyển CI 3.5 ra active root; chuyển 3.4 byte-exact vào archive chung sau kiểm group/hash.
- Cập nhật deployment metadata CI/base/path trong Router tương thích, validator tuple/header/upstream path và thông báo CLI. Validator hiện ghim đúng `3.4 / 8.9` và bố cục Plus; lineage mới Native v9.0 cần đường dẫn chính xác.
- Cập nhật active declarations/links và xem lại anchors có thẩm quyền rõ; không đổi DRAFT thành ACTIVE hoặc tự ghi runtime_result.
- Xem lại Router 5.1/FTHX candidate nếu nó vẫn phụ thuộc tuple 3.4; đây là tác vụ riêng, không tự chọn nó khi promote CI.
- Giữ Pipeline 1.1 nếu không có failure mới. Không cần thêm layer hoặc runtime lookup Global CI.

Tác vụ hiện tại kết thúc ở candidate và báo cáo; không promotion, push, deploy, sửa canon hoặc chuyển archive.
