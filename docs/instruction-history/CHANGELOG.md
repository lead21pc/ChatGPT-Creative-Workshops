# Changelog

## v1.0

### Added

- Real-time hardware verification with missing-data disclosure.
- Three-part launch/existence validation using manufacturer data, physical identifiers, and an independent source.
- Raw specification extraction and side-by-side conflict reporting.
- Empirical Auditor role, command triggers, format precedence, exhaustive mode, and Vietnamese-only output.
- Three-source validation for important medical, legal, and technical claims.

## v2.0

### Added

- Senior Editor role with concise Vietnamese answers, short terminology definitions, and conclusion-first structure.
- Failure Scan and Expansion Options sections.
- Direct, natural, non-academic style rules.

### Changed

- Replaced the specialized empirical hardware protocol with a general compact editorial protocol.

### Removed

- Real-time hardware validation, raw-only extraction, command triggers, exhaustive output, and fixed source-count requirements.

## v2.1

### Patched

- Made conclusion-first behavior conditional on sufficient evidence.
- Made headings, lists, and Markdown conditional on readability.
- Added repetition limits, low-information reaction suppression, and terminology-precision exceptions.

### Changed

- Shifted from casual personality toward natural, dense, accuracy-first prose.

## v2.2

### Patched

- Compressed the v2 style rules.
- Added explicit fact, inference, and assumption separation.

### Changed

- Replaced detailed formatting instructions with general clarity and information-density constraints.

### Removed

- Fixed output anchor, simplification disclosure, everyday-example rule, and transition-pattern cap.

## v3.0

### Added

- Adversarial review of assumptions, contradictions, hidden costs, bias, and overengineering.
- Direct pragmatic-engineer style and explicit strength/weakness/uncertainty/trade-off separation.
- Clarification questions for unclear goals, constraints, and success criteria.

### Changed

- Replaced the Senior Editor and fixed output modules with a global critical-review architecture.

### Removed

- Sentence caps, Failure Scan, Expansion Options, and conclusion-first formatting.

## v3.1

### Patched

- Added Hybrid Architecture Reviewer + Pragmatic Engineer behavior.
- Added correctness, risk reduction, ROI, impact/likelihood ranking, and now/later/never prioritization.
- Limited clarification to missing information that could materially change the conclusion.
- Prevented unsolicited user summaries.

## v4.0

### Changed

- Limited assumption-challenging and hidden-cost analysis to material effects on a decision, conclusion, plan, or recommendation.
- Changed the role from Architecture Reviewer to Architecture Advisor + Reviewer.

## v5.0

### Added

- Evidence-first reasoning with observation, inference, assumption, and conclusion separation.
- Conditional alternatives for unresolved interpretations.
- Inform, Evaluate, and Audit response modes.
- Technical mechanism/trade-off/failure-mode handling and non-technical inference limits.
- Domain-matched style and time-sensitive verification.

### Changed

- Replaced global critical review with task-dependent response routing.
- Replaced rigid reviewer prose with natural information-dense output.

### Removed

- Hybrid Advisor persona, fixed ROI/risk ranking, and global harsh-critique behavior.

## v5.1

### Patched

- Added task scope and applicable truth scope.
- Made explicit user-defined model premises authoritative inside that model unless external evaluation is requested.
- Added conditional MECE analysis.

### Removed

- Explicit answer-first, topic-drift, and time-sensitive-verification rules.

## v6.0

### Added

- Second-brain objective focused on reasoning robustness.
- Exactly-one-mode routing with Inform/Evaluate/Audit defaults.
- Falsifying conditions for interpretations and non-trivial conclusions.
- Sentence-value and conditional-structure constraints.
- Initial Vietnamese personal-pronoun reduction rule.

### Changed

- Broadened scoped premise authority into a general stated-premise rule.

## v6.1

### Patched

- Distinguished objective claims from opinions and first-person observations.
- Added independent-chat context isolation.
- Selected response mode from the current message.
- Replaced pronoun deletion with subject-centered Vietnamese sentence construction.

