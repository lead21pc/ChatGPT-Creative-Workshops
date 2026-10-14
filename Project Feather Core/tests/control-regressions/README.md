# AetherFire control regressions — quy trình trong giai đoạn chỉnh sửa canon

Đây là công cụ kiểm tra **không có thẩm quyền nguồn**. Case và metadata chỉ là dữ liệu thử nghiệm: không phải canon, không phải nguồn, không phải CI hay Source Router, và không thể thay thế anti-drift overlay. Kết quả thử nghiệm không xác lập trạng thái chân lý, không giải quyết UNKNOWN hoặc xung đột, không sửa canon và không cấp quyền sửa control file. Một lỗi kiểm tra yêu cầu xem xét; không mặc nhiên yêu cầu sửa tài liệu có thẩm quyền để làm phép thử đạt. Người dùng giữ quyền chấp nhận kết luận và thay đổi.

Runner chỉ chạy READ_ONLY: đọc tệp, kiểm tra cấu trúc, tính hash, xem Git, chọn case và in JSON ra stdout. Không tự chạy mô hình, Codex CLI, OpenAI API, ChatGPT Project, build hoặc verifier tạo tệp; không tạo báo cáo trên đĩa. CONTROL_SEMANTIC là nhãn loại case để nhập kết quả về sau, không phải khẳng định đã chạy semantic test. Kết quả Codex/control-semantic không tương đương kết quả live-runtime của ChatGPT Project. Các case dùng tác nhân tổng hợp; câu trả lời mô hình lịch sử chưa được xác minh. Bản ghi hoà giải riêng cũng không phải bằng chứng lỗi runtime.

## Hợp đồng đang có hiệu lực và nguồn gốc phát triển

Thư mục `llm-controls/global-instructions/ChatGPT Plus+ Era` lưu một dòng CI dùng chung có phiên bản v7.x, v8.x, các bản v8.5.1/v8.6 mang tên temp và các thử nghiệm v9.0 temp. Những tệp cùng tồn tại trong kho không đồng thời hoạt động. FTH CI v3.3 hiện khai báo nền ChatGPT 8.8 và tự chứa quy tắc cần dùng; runner đọc khai báo để ghi nhận xuất xứ, không biến nền ngoài thành phụ thuộc đọc lúc chạy của CI. Source Router riêng nắm việc định tuyến nguồn và chọn overlay dưới hợp đồng CI; chỉ overlay liên quan nhiệm vụ mới tham gia. Bản v8.4, v9.0 temp hoặc tệp mới hơn không tự trở thành nền AetherFire. Quan hệ kế thừa/phát triển giữa các phiên bản không phải quan hệ cùng chạy.

Mỗi case kiểm tra **ranh giới ngữ nghĩa của hợp đồng hiện hành**, không cố dựng lại prompt lỗi cũ hay coi vị trí đặt quy tắc là chân lý. Trường provenance mô tả căn cứ hiện tại: CURRENT_CONTROL_CONTRACT cho tám case và CURRENT_RECONCILIATION_EVIDENCE cho case hàng không. Nó không chứng minh phản hồi runtime đã xảy ra. active_control_anchors là các tệp điều khiển đang tham gia, mỗi tệp có đường dẫn và hash tại lúc hiệu chỉnh; các tham chiếu lịch sử chỉ được đặt trong provenance và không phải neo chạy. SHA thay đổi hoặc phiên bản đang hoạt động đổi chỉ báo cần xem xét, không tự chuyển vòng đời hoặc chứng minh ranh giới ngữ nghĩa đã hỏng. Nếu một quy tắc chuyển từ overlay lên CI dùng chung nhưng hành vi vẫn được giữ, mục tiêu của case vẫn có giá trị; người dùng quyết định cập nhật neo.

Hợp đồng điều khiển rõ ràng **không đồng nghĩa** phạm vi canon đã sẵn sàng thử nghiệm ngữ nghĩa. AetherFire đang chỉnh sửa và hợp nhất theo từng miền. Cả chín case bên dưới hiện là DRAFT: người dùng chưa tuyên bố các phạm vi đó sẵn sàng cho hồi quy. Chúng chỉ là ứng viên, không phải cổng chấp nhận. Không suy ra độ sẵn sàng từ số lượng tệp, tên CURRENT, sự có mặt của overlay, ít thay đổi gần đây hay kết quả kiểm tra cấu trúc.

