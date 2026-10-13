# Các breakpoint được xác minh

Trạng thái: **AUDIT / PROPOSAL**. Các mức độ nói về source-management, không phán quyết canon. `BREAKPOINT_NOW` gồm lỗi đã quan sát ở checkout hoặc đã tái hiện bằng mã hiện hành trong sandbox; không có nghĩa nguồn thật đã chịu mọi failure mô tả. Mọi hướng sửa dưới đây chưa triển khai.

## AR-01 — Inventory archive làm verifier thất bại hiện tại

- **Severity / trạng thái:** `BREAKPOINT_NOW / OBSERVED`.
- **Evidence:** `MANIFEST.md` bảng archive có 27 mục; archive thực có 28. `evidence/package_verifier.txt` báo đúng hai lỗi: `Archive inventory mismatch: internal_first_worldbuilding_core_philosophy.md [=>]` và `Rebuilt MANIFEST.md differs from live manifest.`
- **Current mechanism:** builder:1572–1577 hash mọi Markdown direct child, kể cả file không được đọc để tạo canon. File bổ sung là untracked từ trước.
- **Failure trigger → mode:** đặt một source mới vào archive mà chưa cập nhật manifest → toàn bộ gói bị báo FAIL dù canon output không đổi.
- **Impact:** readiness của provenance/build không đồng nhất với readiness của canon. 12 generated và 27 hash đã liệt kê đều khớp; không gọi đây là lỗi canon hoặc mất dữ liệu.
- **Guardrail:** verifier bắt được; runner chỉ kiểm presence nên không bắt. Rebuild tự bổ sung hash không xác nhận nguồn đã được chấp nhận.
- **Global solution hook:** snapshot inventory với vai trò input/không-import/provenance rõ; tách trạng thái admission khỏi sự hiện diện.
- **Local remediation:** tác vụ riêng quyết định vai trò file này rồi cập nhật manifest theo quyết định; không tự di chuyển/xóa/nhập trong audit.
- **Migration risk:** “làm verifier xanh” bằng regenerate có thể che việc đưa file chưa phân loại vào release. Giữ admission gate, không biến hash thành canon.

## AR-02 — Builder không công bố output như một giao dịch

- **Severity / trạng thái:** `BREAKPOINT_NOW / OBSERVED trong sandbox`.
- **Evidence:** builder:101–109 dùng `WriteAllText` trực tiếp; các write tại 393,716,718,720,785 trước luồng Undie:787; manifest chỉ ghi ở1643. `sandbox_probes.json/partial_write_failure` tái hiện exit1, 5 file đã viết và 7 file giữ generation trước.
- **Current mechanism:** đọc nguồn, biến đổi và ghi xen kẽ. Không có lock, staging generation hay compare-and-swap base revision trong script đã kiểm.
- **Failure trigger → mode:** anchor thiếu sau lần ghi đầu, process dừng, hoặc hai builder xen kẽ → gói có nhiều generation.
- **Impact:** người đọc có thể dùng một phần authority transfer/retcon; manifest cũ không bảo vệ người đọc nếu họ không kiểm nó.
- **Guardrail:** `ErrorActionPreference=Stop` dừng thao tác tiếp, không hoàn tác file đã ghi. Git hỗ trợ phục hồi lịch sử nhưng không làm working tree atomic.
- **Global solution hook:** input snapshot bất biến → build vào staging → verify → công bố một generation được pin. Đọc từ Git tree/bundle bất biến, không đọc thư mục đang viết.
- **Local remediation:** trước migration, chỉ build bản sao và so sánh toàn bộ; thiết kế writer có base-hash guard. Sửa này cần nhiệm vụ triển khai riêng.
- **Migration risk:** atomic rename từng file vẫn không atomic cho cả gói; một pointer chỉ có ích nếu mọi reader pin và kiểm generation ấy.

## AR-03 — Reconciliation phụ thuộc chuỗi và parser không hiểu Markdown

