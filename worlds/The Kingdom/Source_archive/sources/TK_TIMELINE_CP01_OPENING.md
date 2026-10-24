# The Kingdom — Checkpoint 1: Opening Transition

```text
SOURCE_ID: TK-TL-CP01
ROLE: CHECKPOINT
STATUS: ACTIVE
SCOPE: Breakpoint mở cửa; pre-state tối thiểu, direct delta và boundary state CP1.
```

## 1. Identity và phạm vi

**Checkpoint identity:** Bắt đầu mở cửa / mở thương mại.

**Vai trò:** `HISTORICAL CHECKPOINT OWNER FOR REPOSITORY-EXTERNALIZED CP1 STATE`. Theo phạm vi externalization được tác giả cho phép, tệp này sở hữu identity, chuyển tiếp lịch sử, các checkpoint fact đã xác nhận, delta và resulting state có bằng chứng, cùng những cầu nối chưa đủ source của CP1.

**Provenance:** identity được recovery từ lời tác giả ghi dưới nhãn `[USER-PROVIDED]` tại [handoff §4.1 — Checkpoint model][h-id] và được externalize tại đây thành checkpoint owner. [End state của handoff][h-end] vẫn xác định tài liệu gốc là analysis/handoff snapshot; việc chuyển ownership CP1 không nhập các phân tích khác của handoff vào canon.

```text
CHECKPOINT OWNS TRANSITION.
DOMAIN SOURCE OWNS DOMAIN DETAIL.
CHECKPOINT OWNER != COMPLETE WORLD STATE
CHECKPOINT OWNER != DOMAIN SOURCE REPLACEMENT
CHECKPOINT OWNER != PERMISSION TO PROMOTE DRAFT
```

`CONFIRMED CHECKPOINT FACT` bên dưới chỉ dùng cho phần được xác nhận; các nhãn trộn của source tiếp tục được ghi riêng. Thiếu dữ liệu repository được giữ là `REPOSITORY GAP — author state not established here`, không tự đồng nghĩa tác giả chưa quyết định hoặc đã biết nhưng chưa ghi.

## 2. Trạng thái trước checkpoint

**INHERITED PRE-STATE — PRE_CP1.** Baseline lịch sử tối thiểu, từ các block `CANON` của nguồn địa chính trị:

| Thành phần S0 | Source anchor |
|---|---|
| Mẫu quốc tồn tại và đóng kín nội địa lâu dài; gần 2.000 năm người ngoài chưa biết cấu trúc nội địa thật | [§II — Mặt ngoài của Mẫu quốc][g-pre] |
| Bên ngoài biết Mẫu quốc tồn tại và có khả năng phòng thủ vượt hiểu biết của họ, nhưng chưa nhận diện đây là nền văn minh Type II | [§II — §2 Trạng thái nhận thức trước mở cửa][g-pre] |
| DMZ và giao diện tiếp xúc lịch sử đã tồn tại; vào DMZ không đồng nghĩa nhập cảnh nội địa | [§III — DMZ / vùng giao tiếp phi quân sự lịch sử][g-dmz] |
| Nga là quốc gia duy nhất được cấp phép giao dịch hàng hóa trực tiếp trong thời kỳ đóng cửa; hàng đã được trao đổi trước CP1 | [§IV — Quan hệ lịch sử với Nga][g-russia]; [§V — Trao đổi hàng hóa thời kỳ đóng cửa][g-trade] |

S0 vẫn có các liên hệ và giao dịch lịch sử nêu trên. Chi tiết địa chính trị, cơ chế DMZ và logistics tiếp tục thuộc các domain source được dẫn.

## 3. Trigger

**CONFIRMED CHECKPOINT FACT — CP1_EVENT.** Mẫu quốc chủ động phát lời mời mở cửa qua các đấng tối cao của nhiều hệ tín ngưỡng. Đây là nước đi có chủ ý; lõi thông điệp là:

> Mẫu quốc mời mở cửa, hãy cử phái đoàn.

Nguồn: [địa chính trị §IX — §1 Kênh mở cửa][g-invite], nhãn `CANON`. Kênh mời này xác lập bước khởi động mở cửa; không tự xác nhận thứ tự các bên phản hồi.

## 4. Chuyển tiếp checkpoint đã xác nhận

**CONFIRMED CHECKPOINT FACT — CP1_EVENT.**