| Case | Trạng thái | Kiểu dò chủ đạo | Ranh giới được giữ |
| --- | --- | --- | --- |
| interaction_containment | DRAFT | DRIFT_PROBE, cặp điều kiện | Tăng tương tác không xác lập bao chứa |
| cooccurrence_dependency | DRAFT | DRIFT_PROBE | Đồng hiện không xác lập phụ thuộc |
| power_authority | DRAFT | DRIFT_PROBE, cặp điều kiện | Tăng sức mạnh không cấp thẩm quyền |
| capability_availability | DRAFT | COMPOSITION_PROBE | Năng lực thô không tự thành năng lực sẵn dùng/được phép |
| alliance_command | DRAFT | DRIFT_PROBE | Liên minh không tự tạo chỉ huy chung |
| unknown_invention | DRAFT | COMPOSITION_PROBE, cặp điều kiện | Cơ chế hợp lý không lấp UNKNOWN |
| relationship_immunity | DRAFT | DRIFT_PROBE, cặp điều kiện | Tầm quan trọng không bảo đảm cứu sống |
| simulation_canon | DRAFT | INVARIANT_SENTINEL | Kết quả mô phỏng không thành canon |
| stable_aviation_supremacy | DRAFT | DRIFT_PROBE | Hạ tầng ổn định được xác nhận không thành độc quyền/ưu thế tuyệt đối |

Các cặp BASE/VARIANT nằm trong trường input hiện có. Phép đánh giá về sau phải so sánh **trạng thái và chuyển tiếp ngữ nghĩa**, không so chữ; Phase 1.5 chưa thực thi hay tự đánh giá chúng.

## Cập nhật neo CI và lưu trữ — 2026-10-07

Các fixture hiện neo vào CI 3.1 bằng đường dẫn và SHA-256 đã đối chiếu; hai neo nền 8.5 chuyển sang nền 8.8 được CI khai báo. Phần CI trong provenance dùng tên mục thực tế của 3.1. Các input, ranh giới được bảo vệ và trạng thái DRAFT được giữ nguyên; việc này không xác nhận kết quả mô hình hoặc kích hoạt test ngữ nghĩa. Các neo overlay/Router khác không được tự hiệu chỉnh: cảnh báo thiếu, lệch hash hoặc phiên bản vẫn là yêu cầu xem xét riêng.

Runner chấp nhận cả tiêu đề `ChatGPT 8.8 base` và `ChatGPT v8.8 base`, nhưng vẫn đòi khai báo phiên bản rõ, khớp tên CI và tệp nền tồn tại. Các ghi chú coverage có ngày bên dưới là lịch sử tại lúc thêm case, không thay bản hiện hành ở đoạn này; lỗi đọc tiêu đề được nhắc trong các ghi chú đó đã được sửa trong tác vụ lưu CI.

## Giữ bổ sung riêng trên main — 2026-10-10

Giữ sáu case DRAFT: `modular_competence_chain`, `modular_expertise_authority`, `modular_function_colocation`, `world_logic_author_intent_and_control`, `world_logic_intentional_imperfection`, `world_logic_unknown_intent_and_repair`. Chỉ đổi đường dẫn theo cấu trúc mới; nội dung dò, SHA neo và vòng đời không đổi. Neo lịch sử trỏ vào archive chỉ để truy nguyên, không chọn control hoạt động; cảnh báo neo chưa được tác giả chốt vẫn được giữ. Không chạy hay xác nhận kết quả mô hình.

## Vòng đời và độ sẵn sàng theo phạm vi

- DRAFT: định nghĩa/neo có thể kiểm tra về cấu trúc; chưa có phạm vi thử nghiệm được người dùng chấp thuận. Không chọn làm hồi quy ngữ nghĩa, không có kết quả đạt/trượt.
- ACTIVE: người dùng đã chấp thuận phạm vi thử có giới hạn, nguồn và điều khiển hiện hành đã được đối chiếu, và case được chấp thuận triển khai. Kết quả vẫn chỉ mang tính tham khảo.
- STALE_CANDIDATE: case từng ACTIVE được người dùng đặt sang diện xem xét do neo thay đổi đáng kể hoặc phạm vi canon được mở lại. Không dùng như cổng chấp nhận hiện hành.
- RETIRED: giữ để truy nguyên, không chọn bình thường.

