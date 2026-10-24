# Hai Paracosm: The Kingdom và The Academy / Concept Engine

## Tài liệu handoff cho LLM khác

**Mục đích:** cung cấp một mô hình đủ chi tiết để một LLM mới có thể hiểu đúng hai paracosm đang được externalize, không trộn ontology, không ép chúng về cùng một kiểu worldbuilding, và hiểu tại sao quá trình dùng AI đã kéo theo behavior engineering, RAG, local LLM, image generation và app-building.

**Phạm vi:** tài liệu này chỉ phân tích hai paracosm đã được thảo luận trực tiếp:

1. **The Kingdom** — paracosm vận hành chủ yếu như một world-state / historical simulation.
2. **The Academy / Concept Engine** — paracosm vận hành chủ yếu như một ecology của narrative engine / concept có tính modular, portable và composable.

Người tạo đã nói còn **một paracosm thứ ba có độ phức tạp tương đương**, nhưng paracosm thứ ba không nằm trong phạm vi tài liệu này vì chưa có đủ dữ liệu để mô tả.

---

# 0. Quy tắc đọc tài liệu

Tài liệu dùng ba nhãn nguồn:

- **[SOURCE]** — thông tin xuất hiện trực tiếp trong các file đã đọc.
- **[USER-PROVIDED]** — thông tin người tạo nói trực tiếp trong hội thoại nhưng không nhất thiết đã được formalize trong source file hiện có.
- **[INFERENCE]** — kết luận phân tích rút ra từ source + lời người tạo. Không được tự nâng thành canon của paracosm.

Một LLM đọc tài liệu này phải giữ nguyên quy tắc:

```text
UNKNOWN ≠ EMPTY
UNKNOWN ≠ PERMISSION TO INVENT
PROPOSAL ≠ CANON
INTERACTION ≠ CONTAINMENT
CO-OCCURRENCE ≠ DEPENDENCY
COMPOSITION ≠ PERMANENT COUPLING
```

Đây không chỉ là style preference. Đây là lớp chống drift bắt buộc khi làm việc với hai paracosm.

---

# 1. Tóm tắt cực ngắn

## The Kingdom

**Loại runtime:** stateful historical simulation.

**Đơn vị trung tâm:** world-state đang tồn tại và lịch sử tích lũy của nó.

**Câu hỏi cơ bản:**

> Nếu một biến cố xảy ra trong trạng thái hiện tại, xã hội, thể chế, actor và hạ tầng sẽ phản ứng thế nào, rồi trạng thái lịch sử tiếp theo trở thành gì?

**Công thức nén:**

```text
WORLD STATE(t)
→ disturbance / checkpoint
→ distributed reactions
→ normalization / adaptation
→ accumulated consequences
→ WORLD STATE(t+1)
```

**Nguy cơ LLM lớn nhất:** làm hỏng continuity, tự lấp phần chưa externalize, hoặc đưa logic generic fantasy / power fantasy / moral reconciliation vào một lịch sử vốn đã có.

---

## The Academy / Concept Engine

**Loại runtime:** modular causal-engine simulation.

**Đơn vị trung tâm:** engine / concept / module tự trị có primitive, rule, interface, paradox hoặc state-transition riêng.

**Câu hỏi cơ bản:**

> Khi engine X được instantiate hoặc composition với host/configuration Y, nó tạo điều kiện gì, actor/HIP nào xuất hiện hoặc thay đổi, và causal trajectory nào phát sinh?

**Công thức nén:**

```text
ENGINE / CONCEPT
→ conditions / primitives / interface
→ host or configuration
→ actor / HIP / anomaly interaction
→ causal trajectory
→ emergent narrative / state change
```

**Nguy cơ LLM lớn nhất:** collapse module thành hierarchy, ép các engine vào cùng template, biến interaction thành dependency, hoặc biến lore implementation-specific thành core engine.

---

# 2. Khác biệt nền tảng: chúng không chỉ là hai setting khác nhau

[INFERENCE]

The Kingdom và The Academy khác nhau ở tầng sâu hơn genre, aesthetic hoặc lore. Chúng vận hành gần như **hai operating systems khác nhau cho imagination**.

Nếu chỉ đổi từ fantasy sang sci-fi nhưng vẫn giữ cùng cách mô phỏng thì đó chỉ là đổi setting. Ở đây thay đổi cả:

- đơn vị cơ bản của mô hình;
- điều gì được xem là state;
- điều gì được xem là actor;
- causal flow;
- cách history được sinh;
- cách module được nối;
- tiêu chí coherence;
- failure mode;
- cách LLM phải được điều khiển.

Vì vậy người tạo có thể chán một bên rồi chuyển sang bên kia và thực sự đổi loại tải nhận thức, không chỉ đổi skin.

---

# 3. The Kingdom — bản chất paracosm

## 3.1. Nguồn gốc: Imagination Sphere

[USER-PROVIDED]

Trước khi biết thuật ngữ **paracosm**, người tạo tự gọi cấu trúc này là **Imagination Sphere**.

Lý do dùng “Sphere” không chỉ mang tính mỹ học.

Tiền đề ban đầu của The Kingdom là:

- một quốc gia được giả định gần như hoàn hảo về mọi mặt;
- có một miền bên trong rất mạnh, tự đủ và được bảo vệ;
- thế giới bên ngoài là phía muốn chen chân để được vào;
- quan hệ inside/outside là một trục quan trọng ngay từ sớm.

[INFERENCE]

Do đó “Sphere” phản ánh một **miền có biên**, tương đối kín, với quan hệ trung tâm–ngoại vi rõ. Điểm này giải thích vì sao các bài toán biên giới, nhập cảnh, quyền tiếp cận, thương mại, legitimacy và external pressure về sau dễ trở thành hạ tầng tự nhiên của worldbuilding.

---

## 3.2. The Kingdom không bắt đầu như “history is the main actor”

[USER-PROVIDED]

Một correction quan trọng:

- The Kingdom **ngay từ đầu đã được định hướng theo mô hình world simulation**.
- Nhưng **history ban đầu chưa phải main actor**.
- Main actor ban đầu là **The Immortal King đi vi hành**.

Không được kể genealogy sai theo kiểu:

```text
character-centric fiction
→ dần dần worldbuilding lớn lên
→ cuối cùng mới thành simulation
```

Cấu trúc đúng hơn là:

```text
world already oriented toward systemic simulation
+
The Immortal King as central mobile actor / viewpoint
→ world grows in autonomy and scale
→ observation becomes distributed
→ history/world-state becomes the dominant organizing axis
```

[INFERENCE]

The Immortal King có thể được hiểu như **camera di động đời đầu**: một tác nhân bền vững có thể đi xuyên nhiều địa phương, tầng xã hội và giai đoạn lịch sử, cho phép cùng một viewpoint quan sát một thế giới lớn.

Điều sẽ falsify inference này: source cũ cho thấy Immortal King thực ra là causal center khiến thế giới tồn tại chủ yếu để phục vụ plot cá nhân, chứ không phải viewpoint đi xuyên một thế giới vốn đã vận hành độc lập.

---

