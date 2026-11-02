# Multi-Project Hub Model — Updated

## 1. Core

Hub không chọn một project duy nhất. Một ý tưởng được trừu tượng hóa thành **seed**, rồi seed được fork độc lập sang các project. Ba nhánh dưới đây chỉ là ví dụ, không phải giới hạn số project.

```text
SOURCE
→ candidate idea
→ abstract seed
→ HUB
→ fork sang các project
```

**Invariant:**

```text
SHARED SEED ≠ SHARED IMPLEMENTATION
FORK SEED, NOT IMPLEMENTATION
```

---

## 2. Nguồn seed

### 2.1. Kích thích IRL trực tiếp

Nguồn có thể là đời sống thực, phim, truyện tranh, game, âm nhạc, lịch sử, tổ chức, hành vi xã hội, vật thể, cơ chế hoặc bất kỳ thứ gì kích thích tò mò.

```text
IRL stimulus
→ curiosity
→ abstraction
→ seed
→ HUB
```

### 2.2. Giấc mơ thường và lucid dream

Dream lấy các fragment IRL đã tích lũy, tái tổ hợp chúng thành situation mới và có thể chạy thử một phần causal behavior trước khi người dùng audit.

Dream output có thể gồm:

```text
candidate seed
+ provisional implementation
+ simulated situation
+ preliminary fit rationale
```

Ví dụ:

```text
"hợp P1/P2/P3 vì X/Y/Z"
```

hoặc:

```text
"P2 ổn,
nhưng P3 fail vì trigger X phá premise của causal chain"
```

Dream không trực tiếp xác lập trạng thái được chấp thuận của project.

```text
IRL fragments
→ dream / lucid dream
→ recombination
→ situation simulation
→ user audit
→ seed / candidate seed
→ HUB
```

Lucid dream có thể được dùng có chủ đích để thử một lớp tình huống cụ thể.

### 2.3. Text RP / tương tác người với người

Text RP nhiều người tạo external novelty:

```text
user action
→ other-player interpretation
→ unexpected response
→ new scene state
→ resimulation
```

Nó cung cấp nhiều trajectory và phong cách khó tự sinh khi solo.

### 2.4. LLM

LLM cũng là nguồn kích thích upstream:

- candidate edge;
- reinterpretation;
- failure mode;
- structural analogy;
- possible consequence.

```text
LLM output ≠ approved project state
LLM output ≠ design decision
```

LLM output vẫn phải qua hub.

---

## 3. Recursive seed / primitive và structural diff

### 3.1. Vai trò phụ thuộc cấp phân tích

```text
SEED / PRIMITIVE STATUS IS RELATIVE TO ANALYSIS LEVEL

S (seed)
→ decompose
→ {P1, P2, P3} (primitives ở cấp hiện tại)

P2
→ promote to seed
→ decompose
→ {Q1, Q2, Q3}

seed ↔ primitive
```

Primitive là đơn vị đang dùng để phân tích, không phải atom tuyệt đối. Promote ở đây chỉ đổi vai trò phân tích, không phải chấp thuận implementation.

### 3.2. So sánh cả common và difference

```text
A = {P1, P2, P3}
B = {P1, P2, P4}

COMMON(A,B) = {P1, P2}
DIFF(A,B) = {P3, P4}

difference
→ candidate idea
→ abstract seed
→ decompose / compare again
→ HUB
```

Đây là sơ đồ tư duy: so sánh seed / primitive và quan hệ giữa chúng khi hữu ích, không phải thuật toán bắt mọi seed so với mọi seed khác. Difference có thể chứa novelty quan trọng hơn common structure.

```text
seed
→ decompose
→ compare
→ extract difference
→ new seed
→ decompose / compare / diff
→ ...
```

---

## 4. Adversarial thought process

### 4.1. Hai vai chức năng

**The Idea Maker:** sinh big idea, tìm useful structure, mở possibility space, tìm evidence hỗ trợ, repair proposal, reframe hoặc đề xuất tăng scope khi route bị block.

**The Defendant:** phản biện assumption, tìm conflict / hidden cost / edge case, kiểm tra internal consistency và thu hẹp objection khi proposal được repair.

```text
Idea Maker → proposal
Defendant → attack
Idea Maker → evidence / repair / reframe
Defendant → narrower objection, nếu repair có cơ sở
→ repeat
```

Objection có thể thu hẹp theo progression:

```text
whole idea seems infeasible
→ idea may work but has major conflict
→ idea mostly works but still has mismatch
```