- **Severity / trạng thái:** `BREAKPOINT_NOW / OBSERVED trong sandbox`.
- **Evidence:** builder:20–68 dùng `IndexOf`/heading để lấy range;83–98 dịch heading bằng regex;111–124 `Replace-Required` chỉ kiểm có ít nhất một lần;239 dùng `.Replace` không kiểm số lần. Probe `silent_replacement_miss`: exit0 và sentinel chưa reconcile đi vào `80`; `heading_in_fence`: `# literal` thành `## literal` bên trong code fence.
- **Current mechanism:** trộn phép thay bắt buộc, thay tùy chọn và phép cắt section theo chuỗi. Thiếu pre/postcondition xác nhận số lượng occurrence và ranh giới cú pháp.
- **Failure trigger → mode:** wording đổi, heading lặp hoặc `#` nằm trong fence → không thay, thay quá rộng hoặc cắt sai; build có thể vẫn thành công.
- **Impact:** tái lập đúng một lỗi vẫn cho cùng hash. Không kết luận current output đang có semantic corruption từ probe tổng hợp.
- **Guardrail:** anchor bắt buộc bắt một số thiếu chuỗi; verifier chỉ đối chiếu bytes với cùng generator nên không chứng minh nghĩa.
- **Global solution hook:** recipe có ID, selector được khóa revision, expected cardinality, assertions và source map; chỉ dùng Markdown parser khi thực sự cần cắt cấu trúc.
- **Local remediation:** phân loại các replacement đang là optional/intended; thêm kiểm occurrence vào recipe đã duyệt, không sửa đồng loạt logic canon.
- **Migration risk:** thay parser có thể làm đổi whitespace, fences, heading hoặc phạm vi import; yêu cầu byte-equivalence trước semantic delta riêng.

## AR-04 — Builder chứa văn bản biên tập và dependency đọc nhưng không dùng

- **Severity / trạng thái:** `MAINTENANCE_DEBT / OBSERVED`.
- **Evidence:** builder:203–207 đọc `$mc4Source`, `$academySource`, `$rfAxesSource`, `$rfGeopoliticsSource`, `$taintedCosmosMerged`; mỗi biến chỉ có một occurrence trong script. MC4 output là here-string:1213–1283; RF:446, Academy:527, ML summary:638. `$rpHistory` được đọc và kiểm 5 anchor:190–195, không nội suy vào output.
- **Current mechanism:** một số source là căn cứ biên tập/provenance; bản được curate nằm trong code. Không phải mọi input được đọc đều chảy text vào output.
- **Failure trigger → mode:** thêm/chỉnh nguồn được phép rồi tưởng builder tự import → output không đổi; source không dùng cho text bị thiếu vẫn làm toàn build dừng.
- **Impact:** editing owner thực nằm rải giữa archive bất biến và literal trong builder; registry trỏ generated file không giải quyết điều này.
- **Guardrail:** workflow yêu cầu đọc output và explicit acceptance; có tác dụng nếu làm đúng, chưa có source map máy kiểm.
- **Global solution hook:** tách read authority, editable input, provenance dependency và transform recipe; đưa literal đã duyệt sang Markdown biên tập trong giai đoạn riêng.
- **Local remediation:** trước mắt ghi nhãn `curated_literal`, `presence_only`, `transformed_input` cho từng build dependency. Không bỏ dependency chỉ vì variable không được dùng.
- **Migration risk:** sao chép generated thành input có thể giữ lại marker history hoặc bỏ mất một phép reconcile. Migration phải chứng minh nội dung và decision mapping được bảo toàn.

## AR-05 — Resolver của runner khác resolver trong Router

