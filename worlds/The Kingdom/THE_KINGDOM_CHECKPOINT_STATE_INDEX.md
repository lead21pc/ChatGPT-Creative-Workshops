# The Kingdom — Checkpoint State Index

## 1. Mục đích và thẩm quyền

**Mục đích:** điều hướng chronology checkpoint, quan hệ giữa các state và nơi lưu từng phần của trạng thái The Kingdom đã externalize.

**Thẩm quyền:** index không tạo canon, không thay thế domain source hoặc xác nhận tường minh mới hơn của tác giả. “Nơi lưu” xác định vị trí mệnh đề trong repository, không trao quyền quyết định canon cho tệp đó. Nhãn trong bảng là nhãn của source; liên kết một đoạn với checkpoint là quan hệ điều hướng có giới hạn được ghi kèm.

**Phạm vi:** chỉ trạng thái đã externalize trong repository; không phải world bible, bản chép lại checkpoint hoặc toàn bộ runtime tác giả.

```text
REPOSITORY STATE != FULL PARACOSM
NOT FOUND != FALSE
INDEX ENTRY != CANON PROMOTION
INDEX != REPLACEMENT FOR DOMAIN SOURCE
FILE LOCATION != SEMANTIC AUTHORITY
SOURCE ROLE != CANON PROMOTION
```

Giữ riêng ba trạng thái tri thức:

| Trạng thái | Cách đọc |
|---|---|
| `AUTHOR UNKNOWN` | Tác giả chưa quyết định; chỉ ghi khi tác giả/source xác nhận cụ thể. “Còn mở” trong một source phản ánh trạng thái được source ghi lại, không chứng minh tác giả vẫn chưa quyết định hôm nay. |
| `AUTHOR-KNOWN / REPO-UNKNOWN` | Tác giả biết nhưng phần đó chưa externalize; chỉ gán cho một nội dung cụ thể khi tác giả/source xác nhận. |
| `REPO-KNOWN / SESSION-UNKNOWN` | Đã có trong source nhưng phiên hiện tại chưa đọc hoặc chưa tìm đúng; mở anchor tương ứng trước khi kết luận thiếu. |

Với cầu nối còn thiếu, mặc định ghi **REPOSITORY GAP — author state not established by this index**. Không biến thiếu dữ liệu repository thành quyết định chưa có của tác giả. Các giới hạn này phù hợp với [README — Cách đọc đúng chuẩn][R] và [CI — Canon and Epistemic State][ci-status]; việc dẫn CI không xác nhận CI đó đang được cài trong Project.

## 2. Tổng quan timeline

Nguồn lịch sử CP1: [Sources/checkpoint 1.md][cp1-owner]. Đọc chuỗi này cùng status tại §3–4; mũi tên không chứng minh draft đã xảy ra hoặc lấp các cầu nối thiếu.

```text
PRE-CP1 / S0
    ↓
CP1 — chuyển sang mở cửa; historical owner: Sources/checkpoint 1.md
    ↓
DIRECT STATE DELTA — xem §3.3; giữ nhãn gốc
    ↓
POST-OPENING STATE / S1 — mới externalize một phần
    ↓
khoảng 2 năm thích nghi — chưa externalize đủ diễn biến
    ↓
trạng thái trước sự kiện trong nguồn CP2
    ↓
ứng viên sự kiện CP2 — tương ứng ngữ nghĩa mạnh, thiếu liên kết identity
```

**S1 ngay sau CP1 không nhất thiết giống state ngay trước CP2.** Source hiện chưa tách đầy đủ những gì đổi ngay khi mở cửa và những gì tích lũy trong khoảng hai năm. Khoảng thời gian được ghi tại [H §4.1 — Checkpoint model][h-id]; quan hệ kế thừa được mô tả tại [H §4.2 — Path dependence][h-path].

## 3. CP1

### 3.1 Identity

**Historical owner:** [Sources/checkpoint 1.md — §1 Identity và phạm vi][cp1-id]. **Identity:** “Bắt đầu mở cửa / mở thương mại”.

**Provenance:** identity ban đầu được recovery từ lời tác giả ghi tại [H §4.1 — Checkpoint model][h-id], nhãn `[USER-PROVIDED]`, và nay được externalize thành CP1 historical ownership theo yêu cầu tường minh của tác giả. [H — End state][h-end] vẫn xác định handoff là analysis/snapshot, không phải canon source; việc chuyển ownership không nhập toàn bộ handoff vào canon. Index dẫn tới owner mới, không tự tạo historical fact.