## 3.3. Trạng thái hiện tại: world/history là actor gần nhất với “main character”

[USER-PROVIDED + PRIOR PROJECT MATERIAL]

Ở cấu trúc hiện tại, The Kingdom không ưu tiên pipeline:

```text
main character
→ goal
→ chapter
→ climax
```

Mà ưu tiên:

```text
world-state
→ checkpoint
→ state transition
→ social/institutional reaction
→ normalization
→ next checkpoint
```

“Main character” gần nhất là **world-state theo thời gian**.

Nhân vật vẫn tồn tại nhưng thường có chức năng giống **camera cục bộ** giúp quan sát một phần hệ thống.

---

# 4. The Kingdom — runtime

## 4.1. Checkpoint model

[USER-PROVIDED]

Lịch sử được tổ chức bằng **checkpoint (CP)**, không phải scene tuyến tính.

Một checkpoint là một historical event hoặc environmental shock làm thay đổi state.

Ví dụ đã được nêu:

- **CP1:** bắt đầu mở cửa / mở thương mại.
- **CP2:** các nước láng giềng bắt đầu hostile/aggression.
- Khoảng cách CP1 → CP2 chỉ khoảng **2 năm**.

Điều này làm giai đoạn giữa CPs trở thành vùng có causal density cao: thương mại, công nghệ, lao động, nhận thức về outsider, truyền thông, interest conflict và institutional response có thể đổi nhanh.

---

## 4.2. Path dependence

The Kingdom có **path dependence** rất mạnh.

```text
CP(n)
→ changes state
→ actor/institution adapts
→ CP(n+1) inherits result
```

Do đó một thay đổi nhỏ ở quá khứ có thể đòi regression test rất sâu về tương lai.

Một NPC/social stratum ở CPn không thể phản ứng theo cách mâu thuẫn với trạng thái mà chính họ trở thành ở CPn+1 nếu không có causal bridge.

Đây là lý do thêm “một ý hay” vào đầu timeline không hề rẻ.

---

## 4.3. Multi-scale simulation

[USER-PROVIDED]

The Kingdom có thể zoom:

```text
world
→ state
→ institution
→ agency
→ company / organization
→ profession
→ citizen / NPC
```

Nhưng người tạo **không chủ trương mô phỏng full POV của mọi NPC** vì chi phí quá lớn.

Thay vào đó dùng các kênh quan sát thụ động / diegetic như:

- radio;
- báo;
- livestream công dân;
- public notice;
- podcast;
- gossip;
- meme;
- công văn;
- nghề nghiệp / đời sống cục bộ.

Các kênh này hoạt động như **social sensors**: chúng không cho omniscient truth, mà cung cấp các lát cắt biased nhưng có thể đọc được của world-state.

Điều này có hai chức năng:

1. giảm chi phí full NPC simulation;
2. giữ cảm giác thế giới có đời sống phân tán.

---

## 4.4. Institutional runtime

[USER-PROVIDED]

Một mục tiêu thiết kế lâu dài là tạo thể chế:

- đủ competent để không trở thành phông nền cho power-fantasy MC;
- nhưng không hoàn hảo;
- agency phải phối hợp đủ để xã hội phát triển;
- đồng thời vẫn có self-interest, greed, jurisdiction và conflict đủ để constrain lẫn nhau.

Đây là bài toán khó vì “competent ≠ perfect” không giải quyết được implementation. Cần tạo ra **imperfection có tính hữu cơ** mà không phá competence tổng thể.

Người tạo mô tả nó gần như làm toán / game theory.

---

# 5. The Kingdom — ontology

## 5.1. World membership mạnh hơn The Academy

[INFERENCE]

The Kingdom có ontology mang tính **world-embedded** mạnh:

- citizen thuộc world;
- institution thuộc state;
- faction có lore membership;
- geography/infrastructure tạo constraint;
- lịch sử tích lũy tạo identity.

Tuy vậy, source anti-drift xác nhận một faction vẫn có thể:

```text
Faction --BELONGS_TO--> The Kingdom
Faction --CAN_RUN_WITHOUT--> Full Kingdom Simulation
Faction --REINTEGRATES_INTO--> Kingdom State
```

Nghĩa là **lore containment không đồng nghĩa simulation dependency**.

The Kingdom vẫn có thể zoom một module ra chạy độc lập rồi reintegrate state.

---

## 5.2. State là thứ phải giữ

Nếu phải chọn thứ có giá trị ontology cao nhất trong runtime The Kingdom, đó là:

- world-state;
- historical continuity;
- actor knowledge;
- institutional state;
- causal inheritance.

Một retcon hoặc proposal sai có thể gây **continuity debt** xuyên timeline.

---

# 6. The Kingdom — triết lý

[INFERENCE dựa trên USER-PROVIDED]

Triết lý vận hành có thể nén thành:

> **Thế giới phải có khả năng phản ứng như một hệ thống, không như sân khấu dành cho một protagonist.**

Các hệ quả:

- một cá nhân mạnh đến cấp planet-destroying vẫn phải đối diện legitimacy, fear và institutional response;
- nhà nước có lý do rational để sợ và constrain power;
- payoff không nhất thiết là “face-slapping” cá nhân;
- conflict có thể nằm ở state, institution, law, interest, economy, legitimacy;
- thế giới không được tự làm ngu để protagonist trông thông minh.

The Kingdom vì vậy chống lại một failure mode phổ biến của LLM: biến worldbuilding thành MC-centric wish fulfillment.

---

# 7. The Kingdom — quy mô và hạ tầng

[USER-PROVIDED]

Genre direction được mô tả là **neo fantasy**:

- “Neo” = technology;
- không đồng nghĩa cyberpunk;
- fantasy vượt high fantasy thông thường;
- có xu hướng grim / grimdark nhưng không nhất thiết nihilistic;
- worldbuilding có thể đạt quy mô **Type II civilization**.

Ví dụ đã nêu về logistics:

- central port có thể là **floating island / flying fortress** ở high airspace;
- sea port có thể đặt dưới đất;
- central port là transfer hub giữa sea port và atmospheric/interplanetary infrastructure.

Một insight của người tạo:

> đưa nhiều hạ tầng lên trời có thể giảm constraint địa hình, nhưng complexity không mất; nó chuyển thành bài toán phải tự thiết kế hạ tầng nguyên bản.

Một reference đời thật như Port of Rotterdam đã lập tức được “ăn” vào paracosm và giải quyết hai khoảng trống logistics, cho thấy The Kingdom có xu hướng **hấp thụ mọi structured interest như R&D**.

---

# 8. The Academy / Concept Engine — genealogy

## 8.1. Đây không phải một engine được thiết kế sạch từ đầu

[SOURCE: `engine_genealogy_and_development.md`]

Genealogy được formalize như một quá trình nhiều năm:

```text
cultural exposure
→ idea trigger
→ simulation
→ worldbuilding
→ reuse
→ remake
→ engine
→ meta engine
→ AI formalization
```

Nguồn ảnh hưởng gồm:

- phim;
- truyện;
- anime/manga;
- tokusatsu;
- forum/community;
- event;
- lucid dream;
- worldbuilding cá nhân;
- OC;
- nhiều lần remake/restructure.