- **Severity / trạng thái:** `BREAKPOINT_NOW / OBSERVED trong sandbox`.
- **Evidence:** Router:25 loại draft/rejected/superseded và29 yêu cầu kiểm header/README; runner:68–112 chỉ nhận tên,139–148 chỉ enumerate tên file. Probe thêm CI2.99 header `Status: DRAFT` vào bản sao: runner chọn nó, overall `LIMITED_CHECK`, exit0.
- **Current mechanism:** kiểm version numeric đúng nhưng chưa thực thi bước eligibility/status của hợp đồng.
- **Failure trigger → mode:** một bản draft có tên chuẩn nằm trong resolver directory → test neo vào control không được Router cho active.
- **Impact:** kết quả kiểm control không đáng dùng làm chứng nhận active resolution ở trạng thái đó. Baseline hiện tại vẫn chọn đúng2.6/3.2, không nói đang kích hoạt nhầm.
- **Guardrail:** isolation GitHub_Only hiện chặn experimental pair; anchor warning không sửa việc chọn candidate draft.
- **Global solution hook:** activation manifest pin cả cặp control; cùng một resolver thuần cho tool và hợp đồng đọc.
- **Local remediation:** parity tests header/README conflict, draft, numeric alias, unreadable candidate; sau đó sửa resolver có phạm vi.
- **Migration risk:** thay auto-latest thành explicit activation là đổi hợp đồng, cần phê duyệt; không kích hoạt version đề xuất chỉ do tên.

## AR-06 — Chưa có snapshot thống nhất của controls, canon và môi trường dùng

- **Severity / trạng thái:** `BREAKPOINT_SOON / OBSERVED + INFERENCE`.
- **Evidence:** README CI:9–22 phân biệt installed Project và local; workflow promotion:7 định danh canon GitHub main; Router:51–65 dùng package; CI:37 pin Router3.2 trong khi runner tự resolve họ Router. `main=67fef7f`, localHEAD=`f4b7780`, 11 path khác ở AetherFire.
- **Current mechanism:** control version, package current, Git branch và Project upload có các cách cập nhật riêng; chưa có tuple được kiểm chung.
- **Failure trigger → mode:** control mới cùng package cũ, cập nhật upload một phần, hoặc dùng local-only làm published canon → đọc hỗn hợp revision/authority.
- **Impact:** đúng từng file vẫn sai tập nguồn. Canon10–80 hiện giống remote; khác biệt history/control là thật, không suy toàn bộ canon lệch.
- **Guardrail:** README/workflow đã cảnh báo, nhưng numeric activation và filename pins chưa có compatibility check thống nhất.
- **Global solution hook:** release descriptor pin control IDs/hashes, schema, source snapshot, builder/metadata revisions và publication target.
- **Local remediation:** mỗi audit/handoff ghi tuple local/remote/installed riêng; activation drift phải block nhánh phụ thuộc.
- **Migration risk:** không lấy local proposal làm baseline published; rollback controls phải đi cùng registry/schema/source snapshot tương thích.

## AR-07 — Đơn vị nạp file lớn, chưa có chứng cứ cho phép cắt node

- **Severity / trạng thái:** `SCALING_RISK / OBSERVED cơ chế; INFERENCE tác động`.
- **Evidence:** Router:81 bắt đọc đầy đủ routed file; `30`4,163 dòng, `90`4,060 dòng; mỗi lượt còn `00/92`. `static_audit.json` ghi bytes/dòng.
- **Current mechanism:** yêu cầu đọc đủ dựa trên physical file, không dựa trên node và dependency đã review.
- **Failure trigger → mode:** câu hỏi nhỏ chạm nhiều file lớn → lượng nạp tăng; giảm tùy tiện còn nguy hiểm hơn vì mất exception/unknown.
- **Impact:** amplification đo được ở kích thước văn bản, chưa đo latency/token/correctness của model; không dùng số dòng làm benchmark LLM.
- **Guardrail:** full-read bảo vệ ngữ cảnh; vẫn cần giữ cho audit toàn miền, authority conflict, node map stale hoặc closure chưa review.
- **Global solution hook:** node có mandatory context, source selector, dependency review và revision witness; bật theo module/task đã kiểm.
- **Local remediation:** shadow map trước, so decisive evidence với full-file route; không thay policy hiện hành trong pass này.
- **Migration risk:** node ngắn nhưng bỏ qualifier đầu file tạo sai nghĩa mà hash node vẫn khớp.

## AR-08 — Inventory lặp và route MC4 thiếu hàng trực tiếp

