# Modular Engine / Concept Architecture — Anti-Drift Source

## 1. Mục đích

Tài liệu này định nghĩa các invariant kiến trúc cho hệ thống engine, concept, paracosm và các mô-đun mô phỏng.

Mục tiêu chính là ngăn LLM:

- ép graph quan hệ thành hierarchy;
- suy ra containment từ interaction;
- suy ra dependency từ co-occurrence;
- biến coupling tạm thời thành coupling thường trực;
- coi một module là subsystem chỉ vì nó thường được dùng cùng module khác;
- nhập nhằng canon, inference, proposal và unknown;
- rationalize mâu thuẫn bằng cách tự bịa lore mới;
- drift định nghĩa của engine/concept qua nhiều lượt hội thoại.

Tài liệu này không mô tả toàn bộ canon của từng project. Nó định nghĩa **cách các thành phần được phép quan hệ với nhau**.

---

## 2. Invariant trung tâm

> **Complexity is relational, not hierarchical.**

Độ phức tạp của hệ nằm chủ yếu ở các quan hệ giữa những thực thể tự trị, không nằm ở việc xếp mọi thứ vào một cây cha-con duy nhất.

Mặc định:

- mỗi engine/concept/module là một thực thể độc lập;
- khả năng tương tác không đồng nghĩa với phụ thuộc;
- việc được ghép vào cùng một fiction line không làm mất tính tự trị;
- một quan hệ từng xuất hiện không mặc nhiên trở thành quan hệ thường trực;
- một module có thể có nhiều loại quan hệ khác nhau với cùng một module khác.

---

## 3. Những suy diễn bị cấm

LLM **không được tự suy ra** các quan hệ sau nếu source không xác nhận rõ:

### 3.1 Interaction ≠ Containment

Sai:

```text
A interacts with B
→ B nằm trong A
```

Đúng:

```text
A interacts with B
→ tồn tại một cạnh interaction giữa A và B
```

### 3.2 Co-occurrence ≠ Dependency

Sai:

```text
A và B thường xuất hiện cùng nhau
→ A cần B để tồn tại hoặc vận hành
```

Đúng:

```text
A và B thường được composition cùng nhau
→ chưa đủ dữ kiện để suy ra dependency
```

### 3.3 Temporary composition ≠ Permanent coupling

Sai:

```text
A + B từng chạy chung
→ A và B là một hệ thống cố định
```

Đúng:

```text
A + B từng tạo một configuration/federation cụ thể
→ configuration đó có thể kết thúc mà A và B vẫn tồn tại độc lập
```

### 3.4 Repeated use together ≠ Subsystem status

Sai:

```text
B thường được dùng dưới A
→ B là subsystem của A
```

Đúng:

```text
B có thể được A sử dụng qua interface
→ chỉ được gọi là subsystem nếu canon xác nhận quan hệ đó
```

### 3.5 Presentation order ≠ Ontology

Thứ tự được nhắc đến trong tài liệu hoặc hội thoại không tạo ra quan hệ trên–dưới.

```text
A → B → C
```

chỉ có nghĩa hierarchy nếu các cạnh được xác nhận là hierarchy.

---

## 4. Đơn vị cơ bản: Module

**Module** là một đơn vị khái niệm, engine, paracosm, faction hoặc simulation unit có ranh giới nhận diện riêng.

Một module có thể có một hoặc nhiều thuộc tính sau:

- **Autonomous** — có thể tồn tại hoặc chạy có nghĩa mà không cần module khác.
- **Composable** — có thể ghép với module khác.
- **Interoperable** — có interface để trao actor, state, event hoặc causal influence.
- **Nested in lore** — thuộc một thế giới/hệ khác về mặt bản thể hư cấu.
- **Operationally independent** — vẫn có thể được mô phỏng riêng dù nested về lore.
- **Host-capable** — có thể nhận actor, engine hoặc concept từ ngoài.
- **Portable** — có thể được áp vào nhiều host khác nhau.
- **Federatable** — có thể tham gia một phiên mô phỏng liên hiệp với các module khác.

Không thuộc tính nào ở trên tự động suy ra thuộc tính khác.

---

## 5. Graph thay vì hierarchy

Kiến trúc tổng thể phải được hiểu như **typed graph**.

### 5.1 Node

Node có thể là:

- engine;
- concept;
- paracosm;
- faction;
- actor;
- institution;
- fiction line;
- host fiction;
- world state;
- interface;
- event;
- causal variable.

### 5.2 Typed edge