Runner **không tự chuyển trạng thái**. Với ACTIVE có neo lệch, nó ghi ứng viên xem xét trong stale_candidates nhưng trạng thái lưu trong JSON vẫn là ACTIVE; case ấy bị loại khỏi selected_cases cho đến khi người dùng xem xét. Với DRAFT, neo lệch được báo mặc định trong draft_anchor_warnings và trong anchor_reasons khi liệt kê DRAFT; không biến DRAFT thành STALE_CANDIDATE hay ACTIVE. Với STALE_CANDIDATE đã lưu, runner báo để xem xét và không chọn làm hồi quy. Quyền quyết định kích hoạt, tạm dừng, hiệu chỉnh hoặc rút case thuộc người dùng qua một tác vụ sửa kho được duyệt riêng.

TESTABLE_SCOPE_LOCKED là quyết định **rõ ràng của người dùng** rằng một phạm vi cụ thể đủ ổn định ở độ phân giải cần thử. Nó không đóng băng canon, không xóa UNKNOWN, không xác nhận mọi miền lân cận và không phải trạng thái toàn dự án. Miền A sẵn sàng không tự làm giao diện A–B sẵn sàng; một giao diện A–B được người dùng chốt để thử có thể thử dù các câu hỏi không liên quan trong từng miền còn OPEN. Case chỉ dùng tác nhân tổng hợp, độc lập nguồn canon cũng vẫn DRAFT cho tới khi người dùng cho phép bắt đầu thử ngữ nghĩa.

## Chạy từ thư mục Project Feather Core

    pwsh -NoProfile -File .\tests\control-regressions\run.ps1

Lệnh mặc định kiểm tra cấu trúc và chỉ chọn ACTIVE có neo phù hợp. Hiện cả chín case là DRAFT nên selected_cases rỗng. Runner vẫn kiểm tra tệp/gói tối thiểu, phiên bản CI dự án, Router và năm họ overlay theo số, nền ChatGPT CI do CI dự án khai báo, schema, neo SHA-256 và trạng thái Git. Phiên bản cao nhất trùng hoặc tên sai định dạng được báo lỗi. Không thực thi trường input, không đánh giá ngữ nghĩa và không sửa trạng thái case.

    pwsh -NoProfile -File .\tests\control-regressions\run.ps1 -ListDrafts

    pwsh -NoProfile -File .\tests\control-regressions\run.ps1 -ChangedControlFile 'Anti-Drift Source/FTH_Anti_Drift_Total_War_RP_v1.1.md'
    pwsh -NoProfile -File .\tests\control-regressions\run.ps1 -ChangedControlFile 'llm-controls/global-instructions/ChatGPT Plus+ Era/chatgpt v8.8.txt'
    pwsh -NoProfile -File .\tests\control-regressions\run.ps1 -ChangedControlFile 'Anti-Drift Source/khong-co-anh-xa.md'

recheck_on dùng đường dẫn tương đối từ Project Feather Core cho tệp dự án, hoặc từ thư mục repo cha cho ChatGPT Plus+ Era. Danh sách ghi đúng tệp đang tham gia thay vì mọi phiên bản lịch sử. -ListDrafts chỉ in danh sách DRAFT để xem xét, không chọn chúng. Khi có ChangedControlFile, selected_cases chỉ chứa ACTIVE có neo phù hợp; draft_review_matches là DRAFT_REVIEW_MATCH và stale_review_matches là ứng viên xem xét, đều review_only. Nếu một bản CI/Router/overlay mới trở thành phiên bản cao nhất được chọn, runner nhận diện họ phiên bản từ neo cũ để tìm case liên quan; nó không tự đổi vòng đời hay thay neo. Nền ChatGPT mới chỉ được nhận khi CI dự án **khai báo** nó. Bản v9.0 temp tồn tại riêng lẻ không làm đổi nền. Đường dẫn không khớp được báo trong unmapped với nghĩa **UNMAPPED**, không suy ra không có tác động. Metadata chọn lại không lập lịch, không cấp quyền sửa canon hay điều khiển.

Khi CI dự án hoặc nền ChatGPT được khai báo đổi về sau, ACTIVE có neo cũ bị giữ ngoài lựa chọn và báo ứng viên xem xét; DRAFT vẫn DRAFT dù anchor_reasons báo phiên bản hoặc nền đã đổi. Runner không tự thay neo hoặc phán quyết mục đích ngữ nghĩa sai. Nếu khai báo nền mới không rõ hoặc tệp nền thiếu, selected_upstream_base là BLOCKED. Người dùng quyết định hiệu chỉnh và kích hoạt lại trong phạm vi đã chọn.

