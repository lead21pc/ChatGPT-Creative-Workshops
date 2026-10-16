# FTH Anti-Drift Control Vocabulary Glossary v1.0

> Role: MAINTENANCE / INTERPRETATION REFERENCE.
> Use: control authoring, review, translation, and terminology calibration.
> Not: CANON, CURRENT_SOURCE, anti-drift overlay, Source Router, CI, runtime authority, ontology, schema, or validator.

```text
GLOSSARY SUMMARIZES ESTABLISHED CONTROL USAGE.
IT DOES NOT CREATE MEANING BY ITSELF.
```

## 1. Reading And Maintenance Boundary

The active CI, Router, and applicable specialized owner retain their established authority. If this summary conflicts with one of them, follow the controlling source and correct the glossary; do not change the owner to fit the glossary. Runtime invariants remain in their owning controls. This document is not a default read, MODULE_REQUIRES target, Router gate, or deployment instruction.

Entries describe material distinctions, not mutually exclusive categories, mandatory fields, a status enum, or a temporal pipeline. In these controls, `A != B` protects against automatic equivalence or implication; it does not prohibit an evidenced relationship or co-location. Preserve valid context-specific meanings rather than force one universal definition. Unspecified meaning stays unspecified; this reference supplies no missing lore or authority.

Owner abbreviations and section numbers below refer to the inspected versions in Section 7. They are maintenance pointers, not a permanent version selector. If an owner is superseded, review its current usage and update this reference; a glossary link never reactivates the predecessor.

## 2. Authority And Action

| Term / Vietnamese mapping | Established usage and material reading risk | Scope / owner |
| --- | --- | --- |
| **Power / capability**: quyền lực or sức mạnh / năng lực | Causal power or ability is distinct from authorization, institutional capacity, present availability, and success. Do not turn a powerful or capable actor into the rightful decision-maker, or treat possession as timely, deployable, sustainable use. | CI: Relations and simulation; MCA 12; TW 6,11,16; Mortality 3 |
| **Authority / mandate**: thẩm quyền / nhiệm vụ hoặc thẩm quyền được giao | In-world authority concerns the established right to authorize or decide within scope; mandate concerns the assigned remit. Neither expertise nor responsibility for a problem establishes every information, decision, or execution function. Mandate alone does not establish final decision rights; those rights do not prove a decision occurred. | MCA 12; TW 4,11; WIL 6-7 |
| **Permission / jurisdiction**: sự cho phép / phạm vi thẩm quyền | Permission to perform an action and the domain in which authority applies are different questions. Access, ability, a mandate, or authorization elsewhere does not answer both. Do not import a universal legal hierarchy from these words. | CI: Relations and simulation; WIL 9; TW 11 |
| **Legitimacy**: tính chính danh; basis of accepted authority | Explains supported acceptance or tolerance of authority; it is not morality, consensus, command, or unlimited capacity. Cultural recognition may matter without proving legal authorization, obedience, or resources. | WIL 7; Belief 6; Actor 3 |
| **Access**: khả năng hoặc quyền tiếp cận | An established path or condition for reaching information, resources, a place, or an interface. Physical availability, permission, receipt, knowledge, understanding, and authority are not interchangeable. Name the object and relevant sense; do not assume an access-control entitlement. | MCA 11-12; WIL 5,9; Actor 2,4-5; TW 7,10-11 |
| **Control / influence**: kiểm soát / ảnh hưởng | Read the actual supported relation: governing, constraining, affecting, using, or controlling a flow are not one edge. Influence or pressure does not itself establish command, ownership, or a determined outcome. In "control layer," control means scoped reasoning governance, not an in-world controller or an implied feedback system. | CI: Subordinate controls; MCA 4,10,12-13; WIL 9 |
| **Ownership / owner**: sở hữu; nguồn phụ trách; phần sửa thuộc tác vụ | Source ownership identifies the controlling document/domain, not in-world property, command, or actor knowledge. Architectural ownership needs its own relation; document location and genealogy do not prove it. Workflow ownership of a change set is a Git work boundary, not canon admission. Do not import software-component ownership or property rights across these senses. | CI: Source gate; Router 3,6; MCA 3-6,13; Actor 2; Workflow |