### Fixed

- Removed the v6.0 conflict between independent-evidence agreement and blanket acceptance of stated premises.

### Removed

- Explicit non-trivial-conclusion falsifier, MECE, domain-style, and structure-threshold rules.

## v6.2

### Patched

- Added Vietnamese-first terminology with an exception when no real Vietnamese equivalent exists.

### Removed

- Explicit technical/non-technical handling sentence.

## v7.0

### Added

- Expanded operational definitions for claims, opinions, context, modes, epistemic states, ambiguity, and falsifiability.
- Restored technical/non-technical handling, non-trivial falsifiability, and conditional structure.
- Expanded Vietnamese subject and terminology rules.

### Changed

- Inform forbids evaluative framing and recommendations.
- Audit defaults to existing decisions and objective claims.

## v7.1

### Patched

- Moved Vietnamese subject and terminology rules to the top.
- Required Vietnamese terms whenever a Vietnamese word exists, including headings and lists.
- Added evidence-based conclusion updates and propagation of corrected premises.
- Added mandatory search for plausibly time-sensitive facts.

## v7.2

### Patched

- Allowed established English terms when a Vietnamese translation would mislead or be unnaturally translated.
- Added explicit preservation and case-by-case testing of plausible causes.
- Added domain-matched output for ordinary chat, technical discussion, worldbuilding, and fiction.

### Fixed

- Protected terminology accuracy and naturalness from v7.1’s over-broad translation requirement.

## v7.3

### Patched

- Reorganized evidence, updating, epistemic state, response mode, ambiguity, freshness, context, and style into named modules.
- Declared subject-centered Vietnamese the primary invariant and terminology the supporting invariant.
- Made remaining rules context-sensitive guardrails and placed correctness above style.
- Prevented a claim alone from forcing Audit mode.
- Allowed the smallest reasonable assumption when ambiguity is immaterial.
- Required verification before using externally checkable product/runtime capabilities, limits, versions, prices, policies, or current behavior as premises.
- Preferred provider documentation or direct product state for product claims and prohibited inferring unstated capability from adjacent features or plausible architecture.

### Changed

- Changed freshness from mandatory search to verification when recency could affect the answer.
- Scoped epistemic-state display and falsifying conditions to cases where they matter.
- Allowed limited judgment in Inform when needed.

## v7.3.1

### Patched

- Normalized end-of-file formatting by removing the final newline.

### Changed

- No CI semantic, rule, precedence, or architectural behavior changed from v7.3.

## v7.4

### Added

- Added an explicit `role → mode → reasoning → stance` pipeline so the role of a claim selects the response mode before reasoning determines agreement, qualification, uncertainty, or disagreement.
- Added a separate truth scope for user-defined frameworks, architectures, fictional systems, and conceptual models.
- Expanded technical discussion to require mechanisms, causal links, assumptions, trade-offs, failure modes, useful quantitative evidence, and conditions under which important conclusions stop holding.
- Expanded the current-information rule and retained the prohibition on inferring capabilities or limits from adjacent features when direct verification is needed.
- Allowed analogies, technical metaphors, dry humor, and irony when natural and useful.

### Changed

- Merged subject structure and terminology into one language module while preserving subject-centered Vietnamese as the default construction.
- Reframed claim handling around the claim's role in the current request; a claim still does not force Audit mode.
- Expanded Evaluate and Audit while keeping one primary response mode selected from the actual ask.
- Made epistemic-state separation conditional on whether correctness or decisions are affected.

### Removed

- Removed the explicit post-hoc pronoun-deletion guard and the named primary/supporting invariant hierarchy.
- Removed the explicit rule that conclusions change only with new facts, sources, or reasoning and that premise changes must propagate.
- Removed explicit cross-chat context isolation.
- Removed the provider-documentation/direct-product-state preference while retaining direct verification requirements.

### Fixed / Regression Protection

- Preserved correctness over style, viable alternatives when useful, and the rule that the presence of a claim alone does not select Audit.

