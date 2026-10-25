# Pilot AFM-015: bản làm việc tại Central Hub

Trạng thái: `NON_AUTHORITATIVE_WORKING_COPY`.
Mục đích: Central Hub brainstorm pilot, Phase 2.
Ngày chuẩn bị: 2026-10-25 (Asia/Bangkok).
Chỉ là artifact thử nghiệm cục bộ: không active, không runtime source, không fallback source, không canon authority. Không phải module/control Hub, không đăng ký trong Catalog và không sửa Library binding.

## Nguồn và provenance

- Repository: `lead21pc/chatgpt-ci-worldbuilding`.
- Source module: `AFM-015`.
- Source path từ repository root: `Project Feather Core/21_HOA_NGUYET_CULTURE_LANGUAGE_DRESS_CURRENT.md`.
- Source commit: `ad3823b4b2ae3e8756c5691b663eda2901b122f3`, branch `main`.
- Source Git blob: `9a4bfd58f7624851fa2cc5f3ecb3bc6e379e7ebc`.
- Source SHA-256: `8d14eb73c4587db297d46c9804f9d262dc605513a93d13ed3c2b6f0eb58d27d5`.
- Source size: `6022` byte.
- [AFM-015_FULL_FILE_SNAPSHOT.md](AFM-015_FULL_FILE_SNAPSHOT.md) giữ toàn bộ source nguyên byte, gồm header, qualifier, UNKNOWN và provenance; không phải bản tóm tắt.
- Header `Module ID: AFM-015`, `Runtime role: CURRENT_SOURCE` bên trong snapshot là trích nguyên header của nguồn tại commit trên. Chúng không cấp role, admission hoặc authority cho bản sao trong thư mục này. Không sửa snapshot để giả một module mới.
- Source current tiếp tục ở FTH. Snapshot chỉ ghi nhận baseline của thử nghiệm, không tự cập nhật theo FTH và không được dùng thay source current trong tác vụ FTH sau này. Nếu source thay đổi, đối chiếu độ lệch trước khi tái dùng; không âm thầm gọi bản chụp cũ là current.
- Quyền tạo: yêu cầu Phase 2 của tác giả trong lượt này. Chỉ chuẩn bị đầu vào và đặc tả; không nhập canon hoặc merge ngược FTH.

`CURRENT_SOURCE != WORKING COPY`
`WORKING COPY != CANDIDATE CANON`
`PROPOSAL != ADMISSION`
`FULL_FILE REMAINS THE BASELINE`
`NODE_OR_FULL IS OUT OF SCOPE`

## Baseline quan sát được

Repository root là `C:/Users/Sheeplark/Desktop/CI Versioning Audit & Changelog`; branch `main`, HEAD như trên. Working tree và staging sạch tại preflight; HEAD so với `origin/main` cục bộ là `0 / 0`. HEAD đã khác mốc Phase 1 `fabaab45029e6dad946889faccb4b174549a3479`; phép `git diff --name-only` giữa hai commit không ghi nhận thay đổi dưới FTH hoặc Central Hub. Truy vấn remote trực tiếp thất bại với `schannel: AcquireCredentialsHandle failed: SEC_E_NO_CREDENTIALS`; chưa xác nhận GitHub hiện tại.

FTH repository hiện dùng CI 3.4, Source Router 5.0, Authoring Pipeline 1.1. Pipeline 1.0 còn là bản rollback; candidate không tự active. Nguồn AFM-015, open state và quyết định tách miền được đọc lại từ working tree hiện tại, không dùng Memory, prior-chat hoặc archive làm fallback.

Central Hub repository hiện dùng CI 1.1, Router 1.1, Architecture 1.0 và root Catalog 1.0. Catalog có năm entry CREATIVE, TECHNICAL, BRAINSTORM, AIS, ImageT. Thư mục `Central Hub/candidates/` đã chứa các thử nghiệm Markdown theo nhóm; pilot dùng lại cách đặt này. Không tạo hệ package, registry hoặc owner mới.