- CP1 đánh dấu bước chủ động mở cửa từ trạng thái nội địa đóng kín với giao diện liên hệ/giao dịch lịch sử hạn chế. Identity ở §1 và trigger ở §3 xác lập chuyển tiếp này; chưa xác lập đầy đủ một chế độ giao thương mới.
- Mục tiêu mở cửa chủ yếu là **trao đổi văn hóa**, theo [địa chính trị §X — §1 Mục tiêu][g-culture], `CANON`.
- Đoàn đầu tiên có mandate **xác minh**, không phải đàm phán chiến lược, theo [địa chính trị §XIII — Phái đoàn đầu tiên và phạm vi hợp lý][g-delegation], `CANON`.

**FIRST-CONTACT EXECUTION:** mandate đã xác nhận; detailed itinerary chưa được xác nhận trong các source đang được dẫn. [Sứ đoàn §2 — Trình tự tiếp đón (draft, có thể sửa)][d-draft] là `DRAFT / CANDIDATE`. Các bước scan, liaison, di chuyển, lưu trú và xác minh tôn giáo tại đó chưa được nhập thành chuỗi event lịch sử đã xảy ra.

## 5. Interface mở cửa liên quan

Các nhãn dưới đây phân biệt bằng chứng về sử dụng thực tế với phương án sử dụng và khả năng thường trực. `CANDIDATE / DRAFT USED` chỉ có nghĩa sử dụng được đề xuất, không chứng minh đã thực hiện.

| Interface | Trạng thái sử dụng trong CP1 / nguồn |
|---|---|
| Kênh lời mời qua các đấng tối cao | `CONFIRMED USED`: lời mời ở §3, [địa chính trị §IX.1][g-invite], `CANON`. |
| DMZ / biên tiếp xúc bên ngoài | `PERSISTENT CAPABILITY ONLY`: DMZ lịch sử là canon ([§III][g-dmz]); cách dùng DMZ cho xác minh rồi nhập cảnh sâu hơn ở [§XIII — Vai trò của DMZ][g-delegation] là `HỆ QUẢ SUY LUẬN`. Chưa xác nhận itinerary đã dùng. |
| Vành mở cửa, di chuyển và tiếp nhận | `CANDIDATE / DRAFT USED`: [sứ đoàn §2][d-draft]; [hạ tầng §6 — Vành đai mở cửa][i-rings], [§9 — Quy trình mở cửa hợp lý][i-sequence], [§13 — Di chuyển ngày đầu][i-movement]. Giữ tính draft, “chuỗi hợp lý” và khuyến nghị; an ninh/liên lạc chi tiết xem §11–12 trong cùng nguồn hạ tầng. |
| Scan / containment tại biên giới | `PERSISTENT CAPABILITY ONLY`: [y tế §2 — Hệ thống kiểm soát bệnh của người ngoài][y-scan] mô tả interface, không xác định CP1 tạo ra nó; việc sử dụng trong [itinerary][d-draft] còn là draft. Không đồng nhất kiểm dịch với quyền được chữa bệnh. |
| Đại sứ quán tiền tiêu và kiểm soát tri thức | `DOMAIN REFERENCE`: [phản gián §II][s-embassy] có block `CANON` nói “có thể” xây đại sứ quán trước mở cửa hoàn toàn; không chứng minh đã xây hoặc đã dùng ở CP1. [Các §III–V trong nguồn phản gián][S] giữ khả năng xuất khẩu/tiếp cận tri thức xen phương án, không có ngày kích hoạt CP1. |
| Tiết lộ dân dụng có chọn lọc | `DOMAIN REFERENCE`: [hạ tầng §14 — Nguyên tắc tiết lộ][i-reveal] có khuyến nghị; state hậu mở cửa có bằng chứng riêng tại §7. Không biến chính sách được đề xuất thành itinerary đã được chấp nhận. |

Các interface hỗ trợ mở cửa không tự trở thành `CP1-CREATED DELTA`. Domain source tiếp tục giữ implementation và phạm vi năng lực.

## 6. Direct state delta