**MISSING BRIDGE / UNRESOLVED SEMANTIC:** [CP1 §9 — Những cầu nối chưa đủ source][cp1-gaps] tiếp tục giữ delta chính xác của “mở thương mại” là chưa được externalize đủ. Nga đã được cấp phép giao dịch hàng hóa trực tiếp trong thời kỳ đóng cửa ([G §IV — Quan hệ lịch sử với Nga][g-russia]; [G §V — Trao đổi hàng hóa thời kỳ đóng cửa][g-trade], các block `CANON`). Không diễn giải CP1 thành “trước đó không có thương mại”. Thay đổi về đối tác, hàng hóa, quyền tiếp cận, giấy phép hay tuyến vận tải vẫn là **REPOSITORY GAP — author state not established by this index**.

### 3.2 Pre-CP1 / S0

Baseline lịch sử CP1 được giữ tại [CP1 §2 — Trạng thái trước checkpoint][cp1-pre]; bảng dưới tiếp tục dẫn domain detail và nhãn nguồn.

| State cần tìm | Source anchor | Status / giới hạn |
|---|---|---|
| Đóng kín nội địa lâu dài; người ngoài chỉ thấy giao diện biên giới | [G §II — Mặt ngoài của Mẫu quốc][g-pre] | §1: `CANON`; không đồng nghĩa tuyệt đối không có tiếp xúc. |
| Bên ngoài chưa nhận diện Mẫu quốc là Type II | [G §II — §2 Trạng thái nhận thức trước mở cửa][g-pre] | `CANON`; tách tri thức bên ngoài khỏi năng lực thật. |
| DMZ và kênh giao tiếp lịch sử | [G §III — DMZ][g-dmz] | §1–2: `CANON`; sơ đồ vận hành và tác động mở cửa thuộc `HỆ QUẢ SUY LUẬN`. DMZ không phải nhập cảnh nội địa. |
| Nga có giao dịch hàng hóa trực tiếp trước mở cửa | [G §IV][g-russia] và [§V][g-trade] | Quyền giao dịch và logistics: `CANON`; các suy luận tình báo/giới hạn hàng hóa giữ nhãn riêng. Không suy quyền đại diện ngoại giao từ quyền giao dịch. |

### 3.3 Trigger / transition

Đọc chuyển tiếp lịch sử trước tiên tại [CP1 §3 — Trigger][cp1-trigger], [§4 — Chuyển tiếp checkpoint đã xác nhận][cp1-transition] và [§6 — Direct state delta][cp1-delta]. Các anchor domain dưới đây giữ bằng chứng và status chi tiết.

| Thành phần chuyển trạng thái | Source anchor | Status gốc / cách dùng |
|---|---|---|
| Lời mời qua các đấng tối cao | [G §IX — §1 Kênh mở cửa][g-invite]; [D §1 — Bối cảnh đã chốt][d-context] | G §1: `CANON`; D đặt trong bối cảnh đã chốt. |
| Mục tiêu mở cửa chủ yếu là trao đổi văn hóa | [G §X — §1 Mục tiêu][g-culture] | `CANON`; mục tiêu này không giải thích thay thời điểm “tại sao bây giờ”. |
| Đoàn đầu là đoàn xác minh, không phải đoàn đàm phán chiến lược | [G §XIII — Phái đoàn đầu tiên và phạm vi hợp lý][g-delegation]; [D §1][d-context] | G: `CANON`; mandate không tự xác nhận itinerary cụ thể. |
| Thay đổi mặt trận chính danh / quyền xác minh | [G §IX — §2–3][g-invite]; [G §X — §3][g-culture]; [D §1][d-context] | G §IX.2 và §X.3: `CANON / HỆ QUẢ TRỰC TIẾP`; §IX.3: `CANON`. D ghi hệ quả về độc quyền đại diện ngoại giao trong bối cảnh đã chốt. Giữ phạm vi từng cách phát biểu. |
| Áp lực cấm vận văn hóa và chuỗi “phá hàng” | [G §X — §2][g-culture]; [G §XI — Các nước nhỏ, trung lập và hiện tượng “phá hàng”][g-cascade] | `HỆ QUẢ SUY LUẬN`; không dùng chuỗi nước A/B/C như danh sách các chuyến tiếp xúc đã xảy ra. |

### 3.4 Tiếp xúc đầu tiên và các interface mở cửa

[CP1 §5 — Interface mở cửa liên quan][cp1-interfaces] phân biệt sử dụng đã xác nhận, candidate/draft và capability/domain reference; implementation chi tiết tiếp tục ở các source dưới đây.

