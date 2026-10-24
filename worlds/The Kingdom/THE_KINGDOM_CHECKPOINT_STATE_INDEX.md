# The Kingdom — Checkpoint State Index

```text
SOURCE_ID: TK-NAV-TIMELINE
ROLE: NAVIGATION
STATUS: ACTIVE
SCOPE: Điều hướng temporal owner, runtime/method và domain; không sao chép timeline hoặc tạo canon.
```

## 1. Cách đọc và thẩm quyền

```text
DOMAIN = persistent systems / world truth
METHOD = cách quan sát và truyền state qua fiction
CHECKPOINT = breakpoint / direct boundary delta
INTERVAL = progression và phản ứng tích lũy
INDEX = navigation
```

Repository chỉ externalize một phần paracosm. `INDEX != CANON OWNER`, `INDEX != DUPLICATE TIMELINE`, `SOURCE_ID != REGISTRY`, `HANDOFF != AUTOMATIC CURRENT STATE`. ACTIVE xác định vai trò source; không chấp nhận mọi proposal bên trong.

Giữ `CANON`, `USER-PROVIDED STATE`, `DECIDED`, `INFERENCE`, `PROPOSAL`, `UNDER CONSIDERATION`, `UNKNOWN`, `STALE`, `CONFLICTED`. Gap mặc định là `REPOSITORY GAP — author state not established here`, không suy thành tác giả chưa biết. `AUTHOR UNKNOWN`, `AUTHOR-KNOWN / REPO-UNKNOWN` và `REPO-KNOWN / SESSION-UNKNOWN` là các tình huống khác nhau; mở nguồn trước khi kết luận thiếu.

