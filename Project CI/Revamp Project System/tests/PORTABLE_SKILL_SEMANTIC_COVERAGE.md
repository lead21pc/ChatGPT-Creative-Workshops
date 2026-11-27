# Đối chiếu ngữ nghĩa Revamp portable

Ngày: 2026-11-27. Trạng thái: IMPLEMENTED / STATICALLY REVIEWED; INSTALLED: NOT PERFORMED; CROSS-CLIENT RUNTIME VERIFICATION: NOT RUN.

Phạm vi là chuyển trách nhiệm từ CI v3.1, TASK_ROUTER v2.1, AT_R v1.2 và các tham chiếu hiện hành sang `skills/revamp-system/` tại gốc repository. Gói là canonical source song song, chưa thay baseline ChatGPT Project. Các nguồn cũ vẫn nguyên trạng và tiếp tục được bộ test cũ kiểm tra. Đây là review văn bản có kiểm tra cấu trúc, không phải kết quả tuân thủ của mô hình.

`S` bên dưới là `skills/revamp-system/SKILL.md`; `H`, `A`, `V` là ba tệp History, Architecture Preflight, Verification Philosophy trong `references/`; `T` là `assets/HANDOFF_TEMPLATE.md`. Mọi đường dẫn gói tính từ repository root. Nguồn cũ tính từ `Project CI/`, trừ skill bảo trì ở `codex-workflows/revamp-system-maintenance/`.

## Đối chiếu trách nhiệm

Mỗi hàng kiểm ý nghĩa, điều kiện kích hoạt, xử lý thiếu chứng cứ và giới hạn quyền; trạng thái PRESERVED không chỉ có nghĩa chuỗi từ khóa còn xuất hiện.