## 3. Information And Reception

| Term / Vietnamese mapping | Established usage and material reading risk | Scope / owner |
| --- | --- | --- |
| **Information / knowledge / understanding**: thông tin / điều actor biết / sự hiểu | Available or received content, what an actor knows, and what it understands remain distinct. Source or simulation knowledge is not actor knowledge. Observation does not establish understanding, mandate, action feasibility, or success; use an evidenced access path and task-relevant timing. | MCA 11-12; Actor 2,4-5; TW 10; Mortality 12 |
| **Belief**: điều actor tin; niềm tin | Actor-level conviction can differ from emotion, preference, outward conduct, or the truth of the claim. Belief / Culture distinguishes conviction from doctrine, practice, norm, identity, and institution at the evidenced cultural scope; it delegates actor-specific inference to Actor Reception. These are compatible levels, not competing truth authorities or two required belief variables. | Actor 3,7; Belief 1-3 |
| **Acceptance**: sự chấp nhận, with the subject stated | Actor reception distinguishes believing, accepting, complying, and enforcement. CI canon acceptance is a scoped author decision, not an actor attitude. Workflow acceptance of a patch or review result is not either of those. Never transfer approval between subjects, objects, or operations. | Actor 4; CI: Turn and canon; Review; Workflow |
| **Appraisal**: cách actor đánh giá một tín hiệu hoặc tình huống | Task-relevant evaluations may coexist with belief, incentives, priors, and competing signals. Correct semantic understanding or belief need not collapse the actor's evaluation into one attitude. Familiarity may matter only through supported priors/experience; no direction, urgency score, complete psychology, or automatic desensitization is implied. | Actor 1,3-4,7-8; MCA 11 |
| **Public position / private intent / action**: lập trường công khai / ý định riêng / hành động | Public support or compliance does not prove private agreement; intent is not action or completed execution. Private states need evidence or a labeled premise. Do not infer a collective private mind or choose the downstream action from a reception label. | Actor 2-3,8; Mortality 9; TW 5,11 |
| **Source authority / in-world authority**: thẩm quyền của nguồn / thẩm quyền trong thế giới | The first determines which source controls a claim; the second belongs to evidenced fictional actors and institutions. Router resolution does not tell actors who owns a rule, grant them information, or make that rule binding. Connector access is neither kind of authority. | Router 6,6A; Actor 2; MCA 12 |

## 4. Architecture And Relations