| Phần cần tìm | Source anchor | Temporal / epistemic boundary |
|---|---|---|
| Itinerary tiếp đón ứng viên | [D §2 — Trình tự tiếp đón (draft, có thể sửa)][d-draft] | `DRAFT / có thể sửa`; không nâng scan, di chuyển, lưu trú và chương trình ngày đầu thành event đã chốt chỉ vì cùng nằm trong timeline. |
| Xác minh ở DMZ rồi nhập cảnh sâu hơn | [G §XIII — Vai trò của DMZ][g-delegation]; [G §III][g-dmz] | Mô hình thực hiện: `HỆ QUẢ SUY LUẬN`; DMZ lịch sử có block canon riêng. Quan hệ itinerary đã được chấp nhận với D §2 còn thiếu. |
| Vành đai và chính sách tiết lộ | [I §6 — Vành đai mở cửa và mức độ tiết lộ][i-rings]; [I §14 — Nguyên tắc tiết lộ trong giai đoạn mở cửa][i-reveal] | Mô tả chức năng xen khuyến nghị “nên/không cần”; không tự gán toàn bộ là event canon. |
| Tiến trình đối ngoại, tổ chức đoàn, di chuyển | [I §9 — Quy trình mở cửa hợp lý][i-sequence]; [§10 — Phái đoàn ngoại giao đầu tiên][i-delegation]; [§13 — Di chuyển của phái đoàn trong ngày đầu][i-movement] | Chuỗi hợp lý, ví dụ quy mô và phương án; không chứng minh mọi bước, kể cả quan hệ thường trú, đã hoàn thành. |
| An ninh và communication | [I §11 — An ninh của phái đoàn][i-security]; [§12 — Liên lạc của sứ đoàn][i-comms] | Khuyến nghị / phương án tác nghiệp; giữ nguyên tính điều kiện và chưa tự xác lập protocol lịch sử. |
| Scan và containment ở biên giới | [Y §2 — Hệ thống kiểm soát bệnh của người ngoài][y-scan]; [§6 — Phân tầng quyền lợi y tế][y-rights]; [D §2][d-draft] | Y mô tả concept/interface, không gắn nhãn canon cho từng block hay ngày hình thành. D dùng interface trong draft. Kiểm dịch không đồng nghĩa đặc quyền chữa bệnh. |
| Đại sứ quán tiền tiêu | [S §II — §1 Thiết kế nhân sự][s-embassy] | Block `CANON` nói “có thể” trước khi mở cửa hoàn toàn. Không chứng minh đã xây, cũng không đủ đặt chắc trước CP1. §2 là suy luận, §3 là phương án thiết kế. |
| Vật phẩm, phần mềm và tri thức sâu | [S §III — Vật phẩm][s-goods]; [§IV — Phần mềm][s-software]; [§V — Oath][s-oath] | Canon về khả năng xen phương án mở rộng và câu hỏi chưa chốt. Thời điểm áp dụng so với giao dịch Nga, CP1 và giai đoạn sau chưa được neo; không gán cả tệp S cho CP1. |

Hạ tầng nền tại [I §2][i-base], [I §3][i-airspace] và các interface Y/S ở trên là **CAPABILITY / INTERFACE USED BY OPENING — NOT ESTABLISHED AS CP1-CREATED DELTA**: chúng hỗ trợ bối cảnh mở cửa, nhưng index không xác định CP1 là thời điểm tạo ra chúng. Việc sử dụng trong itinerary cụ thể vẫn giữ status draft/phương án tương ứng.

### 3.5 Direct / inherited post-opening state

Phân biệt delta trực tiếp và state kế thừa theo [CP1 §6][cp1-delta] và [§7 — Trạng thái hậu mở cửa][cp1-post]. Snapshot trong C vẫn chỉ là bằng chứng cho state ở thời điểm source C lưu lại.

| Lớp state | Source anchor | Status / giới hạn thời gian |
|---|---|---|
| Direct political delta của lời mời | Các anchor tại §3.3 | Giữ riêng `CANON`, nhãn trộn và hệ quả suy luận; không đồng nhất mục tiêu chính trị với mọi kết quả đã đạt. |
| Khách được vào các vành mở cửa bắt đầu thấy năng lực dân dụng vượt chuẩn hiện đại | [G §XIV — §2 Sau khi mở cửa][g-post] | `CANON / HỆ QUẢ SUY LUẬN`; không tự suy bên ngoài đã biết toàn bộ cơ chế hoặc nhận diện đúng Type II. |
| `INHERITED POST-OPENING STATE`: tiết lộ dân dụng, phép thuật công nghiệp hóa, y tế, AI, hạ tầng; chưa công khai toàn bộ quân lực hoặc trần chiến lược | [C §I — §1 Trạng thái nhận thức của thế giới ngoài][c-pre] | `CANON` trong source C. Đây là snapshot trước sự kiện của C, được dẫn về mở cửa ở cấp quan hệ điều hướng. |