AI xuất hiện **muộn**, không phải nguồn gốc của tư duy engine.

---

## 8.2. Hai thủy tổ lớn

[SOURCE]

### The One

Ảnh hưởng chính:

- structured multiverse;
- travel giữa reality;
- multiverse policing;
- jurisdiction;
- arrest thay vì chỉ annihilation;
- tội phạm xuyên reality như vấn đề có tổ chức/pháp lý.

### Đội đặc nhiệm thời gian

Ảnh hưởng chính:

- spec ops;
- time travel;
- dark sci-fi;
- thí nghiệm / tẩy não / huấn luyện khắc nghiệt;
- con người như resource;
- lịch sử/thời gian như operational space.

Hai nguồn này dẫn đến **Multiverse Police**.

---

## 8.3. Multiverse Police → The Academy

[SOURCE]

Multiverse Police từng có:

- Earth như gateway hub;
- anomaly / criminal / outsider xuyên multiverse/time;
- lực lượng bảo vệ Earth;
- self-insert đứng đầu spec ops;
- science + magic tồn tại cùng nhau.

Cấu trúc ban đầu dính chặt:

```text
creator
+ self-insert
+ world lore
+ organization
+ mechanism
```

Quá trình lâu dài là tháo dần scaffolding:

```text
self-insert
→ Earth guard
→ organization with function
→ less dependency on central character
→ creator separated from in-world role
→ engine
→ meta engine
```

The Academy là hậu duệ trực tiếp chứ không phải remake sạch.

---

## 8.4. V1 → V2: chuyển từ reactive sang generative

[SOURCE]

### V1

```text
fiction host tạo MC/HIP
→ HIP bị đẩy tới
→ hệ thống đánh giá
→ cooperate: guest treatment
→ resist: arrest
→ attempt return
```

Hệ thống còn mang DNA cảnh sát và **phụ thuộc HIP ngoại sinh**.

### V2

```text
engine / Executor
→ tác động điều kiện
→ HIP được tạo / khuếch đại
→ HIP có agency
→ HIP tham gia history
```

Đây là bước engine thoát khỏi sự phụ thuộc vào fiction host phải tự sinh sẵn protagonist/anomaly.

---

## 8.5. Zero no Tsukaima và HIP agency

[SOURCE]

Checkpoint quan trọng là việc một HIP không nhất thiết phải chờ host triệu hồi.

Ý niệm phát triển:

```text
host creates/summons HIP
→ HIP gains cross-reality agency
→ HIP can find host
→ engine can create conditions for HIP to emerge
```

---

## 8.6. Greed có trước The Academy

[SOURCE]

Greed ban đầu là OC.

Sau đó Greed được convert thành narrative engine.

Cơ chế Greed đi xuyên reality để phát Ring làm lộ bài toán:

- authority;
- legitimacy;
- infrastructure;
- jurisdiction.

Câu hỏi không còn là “Greed đủ mạnh không?” mà là:

> **Điều gì hợp thức hóa quyền của Greed để đi qua fiction host khác và can thiệp?**

Chính áp lực này góp phần buộc The Academy tiến hóa.

---

## 8.7. Mahō Sensei Negima! và authority layer

[SOURCE]

Negima là checkpoint nổi bật trong giai đoạn V1.5 vì đưa ra hình ảnh:

```text
academy
+ magic society
+ entities
+ hierarchy
+ authority
+ organization larger than individual
```

Điều này cung cấp lời giải kiến trúc:

```text
individual does not need to be ultimate authority
→ belongs to larger system
→ system grants legitimacy / jurisdiction
→ individual can operate as narrative engine
```

Tên **The Academy** được giữ lại như **artifact lịch sử**, dù chức năng hiện tại đã vượt xa nghĩa “học viện”.

---

# 9. The Academy — đơn vị cơ bản

[SOURCE: `modular_engine_concept_anti_drift.md`]

Invariant trung tâm:

> **Complexity is relational, not hierarchical.**

Đơn vị cơ bản là **module**.

Module có thể là:

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

Module có thể mang các thuộc tính độc lập:

- Autonomous;
- Composable;
- Interoperable;
- Nested in lore;
- Operationally independent;
- Host-capable;
- Portable;
- Federatable.

**Không thuộc tính nào tự động suy ra thuộc tính khác.**

---

# 10. The Academy — ontology

## 10.1. Typed graph, không phải tree

[SOURCE]

Quan hệ phải giữ kiểu cạnh:

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

Không được collapse thành parent-child chung chung.

Một node có thể có vị trí khác nhau trong nhiều graph cùng lúc:

```text
Lore graph:
Faction A --BELONGS_TO--> The Kingdom

Simulation graph:
Faction A --CAN_RUN_WITHOUT--> Full Kingdom Simulation
```

Hai mệnh đề cùng đúng.

---

## 10.2. Autonomy là mặc định

[SOURCE]

Nếu source không xác nhận dependency:

> **mặc định module autonomous.**

Điều này đặc biệt quan trọng với engine.

Một engine có thể:

- giữ logic riêng;
- chạy standalone;
- có interface;
- áp vào nhiều host;
- sinh output khác nhau tùy host;
- không sở hữu host;
- không bị host sở hữu;
- không biến host thành subsystem chỉ vì dùng thường xuyên.

---

## 10.3. Composition là operation, không phải ontology

[SOURCE]

Ví dụ:

```text
Narrative Engine
+
The Academy
+
The Kingdom
```

có thể tạo một fiction line.

Nhưng không được suy ra:

```text
Narrative Engine contains The Kingdom
The Kingdom depends on Narrative Engine
The Academy is a subsystem of The Kingdom
```

Composition chỉ nói rằng module đã được cho tương tác trong configuration đó.

---

## 10.4. Federation

[SOURCE]

Khi nhiều simulation autonomous chạy cùng, trao đổi:

- state;
- actor;
- event;
- causal influence;

có thể xem cấu hình đó như **simulation federation**.

Federation:

- không xóa module boundary;
- không tạo permanent dependency nếu source không nói;
- có thể chỉ tồn tại trong một phiên / fiction line;
- có thể giải thể;
- có thể sinh emergent fiction không thuộc riêng module nào.

---

# 11. The Academy — runtime

[INFERENCE grounded in SOURCE]

Runtime tổng quát không phải một universal engine template. Wrapper chỉ tạo điều kiện để các implementation khác nhau được chứa và interoperable.

Mẫu khái quát tối thiểu:

```text
engine / concept
→ primitive / condition / rule / state
→ instantiate in configuration or host
→ actor/HIP/anomaly interaction
→ transition / feedback / paradox
→ causal trajectory
→ narrative consequence
```

Không được hiểu sơ đồ này như một template bắt buộc cho Greed, Sloth, Lust, Wrath.

---

# 12. The Academy — wrapper principle

[SOURCE: Wrath materials]

The Academy **không yêu cầu các engine có cùng internal structure**.

Greed, Sloth, Lust, Wrath có thể khác nhau hoàn toàn về:

- internal logic;
- flow;
- primitive;
- governor relation;
- state model;
- paradox;
- embodiment;
- failure state;
- narrative function.