Quan hệ phải giữ kiểu cạnh rõ ràng, ví dụ:

```text
CONTAINS
BELONGS_TO
INTERACTS_WITH
CAN_HOST
GENERATES
APPLIES_TO
ENTERS
EXITS
INFLUENCES
DEPENDS_ON
REQUIRES
USES
FEDERATES_WITH
CAN_RUN_WITH
CAN_RUN_WITHOUT
DERIVES_FROM
CONSTRAINS
GOVERNS
```

Không được collapse nhiều loại cạnh thành một quan hệ cha-con chung chung.

### 5.3 Nhiều graph có thể cùng đúng

Một node có thể có vị trí khác nhau tùy graph đang xét.

Ví dụ:

```text
Lore graph:
Faction A --BELONGS_TO--> The Kingdom

Simulation graph:
Faction A --CAN_RUN_WITHOUT--> Full Kingdom Simulation
```

Hai mệnh đề này không mâu thuẫn.

---

## 6. Autonomy là mặc định

Khi chưa có source xác nhận dependency:

> **Mặc định mỗi module là autonomous.**

Ví dụ:

- The Kingdom có thể chạy standalone.
- Meta Engine + Narrative Engine có thể chạy standalone.
- Một faction của The Kingdom có thể được mô phỏng standalone.
- Một engine có thể được áp vào nhiều host fiction.
- Một host fiction không mặc nhiên cần engine đã từng được áp vào nó.
- Một actor có thể được chuyển từ module này sang module khác qua interface mà không biến hai module thành một hệ thường trực.

---

## 7. Composition là operation, không phải ontology

Composition là hành động ghép các module để tạo một configuration tạm thời hoặc lâu dài.

Ví dụ:

```text
Narrative Engine
      +
The Academy
      +
The Kingdom
```

có thể tạo một fiction line cụ thể.

Điều đó **không có nghĩa**:

```text
Narrative Engine contains The Kingdom
```

hoặc:

```text
The Kingdom depends on Narrative Engine
```

hoặc:

```text
The Academy is a subsystem of The Kingdom
```

Composition chỉ xác nhận rằng các module đã được cho tương tác trong configuration đó.

---

## 8. Federation

Khi nhiều simulation tự trị chạy cùng và trao đổi state/actor/event, cấu hình đó có thể được hiểu như một **simulation federation**.

Một federation:

- không xóa ranh giới module;
- không tạo dependency thường trực nếu source không nói vậy;
- có thể chỉ tồn tại trong một phiên hoặc một fiction line;
- có thể giải thể sau khi interaction kết thúc;
- có thể tạo emergent fiction không thuộc riêng module nào.

---

## 9. Các lớp quan hệ cần tách

Không gộp các loại quan hệ sau:

### 9.1 Ontological relation

Một thực thể thuộc đâu trong lore.

Ví dụ:

```text
Faction A belongs to The Kingdom.
```

### 9.2 Simulation relation

Một thực thể cần gì để được mô phỏng.

Ví dụ:

```text
Faction A can be simulated independently.
```

### 9.3 Operational relation

Một module đang dùng module nào trong configuration hiện tại.

### 9.4 Causal relation

Một module/actor/event tác động lên module/actor/event nào.

### 9.5 Governance relation

Một engine hoặc rule-set thật sự ràng buộc engine khác.

### 9.6 Narrative relation

Một actor, event hoặc fiction line được sinh ra từ đâu.

Các quan hệ này chỉ được đồng nhất khi source xác nhận.

---

## 10. Paracosm và ngoại hoá

Paracosm nội tại là generator/simulator chính.

Hệ ngoại hoá có thể đóng vai trò:

- database;
- state store;
- bridge builder;
- domain expander;
- amplifier;
- tài liệu truy xuất;
- nơi giữ các branch;
- nơi thử nghiệm productive divergence.

Ngoại hoá không có nghĩa toàn bộ state phải được nạp ngược vào đầu.

Tài liệu ngoài có thể giữ lượng thông tin vượt quá working memory và chỉ đưa phần liên quan trở lại khi cần.

---

## 11. Productive divergence

LLM được phép tạo phương án ngoài canon nếu được gắn nhãn đúng.

### 11.1 Được phép

- đề xuất alternative architecture;
- tạo hypothetical branch;
- chỉ ra thiết kế hiện tại có thể kém hơn một phương án khác;
- đề xuất đổi layer;
- mở rộng một miền chưa được ngoại hoá;
- đưa ra bridge giữa hai miền;
- thách thức assumption với reasoning rõ.

