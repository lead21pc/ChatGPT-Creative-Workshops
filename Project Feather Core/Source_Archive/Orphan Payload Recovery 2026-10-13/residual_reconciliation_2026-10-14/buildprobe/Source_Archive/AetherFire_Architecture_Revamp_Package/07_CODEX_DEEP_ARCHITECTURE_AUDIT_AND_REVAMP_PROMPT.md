# Prompt cho Codex — Deep Architecture Audit & Modular Revamp

Hãy thực hiện một **audit kiến trúc toàn repository AetherFire** với mục tiêu chuẩn bị một major revamp của source-management, CI, Router, module architecture và validation.

Đây không phải nhiệm vụ sửa lore.

Đây không phải nhiệm vụ canonize proposal.

Đây không phải nhiệm vụ “chỉ thêm mục lục”.

Mục tiêu là tìm và xử lý tận gốc các giới hạn sẽ xuất hiện khi:

```text
độ rộng lore
+
số module
+
số cross-domain interface
+
số open issue
+
số vòng reconciliation

tăng nhanh hơn độ sâu cập nhật của từng miền.
```

---

# A. Quy tắc an toàn đầu tiên

1. Resolve active AetherFire CI theo runtime rules hiện hành.
2. Đọc Source Router hiện hành trước.
3. Phân loại task này là:
   - architecture audit;
   - control/source-management design;
   - **không được phép thay đổi canon**.
4. Không dùng design history hoặc superseded source làm baseline.
5. Không resolve `UNKNOWN`, `OPEN`, `DEFERRED`, `CONFLICTED`.
6. Không rewrite lore để làm kiến trúc “đẹp”.
7. Không coi filename, recency hoặc độ dài là authority.
8. Mọi kết luận về repository phải dựa vào file thật trong repo, Git state hoặc kiểm tra tĩnh; không dựa vào danh sách trong prompt nếu repo cho bằng chứng khác.

---

# B. Đọc bộ proposal trước

Đọc toàn bộ:

```text
00_AetherFire_Architecture_Revamp_Package_INDEX.md
01_ARCHITECTURE_PAIN_AND_BREAKPOINT_AUDIT.md
02_GLOBAL_INTEGRATED_SOLUTION_ARCHITECTURE.md
03_MODULAR_EXPANSION_FRAMEWORK.md
04_ARCHITECTURE_GLOSSARY.md
05_CI_REVAMP_PROPOSAL.md
06_MANAGEMENT_FILE_SUITE_PROPOSAL.md
```

Các file này là `PROPOSAL`.

Không coi chúng là kiến trúc đã được chấp nhận.

---

# C. Audit repository thật

Hãy kiểm tra toàn repository, không chỉ các file được nêu.

## C1. Inventory

Liệt kê:

```text
active CI versions
Router versions
current canon modules
anti-drift overlays
derived/generated views
open-issue files
reconciliation files
history files
source archive
scripts
schema/config files
README/control docs
```

Phát hiện:

```text
unregistered current sources
registered-but-missing paths
duplicate version numbers
draft/superseded ambiguity
orphan files
dead files
```

---

## C2. Authority audit

Tìm mọi trường hợp:

```text
two current-looking files claim same controlling scope
authority split but content still duplicated
summary source accidentally becomes controlling
old source still referenced as current
cross-domain relation has no clear owner
```

Đặc biệt kiểm tra những trường hợp tương tự:

```text
10 vs 70
```

nhưng không giả định đây là trường hợp duy nhất.

---

## C3. Duplication audit

Dùng static analysis để tìm:

```text
exact duplicated blocks
near-duplicated blocks
same heading/content copied across current files
same rule repeated in control files
```

Phân loại:

```text
intentional summary
dangerous mirror
authority duplication
historical preservation
```

Không tự xóa.

---

## C4. Routing audit

Kiểm tra:

```text
Router domain table
00 inventory
92 dependencies
module headers
overlay routing
physical paths
```

Tìm bất一致:

```text
Router knows file that package lacks
file exists but Router cannot reach
00 lacks current module
92 points to module not in 00
overlay dependency not declared centrally
```

---

## C5. Coverage audit

Đo:

```text
file size
heading count
UNKNOWN density
open-issue count
cross-reference count
change frequency if Git available
```

Không dùng các số này làm quality score.

Mục tiêu là phát hiện:

```text
very thin current modules
very deep current modules
domains whose boundary is known but internals are not
domains with disproportionate reconciliation load
```

