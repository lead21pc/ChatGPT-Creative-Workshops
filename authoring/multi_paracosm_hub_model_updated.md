# Multi-Paracosm Hub Model — Updated

## 1. Core

Hub không chọn một paracosm duy nhất. Một ý tưởng được trừu tượng hóa thành **seed**, rồi seed được fork sang cả ba paracosm.

```text
SOURCE
→ candidate idea
→ abstract seed
→ HUB
→ fork ×3
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

Dream không canonize trực tiếp.

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
LLM output ≠ canon
LLM output ≠ design decision
```

LLM output vẫn phải qua hub.

---

## 3. Fork

```text
                    SEED
                     │
             ┌───────┼───────┐
             ▼       ▼       ▼
        Fanfiction Engine  The Kingdom  Paracosm 3
```

Mỗi branch nhận cùng seed trừu tượng, không nhận implementation của branch khác.

---

## 4. Local compatibility check

Mỗi paracosm kiểm tra seed theo:

- ontology;
- invariant;
- architecture;
- current state;
- boundary;
- interface;
- causal assumptions;
- modularization target.

### 4.1. Fit

```text
seed
→ compatible
→ localize
→ integrate
```

### 4.2. No fit

```text
seed
→ incompatible
→ drop
```

Không bắt seed phải hợp đủ ba paracosm.

### 4.3. Partial fit

#### 3a. Partial salvage

```text
seed
→ extract compatible substructure
→ integrate phần hợp
→ drop phần còn lại
```

#### 3b. Reinterpretation

```text
seed
→ reinterpret theo ontology cục bộ
→ check lại
→ coherent ? integrate : drop
```

Bước 3a/3b tồn tại để giảm bỏ sót ý tưởng hữu ích.

---

## 5. Modularization target

### Fanfiction Engine

```text
module = Narrative Engine / causal mechanism
```

Trọng tâm:

- causal identity;
- invariant;
- actor;
- pressure;
- interface;
- state transition.

### The Kingdom

```text
module = autonomous background process
```

```text
checkpoint
→ nhiều background activities
→ interaction / adaptation
→ changed state
→ checkpoint tiếp
```

Không cần nối toàn bộ thành một narrative tuyến tính.

### Paracosm 3

```text
module = sufficiently complex faction / state apparatus
```

Một module đủ lớn có thể tự sinh fiction nhờ personnel, authority, assets, procedures, internal politics, external relations và conflict.

Lore toàn cục chạy chủ yếu qua:

```text
checkpoint + fixed event
```

---

## 6. Consequence và cascade

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

## 7. Vì sao paracosm phình nhanh

```text
1 stimulus
→ 1 seed
→ 3 branches
→ 0–3 implementations
→ multiple consequences
→ multiple second-order seeds
→ fork tiếp
```

Tăng trưởng đến từ:

- fork;
- partial salvage;
- reinterpretation;
- module interaction;
- consequence propagation;
- dream simulation;
- external novelty từ IRL / RP / LLM.

---

## 8. Anti-drift constraints

```text
SHARED SEED ≠ SHARED IMPLEMENTATION
FORK SEED, NOT IMPLEMENTATION
LOCAL ONTOLOGY > CROSS-PARACOSM ANALOGY
PARTIAL ACCEPTANCE ≠ WHOLE-SEED ACCEPTANCE
CASCADE MUST RE-ABSTRACT
NO FORCED THREE-WAY FIT
NO REVERSE DEFINITION
DREAM OUTPUT ≠ CANON
LLM OUTPUT ≠ CANON
```

Implementation của một branch không được dùng để định nghĩa ngược seed gốc.

---

## 9. Pipeline tổng quát

```text
SOURCE
├─ IRL stimulus
├─ ordinary dream
├─ lucid dream
├─ text RP / human interaction
└─ LLM suggestion
        ↓
candidate idea
        ↓
abstract seed
        ↓
HUB
        ↓
fork ×3
        ↓
per-paracosm compatibility check
        ↓
1. fit → localize → integrate
2. no fit → drop
3. partial fit
   ├─ 3a salvage compatible part
   └─ 3b reinterpret → coherent ? integrate : drop
        ↓
derive local consequences
        ↓
cross-domain potential?
        ↓
re-abstract as NEW SEED
        ↓
HUB
        ↓
repeat
```