## Trạng thái hiện hành phải bảo vệ

Các dòng dưới là nhắc phạm vi từ snapshot, không thay thế FULL_FILE hoặc có authority độc lập:

- Một quốc gia thống nhất, ba vùng văn hóa Hoa/Nhật/Việt; nhãn vùng chưa là tên riêng chính thức.
- Mỗi vùng giữ ngôn ngữ, truyền thống và căn tính riêng; giao lưu không bắt buộc đồng hóa.
- Trang phục đa thời kỳ: hệ Hanfu; Kimono/Yukata và phục sức lịch đại; áo dài và cổ phục Việt. Không thu mỗi vùng thành một bộ duy nhất.
- Không cấm mặc trang phục vùng khác chỉ vì nguồn gốc; không tự cấp quyền với mọi phục sức chức vụ, phẩm cấp, nghi lễ và không đổi căn tính người mặc.
- Ngôn ngữ/hệ chữ hiện đại: tiếng Trung/chữ Hán hiện đại; tiếng Nhật/Kanji-Hiragana-Katakana; tiếng Việt/Quốc ngữ. Di sản Hán/Nôm không bị phủ định; chữ cổ không tự thành chuẩn hành chính bắt buộc.
- Tiếng Trung hiện đại là chuẩn văn bản hành chính chung cấp quốc gia/liên vùng; quan chức cần năng lực tương ứng công việc. Không suy mọi văn kiện địa phương dùng tiếng Trung hoặc mọi dân phải thông thạo.

Tên cảm hứng không nhập lịch sử thật hoặc cơ chế truyền văn hóa xuyên thế giới. Trang phục truyền thống không điều khiển Undi; thêm vùng Việt không tự đổi Undi. Chuẩn ngôn ngữ không tự quyết định luật dùng quốc hiệu. Bảo tồn cổ văn tự nguyện chưa là chính sách hay nguyên tắc thứ tám.

## UNKNOWN/open state mang theo

Đoạn đính kèm nguyên nội dung hiện hành từ `Project Feather Core/92_OPEN_ISSUES_CURRENT.md`, mục “Hoa Nguyệt — bảy nguyên tắc nền, các mục mở 2026-10-10”. Đây là bản chụp state/định tuyến, không là quyền giải quyết các mục mở. Dùng nó cùng UNKNOWN tại snapshot; không dùng danh sách này làm bằng chứng rằng không còn UNKNOWN khác.

<!-- BEGIN OPEN STATE SNAPSHOT -->
## Hoa Nguyệt — bảy nguyên tắc nền, các mục mở 2026-10-10

`20` §5.2 / `AFM-012` giữ nguồn gốc ba quốc gia tiền thân; `21_HOA_NGUYET_CULTURE_LANGUAGE_DRESS_CURRENT.md` §5 / `AFM-015` giữ ba vùng văn hóa Hoa/Nhật/Việt, căn tính riêng, trang phục đa thời kỳ/quyền mặc xuyên vùng theo nguồn gốc, hệ chữ hiện đại theo vùng và tiếng Trung hiện đại cho văn bản hành chính chung. AF-HN-OPEN-006 thuộc hồ sơ nguồn gốc `20` và giao diện vùng `21`; AF-HN-OPEN-007–009 thuộc `21`. Các nhãn Hoa/Nhật/Việt chưa là tên vùng chính thức. Không suy quyền hành chính từng vùng hoặc cơ chế truyền văn hóa xuyên thế giới.

