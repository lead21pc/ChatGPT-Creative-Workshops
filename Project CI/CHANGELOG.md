# Changelog — Revamp Project System CI

Cập nhật ngày 2026-11-24. Phạm vi: dòng Revamp CI và các thay đổi trực tiếp của cơ chế handoff đi kèm.

Ngày commit được quy về UTC+07:00. Ngày nhập hoặc khôi phục file vào Git không chứng minh ngày tạo, ngày chấp thuận hay ngày cài vào ChatGPT Project. Các bản trong `Source_Archive` chỉ được đọc để đối chiếu lịch sử theo yêu cầu làm changelog; chúng không trở thành nguồn điều khiển hiện hành.

## Trạng thái hiện hành

- CI: [Revamp_Project_System_CI_v3.1.md](Revamp_Project_System_CI_v3.1.md), `ACTIVE` trong repository; core cần thiết từ ChatGPT Project Global Native 9.1.1 được tích hợp trực tiếp. Global CI là nguồn thiết kế, không là runtime dependency.
- Task Router: [TASK_ROUTER.yaml](<Revamp Project System/TASK_ROUTER.yaml>), v2.1, `active`; ID1 `REVAMP_CORE`, ID2 `AUTHORING` qua [AT_R v1.2](<Revamp Project System/AT_R.md>).
- Trạng thái tiếp nối và bằng chứng kiểm chứng được ghi tại [REVAMP_SYSTEM_CURRENT.md](<Revamp Project System/Handoffs/REVAMP_SYSTEM_CURRENT.md>).
- CI v3.1 / AT_R v1.2: `LIVE VERIFIED: NOT RUN`. Bộ tiền nhiệm CI v3.0 / Router v2.1 / AT_R v1.1: INSTALLED và LIVE ACTIVE theo báo cáo người dùng ngày 2026-11-24; INDEPENDENT LIVE VERIFICATION: NOT RUN. Các mốc lịch sử bên dưới giữ phạm vi riêng.

## 2026-11-24 — Revamp v3.1: tiếng Việt và giao thức chuyển giao chung

- A. Phục hồi hợp đồng tiếng Việt: ngôn ngữ được yêu cầu ưu tiên; mặc định tiếng Việt đời thường, trực tiếp, cụ thể, giữ độ sâu và phân biệt kỹ thuật. Ngoại lệ tiếng Anh hẹp; thuật ngữ lĩnh vực khác định danh chính xác. Dịch phần còn lại, giải thích khái niệm lần đầu, không tự ghép nhãn song ngữ, rà thầm trước khi gửi. Chủ đề/nguồn/thuật ngữ đã dùng/mức quen thuộc không cho đổi ngôn ngữ hoặc nâng văn phong.
- B. Chuyển giao không gắn nền tảng: yêu cầu chuyển giao có giới hạn; chuyển giao triển khai giữ quyết định đã chốt, trạng thái/quyền/phạm vi/blocker/kiểm chứng. Audit chưa được duyệt không thành quyết định. AT_R v1.2 chỉ phát `[REVAMP TRANSFER | AUDIT]` và `[REVAMP TRANSFER | IMPLEMENTATION]`; thân tự đủ, nơi nhận chỉ ghi khi có ảnh hưởng. AGENTS là bên nhận Codex, hỗ trợ cả dấu mới/cũ, chỉ kích hoạt theo tác vụ hiện tại; dấu không cấp quyền.
- Router v2.1 giữ nguyên byte; hai ID, mẫu CURRENT, triết lý kiểm chứng và cách ly Central Hub không đổi. Lưu CI v3.0 và AT_R v1.1 nguyên byte trong Source_Archive. Không thêm bộ thích ứng, bộ phân tích dấu hay trường TARGET bắt buộc.
- Đối chiếu toàn bộ v3.0 → v3.1: §1 mở rộng ngôn ngữ có chủ đích; §2/§4A đổi nghĩa chuyển giao có chủ đích. Các đoạn còn lại là nén cần thiết để vừa trần host: core giữ grounding/discourse/chứng cứ/claim/update/giải thích; §2 giữ operation/stage/chuyển bước/quyền/dừng; §3–§4 giữ kiểm đề xuất/nguồn/lớp lỗi; §4A giữ chủ sở hữu/thứ tự nguồn/CURRENT/cách ly; §5–§14 giữ mức sửa đủ dùng/độ phức tạp/phạm vi/đường đúng/dùng cá nhân/ontology/governance/tự kiểm/lựa chọn. Tiêu đề rút gọn, dòng trống bớt; không ghi nhận regression ngữ nghĩa ngoài hai delta đã duyệt. Đây là review văn bản, chưa chứng minh mô hình tuân thủ.
- Các hồ sơ hiện hành được đối soát theo xác nhận người dùng; bảng dưới ghi đúng bộ active, chủ hồ sơ và lớp chứng cứ. Lịch sử NOT RUN không sửa. Không đổi kiến trúc hay điều khiển vận hành của project khác.