| Term / Vietnamese mapping | Established usage and material reading risk | Scope / owner |
| --- | --- | --- |
| **Module**: đơn vị có phạm vi xác định, with context stated | MCA allows engines, concepts, institutions, actor groups, interfaces, and other bounded domains. Router modules are admitted scoped source units with a reviewed header contract; legacy unheadered sources are not fabricated modules. An overlay is not a lore module. Do not import code compilation, encapsulation, parent ownership, or automatic coupling from software usage. | MCA 3; Router 2-3; Actor 2 |
| **Engine / host**: cơ chế / môi trường hoặc cấu hình vận hành | MCA separates mechanism, operating environment, established lore implementation, and story trajectory analytically, unless the source establishes another model. These are not mandatory canon entities, executable programs, deployment hosts, or a universal engine template. | MCA 8-10 |
| **Interface / contract / implementation**: giao diện hoặc điểm nối / điều kiện tương tác / cách thực hiện | A task-material crossing or shared workflow can be coherent without identical internals. Shared contract is not shared subsystem, ontology, or implementation. "Interface" does not require an API, exhaustive economic model, or a standardized software protocol. Check only conditions that can change the task. | MCA 7; WIL 9; Economy 3-5,11; TW 4,7 |
| **Interaction / co-occurrence / containment / composition**: tương tác / đồng hiện / quan hệ chứa / kết hợp trong một cấu hình | Interaction is not containment; co-occurrence is not dependency. Configured composition establishes that interaction only, not permanent ownership, shared ontology, hierarchy, or universal compatibility. Document order and folder containment establish none of these world relations. | CI: Relations and simulation, Source gate; MCA 1,3-6 |
| **Dependency**: phụ thuộc, with the graph and task stated | A causal or simulation prerequisite is not obedience or ownership. Router MODULE_REQUIRES and NODE_REQUIRES are reviewed decisive prerequisites for specified tasks/closures, not inferred mentions or compilation imports. Overlay prerequisites govern scoped reasoning, not lore edges. Workflow tool dependencies are another scope. | Router 3-5,7; MCA 4-5; WIL 9 |
| **Graph / typed relation**: mạng quan hệ / quan hệ có loại xác định | Ontology, simulation requirements, operational use, causality, authority, information, narrative provenance, and design genealogy can describe the same entities differently. A relation in one graph needs an established bridge before reuse in another. This is reasoning discipline, not a required graph database or whole-project model. | MCA 4-5,19; CI: Relations and simulation |
| **Genealogy / derivation / provenance**: lịch sử hình thành / bắt nguồn từ / căn cứ và đường truy nguồn | Genealogy or DERIVED_FROM explains origin without proving current hierarchy, containment, control, or runtime need. Source provenance supports tracing claims/decisions; operational information provenance concerns an actor's path, timing, and reliability. Neither automatically establishes current authority or canon. | MCA 13; Router 6; TW 10; Audit notes |

## 5. Source And Evidence Status

| Term / Vietnamese mapping | Established usage and material reading risk | Scope / owner |
| --- | --- | --- |
| **Canon / current canon / current source**: canon / canon hiện hành / nguồn hiện hành | Current canon is accepted world content within its supported scope. A current-source declaration is a role claim checked against identity, admission, owners, package status, and author decisions; it is not self-proving canon. File presence, compatibility, recency, and a valid header do not grant admission. "Current" must name what is current, not universally promote every nearby claim. | CI: Turn and canon, Source gate; Router 2-3,6 |
| **Runtime / runtime role**: vận hành thực tế / vai trò khai báo khi sử dụng nguồn | Runtime may refer to live ChatGPT Project behavior or an MCA configured run; it does not automatically mean executable software. Router Runtime role is a source-header declaration, not self-granted truth authority. Repository versions, readable files, commits, and checks do not prove live installation, retrieval, or behavior. | Router header,3,5; MCA 6; Context 7,11-12 |
| **Accepted / admitted / confirmed / established**: được chấp nhận / được đưa vào phạm vi hợp lệ / được xác nhận / đã có căn cứ xác lập | State who accepted or confirmed what, in which scope. Canon acceptance belongs to the author; module admission checks role/identity/ownership against package and explicit decisions; an established relation or premise needs its stated support. These words are not a four-step lifecycle or universal synonyms. Accepted one premise does not accept its imagined dependencies; plausible or compatible is not confirmed. | CI: Turn and canon; Router 3,6; MCA 14,18; WIL 1,18 |
| **Unconfirmed / unknown / deferred / conflicted**: chưa xác nhận / chưa biết hoặc chưa xác lập / hoãn xem xét / có xung đột chưa giải quyết | Unconfirmed input has not gained controlling status; unknown does not prove absence; deferred is not resolved. Conflict requires incompatible controlling claims at the same material scope/conditions, not overlap, doctrine/practice differences, or unresolved intent alone. Labels can overlap; no new enum is imposed. | CI: Turn and canon; Router 6,8; MCA 14-15; Belief 2 |
| **Historical / design history / superseded / retired**: lịch sử / lịch sử thiết kế / đã được thay thế / đã ngừng dùng | Provenance or explicitly requested comparison, not a current baseline or fallback. Archive location, failed retrieval, and current silence do not revive them. A retired test case is a tooling lifecycle state, not a claim that its subject ceased to exist in-world. | CI: Turn and canon; Router 6; Archive; Regression |
| **Inference / hypothetical / proposal**: suy luận / giả định hoặc nhánh giả định / đề xuất | Keep derived claims, conditional premises/branches, and suggested changes distinguishable from sourced facts and canon. Requested design may exceed canon with labels; simulated success does not accept the design. A question or example grants no mutation authority. | CI: Evidence and explanation, Relations and simulation; Router 6; WIL 18; TW 24 |
| **PASS / BLOCKED / LIMITED_CHECK / DRAFT**: đạt phép kiểm đã nêu / bị chặn / kiểm tra giới hạn / ca dự thảo | Workflow and runner labels describe their own check, evidence limit, or case lifecycle, not canon status. Structural PASS does not prove runtime behavior; DRAFT is not an active acceptance gate. Router SOURCE_LOAD_BLOCKED/PARTIAL and overlay branch/block decisions retain their own contracts, not a shared status scale. | Regression; Behavior; Router 5,8; TW 15,26 |