C giữ một snapshot hậu mở cửa được kế thừa. Snapshot đó không tự chứng minh mọi thành phần đổi ngay CP1 thay vì trong hai năm tiếp theo. Index không sao chép snapshot thành nguồn canon mới hoặc tuyên bố đã phục hồi đầy đủ S1 tức thời.

### 3.6 Khoảng giữa hai checkpoint

**Ranh giới lịch sử:** [CP1 §8 — Ranh giới giữa hai checkpoint][cp1-interval]. Khoảng cách CP1 → CP2 ≈ 2 năm tiếp tục giữ provenance từ [H §4.1][h-id], nhãn `[USER-PROVIDED]`; ownership mới không tự bổ sung lịch sử thích nghi.

**Coverage repository:** chưa đủ để tái dựng đầy đủ diễn biến thích nghi trong khoảng này. H §4.1 nêu thương mại, công nghệ, lao động, nhận thức về outsider, truyền thông, interest conflict và institutional response là các miền có thể đổi nhanh. Đây là **phạm vi thích nghi có thể/dự kiến trong mô tả runtime**, không phải event list đã xảy ra.

[S §X — §2 Chuyển cuộc chơi từ “lấy bí mật” sang “tìm cái có thể học hợp pháp”][s-adapt] nói đến thay đổi sau vài lần thất bại, nhưng không cung cấp ngày hoặc chuỗi event để index đặt chắc vào khoảng này. Không biến khoảng hai năm thành một timeline do model bổ sung.

### 3.7 Những cầu nối còn thiếu

[CP1 §9 — Những cầu nối chưa đủ source][cp1-gaps] giữ các gap lịch sử sau khi chuyển ownership; các anchor domain dưới đây tiếp tục cho biết giới hạn bằng chứng.

Tất cả các hàng sau là **REPOSITORY GAP — author state not established by this index**, không tự phân loại thành tác giả chưa biết hoặc đã biết.

| Cầu nối | Anchor cho bằng chứng / giới hạn |
|---|---|
| Delta chính xác của “mở thương mại” so với giao dịch Nga trước CP1 | [H §4.1][h-id]; [G §IV][g-russia], [§V][g-trade]. |
| Ai phản hồi lời mời trước; cơ chế phản hồi và thứ tự tiếp đoàn | [G §XVI — Những điểm còn mở cần quyết định sau][g-open]; [§XI][g-cascade] là suy luận. |
| Những phần nào của itinerary đầu tiên đã được chấp nhận | [D §2][d-draft] vẫn là draft; [I §9][i-sequence] và [§13][i-movement] là chuỗi hợp lý. |
| Quan hệ chính xác giữa xác minh ở DMZ và nhập cảnh sâu hơn | [G §XIII][g-delegation] giữ mô hình suy luận; đối chiếu [D §2][d-draft]. |
| Phần state xuất hiện ngay CP1 và phần tích lũy trước sự kiện trong C | [G §XIV.2][g-post]; [C §I.1][c-pre] không chia mốc đầy đủ. |
| Lịch sử thích nghi cụ thể trong khoảng hai năm | [H §4.1–4.2][h-id] giữ khoảng thời gian/mô hình, không giữ đủ historical state. |

## 4. CP2

### 4.1 Identity status

**IDENTITY STATUS: strong semantic correspondence; explicit identity/provenance link absent.**

[H §4.1][h-id] ghi CP2 là “các nước láng giềng bắt đầu hostile/aggression”. [C — Sự kiện thử nước, đánh chặn và phản ứng quốc tế][C] mô tả vụ thử phản ứng bằng khủng bố cùng vai trò các cường quốc và phản ứng của Mẫu quốc. Sự tương ứng mạnh về chủ đề/sự kiện thù địch sau mở cửa chưa thay thế liên kết provenance tường minh.

**MISSING BRIDGE:** C chưa tự gắn sự kiện với mô tả CP2 trong H, khoảng cách hai năm hoặc danh tính các nước láng giềng. [C §XII — Điểm chưa chốt][c-open] còn để mở quốc gia/cơ quan biết trước. Đây là **REPOSITORY GAP — author state not established by this index**. “CP2” bên dưới là nhãn điều hướng tới ứng viên này, không xác nhận identity tuyệt đối từ tên tệp.

### 4.2 Starting state