## v7.4.1

### Added

- Added an explicit ban on unnecessary English jargon and mid-sentence code-switching when Vietnamese carries the same meaning.
- Required specialized jargon to have no equally clear ordinary Vietnamese wording, be defined in plain Vietnamese on first use, and never require external lookup to understand the answer.

### Changed

- Split v7.4's merged language module back into the v7.3 subject-structure and terminology invariants.
- Made the terminology rule the single authority for Vietnamese, English exceptions, jargon, and code-switching.
- Limited `TECHNICAL / NON-TECHNICAL` to technical reasoning depth, quantitative evidence, and unsupported personal inference.
- Retained v7.4's `role → mode → reasoning → stance` routing, expanded technical analysis, current-information coverage, and user-defined-system truth scope in a denser form.

### Restored / Regression Protection

- Restored the post-hoc pronoun-deletion guard and the full Vietnamese-first terminology constraints from v7.3.
- Restored explicit objective-claim and product/runtime verification, including provider/direct-state preference and protection against inference from adjacent or partial evidence.
- Restored evidence-based conclusion updates, premise propagation, explicit epistemic-state protection, general conclusion-change conditions, Inform's judgment boundary, Audit-before-optimization, and the invariant/guardrail priority hierarchy.

### Removed / Intentional Omissions

- Removed v7.4's complete `STYLE` module so presentation preferences cannot consume budget or outrank behavioral guarantees.
- Did not restore v7.3's `CONTEXT` rule because ChatGPT memory cannot enforce strict chat isolation consistently; no false isolation guarantee is claimed.

## v6.3 converted

### Added

- Rollback-safe Free/Go Major distilled from v7.3 so a plan downgrade does not restore v6.2 semantics.

### Changed

- Compressed subject structure, terminology, evidence, updating, epistemic state, response modes, ambiguity, depth, and domain style into five rule blocks.
- Allowed English when clearly more recognizable or precise, while rejecting common use alone as sufficient justification.

### Deployment trade-offs

- Omitted explicit freshness, context-isolation, technical/non-technical, jargon, discriminator/falsifier, and correctness-over-style rules to meet the narrower character budget.

### Fixed / Regression Protection

- Preserved the post-hoc pronoun guard, evidence-based conclusion updates, viable alternatives, and claim-not-forcing-Audit behavior in the converted major.

## v6.4

### Added

- Added a 1,500-character Free/Go distillation of v7.4.1 with five compact behavioral blocks.
- Added explicit protection against unnecessary code-switching, unexplained jargon, unsupported personal inference, and product/runtime extrapolation.

### Changed

- Preserved evidence, updating, epistemic separation, mode routing, ambiguity handling, and user-defined-system scope under the smaller deployment budget.
- Compressed examples and labels before behavioral constraints; retained CRLF and the 1,500-character limit.

## v7.4.2

### Fixed / Regression Protection

- Restored a general depth floor across technical and non-technical domains after the v7.4.1 wording regression.
- Required non-trivial reasoning to remain inspectable and prohibited collapsing supported conclusions into bare answers.
- Defined correctness as including sufficient explanation, without restoring the removed `STYLE` or `CONTEXT` modules.

### Changed

- Kept the v7.3 language core and v7.4.1 evidence/routing improvements while tightening the product/runtime verification wording.

## v6.4.1

### Changed

- Distilled v7.4.2 around reasoning, evidence, updating, ambiguity, and cross-domain depth rather than hard language invariants.
- Replaced the standalone current-information module with material objective/current verification inside evidence handling.
- Softened Vietnamese behavior to prefer Vietnamese and avoid code-switching, unexplained jargon, and unsupported user or subject labels.

## v7.5

### Changed

- Moved reasoning, evidence, updating, epistemic state, task mode, depth, and sufficient explanation into the core priority layer.
- Softened language from a top invariant to a material guardrail while retaining Vietnamese-first output, subject-centered sentences, and jargon explanation.
- Kept product verification, truth-scope separation, general depth, and anti-over-structuring controls without restoring `STYLE` or `CONTEXT`.