Source nói thẳng:

> nếu tất cả engine dùng cùng một internal template, chúng chỉ là cùng một engine với skin khác nhau.

Điểm chung chỉ cần ở wrapper / interoperability layer.

Đây là một trong những triết lý nền tảng nhất của paracosm The Academy.

---

# 13. The Academy — các engine/concept đã đọc

## 13.1. Greed / The Ring

[SOURCE: `the ring.txt`, `Greed Paradox.txt`, `Greed Axe.txt`]

### The Ring

The Ring không phải power-up thông thường.

Mục đích là tạo **một trải nghiệm trọn đời** cho một người.

Protocol:

```text
Greed chọn người
→ trao Ring
→ người nhận được lợi ích
→ sống cùng Ring phần lớn đời
→ đạt thành công / biến đổi
→ Greed quay lại
→ người nhận phải tự nguyện tháo và trả
```

Điều kiện tuyệt đối:

> **người sở hữu phải tự nguyện tháo Ring và trao trả.**

Nếu từ chối:

```text
refusal
→ combat
→ if Greed wins
→ Greed does not reclaim Ring
→ Greed crushes Ring
```

Lý do:

> nếu phải thu hồi bằng bạo lực, Ring đã thất bại.

Thứ được “harvest” không phải Ring mà là:

- success;
- failure;
- choice;
- ambition;
- betrayal;
- gratitude;
- growth;
- corruption;
- toàn bộ trải nghiệm độc nhất của đời người.

### Paradox of Greed

Greed “tham được cho”, không phải đơn giản tham cướp.

Founder trao vô hạn Ring → mỗi Ring là một trách nhiệm một đời → trong vô hạn người sẽ có người từ chối → người giữ Ring có thể đạt Á Thần → refusal có thể tạo trận chiến cấp rất cao.

Feedback loop:

```text
Infinite Rings
→ Infinite Responsibility
→ Infinite Lives cultivated
→ Infinite possibility of refusal
→ Infinite Battles
→ back to Infinite Rings
```

Greed có hai incentive xung đột:

- với tư cách Academy worker: muốn người nhận tự nguyện trả để hoàn thành responsibility/KPI;
- với tư cách Avatar of Greed: một phần lại muốn họ từ chối để được đánh với chính đối thủ mạnh mà mình nuôi cả đời.

Engine tự tạo mâu thuẫn nội tại thay vì cần plot bên ngoài bơm conflict.

### Greed II / weapon concept

Greed II là avatar backup của Greed I về sau trở thành cá thể độc lập.

Core concept vũ khí không nằm ở “Greed mạnh”, mà ở **một gia đình năm servant trở thành cùng một weapon identity**, với ba form và internal disagreement có thể làm suy giảm fusion.

Các form được phát triển bằng simulation/method acting qua nhiều năm, không phải một lần brainstorming.

Điểm này minh họa phương pháp:

```text
simulation
→ embodied observation
→ pattern
→ stable design
→ later formalization
```

---

## 13.2. Sloth

[SOURCE: Sloth / Accommodation / Graze / The Gun]

Sloth là Executor với job hiện tại:

> **Regressors Hunter**

Core Drive không được hiểu bằng định nghĩa Seven Deadly Sins truyền thống.

Các module hiện thấy:

### HIP

Regressor được xem là một dạng **Historical Influence Potential** cao.

Sloth không săn “người yếu”; mục tiêu là anomaly có khả năng thay đổi lịch sử ở quy mô đáng kể.

### Accountability

Counter buộc Sloth hoàn thành trách nhiệm Executor mà không làm Sloth đổi bản chất.

### Accommodation

Catalyst / interface.

Accommodation đại diện cho quyền một thực thể được tiếp tục tồn tại ngoài tiến trình bình thường, do authority nào đó cho phép.

Nó có thể map các fiction mechanism như:

- regression cost;
- World Will / Thiên Đạo permission;
- authority-granted continuation.

Paradox:

> chính catalyst liên tục tạo điều kiện cho loại Regressor mà Sloth phải săn.

### Graze

Doctrine tối thiểu hóa unnecessary interaction:

> **Move only when movement is the cheapest path to completion.**

Flow:

```text
Observe
→ Graze
→ Decisive action
→ Return to rest
```

### The Gun

Tool cố tình generic.

Mục tiêu:

> shortest path between obligation and completion.

Flow điển hình:

```text
Observe
→ Graze
→ Fire
→ Duty discharged
```

Sloth cho thấy engine có thể được phân rã thành:

```text
role
+ target class
+ counter
+ catalyst
+ doctrine
+ tool
+ paradox
```

nhưng **không được suy ra đây là template bắt buộc cho mọi engine khác**.

---

## 13.3. Lust

[SOURCE: `Lust_Working_Draft.md`]

Lust là Executor với job:

> **Nurturer of a Single Historical Influence Potential (HIP).**

Core Drive:

- khao khát chứng kiến một cá thể trưởng thành;
- đầu tư toàn bộ thời gian/resource vào đúng một HIP;
- không đổi đối tượng sau khi đã chọn.

Paradox:

- bản chất muốn possess/protect;
- nhưng role Executor không cho phép giải quyết mọi vấn đề thay HIP;
- càng muốn giữ càng phải học cách buông;
- càng đủ sức bảo vệ càng phải kiềm chế.

Counter: **Nurture**.

Doctrine: **Judgment**.

Core principle:

> **Know when to intervene. Know when to refrain.**

Điểm này tiếp tục chứng minh The Academy không định nghĩa “Sin” theo nghĩa truyền thống mà xây mỗi one thành operational concept riêng.

---

## 13.4. Wrath

[SOURCE: Wrath materials]

Wrath là ví dụ mạnh nhất chống việc ép engine vào template chung.

Type:

> **Hybrid Narrative Engine / Entity**

Wrath đồng thời là:

- narrative engine;
- entity / character;
- tragic antagonist trong *The Tainted Cosmos*;
- HIP theo The Academy;
- thực thể có thể là con chiên hoặc phản đồ tùy context.

Core components:

- **Deus** — vừa giữ nghĩa God thần học, vừa có referent ontological cụ thể trong *The Tainted Cosmos*.
- **Si** — stabilizer, giữ mệnh đề “Deus me relinquit” ở conditional state.
- **Forsaken** — governor.
- **Wrath** — failure state sau collapse.

Minimal runtime:

```text
DEUS
→ silence / action / non-response
→ "Si Deus me relinquit..."
→ SI keeps condition open
→ inquiry: "Why?"
→ reconsideration loop OR collapse
→ FORSAKEN becomes certainty
→ WRATH emerges as failure state
```

Invariant nén:

> **Wrath chỉ còn ổn định khi chữ “Si” vẫn tồn tại.**

Khi `Si` còn:

```text
Có thể ta đã bị Forsaken.
Nhưng tại sao?
Có thật vậy không?
```

Khi `Si` sụp:

```text
Ta đã bị Forsaken.
```

Một question trở thành verdict.

Wrath chứng minh wrapper philosophy: internal engine có thể là state-machine / inquiry-collapse structure hoàn toàn khác Greed hoặc Sloth mà vẫn hợp lệ trong cùng architecture.