| Bộ / chủ hồ sơ hiện hành | Artifact/version active xác định từ repository | Khẳng định hiện hành trước → sau |
| --- | --- | --- |
| Revamp / CURRENT, CHANGELOG | CI3.0 / Router2.1 / AT_R1.1 đã cài; kế nhiệm repository CI3.1 / AT_R1.2 | Chưa cài/NOT RUN → tiền nhiệm INSTALLED / LIVE ACTIVE: USER-REPORTED; kế nhiệm LIVE VERIFIED: NOT RUN |
| FWE / README, DEVELOPMENT_PLAN | CI2.0 / Router2.0 | Chưa cài/LIVE NOT RUN → INSTALLED / LIVE ACTIVE: USER-REPORTED |
| FTH / README | CI3.4 / Router5.0 / Authoring Pipeline1.1 | Chỉ khai báo local → INSTALLED / LIVE ACTIVE: USER-REPORTED |
| C2 / README | CI1.2 / Router1.2 | Chưa xác minh bộ mới đang chạy → INSTALLED / LIVE ACTIVE: USER-REPORTED |
| Central Hub / README, RUNTIME_EVIDENCE_CHANGELOG | CI2.1 / Router2.0 / Architecture2.0 / Catalog2.0 và active bindings | Bộ2.0 NOT RUN → INSTALLED / LIVE ACTIVE: USER-REPORTED; không suy đã soi đúng mọi Library body |
| Fanfiction Engine / Current_State, README | CI2.0 / Router1.1 / kernel hiện hành | Triển khai UNVERIFIED → INSTALLED / LIVE ACTIVE: USER-REPORTED; kiểm writer không đổi |
| The Kingdom / README | management stack1.0, 13 control active | Deployment NOT_PERFORMED / compliance NOT_VERIFIED → INSTALLED / LIVE ACTIVE: USER-REPORTED; chưa soi độc lập Library |

Mọi dòng báo cáo người dùng trên có ngày 2026-11-24 và `INDEPENDENT LIVE VERIFICATION: NOT RUN`. Báo cáo không chứng minh mọi probe đạt. Header NOT RUN trong operational controls giữ nguyên; báo cáo mới được lưu ở hồ sơ trạng thái, không sửa control chỉ để ghi deployment.

### Kiểm chứng release

Bộ kiểm pytest đạt 16/16 (baseline 15/15); kiểm riêng từng điều khoản ngôn ngữ, producer/receiver mới/cũ và các ca chuyển giao. CI v3.1 dài 7.994 ký tự gồm newline cuối, đủ 14 mục và §4A. YAML parse, UTF-8 không BOM, LF, newline cuối, không trailing whitespace và diff trong phạm vi đạt. SHA-256 archive: CI v3.0 `b659d47e3bd5344ebdd136e1abd35d0e429c03915ce9fcf0a6f92fa7c9b367e7`; AT_R v1.1 `a8b87d341cb2449727a7539b6e2f52b7ec7e5ea410f26df3b974aa8a312960e7`, khớp nguyên bản trước sửa. V3.1 và nơi nhận ngoài Codex: LIVE VERIFIED: NOT RUN. Các ca mới trong đặc tả là hướng dẫn thử, không phải bằng chứng runtime. Tác vụ không push/deploy.