- **Severity / trạng thái:** `MAINTENANCE_DEBT / OBSERVED`.
- **Evidence:** `00`:8–18 liệt kê8 domain; Router:142–152 không có hàng60/MC4; `92` AF-OPEN-025/026/028 vẫn route60. Builder có list output:1579–1592; tests có list bắt buộc:119–126 chỉ kiểm một số file.
- **Current mechanism:** index, bảng Router, issue prose và builder mỗi nơi chứa một phần inventory.
- **Failure trigger → mode:** thêm module nhưng quên một bảng → route theo bảng có thể thiếu, verifier byte vẫn pass nếu không kiểm inventory semantics.
- **Impact:** **không phải MC4 unreachable hiện tại**, vì Router yêu cầu dùng index và92; là bất nhất bảng và nguy cơ mở rộng.
- **Guardrail:** read index + cross-domain rule giảm lỗi; chưa có bijection check current registration/output inventory.
- **Global solution hook:** một catalog module pointers; domain table/view được sinh; chỉ bootstrap hardcode ở kernel.
- **Local remediation:** test reachability theo mọi điểm vào hiện có; bổ sung/retire bảng thủ công trong nhiệm vụ được duyệt.
- **Migration risk:** scan `*_CURRENT.md` không đủ xác định authority; proposal/example cũng có thể mang tên này.

## AR-09 — Dependency và reverse impact chưa kiểm được đầy đủ

- **Severity / trạng thái:** `SCALING_RISK / OBSERVED`.
- **Evidence:** headers60→10,70→30/40/10,50→40/30;92 AF-AV-002→AF-OPEN-016; Router:199 yêu cầu propagate. Không có manifest node/typed-edge trong inventory.
- **Current mechanism:** đường dẫn, số file, heading và prose mang nhiều nghĩa: nạp, kiểm soát scope, provenance, quan hệ trong lore.
- **Failure trigger → mode:** retcon một premise → search tìm một số consumer nhưng không chứng minh đã đủ; một backlink không cho biết có cần nạp hay không.
- **Impact:** downstream summary, issue, control hook, recipe và test có thể stale. Tập ảnh hưởng mẫu ở01§5 chỉ là lower bound.
- **Guardrail:** yêu cầu propagate đúng về nguyên tắc; thiếu evidence map để kiểm sự hoàn chỉnh. Full-read không tự tìm các module bị bỏ ngoài candidate set.
- **Global solution hook:** forward typed edges do owner khai báo và review; reverse index chỉ là derived projection; trạng thái dependency review riêng khỏi truth/coverage.
- **Local remediation:** lập map các interface đã biết với chứng cứ và nhiệm vụ; unknown edge không biến thành empty list được chứng nhận.
- **Migration risk:** đảo chiều hoặc gán mọi mention thành REQUIRES tạo graph quá dày; phân loại edge trước khi tối ưu closure.

## AR-10 — Hash/rebuild không ghi đủ phạm vi approval và freshness

- **Severity / trạng thái:** `MAINTENANCE_DEBT / OBSERVED`.
- **Evidence:** manifest có source/output hashes, không hash builder/control tuple; `91` có decision addenda bằng prose; builder tự tạo cả output lẫn hash. Verifier so cùng builder tái tạo output.
- **Current mechanism:** reproducibility và byte integrity có thật; acceptance provenance và metadata dependency freshness không được biểu diễn đầy đủ.
- **Failure trigger → mode:** sửa generator và regenerate, hoặc stale summary/registry không đổi source hash → byte check pass nhưng quyết định đã duyệt chưa chắc được bảo toàn.
- **Impact:** không được dùng `PASS` để gọi canon đúng hoặc architecture được phê duyệt; generated canon không mất authority chỉ vì được sinh.
- **Guardrail:** workflow yêu cầu semantic comparison với decision; thiếu artifact liên kết đủ scope/revision nên thao tác này còn thủ công.
- **Global solution hook:** decision reference có phạm vi, hash toàn bộ input closure gồm recipe/schema/controls; giữ role và materialization độc lập.
- **Local remediation:** thêm evidence receipt cho migration; decision không truy nguyên được phải ghi `UNVERIFIED`, không fabricate chat ID.
- **Migration risk:** blanket rule “derived view != authority” có thể vô hiệu hóa toàn bộ current canon10–80; xemR-04.