| Thành phần | Source anchor | Status gốc |
|---|---|---|
| `CP2_PRECONDITION`: inherited post-opening snapshot | [C §I — §1][c-pre]; xem §3.5 | `CANON`; không phải delta CP2 hoặc bằng chứng S1 tức thời đã hoàn chỉnh. |
| Động cơ “test the water” dưới bất định về sức mạnh và attribution | [C §I — §2 Vấn đề chiến lược của các cường quốc][c-pre] | `HỆ QUẢ SUY LUẬN`; không nâng động cơ suy luận thành kế hoạch đã được ghi nhận của mọi nước. |
| Tác nhân trực tiếp và mức liên quan của bên ngoài | [C §II — Tác nhân gây khủng hoảng][c-actors] | §1: `CANON / PHƯƠNG ÁN THIẾT KẾ`; §2: `CANON`, vẫn giữ các mệnh đề “có thể”. Biết mà không ngăn không đồng nghĩa tài trợ. |

### 4.3 Event

| Phần `CP2_EVENT` cần tìm | Source anchor | Status gốc / giới hạn |
|---|---|---|
| Mục tiêu phản ứng và đánh chặn | [C §III — Mục tiêu phản ứng][c-goals]; [§IV — Trình tự sự kiện][c-sequence] | `PHƯƠNG ÁN THIẾT KẾ`, gồm phát hiện trước và các pha tác nghiệp. |
| Niêm phong và reveal quân lực tầng một | [C §V — Chuyển từ chiến đấu sang nghi thức răn đe][c-reveal] | Pha 3: `PHƯƠNG ÁN THIẾT KẾ`; Pha 4: `CANON / PHƯƠNG ÁN THIẾT KẾ`. Không nâng toàn bộ dàn dựng thành event canon. |
| Công khai attribution | [C §VI — Công khai hóa attribution bằng hologram][c-attribution] | §1: `CANON`; §2 trình bày cấu trúc công khai nhưng không gắn nhãn riêng cho từng lớp. |
| Thông điệp răn đe | [C §VII — Thông điệp răn đe đề xuất][c-message] | `PHƯƠNG ÁN THIẾT KẾ`; không phải transcript đã xác lập. |
| Domain projection về proxy/khủng bố | [S §VII — Phản gián chủ động đối với proxy và khủng bố][s-proxy] | §1: `CANON / HỆ QUẢ TRỰC TIẾP`; §2: `CANON` có điều kiện; §3 không có nhãn riêng. Không kéo các phần xuất khẩu/đại sứ quán của S vào event. |

### 4.4 Resulting state / unresolved scope

| Phần `POST_CP2 CONSEQUENCE` trong source ứng viên | Source anchor | Status / phạm vi |
|---|---|---|
| Phản ứng một giờ đầu | [C §VIII — Phản ứng trong 1 giờ đầu][c-1h] | §0 là `CANON` nền cho VIII–X; §1–2 là `HỆ QUẢ SUY LUẬN`; §3 không gắn nhãn riêng. |
| Phản ứng sau 24 giờ và 72 giờ | [C §IX][c-24h]; [§X][c-72h] | IX.1 và X.2 có nhãn `HỆ QUẢ SUY LUẬN`; các tiểu mục còn lại không gắn nhãn riêng. Không tự nâng phần không gắn nhãn thành canon. |
| Ý nghĩa dài hạn | [C §XI — Ý nghĩa dài hạn][c-long] | Đoạn tổng hợp không gắn nhãn epistemic riêng; không dùng làm current-state snapshot đầy đủ. |
| Chi tiết chưa chốt | [C §XII — Điểm chưa chốt][c-open]; [S §XI — Những lỗ hổng còn cần quyết định][s-open] | Giữ mở danh tính bên liên quan, dàn dựng, cơ chế, phạm vi hologram và chế tài trong C; cơ chế attribution/kiểm soát tri thức trong S. |

Không dùng các phản ứng sau sự kiện ở C §VIII–XI để lấp khoảng thích nghi trước CP2. Identity của nguồn ứng viên và status hỗn hợp tiếp tục áp dụng cho mọi resulting state được dẫn tại đây.

## 5. Ghi chú vai trò nguồn