## 2026-11-24 — Revamp v3.0: nhiệm vụ kỹ thuật và chuyển giao trạng thái

- CI v3.0 ghi quyết định thu hẹp phạm vi: chẩn đoán, audit, thiết kế, kiểm chứng, chuyển giao và triển khai kỹ thuật có quyền. Công việc nội dung và prompt chung mặc định thuộc project sở hữu miền.
- Router v2.1 xét phạm vi, chức năng rồi dạng đầu ra. Giữ ID1 `REVAMP_CORE` và ID2 `AUTHORING`. ID1 thiết kế phép thử. ID2 chuyển giao quyết định, trạng thái hoặc phép thử đã chốt.
- AT_R v1.1 giữ đường dẫn cũ, phục hồi trạng thái trước khi nén, phân biệt file tải xuống, delta dạng văn bản và ghi repository. Mẫu CURRENT giữ 10 mục. Quy tắc thiết kế và chấm phép thử nằm trong nguồn kiểm chứng chung.
- AT_R phát dấu `[REVAMP → CODEX | AUDIT]` hoặc `[REVAMP → CODEX | IMPLEMENTATION]`. AGENTS gốc nhận diện nguồn gốc và loại việc. Quyền thao tác tiếp tục theo yêu cầu người dùng và bằng chứng tại đích.
- Bản tiền nhiệm được lưu nguyên byte: [CI v2.7](Source_Archive/Revamp_Project_System_CI_v2.7.md), [Router v2.0](Source_Archive/TASK_ROUTER_v2.0.yaml), [AT_R chưa đánh số](Source_Archive/AT_R_unversioned_pre_v1.1.md).
- Các probe v3.0 nằm trong [đặc tả kiểm thử](<Revamp Project System/tests/HANDOFF_ROUTE_TEST_CASES.md>). LIVE VERIFIED: NOT RUN.

## 2026-11-23 — CI v2.7: đọc History trước đề xuất cấu trúc hoặc điều khiển

- CI §4A và Router quy định đọc đầy đủ History trước nguồn đích khi Revamp hình thành, đánh giá hoặc lên kế hoạch cho thay đổi cấu trúc hay điều khiển đáng kể. Công việc phụ thuộc hệ thống còn lại giữ thứ tự nguồn trước History. CURRENT chỉ đọc nếu còn nhu cầu tiếp nối có ảnh hưởng.
- Router giữ v2.0 theo tiền lệ bổ sung preflight có điều kiện ở `9a21bf4`. Hai ID, trách nhiệm của CI và Router, cùng cách ly Central Hub được giữ nguyên.
- History §8B ghi lịch sử kỷ luật tiếng Việt và bài học từ lần Hub làm yếu chốt ngôn ngữ khi nén CI. §9.1 và skill bảo trì yêu cầu căn cứ riêng cho hợp đồng và từng chốt. Base semantics được giữ nguyên.
- [CI v2.6](Source_Archive/Revamp_Project_System_CI_v2.6.md) được lưu nguyên byte. SHA-256 `3544b5fffda86fed1daa4c00a698021c102a260d36f5a00c6512134715c82ea5`.

## 2026-11-11 — Cài skill Revamp vào Codex

- Theo yêu cầu riêng của người dùng, cài hai file của `codex-workflows/revamp-system-maintenance/` từ bản local đã commit `f111c83` vào `C:/Users/Sheeplark/.codex/skills/revamp-system-maintenance/`; bản cài khớp byte và validator đạt với `python -X utf8`.
- Skill có thể được chọn từ lượt tiếp theo. Việc cài file không chứng minh hành vi guard; CI v2.6 chưa được cài vào Project Instructions/chưa kiểm live. Các dòng “chưa cài skill” trong mục implementation trước là trạng thái tại thời điểm đó, đã được cập nhật bởi mốc này.

## 2026-11-11 — CI v2.6: tích hợp core, sửa nghĩa base

