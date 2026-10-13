# Audit kiến trúc source-management AetherFire — 2026-09-26

Trạng thái: **AUDIT / PROPOSAL — CHƯA ĐƯỢC CHẤP NHẬN HOẶC KÍCH HOẠT**.

Đây là kết quả thực thi yêu cầu `07_CODEX_DEEP_ARCHITECTURE_AUDIT_AND_REVAMP_PROMPT.md`. Không thay canon, không đóng issue, không đổi CI/Router hiện hành. Các file `00`–`06` đầu vào đã được đọc toàn bộ, đối chiếu như giả thuyết; `PACKAGE_MANIFEST.json` cũng đã kiểm tra. Tám kích thước file trong manifest đầu vào đều khớp.

## Kết luận chính

Repository có kỷ luật authority và quarantine rõ hơn snapshot của proposal. `00` có đủ `60/70/80`; `80` tồn tại; `10` đã giữ giao diện ML thay vì copy toàn miền `70`; có builder và verifier tái lập. Không có căn cứ để làm một đợt “xóa duplicate 10–70” như kế hoạch ban đầu.

Điểm cần ưu tiên là **quản lý phiên bản đồng bộ của cả gói, đầu vào biên tập thật của builder, dependency có kiểu, và bằng chứng cho phép đọc từng node**. Chỉ thêm registry/node index lên trên builder hiện tại sẽ giữ nguyên các nguy cơ cập nhật dở dang và tạo thêm một tầng đồng bộ thủ công.

## Cách đọc kết quả

| Tài liệu | Nội dung |
|---|---|
| [02](02_CONFIRMED_BREAKPOINTS.md) | 15 finding có bằng chứng, trigger, tác động, guardrail và hướng sửa |
| [03](03_ADDITIONAL_RISKS_FOUND.md) | Rủi ro bổ sung, gồm các lỗi abstraction trong proposal |
| [04](04_TARGET_ARCHITECTURE.md) | Kiến trúc đích, ownership, giao dịch và lập luận mở rộng 10 lần |
| [05](05_MODULE_AND_INTERFACE_SCHEMA.md) | Hợp đồng schema, ví dụ, identity, edge, issue, snapshot |
| [06](06_CI_VNEXT_PROPOSAL.md), [07](07_ROUTER_VNEXT_PROPOSAL.md) | Đề xuất CI/Router; không phải file kích hoạt |
| [08](08_MIGRATION_PLAN.md) | Các bước, điều kiện chuyển bước, rollback |
| [09](09_VALIDATION_AND_REGRESSION_PLAN.md) | Kết quả đã chạy, kế hoạch hồi quy, ma trận C/D của yêu cầu |
| [10](10_OPEN_DESIGN_DECISIONS.md) | Những quyết định cần chốt trước triển khai |

Nhãn `OBSERVED` chỉ điều đã đọc/đo/thử; `INFERENCE` là hệ quả có điều kiện; `PROPOSAL` là thiết kế chưa được chấp thuận; `UNKNOWN` là giới hạn bằng chứng. Dòng trích dẫn dưới đây dùng số dòng tại snapshot audit, không dùng làm identity lâu dài.

## 1. Baseline và trạng thái điều khiển

| Trường | Bằng chứng hiện tại |
|---|---|
| Repository | `C:/Users/Sheeplark/Desktop/CI Versioning Audit & Changelog` |
| Phạm vi | `AetherFire Project/` và đúng các dependency được viện dẫn ở repository cha |
| Nhánh khi bắt đầu | `codex/miniconcept-ci-v2-2` |
| HEAD | `f4b7780ac3090dd486cde9bdbe6340ca10cdd9c1` |
| Nhánh lưu kết quả | `codex/aetherfire-architecture-audit-20260926`; cùng HEAD |
| GitHub `main` | `67fef7fa8ce7d3a4791ee728560f69edf24da637`, xác minh bằng `git ls-remote`; không fetch/push |
| CI mặc định cục bộ | `AetherFire CI/AetherFire_CI_version_v2.6.md` |
| Router của CI này | `Anti-Drift Source/AetherFire_Anti_Drift_Source_Router_v3.2.md` |
| Nền phát triển CI được khai báo | `ChatGPT v8.5`; không suy rằng phải tải đồng thời hai CI vào runtime |
| CI/Router thử nghiệm | `GitHub_Only_Experiment/` chứa v2.7/v3.3, cần kích hoạt rõ ràng |
| ChatGPT Project đã cài gì | **UNKNOWN**; repository không chứng minh cấu hình đã upload/cài |

Căn cứ: CI README mục “Activation” và “Active baseline”; Router v3.2:11–46; CI v2.6:35–43; README vùng thử nghiệm:3–7. Đã kiểm kê trực tiếp các file đủ điều kiện. Không thấy collision phiên bản hiện tại. Quy tắc hiện hành chọn số lớn nhất trong direct children **sau** khi loại draft/rejected/superseded bằng status; tên mới nhất tự nó không chứng minh canon.