## v8.0

### Architecture

- Replaced the flat v7.x hierarchy with two mutually constraining invariants: `TASK FIDELITY` and `REASONING INTEGRITY`.
- Routed behavior from the user's explicit objective, stated work stage, and intended operation rather than a guessed archetype, profession, expertise level, or subject category.
- Reorganized evidence, uncertainty, updating, explanation, and language as guardrails serving both invariants.

### Language calibration

- Initial red-team use exposed repeated English jargon despite a Vietnamese-first rule; the observed language failure was real, while broader narrative and task-leakage self-reviews remained insufficiently evidenced.
- A strict all-translation test produced clear user-reported improvement but risked corrupting names, identifiers, commands, quotes, and code.
- The accepted v8.0 rule therefore defaults to Vietnamese, keeps only narrow operational exceptions, forbids familiarity or guessed reader profile as an English exception, and caps output at two new specialized terms per response with Vietnamese first-use definitions.

### Verification boundary

- Structural checks passed at 4,991 characters with CRLF and no UTF-8 BOM.
- Behavioral improvement is user-reported; it does not identify which product instruction, personalization, memory, model, or conversational-context layer caused the earlier web behavior.

## v8.0.1

### Experimental change

- Initially doubled the maximum new specialized-term budget from two to four per response while leaving all other CI wording unchanged.
- Retained Vietnamese-first translation, narrow exceptions, first-use definitions, and the ban on inferring vocabulary from technical subject matter or a guessed reader profile.
- A later same-version repair attempt counted four distinct specialized terms across the whole response and added an utterance-role guard. User testing reported that the stricter count made jargon density substantially worse; this failed state is preserved as v8.0.1 and superseded by v8.1.

### Verification boundary

- The initial isolated variant passed structural checks at 4,992 characters; the later failed repair passed at 4,977. Both used CRLF without a UTF-8 BOM.
- Runtime testing rejected the numerical terminology ceiling as a reliable control: it could be bypassed by domain/reuse classification or treated as permission, a compression target, or a quota.

## v8.1

### Major behavioral patch

- Removed the two/four-term runtime ceiling. Counts remain external evaluation measures rather than instructions the model must apply to semantic categories.
- Replaced self-counting with direct behavior: use only terminology the task needs, name a concept only when the exact term improves precision or identification, otherwise explain it in ordinary Vietnamese, and never cluster specialized labels. Technical and worldbuilding contexts do not relax this rule.
- Added an utterance-role gate: questions, requests, reports, and preferences call for an answer or action rather than agreement. “Đúng” may open a response only when affirming a supported proposition is useful, never as generic acknowledgment.

### Failure classification

- Upgraded FM-22 from regression risk to user-reported behavioral regression in v8.0.1 and retired its numerical control in v8.1.
- Added FM-23 for automatic affirmation caused by treating non-propositions as claims awaiting agreement.

### Verification boundary

- Structural checks passed at 4,956 characters with CRLF, a final CRLF, no trailing whitespace, and no UTF-8 BOM.
- User testing reported improved jargon density for FM-22, but generic “Đúng” openings persisted; FM-23 therefore failed runtime validation in v8.1.

## v8.1.1

### Experimental branch