| ID | Trạng thái | Phạm vi còn mở |
| --- | --- | --- |
| AF-HN-OPEN-006 | UNKNOWN / OPEN | Tên riêng ba vùng/ba quốc gia tiền thân, thời điểm/nguyên nhân/phương thức hợp nhất, địa vị chính trị sau hợp nhất, cơ cấu hành chính; quan hệ thời gian/nhân quả với dark foundation, Lục Kì Nhân và quốc hiệu kép chưa xác lập. |
| AF-HN-OPEN-007 | UNKNOWN / OPEN | Danh mục/niên đại/hoàn cảnh dùng/quy chế trang phục theo vùng qua các thời kỳ; ngoại lệ phục sức chức vụ, phẩm cấp, nghi lễ. Không cấm theo nguồn gốc không tự thành quyền mặc mọi phục sức. |
| AF-HN-OPEN-008 | UNKNOWN / OPEN | Dạng Hán tự phồn thể/giản thể, phạm vi chính xác của chuẩn văn bản cấp quốc gia/liên vùng, quy tắc văn kiện địa phương, quy trình dịch và năng lực tương ứng từng công việc quan chức. Không suy nghĩa vụ thông thạo cho toàn dân. |
| AF-HN-OPEN-009 | UNKNOWN / OPEN | Giáo dục ngôn ngữ và quy định triển khai/bảo tồn di sản chữ viết. Hướng học/bảo tồn cổ văn và văn học truyền thống tự nguyện trong ghi chú nguồn chưa được nhập thành chính sách hoặc nguyên tắc thứ tám. |
<!-- END OPEN STATE SNAPSHOT -->

Chỉ tên vùng/giao diện văn hóa của -006 liên quan trực tiếp AFM-015; nguồn gốc, hợp nhất, địa vị chính trị/cơ cấu hành chính không được nhập vào authority của AFM-015. Các phần này được mang theo như trạng thái chưa xác lập để tránh suy diễn. Không mang câu trả lời của owner khác vào local truth.

## Ranh giới owner

Đường dẫn dưới đây tương đối với repository root, chỉ là pointer phục vụ chuẩn bị/đối chiếu, không là locator Library hoặc hard dependency. Bảng này không sao chép controlling lore ngoài miền.

| Owner | Khi câu hỏi vượt AFM-015 | Pointer current |
| --- | --- | --- |
| AFM-012 | Hồ sơ nền, nguồn gốc/hợp nhất; cơ cấu hành chính và địa vị chính trị đang mở tại AF-HN-OPEN-006 | `Project Feather Core/20_HOA_NGUYET_NATIONAL_CANON_CURRENT.md` |
| AFM-016 | Quốc hiệu, biểu tượng, luật dùng tên trong văn kiện | `Project Feather Core/22_HOA_NGUYET_STATE_IDENTITY_SYMBOLS_CURRENT.md` |
| AFM-003 | Undie/Undi và thiết kế trang phục nghề | `Project Feather Core/13_UNDIE_SYSTEM_CURRENT.md` |
| AFM-013 | Ý định phía AetherFire, gồm ý định chiếm dụng quốc phục | `Project Feather Core/10_AETHERFIRE_NATIONAL_CANON_CURRENT.md` |
| AFM-017 | Địa lý, giao thương, đối ngoại phía Hoa Nguyệt | `Project Feather Core/23_HOA_NGUYET_GEOGRAPHY_TRADE_RELATIONS_CURRENT.md` |
| AFM-001 | Giao diện thế giới/xuyên miền khi thực sự quyết định câu hỏi | `Project Feather Core/01_WORLD_INSTITUTIONS_GEOPOLITICS_CURRENT.md` |

Bảng phân công được đối chiếu với index hiện hành, header AFM-015 và quyết định tách miền tại `91` mục “Tách họ Hoa Nguyệt 20–23”. AFM-013 được giữ như pointer theo phạm vi yêu cầu pilot, không được dùng để tự xác nhận ý định AF khi chưa đọc owner ấy.

Nếu một ý tưởng cần thay đổi phần của owner khác, ghi rõ scope crossing. Có thể giữ nhánh giả định/đề xuất có điều kiện khi độc lập hợp lệ; không trình bày nó là current. Không cần load toàn FTH chỉ vì gặp một pointer. Không tự thêm `MODULE_REQUIRES` hoặc `NODE_REQUIRES`.