- Quyết định của tác giả: `base` là design source/lineage; invariant và core logic cần thiết phải hiện diện trực tiếp trong Revamp CI. v2.5 dùng `governs in full`/`supplement` và `Preserve base operation/stage` nhưng không chứa đầy đủ logic được tham chiếu. Đây là lỗi cấu trúc đã xác nhận; v2.6 thay thế v2.5, không chỉ đổi pin.
- USER-REPORTED RUNTIME FAILURE: từ khoảng v2.0, audit/exploration dễ trượt sang thiết kế sớm dù minimum sufficient change vẫn thường chạy; correction stage/intent giúp phần còn lại hoạt động đúng hơn. Chưa tái hiện độc lập. SUPPORTED CAUSAL MECHANISM: control giảm độ phức tạp phía sau có thể chạy trên operation/stage đã chọn sai vì core phía trước bị tham chiếu ra ngoài. Không kết luận đây là nguyên nhân duy nhất của regression.
- Metadata CI chỉ còn tên/version/status. §1 tích hợp grounding/discourse/epistemic, claim/dependency, verification/action state, updating/uncertainty, reader assumptions và explanation từ 9.1.1. §2 sở hữu operation/stage/transition/exploration/stopping và quyền hành động; §5 chỉ áp minimum sufficient change sau khi operation/stage đã được grounding đúng. Correction chỉ cập nhật premise/kết luận phụ thuộc, giữ scope không liên quan.
- Hai correction 9.1 và 9.1.1 nằm trực tiếp ở §1: compatible clarification/challenge không tự chứng minh prior error; không dựng negative alternative để phủ định khi contrast không có tác dụng cho lượt. Language override giữ quyền dùng ngôn ngữ người dùng yêu cầu. §3–§14 bảo toàn các trách nhiệm Revamp, có gộp/nén wording; giữ hai ID, AT_R, history/conditional CURRENT và Central Hub isolation. Không thêm loader/registry/runtime inheritance. TASK_ROUTER, AT_R và architecture preflight giữ nguyên byte.
- Tạo `codex-workflows/revamp-system-maintenance/SKILL.md` cùng `agents/openai.yaml`, theo convention hiện hành. Preflight xét semantic contract và dependency path, không xét keyword đơn thuần. Signal `HOLD UP: BASE SEMANTICS MISMATCH` chỉ cho đúng mismatch; ngắt phần phụ thuộc, chỉ sửa khi có quyền trong scope, không lan implementation sang project khác. Skill không là CI/runtime/authority; không thay ci-behavior-engineering hoặc project-git-workflow. Chưa cài skill vào môi trường người dùng.
- Cập nhật CURRENT, test path v2.5 → v2.6 và rationale Global đúng nơi active reference trở thành stale. Không đổi kỳ vọng 10 test hiện hành. v2.5 lưu byte-exact trong `Source_Archive/Revamp_Project_System_CI_v2.5.md`, SHA-256 `9fdfe19df25535641460d14ef47c4dba0707a2c189b4a181c5ead68ae5d4a320`. Global 9.0 không sửa/di chuyển; tác vụ không quyết định vòng đời dependency khác.

### Đối chiếu trách nhiệm tích hợp

| Nguồn thiết kế 9.1.1 / trách nhiệm | Vị trí 2.6 / xử lý |
| --- | --- |
| OUTPUT CONTRACT | §1 language override Revamp thay Vietnamese-only; plain language và depth giữ |
| CONTROL GROUNDING / DISCOURSE FIDELITY / EPISTEMIC NON-ESCALATION | §1; grounding trước chọn operation, compatible clarification/challenge không tự sửa claim |
| TURN AND STATE | §2; request → activity/stage → objective; chuyển theo signal, khám phá provisional, findings không mở việc, dừng |
| CLAIM STATE AND DEPENDENCY | §1; local premise khác fact, endorsement khác acknowledgment/conditional use, verification theo dependency/stakes/recency, action reports theo sự kiện |
| UPDATING AND UNCERTAINTY | §1–§2; premise và dependency đổi đúng phạm vi, operation ambiguity khác factual uncertainty, không dựng profile/fluency |
| EXPLANATION | §1; depth/counterexamples/coverage, tránh padding và negative alternative vô ích |
| Revamp-specific | §2–§14 và §4A; proposal-first, evidence classes, complexity/scope/verified behavior/personal premise/ontology/governance/governability/self-check/decision rule |