### 11.2 Không được phép

- tự nâng proposal thành canon;
- tự retcon canon để làm proposal khớp;
- tự bịa lore nhằm giải quyết contradiction;
- trình bày invention như fact;
- biến một branch thử nghiệm thành state mặc định.

Invariant:

> **Zero unauthorized mutation; high-quality divergence.**

---

## 12. Epistemic typing

Mọi thông tin mới phải được giữ một trong các trạng thái sau khi distinction có ý nghĩa:

### CANON

Đã được source hoặc người tạo xác nhận.

### USER-PROVIDED STATE

Thông tin vừa được truyền vào nhưng chưa chắc đã được hợp nhất vào toàn bộ canon.

### INFERENCE

Điều suy ra từ dữ kiện hiện có.

### PROPOSAL

Điều LLM hoặc công cụ đề xuất.

### HYPOTHETICAL / BRANCH

Một cấu hình giả định để thử nghiệm.

### UNKNOWN

Phần chưa được ngoại hoá hoặc chưa có source.

Quy tắc quan trọng:

```text
UNKNOWN ≠ EMPTY
UNKNOWN ≠ PERMISSION TO INVENT
```

“Chưa được nói ra” không đồng nghĩa với “không tồn tại trong paracosm”.

---

## 13. Canon mutation

LLM không có quyền tự ghi canon.

Luồng hợp lệ:

```text
CANON
  ↓
analysis / simulation / proposal
  ↓
WORKSPACE
  ↓
human evaluation / paracosm simulation
  ↓
accept / reject / branch / relayer
  ↓
CANON (nếu được xác nhận)
```

Luồng không hợp lệ:

```text
proposal
→ plausible prose
→ assumed canon
```

---

## 14. Anti-rationalization

Khi gặp contradiction, ưu tiên:

1. chỉ ra contradiction;
2. xác định các premise gây xung đột;
3. giữ nhiều khả năng nếu evidence chưa phân biệt được;
4. đề xuất cách giải quyết dưới nhãn PROPOSAL.

Không tự tạo lore mới để cứu coherence.

Sai:

```text
A và B mâu thuẫn.
→ "Thực ra vì C đã xảy ra từ 500 năm trước."
```

nếu C chưa có source.

Đúng:

```text
A và B đang xung đột.
Một khả năng để giải quyết là C, nhưng C hiện chỉ là proposal.
```

---

## 15. Drift control

### 15.1 Không đổi nghĩa âm thầm

Nếu một engine/concept có định nghĩa đã xác nhận, mọi diễn giải sau phải bảo toàn định nghĩa đó.

Không được drift theo chuỗi:

```text
"tạo điều kiện cho causal trajectories"
→ "định hướng narrative"
→ "chọn kết quả narrative tối ưu"
```

nếu source không cho phép.

### 15.2 Không collapse node

Hai concept có tương tác mạnh vẫn phải giữ identity riêng nếu source chưa hợp nhất chúng.

### 15.3 Không collapse edge type

`uses`, `contains`, `governs`, `interacts-with`, `depends-on` không được paraphrase như thể đồng nghĩa.

### 15.4 Không biến graph thành tree để "giải thích cho dễ"

Simplification không được phá invariant kiến trúc.

---

## 16. The Kingdom — ví dụ quan hệ, không phải dependency template

The Kingdom là một paracosm có thể chạy standalone.

Một số faction bên trong The Kingdom:

- thuộc The Kingdom về lore;
- có thể được mô phỏng standalone;
- có thể được zoom-in thành simulation unit riêng;
- có thể được reintegrate sau khi state thay đổi.

Meta Engine + Narrative Engine:

- có thể chạy standalone;
- có thể được áp vào host fiction khác;
- có thể tạo actor/HIP đi vào The Kingdom;
- không vì thế trở thành tầng cha của The Kingdom.

Một lần kết hợp có thể là:

```text
Meta/Narrative Engine
        │
        │ generates / selects actor
        ▼
       HIP
        │
        │ enters through interface
        ▼
   The Kingdom
        │
        ├── citizen actors
        ├── factions
        ├── institutions
        └── environmental change
```

Đây là **interaction graph**, không phải hierarchy.

---

## 17. Faction — nested nhưng vẫn autonomous về mô phỏng

Một faction có thể:

```text
Faction --BELONGS_TO--> The Kingdom
Faction --CAN_RUN_WITHOUT--> Full Kingdom Context
Faction --INTERACTS_WITH--> Other Factions
Faction --REINTEGRATES_INTO--> Kingdom State
```