---

# 14. The Academy — triết lý

[SOURCE + INFERENCE]

Triết lý cốt lõi có thể nén thành:

> **Lore và story là implementation/output; engine mới là đơn vị cần giữ identity.**

Wrath source nói rõ narrative-engine approach không ưu tiên:

- lore dump;
- full history;
- timeline;
- geography;
- exposition;
- audience interpretation.

Ưu tiên:

- primitive;
- condition;
- governor;
- stabilizer;
- state;
- transition;
- relation;
- failure mode;
- simulation capability.

Một formulation trong discussion source:

```text
Narrative Engine
→ primitive
→ governor
→ state
→ transition
→ interaction
→ simulation
```

Lore/story không phải core và có thể thay bằng host khác nếu engine cho phép.

Không được biến formulation này thành template phổ quát; nó chỉ minh họa engine-oriented thinking.

---

# 15. The Academy — Historical Influence Potential (HIP)

[SOURCE]

HIP không bị khóa thành:

- MC;
- chosen one;
- regressor;
- isekai person;
- powerful fighter.

Định nghĩa chức năng:

> **Historical Influence Potential là tiềm năng một cá nhân, entity, anomaly hoặc system có thể tác động lên tiến trình lịch sử.**

“Potential” và “Influence” được giữ mở để từng engine gán criteria riêng.

HIP là primitive cho phép The Academy làm việc ở tầng trước story:

```text
not "who is the protagonist?"
but
"what has enough potential to alter historical trajectories?"
```

---

# 16. The Academy — lucid dream như simulation substrate lịch sử

[SOURCE]

Lucid dream từng đóng vai trò rất lớn, đặc biệt khoảng 12–25 tuổi và tiếp tục có vai trò đến khoảng 30 tuổi.

Method:

```text
idea
→ keyword anchor
→ carry into lucid dream
→ run / simulate
→ observe
→ keep / revise / discard
```

Đặc biệt được dùng để thử trực giác về:

- time travel;
- grandfather paradox;
- multiple timelines;
- space-time domain breaking;
- interactions giữa các tầng reality.

Mục tiêu không phải physical accuracy tuyệt đối, mà là **intuitive simulation**.

Từ khóa đóng vai trò retrieval key cho cluster trải nghiệm/concept lâu năm.

Điều này hỗ trợ nguyên tắc:

> **simulation first, abstraction later.**

---

# 17. The Kingdom và The Academy: bảng so sánh kiến trúc

| Trục | The Kingdom | The Academy / Concept Engine |
|---|---|---|
| Đơn vị trung tâm | World-state | Engine / concept / module |
| Hình thái hệ | Persistent world | Typed relational graph / engine ecology |
| Runtime chính | State transition theo lịch sử | Causal mechanism / composition / trajectory |
| Input điển hình | Existing world state + event | Engine + conditions + host/configuration |
| Output điển hình | New world state | Emergent trajectory / actor change / narrative consequence |
| Tính tích lũy | Historical continuity | Reusable mechanism identity + relation history |
| Path dependence | Rất cao | Tùy engine/configuration; không phải universal |
| Actor | Embedded trong world và history | Có thể được generated/selected/nurtured/hunted hoặc imported qua interface |
| Membership | Lore/world membership có trọng lượng lớn | Autonomy mặc định; membership và simulation dependency tách nhau |
| Composition | Thường là tương tác giữa thành phần của world | First-class operation giữa module/host/engine |
| Portability | World chạy standalone; faction có thể zoom-run | Engine có thể portable qua host khi source cho phép |
| Main coherence test | "Có khớp lịch sử/state trước-sau không?" | "Engine có giữ identity/rules/interface khi chạy không?" |
| Lỗi LLM nguy hiểm | Continuity corruption | Ontology/module collapse |
| Typical externalization | State, institution, timeline, social response, infrastructure | Primitive, rule, paradox, interface, typed edge, state machine |
| Narrative | Cửa sổ quan sát world-history | Output/consequence của engine simulation |
| Triết lý | World must react as a system | Mechanism must remain reusable and internally distinct |

---

# 18. Khác biệt runtime: “chuyển chế độ mô phỏng”

[INFERENCE]

Việc người tạo chán một paracosm rồi chuyển sang paracosm kia không chỉ là đổi topic.

## Khi chạy The Kingdom

Mental operations thiên về:

- giữ nhiều state;
- nhớ historical inheritance;
- tính reaction across institutions;
- tracking actor knowledge;
- delay / normalization;
- causal consequence;
- regression testing timeline.

Câu hỏi điển hình:

> “Nếu mở thương mại ở CP1 thì hai năm sau CP2, tầng dân cư X, agency Y và nước láng giềng Z đang ở trạng thái nào?”

## Khi chạy The Academy

Mental operations thiên về:

- define engine boundary;
- tìm primitive;
- nhận diện paradox;
- giữ portability;
- test host compatibility;
- relation typing;
- composition;
- failure state;
- emergent trajectory.

Câu hỏi điển hình:

> “Nếu catalyst này tồn tại, nó tạo đối tượng nào, paradox nào tự sinh, và engine còn giữ identity khi đổi host không?”

Vì vậy đây là **mode switch**:

```text
The Kingdom = stateful historical runtime
The Academy = modular causal-engine runtime
```

Một bên mệt vì state/history. Một bên mệt vì abstraction/interface.

Chuyển qua lại có thể thay đổi loại cognitive load.

---

# 19. Hai paracosm có thể tương tác nhưng không được merge ontology

[SOURCE: anti-drift]

Một fiction line có thể cho:

```text
Meta/Narrative Engine
→ generates/selects HIP
→ HIP enters The Kingdom through interface
→ Kingdom citizens/factions/institutions/environment react
```

Nhưng đây chỉ là **interaction graph**.

Không được suy ra:

```text
The Academy contains The Kingdom
The Kingdom is a subsystem of The Academy
The Kingdom depends on The Academy
```

The Kingdom có thể standalone.

The Academy/engines có thể standalone.

Một composition không làm hai paracosm trở thành một ontology.

---

# 20. Failure mode khi LLM xử lý hai paracosm cùng lúc

## 20.1. Cross-paracosm contamination

[INFERENCE]

Model có thể thấy cùng người tạo, cùng chữ “engine”, cùng actor hoặc một lần crossover rồi trộn logic hai bên.

### Lỗi hướng Kingdom → Academy

- ép engine thành lore tree;
- bắt mọi engine cần worldbuilding đầy đủ;
- hỏi geography/history khi engine không cần;
- coi host là canonical home;
- biến engine portable thành setting-specific character.

### Lỗi hướng Academy → Kingdom

- modularize quá mức một world history thành detachable components;
- coi institution như plug-in;
- bỏ qua path dependence;
- đổi causal history thành parameterized simulation;
- coi unknown historical state như slot để generate.

Cả hai đều phá paracosm.

---

## 20.2. Generic LLM failure modes đã được người tạo phải phòng trước

[USER-PROVIDED + SOURCE]