## AR-11 — Issue view có hai tuyến tác giả, không phải phép dẫn xuất từ91

- **Severity / trạng thái:** `MAINTENANCE_DEBT / OBSERVED`.
- **Evidence:**92:3 nói derived từ reconciliation; builder:208 đọc seed92,1512–1567 giữ các hàng mới bằng here-string,1568–1570 ghép rồi ghi. `91` được sinh độc lập tại1428–1510.
- **Current mechanism:** ý nghĩa được curator đồng bộ, không có extraction hoặc foreign-key check91→92. Một số issue trỏ tên addendum, một số chỉ trỏ domain, không có evidence record ID chung.
- **Failure trigger → mode:** cập nhật reconciliation mà quên literal issue/seed → issue vẫn cũ hoặc mất hook; closed/removal cùng bảng cần scope rõ.
- **Impact:** read gate có thể bỏ sót premise chưa ổn định. Không phát hiện sự đóng issue trái phép cụ thể trong baseline này.
- **Guardrail:**92:105 nói không đầy đủ; full domain unknown vẫn có hiệu lực. Rebuild xác nhận bản literal lặp lại, không kiểm khớp ý nghĩa91.
- **Global solution hook:** issue records owner theo scope, retain ID và resolution evidence;92 chỉ projection; không sửa tay generated92 làm authority tạm.
- **Local remediation:** map seed/literal/evidence trước; kiểm mọi AF-ID và không cưỡng ép mọi local unknown phải có global issue.
- **Migration risk:** nhập enum mới có thể biến DEFERRED thành UNKNOWN hoặc gộp hai ID removal; bảo toàn nhãn gốc và alias rõ.

## AR-12 — Controls cũng có kích thước và consumer canon riêng

- **Severity / trạng thái:** `SCALING_RISK / OBSERVED`.
- **Evidence:** 5 overlays:522/513/493/1085/617 dòng; Mortality:6–7 require Modular và conditionally TotalWar; Worldbuilding:58–88 route Economy; TotalWar:414–418 nhắc cụ thể canon aviation.
- **Current mechanism:** dependency và specificity bằng prose; active family table Router/runner hardcode. Invariants lặp có chủ đích; không có bằng chứng cycle lỗi đang active.
- **Failure trigger → mode:** overlay mới hoặc retcon premise hook → nhiều bảng sửa tay; node routing canon giảm tải nhưng full overlay load vẫn lớn.
- **Impact:** control hook stale hoặc ưu tiên không rõ khi nhiều overlay cùng scope. Chưa kiểm runtime nên không khẳng định model đang vi phạm.
- **Guardrail:** Router yêu cầu closure bắc cầu, specific-inside-scope, surfacing conflict; Worldbuilding giữ economy clamp rõ.
- **Global solution hook:** cùng identity/dependency substrate, payload control khác canon; overlay precedence có scope và không tạo hierarchy toàn cục.
- **Local remediation:** pin toàn overlay trước; chỉ cắt node controls sau regression riêng; đưa source hooks thành consumer refs.
- **Migration risk:** deduplicate invariant có thể xóa stop condition quan trọng; không ép mọi overlay đồng hình hoặc đọc toàn bộ graph.

## AR-13 — Cổng kiểm thử có phạm vi hẹp và dependency ngoài package