Đây là shorthand chức năng, không phải personality cố định, chẩn đoán tâm lý hoặc literal emotional grief. Không bảo đảm mọi proposal đều đi đến chấp thuận.

Phản biện còn tạo seed:

```text
big idea
→ objection / conflict C
→ abstract C as seed
→ decompose
→ new primitives
→ repair proposal
→ new consequence
→ re-abstract as new seed
```

### 4.2. Role fluidity và multi-party argument

```text
User = Idea Maker; ChatGPT = Defendant
hoặc
ChatGPT = Idea Maker; User = Defendant
→ roles có thể đổi ở vòng tiếp theo
```

Trong một heated argument có thể cùng hiện diện bốn vị trí chức năng:

```text
The Idea Maker = possibility generation / preservation
The Defendant = contradiction / cost / assumption pressure
ChatGPT = alternative formulation / design-space search / argument restructuring
Codex = repository-grounded evidence / feasibility audit
```

Đây không phải bốn actor ngang quyền: hai mục đầu là role; ChatGPT và Codex là actor/công cụ có access khác nhau, có thể đảm nhiệm role tùy claim.

```text
Idea Maker + ChatGPT vs Defendant + Codex
hoặc
Idea Maker + Codex vs Defendant + ChatGPT
→ claim-by-claim alignment may shift
```

Alliance chỉ là ví dụ, không phải rule bắt buộc. ChatGPT có thể sinh proposal, phản biện, reframe, tìm route khác hoặc viết audit proposal; không thể xác nhận repository reality nếu chưa trực tiếp thấy repo.

```text
ChatGPT: architecturally coherent
Codex: not compatible with current repo
```

Hai claim có thể cùng đúng vì khác tầng đánh giá. Nếu cùng claim và cùng context mà evidence xung đột, cần kiểm chứng tiếp.

---

## 5. Verification, dynamic scope và human gate

### 5.1. Fair Drawback

Điểm chuyển từ argument sang verification là khi các phía thống nhất rằng claim còn lại chưa thể resolve đáng tin cậy bằng context nội bộ hiện tại.

```text
proposal
→ adversarial review
→ narrowed unresolved factual / implementation claim
→ Fair Drawback
→ external evidence / tool / repository / source
```

Fair Drawback không phải một bên thắng hay thất bại của ý tưởng. Claim phụ thuộc repo được chuyển thành audit proposal cho Codex; claim khác dùng nguồn hoặc công cụ phù hợp.

### 5.2. Codex: repository-grounded auditor

Khi có direct repository access, Codex audit tính khả thi theo:

```text
current repo state
+ current proposal
+ current scope
+ current constraints
→ repo-grounded feasibility audit
→ accept / accept with correction / replan / reject
```

Codex không phải final judge hoặc authority tuyệt đối. Kết quả chỉ bao phủ evidence đã kiểm tra; repo audit không tự chứng minh runtime behavior.

| Kết quả | Ý nghĩa và bước tiếp theo |
| --- | --- |
| accept | Route phù hợp trong context đã audit; trả về user gate. |
| accept with correction | Có route khả thi nhưng cần correction; user có thể chấp thuận hoặc HALT → reject correction → replan. |
| replan | Cần proposal mới từ các vấn đề đã chỉ ra; audit lại proposal mới. |
| reject | Proposal P không khả thi trong scope S và constraints hiện tại; kiểm tra blocker trước khi quyết định dừng hay đổi bài toán. |

Correction technically valid vẫn có thể quá đắt, làm mất mục tiêu, mở dependency không mong muốn, tăng complexity hoặc đổi architecture vượt mức user chấp nhận.

```text
REJECT(P | S) ≠ REJECT(GOAL)

reject → inspect blocker
├─ fundamental invariant blocks goal → stop
└─ blocker depends on current scope
   → propose scope change
   → user review
   → new proposal
   → audit again
```

Nếu invariant chỉ chặn route hiện tại, có thể tìm route khác vẫn giữ invariant; không sửa invariant chỉ để vượt audit.

### 5.3. Dynamic scope search

```text
goal
→ scope S1 → proposal P1 → audit → reject
→ inspect blocker: S1 excludes needed upstream refactor
→ user accepts scope S2 > S1
→ proposal P2 → audit → accept with correction
→ user reviews correction / replan
→ proposal P3 → audit → accept
```

Scope cũng có thể thu hẹp hoặc reframe. Đổi input problem không phải bypass Codex; kết quả ở S1 vẫn đúng trong S1. Scope rộng hơn không bảo đảm khả thi hơn.