| Delta / ranh giới | Trạng thái và bằng chứng |
|---|---|
| Từ giao diện lịch sử hạn chế sang chủ động mời mở cửa, với phạm vi đoàn xác minh đã xác định | `CONFIRMED CHECKPOINT FACT — CP1_DIRECT_DELTA`: identity, trigger và mandate tại §1, §3–4. Chưa suy thành toàn bộ quan hệ ngoại giao/thương mại thường trú đã vận hành. |
| Lời mời được truyền qua các đấng tối cao; phạm vi xác minh và chính danh bị tác động | `DIRECT CONSEQUENCE — CANON / HỆ QUẢ TRỰC TIẾP`, theo [địa chính trị §IX.2][g-invite] và [§X.3][g-culture]. Phạm vi được nêu là định nghĩa hiện tượng/lời mời và quyền xác minh, cùng chi phí chính trị của cấm tiếp xúc; không tuyên bố nhà nước mất hoàn toàn quyền đại diện ngoại giao. |
| Knowledge state và giới hạn tiết lộ chiến lược | Có mô tả hậu mở cửa và snapshot kế thừa tại §7; chưa đủ căn cứ phân bổ toàn bộ chúng thành delta tức thời của CP1. |

Các phản ứng “phá hàng” và hiệu ứng dây chuyền trong domain source giữ status suy luận, không trở thành event list đã xảy ra trong CP1.

## 7. Trạng thái hậu mở cửa

**DIRECT CP1 RESULT — phần xác định được:** trạng thái chủ động mở cửa bằng lời mời và mandate xác minh tại §3–4. Kết quả triển khai itinerary cụ thể, thời điểm kết thúc CP1 và toàn bộ S1 tức thời chưa được externalize đủ.

Tiến trình tiếp đoàn, thay đổi tri thức, phản ứng và state tích lũy sau breakpoint thuộc [interval CP1→CP2][interval], không thuộc boundary tức thời này. Source mới đã recovery việc có một số phái đoàn cơ sở/ban đầu trong khoảng đó; thứ tự và itinerary từng đoàn vẫn chưa khóa.

```text
S1 IMMEDIATELY AFTER CP1
!= NECESSARILY
STATE IMMEDIATELY BEFORE CP2
```

## 8. Ranh giới giữa hai checkpoint

[Handoff §4.1][h-id] ghi CP1 → CP2 **≈ 2 năm**, dưới nhãn `[USER-PROVIDED]`. [Interval CP1→CP2][interval] sở hữu phần lịch sử giữa hai breakpoint và final pre-CP2 state. Khoảng thời gian này không tự cung cấp ngày kết thúc CP1 hoặc danh sách event.

CP2 hiện được nhận diện theo recovery reveal và yêu cầu migration của tác giả; xem [owner CP2][cp2]. Danh tính các nước láng giềng trong mô tả cũ và nền chính trị proxy vẫn chưa được xác định. Không kéo reveal quân sự về CP1.

## 9. Những cầu nối chưa đủ source

**UNRESOLVED REPOSITORY SEMANTIC — “mở thương mại”:** chưa xác định rõ thay đổi đối tác, loại hàng, quyền tiếp cận, giấy phép, tuyến vận tải hay combination nào. Giao dịch Nga trước CP1 đã có (§2); không dùng mô hình “không có thương mại → bắt đầu thương mại”.

Các cầu nối còn lại là **REPOSITORY GAP — author state not established here**:

| Cầu nối | Giới hạn hiện có |
|---|---|
| Ai phản hồi lời mời đầu tiên | [Địa chính trị §XVI — Những điểm còn mở cần quyết định sau][g-open] chưa chốt cơ chế phản hồi và thứ tự phá hàng/tiếp xúc. |
| Sequence tiếp đoàn nào được chấp nhận | [Sứ đoàn §2][d-draft] vẫn là draft; các chuỗi tác nghiệp trong hạ tầng vẫn là phương án/khuyến nghị. |
| Quan hệ giữa DMZ verification và deeper entry | Mô hình [địa chính trị §XIII][g-delegation] là suy luận; chưa đủ để xác nhận việc nối với itinerary draft. |
| S1 tức thời so với state tích lũy trước sự kiện trong nguồn CP2 | [Địa chính trị §XIV.2][g-post] và [interval §6][c-pre] chưa chia đầy đủ mốc đạt từng thành phần. |
| Historical adaptation trong khoảng hai năm | [Handoff §4.1][h-id] giữ khoảng thời gian và mô tả runtime, không giữ đủ diễn biến theo actor/domain. |

## 10. Source anchor và giới hạn thẩm quyền

Các anchor trong từng section là provenance của mệnh đề, không chuyển toàn bộ domain source vào ownership CP1. Source địa chính trị tiếp tục giữ chi tiết về địa lý/DMZ/đối ngoại; hạ tầng, y tế và phản gián tiếp tục giữ hệ thống thường trực và các phương án riêng.