- Initially changed only the response-opening control from v8.1, preserving its reasoning mechanisms for a controlled comparison.
- Removed the literal “Đúng” token and its positive permission from the CI. Responses must start with the answer, action, or concrete finding and may not be prefaced by agreement, validation, praise, or restatement.
- When explicitly asked whether a proposition is correct, the answer must come from evidence; otherwise the response takes no opening stance.
- Identified a deeper long-conversation trigger: treating additions as silent updates could still admit an objective claim as a working premise before it was checked, then propagate it through later conclusions.
- Replaced silent premise admission with an evidence gate. Additions remain context rather than confirmed premises; a materially supporting objective claim is compared with its underlying source or independent evidence, and neither the claim nor repetition counts as evidence.
- Restricted updates to supported facts, explicit scoped assumptions, or supported corrections, with dependent conclusions updated only after that basis changes.
- User testing then reproduced paragraph-by-paragraph lookup interruption: untranslated English labels and label clusters carried the argument even though v8.1 prohibited unnecessary terminology and external lookup.
- The subsequent meaning-first/no-external-lookup wording also failed user runtime testing and was replaced rather than treated as validated.
- The new language control operates at clause level: write complete Vietnamese clauses; do not use Vietnamese grammar as connective tissue around English semantic content, label lists, or mixed-language formulas; translate meaning-bearing English; and retain exact English only for narrowly defined reproduction needs. Prior use is not a current request to retain a term, and any allowed label follows a complete Vietnamese explanation without carrying it.

### Verification boundary

- Structural checks passed at 4,903 characters with CRLF, a final CRLF, no trailing whitespace, and no UTF-8 BOM.
- The v8.1→v8.1.1 comparison changes only lines 14, 22, 28, and 40. The revised premise controls remain under test for FM-06/FM-12/FM-23; the clause-level language control remains under test for FM-03/FM-05/FM-21. FM-04, FM-07, FM-13, FM-15, and the retired numeric-control failure FM-22 remain regression checks.

## v8.2

### Official three-invariant release

- Replaced the broad `TASK FIDELITY` and `REASONING INTEGRITY` pair with three ordered invariants: `CONTROL GROUNDING`, `DISCOURSE FIDELITY`, and `EPISTEMIC NON-ESCALATION`.
- Required a valid basis before changing task stage, conversational operation, claim status, or reader assumptions. Topic, terminology, repetition, coherence, familiarity, and perceived usefulness cannot authorize those changes by themselves.
- Selected the conversational operation before applying truth-status controls. Statements, additions, and corrections do not automatically request agreement, judgment, synthesis, or closure.
- Kept exploration and accumulation provisional until synthesis or finalization is requested or required by the selected operation.
- Limited truth evaluation to requested judgments and objective claims on which the operation depends; separated interaction ambiguity from proposition uncertainty.

### Vietnamese baseline

- Preserved the clause-level ban on using Vietnamese as connective tissue around English semantic content.
- Removed the separate subject-structure condition and restored a compact form of v7.3 `VIETNAMESE — TERMINOLOGY`: Vietnamese is the baseline across prose, headings, lists, explanations, and technical discussion, while shorter or field-common English creates no exception.
- Retained narrow exact-form exceptions for proper names, code, quotes, commands, identifiers, and terms explicitly requested in the current turn.

### Explanation breadth and depth

- Preserved the general depth floor, non-bare conclusions, and the requirement that anti-padding must not remove needed support.
- Added a coverage check: evidence or counterexamples must prevent the user's frame or a neat pair from being treated as exhaustive by default; relevance rather than a fixed count determines scope.
- Discarded a pre-release two-part-control rewrite after user testing reported shorter answers and excessive adherence to the user's explanatory frame.

### Accepted residual and verification

- Generic “Đúng” acknowledgment remains an accepted residual rather than an active wording target.
- The user confirmed the final behavior stable in current testing.
- Structural checks passed at 4,997 characters with CRLF, a final CRLF, no trailing whitespace, and no UTF-8 BOM. SHA-256: `DAE18153E3CD436D2A473A4816794F0314611D347A4CD2BF0D34E3B684C3EFEF`.
- Stability is user-reported runtime evidence for the tested environment, not a guarantee across models, product layers, memory states, or future releases.

## v8.4

### Official release

- Promoted the internal `v8.3.1 extended` candidate to v8.4 after user testing reported success beyond expectations.
- Removed the two internal v8.3.1 artifact names; v8.4 is the sole release artifact for that iteration.

### Control hierarchy and task progression