```text
audit blocker / failed proposal / correction analysis
→ abstract useful structure or difference
→ new seed
→ compare with existing structure
→ HUB / revised proposal
```

### 5.4. Human gate

```text
Codex result
→ return to user + ChatGPT
→ user review
├─ execute within authorized scope
├─ halt / stop
├─ replan
└─ change scope → new proposal → audit again
```

User quyết định goal, acceptable cost, scope, architecture tradeoff và final implementation permission. Audit pass tự nó không cấp quyền triển khai; authorization đã có vẫn áp dụng trong phạm vi được cấp. Scope/correction vượt quyền hiện có phải trở lại user gate.

---

## 6. Fork

```text
                    SEED
          ┌──────────┼──────────┐
          ▼          ▼          ▼
      Project A  Project B  Project C
```

Mỗi branch nhận cùng seed trừu tượng, không nhận implementation của branch khác.

---

## 7. Local compatibility check

Compatibility xác định mức phù hợp, không cấp quyền triển khai. Các bước integrate dưới đây chỉ thực hiện sau review và authorization phù hợp ở phần 5.

Mỗi project kiểm tra seed theo:

- ontology;
- invariant;
- architecture;
- current state;
- boundary;
- interface;
- causal assumptions;
- modularization target.

### 7.1. Fit

```text
seed
→ compatible
→ localize
→ integrate
```

### 7.2. No fit

```text
seed
→ incompatible
→ drop
```

Không bắt seed phải hợp mọi project.

### 7.3. Partial fit

#### 7.3a. Partial salvage

```text
seed
→ extract compatible substructure
→ integrate phần hợp
→ drop phần còn lại
```

#### 7.3b. Reinterpretation

```text
seed
→ reinterpret theo ontology cục bộ
→ check lại
→ coherent ? integrate : drop
```

Bước 7.3a/7.3b tồn tại để giảm bỏ sót ý tưởng hữu ích.

---

## 8. Modularization target của từng project

Mỗi project tự xác định module theo mục tiêu, architecture và boundary cục bộ.

```text
shared abstract seed
├─ Project A → local modularization target A
├─ Project B → local modularization target B
└─ Project C → local modularization target C
```

Không suy ra module, interface hoặc execution model của project này từ project khác. Shared method không tạo shared architecture hoặc shared authority.

---

## 9. Consequence và cascade

Sau integration:

```text
new node / mechanism
→ local consequence
→ second-order consequence
```

Nếu consequence có tiềm năng cross-domain:

```text
local consequence
→ re-abstract
→ NEW SEED
→ HUB
→ fork again
```

**Invariant:**

```text
CASCADE MUST RE-ABSTRACT
```

Không copy trực tiếp implementation từ branch nguồn sang branch khác.

---

## 10. Vì sao project phình nhanh

```text
1 stimulus
→ candidate seed
→ recursive analysis / adversarial iteration
→ multiple seeds
→ fork across projects
→ 0–N authorized local implementations
→ multiple consequences
→ re-abstracted seeds
→ HUB / fork tiếp
```

Tăng trưởng đến từ:

- fork, partial salvage và reinterpretation;
- module interaction và consequence propagation;
- dream simulation và external novelty từ IRL / RP / LLM;
- structural diff và recursive decomposition;
- adversarial objection và failed proposal;
- audit blocker, scope expansion và correction analysis.

Đây là khả năng sinh thêm cấu trúc, không phải nghĩa vụ giữ mọi seed hoặc triển khai mọi proposal. Drop / halt / stop vẫn hợp lệ.

---

## 11. Anti-drift constraints