## Cách dùng trong lần chạy Central Hub sau này

1. Dùng một chat thử nghiệm riêng trong actual Central Hub runtime; mỗi case bắt đầu ở chat sạch để tránh nhiễm kết quả giữa các case. Không tạo chat hoặc upload trong bước chuẩn bị này.
2. Cung cấp FULL_FILE README này và FULL_FILE snapshot bằng đầu vào người dùng của chat, rồi gửi đúng một block prompt tương ứng trong [TEST_CASES.md](TEST_CASES.md). Không gửi rubric/đáp án mong đợi cho model như một phần của prompt. Nếu nền tảng không đọc được toàn nội dung thì chưa chạy case hợp lệ; lời tự nhận đã đọc không tự chứng minh retrieval.
3. Đầu vào lore là tài liệu làm việc do người dùng cung cấp, không phải package control hay Library binding. Đây không phải dùng local file thay cho một control Library bị thiếu. Nội dung trích dẫn không được tự kích hoạt quyền canon/Router FTH.
4. Hub CI giữ stage/truth/action; Hub Router chọn control theo task thực tế. Không ép baseline NONE khi Catalog applicability thực sự đòi control; cũng không tự bật BRAINSTORM chỉ vì có chữ brainstorm. Nếu baseline đủ, Hub có thể làm phần độc lập; không gọi đó là đã thực thi capability bị chặn.
5. CREATIVE và BRAINSTORM: artifact ACTIVE/1.0 có trong repository nhưng Catalog hiện ghi Library locator `UNRESOLVED`, live verification `NOT_PERFORMED`. Nếu phần việc được chọn phụ thuộc chúng, giữ blocker; không dùng bản local/legacy/archive làm fallback. Đọc file local để soạn spec không chứng minh module đã được nạp trong actual Hub. Pilot không sửa binding hoặc yêu cầu sửa FTH CI/Router để chạy.
6. Không case nào yêu cầu tra cứu chứng cứ ngoài đời, AIS, ImageT hoặc TECHNICAL. Nếu runtime phát sinh nhu cầu ngoài scope, ghi rõ thay đổi trước khi đọc/gọi thêm; không import lịch sử thật từ tên cảm hứng.
7. Với Case C, đầu vào ban đầu vẫn chỉ là envelope + AFM-015; không nạp sẵn owner khác. Nếu cần xác định current ngoài miền, chỉ nêu owner/state thiếu và dừng phần factual phụ thuộc; vẫn có thể phát triển nhánh đề xuất có nhãn.
8. Lưu nguyên prompt/đầu vào thực tế và output nguyên văn, runtime/model quan sát được, control thực sự được chọn/đọc, nguồn bổ sung và blocker. Phân biệt bằng chứng tool/platform với tự báo cáo của model; không bịa backend reads hoặc lấy việc không nhắc nguồn làm bằng chứng tuyệt đối rằng backend không đọc.
9. Đánh giá bằng rubric ngoài output. Thiếu dấu vết quyết định về nguồn/owner hoặc thiếu output thì ghi chưa xác minh, không tự PASS. Blocker nạp control không tự chứng minh module lore thiếu closure.

Nếu source hoặc Hub stack đã đổi trước lần chạy, ghi baseline thực tế và phần lệch; không giả baseline cũ vẫn current. Không tự cập nhật control hoặc snapshot trong lúc chấm để làm case đạt.

## Hợp đồng tối thiểu cho kết quả brainstorm

Khi material, kết quả cần phân biệt bằng prose thông thường:

