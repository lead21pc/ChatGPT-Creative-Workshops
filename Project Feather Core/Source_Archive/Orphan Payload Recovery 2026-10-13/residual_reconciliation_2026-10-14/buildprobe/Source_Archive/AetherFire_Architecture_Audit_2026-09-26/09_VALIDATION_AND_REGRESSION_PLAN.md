# Kết quả xác minh và kế hoạch validation/regression

Trạng thái: **AUDIT / PROPOSAL**. Tách rõ phép đã chạy khỏi acceptance suite chưa triển khai.

## 1. Đã chạy trong pass này

| Phép kiểm | Kết quả | Ý nghĩa / giới hạn |
|---|---|---|
| Baseline inventory/hash |98 file ban đầu | Gồm untracked inputs; không phải98 file canon |
| Proposal manifest |8/8 byte lengths khớp | Không xác nhận nội dung proposal đúng |
| Current manifest hashes |12 generated +27 archive listed đều MATCH | Byte integrity của các mục đã liệt kê |
| Skill package verifier |FAIL,2 issue | Archive dư1 file chưa liệt kê; rebuilt manifest khác; không tự sửa |
| Isolated builder baseline |Exit0;12/12 output byte-identical | Manifest vẫn khác do archive unlisted |
| Control runner |READ_ONLY / LIMITED_CHECK; schema9/9; selected0; draft-anchor warnings0 | Không chạy model/build;9 case vẫn DRAFT |
| Fault: anchor thiếu sau write đầu |Exit1;5 file rewritten,7 file trước giữ lại | Tái hiện partial-update trong bản sao |
| Fault: unguarded replacement miss |Exit0; sentinel đi vào80 | Build success không bảo đảm reconciliation đã áp dụng |
| Fault: heading trong fence |Exit0; `# literal`→`## literal` | Regex helper sửa cả code literal; chưa chứng minh current file gặp đúng lỗi này |
| Fault: CI2.99 DRAFT |Runner chọn2.99, exit0/LIMITED_CHECK | Eligibility không đồng bộ Router; chỉ fixture temp |
| Graph800→8,000 node |Local closure10; reverse impact100 | Dữ liệu tổng hợp,8→80 module với100 node/module giả lập |
| Fanout / dense / cycle / missing |8,001 impacted; dense80/6,320 edges; cycle kết thúc; missing báo lỗi | Không cắt edge; không kiểm semantic completeness/LLM |

Evidence: `static_audit.json`, `package_verifier.txt`, `control_regressions.json`, `sandbox_probes.json`, `closure_probe.json`. Các file nằm dưới `evidence/`. Kết quả bảo toàn source cuối pass nằm trong `preservation_check.json`.

## 2. Cách tái chạy prototype

Từ `AetherFire Project/`:

```powershell
python -X utf8 './AetherFire_Architecture_Audit_2026-09-26/audit_readonly.py' .
python -X utf8 './AetherFire_Architecture_Audit_2026-09-26/probe_sandbox.py' .
python -X utf8 './AetherFire_Architecture_Audit_2026-09-26/closure_probe.py'
pwsh -NoProfile -File './tests/control-regressions/run.ps1'
```

`audit_readonly.py` đọc nguồn và Git, chỉ in JSON stdout. `probe_sandbox.py` đọc project thật, tạo bản sao dưới OS temp, sửa **bản sao** để tiêm lỗi, chạy builder/runner ở đó rồi xóa temp; không ghi source thật. `closure_probe.py` chỉ tạo graph trong bộ nhớ. Không có model call hoặc network trong3 prototype này.

Runner temp cần Python, PowerShell và Git có sẵn; script sao chép đúng nền `chatgpt v8.5.txt` từ parent để test resolver không bị chặn bởi thiếu base. Không dùng các prototype này làm validator production. Nếu base hoặc cấu trúc repo thay, cần review/rebase probe thay vì coi kết quả cũ vẫn hợp lệ.

Verifier hiện có:

```powershell
pwsh -NoProfile -File 'C:/Users/Sheeplark/.codex/skills/aetherfire-source-audit/scripts/verify_aetherfire_package.ps1' -ProjectRoot (Get-Location).Path
```

Verifier đọc package thật, rebuild dưới temp. Đường dẫn skill ngoài repository là dependency môi trường, phải ghi rõ khi người khác tái chạy. Không chạy builder trực tiếp ở project thật trong pass audit.

## 3. Bốn lớp validation cho vNext

| Lớp | Kiểm gì | Không chứng minh |
|---|---|---|
| S — Cấu trúc | Schema, refs, hashes, IDs, paths, graph types, snapshot, deterministic generation | Dependency ngữ nghĩa đầy đủ; canon đúng |
| E — Bằng chứng đọc | Node/context/qualifier/supersession/issue coverage được review đối với source | Model sẽ dùng đúng evidence |
| M — Hành vi model | Paired full-file versus node route trên prompt/controls/source cố định | Mọi prompt tương lai hoặc Project đã cài đúng |
| R — Runtime triển khai | Đúng bundle/controls trong môi trường thật, actual responses/receipt | Authority cho canon mới hoặc quyền publication ngoài scope |