| Source | Phần đang được lưu / vai trò điều hướng |
|---|---|
| [CP1 — checkpoint 1.md][cp1-owner] | Historical owner cho identity, chuyển tiếp CP1, delta/resulting state có bằng chứng và gap; domain detail tiếp tục thuộc source riêng. |
| [H — Handoff snapshot][H] | Provenance gốc của CP1 identity, khoảng thời gian và mô tả runtime; CP1 historical owner đã chuyển tới source mới. H vẫn giữ giới hạn analysis/handoff. |
| [G — Địa chính trị, DMZ và quan hệ quốc tế][G] | S0, giao dịch Nga trước mở cửa, chuyển tiếp chính trị, mandate đoàn và mô tả sau mở cửa. |
| [D — Sứ đoàn xác minh và stress-test][D] | Bối cảnh đã chốt; draft tiếp đón; câu hỏi suy từ logic (§3), phương án “tại sao bây giờ” (§4), stress-test (§5), điểm mở (§6). |
| [I — Hạ tầng, không lưu và mở cửa][I] | Hạ tầng thường trực và phương án interface vật lý/tác nghiệp; không phải một event log CP1. |
| [Y — Hệ thống sức khỏe][Y] | Concept kiểm dịch, quyền tiếp cận và điểm mở; không xác định ngày CP1 tạo ra hệ thống. |
| [S — Phản gián và kiểm soát tri thức][S] | Source xuyên nhiều phạm vi thời gian: đại sứ quán, xuất khẩu, tri thức sâu, proxy/khủng bố và thích nghi chưa định ngày. |
| [C — checkpoint 2.md][C] | Inherited baseline, sự kiện ứng viên CP2 và phản ứng sau sự kiện với status hỗn hợp. |

Các mệnh đề lặp trong nhiều nguồn không tạo thứ bậc mới. Index dẫn nơi cần đọc; nếu source đổi hoặc bất đồng, đọc lại phần được dẫn và giữ bất đồng chưa giải quyết thay vì chọn theo vị trí tệp, số lần nhắc hoặc tên “checkpoint”.

## 6. Loại trừ và chống đọc nhầm

- **Method example != history.** [Phương pháp sáng tác §V][m-example-a] dùng Checkpoint A/B và [§XIII][m-example-1] dùng “Checkpoint 1: reveal quân sự; Checkpoint 2: mở tuyến vận tải” dưới chữ “Ví dụ”. Không dùng chúng làm chronology cạnh tranh với identity lịch sử tại [CP1 §1][cp1-id]; H tiếp tục giữ provenance gốc. [POV–perspective][V] là phương pháp kể chuyện, không phải event log.
- **Persistent infrastructure != checkpoint delta.** Hạ tầng [I §2–3][i-base], [y tế][Y], [POT][P], [Universal Language và tôn giáo][L] không tự trở thành CP1-created. Mô tả một người vào Thần Điện không tự xác nhận quyền vào của đoàn đầu tiên.
- **Historical snapshot != duplicate error.** [C §I][c-pre] có thể hợp lý khi giữ state kế thừa làm input sự kiện mới; đọc nó khi phục hồi hậu mở cửa nhưng giữ giới hạn tại §3.5.
- **Mixed status must remain mixed.** Giữ riêng `CANON`, `HỆ QUẢ SUY LUẬN`, `DRAFT`, `PHƯƠNG ÁN THIẾT KẾ` và nhãn trộn. Phần không gắn nhãn không tự thừa hưởng certainty do index cần chuỗi liên tục.
- **Câu hỏi / stress-test != event đã xảy ra.** [D §3][d-questions] không phải transcript; [§5][d-test] không phải lịch sử; [§4][d-why] và [§6][d-open] giữ phương án/điểm mở. Mục tiêu trao đổi văn hóa không tự chọn đáp án “tại sao bây giờ”.
- **Control / kiến trúc không quyết định thời gian lịch sử.** [Anti-drift][A] giữ quan hệ và provenance, không đặt event vào CP1. Các biến thể CI hoặc các đời thiết kế Law không tự xác lập chronology checkpoint.