Đề xuất coverage classification nhưng không canonize.

---

## C6. Dependency audit

Tìm:

```text
explicit dependency
implicit dependency in headers
cross-file references
required sibling sources
interface references
overlay dependencies
```

Phát hiện:

```text
cycles
dangling refs
hidden dependency
dependency encoded only by prose
dependency that points to path instead of stable identity
```

---

## C7. Reverse-impact audit

Với một số canon node đại diện, thử trả lời:

```text
nếu node này đổi
ai phụ thuộc vào nó?
```

Nếu không thể chứng minh đầy đủ từ cấu trúc hiện tại, ghi đó là finding.

Không mutate canon.

---

## C8. Interface audit

Tìm các cross-domain interface quan trọng.

Kiểm tra xem relation đang được lưu:

```text
in one side
in both sides
in reconciliation only
in global file
in duplicated copies
```

Đề xuất một owner/contract model ở cấp kiến trúc, không đổi lore.

---

## C9. Generated-view audit

Với các file tự nhận là generated/control view:

```text
00
92
và các file khác nếu có
```

xác minh:

```text
generator có tồn tại không?
source-of-generation là gì?
có hash/revision/schema không?
file có bị sửa tay không?
có thể phát hiện stale không?
```

Nếu không chứng minh được, ghi rõ.

---

## C10. Reconciliation/history scaling audit

Kiểm tra `90`, `91` và các provenance source khác:

```text
có phải monolith đang tăng?
route-by-ID có đủ không?
khi nào split là đáng?
split có tạo fragmentation không?
```

Không split chỉ vì file dài.

---

## C11. CI coupling audit

Kiểm tra active CI:

```text
bao nhiêu rule phụ thuộc inventory hiện tại?
bao nhiêu domain/file name hard-coded?
bao nhiêu rule nên thuộc glossary/schema/router/overlay?
```

Mục tiêu:

```text
CI change frequency
<<
module change frequency
```

---

## C12. Overlay scaling audit

Kiểm tra:

```text
overlay size
activation overlap
dependency cycles
duplicated invariants
scope conflicts
full-read cost
```

Đề xuất dùng cùng module/node framework nếu phù hợp.

---

# D. Mở rộng audit ngoài danh sách proposal

Không dừng ở các vấn đề đã nêu.

Chủ động tìm thêm failure mode, đặc biệt:

## D1. Concurrency

Nếu ChatGPT/Codex/human sửa nhiều file song song:

```text
merge conflict
stale generated view
partial migration
half-applied authority transfer
```

xử lý thế nào?

## D2. Crash/partial commit

Nếu structural migration dừng giữa chừng:

```text
registry updated
but source not moved
```

hoặc ngược lại, có rollback path không?

## D3. Module split/merge/rename

Kiểm tra alias, redirects, stable identity, old references.

## D4. Schema evolution

Nếu `Architecture Schema v2` xuất hiện:

```text
Router v4 đọc được không?
mixed-schema package có được phép không?
```

## D5. Multi-owner interface

Nếu một interface thực sự có ba hoặc nhiều module tham gia, contract model có chịu được không?

## D6. High-fanout node

Nếu một node có hàng chục consumer:

```text
reverse-impact closure
```

có làm runtime nổ không?

## D7. Circular module dependencies

Phân biệt:

```text
valid mutual interface
vs
invalid dependency cycle
```

## D8. Partial coverage

Nếu một module chỉ `BOUNDARY_ONLY`, Router phải ngăn loại task nào?

## D9. Stale summaries

Nếu summary đúng phần lớn nhưng sai một claim quyết định, validator có bắt được không?

## D10. False confidence from metadata

Coverage/index/registry có thể làm model quá tin metadata.

Thiết kế guardrail.

## D11. Registry single point of failure

Nếu registry lỗi/mất/stale, canon phải vẫn recoverable.

## D12. Archive leakage

Kiểm tra cách search/retrieval có thể đưa archived/superseded source vào candidate set và cách Router chặn.

## D13. ID collision

Nếu hai branch tạo cùng Node ID/Interface ID.

## D14. Git history and rollback

Kiến trúc mới có làm rollback source khó hơn không?

## D15. Derived-view merge conflicts

Generated files có nên commit vào Git hay generate runtime?

Phân tích trade-off.

## D16. Performance

Đánh giá:

```text
node count
dependency fanout
closure size
validator cost
regeneration cost
```

Không tối ưu vi mô nếu chưa cần.

## D17. Human usability