- thấy UNKNOWN → tự lấp;
- thấy proposal plausible → dần nâng thành canon;
- thấy contradiction → tự bịa lore để rationalize;
- thấy hai module đi cùng → suy ra dependency;
- thấy interaction → suy ra containment;
- thấy complex graph → giản lược thành tree;
- thấy fiction → tự sinh drama/MC-centric arc;
- thấy state-level conflict → làm mềm thành reconciliation;
- thấy strong individual → làm institution ngu để tạo power fantasy;
- knowledge leakage giữa actor;
- context dài → drift definition;
- summary → mất provenance;
- repeated mention → proposal contamination.

---

# 21. Behavior engineering: tại sao nó trở thành bắt buộc

[USER-PROVIDED]

Người tạo bắt đầu sử dụng AI chủ yếu để làm worldbuilding/paracosm, **không phải vì behavior engineering thú vị**.

Nhưng vì failure mode của LLM có thể phá externalized canon, phải thiết kế trước một behavioral firewall.

Riêng **The Kingdom CI đã dài khoảng 8.000 ký tự**.

Behavior engineering ở đây không chỉ là “tone prompt”. Nó phải quy định:

- được suy luận khi nào;
- nguồn nào ưu tiên;
- epistemic state;
- actor knowledge;
- prohibited inference;
- canon mutation rules;
- handling contradiction;
- handling unknown;
- relation typing;
- anti-drift;
- anti-rationalization;
- conditions for productive divergence.

[INFERENCE]

Đây gần **defensive programming / requirements engineering cho một cognitive tool không deterministic** hơn prompt styling thông thường.

---

# 22. Epistemic typing và anti-drift kernel

[SOURCE]

Các trạng thái cần giữ riêng khi distinction có ý nghĩa:

- **CANON**
- **USER-PROVIDED STATE**
- **INFERENCE**
- **PROPOSAL**
- **HYPOTHETICAL / BRANCH**
- **UNKNOWN**

Canon mutation hợp lệ:

```text
CANON
→ analysis / simulation / proposal
→ WORKSPACE
→ human evaluation / paracosm simulation
→ accept / reject / branch / relayer
→ CANON if explicitly confirmed
```

Không hợp lệ:

```text
proposal
→ plausible prose
→ assumed canon
```

Khi contradiction:

1. chỉ ra contradiction;
2. xác định premise xung đột;
3. giữ nhiều khả năng nếu evidence chưa phân biệt;
4. proposal giải pháp phải gắn nhãn.

Không tự bịa C để cứu A và B.

---

# 23. Externalization: hai paracosm cần hai chiến lược khác nhau

## 23.1. The Kingdom

[INFERENCE]

Externalization gần với:

> **decompression / reverse engineering của một lịch sử đã tồn tại trong paracosm nội tại.**

Công việc trọng tâm:

- kéo implicit state ra ngoài;
- ghi historical continuity;
- formalize institution;
- build interfaces;
- preserve causal history;
- giữ actor knowledge;
- tạo observable diegetic channels;
- regression-test khi retcon.

Rủi ro lớn:

> external tool tưởng “chưa ghi” = “chưa tồn tại” rồi generate sai.

---

## 23.2. The Academy

[INFERENCE]

Externalization gần với:

> **formalization của engine identity và relational architecture đã được mô phỏng/tiến hóa lâu năm.**

Công việc trọng tâm:

- tìm primitive;
- đặt boundary;
- tách lore khỏi mechanism;
- giữ portability;
- define state / transition;
- identify paradox;
- type relation;
- maintain provenance;
- test composition;
- giữ diversity giữa engine implementations.

Rủi ro lớn:

> external tool ép mọi engine vào một ontology/template để “dễ hiểu”, làm mất identity.

---

# 24. The Kingdom và The Academy đều không bắt đầu từ AI

[SOURCE + USER-PROVIDED]

Điểm cần nói rõ cho LLM mới:

- AI **không tạo ra hai paracosm**.
- AI xuất hiện ở giai đoạn muộn để externalize, refine, formalize và build supporting infrastructure.
- Nhiều structure đã tồn tại trước khi có tên kỹ thuật.
- Với The Academy, simulation và lucid dream từng đi trước abstraction.
- Với The Kingdom, history/world logic đã tồn tại trước các tài liệu formal hiện tại.

Do đó không được đọc tài liệu mới rồi suy rằng thứ nào “chỉ mới tồn tại khi được viết xuống”.

---

# 25. Sáu tháng học AI: infrastructure tax của paracosm

[USER-PROVIDED]

Người tạo mô tả xuất phát điểm là **gần như từ số 0 về AI**, trong khi mục tiêu chính chỉ là worldbuilding.

Trong khoảng **6 tháng**, đồng thời phải học:

## 25.1. Behavior engineering

Mục tiêu:

- ngăn LLM phá canon;
- kiểm soát drift;
- giữ ontology;
- phân tách proposal/inference/canon;
- xử lý context dài.

Đây không phải phần “vui” của hobby mà là chi phí bắt buộc để công cụ đủ an toàn.

## 25.2. SD.Next trên AMD

Mục tiêu:

- local image generation / visual externalization.

[USER-PROVIDED]

Việc cấu hình SD.Next trên AMD được mô tả như một **“hell thứ 2”**.

Chi phí đến từ ecosystem không thuận lợi bằng đường CUDA/NVIDIA, khiến một người chỉ muốn tạo visual phải đụng vào backend, compatibility, driver/runtime và performance issues.

## 25.3. LM Studio

Mục tiêu:

- chạy local LLM;
- thử model;
- kiểm soát inference/context tốt hơn;
- giảm phụ thuộc hoàn toàn vào cloud model.

## 25.4. Obsidian + RAG

Mục tiêu ban đầu gần như:

> “cho AI đọc được kho ghi chú/paracosm”.

Nhưng RAG kéo theo:

- chunking;
- metadata;
- provenance;
- retrieval strategy;
- stale version;
- canon/proposal separation;
- retrieval error.

Đối với paracosm, retrieval sai không chỉ là QA sai; nó có thể tạo **canon contamination**.

## 25.5. Codex + local apps

Khi Markdown/wiki không đủ để thao tác complexity, người tạo bắt đầu dùng Codex để build app hỗ trợ:

- quản lý state;
- xem relation;
- hỗ trợ workflow;
- externalize UI;
- giảm manual cognitive burden.

---

# 26. Điều người tạo đã trải qua

[USER-PROVIDED + SOURCE]

## 26.1. Trước AI

- paracosm đã tồn tại lâu năm;
- concept phát triển bằng daydreaming, simulation, lucid dream, media influence, forum/community, OC, remake;
- nhiều concept tồn tại dưới dạng intuitive structure trước khi có formal name;
- The Kingdom và The Academy đã phát triển theo hai philosophy khác nhau.

## 26.2. Khi bắt đầu externalize bằng AI

Ban đầu AI được kỳ vọng là cognitive assistant.

Rất nhanh xuất hiện failure modes:

- fill blank;
- genre prior;
- canon drift;
- hierarchy bias;
- proposal contamination;
- moral smoothing;
- MC-centric narrative;
- continuity break.

Kết quả: phải học behavior engineering dù không có hứng coi nó là hobby.