## 6. Design And Simulation

| Term / Vietnamese mapping | Established usage and material reading risk | Scope / owner |
| --- | --- | --- |
| **Design / audit / simulation**: thiết kế / đối chiếu và đánh giá / mô phỏng | Design offers labeled unaccepted options; audit identifies material gaps without silently redesigning; simulation tests established or authorized premises without canonizing the result. Workflow implementation/approval authorizes only its stated task, not these other operations or live deployment. | CI: Relations and simulation; WIL 17-18; Belief 7; Behavior; Workflow |
| **Branch / trajectory / outcome / world state**: nhánh / diễn tiến / kết quả / trạng thái thế giới | A branch is conditional; a mechanism changes conditions, not the chosen endpoint. A possible trajectory is not a canon outcome; a proposed snapshot is not current world state. Preserve agency and persistent consequences rather than reverse-engineer a guaranteed save, death, or escalation. A simulation branch is not a Git branch. | MCA 9-10,16,18; WIL 18; Mortality 2,6,10,13; TW 9,19,23-24; Git workflow |
| **Causal path / causal closure / black box**: đường nhân quả / đủ căn cứ nhân quả cho tác vụ / cơ chế tạm giữ kín | Closure means sufficient task-local support for a valid conclusion, conditional branch, or named block, not accounting completeness or a globally closed world. Black boxing preserves the supported interface and material unknowns, not omnipotence or flattened ontology. Open decisive hidden links only. Router VERIFIED_MODULE_CLOSURE instead concerns actually loaded reviewed evidence; reasoning closure cannot substitute for it. | MCA 19; WIL 12,19; Economy 1,3-5,9; TW 25; Router 5 |
| **Failure / vulnerability / controlled loophole / intentional imperfection**: thất bại / điểm dễ bị khai thác / kẽ hở có kiểm soát / sự bất toàn có chủ đích | An imperfect surface is not automatically a design defect or repair mandate. Distinguish supported unintended failure, tolerated cost, deliberate exposure, incentive, surveillance/extraction function, trade-off, and unknown intent only when material. Plausible benefit is not confirmed intent; authorial intent is not actor knowledge or guaranteed containment. Preserve evidenced boundaries/spillover without treating every exploit as tolerated or every flaw as intentional. | WIL 14; MCA 15; Economy 14; Mortality 11; TW 20-21 |

### Translation-Sensitive Reading

Vietnamese mappings above are contextual aids, not locked one-to-one replacements. English prose retains owner identifiers; local Vietnamese text should name the specific relation rather than collapse it into **"quyền"**. That word may mean authority, permission, a sourced right, power, or mandate; **"quyền tiếp cận"** may describe an entitlement while **"khả năng tiếp cận"** describes feasibility. Determine the established scope before choosing either. This glossary creates no right or authority.