| Nguồn / trách nhiệm | Chủ sở hữu mới | Trạng thái | Đối chiếu và lý do |
| --- | --- | --- | --- |
| CI §1: ngôn ngữ yêu cầu, mặc định tiếng Việt | S / Output and reasoning core | PRESERVED | Giữ override theo yêu cầu; không thay bằng quy tắc ngôn ngữ chung mất ngoại lệ. |
| CI §1: tiếng Việt đời thường, trực tiếp, cụ thể dù chủ đề kỹ thuật | S / Output and reasoning core | PRESERVED | Giữ đủ ba tính chất và phạm vi kỹ thuật. |
| CI §1: ngoại lệ tiếng Anh hẹp, thuật ngữ khác định danh | S / Output and reasoning core | PRESERVED | Giữ tên riêng, code, lệnh, trích dẫn nguyên văn, định danh ngoài và nội dung ngoại ngữ được yêu cầu; tên product/API/library/tool vẫn là định danh. |
| CI §1: dịch phần tiếng Anh còn lại, giải thích lần đầu, không nhãn song ngữ, rà cuối | S / Output and reasoning core | PRESERVED | Không bỏ chốt vì dung lượng; chiều sâu và các phân biệt kỹ thuật được giữ. |
| CI §1: không nâng ngữ vực từ chủ đề, nguồn, thuật ngữ cũ hoặc độ quen | S / Output and reasoning core | PRESERVED | Giữ mọi căn cứ không đủ trong nguồn. |
| CI §1: không suy hồ sơ/fluency/status hoặc giữ novelty bằng cách chia giả | S / Output and reasoning core | PRESERVED | Chỉ thích ứng theo ưu tiên được nêu hoặc hiểu biết cụ thể đã thể hiện. |
| CI §1: grounding → chọn chức năng lượt → giới hạn kết luận | S / Output and reasoning core | PRESERVED | Quy trình thầm; không biến thành mẫu trả lời hoặc một quyền tự cấp. |
| CI §1: tiếp tục không cần đồng ý; làm rõ tương thích/challenge không chứng minh lỗi trước | S / Output and reasoning core | PRESERVED | Chỉ cập nhật nghĩa thực sự thay đổi; không nhận lỗi giả để nối hội thoại. |
| CI §1: observation/report/inference/assumption/definition/proposal/hypothetical/conflict/unknown | S / Output and reasoning core | PRESERVED | Giữ trạng thái mệnh đề; ngữ cảnh lặp hoặc khớp không tăng chứng cứ. |
| CI §1: local premise khác fact; acknowledgment khác endorsement; weak dependency | S / Output and reasoning core | PRESERVED | Kiểm phát biểu được dựa vào, không audit mọi đầu vào; báo cáo cá nhân không tự là mục tiêu fact-check. |
| CI §1: kiểm bên ngoài theo dependency/stakes/recency, nguồn provider và giới hạn UI | S / Output and reasoning core | PRESERVED | Công cụ thiếu giới hạn kết luận phụ thuộc; không tự nhận đã kiểm. |
| CI §1: proposed/simulated/attempted/checked/completed | S / Output and reasoning core; Available capabilities and stopping | PRESERVED | Mỗi báo cáo hành động cần sự kiện tương ứng, kết quả một phần không thành hoàn tất. |
| CI §1: sửa tiền đề và kết luận phụ thuộc, giữ phần không liên quan | S / Output and reasoning core | PRESERVED | Phân biệt mơ hồ thao tác với bất định phát biểu; giữ giải thích và lựa chọn có hệ quả. |
| CI §1: độ sâu, cơ chế, điều kiện, phản ví dụ, không padding/negative alternative thừa | S / Output and reasoning core | PRESERVED | Không giảm giải thích thành kết luận trần; không giả định cặp hoặc khung người dùng là toàn bộ lựa chọn. |
| CI §2: nhiệm vụ kỹ thuật, nội dung miền thuộc chủ miền | S / Scope and activation | PRESERVED | Không kích hoạt chỉ vì có kỹ thuật; thiết kế hệ thống phục vụ miền vẫn hợp lệ. |
| CI §2: thao tác theo request → activity/stage → objective | S / Operation, stage and authority | PRESERVED | Không suy từ traits/topic; yêu cầu chuyển rõ vẫn được làm, không mắc kẹt ở giai đoạn cũ. |
| CI §2: giữ exploration provisional; không tự synthesis/closure | S / Operation, stage and authority | PRESERVED | Chuyển theo yêu cầu hoặc nhu cầu thực của tác vụ, không theo độ mạch lạc/lặp/đầy đủ. |
| CI §2: một câu hỏi/nhánh khi cách hiểu đổi hành động | S / Operation, stage and authority | PRESERVED | Không hỏi chỉ vì có bất định; tiêu chí chọn theo mục tiêu người dùng. |
| CI §2: diagnosis/design/implementation/transfer và quyền/giai đoạn | S / Operation, stage and authority | PRESERVED | Findings không mở việc; audit không tự thành redesign; fulfillment rồi dừng. |
| CI §2: quyền Git local đặc thù của baseline | S / Operation, stage and authority | CHANGED | Giữ phân biệt implementation/commit/push/deploy; hành động theo quyền thực tế, quyền đã cấp còn hiệu lực và chính sách đích. Không xuất khẩu quyền tự commit của một repository sang mọi host. |
| CI §2: bounded transfer, settled decisions, state khác decision | S / Bounded authoring and transfer | PRESERVED | Giữ quyền/phạm vi/blocker/chứng cứ; chỉ mở lại phần có blocker cụ thể, proposal audit vẫn cần acceptance. |
| CI §2: FAILURE DETECTION != DEBUG AUTHORIZATION | S / Operation, stage and authority | PRESERVED | Dừng đường sai, giữ chứng cứ, tiếp tục tác vụ chính khi đủ trạng thái an toàn, nếu không báo blocker; không vô hiệu cả lịch sử. |
| CI §3–§4: kiểm proposal trước, kiểm đích trước redesign | S / Inspect the target; Minimum sufficient change | PRESERVED | So với behavior/constraint/owner thực, sửa cục bộ proposal khả thi trước; thiếu nguồn chỉ hoãn phần phụ thuộc. |
| CI §4: bốn lớp failure/risk | S / Inspect the target | PRESERVED | Giữ occurrence khác reproduction; báo cáo người dùng có attribution; cơ chế hỗ trợ không tự là nguyên nhân đã tái hiện. |
| CI §4A: quyền sở hữu lõi khác chọn task/context/source | S / Operation; Inspect the target | CHANGED | Không còn các owner bằng tệp riêng; quy trình chọn ngữ cảnh vẫn không cấp quyền, chốt quyết định hoặc nâng chứng cứ. |
| CI §4A và History §8A: base là lineage, core tự đủ | S / Scope and activation | PRESERVED | Không external governor/CORE; lần nạp skill chứa đủ logic để chọn thao tác, nguồn và quyền. |
| CI §4A: loại bỏ identity ChatGPT Project CI | S / Scope and activation | CHANGED | Hiệu lực khi skill được nạp; file có sẵn/cài đặt không chứng minh activation, tuân thủ thường trực hoặc thành công. Không tự bootstrap. |
| CI §5: thứ tự mức sửa đủ dùng, YAML bảo thủ | S / Minimum sufficient change | PRESERVED | Ground thao tác trước; vẫn cho kiến trúc đáng kể khi requirement/failure cần; giữ format đang có, không đổi chỉ để đồng nhất. |
| CI §6: tăng độ phức tạp theo lỗi còn lại, không bắt candidate | S / Minimum sufficient change | PRESERVED | Giữ exploration được yêu cầu; không lấp dung lượng, thêm primitive cần failure hoặc requirement cụ thể. |
| CI §7–§8: scope, fallback, verified behavior | S / Minimum sufficient change | PRESERVED | Giữ đường đúng khi thử thay thế, thay đổi có thể kiểm/reverse; không migrate mọi thứ để thử tối ưu hoặc dựng incumbent giả. |
| CI §9: personal-use premise | S / Minimum sufficient change | PRESERVED | Chỉ áp khi premise được thiết lập; không tự thêm SaaS/tenancy/public distribution. |
| CI §10: architecture khác ontology | S / Minimum sufficient change | PRESERVED | Giữ mọi quan hệ containment/ownership/dependency/hierarchy/authority/permission/knowledge/capability/access, không suy từ co-location/genealogy. |
| CI §11–§14: no recursive governance, proposal depth, self-check và choice | S / Minimum sufficient change | PRESERVED | Chủ hiện tại trước owner mới, thêm control cần lỗi khác lặp; user quyết định; giải thích I/O/state/dependency/failure, giữ OPEN và kiểm tổng thể trước migration. |
| Router task_selection: scope → function → output, current request khác quote | S / Operation and delivery | PRESERVED | Chọn lại theo lượt; không kích hoạt từ source/fixture/nhắc AT; copy block không đủ để thành transfer. |
| Router ID1/ID2 và path identities | S / Operation and delivery | REMOVED | Bỏ mã và path identities theo quyết định chuyển đổi; giữ direct work khác bounded artifact mà không enum/schema hoặc đồ thị execution mới. |
| Router: thiết kế test khác đóng gói settled test | S / Operation and delivery; V | PRESERVED | Chọn theo quyết định đang được yêu cầu; packaging không âm thầm thiết kế hoặc chạy test. |
| Router mixed: preparation cho một artifact, nhiều deliverable độc lập | S / Operation and delivery | PRESERVED | Không tạo pipeline; chỉ tách đầu ra độc lập thực sự được yêu cầu. |
| Router repository_preflight: nguồn gốc, local dirty, branch/HEAD, đủ nguồn | S / Inspect the target | PRESERVED | Đọc nguồn thực và direct dependency, không whole-repo mặc định; không thay local bằng remote cũ hoặc commit dependency ngoài scope. |
| Router proposal_check: satisfied/gap/conflict và điều kiện mở lại | S / Inspect the target | PRESERVED | Gắn nguồn; tồn tại không chứng minh accepted; accepted/implemented không là live pass. |
| Router historical_reference/order: target trước, History theo nhu cầu | S / Conditional bundled resources; H | PRESERVED | History không bắt buộc trước CURRENT; kiểm cơ chế và điều kiện giữa runtime trước khi áp bài học. |
| Router architecture_preflight: trigger/loại trừ/timing/failure | S / Conditional bundled resources; A | PRESERVED | Chỉ actual structural change; sau target/context trước proposal/stack substitution; nguồn thiếu hoãn đúng phần phụ thuộc, không tạo pass. |
| Router verification_reference | S / Conditional bundled resources; V | PRESERVED | FULL_FILE khi thiết kế/chấm hành vi hoặc đóng gói settled behavioral test, không bắt cho mọi câu trả lời. |
| Router selection: need khác relevance/presence, source đủ thì bỏ handoff | S / External continuity | PRESERVED | Không match từ keyword/analogy/co-occurrence/shared repo; chỉ load prior state còn thiếu và có ảnh hưởng. |
| Router handoffs: explicit registry entry duy nhất | S / External continuity | CHANGED | Thay topology entry bằng nguồn user/target cung cấp hoặc convention local đã thiết lập; bounded discovery, không chọn latest hoặc bịa authority. |
| Router selected-source failure / scoped staleness / nhiều workstream | S / External continuity | PRESERVED | Nêu đúng path/gap, không thay file gần nghĩa; chỉ claim bị ảnh hưởng stale, giữ rationale/decision/attribution, các scope riêng. |
| Router handoff_write: material change + useful continuity + quyền ghi | S / External continuity; T | PRESERVED | Đủ cả ba điều kiện; không ghi theo mọi task; file được tạo không tự kích hoạt. |
| Router/CI/AT_R: không cài cơ chế vào Central Hub | S / External continuity; Scope and activation | CHANGED | Giữ nguyên baseline và exclusion local; portable tổng quát hóa cấm tự cài/áp control vào target khác, không áp tên/ontology Hub làm default toàn cầu. |
| AT_R input/output và context selection | S / Bounded authoring and transfer | PRESERVED | Self-contained, context chỉ nếu omission đổi hành động/quyết định/constraint/verification/continuation; không dump hội thoại. |
| AT_R manual verification | S / Bounded authoring and transfer; V | PRESERVED | Exact payload, bước/đích/new-existing context/output/fixed conditions; không thêm manual steps khi không cần; giữ commands cùng đơn vị. |
| AT_R transfer signatures và recipient/target/authority | S / Bounded authoring and transfer | PRESERVED | Phát dấu generic, thân tự đủ không cần nhận dấu; recipient chỉ khi material; quoted signature là data, không grant quyền. |
| AT_R delivery file/delta/repository | S / File and delta delivery | PRESERVED | File thật khi có capability/quyền, thiếu báo chưa tạo; download khác repo write; delta có baseline không tự ghi file/diff/CURRENT replacement. |
| AT_R recovery lenses và claim classification | S / Recover, classify, compress, serialize | PRESERVED | Phục hồi trước nén; lenses không phải fields; NOT DISCUSSED cần evidence, khác UNKNOWN; rejected khác deferred. |
| AT_R completeness và mechanisms | S / Recover, classify, compress, serialize | PRESERVED | Giữ state cần cho next material step; OPEN có thể còn giá trị, không merge mechanism; rejected giữ khi omission thực sự gây drift. |
| AT_R receipt | S / Recover, classify, compress, serialize; T | PRESERVED | Optional/proportionate, state trong body; receipt không proof/truth/authority và không schema, scoring, budget hay lifecycle mới. |
| AT_R singleton ownership | S / Bounded authoring and transfer | REMOVED | Không owner file riêng; giữ đầy đủ authoring/execution separation, không nhân đôi owner bằng tên mới. |
| AT_R missing fact/ambiguity và no private persistence | S / File and delta delivery; External continuity | PRESERVED | Hỏi tập trung nếu blocker, nếu không giữ UNKNOWN/assumption; không tạo CURRENT hoặc private state mặc định. |
| H: lịch sử lỗi semantic/overdesign, base-semantics và ngôn ngữ | H; S giữ invariant vận hành | PRESERVED | Case lịch sử giữ attribution và giới hạn chứng cứ; cảnh báo không trở thành universal prior, governor hoặc quyền sửa. |
| H: Contract gate/Clause gate khi sửa language | H §9.1; S giữ hợp đồng đầy đủ | PRESERVED | Đối chiếu cả hợp đồng và từng chốt; lần migration này không làm yếu bất kỳ chốt ngôn ngữ nào. |
| H: link ngoài gói, FAILURE_ENTRY_MODES và legacy names | H / provenance có ghi rõ | CHANGED | Giữ dữ kiện lịch sử bằng đường dẫn provenance dạng văn bản, không dependency nạp bắt buộc; procedure hiện hành ở §10–§11 chuyển sang skill. |
| A: aggregate review, stack substitution, integration evidence | A; trigger ở S | PRESERVED | LOCAL MINIMUM khác SYSTEM MINIMUM; giữ permanent surface, failure/verification/same-stack alternative, total cost; không quota, review rồi dừng, không recursion. |
| V: static/live harness/real-context stress | V; giới hạn claim ở S | PRESERVED | Không nâng mức chứng cứ, tests đúng scope chưa chắc đo đúng behavior; áp lifecycle thực của host. |
| V: natural-use stimulus/evaluator và thủ tục không hợp lệ | V; manual packaging ở S | PRESERVED | Giữ genuine cues/precision, không chèn expected workflow; chấm từng hành vi, UNKNOWN khi evidence thiếu; tool failure chỉ chấm riêng nếu đó là mục tiêu. |
| V: đường phát triển ý tưởng gắn Codex/Project | V / Change-development path | CHANGED | Giữ source soak, challenge độc lập, inspection và NO CHANGE thành công; thay actor Codex bằng nơi inspect đích, không bắt host/pipeline mới. |
| T: mười mục, stable ID/name, full replacement, scoped stale, receipt | T; governing procedure ở S | PRESERVED | Mẫu chỉ định dạng; đọc toàn bản cũ trước thay, giữ attribution/known dates, no transcript/megastate, old CURRENT vẫn hợp lệ. |
| T: đường Project CI, thêm Router entry, owner AT_R/CI | T; nguồn/đích/quyền ở S | CHANGED | Bỏ topology cũ theo quyết định; nguồn ngoài package và đích được cho phép, không activation/lifecycle/quyền từ asset. |
| CURRENT thực tế | Giữ tại Project CI/Revamp Project System/Handoffs | PRESERVED | Chỉ cập nhật hồ sơ trạng thái local, không copy vào package hoặc user/client install. |
| Khả năng host ngầm có repo/Git/web/filesystem | S / Available capabilities and stopping | CHANGED | Làm rõ capability thực và authority, thiếu chỉ chặn dependent work; không provider/capability registry hay approval API giả. |