Không cho structural PASS tự thay semantic gate; không dùng test để đóng UNKNOWN. Các case schema hợp lệ có thể expected BLOCKED.

## 4. Ma trận test cấu trúc cần triển khai

| ID | Fixture / thay đổi | Kết quả kỳ vọng |
|---|---|---|
| S01 | Registered path mất; current accepted source chưa đăng ký | FAIL binding/inventory, không auto-register |
| S02 | Duplicate Module/Node/Interface ID, kể cả merge hai branch | FAIL uniqueness, không rename tự động |
| S03 | Path `..`, absolute, casefold/reparse collision | FAIL portable/root binding |
| S04 | Node marker mất/lặp/nằm trong fence; span gap/overlap | FAIL selector/segmentation; full-source fallback khi authority còn đúng |
| S05 | Required edge target thiếu | Block affected closure |
| S06 | Read cycleA↔B; derivation/supersession cycle | Read mỗi node một lần; reject hai graph cycle sau |
| S07 | Condition TRUE/FALSE/UNKNOWN | TRUE load; FALSE có căn cứ bỏ; UNKNOWN conservative load/block, không silently skip |
| S08 | Metadata hash khác source; summary owner đổi một qualifier | Stale/index invalid; SUMMARY_REVIEW_REQUIRED |
| S09 | Hai exclusive owners cùng scope; facet partition có evidence | Reject overlap chưa giải; accept partition đã review |
| S10 | Issue trỏ node retired; RESOLVED thiếu decision; raw label bị mất | Reject active dangling/resolution/mapping |
| S11 | DRAFT version cao, numeric alias, malformed candidate, README/header conflict | Resolver parity với active contract; không active draft |
| S12 | CI/Router/schema/features không tương thích; mixed schema | Block, hoặc explicit approved adapter cho đúng version |
| S13 | Thay generator/schema/input/controls nhưng cache/view cũ | Invalidate dependency fingerprint |
| S14 | Crash tại mỗi write boundary; disk-full fixture; publisher thất bại | Active generation không đổi, staging không được đọc như active |
| S15 | Source thay giữa read/hash; stale base của writer; hai writer | Snapshot bytes consistent; reject stale publish |
| S16 | Node đổi owner/path; one-to-many split; retired alias | ID giữ khi meaning giữ; consumer review khi split; tombstone truy được |
| S17 | Interface3+ participants, mỗi facet owner khác nhau | Giữ semantics, không pairwise copy tạo nhiều controlling records |
| S18 | Registry/cache mất nhưng authority receipt có/mất | Bounded full-read nếu chứng minh source; nếu không block canon |
| S19 | Archive/proposal source được search ưu tiên cao | Candidate có nhãn, không trở thành current premise |
| S20 | Rebuild2 lần; clean checkout; merge generated artifacts | Output byte-identical hoặc khác biệt được khai báo; no nondeterministic timestamps |
| S21 | Thin module hỗ trợ lookup nhưng thiếu premise simulation | Lookup allowed nếu đủ; simulation BLOCK/conditional, không fill |
| S22 | Consumer trong overlay/test/recipe, ngoài current module | Reverse impact vẫn bao gồm và yêu cầu review phù hợp |

Đây là danh sách acceptance fixtures, **chưa có S01–S22 production suite**. Một vài failure mechanism đã được probe ở§1 không đồng nghĩa mọi case ở đây đạt.

## 5. Semantic differential tests cần phê duyệt

Giữ model/version, instructions/personality/memory, history, prompt, source snapshot và toàn control không thuộc biến thử cố định. Khác biệt có chủ đích duy nhất là tập source/full-file versus node closure; không dùng một control pair khác để kết luận chỉ routing tốt hơn.

| Nhóm | Prompt boundary / oracle |
|---|---|
| MC4 local | Identity liên tục không tự import legacy ability; Academy link khi task cần |
| ML interface | Creed quorum / relic loan / oath không tự nhập thủ tục; AF-ML-005/006 còn mở |
| Aviation | Sole-confirmed infrastructure≠monopoly/air supremacy; sovereignty≠ATC≠economy |
| White/status | Eligibility≠completion; preserved unknown criteria |
| Cross-domain timeline | Narrator split không tự là ability transfer/loss |
| Old canon | Missing current retrieval không phục hồi Quad Night/removed routes |
| Summary stale | Một câu qualifier ở owner thay → không dùng summary chưa review |
| False metadata confidence | Coverage rộng nhưng decisive source thiếu → đúng BLOCKED/partial boundary |
| Mutation scope | Một acceptance không resolve các issue lân cận; reverse consumers được báo |
| Stage/output | Route-only không kết luận; proposal vẫn proposal; prose tiếng Việt |