## 26.3. Toolchain phình ra

Một nhu cầu kéo theo một lớp kỹ thuật:

```text
worldbuilding
→ LLM
→ behavior control
→ local LLM
→ RAG
→ image generation
→ knowledge management
→ custom apps
```

Người tạo không đi theo curriculum AI chuẩn.

Flow thực tế:

```text
paracosm problem
→ find tool
→ tool fails / is insufficient
→ learn enough technical layer to control it
→ discover next failure mode
→ build more infrastructure
```

---

# 27. Điều người tạo đang trải qua

[USER-PROVIDED + INFERENCE]

Hiện tại công việc không còn là “viết lore”.

Nó gồm đồng thời:

- externalization;
- reverse engineering nội dung trong đầu;
- formalization;
- ontology management;
- provenance;
- regression reasoning;
- behavior engineering;
- RAG / retrieval design;
- tool building;
- UI/wiki/frontend;
- model selection / local inference;
- visual externalization.

Một phần lớn cognitive load hiện nay đến từ **hạ tầng phục vụ hobby**, không phải hobby itself.

The Kingdom và The Academy còn yêu cầu hai profile LLM khác nhau vì failure modes khác nhau.

---

# 28. Những gì có khả năng sắp phải đối diện

**[INFERENCE / FORESEEABLE PRESSURES — không phải canon hay dự đoán chắc chắn]**

Dựa trên kiến trúc hiện tại, các pressure kỹ thuật sau có khả năng tăng khi externalization tiếp tục.

## 28.1. Tách common behavioral kernel khỏi paracosm-specific CI

Nhiều rule hiện nay là cross-paracosm:

- UNKNOWN ≠ EMPTY;
- proposal ≠ canon;
- source priority;
- anti-rationalization;
- provenance;
- no silent mutation;
- no ontology collapse.

Trong khi runtime-specific rule khác nhau:

- Kingdom: continuity / state / actor knowledge / path dependence;
- Academy: autonomy / typed edge / portability / wrapper diversity.

Nếu tất cả bị copy vào từng CI, maintenance cost có thể tăng nhanh.

## 28.2. Cross-paracosm retrieval isolation

RAG chung có nguy cơ lấy đúng semantic keyword nhưng sai paracosm/runtime.

Ví dụ chữ “engine”, “authority”, “state”, “actor” có thể mang nghĩa khác theo context.

Do đó retrieval cần giữ mạnh:

- paracosm identity;
- source provenance;
- epistemic type;
- version;
- module/host scope.

## 28.3. Canon regression testing

The Kingdom càng externalize nhiều càng cần biết:

> thay đổi X ảnh hưởng checkpoint/module nào downstream?

The Academy càng nhiều engine càng cần biết:

> đổi primitive/interface X phá host compatibility hoặc engine identity nào?

Hai dạng regression khác nhau.

## 28.4. Toolchain maintenance

SD.Next, local model, RAG, Codex app, UI và model behavior đều có version drift riêng.

Hobby có nguy cơ sinh một “maintenance layer” đủ lớn để cạnh tranh thời gian với actual paracosm work.

## 28.5. Context architecture

Một paracosm có thể vượt xa context window hữu dụng của một chat.

Do đó likely direction là:

```text
root provenance
→ project-specific kernel
→ module-specific source
→ retrieved working set
→ temporary branch/workspace
→ human/paracosm validation
```

Điều này phù hợp với architecture đang hình thành nhưng không nên tự động xem là canon workflow nếu người tạo chưa chốt.

---

# 29. Vì sao “chán bên này thì chạy sang bên kia” thực sự có tác dụng

[USER-PROVIDED + INFERENCE]

Người tạo nói nếu chán một trong hai thì chỉ cần chạy sang bên kia.

Điều này hợp cấu trúc vì hai bên sử dụng tải nhận thức khác nhau.

## The Kingdom fatigue

Có thể đến từ:

- historical state overload;
- institution design;
- social causality;
- infrastructure;
- regression burden.

Chuyển sang The Academy sẽ đổi sang:

- abstract mechanism;
- paradox;
- engine boundary;
- portability;
- composition.

## The Academy fatigue

Có thể đến từ:

- abstraction;
- ontology;
- relation typing;
- engine formalization;
- interface design.

Chuyển sang The Kingdom sẽ đổi sang:

- lived society;
- history;
- media;
- physical infrastructure;
- state behavior;
- concrete institutional consequence.

Đây là **cognitive mode switching**, không chỉ genre switching.

---

# 30. Một khác biệt rất quan trọng: thứ gì được coi là “artifact lịch sử”

## The Kingdom

[USER-PROVIDED]

Các stage cũ, actor cũ hoặc world structure cũ có thể tồn tại như lịch sử của cùng paracosm. Immortal King từng là main actor nhưng không cần phải là organizing center hiện tại.

## The Academy

[SOURCE]

Tên “The Academy” itself được giữ như **artifact lịch sử** của giai đoạn chịu ảnh hưởng academy/magic society, dù current function đã thành meta-engine wrapper rộng hơn.

Greed cũng mang genealogy riêng:

```text
Greed OC
→ conversion pressure
→ contributes to Academy authority problem
→ later becomes narrative engine / Executor relation
```

Do đó genealogy không phải một clean tree.

---

# 31. The Kingdom từng là một ví dụ “engine → decomposition → worldbuilding”

[SOURCE: `engine_genealogy_and_development.md`]

Một chi tiết rất quan trọng kết nối hai paracosm mà không merge chúng:

The Kingdom từng được mô tả như:

```text
engine
→ decomposition
→ worldbuilding
→ modularize again
→ diegetic fiction
```

Base engine ban đầu bị phân rã, phần còn lại trở thành worldbuilding cụ thể.

Cơ chế thể hiện chuyển sang:

- in-world vlog;
- travel guide;
- artifact;
- diegetic experience.

Điểm này cho thấy cùng một người tạo có thể phát triển hai paracosm từ shared historical habits, nhưng để chúng **phân kỳ thành hai ontology/runtime rất khác**.

Không được suy rằng vì có chung ancestry về tư duy engine nên The Kingdom hiện là subsystem của The Academy.

---

# 32. Common substrate nhưng different operating systems

[INFERENCE]

Hai paracosm vẫn có một số substrate chung ở cấp người tạo:

- simulation-first tendency;
- long-term continuity;
- retcon/remake;
- sensitivity to logical consistency;
- reuse of external references;
- preference for mechanism over superficial trope;
- willingness to externalize bằng artifact/tool;
- resistance to LLM average priors.

Nhưng substrate chung **không xóa runtime difference**.

Analogy phù hợp:

```text
same hardware / imagination substrate
↓
OS A: The Kingdom
OS B: The Academy
```

OS A quản world-state/history.

OS B quản engine/module/causal composition.

---

# 33. Những điều LLM mới tuyệt đối không được làm

## 33.1. Với The Kingdom

Không được:

- coi unknown note như blank worldbuilding space;
- tự thêm lore để “hoàn thiện setting”;
- ép narrative về protagonist;
- làm institution ngu để tạo payoff;
- bỏ qua state inheritance;
- làm actor biết thông tin không có channel;
- retcon quá khứ mà không audit downstream;
- dùng generic fantasy prior thay source.