### Propagation scan chỉ đọc

Phạm vi là active CI, Router/deployment metadata và intent/architecture trực tiếp của từng project; không phải audit toàn bộ lore, archive, candidate hoặc mọi nhánh riêng. Repository xác nhận `Project Cosmic Core/README.md` đặt tên Project Cosmic Core (`C2`).

| File / thành phần | Nghĩa base hiện tại | Kết luận | Căn cứ |
| --- | --- | --- | --- |
| `Central Hub/HUB_CI_v1.2.md`, `HUB_ROUTER_v1.1.yaml` | Core nằm trực tiếp ở CI; Router nhận delegation chọn specialization | MATCH | CI chứa grounding/operation/claims/updating/explanation; Router phân rõ CI sở hữu global behavior, không tải Global CI |
| `Central Hub/HUB_ARCHITECTURE_v1.16.md` §5 (relations) | Base trong REFINES là trách nhiệm ngoài matched scope vẫn giữ; package có thể được đọc theo composition need riêng | MATCH | REFINES != REQUIRES, không autoload target; đây là quan hệ specialization của Hub, không external governing Global CI hay copy semantics Revamp |
| `Project Feather Core/Project Feather Core CI/FTH_CI_version_v3.4.md`, README | ChatGPT 8.9 base là lineage; core được tích hợp trực tiếp | MATCH | CI chứa kernel/operation/claim/update; Source gate cấm Router discover/select/load/infer/validate/confirm CI tại runtime |
| `Project Feather Core/Anti-Drift Source/FTH_Anti_Drift_Source_Router_v5.0.yaml` deployment | `upstream_base: 8.9` cùng CI tuple là metadata bảo trì | MATCH | Comment nói maintenance references only; runtime stages không có CI operation. Không đánh dấu lỗi từ chữ base hoặc đường dẫn archive trong metadata |
| `Project Cosmic Core/Project Cosmic Core CI/C2_CI_v1.0.md`, Router 1.0 JSON, README | Core tích hợp; Router chỉ chọn source/control dưới CI | MATCH | Source gate cấm runtime discover/select/load/infer/validate/confirm CI; deployment tuple không là runtime load |

Không tìm thấy cùng failure shape trong phạm vi active đã kiểm. Không suy điều này chứng minh các project đã cập nhật mọi correction Global mới, live installation đúng hoặc mọi candidate/nhánh khác đều không có lỗi. Không sửa Hub/FTH/C2.

### Kiểm chứng và giới hạn

- Bộ 10 test cấu trúc/contract hiện hành đạt trước và sau correction; chỉ đổi active filename trong test. Router YAML parse/conservative token và ID/authority boundaries vẫn được kiểm.
- CI 2.6: 8.000 ký tự gồm newline cuối; UTF-8 không BOM, LF, không trailing whitespace; archive predecessor khớp SHA-256. Skill validator đạt khi chạy Python `-X utf8` (lần đầu gặp UnicodeDecodeError do default Windows encoding); YAML metadata và diff đạt. Kết quả cuối ghi CURRENT.
- Review tĩnh đối chiếu full 9.1.1 và v2.5 xác nhận các trách nhiệm trên hiện diện trong artifact, không cần Global CI runtime. Bỏ metadata ngoài tên/version/status không làm mất control: không có metadata khác. Đây là kết luận review văn bản, không phải chứng minh model tuân thủ.
- `git diff --check` trong phạm vi sửa đạt. Kiểm toàn repository gặp `Filename too long` ở archive FTH ngoài scope; không sửa cấu hình/nguồn ngoài task để né lỗi. Checker trước archive trả PASS_SHARED; gọi checker với source đã nằm trong archive bị từ chối đúng bảo vệ, hash/layout được xác minh riêng.
- Thêm ca kiểm chứng manual S01–S10 trong đặc tả hiện có. Chưa chạy model/runtime, chưa cài Project Instructions hoặc skill; không dùng static pass làm live pass. Tác vụ chỉ cho local implementation/commit, không branch/tag/push/deploy.