[H]: <two_paracosms_the_kingdom_vs_the_academy.md>
[G]: <Sources/the_kingdom_dia_chinh_tri_dmz_quan_he_quoc_te.md>
[D]: <Sources/the_kingdom_su_doan_xac_minh_va_stress_test.md>
[I]: <Sources/the_kingdom_ha_tang_khong_luu_mo_cua.md>
[Y]: <Sources/the_kingdom_he_thong_suc_khoe.md>
[S]: <Sources/the_kingdom_he_thong_phan_gian_va_kiem_soat_tri_thuc.md>
[C]: <Sources/checkpoint%202.md>
[V]: <Sources/the_kingdom_pov_perspective_architecture.md>
[P]: <Sources/the_kingdom_POT_personal_terminal_watch.md>
[R]: <README.md>
[L]: <Sources/the_kingdom_language_religion_meta.md>
[A]: <modular_engine_concept_anti_drift.md>
[h-id]: <two_paracosms_the_kingdom_vs_the_academy.md#41-checkpoint-model>
[h-path]: <two_paracosms_the_kingdom_vs_the_academy.md#42-path-dependence>
[h-end]: <two_paracosms_the_kingdom_vs_the_academy.md#end-state>
[g-pre]: <Sources/the_kingdom_dia_chinh_tri_dmz_quan_he_quoc_te.md#ii-mặt-ngoài-của-mẫu-quốc>
[g-dmz]: <Sources/the_kingdom_dia_chinh_tri_dmz_quan_he_quoc_te.md#iii-dmz--vùng-giao-tiếp-phi-quân-sự-lịch-sử>
[g-russia]: <Sources/the_kingdom_dia_chinh_tri_dmz_quan_he_quoc_te.md#iv-quan-hệ-lịch-sử-với-nga>
[g-trade]: <Sources/the_kingdom_dia_chinh_tri_dmz_quan_he_quoc_te.md#v-trao-đổi-hàng-hóa-thời-kỳ-đóng-cửa>
[g-invite]: <Sources/the_kingdom_dia_chinh_tri_dmz_quan_he_quoc_te.md#ix-mở-cửa-và-lời-mời-tôn-giáo>
[g-culture]: <Sources/the_kingdom_dia_chinh_tri_dmz_quan_he_quoc_te.md#x-trao-đổi-văn-hóa-như-mục-tiêu-mở-cửa>
[g-cascade]: <Sources/the_kingdom_dia_chinh_tri_dmz_quan_he_quoc_te.md#xi-các-nước-nhỏ-trung-lập-và-hiện-tượng-phá-hàng>
[g-delegation]: <Sources/the_kingdom_dia_chinh_tri_dmz_quan_he_quoc_te.md#xiii-phái-đoàn-đầu-tiên-và-phạm-vi-hợp-lý>
[g-post]: <Sources/the_kingdom_dia_chinh_tri_dmz_quan_he_quoc_te.md#xiv-tương-quan-sức-mạnh-và-cách-thế-giới-ngoài-nhìn-mẫu-quốc>
[g-open]: <Sources/the_kingdom_dia_chinh_tri_dmz_quan_he_quoc_te.md#xvi-những-điểm-còn-mở-cần-quyết-định-sau>
[d-context]: <Sources/the_kingdom_su_doan_xac_minh_va_stress_test.md#1-bối-cảnh-đã-chốt>
[d-draft]: <Sources/the_kingdom_su_doan_xac_minh_va_stress_test.md#2-trình-tự-tiếp-đón-draft-có-thể-sửa>
[d-questions]: <Sources/the_kingdom_su_doan_xac_minh_va_stress_test.md#3-bộ-câu-hỏi-hợp-lý-của-đoàn-xác-minh-suy-từ-logic-không-bịa-thêm>
[d-why]: <Sources/the_kingdom_su_doan_xac_minh_va_stress_test.md#4-bốn-hướng-lý-do-tại-sao-là-bây-giờ-chưa-chốt--để-ngỏ-cho-tác-giả-chọn>
[d-test]: <Sources/the_kingdom_su_doan_xac_minh_va_stress_test.md#5-bộ-câu-hỏi-stress-test-llm-khi-làm-worldbuilding>
[d-open]: <Sources/the_kingdom_su_doan_xac_minh_va_stress_test.md#6-điểm-còn-mở-cần-quyết-định-ở-phiên-sau>
[i-base]: <Sources/the_kingdom_ha_tang_khong_luu_mo_cua.md#2-nền-tảng-hạ-tầng-của-mẫu-quốc>
[i-airspace]: <Sources/the_kingdom_ha_tang_khong_luu_mo_cua.md#3-phân-tầng-giao-thông-và-không-lưu>
[i-rings]: <Sources/the_kingdom_ha_tang_khong_luu_mo_cua.md#6-vành-đai-mở-cửa-và-mức-độ-tiết-lộ>
[i-sequence]: <Sources/the_kingdom_ha_tang_khong_luu_mo_cua.md#9-quy-trình-mở-cửa-hợp-lý>
[i-delegation]: <Sources/the_kingdom_ha_tang_khong_luu_mo_cua.md#10-phái-đoàn-ngoại-giao-đầu-tiên>
[i-security]: <Sources/the_kingdom_ha_tang_khong_luu_mo_cua.md#11-an-ninh-của-phái-đoàn>
[i-comms]: <Sources/the_kingdom_ha_tang_khong_luu_mo_cua.md#12-liên-lạc-của-sứ-đoàn>
[i-movement]: <Sources/the_kingdom_ha_tang_khong_luu_mo_cua.md#13-di-chuyển-của-phái-đoàn-trong-ngày-đầu>
[i-reveal]: <Sources/the_kingdom_ha_tang_khong_luu_mo_cua.md#14-nguyên-tắc-tiết-lộ-trong-giai-đoạn-mở-cửa>
[y-scan]: <Sources/the_kingdom_he_thong_suc_khoe.md#2-hệ-thống-kiểm-soát-bệnh-của-người-ngoài>
[y-rights]: <Sources/the_kingdom_he_thong_suc_khoe.md#6-phân-tầng-quyền-lợi-y-tế>
[s-embassy]: <Sources/the_kingdom_he_thong_phan_gian_va_kiem_soat_tri_thuc.md#ii-lớp-1--nhân-sự-đại-sứ-quán-tiền-tiêu>
[s-goods]: <Sources/the_kingdom_he_thong_phan_gian_va_kiem_soat_tri_thuc.md#iii-lớp-2--vật-phẩm-trao-đổi-có-creed-hoặc-curse>
[s-software]: <Sources/the_kingdom_he_thong_phan_gian_va_kiem_soat_tri_thuc.md#iv-lớp-3--phần-mềm-có-curse-cá-nhân-hóa>
[s-oath]: <Sources/the_kingdom_he_thong_phan_gian_va_kiem_soat_tri_thuc.md#v-lớp-4--oath-cho-cá-nhân-tiếp-cận-tri-thức-sâu>
[s-proxy]: <Sources/the_kingdom_he_thong_phan_gian_va_kiem_soat_tri_thuc.md#vii-phản-gián-chủ-động-đối-với-proxy-và-khủng-bố>
[s-adapt]: <Sources/the_kingdom_he_thong_phan_gian_va_kiem_soat_tri_thuc.md#x-những-gì-hệ-này-làm-tốt>
[s-open]: <Sources/the_kingdom_he_thong_phan_gian_va_kiem_soat_tri_thuc.md#xi-những-lỗ-hổng-còn-cần-quyết-định>
[c-pre]: <Sources/checkpoint%202.md#i-bối-cảnh-chiến-lược-trước-sự-kiện>
[c-actors]: <Sources/checkpoint%202.md#ii-tác-nhân-gây-khủng-hoảng>
[c-goals]: <Sources/checkpoint%202.md#iii-mục-tiêu-phản-ứng-của-mẫu-quốc>
[c-sequence]: <Sources/checkpoint%202.md#iv-trình-tự-sự-kiện>
[c-reveal]: <Sources/checkpoint%202.md#v-chuyển-từ-chiến-đấu-sang-nghi-thức-răn-đe>
[c-attribution]: <Sources/checkpoint%202.md#vi-công-khai-hóa-attribution-bằng-hologram>
[c-message]: <Sources/checkpoint%202.md#vii-thông-điệp-răn-đe-đề-xuất>
[c-1h]: <Sources/checkpoint%202.md#viii-phản-ứng-trong-1-giờ-đầu>
[c-24h]: <Sources/checkpoint%202.md#ix-phản-ứng-sau-24-giờ>
[c-72h]: <Sources/checkpoint%202.md#x-phản-ứng-sau-72-giờ>
[c-long]: <Sources/checkpoint%202.md#xi-ý-nghĩa-dài-hạn>
[c-open]: <Sources/checkpoint%202.md#xii-điểm-chưa-chốt>
[m-example-a]: <Sources/the_kingdom_phuong_phap_sang_tac_fiction.md#v-checkpoint-không-phải-chương>
[m-example-1]: <Sources/the_kingdom_phuong_phap_sang_tac_fiction.md#xiii-không-escalation-chỉ-vì-checkpoint-trước-lớn>
[ci-status]: <The_Kingdom_CI_English_Compact_Revised.md#canon-and-epistemic-state>
[cp1-owner]: <Sources/checkpoint%201.md>
[cp1-id]: <Sources/checkpoint%201.md#1-identity-và-phạm-vi>
[cp1-pre]: <Sources/checkpoint%201.md#2-trạng-thái-trước-checkpoint>
[cp1-trigger]: <Sources/checkpoint%201.md#3-trigger>
[cp1-transition]: <Sources/checkpoint%201.md#4-chuyển-tiếp-checkpoint-đã-xác-nhận>
[cp1-interfaces]: <Sources/checkpoint%201.md#5-interface-mở-cửa-liên-quan>
[cp1-delta]: <Sources/checkpoint%201.md#6-direct-state-delta>
[cp1-post]: <Sources/checkpoint%201.md#7-trạng-thái-hậu-mở-cửa>
[cp1-interval]: <Sources/checkpoint%201.md#8-ranh-giới-giữa-hai-checkpoint>
[cp1-gaps]: <Sources/checkpoint%201.md#9-những-cầu-nối-chưa-đủ-source>