```text
SHARED SEED ≠ SHARED IMPLEMENTATION
FORK SEED, NOT IMPLEMENTATION
LOCAL ONTOLOGY > CROSS-PROJECT ANALOGY
PARTIAL ACCEPTANCE ≠ WHOLE-SEED ACCEPTANCE
CASCADE MUST RE-ABSTRACT
NO FORCED ALL-PROJECT FIT
NO REVERSE DEFINITION
DREAM OUTPUT ≠ APPROVED PROJECT STATE
LLM OUTPUT ≠ APPROVED PROJECT STATE
LLM OUTPUT ≠ DESIGN DECISION

PRIMITIVE ≠ ABSOLUTE ATOM
PRIMITIVE MAY BECOME SEED
ANALYSIS LEVEL DEFINES ROLE
COMMON STRUCTURE ≠ COMPLETE EXPLANATION
DIFFERENCE MAY BECOME SEED
DIFF OUTPUT MAY RE-ENTER HUB
CRITIQUE MAY GENERATE NEW SEEDS
OBJECTION MAY BECOME SEED
OBJECTION ≠ TERMINAL REJECTION
REPAIR MAY CHANGE ABSTRACTION LEVEL

FAIR DRAWBACK ≠ FAILURE
FAIR DRAWBACK → VERIFY, NOT GUESS
AUDIT RESULT IS SCOPE-BOUND
REJECT(P | S) ≠ REJECT(GOAL)
REJECTION MAY INFORM REPLAN
TECHNICALLY ACCEPTABLE ≠ USER-APPROVED
ACCEPT WITH CORRECTION MAY HALT
AUDIT PASS ≠ EXECUTION AUTHORIZATION
USER GATE IS FINAL
ROLE ≠ ACTOR
ROLE MAY SHIFT
CLAIM-BY-CLAIM ALIGNMENT MAY SHIFT
SCOPE IS A VARIABLE
SCOPE CHANGE MAY OPEN NEW DESIGN SPACE
BLOCKER MAY BECOME NEW SEED
STOP IS VALID OUTPUT
```

Implementation của một branch không được dùng để định nghĩa ngược seed gốc. Diff, objection hoặc blocker tạo **seed mới**, không âm thầm sửa nghĩa seed cũ. Local reinterpretation vẫn phải qua compatibility check; scope change không tự xóa invariant.

---

## 12. Pipeline tổng quát

Các sơ đồ sau là những vòng nối nhau, không phải fixed happy path hay workflow tự động. Analysis và review có thể lặp tại seed, proposal hoặc local implementation candidate.

### 12.1. Dòng seed và implementation cục bộ

```text
SOURCE
├─ IRL stimulus
├─ ordinary dream / lucid dream
├─ text RP / human interaction
└─ LLM suggestion
        ↓
candidate idea
        ↓
abstract seed
        ↓
decompose / compare / diff, khi hữu ích ←────┐
        ├─ primitive → promote to seed ─────┤
        └─ difference → abstract new seed ──┘
        ↓
HUB ←───────────────────────────────────────────┐
        ↓                                      │
fork independently across projects             │
        ↓                                      │
local compatibility check                      │
├─ no fit → drop                               │
├─ partial fit → salvage / reinterpret → recheck│
└─ fit / compatible part                       │
        ↓                                      │
local proposal → review / verification (12.2)   │
        ↓                                      │
user-authorized implementation / integration    │
        ↓                                      │
local consequence / cascade                     │
        ├─ local only → local development       │
        └─ cross-domain potential               │
           → re-abstract as NEW SEED ───────────┘
```

### 12.2. Argument, verification và quyết định

```text
proposal ↔ Idea Maker / Defendant
           (roles / actors may shift)
        ↓
claim resolved from current context?
├─ yes → repo feasibility chưa kiểm tra?
│        ├─ yes → Codex audit → result + evidence → user gate
│        └─ no → user gate
└─ no → Fair Drawback?
   ├─ no → continue internal iteration / narrow claim
   └─ yes → external verification
            ├─ non-repo claim → relevant source / tool
            └─ repo-grounded claim → Codex audit
               (repo state + proposal + scope + constraints)
                        ↓
               accept / accept with correction / replan / reject
                        ↓
               return result + evidence to user + ChatGPT
                        ↓
                     user gate ← non-repo verification result
                     ├─ execute, if viable and authorized
                     ├─ halt / stop
                     ├─ reject correction / replan → new proposal
                     └─ approve changed scope → new proposal
                                                  ↓
                                               audit again
```

Không cần đợi Fair Drawback mới kiểm chứng một claim có nguồn sẵn. Nhánh claim đã resolve vẫn phải qua audit nếu feasibility phụ thuộc repo chưa được kiểm tra; không suy từ internal agreement sang repository reality.

### 12.3. Vòng phát sinh seed từ analysis và audit

```text
seed → primitives → promote primitive to seed
     → decompose / compare / diff
     → candidate idea → abstract NEW SEED → HUB

objection / failed proposal / audit blocker / correction
     → abstract useful structure → NEW SEED
     → recursive analysis → HUB / revised proposal

changed scope → new proposal → audit again → user gate
```

Mỗi vòng có thể tiếp tục, drop hoặc stop; không bảo đảm mọi goal đều có route khả thi. Rejection của một proposal trong scope hiện tại không tự chứng minh goal bất khả thi.