## 2026-11-05 — CI v2.5: Task Router và hai Task ID

- Triển khai decision handoff được người dùng chốt: CI là authority duy nhất; Router chỉ chọn task/context. ID không tạo permission, acceptance hay chuyển stage.
- CI v2.5 thay v2.4, delta ở metadata/scope và §4A; §1–§4, §5–§14 giữ nguyên, kể cả Codex decision handoff và quyền commit local sau kiểm chứng. CI có 7.984 ký tự gồm newline cuối.
- TASK_ROUTER v2.0 thay HANDOFF_ROUTER v1.1; ID1 mặc định cho công việc Revamp trực tiếp, ID2 khi output chính là prompt/brief/handoff. Preflight repo/history và conditional CURRENT cũ giữ cho context phụ thuộc system/repository trong cả hai ID; task độc lập không bị buộc nạp repo/handoff.
- AT_R là contract tối thiểu, giữ mục tiêu/context cần thiết/settled constraints, tạo artifact tự đủ nghĩa; authoring không thực thi downstream. Không thêm composition, registry, schema, target inventory hoặc control vào Central Hub.
- CI v2.4 và Router v1.1 được lưu byte-exact trong Source_Archive chung. Đồng bộ current anchors/history, giữ 43 case đặc tả cũ, thêm 15 case task selection và 8 kiểm tra tự động cấu trúc/contract. Kết quả thực tế ghi trong CURRENT; không có kiểm chứng live hoặc deployment.

## 2026-11-01 — CI v2.4: chuyển quyết định sang Codex và promotion trực tiếp

- Người dùng duyệt promotion trực tiếp v2.4 ACTIVE; không tạo candidate stage. Governing base vẫn là ChatGPT Project Global Native 9.0.
- §2 coi yêu cầu prompt Codex là decision handoff: mang scope/quyết định đã chốt sang prompt, chỉ mở lại phần bị concrete blocker.
- §6 giữ exploration chưa chốt ở trạng thái provisional và thêm `CANDIDATE != REQUIRED STAGE`; baseline được người dùng duyệt có thể promote trực tiếp.
- §8 giữ đường known-correct khi thử bản thay thế, không dựng incumbent hoặc đường candidate giả cho kiến trúc mới.
- Chỉ thay đúng ba đoạn đã duyệt cùng version/ngày adoption; lưu v2.3 byte-exact trong `Source_Archive` và cập nhật CURRENT. v2.4 dài 7.978 ký tự gồm newline cuối; kiểm tra tĩnh A–F và định dạng đạt. LIVE VERIFIED: NOT RUN.

## 2026-10-29 — CI v2.3: chuyển governing base sang Global Native 9.0

Commit: `34e250c` — `Promote Revamp CI v2.3 to Global Native 9.0`.

- Chuyển base từ ChatGPT 8.9 sang ChatGPT Project Global Native 9.0; cập nhật version và ngày adoption.
- Giữ nguyên toàn bộ nội dung từ §1 đến cuối so với v2.2, gồm quyền stage/commit local, quy tắc tiền đề sai và handoff. Đây là thay đổi base được kế thừa; không phải bằng chứng hành vi tổng thể của hai base giống nhau.
- Lưu v2.2 byte-exact trong `Source_Archive`; cập nhật CURRENT cho v2.3 `ACTIVE`.
- Bằng chứng đã ghi trong CURRENT: 7.992 ký tự gồm newline cuối, đủ 14 section và §4A, kiểm tra UTF-8/LF/whitespace và đường dẫn đạt; live chưa chạy.

## 2026-10-28 — CI v2.2: quyền commit local và xử lý tiền đề sai

Commits: `c8a98d1` — sửa nội dung trên file v2.1 lúc đó; `7c20340` — tách thành v2.2 và bảo toàn v2.1 trước sửa.