Trạng thái dirty khi bắt đầu:

- xóa từ trước `../ChatGPT Plus+ Era/chatgpt v8.5.1.txt`;
- chưa theo dõi: gói proposal đầu vào, `New Canon and Consideration/`, `Source_Archive/internal_first_worldbuilding_core_philosophy.md`, `../ChatGPT Plus+ Era/chatgpt v8.6.txt`, `../The Academy Project/`.

Không nhận ownership hoặc stage các thay đổi này. Baseline hash ghi đủ **98 file có sẵn** trong phạm vi AetherFire trước khi tạo thư mục kết quả; xem `evidence/baseline_hashes.json`. `git_status_before.txt` được lưu ngay sau khi tạo thư mục báo cáo nên có thêm chính thư mục kết quả; danh sách trên phản ánh status đọc trước lần ghi đầu tiên.

`main` và local HEAD khác nhau ở 11 đường dẫn AetherFire. Các commit liên quan chưa có trên `main`: `ce707c1`, `ded0428`, `2d6652d`, `28cdcaa`. `10`–`80` không khác giữa hai Git tree; `90`, builder, manifest và một số controls khác. File promotion workflow ở local viện dẫn `main` làm canon xuất bản; Router mặc định vẫn là bộ nạp package. Audit không tự hợp nhất hai miền authority này và không gán local-only thành đã xuất bản.

## 2. Inventory và độ bao phủ

Trước báo cáo: 98 file, gồm 84 Markdown, 10 JSON, 2 PowerShell, 2 `.gitattributes`. Toàn bộ danh sách, hash và thống kê ở `evidence/static_audit.json`.

| Nhóm | Inventory / vai trò |
|---|---|
| Current domain | 8 file `10`–`80`; authority có phạm vi, không phải mọi đoạn đều là khẳng định đã chốt |
| Generated | 12 file `00`, `10`–`80`, `90/91/92`, cộng `MANIFEST.md` |
| CI | 7 phiên bản v2.0–v2.6; bản compact/legacy, README, promotion workflow; không nhập vào canon |
| Overlay active candidates | Economy v1.1; Modular v1.0; Mortality v1.1; Total War v1.1; Worldbuilding v1.1 |
| Lịch sử controls | 10 file dưới `Anti-Drift Source/Source_Archive/`; routers cũ trong CI bị README loại |
| Archive package | 28 Markdown thực tế; 27 được manifest liệt kê; 24 lệnh đọc source trực tiếp trong builder |
| Candidate | 1 Markdown trong `New Canon and Consideration/`; không tự active dù bytes trùng một bản archive |
| Kiểm tra | Runner PowerShell + README + 9 JSON case `DRAFT` |
| Schema cấu trúc | Chưa có module/node/interface schema hoạt động trong inventory này |
| Verifier | Có trong skill người dùng, **ngoài repository**; không nên nói repository không có khả năng kiểm chứng |

### Số đo thực tế

Heading đếm theo regex, có thể gồm heading trong code fence. `UNKNOWN` là số dòng có token `UNKNOWN` hoặc `NOT ESTABLISHED`, không phải số sự kiện thiếu canon. Tỷ lệ = số dòng này / tổng dòng, không là quality score. Cột Git là số commit chạm đường dẫn trong toàn lịch sử reachable từ HEAD, không follow rename; không phải giờ công hoặc tốc độ phát triển.

| File | Bytes | Dòng | Heading | Dòng UNKNOWN | Tỷ lệ | Commit |
|---|---:|---:|---:|---:|---:|---:|
| 10 | 57,725 | 1,262 | 80 | 32 | 2.54% | 3 |
| 20 | 39,889 | 1,592 | 76 | 24 | 1.51% | 1 |
| 30 | 87,784 | 4,163 | 180 | 14 | 0.34% | 2 |
| 40 | 39,611 | 1,560 | 80 | 8 | 0.51% | 2 |
| 50 | 20,683 | 1,063 | 47 | 1 | 0.09% | 1 |
| 60 | 3,361 | 68 | 7 | 6 | 8.82% | 1 |
| 70 | 18,154 | 873 | 55 | 7 | 0.80% | 1 |
| 80 | 15,468 | 427 | 21 | 8 | 1.87% | 1 |
| 90 | 131,474 | 4,060 | 206 | 34 | 0.84% | — |
| 91 | 44,653 | 640 | 54 | 46 | 7.19% | — |
| 92 | 13,659 | 105 | 10 | 42 | 40.00% | — |