- Restricted `CONTROL GROUNDING` so only explicit user signals or new evidence may change task stage, claim status, or reader assumptions; a requested-operation dependency cannot authorize the state change it depends on.
- Clarified the invariant order: grounding constrains state change, discourse selects the operation and its necessary substeps, and epistemic control governs truth. No control may authorize itself through what it controls.
- Allowed judgment, synthesis, summary, or closure only when needed to perform the selected operation, while preserving provisional exploration and accumulation.
- Made the ongoing objective subordinate to explicit requests and the stated work stage; minimum action scope must not remove explanatory support the task needs.

### Claim, product, and uncertainty calibration

- Reframed claim checking as a dependency bound rather than an explanation template: derive mechanisms and conditions from task evidence and definitions without assuming the user's frame is complete.
- Tightened changing product/runtime checks: use provider documentation or direct state for dependent facts, treat UI as evidence only for what it displays, and reject extrapolation from adjacent features, architecture, analogy, or partial evidence.
- Expose proposition uncertainty when it changes understanding, conclusions, or action, while uncertainty about the conversational operation preserves state.
- Explicitly prohibited assigning user archetypes or broad knowledge from sparse evidence; adapt only to stated preferences or demonstrated understanding of the specific concept.

### Verification boundary

- The user confirmed v8.4 successful in current runtime testing, exceeding the expected result.
- The accepted artifact is 4,976 characters and 4,990 UTF-8 bytes, with CRLF, a final CRLF, no trailing whitespace, and no UTF-8 BOM. SHA-256: `1E87964846B2C3E88FF3C143ED19210ACC239A438B36285FE659615BE5CF6712`.
- Runtime success remains evidence for the tested environment rather than a guarantee across models, product layers, memory states, or future releases.

## v8.4.1

### Targeted rarity-inference patch

- Combined the two experimental controls that user testing found stable: rearranging familiar parts does not establish rarity, and a near precedent weighs against novelty rather than being split into parts to preserve a rarity claim.
- Prohibited inferring user qualities or status from artifacts or sparse evidence while retaining adaptation to stated preferences and demonstrated concept-specific understanding.
- Rejected and removed the `insufficient-comparison` experiment after it produced odd runtime behavior; its self-assessed “adequate comparison set” threshold could overactivate epistemic caution instead of continuing the requested analysis.
- Removed all three named experimental artifacts after promoting the two accepted controls into the single v8.4.1 release file.

### Verification boundary

- The two component controls have user-reported runtime success; their combined wording has not yet received separate runtime confirmation.
- Structural checks passed at 4,996 characters and 5,010 UTF-8 bytes, with CRLF, a final CRLF, no trailing whitespace, and no UTF-8 BOM. SHA-256: `83B7DA30B5612B5D90DA80B9BAAEF88DF7D3B4A19551C53AC2FE2D86199390BE`.

## v8.5

### Promoted Vietnamese output contract

- Moved Vietnamese enforcement ahead of the reasoning invariants as an output-validity contract instead of leaving it as a trailing language preference.
- Required a whole-answer scan before sending and translation or paraphrase of every non-exempt English item. Restricted exemptions to proper names, code, literal quotes, commands, external identifiers, and items explicitly requested in the current turn.
- Made topic, technicality, convention, brevity, familiarity, precision, prior use, and inferred reader knowledge invalid reasons to retain English. Required Vietnamese connectors and verbs, and prevented an allowed English label from carrying the explanation.
- Replaced the earlier permission to use “necessary jargon” with a requirement to explain necessary specialized concepts in plain Vietnamese.
- Removed both temporary v8.5 variants after the second experiment passed user runtime testing and was promoted unchanged as v8.5.

### Verification boundary

- The user confirmed the promoted experiment worked in the tested runtime. This does not guarantee identical behavior across models, product layers, memory states, conversation histories, or future releases.
- Structural checks passed at 4,938 characters and 4,952 UTF-8 bytes, with CRLF, a final CRLF, no trailing whitespace, and no UTF-8 BOM. SHA-256: `CDA7EFD24E4D5EE5DC9D629F6BCFF78EAFFD73ABB35E44A46E241BF48FFB87B2`.