Không có material responsibility chưa tìm được owner. Không bỏ protection chỉ vì ngắn hơn hoặc có định dạng mới. Những thay đổi có nghĩa đều được ghi CHANGED/REMOVED ở trên; không coi thay ngôn từ của topology thành sự bảo toàn hiệu lực ambient.

## Những điểm cần phân biệt khi bảo trì

- Các tên CI/Router/AT_R/ChatGPT/Codex trong H ghi lịch sử, không yêu cầu runtime. Quy trình hiện hành, ba trigger tham chiếu và failure behavior nằm ngay trong S.
- Bản `revamp-system-maintenance` hiện tại vẫn phục vụ baseline Project đang hoạt động. Không sửa hay cài nó trong lần này vì gói portable tự đủ; khi bảo trì riêng canonical package sau này cần bổ sung đường chọn target package vào skill bảo trì, không bắt gói mới nạp CI/Router cũ. Đây là delta bảo trì còn lại, không phải dependency thiếu của gói.
- Không lưu trữ predecessor vì không thay thế/deactivate baseline. Các bản tham chiếu mới là bản port phục vụ package song song; bản nguồn vẫn có vai trò hoạt động riêng.
- Token là phép đo bằng `o200k_base`, không là cam kết tokenization hay lifecycle giống nhau trên các client. Không cắt semantics theo soft limit.