Kiến trúc tốt cho machine nhưng có làm user khó edit Markdown thủ công không?

Phải giữ human-editable.

## D18. Over-modeling

Tìm dấu hiệu framework proposal đang phức tạp quá nhu cầu thật.

Đề xuất cắt bỏ nếu cần.

## D19. Wrong abstraction boundary

Kiểm tra liệu `module`, `domain`, `interface`, `node` có đủ hay cần primitive khác.

Chỉ đề xuất primitive mới nếu có failure không biểu diễn được.

## D20. Canon-change transaction

Stress-test với:
- local retcon;
- cross-domain retcon;
- authority transfer;
- module retirement;
- newly canonized proposal.

---

# E. Kiến trúc đích bắt buộc phải đạt

Không nhất thiết dùng đúng implementation trong proposal.

Nhưng thiết kế cuối phải đạt các property:

```text
1. source authority không yếu đi;
2. UNKNOWN không bị fill;
3. old canon quarantine còn nguyên;
4. module mới không bắt sửa CI;
5. module có identity ổn định độc lập path;
6. local task không bắt full-read vô lý;
7. full-read fallback vẫn tồn tại;
8. cross-domain interface có owner/contract rõ;
9. coverage được biểu diễn riêng truth;
10. canon mutation có reverse-impact analysis;
11. generated views có stale detection;
12. structure có validator;
13. registry không trở thành canon;
14. registry failure không làm canon unrecoverable;
15. framework không tạo hàng chục management source-of-truth.
```

---

# F. Đầu ra yêu cầu

Tạo một thư mục proposal mới, không sửa current canon trong pass này.

Tối thiểu tạo:

```text
01_REPO_ARCHITECTURE_AUDIT.md
02_CONFIRMED_BREAKPOINTS.md
03_ADDITIONAL_RISKS_FOUND.md
04_TARGET_ARCHITECTURE.md
05_MODULE_AND_INTERFACE_SCHEMA.md
06_CI_VNEXT_PROPOSAL.md
07_ROUTER_VNEXT_PROPOSAL.md
08_MIGRATION_PLAN.md
09_VALIDATION_AND_REGRESSION_PLAN.md
10_OPEN_DESIGN_DECISIONS.md
```

Nếu thấy cấu trúc khác tốt hơn, có thể thay đổi số file nhưng phải tránh fragmentation.

---

# G. Mỗi finding phải có cấu trúc

```text
ID
Severity
Evidence
Current mechanism
Failure trigger
Failure mode
Impact
Why existing guardrail does/does not catch it
Global solution hook
Local remediation
Migration risk
```

Severity đề xuất:

```text
BREAKPOINT_NOW
BREAKPOINT_SOON
SCALING_RISK
MAINTENANCE_DEBT
OPTIONAL_IMPROVEMENT
```

Không dùng severity để dramatize.

---

# H. Phân biệt bằng chứng và proposal

Trong mọi output:

```text
OBSERVED
INFERENCE
PROPOSAL
UNKNOWN
```

phải tách khi material.

Không biến static-analysis result thành canon claim.

---

# I. Không triển khai ngay những thay đổi sau

Trong pass audit/design này, không:

```text
- xóa duplicate canon;
- move current files;
- split 90/91;
- rewrite 00/92;
- bump active CI;
- activate new Router;
- change canon wording;
- resolve open issue.
```

Chỉ tạo proposal + migration plan + validation prototype nếu cần.

Có thể tạo script audit/validator thử nghiệm nếu:
- không sửa source;
- output rõ là prototype;
- có thể chạy read-only.

---

# J. Yêu cầu chất lượng

Không đưa danh sách ý tưởng chung chung.

Mỗi đề xuất phải trả lời:

```text
pain point nào?
owner nào?
source of truth nào?
failure behavior nào?
fallback nào?
migration thế nào?
validation thế nào?
scale thế nào?
```

Không tạo framework chỉ đẹp trên sơ đồ.

Stress-test nó với repository thật.

---

# K. Câu hỏi cuối cùng Codex phải tự trả lời

Sau audit, kết luận riêng:

```text
Nếu AetherFire tăng gấp 10 lần số module hiện tại,
kiến trúc đề xuất có cần major rewrite nữa không?

Nếu có:
→ chỉ ra abstraction nào vẫn sai.

Nếu không:
→ chỉ ra vì sao module addition không làm control layer phình tương ứng.
```

Đây là tiêu chí chính của đợt revamp.