- **Severity / trạng thái:** `SCALING_RISK / OBSERVED`.
- **Evidence:** runner output `LIMITED_CHECK`, schema9/9, selected0, model_executed=false;9 case DRAFT. Runner:31,179–185 cần parent `ChatGPT Plus+ Era/chatgpt v8.5.txt`; verifier là file skill ngoài repo. Required list không bao trùm mọi current path.
- **Current mechanism:** kiểm name/version/schema/hash anchors; không structural module graph, không model execution. Verifier separate không được runner gọi.
- **Failure trigger → mode:** copy riêng package sang môi trường khác hoặc dựa vào exit0 để bật Router mới → công cụ có thể block/missing hoặc tạo cảm giác đã thử ngữ nghĩa.
- **Impact:** migration chưa có regression oracle đủ; package build tự chứa không có nghĩa mọi dev tool tự chứa.
- **Guardrail:** README và output báo giới hạn rất rõ; đây là giới hạn đã công bố, không phải tool tuyên bố sai.
- **Global solution hook:** đóng gói verifier/versioned test tooling với repo khi được duyệt, tách structural, reviewed-evidence, semantic và live-runtime gates.
- **Local remediation:** giữ DRAFT; chạy structural shadow theo phạm vi task; chỉ bật semantic suite theo phê duyệt riêng như README.
- **Migration risk:** tự ACTIVE hóa cases hoặc đổi neo để xanh sẽ xóa căn cứ thử nghiệm; không làm trong migration cơ học.

## AR-14 — Một số tham chiếu provenance không resolve trong package

- **Severity / trạng thái:** `MAINTENANCE_DEBT / OBSERVED phạm vi package`.
- **Evidence:** `10`:284–288 liệt kê5 basename không tồn tại trong inventory98 file: world_bible_snapshot, ontology_genealogy, chat_synthesis, chot_canons_mc2, delta_since_last_export; tên chính xác ởstatic_audit.json.
- **Current mechanism:** danh sách nguồn tiền hợp nhất được giữ trong merged content; builder dùng `aetherfire_canon_hop_nhat_merged_v2.md`, không đọc trực tiếp5 file đó.
- **Failure trigger → mode:** người audit truy ngược tới original hoặc generic link checker coi mọi mention là runtime input → truy nguyên dừng hoặc false alarm.
- **Impact:** provenance transitive không đủ để khôi phục mọi source gốc từ package này; **không phải build input mất** và không chứng minh canon thiếu.
- **Guardrail:** package rebuild vẫn đủ input trực tiếp; quarantine ngăn tìm file legacy rồi dùng làm current.
- **Global solution hook:** reference type `PROVENANCE_ONLY`, source snapshot locator, `UNAVAILABLE_ORIGINAL` cho chuỗi không truy được; không tự tìm khắp máy.
- **Local remediation:** chú giải resolution class; xin nguồn chỉ khi tác vụ truy nguyên cần, không fabricate original.
- **Migration risk:** auto-remap cùng basename hoặc xóa refs để hết dangling sẽ phá provenance.

## AR-15 — Summary hợp lệ chưa có chứng cứ freshness theo owner

- **Severity / trạng thái:** `BREAKPOINT_SOON / OBSERVED cơ chế; INFERENCE failure`.
- **Evidence:** ML summary literal builder:638–673 và aviation summary:514–525; owner70/80 sinh từ source+reconcile; summary10 không có `reviewed_against` hash/selector. Đã đọc cặp10–70–80 và không xác nhận mirror block hoặc authority conflict hiện tại.
- **Current mechanism:** summary có authority boundary rõ, được curator bảo trì riêng với nội dung chi tiết.
- **Failure trigger → mode:** owner đổi một qualifier quyết định, summary gần như vẫn đúng → checker byte/rebuild không phát hiện lệch nghĩa.
- **Impact:** đọc summary đơn lẻ có thể cho câu trả lời sai; node routing làm rủi ro này rõ hơn nếu summary được coi đủ bằng chứng.
- **Guardrail:** Router hiện full-read các miền bị tác động; boundary header giúp chọn owner, nhưng không tự chứng minh summary đồng bộ.
- **Global solution hook:** summary không authoritative cho claim chi tiết; declared source refs + fingerprint chỉ phát hiện cần review; projection verbatim có thể kiểm máy, paraphrase cần review ngữ nghĩa.
- **Local remediation:** đánh dấu summary consumer và gate re-review khi owner đổi, không xóa summary hiện tại.
- **Migration risk:** regenerate paraphrase bằng model không phải phép biến đổi xác định và có thể sáng tác; giữ bản biên tập được review.