## 33.2. Với The Academy

Không được:

- ép Greed/Sloth/Lust/Wrath vào một template;
- collapse graph thành hierarchy;
- suy interaction = containment;
- suy repeated use = dependency;
- coi host là owner của engine;
- coi engine là owner của host;
- biến implementation lore thành engine invariant;
- coi narrative output là engine definition;
- tự invent relation để graph “đẹp hơn”.

## 33.3. Với cả hai

Không được:

- proposal → canon;
- inference → fact;
- contradiction → invented lore;
- summary → provenance loss;
- simplify ontology chỉ vì muốn câu trả lời dễ đọc.

---

# 34. Cách một LLM nên trả lời khi làm việc với người tạo

[INFERENCE grounded in behavior requirements]

## Khi người tạo cung cấp objective claim về architecture

- audit source nếu source tồn tại;
- không mở đầu bằng validation rỗng;
- tách observation / inference / assumption / conclusion.

## Khi source thiếu

Giữ `UNKNOWN`.

Nếu phải tiếp tục:

- dùng assumption tối thiểu;
- gắn nhãn;
- không merge vào canon.

## Khi phát hiện contradiction

Nêu contradiction và premise.

Không tự cứu bằng lore.

## Khi đưa proposal

Proposal phải rõ là workspace / branch.

## Khi giải thích

Giảm độ khó câu chữ, **không giảm relational complexity**.

---

# 35. Kết luận kiến trúc

## The Kingdom

[INFERENCE]

Có thể mô tả ngắn nhất là:

> **Một paracosm dạng stateful, path-dependent historical world simulation, nơi world-state và lịch sử tích lũy là organizing center; nhân vật và media hoạt động như các camera/sensor cục bộ để quan sát hệ thống.**

## The Academy / Concept Engine

[INFERENCE]

Có thể mô tả ngắn nhất là:

> **Một paracosm dạng modular causal-engine ecology, nơi các engine/concept tự trị được giữ bằng typed relations, có thể composition/federate/port qua host và sinh historical/narrative trajectories mà không cần chia sẻ cùng internal template.**

## Khác biệt nền tảng

```text
THE KINGDOM
asks:
"What does this world become after this event?"

THE ACADEMY
asks:
"What trajectories can this mechanism generate under these conditions?"
```

Một bên tích lũy **history**.

Một bên tích lũy **history-generating mechanisms**.

Hai bên có thể tương tác, nhưng không được merge ontology.

---

# 36. Điều sẽ falsify hoặc buộc sửa phân tích này

Để tránh biến analysis thành canon, các kết luận trên phải được sửa nếu xuất hiện source cho thấy:

1. **The Kingdom** không thật sự được định hướng systemic từ đầu mà world autonomy chỉ xuất hiện rất muộn.
2. **Immortal King** là causal center tuyệt đối chứ không chỉ main actor/viewpoint của early phase.
3. The Kingdom current runtime không còn path-dependent/world-state-centric như mô tả.
4. **The Academy** thực ra có một universal internal template bắt buộc mọi engine phải tuân theo.
5. Engine không portable/autonomous như anti-drift source hiện định nghĩa.
6. Composition thực ra tạo permanent ontology/dependency trong những trường hợp đang được mô tả là optional.
7. HIP có một định nghĩa đóng/chặt hơn source hiện tại.
8. Greed/Sloth/Lust/Wrath về sau được retcon đến mức examples hiện tại không còn đại diện cho architecture.
9. Người tạo chốt một workflow externalization khác với phần “foreseeable pressures” ở trên.

---

# 37. Source provenance đã dùng

## File trực tiếp

- `engine_genealogy_and_development.md`
- `modular_engine_concept_anti_drift.md`
- `the ring.txt`
- `Greed Paradox.txt`
- `Greed Axe.txt`
- `Accommodation_Working_Draft.md`
- `Graze_Doctrine_Working_Draft.md`
- `Sloth_Working_Draft.md`
- `The_Gun_Working_Draft.md`
- `Lust_Working_Draft.md`
- `Wrath_Working_Draft.md`
- `Wrath_Engine_Discussion_Transcript.md`
- `Historical_Influence_Potential.md` (tên file được cung cấp; định nghĩa HIP cũng được phản ánh trong genealogy và các engine draft)

## User-provided conversation state quan trọng

- The Kingdom trước khi biết từ paracosm được gọi là **Imagination Sphere**.
- The Kingdom ban đầu giả định một quốc gia hoàn hảo và outside world muốn chen chân vào.
- The Kingdom ngay từ đầu đã system-oriented; early main actor là **The Immortal King đi vi hành**.
- Current organization chuyển mạnh sang world/history as actor.
- Checkpoint model, CP1 mở thương mại và CP2 hostility/aggression cách nhau khoảng hai năm.
- Media/social sensors được dùng thay cho full NPC POV simulation.
- The Kingdom có neo-fantasy / high-tech / Type-II-scale infrastructure direction.
- Người tạo có tổng cộng ba paracosm phức tạp; tài liệu này chỉ xử lý hai cái đã có đủ dữ liệu.
- Có thể chuyển từ một paracosm sang cái kia khi chán vì chúng dùng hai mental runtime khác nhau.
- Trong khoảng sáu tháng từ gần số 0 về AI đã đồng thời học behavior engineering, SD.Next trên AMD, LM Studio, Obsidian-based RAG và Codex để build local support apps.
- Riêng custom instructions của The Kingdom đã dài khoảng 8.000 ký tự.
- Behavior engineering không được làm vì vui; nó là infrastructure tax để LLM không phá externalized paracosm.

---

# 38. Handoff prompt ngắn cho LLM mới

Nếu cần nạp tài liệu này vào một LLM khác, có thể dùng instruction tối thiểu sau:

```text
You are working with two distinct paracosms created by the same person.

Do not merge their ontologies.

THE KINGDOM:
- Stateful, path-dependent historical world simulation.
- World-state/history is the current organizing center.
- Institutions, actors, media and infrastructure react to checkpoints.
- Unknown externalized information may already exist internally.
- Main risk: continuity corruption.

THE ACADEMY / CONCEPT ENGINE:
- Modular causal-engine ecology.
- Modules are autonomous by default.
- Relationships are typed edges, not an implicit hierarchy.
- Composition is an operation, not ontology.
- Engines may be portable across hosts.
- Greed, Sloth, Lust and Wrath do not share a mandatory internal template.
- Main risk: ontology collapse and definition drift.

GLOBAL RULES:
UNKNOWN ≠ EMPTY.
PROPOSAL ≠ CANON.
INTERACTION ≠ CONTAINMENT.
CO-OCCURRENCE ≠ DEPENDENCY.
Do not invent lore to repair contradictions.
Preserve provenance and epistemic type.
Simplify wording, not ontology.
```

---

# End state

Tài liệu này là **analysis/handoff snapshot**, không phải canon source của The Kingdom hay The Academy.

Nó phải được cập nhật khi source mới thay đổi architecture, genealogy hoặc runtime.