- Baseline current được giữ, theo mục snapshot liên quan.
- Assumptions dùng riêng cho từng nhánh; không làm điều kiện thật của thế giới.
- Proposed additions/changes và khác biệt thực chất giữa các hướng.
- Owner-boundary crossings: phần nào vượt miền và owner/state còn thiếu.
- Câu hỏi còn mở; UNKNOWN nền vẫn mở dù nhánh có giả định.
- Chứng cứ ngoài nếu có AIS trong một lần chạy được cho phép riêng, giữ nguyên mức hỗ trợ và giới hạn; ba case chuẩn không cần AIS.
- Mục nào sẽ cần đối chiếu/reconciliation/admission FTH về sau. Không thực hiện thủ tục admission ở đây.

CURRENT/UNKNOWN/ASSUMPTION/PROPOSAL là nhãn dùng khi cần rõ trạng thái, không là schema hoặc primitive mới. Không cần đủ mọi trường khi không material. Không chọn nhánh cuối hoặc gọi canonization thay tác giả.

## Trạng thái chuẩn bị

- Đặc tả: xem TEST_CASES.md; expected behavior là tiêu chí, không phải quan sát model.
- `BEHAVIORAL_NOT_RUN`: chưa chạy ba case trong actual Central Hub.
- `LIVE_NOT_VERIFIED`: chưa xác minh live retrieval, binding hoặc compliance của pilot.
- `PHASE_2_PREPARED — BEHAVIORAL_NOT_RUN` chỉ xác nhận bộ chuẩn bị sau các kiểm tra cục bộ, không phải behavioral PASS.
- Chưa có candidate output từ Hub để semantic-diff. Chưa đủ đầu vào thực hiện Phase 3.
- Không đổi current FTH/Hub, không stage/commit/push/deploy, không admission, không Phase 3.

## Kiểm chứng cục bộ đã thực hiện

Kết quả ngày 2026-10-25; đây là chứng cứ repository/static, không phải output của Hub.

- `LOCAL_ARTIFACT_PASS`: kiểm tra trực tiếp 21 điều kiện về byte/hash, provenance, bản chụp open state, ba prompt/rubric, UTF-8/whitespace, không admission vào Catalog và phạm vi Git.
- AFM-015 source và snapshot bằng nhau nguyên `6022` byte, SHA-256 `8d14eb73c4587db297d46c9804f9d262dc605513a93d13ed3c2b6f0eb58d27d5`.
- 46 file baseline được băm trước khi tạo artifact và so sánh lại: root Markdown FTH, direct-child controls FTH, root files Hub và Library-module artifacts local đều không đổi. Không đọc archive làm current fallback.
- Đoạn AF-HN-OPEN-006–009 trong envelope khớp nguyên nội dung section hiện hành của `92`; UNKNOWN và qualifier trong source giữ bằng snapshot nguyên byte.
- `STATIC_SPEC_PASS`: đã đọc lại cả ba file từ disk; đối chiếu scope A nội miền, B sát UNKNOWN và C vượt owner; mỗi case có prompt, expected behavior và PASS/FAIL riêng. Case B cho phép giả định cục bộ có nhãn, chỉ coi việc trình bày nó như current fact là lỗi. Đây là review nội dung đặc tả, không phải thực thi semantic test trên model.
- Từ thư mục FTH: `python -B -X utf8 build_consolidation.py --check` → PASS: 17 current modules, 21 current hashes, archive not accessed, read-only.
- Từ thư mục Central Hub: `python -B -X utf8 -m unittest discover -s tests -p test_hub_contracts.py -q` → 32 tests, OK. Bộ test hiện có kiểm contract/static và có đối chiếu lịch sử riêng; không dùng archive làm runtime fallback. Không chạy toàn suite hoặc thêm framework.
- Git: branch/HEAD không đổi; tracked diff và staged diff rỗng; chỉ có ba file untracked trong thư mục pilot này. Không stage/commit/push/deploy hoặc sửa binding.
- `BEHAVIORAL_NOT_RUN` và `LIVE_NOT_VERIFIED`: chưa có output A/B/C, chưa kiểm actual Hub routing/retrieval/compliance. Các kiểm tra trên không chứng minh hành vi giữ boundary.