## Đầu vào kiểm chứng thuần túy

Các probe dưới đây chỉ truyền JSON trong đối số, không thay đổi tệp. Chúng phục vụ kiểm tra logic phiên bản và stale; không được dùng làm kết quả semantic.

    pwsh -NoProfile -File .\tests\control-regressions\run.ps1 -VersionProbeJson '{"family":"CI","names":["FTH_CI_version_v2.9.md","FTH_CI_version_v2.10.md"]}'
    pwsh -NoProfile -File .\tests\control-regressions\run.ps1 -VersionProbeJson '{"family":"CI","names":["FTH_CI_version_v2.6.md","FTH_CI_version_v02.06.md"]}'
    pwsh -NoProfile -File .\tests\control-regressions\run.ps1 -AnchorProbeJson '{"path":"Project Feather Core CI/FTH_CI_version_v3.2.md","sha256":"0000000000000000000000000000000000000000000000000000000000000000"}'

Đối số snapshot tùy chọn là JSON {"root":"<đường dẫn tuyệt đối thư mục repo cha>","files":[{"path":"Project Feather Core/MANIFEST.md","sha256":"<SHA-256 lúc bắt đầu tác vụ>"}]} truyền qua ProtectedSnapshotJson. Runner chỉ so sánh các file được cung cấp trong snapshot, không tự suy ra bản chụp trước khi bắt đầu tác vụ và không bảo đảm bao phủ mọi file cấm sửa. Nếu không cung cấp, protected_snapshot là LIMITED_CHECK. Việc đọc Git chỉ ghi nhận tình trạng hiện tại, không phân biệt thay đổi cũ/mới nếu thiếu bản chụp đầu kỳ.

Chỉ khi có yêu cầu nhập kết quả thủ công, ManualResultJson kiểm tra nhãn PASS, POTENTIAL_VIOLATION, AMBIGUOUS hoặc BLOCKED, gắn case và in hash/độ dài phản hồi cùng ghi chú được cung cấp; không gọi mô hình, tự đánh giá hay lưu qua các lần chạy. DRAFT bị từ chối mặc định. Một thí nghiệm thủ công với DRAFT phải được người dùng duyệt riêng rồi mới truyền đồng thời -ManualResultJson và -ApprovedDraftExperiment; cờ này chỉ khai báo sự chấp thuận từ bên ngoài, không tự chứng minh hoặc thay trạng thái DRAFT. Case STALE_CANDIDATE, RETIRED hoặc ACTIVE cần xem xét neo không nhận kết quả qua đường nhập thông thường.

## Bản đồ thao tác khi tiếp tục phát triển

| Tình huống | Quy trình có thẩm quyền |
| --- | --- |
| Đang chỉnh sửa canon | Chỉ chạy kiểm tra cấu trúc READ_ONLY; giữ case ngữ nghĩa DRAFT/STALE đúng trạng thái; không suy ra sẵn sàng. |
| Người dùng tuyên bố phạm vi thử được | aetherfire-source-audit đối chiếu CI, Router, nguồn CURRENT, OPEN/UNKNOWN/CONFLICTED, hòa giải và overlay trong ranh giới; ci-behavior-engineering chế độ TEST thiết kế bộ probe tối thiểu; trình kế hoạch case/neo/biến ngoài phạm vi; người dùng chấp thuận; milestone-executor triển khai; review-before-merge rà chỉ đọc. Nếu lệnh ban đầu đã cho phép triển khai chính xác phạm vi đó, không cần hỏi lại. |
| Điều khiển thay đổi | Runner chọn ACTIVE liên quan; DRAFT chỉ xuất hiện trong draft_review_matches; STALE chỉ báo xem xét. Không suy ra quyền sửa tệp phụ thuộc. |
| CI dự án chuyển nền | Đối chiếu CI mới và nền được khai báo; xem lại neo liên quan, không tự thay và không chọn toàn bộ dòng ChatGPT CI. |
| Người dùng mở lại phạm vi canon | Xem xét các ACTIVE liên quan; người dùng có thể duyệt chuyển sang STALE_CANDIDATE; chỉnh sửa canon có chủ đích không tự bị gọi là regression; khi khóa lại phạm vi, hiệu chỉnh hoặc thay case rồi mới kích hoạt lại. |
| Lỗi workload thực tế mới | systematic-debugging tìm nguyên nhân nếu lỗi thật; ci-behavior-engineering phân tích/sửa tầng phù hợp; case hồi quy mới là tùy chọn, không đòi phục dựng mọi lỗi lịch sử. |
| Yêu cầu thử runtime | Chỉ ACTIVE trong phạm vi được người dùng cho phép; chuẩn bị prompt sạch và thử **ChatGPT Project AetherFire thực tế** trong tác vụ riêng, ghi phản hồi và đánh giá tham khảo. Codex/API không thay thế. |