Nhãn `CANON / HỆ QUẢ TRỰC TIẾP`, `CANON / HỆ QUẢ SUY LUẬN`, draft và phương án không bị rút thành plain canon. Source không gắn nhãn hoặc không ghi ngày không tự nhận certainty/chronology mới từ tệp checkpoint này. Xác nhận tường minh mới hơn của tác giả tiếp tục có ưu tiên.

Các checkpoint đánh số trong [phương pháp sáng tác §XIII — Không escalation chỉ vì checkpoint trước lớn][m-example-1] là ví dụ phương pháp; không nhập chúng vào lịch sử CP1.

[h-id]: <../two_paracosms_the_kingdom_vs_the_academy.md#41-checkpoint-model>
[h-end]: <../two_paracosms_the_kingdom_vs_the_academy.md#end-state>
[g-pre]: <the_kingdom_dia_chinh_tri_dmz_quan_he_quoc_te.md#ii-mặt-ngoài-của-mẫu-quốc>
[g-dmz]: <the_kingdom_dia_chinh_tri_dmz_quan_he_quoc_te.md#iii-dmz--vùng-giao-tiếp-phi-quân-sự-lịch-sử>
[g-russia]: <the_kingdom_dia_chinh_tri_dmz_quan_he_quoc_te.md#iv-quan-hệ-lịch-sử-với-nga>
[g-trade]: <the_kingdom_dia_chinh_tri_dmz_quan_he_quoc_te.md#v-trao-đổi-hàng-hóa-thời-kỳ-đóng-cửa>
[g-invite]: <the_kingdom_dia_chinh_tri_dmz_quan_he_quoc_te.md#ix-mở-cửa-và-lời-mời-tôn-giáo>
[g-culture]: <the_kingdom_dia_chinh_tri_dmz_quan_he_quoc_te.md#x-trao-đổi-văn-hóa-như-mục-tiêu-mở-cửa>
[g-delegation]: <the_kingdom_dia_chinh_tri_dmz_quan_he_quoc_te.md#xiii-phái-đoàn-đầu-tiên-và-phạm-vi-hợp-lý>
[g-post]: <the_kingdom_dia_chinh_tri_dmz_quan_he_quoc_te.md#xiv-tương-quan-sức-mạnh-và-cách-thế-giới-ngoài-nhìn-mẫu-quốc>
[g-open]: <the_kingdom_dia_chinh_tri_dmz_quan_he_quoc_te.md#xvi-những-điểm-còn-mở-cần-quyết-định-sau>
[d-draft]: <the_kingdom_su_doan_xac_minh_va_stress_test.md#2-trình-tự-tiếp-đón-draft-có-thể-sửa>
[i-rings]: <the_kingdom_ha_tang_khong_luu_mo_cua.md#6-vành-đai-mở-cửa-và-mức-độ-tiết-lộ>
[i-sequence]: <the_kingdom_ha_tang_khong_luu_mo_cua.md#9-quy-trình-mở-cửa-hợp-lý>
[i-movement]: <the_kingdom_ha_tang_khong_luu_mo_cua.md#13-di-chuyển-của-phái-đoàn-trong-ngày-đầu>
[i-reveal]: <the_kingdom_ha_tang_khong_luu_mo_cua.md#14-nguyên-tắc-tiết-lộ-trong-giai-đoạn-mở-cửa>
[y-scan]: <the_kingdom_he_thong_suc_khoe.md#2-hệ-thống-kiểm-soát-bệnh-của-người-ngoài>
[s-embassy]: <the_kingdom_he_thong_phan_gian_va_kiem_soat_tri_thuc.md#ii-lớp-1--nhân-sự-đại-sứ-quán-tiền-tiêu>
[S]: <the_kingdom_he_thong_phan_gian_va_kiem_soat_tri_thuc.md>
[c-pre]: <TK_TIMELINE_INTERVAL_CP01_CP02.md#6-final-pre-cp2-state>
[m-example-1]: <the_kingdom_phuong_phap_sang_tac_fiction.md#xiii-không-escalation-chỉ-vì-checkpoint-trước-lớn>
[interval]: <TK_TIMELINE_INTERVAL_CP01_CP02.md>
[cp2]: <TK_TIMELINE_CP02_REVEAL.md>