[README](README.md) giữ định hướng; [CI — epistemic state](The_Kingdom_CI_English_Compact_Revised.md#canon-and-epistemic-state) là tham chiếu kiểm soát, không chứng minh CI đang cài ở Project.

## 2. Temporal navigation

```text
CP1 → INTERVAL CP1–CP2 (≈ 2 YEARS) → CP2 → POST-CP2 MATERIAL
```

| SOURCE_ID | Vai trò / owner | Temporal boundary |
|---|---|---|
| TK-TL-CP01 | [CP1 — mở cửa](Sources/TK_TIMELINE_CP01_OPENING.md) | Pre-CP1 tối thiểu → breakpoint mở cửa → direct resulting boundary. |
| TK-TL-I01-02 | [Interval CP1→CP2](Sources/TK_TIMELINE_INTERVAL_CP01_CP02.md) | Sau boundary CP1 → ngay trước CP2; tiến trình và state tích lũy. |
| TK-TL-CP02 | [CP2 — đánh chặn / reveal](Sources/TK_TIMELINE_CP02_REVEAL.md) | Precondition tối thiểu → sự kiện / direct delta → immediate boundary. |
| TK-TL-POST02 | [Material hậu CP2](Sources/TK_TIMELINE_POST_CP02.md) | Sau reveal, chưa xác định end; suy luận phản ứng và premise tuyến Nga. Không gán CP3. |

Khoảng ≈ 2 năm theo [handoff gốc §4.1](two_paracosms_the_kingdom_vs_the_academy.md#41-checkpoint-model), không xác định ngày từng event. [Path dependence §4.2](two_paracosms_the_kingdom_vs_the_academy.md#42-path-dependence) không cho phép reset state hoặc đưa knowledge tương lai ngược về trước.

## 3. CP1 và interval

- [CP1 identity/provenance](Sources/TK_TIMELINE_CP01_OPENING.md#1-identity-và-phạm-vi): “Bắt đầu mở cửa / mở thương mại”; externalize từ lời tác giả được ghi trong handoff gốc, không nhập toàn bộ handoff vào canon.
- [CP1 S0](Sources/TK_TIMELINE_CP01_OPENING.md#2-trạng-thái-trước-checkpoint), [trigger](Sources/TK_TIMELINE_CP01_OPENING.md#3-trigger), [transition](Sources/TK_TIMELINE_CP01_OPENING.md#4-chuyển-tiếp-checkpoint-đã-xác-nhận), [direct delta](Sources/TK_TIMELINE_CP01_OPENING.md#6-direct-state-delta), [boundary](Sources/TK_TIMELINE_CP01_OPENING.md#7-trạng-thái-hậu-mở-cửa).
- [Interface](Sources/TK_TIMELINE_CP01_OPENING.md#5-interface-mở-cửa-liên-quan) phân biệt used / draft / persistent capability; domain implementation không thành event chỉ vì có link.
- [Interval known chronology](Sources/TK_TIMELINE_INTERVAL_CP01_CP02.md#3-known-chronology--events), [actor reactions](Sources/TK_TIMELINE_INTERVAL_CP01_CP02.md#4-actor-và-institutional-reactions), [final pre-CP2 state](Sources/TK_TIMELINE_INTERVAL_CP01_CP02.md#6-final-pre-cp2-state): không đồng nhất S1 tức thời với state tích lũy.
- [CP1 gaps](Sources/TK_TIMELINE_CP01_OPENING.md#9-những-cầu-nối-chưa-đủ-source) và [interval gaps](Sources/TK_TIMELINE_INTERVAL_CP01_CP02.md#7-repository-gaps) giữ nghĩa “mở thương mại”, itinerary, DMZ/deeper entry, phân bố tri thức và missing two-year history. Recovery có một số đoàn ban đầu, chưa có lịch từng đoàn.

## 4. CP2

[Owner CP2 §0](Sources/TK_TIMELINE_CP02_REVEAL.md#0-identity-boundary-và-recovery) liên kết identity hiện hành theo recovery và task migration. Mô tả hostile/aggression trong handoff gốc còn thiếu danh tính các nước/cơ quan; không mặc định mọi láng giềng là sponsor.

- [Premise reveal mới](Sources/TK_TIMELINE_CP02_REVEAL.md#01-premise-reveal-được-recovery): đội hình, Totem, trường lực, radar, vị trí neo và điều kiện quan sát.
- [Pháp sư / knowledge boundary](Sources/TK_TIMELINE_CP02_REVEAL.md#02-pháp-sư-và-giới-hạn-tri-thức): chức năng đã quyết định, biểu hiện cụ thể chưa hoàn thành.
- [Direct delta](Sources/TK_TIMELINE_CP02_REVEAL.md#03-direct-delta-và-boundary-state), [proxy politics](Sources/TK_TIMELINE_CP02_REVEAL.md#04-nền-chính-trị-chưa-được-khóa), [event-specific gaps](Sources/TK_TIMELINE_CP02_REVEAL.md#13-cầu-nối-còn-mở-sau-recovery).
- [Đánh chặn kế thừa §IV](Sources/TK_TIMELINE_CP02_REVEAL.md#iv-trình-tự-sự-kiện) vẫn là dàn dựng; [attribution §VI](Sources/TK_TIMELINE_CP02_REVEAL.md#vi-công-khai-hóa-attribution-bằng-hologram) giữ phân tầng trách nhiệm.
- [Phản ứng 1h/24h/72h](Sources/TK_TIMELINE_POST_CP02.md#4-material-phản-ứng-kế-thừa) và [tuyến vận tải Nga](Sources/TK_TIMELINE_POST_CP02.md#2-tuyến-vận-tải-nga-mẫu-quốc) có owner hậu CP2. Nhãn cũ gọi tuyến Nga là CP2 giữ `CONFLICTED / UNRESOLVED CHRONOLOGY LABEL`; không đổi thành CP3.

## 5. Runtime / authoring method

| SOURCE_ID | Owner | Giới hạn |
|---|---|---|
| TK-METHOD-FICTION | [Phương pháp fiction](Sources/the_kingdom_phuong_phap_sang_tac_fiction.md#xxix-temporal-ownership-và-runtime-xuyên-timeline) | World-state, checkpoint/interval, normalization; ví dụ checkpoint không là historical numbering. |
| TK-METHOD-POV | [POV / perspective](Sources/the_kingdom_pov_perspective_architecture.md#xxi-runtime-xuyên-timeline-và-recovery) | Chạy xuyên timeline; actor + time + available information. Các cơ chế nén POV vẫn giữ status proposal; kiểm thử narrative chưa chạy. |

Không có MC trung tâm, file mỗi POV hoặc ontology tree cho actor. World truth, observation, internal analysis, public information và social interpretation phải phân biệt.

## 6. Domain detail và giới hạn liên quan

| Domain owner | Anchor material |
|---|---|
| [Địa chính trị](Sources/the_kingdom_dia_chinh_tri_dmz_quan_he_quoc_te.md) | [DMZ §III](Sources/the_kingdom_dia_chinh_tri_dmz_quan_he_quoc_te.md#iii-dmz--vùng-giao-tiếp-phi-quân-sự-lịch-sử), [Nga §IV](Sources/the_kingdom_dia_chinh_tri_dmz_quan_he_quoc_te.md#iv-quan-hệ-lịch-sử-với-nga), [trade §V](Sources/the_kingdom_dia_chinh_tri_dmz_quan_he_quoc_te.md#v-trao-đổi-hàng-hóa-thời-kỳ-đóng-cửa). Quyền giao dịch không là quyền đại diện; DMZ không là nhập cảnh nội địa. |
| TK-DOM-INFRA — [Hạ tầng/không lưu](Sources/the_kingdom_ha_tang_khong_luu_mo_cua.md) | [Nền tảng §2](Sources/the_kingdom_ha_tang_khong_luu_mo_cua.md#2-nền-tảng-hạ-tầng-của-mẫu-quốc), [vành mở cửa §6](Sources/the_kingdom_ha_tang_khong_luu_mo_cua.md#6-vành-đai-mở-cửa-và-mức-độ-tiết-lộ). Type II và tích hợp phép–công nghệ là world truth, không tự thành tri thức người ngoài. |
| [Y tế](Sources/the_kingdom_he_thong_suc_khoe.md) | [Scan §2](Sources/the_kingdom_he_thong_suc_khoe.md#2-hệ-thống-kiểm-soát-bệnh-của-người-ngoài), [quyền lợi §6](Sources/the_kingdom_he_thong_suc_khoe.md#6-phân-tầng-quyền-lợi-y-tế); kiểm dịch không là quyền được chữa. |
| [Phản gián](Sources/the_kingdom_he_thong_phan_gian_va_kiem_soat_tri_thuc.md) | [Proxy/attribution §VII](Sources/the_kingdom_he_thong_phan_gian_va_kiem_soat_tri_thuc.md#vii-phản-gián-chủ-động-đối-với-proxy-và-khủng-bố), [gaps §XI](Sources/the_kingdom_he_thong_phan_gian_va_kiem_soat_tri_thuc.md#xi-những-lỗ-hổng-còn-cần-quyết-định). Không đặt toàn bộ capability vào ngày CP1/CP2. |
| [POT](Sources/the_kingdom_POT_personal_terminal_watch.md), [ngôn ngữ/tôn giáo](Sources/the_kingdom_language_religion_meta.md), [Law](Sources/THE_KINGDOM_LAW_V2_CONSOLIDATED.md) | Persistent domain; task này không đổi authority, Law design hoặc hoạt động CI. |

[Handoff phân tích gốc](two_paracosms_the_kingdom_vs_the_academy.md#end-state) vẫn là analysis/snapshot; [anti-drift](modular_engine_concept_anti_drift.md) không tự quyết định chronology. Câu hỏi/stress-test trong [sứ đoàn](Sources/the_kingdom_su_doan_xac_minh_va_stress_test.md) không phải transcript hoặc lịch sử.