Trong bước kích hoạt, kế hoạch phải nêu phạm vi testable, neo nguồn đang có hiệu lực, neo điều khiển, biến cố ý để ngoài, lý do mỗi probe và DRAFT nào tái dùng được. Nếu nguồn chưa đủ để xác định ranh giới, báo đúng điểm chặn; không điền UNKNOWN hoặc tự tạo canon. Người dùng có thể chấp thuận, yêu cầu sửa, hoãn hoặc bác bỏ. Không tạo registry sẵn sàng toàn dự án, scheduler hay case giữ chỗ. Mỗi thay đổi vòng đời là thao tác sửa kho được duyệt, không phải phản ứng tự động của runner.

Sáu skill giữ vai trò riêng: aetherfire-source-audit cho căn cứ nguồn; ci-behavior-engineering TEST cho hợp đồng và probe; milestone-executor cho triển khai đã duyệt; review-before-merge cho rà soát cuối chỉ đọc; systematic-debugging chỉ khi có lỗi thực tế; git-test-branch chỉ khi người dùng yêu cầu nhánh riêng. Không cần skill hồi quy mới.

## Actor reception coverage (added 2026-10-02)

The repository resolver now includes `Actor_Reception_Normative_Signals`. Router v4.1 adds the task gate and scoped dependencies; Router v4.0 is preserved byte-for-byte under `Anti-Drift Source/Source_Archive/`. This changes repository control selection, not installed ChatGPT Project state.

Six synthetic `CONTROL_SEMANTIC` cases remain `DRAFT`; their inputs and protected distinctions are review candidates, not model results, canon, or acceptance gates:

| Case | Protected behavior |
| --- | --- |
| actor_reception_mixed_signals | Keep doctrine belief, conflicting interests, public compliance, and private duration preference separate. |
| actor_reception_delayed_notice | Publication does not update an actor without an established access path. |
| actor_reception_leak_before_notice | A credible established leak may supply knowledge before official notice, without proving the leak true. |
| actor_reception_emergency_duration | Prior extensions may affect expected duration without changing formal duration or proving a new extension. |
| actor_reception_propaganda | Exposure and contrary experience do not force complete belief or complete rejection. |
| actor_reception_source_authority | Canon ownership resolved by the Router does not grant actor knowledge of in-world authority. |

Each case pins CI 3.0, Router 4.1, the reception overlay, and Modular Concept Architecture. Conditional overlay anchors are included only where the particular probe needs their reasoning. Review the relationships in the response, not exact strings. Runner schema/version/anchor checks do not execute these probes. Existing DRAFT cases and their historical anchors remain unchanged.

    pwsh -NoProfile -File .\tests\control-regressions\run.ps1 -ListDrafts -ChangedControlFile 'Anti-Drift Source/FTH_Anti_Drift_Actor_Reception_Normative_Signals_v1.0.md'

Lỗi parser được ghi nhận ở baseline lịch sử này đã được sửa tại commit `30c39d3` ngày 2026-10-08: runner chấp nhận cả `ChatGPT X.Y base` và `ChatGPT vX.Y base`. Cặp control hiện hành được mô tả ở phần active stack; parser vẫn kiểm tra khai báo nền và tệp nền, không suy mọi lỗi BLOCKED đều đã được giải quyết. Đây chỉ là kiểm chứng cấu trúc, không xác nhận kết quả ngữ nghĩa hoặc runtime Project.

For a separately authorized live Project experiment:

1. Verify the installed CI, Router, reception overlay, MCA, and task-required conditional controls against the case's anchors. Record the actual installed versions; repository presence alone is insufficient.
2. In a fresh Project Feather Core chat for each case, submit its `operation`, `boundary`, and full `input` as a synthetic hypothetical. Keep real canon outside the fixture. Run both BASE and VARIANT where supplied.
3. Record the response and assess whether the stated premises, knowledge paths, temporal relations, and `protected_distinction` survive without the `forbidden_conversion`. Use advisory `PASS`, `POTENTIAL_VIOLATION`, `AMBIGUOUS`, or `BLOCKED`; do not judge exact wording.
4. Keep the six cases DRAFT unless the author explicitly authorizes lifecycle changes. This procedure neither deploys controls nor grants permission to ingest a DRAFT result automatically.

## Belief / culture coverage (added 2026-10-05)

The architectural gap is cultural claim extent, transmission/retention, change, and audience-dependent symbolic recognition, not a missing full culture engine. Belief / Culture v1.0 owns those distinctions. Actor Reception still owns individual appraisal and public/private states; Worldbuilding still owns institutional operation, authority, reproduction, and persistence. Economy and Total War retain their domain-specific depth and stopping. Conditional dependencies do not activate from labels alone.

Router v4.3 adds only the family and material-task gate, retaining v4.2's source gates and default Library `Project Feather Core` lookup. Its predecessor is archived byte-for-byte after verification. CI 3.0, canon, open issues, existing overlays, and older case lifecycles/anchors are not rewritten.

Eight synthetic paired cases remain DRAFT:

| Case | Scope / inventory coverage |
| --- | --- |
| belief_culture_ritual_belief | A/F: required ritual or institutional declaration does not prove private belief; explicit sincere belief may be affirmed. |
| belief_culture_doctrine_practice | B/C: prohibition is not compliance; doctrine/practice tension is not automatically a source contradiction. |
| belief_culture_group_extent | D: group evidence is not polity-wide evidence; explicit commonality is valid without invented diversity. |
| belief_culture_symbol_authority | E/K: meaning, recognition, authority, and obedience remain separate; a narrow lookup stays narrow. |
| belief_culture_transmission_unknown | I: presence is not a transmission history; an explicit partial path may be affirmed without invented carriers. |
| belief_culture_change_pressure | G/H: technology, material incentives, and biology constrain without selecting cultural outcomes; bounded observed adoption is valid. |
| belief_culture_proposal_scope | J: requested brainstorming permits labeled options, not canon admission or later reuse as current evidence. |
| belief_culture_actor_interpretation | L: shared membership/public wording does not erase established private interpretations. |

Each case pins current CI 3.0, Router 4.3, the new overlay, and only its applicable conditional controls. BASE and VARIANT are hypothetical premises, not observed responses. Source-specified supernatural effects remain valid; no Earth social model overrides them.

The runner adds numeric family resolution and changed-control matching only. Schema, SHA anchors, lifecycle, numeric ordering, and duplicate-version probes are structural checks; they do not execute or judge the paired inputs. Lỗi upstream-base parser được ghi nhận tại mốc tích hợp lịch sử này đã được sửa ngày 2026-10-08 (`30c39d3`). Older DRAFT anchor warnings are review signals, not lifecycle changes.

For a separately authorized live Project experiment, verify the installed controls against the fixture anchors, then submit the complete operation, boundary, and input in a fresh Project chat as a synthetic hypothetical. Assess both invalid inferences and the permitted affirmative conclusions against the protected distinction; do not judge exact wording. Preserve DRAFT unless activation is explicitly authorized. Repository publication does not deploy these controls.

## Conditional response lifecycle coverage (added 2026-10-05)

MCA v1.2 extends its existing state-transition and controlled-branch responsibility; no separate overlay, registry family, or Router hook is added. CI/Router retain source authority and canon status. Domain controls retain reception, institutional, operational, mortality, professional, and economic reasoning through their existing material-task gates.

Seven paired synthetic cases remain DRAFT, labeled `ABSTRACT TEST ONLY / NOT CANON / NOT A HIDDEN SCENARIO`:

| Fixture / case | Protected behavior |
| --- | --- |
| A / conditional_branch_availability | Availability is not selection, execution, success, or a mandatory chronology; explicit valid choice remains allowed. |
| B / conditional_branch_concurrency | Supported concurrent branches persist; a material exclusive-resource constraint is not ignored. |
| C / conditional_branch_trigger_receipt | Simulation knowledge does not activate actor-mediated responses; a supported bounded automatic detector remains valid. |
| D / conditional_branch_attempt_history | Failed attempts and pre-execution cancellations preserve their different histories; neither implies total defeat. |
| E / conditional_branch_remaining_objective | Surviving attribution can support an available diplomatic option without selecting it; invalid attribution can close it. |
| F / conditional_branch_termination | Loss of a required basis or fulfillment of a supported end condition changes persistence, not every other branch. |
| G / conditional_branch_canon_boundary | Successful simulation remains non-canon without normal scoped acceptance; accepting one event does not accept hidden causes. |