`92` chứa bảng issue và trích nhiều ID evidence; 61 ID khác nhau được regex tìm thấy **không phải 61 active issues**. Dữ liệu raw giữ riêng số ID và cross-reference để tránh đánh đồng. Issue cục bộ không có ID vẫn tồn tại, chính `92`:105 thừa nhận phạm vi không đầy đủ.

Đề xuất độ phủ theo task: `60` đủ tra cứu identity được xác lập, không đủ cơ chế switching/định lượng; `70` đủ ranh giới quyền lực đã ghi, không đủ toàn bộ Creed/constitution; `80` đủ phân biệt capability–authority, không đủ throughput; `20/30` sâu về các route được mô tả nhưng vẫn có giao diện chưa chốt. Đây là đánh giá phạm vi đọc, **không cấp nhãn OPERABLE cho cả module**.

## 3. Đối chiếu toàn bộ BP trong proposal

| BP | Kết luận tại repository | Finding / xử lý |
|---|---|---|
| 01 | Xác nhận quy tắc full-file; tác hại LLM chưa đo | AR-07 |
| 02 | Bác bỏ tình trạng `00` bỏ 60/70; rủi ro nhiều inventory vẫn còn | AR-08 |
| 03 | Bác bỏ mirror ML lớn trong `10` hiện tại | AR-15: summary có chủ đích, cần cơ chế cập nhật |
| 04 | Đúng: nhiều khai báo topology, nhưng builder đã là nguồn sinh | AR-08/04 |
| 05 | Đúng một phần: có giới hạn prose; thiếu metadata kiểm chứng theo task | R-03 |
| 06 | `10` đa miền; không kết luận phải split ngay | AR-07, kế hoạch thử node trước |
| 07 | Có split ML thực tế, thiếu protocol tổng quát | R-01/R-05 |
| 08 | Rủi ro có điều kiện; không suy graph thực tế là O(n²) | R-06 |
| 09 | Dependency có trong prose, chưa thành graph kiểm được | AR-09 |
| 10 | Chưa có reverse graph đầy đủ | AR-09 |
| 11 | Rủi ro tăng trưởng; `92` hiện 105 dòng, chưa monolith | AR-11, không tạo issue database ngay |
| 12 | `91` có nhiều lớp addendum; chưa đo chi phí truy xuất | AR-10/11 |
| 13 | `90` 4,060 dòng đúng; không đủ để chứng minh cần tách | AR-07/14 |
| 14 | Bác bỏ “không thấy generator/hash”; có builder, manifest, verifier | AR-01/02/04, vấn đề ở contract sâu hơn |
| 15 | Thiếu kiểm đăng ký đầy đủ | AR-08/13 |
| 16 | Có phát hiện byte drift/rebuild; thiếu freshness về nghĩa/controls | AR-10/15 |
| 17 | Có authority boundary bằng prose, thiếu record chuẩn | AR-09/15; sửa thiết kế R-02 |
| 18 | Có domain contract prose, chưa có schema máy đọc | 05 |
| 19 | Vocabulary chưa chuẩn metadata; typed relation discipline đã có | R-04, glossary 05 |
| 20 | Guardrail tách graph đã có ở CI/Modular/index | Giữ; không báo như lỗi đã xảy ra |
| 21 | 493–1,085 dòng/overlay; full-read chuyển tải context sang controls | AR-12 |
| 22 | Dependency Mortality có prose rõ; World→Economy phân tán; thiếu validator | AR-12 |
| 23 | Chưa có architecture schema/version contract | R-08 |
| 24 | Có promotion workflow; chưa có publication transaction tự động | AR-02/06 |
| 25 | Có orphan prose và issue; không cần registry orphan riêng | AR-09/R-05 |
| 26 | Có giới hạn nguồn và MUST_OPEN/MAY_STOP; chưa đủ schema theo task | R-03 |
| 27 | Bác bỏ “không có structural tests”; runner/verifier có nhưng hẹp | AR-05/13 |
| 28 | Chưa có impact graph; enum “budget” không giải quyết đầy đủ | AR-09/R-06 |
| 29 | Đúng: filename/heading gánh identity; ID đề xuất lại dính owner | R-01 |
| 30 | Rủi ro đúng và xuất hiện ngay trong thiết kế registry giao diện | R-02/R-04 |

Phần 1.1 proposal dùng số đo từ snapshot khác (`10`:2,122 dòng; hiện 1,262). Phần 1.4 chỉ nói không có `80` trong gói cung cấp; không được diễn giải thành source đã mất ở repository.

## 4. Duplication, authority và giao diện

Phép dò exact xét block liên tiếp ≥3 dòng và ≥120 ký tự; near xét paragraph ≥120 ký tự, Jaccard từ ≥0.65, độ giống ký tự ≥0.85. Đây là ngưỡng tìm ứng viên, không chứng minh tương đương ngữ nghĩa. Trong các cặp current file và cặp active controls, không có block đạt hai tiêu chí này; vẫn có một vài dòng chung dài ≥40 ký tự. Không thể suy “không có duplication ngữ nghĩa”.

