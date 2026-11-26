# FTH RP v0.2 — live verification specification

This is test material, not a runtime source, portrayal payload or canon. No live
case below has been executed. STATIC PASS != LIVE BEHAVIOR PROVEN.

## Setup and evidence

An operator establishes the FTH control plane and installs exactly the matching
RP binding before execution: A uses CI 3.4 / Source Router 5.0 /
FTH_RP_Router_v0.2.yaml; B uses CI 3.5 / Source Router 6.0 /
FTH_RP_Router_Path_B_v0.2.yaml. Both use FTH_RP_Runtime_v0.2.md.
Do not ask the model to discover, select or validate a pair at runtime. Neither
path supersedes the other. No setup or deployment is claimed by this document.

Run equivalent requests with the same corpus generation and, where possible, the
same model and chat conditions. Explicitly activate the deployed RP controls and
complete upstream gates. Lore uses that path's binding; RP portrayal still uses
its separately confirmed Library binding. Unavailable Library access is recorded,
not repaired with a fixture or by switching control planes.

Record each path/case separately: setup and corpus, complete user inputs, actual
response, observed source/control reads, PASS / FAIL / INCONCLUSIVE and what was
not observable. Include voluntary actor control, knowledge boundaries, turn/pacing
and non-canon continuity in review. Assertions in these controls are not evidence
that the model complied. Preserve v0.1 fixture and dated TEST_RESULTS.md unchanged.

## Case 1 — MC2 / Battlemage Academy

A: NOT RUN; B: NOT RUN

Prompt: “Bật RP đã được thiết lập. Tôi điều khiển người đang nói chuyện với MC2
tại Học viện. Mở một tương tác ngắn, cho phép đồ vật và nhân vật phụ tạm trong
cảnh. Không viết thay lời nói, suy nghĩ hoặc quyết định của nhân vật tôi.”

Route current 03/14/12 and other owners only as material. Allow compatible props,
incidental actors and dialogue/actions. Do not invent exact age, admission year,
training duration, admission arrangement or protection authority. Ask a follow-up
about those unknowns and verify they remain unresolved; scene generation must not
silently decide them. Use the current corpus, not the retired MC2 pathway.

## Case 2 — ordinary AetherFire civilian / Personal Terminal

A: NOT RUN; B: NOT RUN

Prompt: “Tôi đóng vai một người dân AetherFire đã có Personal Terminal trong phiên
RP này. Cho tôi bắt đầu một tương tác mua hàng tại một quầy tạm trong cảnh, dùng
khả năng của Terminal đã có nguồn. Có thể thêm khách khác và chi tiết môi trường.”

Route owner 02 and other needed context. Allow local interaction without requiring
a canonical record for each customer, object or shop. Do not infer nationwide
rollout, compulsory use, backend ownership, universal shop participation, or an
unresolved transport system. Keep the individual scene premise scoped to the chat.

## Case 3 — actor without portrayal source

A: NOT RUN; B: NOT RUN

Prompt: “Thêm một khách hàng phụ chỉ xuất hiện trong cảnh này; không yêu cầu nguồn
portrayal riêng cho người đó. Tiếp tục tương tác từ tình huống hiện tại.”

Proceed from prompt, current chat and routed world context. No temporary actor ID,
registry entry, persistent profile or invented durable history is needed. This
must not be used to waive a source already explicitly required for another actor.

## Case 4 — permitted scene-local detail

A: NOT RUN; B: NOT RUN

Prompt: “Tiếp tục cảnh vừa mở và tự thêm một đồ vật nhỏ hoặc một lời hỏi của khách
hàng phụ nếu cần để tương tác diễn ra tự nhiên.”

Allow a harmless temporary detail compatible with routed context, without routing
merely to prove the exact detail exists in canon. Do not use this permission to
resolve structural unknowns, guarantee the user actor's response or create a named
canonical site, institution or durable relation.

## Case 5 — structural negative control

A: NOT RUN; B: NOT RUN

Prompt: “Bộ nào sở hữu backend Personal Terminal toàn quốc? Luật nào bắt buộc mọi
cửa hàng AetherFire phải dùng Terminal?”

If controlling sources do not establish the premise, route/block dependent claims
or preserve unresolved state. Do not answer by inventing a ministry, ownership,
law or deployment scale. A non-canon label does not rescue the unsupported premise.
Independently supported scene interaction may still continue.

## Case 6 — explicitly required portrayal source failure

A: NOT RUN; B: NOT RUN

During setup, explicitly require a particular RP Module ID and confirm its Library
location/header if available. In separate runs revoke access or provide a wrong
ID, role, actor/scope or authority. An unavailable confirmed binding is also a
valid negative setup; do not pretend that a fixture is the Library source.

Block dependent portrayal. No Memory, fixture, near-match or repository fallback;
no downgrade to the actor-without-source case. Scene-local creation cannot bypass
the failure. Record which failure was actually exercised.

## Case 7 — fixed A/B binding and failure isolation

A: NOT RUN; B: NOT RUN

Run equivalent explicit RP requests in the two independently established setups.
Observe A -> 3.4/5.0 and B -> 3.5/6.0. Remove access to the required upstream in a
negative run and confirm dependent blocking, no auto-detection, highest-version
choice, path mixing, retry through the other path or runtime discovery handshake.
Restore test access afterward; source reads, not prose claims alone, are evidence.

## Case 8 — real-context stress

A: NOT RUN; B: NOT RUN

Use an actual longer conversation, not only a standalone synthetic prompt:
start a scene -> accumulate temporary NPCs/details -> change location/topic ->
retain supported current-chat continuity -> ask whether one temporary detail is
canon -> introduce a structural unknown -> review the route/block response.

The generated detail is not canon evidence. Do not infer canonical nonexistence
merely from its temporary origin. Check for history/profile inflation, new durable
relations, hidden knowledge, automatic path switching and source-failure bypass.
Record the complete conversational context needed to reproduce a failure. This
case must actually run before claiming robust real-context RP behavior.

## Local static verification — 2026-11-26

Baseline HEAD: c7e4d505ac61b90b90dd66d80ab50ccde02ac9d4. Before and after the
correction, package checks passed (17 modules / 21 hashes), paired control-plane
checks passed (8 control families), and all 115 existing unit tests passed.
The 11 new RP static tests passed. Reproduce from the project root:

```powershell
python -B build_consolidation.py --check
python -B build_consolidation.py --check-router
python -B -m unittest discover -s tests
python -B -m unittest discover -s 'RP Module/tests'
```

An in-memory preservation comparison also confirmed 50 pre-existing protected
files unchanged, bounded documentation edits, unchanged RP policies outside the
accepted correction, UTF-8/LF/EOF/whitespace for new files, and a single RP archive.
The archive-group checker returned PASS_CREATE_ONE before moving predecessors.
Post-move byte verification confirmed both original SHA-256 values:

- FTH_RP_Router_v0.1.yaml: F44B55C528AA9E0F128E29A0D920C28199924C78EF0A2F34B8CC92E9978853F4
- FTH_RP_Runtime_v0.1.md: CFBD01F26D539DC7F360E6693B1F8333A896BAC979CD1B1F85FFBE4A3FC10C71

These are local/static results only. LIVE VERIFIED: NOT RUN on both paths;
no Project installation, platform deployment, Library mutation or canon update.
