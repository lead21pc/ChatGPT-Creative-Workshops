# Kế hoạch migration có cổng kiểm chứng

Trạng thái: **PROPOSAL**. Pass hiện tại chỉ hoàn tất audit/design/prototype độc lập; các giai đoạn triển khai bên dưới cần được chấp nhận theo phạm vi. Không dùng bảng này làm quyền tự sửa canon.

## 1. Baseline phải chọn trước

Phải quyết định gói đích là GitHub `main` đã xác minh hay local chain có các thay đổi chưa công bố. Không âm thầm mang `90`/Worldbuilding/promotion workflow local-only vào release từmain. `10`–`80` giống nhau không khiến toàn control/package tương đương.

Giữ dirty inputs hiện có; không broad stage. Tạo checkout/nhánh phù hợp từ base đã chọn cho implementation. Mọi output audit ở thư mục này vẫn PROPOSAL và không vào resolver directory.

## 2. Các giai đoạn

| Giai đoạn | Thay đổi được đề nghị | Điều kiện vào / bằng chứng ra | Rollback / giới hạn |
|---|---|---|---|
| P0 — Audit | Bộ10 tài liệu, evidence,3 prototype | Hoàn tất ở pass này; lỗi package baseline được ghi rõ | Không ảnh hưởng controls/canon; chưa là readiness migration |
| P1 — Chốt hợp đồng | Scope/identity/status/activation/snapshot/schema draft và base | Quyết định design ở10; invariant matrix; schema được review | Có thể bác bỏ toàn proposal; chưa thay runtime |
| P2 — Gia cố kiểm chứng cũ | Verifier versioned trong repo; resolver parity; build staging/snapshot/preconditions có phạm vi | Tái hiện AR-02/03/05; local package inventory được xử lý theo quyết định riêng; current outputs byte-equivalent | Không ghép lore delta; checkpoint chỉ khi task checks đạt; không regenerate live để che FAIL |
| P3 — Shadow catalog | Whole-file mappings cho8 current domains và active control families; source/edit/provenance bindings | Registration bijection; no active runtime read từ shadow; unknown review giữ UNASSESSED | Xóa khỏi activation candidate là đủ; giữ evidence lịch sử |
| P4 — Làm rõ đầu vào biên tập | Tách curated literals khỏi builder sang Markdown inputs theo từng nhóm | Decision scope mapping, baseline output equivalence, archive byte preservation, provenance chain | Revert nguyên nhóm input+recipe+manifest; không revert một output lẻ |
| P5 — Shadow node routing | Pilot trên60, ranh giới70, aviation80 và context10; whole-file fallback cho phần còn lại | Segmentation đầy đủ, source/ref/issue/negative evidence review; paired old/new routing plan | Router3.2 vẫn active; không giảm full-read thật trước gate |
| P6 — Bật node read-only có giới hạn | Activate cặp controls+schema+snapshot đã review cho đúng task classes | Structural PASS, evidence oracle pass, semantic test được duyệt; installed environment được xác minh | Rollback whole compatible release; mutation qua pipeline mới chưa bật |
| P7 — Đồng bộ issue/view | Chuyển seed+literal92 thành records theo owner, projection00/92; summary review fingerprints | Bảo toàn IDs/raw statuses/resolution evidence, không mất local unknown, generated determinism | Không dùng92 làm file sửa tay tạm; rollback records+generator+views cùng nhau |
| P8 — Bật mutation transaction | Reverse impact, base revision check, stage/validate/publish receipt | Các tình huống local/cross-domain/transfer/retire/promotion đều đạt trên fixture; approval publication riêng | Không công bố partial; không push/merge chỉ vì local acceptance |
| P9 — Mở rộng theo nhu cầu | Thêm module/pilot scope; split90/91 hoặc paths khi có lợi ích đo được | Đủ invariants, task/evidence coverage và chi phí bảo trì được đo | Không cần chuyển folder toàn repo; IDs giữ nguyên |

P4 có thể chia rất nhỏ, không bắt chuyển tất cả canon sang input layout mới trước pilot. Khi generated pipeline cũ còn tồn tại, node map bind vào output byte revision; input edit vẫn đi qua recipe cũ đã pin. Không được duy trì hai editing owner cho cùng claim.

P7 có thể xây shadow sớm, nhưng activation cùng bộ sources/controls đã kiểm. Thứ tự thực tế được điều chỉnh theo dependencies đã chứng minh, không theo số file trong proposal đầu vào.

## 3. Pilot cụ thể