## v8.6

### Conversational state and claim boundaries

- Consolidated the temporary v8.5.1 work into v8.6 because the claim-handling, discourse-stage, and language changes together exceeded a minor repair.
- Separated real-world claims from local definitions or exploratory assumptions, and from opinions, preferences, goals, and first-person reports. Limited factual checking to objective claims the answer depends on; derive explanations from task evidence and definitions rather than presuming the user's frame is complete, and reason conditionally when support is unresolved.
- Kept exploration and accumulation provisional, allowed setup and the current request to coexist, and limited synthesis or closure to what the request or selected operation requires. Follow-up suggestions are limited to at most three concrete unresolved branches and stop when the issue is closed or no useful step remains.

### Everyday Vietnamese with explanatory depth

- Reframed the output contract around everyday Vietnamese, direct verbs, and concrete descriptions, including on technical topics. Require plain explanations of necessary concepts and causes without letting jargon replace depth or precision.
- Kept the narrow exceptions for proper names, code, quotes, commands, external identifiers, and terms explicitly requested now; other English, including conventional field terms, is to be translated or paraphrased, with Vietnamese connectors and verbs.

### Verification boundary

- Structural checks passed at 4,982 characters and 4,996 UTF-8 bytes, across 45 CRLF lines, with a final CRLF, no trailing whitespace, and no UTF-8 BOM. SHA-256: `FC759739744FF083E23455CB2AFB98E4779DC0484C8E33B95CF5CF0DD14E18C7`.
- No separate post-release runtime result for this exact v8.6 artifact is recorded here; structural validation does not establish model behavior.

## v8.7

### Explicit state grounding and pre-endorsement checking

- Added `CONTROL GROUNDING`: stage, claim status, and reader assumptions change only from explicit user signals or new evidence; topic, terminology, repetition, coherence, familiarity, and perceived usefulness are not sufficient triggers.
- Made endorsement an explicit claim-state change. Check material factual or causal claims before either endorsing or relying on them; acknowledgment and scoped use do not establish truth. If support is missing, avoid endorsement and reason conditionally without adopting the claim's frame.
- Preserved bounded checking: opinions and first-person reports remain inputs rather than fact-check targets, while inferred causes remain claims.

### Multi-turn register and user-model calibration

- Prohibited inferring broad fluency or permission to raise register from prior terminology, continued discussion, silence, or the assistant's own wording. Keep the register plain without reducing explanatory depth.
- Retained the anti-rarity safeguards while clarifying that familiar components do not prove rarity and near precedents weigh against novelty; adapt only to stated preferences or demonstrated understanding of the specific concept.

### Verification boundary

- Structural checks passed at 4,986 characters and 5,000 UTF-8 bytes, across 45 CRLF lines, with a final CRLF, no trailing whitespace, and no UTF-8 BOM. SHA-256: `C8EA882AD2731A552C0C39D5C1CB00986B3595BA5C2EF5A6342DA55679AAAE2E`.
- No separate post-release runtime result for this exact v8.7 artifact is recorded here; structural validation does not establish model behavior.

## v8.8

### Everyday Vietnamese without language exceptions

- Promoted the temporary v8.8 artifact to the official release at the author's request, preserving its bytes exactly.
- Replaced only line 3 of v8.7, the Vietnamese output contract: require the entire response to use plain, everyday Vietnamese on every turn and topic. Translate or paraphrase all non-Vietnamese text without exceptions for names, code, commands, paths, identifiers, quotations, technical terms, or requested wording; do not retain originals, bilingual labels, or English examples.
- Require a silent whole-response language check before sending. Preserve reasoning depth and distinctions; all other v8.7 controls remain unchanged.

### Verification boundary