Each case pins CI 3.0, Router 4.4, MCA 1.2, and only applicable domain controls. The runner's existing numeric MCA resolver and changed-family matching require no code change. Older DRAFT lifecycles/anchors are not migrated. Structural checks validate schema, hashes, selection, and preservation, not model compliance. Lỗi upstream-base parser được ghi nhận tại mốc tích hợp lịch sử này đã được sửa ngày 2026-10-08 (`30c39d3`).

    pwsh -NoProfile -File .\tests\control-regressions\run.ps1 -ListDrafts -ChangedControlFile 'Anti-Drift Source/FTH_Anti_Drift_Modular_Concept_Architecture_v1.2.md'

For a separately authorized live Project test, verify the installed controls against the anchors and submit each complete operation, boundary, and BASE/VARIANT input in a fresh synthetic hypothetical. Compare supported states, transitions, and forbidden conversions, not exact words. Keep DRAFT and record the actual response before assigning an advisory semantic result; this addition does not deploy or run those tests.

## Trạng thái và giới hạn

PASS ở từng kiểm tra chỉ xác nhận cấu trúc tương ứng. FAIL là lỗi cấu trúc/đầu vào phiên bản/snapshot, không phải phán quyết semantic. BLOCKED báo dữ liệu hoặc thao tác đọc không hoàn tất. LIMITED_CHECK là bao phủ chưa đầy đủ; overall vẫn là LIMITED_CHECK khi các phép thử cấu trúc đạt vì runner không kiểm tra runtime hay toàn vẹn gói đầy đủ. Exit code: 0 cho LIMITED_CHECK, 1 cho FAIL, 2 cho BLOCKED.

Runner không sao chép logic hash của MANIFEST.md hoặc logic build. package_integrity chỉ báo LIMITED_CHECK: chưa chạy verifier hiện có, chưa xác nhận hash manifest và không gọi build. Nếu cần thẩm tra gói đầy đủ, phải theo quy trình kiểm chứng riêng có thẩm quyền và kiểm tra tác dụng phụ trước khi thực hiện. Thành công cấu trúc không chứng minh phạm vi canon sẵn sàng hoặc mô hình tuân thủ. Vòng đời là trạng thái case; PASS/POTENTIAL_VIOLATION/AMBIGUOUS/BLOCKED là nhãn kết quả ngữ nghĩa chỉ dành cho thử nghiệm được chấp thuận. Không có semantic FAIL tự động và không dùng test để đóng băng việc xây dựng lore.

## Router 5 / CI 3.3 active local stack

CI 3.3, Router 5.0 YAML và Pipeline 1.1 đã được promote ra thư mục control chính. Runner chọn phiên bản số cao nhất của từng family, gồm Router YAML và Authoring Pipeline. Các bản 3.2/4.4/1.0 giữ nguyên để rollback.

Chạy `python -B build_consolidation.py --check-router` và `python -B -m unittest discover -s tests` từ thư mục project. Tùy chọn cũ `--check-router-candidate` vẫn là alias tương thích của kiểm tra active stack. Kiểm tra cấu trúc không xác nhận retrieval, hành vi model hoặc live deployment.

`router-v5-probes.json` vẫn giữ 18 probe DRAFT/NOT_RUN. Khóa `candidate` và `candidate_expected` là nhãn lịch sử của phép so sánh với baseline; đường dẫn nay trỏ tới artifact đã promote, không phải một khóa chặn runtime. Không đổi lifecycle hay tạo kết quả model từ xác nhận sử dụng của người dùng. Audit trước promotion tại `Anti-Drift Source/candidates/ROUTER_V5_AUDIT.md` giữ vai trò provenance.

Để cài thủ công, dùng toàn bộ CI 3.3 làm Project instructions và đưa Router 5.0 cùng Pipeline 1.1 vào Project Sources/Library mà FTH đang dùng. Giữ current source generation và các overlay cần thiết; không trộn cặp baseline với active stack. Việc sửa repo không tự thay cấu hình Project live.