| Pilot | Vì sao chọn | Phải giữ | Chưa làm |
|---|---|---|---|
|60 identity | Nhỏ, có dependency Academy và unknown rõ | Whole-file node ban đầu; không import legacy powers | Không gán OPERABLE cho switching simulation |
|70 relic/quorum | Có nhiều qualifier, interface và issue005/006 | Quorum/loan/oath khác thủ tục nếu source chưa nối; owner30/40 khi chạm scope | Không resolve relic catalogue hoặc Creed mechanics |
|80 airspace | Có distinction capacity/authority, route geopolitical và control consumer | AF-AV-002→AF-OPEN-016, current-stage UNKNOWN, TotalWar hook | Không thăng strategic direction thành implementation |
|20/30 White | Kiểm cross-status và exception | White ở Undie đến khi transition hoàn tất, issue criteria | Chưa chọn node cutpoints trước review toàn affected source |

Không dùng một pilot “dễ” để tuyên bố all-domain equivalence. Khi mở20/30 trong implementation semantic phase, phải đọc đủ affected current domain theo controls còn hiệu lực; audit cấu trúc hiện tại không thay phần đó.

## 4. Mapping hiện tại → đích

| Hiện tại | Shadow | Sau migration được duyệt |
|---|---|---|
|00 | Toàn file source-map reference | Generated navigation từcatalog/scopes; các truth boundaries chuyển vào owner được duyệt, không bị mất |
|10–80 | Read-current whole-file binding, generated=true | Source nodes có context; current outputs vẫn giữ authority scope đã accepted |
|Builder literals | Mark `curated_literal` + evidence | Markdown editing inputs + recipe xác định |
|Source_Archive | Byte-exact snapshot, import role | Không sửa file cũ; nguồn mới admission riêng |
|90 | History source, full-read khi cần | Có history nodes; chỉ split khi task/cadence/concurrency có bằng chứng |
|91 | Evidence records/section locators khóa revision | Record IDs ổn định; summary nếu chia shard có lý do |
|92 | Generated seed+literal mapping | Projection issue records; preserve raw states và closed records |
|CI/Router/overlays | Active pair pinned cho shadow comparison | Explicit release activation; payload control giữ ranh giới riêng |
|tests DRAFT | Giữ nguyên lifecycle/anchors | Thêm structural fixtures riêng; semantic activation phải được duyệt |

## 5. Stress-test giao dịch trước activation

| Tình huống giả lập | Luồng bắt buộc | Không được làm |
|---|---|---|
| Local retcon | Scope decision → owner input → consumers/summary/issue → validate | Chỉ sửa generated node |
| Cross-domain retcon | Collect affected facets/owners → full affected evidence → update bắc cầu → publish một generation | Lấy module nhiều mention làm global owner |
| Authority transfer | Quyết định tài liệu riêng → remove old scope claim/add new claim cùng snapshot → aliases/consumers → overlap check | Hai owner exclusive active tạm thời |
| Module retirement | Tombstone → kiểm mọi active consumer → remap có scope hoặc block → release | Xóa path rồi để search tìm bản archive |
| Proposal được canonize | Exact scoped acceptance → provenance byte-exact → approved import mapping → carried-open issue list | Canonize toàn file vì một đoạn được đồng ý |
| Crash sau edit | Base snapshot vẫn active; incomplete staging bị loại | Công bố manifest mới trước đủ outputs |
| Hai branch đổi cùng node/interface | Compare base/review scope/IDs, revalidate affected closure | Chọn bên có version cao hoặc timestamp mới |
| Rollback qua schema version | Pin whole compatible controls/schema/source bundle | Router mới parse metadata cũ bằng đoán |

Các tình huống này là kế hoạch acceptance, không sự kiện canon. Expected result của một case có thể là BLOCKED/REVIEW_REQUIRED, không phải luôn PASS nội dung.

## 6. Git và artifact policy

Checkpoint theo milestone đã kiểm, stage đúng file của tác vụ, xem check/stat/full staged diff. Tách commit cơ học và commit semantic delta. Không dùng diff sạch để chứng nhận authority review. Khi kiểm package thất bại vì trạng thái baseline, ghi rõ và giải quyết bằng quyết định đúng ownership; không commit với lời mô tả “verified package” sai.

Generated current files đã là artifact được repository theo dõi; tiếp tục commit theo policy này trong migration. Cache graph/report tạm có thể không commit; release manifest và validation receipt cần được giữ đủ để audit. Generated merge conflict phải được rebuild từ nguồn hợp nhất, không sửa tay cho hết conflict.

Không push, tag, release, merge hoặc PR nếu chưa có yêu cầu rõ. Đây là các bước riêng khỏi chấp nhận thiết kế/acceptance local.