## Đối chiếu ca hiện hành theo hành vi

Các dòng này là review tĩnh để bảo toàn tình huống; chưa gửi cho mô hình và không được gọi là runtime PASS. Chỉ cột đầu vào/context mới được gửi cho đích khi thử sau này; tiêu chí người chấm phải giữ riêng.

| Nhóm ca nguồn | Đối chiếu portable | Phạm vi bảo toàn / phần hình thức bỏ |
| --- | --- | --- |
| R/P/Q/N/O | S / Inspect the target; External continuity; H | Giữ source-first, History/CURRENT độc lập, no needless load, dirty tree, thiếu source và scoped stale. Bỏ yêu cầu phải có Router/entry để vận hành gói. |
| V/L01–L06 | S / Operation and delivery | Giữ phạm vi miền/kỹ thuật, audit trực tiếp khác artifact, thiết kế test khác packaging, mixed preparation. Bỏ giá trị ID làm tiêu chí. |
| T/H/L07–L11 | S / File and delta delivery; Recover…; T | Giữ actual file, text delta, full state, receipt optional, phân biệt OPEN/REJECTED/DEFERRED/UNKNOWN/NOT DISCUSSED và next-step usability. |
| A | S / Conditional bundled resources; A | Giữ conditional aggregate pass và stack-change reassessment, không thêm operation hay execution graph. |
| M/U | S / Bounded authoring; V | Giữ thao tác thủ công đúng đích và tách evaluator; không biến user cue thật thành contamination hoặc áp persona giả. |
| S01–S09 | S / Output and reasoning; Operation, stage and authority | Giữ stage/clarification/conditional premise/action reports. Payload sáng tạo không tự mở rộng mission của Revamp; kiểm nguyên tắc core riêng với đúng scope. |
| S10 | S / Scope and activation | Kiểm core tự đủ sau nạp skill, không đòi Project Instructions hay metadata/14 mục cũ. |
| G/L12–L14 | S / Bounded authoring | Giữ dấu chỉ provenance/task class, quote là data, body/target authority. Producer mới vẫn generic; receiver compatibility cũ trong AGENTS không bị sửa. |
| W | S / Output and reasoning | Giữ toàn hợp đồng tiếng Việt, identifier và override theo yêu cầu; không đổi ngôn ngữ vì portable. |