Oracle là **danh sách bằng chứng quyết định và điều cấm suy**, không exact output string. Đo missing decisive evidence, wrong-authority use, unresolved-state preservation, false block/false allow, đọc thực/bytes/context, thời gian theo môi trường và chi phí update metadata. Không tự đặt tỷ lệ “đủ tốt” để bỏ lỗi authority; sai authority, UNKNOWN promotion hoặc bỏ decisive evidence là chặn activation scope đó.

Giữ9 case DRAFT hiện tại. Chỉ user-approved bounded experiment được nhập/chạy theo README; không lén dùng `ApprovedDraftExperiment` như bằng chứng đã được duyệt. Suite mới có thể tái dùng boundary, nhưng readiness không được suy từ schema9/9.

## 6. Stress-test10 lần và tiêu chí thiết kế

Chạy thưa, dense, high fanout, multi-party interfaces, read cycles, long supersession chains, nhiều local issues và concurrent edits. Đo riêng metadata traversal, bytes đọc và semantic success. Graph80 module thưa local phải không kéo toàn bộ node của80 module; high-fanout thật phải báo đủ impact, không cắt để đẹp benchmark.

Module addition không sửa CI/Router algorithm khi primitive cũ đủ; chỉ metadata/source/release đổi. Thêm một locale, domain hoặc phép thuật không tự thêm global management registry. Tối ưu cache khi số đo chứng minh có ích; cache loss không làm mất authoritative inputs hoặc provenance.

## 7. Bao phủ yêu cầu C1–C12

| Mục | Kết quả / giới hạn |
|---|---|
| C1 inventory |98 file, vai trò/versions/Git ở01 vàJSON; không tự xóa dead-looking files |
| C2 authority |Đối chiếu10/70/80,20/30,40/50,local/published; không chứng nhận mọi claim lore |
| C3 duplication |Exact/near candidates + manual summary/control/history classification; không xóa |
| C4 routing |00/92/Router/path/build inventories; MC4 table omission,80 present |
| C5 coverage |Bytes/lines/headings/unknown ratio/refs/issueIDs/Git path counts; không quality score |
| C6 dependency |Headers,prose,build bindings,overlay conditions,unresolved provenance refs |
| C7 reverse impact |5 đại diện ở01; chưa chứng minh complete graph |
| C8 interfaces |ML/AF/TE,RF aviation,status,narrator facets; owner model ở04/05 |
| C9 generated |Builder/seed/literal/hash/rebuild, partial failure, source-map gaps |
| C10 history |90/91 layers vàprovenance; split deferred cho tới có nhu cầu đo được |
| C11 CI coupling |CI đã không inventory; pinned Router/base khác control runtime pairing |
| C12 overlays |Sizes,dependency/specifity/source hooks; không có runtime compliance claim |

## 8. Bao phủ yêu cầu D1–D20

| Mục | Finding / thiết kế / kiểm thử |
|---|---|
| D1 concurrency |AR-02,R-05; base revision+snapshot;S15 |
| D2 crash/partial |Sandbox partial failure; staging publish;S14 |
| D3 split/merge/rename |R-01; tombstones/scope successor;S16 |
| D4 schema evolution |R-08; explicit features/adapters;S12 |
| D5 multi-owner |R-02; facets và3+participants;S17 |
| D6 high fanout |R-06;8,001 impacted synthetic;no truncation |
| D7 cycles |Read SCC khác derivation/authority;S06 |
| D8 partial coverage |R-03; task-scoped sufficiency;S21 |
| D9 stale summaries |AR-15; hash invalidation+semantic review;S08 |
| D10 false confidence |R-03/R-07; E/M gates, không metadata-only proof |
| D11 registry SPOF |R-09; recoverability khác authorization;S18 |
| D12 archive leakage |Router quarantine hiện có;source role filters;S19 |
| D13 ID collision |R-01/R-10;merge uniqueness;S02 |
| D14 Git rollback |Whole compatible release revert;08§5/6 |
| D15 generated merge |Giữ tracked outputs ban đầu,regenerate khi merge;S20 |
| D16 performance |Prototype O(V+E) traversal vàlimits;04§9 |
| D17 human usability |Markdown editable,whole-file node,derived local table;04§10 |
| D18 over-modeling |Bỏ global lore-payload interface registry,orphan registry;03 kết luận |
| D19 abstraction |Opaque identity,role/materialization/status,facet contracts;05 |
| D20 canon transactions |8 tình huống trong08§5;chưa migration/resolve canon |

## 9. Điều còn chưa xác minh

Chưa chạy live ChatGPT, chưa đo model token/latency/evidence-selection accuracy; chưa thử publisher atomicity đa môi trường, JSON Schema production validator hoặc8,000 node nguồn thật. Không kiểm toàn bộ lore ngữ nghĩa hoặc originals ngoài package. Package baseline chưa PASS do2 lỗi đã nêu. Những giới hạn này là cổng cần xử lý trước activation, không được xóa khỏi handoff chỉ vì báo cáo đã hoàn tất.