Similarly, **"biết"** is not automatically understanding, belief, or official receipt; **"chấp nhận"** needs its subject and object; **"phụ trách"** does not grant every competence function; **"nguồn"** may mean a controlling document, an actor's information channel, or a resource origin. Do not translate **"hiện hành"** into automatic canon acceptance or live deployment.

## 7. Inspected Owners And Deliberate Omissions

The audit found distributed, compatible distinctions rather than an incompatible shared definition requiring a control patch. The material risks are cross-scope substitution and imported technical defaults. This reference adds no runtime invariant or regression gate.

| Abbreviation | Inspected owner / scope |
| --- | --- |
| CI | [FTH CI 3.4](../Project%20Feather%20Core%20CI/FTH_CI_version_v3.4.md): operations, canon decisions, evidence and relation boundaries. |
| Router | [Source Router 5.0](FTH_Anti_Drift_Source_Router_v5.0.yaml): source roles, admission, loading, reconciliation, and overlay gates. |
| MCA | [Modular Concept Architecture 1.2](FTH_Anti_Drift_Modular_Concept_Architecture_v1.2.md): architectural relations, function allocation, actor information/agency, and conditional response lifecycle. |
| WIL | [Worldbuilding Internal Logic 1.2](FTH_Anti_Drift_Worldbuilding_Internal_Logic_v1.2.md): bounded coherence/design reasoning and imperfection intent. |
| Actor | [Actor Reception Normative Signals 1.0](FTH_Anti_Drift_Actor_Reception_Normative_Signals_v1.0.md): actor-specific reception and appraisals. |
| Belief | [Belief / Culture 1.0](FTH_Anti_Drift_Belief_Culture_v1.0.md): cultural claim distinctions, extent, transmission, and recognition. |
| Economy | [Interface Economy / State Stabilization 1.1](FTH_Anti_Drift_Interface_Economy_State_Stabilization_v1.1.md): economic interface depth, intervention, and stopping. |
| Mortality | [Mortality / Relationship / Plot Immunity 1.1](FTH_Anti_Drift_Mortality_Relationship_Plot_Immunity_v1.1.md): symmetric causal resolution and survival-path evidence. |
| TW | [Total War RP 1.1](FTH_Anti_Drift_Total_War_RP_v1.1.md): bounded operational transitions, availability, and persistent loss. |
| Context | [SYSTEM_CONTEXT](../../SYSTEM_CONTEXT.md): authoring, repository, and live-runtime boundaries. |
| Workflow | Milestone Executor: bounded edits and authorization. |
| Review | Review Before Merge: read-only acceptance assessment, not automatic fixes or canon approval. |
| Behavior | CI Behavior Engineering: observed failure versus wording risk and structural versus behavioral checks. |
| Archive | Artifact Source Archive: byte-preserving retirement, not canon admission. |
| Git workflow | [Project Git Workflow](../../codex-workflows/project-git-workflow/SKILL.md): stable chat/checkout/branch binding and scoped commits, distinct from simulation branches. |
| Audit notes | Repository audit protocol and package workflow, inspected as terminology evidence only; not invoked or made prerequisites. |
| Regression | [Control regression documentation](../tests/control-regressions/README.md): tooling lifecycle, advisory results, and execution limits; dated baseline notes do not select active controls. |

Also checked Systematic Debugging and CI Language Calibration: supported diagnosis and contextual explanation, not technical-standard normalization or a compulsory dictionary in every response.

Deliberately omitted: lore names and legal/status taxonomies (current lore owns them); ordinary actor/event/time/result/system definitions (no material collision found); standalone headroom metrics, intent scores, power scores, or exhaustive permission matrices (not established shared models). Specialized operational labels remain with their owner. The grouped entries are a selective maintenance aid, not a complete list of valid concepts or required source fields.