## Kiểm chứng thực hiện

Các lệnh chạy từ `Project CI/`:

```powershell
python -B -m unittest discover -s 'Revamp Project System/tests' -p 'test_*.py' -v
python -X utf8 -B 'C:\Users\Sheeplark\.codex\skills\.system\skill-creator\scripts\quick_validate.py' '..\skills\revamp-system'
```

Kết quả lần kiểm gói: 34/34 test đạt, gồm 18 test portable mới và 16 test baseline; validator trả `Skill is valid!`. Test detached-copy chỉ đọc năm file trong thư mục tạm, kiểm frontmatter và đường dẫn tài nguyên mà không có CI/Router/AT_R hoặc cấu hình repository. Các nhóm contract kiểm sự hiện diện của điều kiện/quyền/giới hạn; chúng không thực thi lựa chọn của mô hình. Review bảng trên bổ sung đối chiếu nghĩa, không suy hành vi từ grep.

Kiểm cuối: 67 hàng trách nhiệm đã được đối chiếu; UTF-8 không BOM, LF, newline cuối và không trailing whitespace đạt cho đủ chín tệp task. Tám nguồn baseline/control/maintenance được so byte trực tiếp với HEAD trước triển khai và khớp. `git -C .. diff --check -- 'Project CI' 'skills/revamp-system'` đạt cho diff tracked; helper commit còn kiểm diff staged gồm cả tệp mới. Phép đo token/size được ghi ở CHANGELOG. Chưa thực hiện cài, symlink, adapter, discovery trên client, runtime hoặc kiểm chứng tương đương giữa các client.