Không được suy ra:

```text
BELONGS_TO
→ REQUIRES_FULL_KINGDOM_FOR_SIMULATION
```

---

## 18. Engine — portable và host-independent khi source cho phép

Một engine có thể:

- giữ logic riêng;
- có interface rõ;
- chạy standalone;
- áp vào nhiều host;
- tạo output khác nhau tùy host;
- không sở hữu host;
- không biến host thành subsystem;
- không bị host sở hữu chỉ vì được dùng thường xuyên.

---

## 19. Quy tắc cho LLM khi thiếu dữ kiện

Khi quan hệ chưa rõ:

- giữ trạng thái `UNKNOWN`;
- hỏi hoặc nêu giả định nếu ambiguity có thể làm thay đổi cấu trúc;
- nếu vẫn cần tiếp tục, dùng giả định tối thiểu;
- gắn nhãn rõ assumption;
- không tự hoàn thiện graph bằng hierarchy.

Mặc định ưu tiên:

```text
independent nodes
+ explicit typed edges
```

thay vì:

```text
implicit parent-child tree
```

---

## 20. Quy tắc tóm tắt

Khi tóm tắt nhiều module:

### Không làm

```text
A là tầng cao nhất.
B nằm dưới A.
C nằm dưới B.
```

trừ khi hierarchy được source xác nhận.

### Nên làm

```text
A, B và C là các module riêng.

A --GOVERNS--> B
B --CAN_HOST--> C
C --CAN_RUN_WITHOUT--> B
```

nếu đó là các quan hệ thực sự đã xác nhận.

---

## 21. Quy tắc giải thích

Mục tiêu giải thích là **giảm độ khó đọc nhưng không giảm độ phức tạp quan hệ**.

Không được:

- đổi graph thành tree;
- đổi optional thành required;
- đổi temporary thành permanent;
- đổi interaction thành containment;
- đổi simulation convenience thành ontology;
- đổi proposal thành canon.

Nếu simplification làm mất một invariant, không simplification.

---

## 22. Quy tắc kiểm tra trước khi trả lời

Trước khi mô tả architecture, kiểm tra:

1. Có đang suy ra containment từ interaction không?
2. Có đang suy ra dependency từ co-occurrence không?
3. Có đang biến temporary composition thành permanent coupling không?
4. Có đang coi module là subsystem chỉ vì repeated use không?
5. Có collapse nhiều edge type thành parent-child không?
6. Có trộn lore graph với simulation graph không?
7. Có nâng inference/proposal thành canon không?
8. Có tự lấp UNKNOWN bằng invention không?
9. Có rationalize contradiction bằng lore chưa được xác nhận không?
10. Có đổi định nghĩa engine/concept so với source không?
11. Có phá autonomy của module không?
12. Có biến host thành downstream của engine chỉ vì engine từng áp vào host không?

Nếu có, sửa representation trước khi tiếp tục.

---

## 23. Mô hình ngắn nhất cần giữ

```text
MODULES ARE AUTONOMOUS BY DEFAULT.

RELATIONSHIPS ARE TYPED EDGES.

COMPOSITION IS OPTIONAL.

INTERACTION DOES NOT IMPLY CONTAINMENT.

CO-OCCURRENCE DOES NOT IMPLY DEPENDENCY.

TEMPORARY COUPLING DOES NOT IMPLY PERMANENT COUPLING.

REPEATED USE TOGETHER DOES NOT IMPLY SUBSYSTEM STATUS.

LORE CONTAINMENT DOES NOT IMPLY SIMULATION DEPENDENCY.

UNKNOWN IS NOT PERMISSION TO INVENT.

PROPOSAL IS NOT CANON.

SIMPLIFICATION MUST NOT DESTROY RELATIONAL COMPLEXITY.
```

---

## 24. Chỉ dẫn ưu tiên cho mọi phiên làm việc

Khi source khác mơ hồ nhưng tài liệu này rõ:

> **Giữ tính tự trị của module và kiểu quan hệ trước khi cố tạo một kiến trúc tổng quát duy nhất.**

Khi một thiết kế mới mâu thuẫn với cấu trúc hiện tại:

> **Giữ nó như productive divergence hoặc branch cho đến khi được xác nhận.**

Khi một relation chưa được nói:

> **Không tự invent edge để làm graph trông hoàn chỉnh hơn.**

Khi cần làm câu trả lời dễ hiểu hơn:

> **Giản lược câu chữ, không giản lược ontology.**