- §2 cho phép implementation local đã được cấp quyền stage và commit thay đổi đúng phạm vi sau kiểm chứng. Branch, tag và push vẫn cần quyền riêng; audit/design/proposal không tự cấp quyền implementation.
- Thêm `FAILURE DETECTION != DEBUG AUTHORIZATION`: ngừng dùng đường phụ thuộc tiền đề không hợp lệ, giữ làm bằng chứng; tiếp tục từ trạng thái hiện hành đủ dùng khi an toàn, nếu không báo blocker.
- Bỏ câu quyền Git lặp ở §4A; rút phần ẩn dụ ở §14. Không thêm recovery framework.
- Phát hành v2.2 `ACTIVE`, tiếp tục dùng ChatGPT 8.9; archive giữ v2.1 trước đợt sửa, không phải bản trung gian đã sửa dưới tên v2.1.
- Bằng chứng đã ghi trong CURRENT: 7.985 ký tự, wording được duyệt xuất hiện đúng một lần, §5–§6 giữ nguyên, kiểm tra định dạng đạt; live chưa chạy.

## 2026-10-24 — Router v1.1: kiểm tra repository trước khôi phục trạng thái

Commit: `12a9a25` — `Promote Revamp handoff router v1.1 with repository preflight`.

- Thêm repository preflight: đọc nguồn hiện hành liên quan, đối chiếu quyết định đã chấp thuận và phần đã triển khai trước khi đề xuất; làm local phải dùng working tree hiện tại, kể cả dependency dirty có liên quan.
- Thứ tự đọc trở thành Router → nguồn repository hiện hành → history đầy đủ → CURRENT phù hợp → kiểm tra thêm file/runtime khi cần.
- Phân biệt điều đã đáp ứng, gap và conflict với source anchor; không trình bày lại giải pháp đã chấp thuận như ý tưởng mới. Thiếu chứng cứ thì hoãn kết luận phụ thuộc.
- Đánh số Router v1.1, lưu predecessor tại `Source_Archive/HANDOFF_ROUTER_pre_v1.1.yaml`; đồng bộ thứ tự trong history, CURRENT và đặc tả test. CI vẫn là v2.1; CI và template không đổi.
- CURRENT ghi YAML parse và kiểm tra cấu trúc đạt; thêm 4 tình huống repository preflight. Đây là đặc tả/review, không phải kết quả chạy live.

## 2026-10-24 — bổ sung historical preflight

Commit: `8ca2b6b` — `Integrate Revamp historical preflight before CURRENT recovery`.

- Thêm `HISTORY_AND_WHAT_NOT_TO_DO.md` và yêu cầu đọc đầy đủ trước khôi phục CURRENT trong công việc Revamp substantive.
- Ghi bối cảnh lỗi lịch sử, giới hạn chống mở rộng kiến trúc và ranh giới `HISTORY != CURRENT STATE`, `PAST FAILURE != PRESENT FAILURE`.
- Cập nhật Router, CURRENT và đặc tả test; không đổi version CI. Bước repository preflight được bổ sung ở commit tiếp theo cùng ngày.

## 2026-10-18 — CI v2.1: ACTIVE và handoff theo workstream

Commit: `2fed113` — `Promote Revamp CI v2.1 and add workstream handoff controls`.

- Chuyển từ v2.0 `PROPOSAL` sang v2.1 `ACTIVE` theo adoption; tiếp tục governing base ChatGPT 8.9.
- Thêm §4A `CROSS-CHAT HANDOFF`: chọn nguồn liên quan, đọc `FULL_FILE`, giữ trạng thái các workstream riêng; handoff không tự chứng minh trạng thái thực tế, acceptance hoặc authorization.
- Tạo Router, template, CURRENT đầu tiên và đặc tả route test. Cập nhật CURRENT khi có thay đổi đáng kể trong phạm vi được phép, không theo từng tin nhắn.
- Rút gọn wording để giữ giới hạn CI 8.000 ký tự; giữ 14 section gốc và các nguyên tắc evidence, minimum sufficient change, YAML default.
- Giới hạn cơ chế cho Revamp; Central Hub không kế thừa CI handoff, Router, CURRENT hay hành vi nạp này. Archive v2.0 byte-exact.
- CURRENT ghi kiểm tra cấu trúc đạt, gồm 18 tình huống route và 6 tình huống template trong đặc tả; không phải 24 lần chạy hành vi. Live chưa chạy.