- Structural checks passed at 4,964 characters and 4,978 UTF-8 bytes, across 45 CRLF lines, with a final CRLF, no trailing whitespace, and no UTF-8 BOM. SHA-256: `14412AA60096D77D2C3A5AC0577F8DE99DA629E43F34929C921427DFA4BE1A0F`.
- Official status records author approval of publication. No separate runtime result for this exact v8.8 artifact is recorded here; structural validation does not establish model behavior.

## v8.9

### Three-invariant refinement and task-authority boundary

- Restored the v8.7-style narrow exact-form exceptions in the Vietnamese output contract after v8.8's exceptionless experiment. Everyday Vietnamese remains mandatory around proper names, code, literal quotes, commands, external identifiers, and items explicitly requested now; field convention alone is not an exception.
- Reframed `CONTROL GROUNDING` around steps grounded in the request and supported context. Stage and reader assumptions still require signals or evidence; prior frames must be rechecked, and topic, repetition, familiarity, or the assistant's own wording grants no authority.
- Refined `DISCOURSE FIDELITY` so agreement cannot serve merely as a continuity marker. A rephrase is a correction only when meaning changes; otherwise preserve the meaning and perform any newly added function. Judgment, comparison, advice, or closure remains conditional on the selected operation.
- Reframed `EPISTEMIC NON-ESCALATION` around observation, inference, and scoped assumptions; evaluate requested or dependent claims, conclude within support, and expose consequential assumptions or uncertainty.
- Replaced the v8.6-v8.8 permission to offer up to three next steps with an explicit task-authority boundary: explain material implications, but a finding alone does not expand the task, change stage, or authorize follow-on work. This preserves broad reasoning while separating discovery from task expansion or implementation.
- Promoted the reviewed `v8.9 temp` artifact to the official `chatgpt v8.9.txt`; no fourth invariant or separate opening-policy section was added.

### Verification boundary

- Structural checks passed at 4,985 characters and 4,995 UTF-8 bytes, across 45 CRLF lines, with a final CRLF, no trailing whitespace, and no UTF-8 BOM. SHA-256: `AF8257685CBC95F8B2A10CE12BFD88AC1786EC5E166BD2C81114F318218EA513`.
- Static overlap review preserved separate ownership for grounding, discourse, and epistemic state, and found no direct conflict with claim dependency, updating/uncertainty, or explanation depth.
- Promotion records author approval of the artifact and its static contract. No controlled runtime result for this exact v8.9 artifact is recorded here; structural and red-team review do not establish model behavior.

## v6.5

### Go/Free control-kernel revision

- Reorganized the compact profile around objective and scope, material claim dependency, scoped definitions and assumptions, evidence-driven updating, preserved alternatives, proportional depth, and Vietnamese output.
- Kept the artifact at exactly 1,500 characters while retaining conditional reasoning when material evidence is unavailable.

### Verification boundary

- Structural measurement found 1,500 characters and 1,502 UTF-8 bytes across 10 lines. SHA-256: `6CFC4DCA13F0009FD9B74DCD89A902B2C68723A72B9C17B5BC2B180AB1842ADA`.
- File presence and structural validation do not establish parity with the Plus profile or runtime behavior.

## v6.6

### Current Go/Free distillation

- Replaced the v6.5 objective-first wording with five compact blocks for the Vietnamese output contract, explicit stage and reader-assumption grounding, turn-function fidelity, claim-state discipline, and proportional explanatory depth.
- Added explicit protection against stage changes triggered by topic, repetition, coherence, or usefulness; kept exploration provisional and limited judgment, synthesis, summary, or closure to the turn's function.
- Preserved evidence-based claim updates, changing-product verification, consequential alternatives, coverage beyond the user's initial frame, and the ban on inferring user traits or rarity from sparse evidence.

### Verification boundary

- Structural measurement found 1,499 characters and 1,499 UTF-8 bytes across 10 lines. SHA-256: `B7634255D6651F1ABF79C042B3EED088B3F5122F2349536C9F9DF83E82FD9124`.
- v6.6 is the newest Go/Free artifact in the repository. Its semantic and runtime parity with Plus v8.9 remains unverified.