Đối chiếu thủ công:

| Vị trí | Phân loại | Kết luận |
|---|---|---|
| `10`:1219–1255 ↔ `70`:1–873 | Summary có chủ đích | `10` chỉ rõ `70` kiểm soát nội bộ; không có block 240 dòng như proposal |
| `10`:1100 trở đi ↔ `80`:1–427 | Summary có chủ đích | Aviation có owner rõ, nhưng summary chưa gắn revision của owner |
| `20`:74 ↔ `30`:87,1139–1300 | Nhắc lại ranh giới giao diện | White/status cần hiện ở cả hai scope; không có bằng chứng hai controlling owner mâu thuẫn |
| `50`:3–6 ↔ `40`:3–5 | Tham chiếu authority | Timeline và narrator tách rõ; clothing bị loại khỏi `50` |
| Total War:414–418 ↔ `80` | Hook canon trong control | Không thành authority mới, nhưng cần consumer edge để retcon không bỏ sót |
| CI/overlay lặp UNKNOWN, agency, power≠authority | Lặp invariant có chủ đích | Không xóa chỉ để giảm dòng; kiểm tương thích khi phiên bản thay đổi |
| Candidate RP ↔ archive RP | Bảo tồn provenance, cùng SHA | Hai vai trò khác nhau; không phải bản canon trùng cần xóa |
| Economy legacy, Modular legacy ở hai archive/control vị trí | Bảo tồn lịch sử, cùng SHA | Không activate bằng tìm kiếm hoặc tên |

Không xác nhận được một **authority conflict giữa các current canon owner** trong các ranh giới được đối chiếu. Khác biệt local/published snapshot là vấn đề miền xuất bản; hai nguồn “current-looking” không tự chứng minh hai claim canon mâu thuẫn.

## 5. Dependency và reverse impact đại diện

Các tập dưới đây là **tập consumer tìm được**, không tuyên bố closure đầy đủ:

| Premise/ranh giới | Consumer hiện có | Điểm còn thiếu |
|---|---|---|
| MC4 identity/Academy | `60` → Academy trong `10`; cross-world ở `40`; issues 025/026/028; builder:1213 | Không có graph đảm bảo mọi consumer của node identity đã tìm hết |
| ML relic access | `70` §§9–11; summary `10`; issue AF-ML-006; `91` authority integration; literal builder:638 | Topic similarity không chứng minh relic catalogue và seal relic cùng một vật |
| AF–TE transfer | `70` §§16–17; `30` boundary; `10` summary; issues AF-ML-007/008 | Một interface có nhiều mặt: event, status law, operation; không gán hết cho một domain |
| Aviation sole-confirmed | `80`; `10` summary; `91/92`; Total War:414–418; case `stable_aviation_supremacy.json`; builder:231–246 | Có consumer control/test ngoài current files; static test không xác nhận model giữ nghĩa |
| White → Citizen | `30` §§19–24; `20` ontology/career/route; `00`; `91` AF-CX-005/007; `92` | Độ sâu nguồn không giải quyết unknown criteria; search không thành impact proof |

Chu trình `10`↔`70`, `10`↔`80`, `40`↔`50` ở cấp dẫn chiếu không tự là lỗi. Cần phân biệt nạp bằng chứng, sinh output, thẩm quyền và genealogy trước khi chạy cycle check.

## 6. Giới hạn đọc và kiểm chứng

- Đọc đầy đủ: toàn gói proposal; active CI/Router; CI README/promotion workflow; `00/92/MANIFEST`; `10/60/70/80`; Modular và Worldbuilding; runner/README.
- Đọc theo luồng cấu trúc/đoạn liên quan: builder (helpers, đọc input, write path, literal blocks, issue/manifest generation); `20/30/40/50/90/91` (header, boundary, issue/evidence, các đoạn đối chiếu); Economy/Mortality/Total War (activation, dependencies, scope clamp và source hook). Các dòng/section được viện dẫn đã mở trực tiếp.
- Máy đọc toàn byte của 98 file để inventory/hash; đo text và similarity trên nhóm đã nêu. Không gọi đó là đọc ngữ nghĩa toàn bộ canon. Archive không được mở hàng loạt làm baseline; chỉ dùng provenance tên/bytes và input build cô lập.
- Không audit mọi mệnh đề lore, không chứng nhận canon-complete hoặc graph ngữ nghĩa hoàn chỉnh. Source snippets ngoài package thiếu được phân loại là provenance gap, không phủ định nội dung trong canon hiện tại.
- Có kiểm thực thi script trên bản sao; không chạy model, không thử live ChatGPT, không thay nguồn thật. Bộ kết quả này hoàn tất phạm vi audit/design cấu trúc, không phải chứng nhận sẵn sàng migration.