## 2026-10-12 — CI v2.0: governing base ChatGPT 8.9

Commit: `68386b1` — `Add Revamp Project System CI v2.0`.

- Thêm v2.0 vào `Project CI`, trạng thái trong file là `PROPOSAL`.
- So với v1.1 được lưu, đổi version và governing-base references từ ChatGPT 8.9 temp sang ChatGPT 8.9; các quy tắc còn lại giữ nguyên.
- Giữ mô hình supplement kế thừa toàn bộ base, language override và YAML default.

## 2026-10-13 — khôi phục lineage vào archive

Commit: `40663bb` — `recover(project-ci): preserve current archive lineage`.

- Khôi phục bản Revamp không đánh số, v1.0 và v1.1 vào `Project CI/Source_Archive`, cùng một số artifact CI lịch sử khác.
- Đây là mốc bảo toàn lịch sử trong Git, không phải đợt phát hành hay bằng chứng các bản được tạo ngày 2026-10-13. Thứ tự mục changelog ưu tiên dòng phiên bản; mốc khôi phục này xảy ra sau commit thêm v2.0.

## v1.1 và v1.0 — các bản đề xuất lịch sử

Nguồn: các file lưu trong `Source_Archive`, được nhập tại `40663bb`. Chưa xác lập ngày tạo/adoption riêng từ các nguồn đã kiểm tra.

- **v1.1 so với v1.0:** thêm YAML default ở §5 cho Router/manifest/index/registry và machine config; dùng YAML bảo thủ, tránh anchor/alias, merge key, custom tag và cú pháp phụ thuộc parser. Không ép đổi prose hoặc live config chỉ để đồng nhất; không tạo schema/validator mới nếu thiếu lỗi cụ thể.
- **v1.0 so với bản không đánh số:** chuyển base từ ChatGPT 8.7 sang ChatGPT 8.9 temp với yêu cầu kế thừa đầy đủ; khai báo language override; làm rõ repository access chỉ cho inspection, target mặc định local và quyền branch/tag/commit/push tách riêng.
- Cả hai file đều khai báo `PROPOSAL`; việc có mặt trong archive không chứng minh từng được kích hoạt.

## 2026-09-30 — bản Revamp không đánh số, dựa trên ChatGPT 8.7

Commit: `568d42d` — `Add Project System CI revamp`.

- Thêm `Revamp Project System CI.md` với trạng thái `PROPOSAL`.
- Thiết lập 14 section: bảo toàn tác vụ/giai đoạn, đánh giá đề xuất người dùng trước, kiểm tra hệ thống thực tế, sửa đổi đủ dùng, tăng độ phức tạp theo bằng chứng, giữ phạm vi và hành vi đã kiểm chứng, tách kiến trúc lưu trữ khỏi ontology, tránh recursive governance.
- Phân biệt `OBSERVED FAILURE`, `REPRODUCED FAILURE`, `SUPPORTED RISK`, `HYPOTHETICAL FUTURE RISK`; cho phép exploration được yêu cầu nhưng không tự nâng proposal thành baseline.
- File hiện được bảo toàn tại `Source_Archive/Revamp Project System CI.md`. Ngày trên là ngày commit, không khẳng định ngày khởi thảo hoặc live adoption.

## Nguồn và giới hạn kiểm chứng

- Đối chiếu nội dung CI hiện hành, Router, history, CURRENT, các bản Revamp lưu và commit/diff liên quan trong Git local. Không suy trạng thái remote từ lịch sử local.
- Các kết quả kiểm tra tĩnh lịch sử ở trên là bằng chứng đã được CURRENT ghi nhận; tác vụ viết changelog không chạy lại toàn bộ kiểm tra cũ hay thử nghiệm live.
- Changelog không thay đổi CI, Router, CURRENT, artifact lưu hoặc trạng thái deployment; không tạo version CI mới.
