# The Academy V1.5 — Architecture Baseline & Anti-Drift Reference

**Trạng thái:** `MIGRATION / PROVENANCE REFERENCE` sau soft migration M7.  
**Mục đích lịch sử:** mốc reconstruction được khóa ngày 2026-08-28; giữ nguyên nội dung để truy vết cách V1.5, V2 và hướng V2.5 từng được tổ chức trong baseline này.  
**Đường đọc mặc định hiện hành:** [V1.5 Architecture](The_Academy_V1_5_Architecture.md), [V1.5 Open Registry](The_Academy_V1_5_Open_Registry.md), [V2 Architecture](../V2/The_Academy_V2_Architecture.md), và [Academy Revise branch](../BRANCHES/The_Academy_V2_5_Revise_Branch.md).  
**Lưu ý:** việc hạ vai trò file này khỏi đường đọc mặc định không tự phủ định dữ kiện/provenance bên dưới; khi có khác biệt về trạng thái hiện hành, dùng nguồn scoped mới và Current State để định tuyến.  
**Ngày khóa bản:** 2026-08-28  

---

# 0. Phạm vi và quy tắc sử dụng

Tài liệu này không phải world bible hoàn chỉnh, không phải bản lore kể lại, và không phải permission để điền các khoảng trống của V1.5.

Nó có bốn nhiệm vụ:

1. khóa những gì hiện đã được xác nhận;
2. tách những invariant được phép dùng làm tham chiếu khỏi những invariant chỉ được phép xác nhận rằng chúng tồn tại;
3. giữ `UNKNOWN` và phần chờ xác nhận ở đúng trạng thái;
4. ngăn LLM dùng prior về school fiction, worldbuilding hoặc V2 để tái cấu trúc sai V1.5.

## 0.1. Epistemic labels

### `[CANON-REF]`
Canon có thể được dùng làm **ràng buộc và mốc tham chiếu** khi phục dựng/thiết kế tiếp.

### `[CANON-EXISTENCE-ONLY]`
Canon chỉ cho phép xác nhận **một sự kiện/thực thể/trường hợp có tồn tại hoặc đã xảy ra**.

Không được dùng nội dung đó để:

- suy ra cơ chế;
- suy ra tiêu chí;
- suy ra actor state;
- dựng ví dụ chi tiết;
- suy ra quan hệ mới;
- dùng làm dữ liệu tham chiếu cho một project khác.

### `[LEGACY-BASE]`
Chi tiết thuộc lore/cấu trúc cũ đã được người tạo đưa ra làm **base để tái thiết kế**, nhưng không mặc định rằng implementation cũ sẽ được giữ nguyên.

### `[LEGACY-LORE / AWAITING CONFIRMATION]`
Chi tiết lore gốc đã được nhớ lại nhưng **chưa được khóa lại** thành baseline hiện hành.

### `[WORKING]`
Cách biểu diễn tạm thời để giúp externalize structure. Không phải canon ontology.

### `[UNKNOWN]`
Chưa được externalize hoặc chưa được xác nhận.

```text
UNKNOWN ≠ EMPTY
UNKNOWN ≠ PERMISSION TO INVENT
```

### `[PROPOSAL]`
Phương án mới do quá trình thiết kế/AI đề xuất. Chỉ thành canon sau khi được người tạo chấp nhận.

---

# 1. Invariant chống drift cấp cao nhất

Các invariant từ [modular_engine_concept_anti_drift.md](../../12_ANTI_DRIFT/modular_engine_concept_anti_drift.md) áp dụng trực tiếp:

```text
COMPLEXITY IS RELATIONAL, NOT HIERARCHICAL.

INTERACTION ≠ CONTAINMENT
CO-OCCURRENCE ≠ DEPENDENCY
TEMPORARY COMPOSITION ≠ PERMANENT COUPLING
REPEATED USE TOGETHER ≠ SUBSYSTEM STATUS
GENEALOGY ≠ CURRENT HIERARCHY
PRESENTATION ORDER ≠ ONTOLOGY
LORE CONTAINMENT ≠ SIMULATION DEPENDENCY
UNKNOWN ≠ PERMISSION TO INVENT
PROPOSAL ≠ CANON
```

Mặc định:

```text
independent nodes
+ explicit typed edges
```

thay vì:

```text
implicit parent-child tree
```

---

# 2. The Academy V1.5 là gì?

## 2.1. Định nghĩa vận hành

**[CANON-REF]**

The Academy V1.5 là **miền causal thể chế trước tốt nghiệp** của The Academy.

Nó giữ phần mà hình thức học viện/institution bản thân là causal apparatus:

```text
HIP được chọn
→ recruitment / consent
→ The Academy
→ institutional Narrative Engines / factions
→ education + cross-civilization exposure + interaction
→ graduation
→ return to origin
→ V1.5 kết thúc
```

### Boundary bắt buộc

```text
RETURN TO ORIGIN
= V1.5 TERMINUS
```

Phần HIP tiếp tục sống, hành động, thay đổi lịch sử và có thể bị Narrative Engine hậu tốt nghiệp tiếp cận **không nằm trong active runtime của V1.5**.

---

## 2.2. V1.5 không phải school-worldbuilding thông thường

**[CANON-REF]**

The Academy từng là một concept có lore đầy đủ và thực sự hoạt động như một Academy xuyên không-thời gian. Quá trình formalization về sau bóc dần phần lore cụ thể, giữ causal architecture và nâng The Academy thành Meta-Engine.

Do đó:

```text
INSTITUTION
≠ decorative school skin
```

Một institutional factor/faction có thể chính là một Narrative Engine.

Ví dụ đã khóa trong handoff:

```text
Teaching
= Institution
+ Narrative Engine
```

---

# 3. Triết lý cốt lõi của V1.5

## 3.1. Engine sinh nội dung, không xây MC từ dưới lên

**[CANON-REF]**

The Academy không vận hành như worldbuilding truyền thống:

```text
world → society → institution → character → plot
```

Thay vào đó, người tạo chọn một actor/HIP từ Host Fiction, full OC hoặc scenario có sẵn rồi cho actor đó chạy qua engine:

```text
Host Fiction / OC / Scenario
→ user selects HIP
→ HIP enters The Academy
→ institutional engines alter conditions / exposure / relations
→ HIP acts with its own agency
→ simulation produces fanfiction / OC trajectory / scenario
```

The Academy không cần tự tạo protagonist.

---

## 3.2. HIP là common gateway, không phải universal metric

**[CANON-REF — source: [Historical_Influence_Potential.md](../../01_HIP/Historical_Influence_Potential.md)]**

HIP là **criteria-agnostic evaluation gateway**.

HIP tự thân không định nghĩa:

- thế nào là potential;
- thế nào là influence;
- magnitude nào đáng kể;
- historical change phải có hình thức gì;
- target nào đủ tiêu chuẩn.

```text
Context-specific criteria
→ HIP gateway
→ evaluate target
```

Không được biến HIP thành:

```text
power level
protagonist score
chosen-one marker
morality score
Regressor definition
```

---

## 3.3. HIP không đi qua curriculum tuyến tính chung

**[CANON-REF]**

HIP lựa chọn hoặc tương tác với các institutional factions theo:

- mục đích;
- sở thích;
- năng lực;
- tính cách;
- tham vọng;
- hoàn cảnh;
- agency của chính HIP.

Một thuộc tính không tạo routing bắt buộc.

Ví dụ nguyên tắc:

```text
"thích phép thuật"
≠ bắt buộc chỉ vào Faction Phép thuật

"giỏi võ"
≠ bắt buộc vào Faction Võ kỹ

"không thích bạo lực"
≠ bị cấm học võ
```

Traits tham số hóa simulation; chúng không phải bảng định tuyến cứng.

---

## 3.4. Institutional faction là một Narrative Engine đủ lớn để tự sinh chuyện

**[CANON-REF]**

Theo phép so sánh bằng ngôn ngữ đời thường:

> Mỗi institutional Narrative Engine/faction gần với **một trường đại học** nằm trong một đoàn thể lớn có nhiều trường đại học.

Theo phép so sánh với fiction truyền thống:

> Mỗi faction-engine gần với **một arc lớn**.

Nhưng:

```text
Faction Engine
≠ prewritten arc
```

Đúng hơn:

```text
Faction Engine
= causal system có khả năng sinh nhiều arc khác nhau
  khi các HIP khác nhau chạy qua
```

Mỗi faction phải có đủ causal depth để HIP có **một trajectory đáng kể để nói** trước khi chuyển sang faction khác.

---

## 3.5. Cross-HIP interaction là core causal source

**[CANON-REF — source: `OC Academy.txt`]**

HIP không chỉ học từ staff/teacher mà còn học và tương tác với HIP đến từ những thực tại khác.

```text
Institutional Engine
        │
  ┌─────┼─────┐
  ▼     ▼     ▼
HIP A  HIP B  HIP C
  └── peer interaction ──┘
```

Peer difference có thể tự tạo causal pressure mà không cần engine prewrite conflict.

---

## 3.6. Agency và outcome neutrality

**[CANON-REF]**

The Academy thay đổi điều kiện, tri thức, exposure và option space; nó không quyết định graduate sẽ trở thành loại người nào.

```text
engine changes conditions
→ HIP chooses / adapts / resists
→ outcome is not preselected
```

V1.5 kết thúc ở `return to origin`.

---

# 4. Lịch sử hình thành — genealogy, không phải current hierarchy

## 4.1. Nguồn phát triển lớn

**[SOURCE / GENEALOGY]**

Các checkpoint được ghi nhận trong [engine_genealogy_and_development_updated.md](../../06_ENGINE_GENEALOGY/engine_genealogy_and_development_updated.md):

```text
The One
+
Đội đặc nhiệm thời gian
→ Multiverse Police
→ giai đoạn V1 / cảnh sát không-thời gian
```

Các áp lực chuyển pha quan trọng:

```text
Zero no Tsukaima
→ HIP agency / khả năng actor tự vận hành xuyên host

Greed OC → Narrative Engine
→ phát sinh bài toán authority / legitimacy / jurisdiction

Mahō Sensei Negima!
→ academy / institution / larger authority structure
→ góp phần tạo V1.5
```

Tên `The Academy` được giữ như một artifact genealogy của giai đoạn học viện.

---

## 4.2. Từ lore-rich concept sang Meta-Engine

**[CANON-REF — user-confirmed]**

The Academy ban đầu là một concept có lore đầy đủ:

```text
cross-time / cross-reality Academy
+ recruitment
+ institutions
+ students
+ staff
+ physical/lore implementation
```

Sau đó:

```text
lore-rich Academy concept
→ strip specific lore
→ preserve causal architecture
→ The Academy as Meta-Engine
```

Do độ phức tạp quá lớn, cùng một engine được formalize thành hai miền trọng tâm:

```text
V1.5
→ pre-grad institutional causality

V2
→ post-grad Narrative Engine causality
```

Hai version không phải hai engine cạnh tranh và không được coi là độc lập tuyệt đối.

---

## 4.3. Development asymmetry

**[CANON-REF — user-confirmed]**

Trong khoảng hai thập kỷ, phần V2 được phát triển nhiều hơn đáng kể. V2 gần đây mới được formalize mạnh với hỗ trợ của ChatGPT.

V1.5 được đào lại trong 2026 vì AI hiện có khả năng hỗ trợ:

- externalize quan hệ chồng chéo;
- tạo proposal có nhãn;
- stress-test coverage;
- giữ state/unknown;
- giảm tải việc một người phải tự chạy quá nhiều branch trong đầu.

AI không phải nguồn gốc của paracosm hay engine logic.

---

# 5. Baseline tuyển HIP và cohort

## 5.1. Cơ cấu lore gốc dùng làm base tái thiết kế

**[LEGACY-BASE]**

Mỗi world/reality trong lore gốc có tối đa **10 HIP** được chọn theo cấu hình:

```text
1 dân thường
1 con thương nhân
2 hoàng gia / quốc gia, tối đa 6 hoàng gia trong world
2 thánh nữ / thánh tử
────────────────────────────────────
tối đa 10 HIP / world
```

Không được suy ra rằng các category này là định nghĩa HIP hoặc universal criteria của The Academy.

Chúng là **sampling structure của lore gốc**, được giữ làm base khi tái thiết kế.

---

## 5.2. Cohort / class

**[LEGACY-BASE]**

Trong lore gốc:

```text
3 worlds đồng thời
× tối đa 10 HIP / world
= tối đa 30 HIP / class/cohort
```

### Anti-collapse invariant

```text
COHORT / CLASS
≠ FACTION
≠ DEPARTMENT
```

Quan hệ chính xác giữa cohort, lecture hall, faction và department vẫn cần externalize.

---

## 5.3. Một world có thể được chọn nhiều lần

**[CANON-REF]**

```text
World X
├── recruitment cycle A → HIP set A
├── recruitment cycle B → HIP set B
├── recruitment cycle C → HIP set C
└── ...
```

Không suy ra:

- cùng một HIP được nhập học lặp lại;
- world phải được chọn lại theo chu kỳ cố định;
- số lần tối đa;
- tiêu chí trigger cho lần chọn tiếp.

Các điểm đó là `UNKNOWN`.

---

# 6. Consent, pass và compensation

## 6.1. Consent

**[CANON-REF]**

HIP có quyền không tham gia The Academy.

```text
Academy offer
→ ACCEPT / REFUSE
```

Recruitment không đồng nghĩa với cưỡng ép hoặc Academy ownership.

---

## 6.2. Pass

**[CANON-REF]**

HIP có thể **pass lượt cho người khác tối đa 1 lần/người**.

Cơ chế recipient cố tình để mở.

**[UNKNOWN BY DESIGN]**

- người nhận lượt là ai;
- có phải qua HIP evaluation lại không;
- có phải cùng social category không;
- recipient có thể từ chối hay pass tiếp không;
- slot xử lý thế nào nếu recipient không nhận.

Không được tự điền.

---

## 6.3. Compensation

**[CANON-REF]**

Nếu HIP còn người nhà và người nhà chấp nhận, người nhà có thể nhận bồi thường.

Cơ chế bồi thường **cố tình để mở**.

Không được tự biến nó thành:

- tuition;
- scholarship;
- salary;
- purchase contract;
- ownership compensation;
- fixed monetary system.

---

# 7. Time-space baseline

## 7.1. Academy nằm ngoài thời-không của world gốc

**[LEGACY-BASE]**

The Academy có temporal relation khác với world/reality gốc.

Tỷ lệ lore gốc dùng làm base:

```text
10 năm bên trong The Academy
=
1 năm ở world/reality gốc
```

Không được tự suy ra thời lượng khóa học bằng 10 năm.

---

## 7.2. Biological age

**[CANON-REF]**

Tuổi sinh học của HIP **không tăng** theo thời gian ở The Academy.

Không được tự suy ra:

- tuổi tâm lý không thay đổi;
- memory không tích lũy;
- fatigue không tồn tại;
- cơ chế sinh học/ma thuật cụ thể;
- thời lượng học bắt buộc.

---

# 8. Institutional architecture

## 8.1. Faction-level engine ecology

**[CANON-REF]**

V1.5 phải được phục dựng như một ecology các institutional Narrative Engine.

```text
THE ACADEMY V1.5
        │
        ├── Faction / Institutional Engine A
        │       ├── values
        │       ├── definitions
        │       ├── criteria
        │       ├── actors
        │       ├── internal departments
        │       ├── lecture / shared spaces
        │       └── HIP interactions
        │
        ├── Faction / Institutional Engine B
        │       └── different causal identity
        │
        └── Faction / Institutional Engine N
```

Mỗi faction không được mặc định dùng cùng internal schema.

---

## 8.2. Departments không tự động là Narrative Engine

**[CANON-REF / ANTI-DRIFT]**

```text
Faction
= may be Narrative Engine

Department inside faction
≠ automatically Narrative Engine
```

Department có thể là:

- specialization;
- teaching unit;
- interface;
- actor cluster;
- local configuration;
- hoặc một engine riêng nếu canon sau này xác nhận.

---

## 8.3. Teaching

**[CANON-REF]**

```text
Teaching
= Institution
+ Narrative Engine
```

Một hoặc nhiều teacher có thể là Narrative Actors của Teaching.

HIP/student tương tác với Teaching nhưng không mặc định là protagonist của Teaching Engine.

**[UNKNOWN]**

- primitive;
- criteria;
- state model;
- relation giữa teacher actors;
- relation với curriculum;
- relation với exams/placement;
- termination/failure mode.

---

## 8.4. Faction An ninh

**[CANON-REF — existence]**

Faction An ninh **thực sự tồn tại** trong V1.5.

Tuy nhiên implementation/cơ chế hiện cần được **định nghĩa lại**.

### Historical reconstruction lead — không phải final mechanism

**[LEGACY-LORE / AWAITING REDEFINITION]**

Trong mô tả cũ, Faction An ninh có liên quan đến việc cách ly/kiểm soát đồ cá nhân và các yếu tố host-native có khả năng nguy hiểm, bao gồm ví dụ như:

- truyền thừa;
- phép thuật huyết thống;
- rune;
- các capability tương tự.

Các năng lực nội tại như võ thuật, khéo léo và kiến thức nền từng được mô tả là giữ lại.

**Không dùng mô tả này như current specification cho đến khi Faction An ninh được tái định nghĩa.**

---

## 8.5. Known legacy institutional components

**[LEGACY-BASE / PARTIALLY CONFIRMED]**

Các component đã từng tồn tại/được nhắc tới trong V1.5 gồm:

- recruitment / enrollment;
- gateway / secondary space;
- student handbook;
- school uniforms;
- teaching staff;
- curriculum;
- modern-world technology integration;
- entrance examination;
- class placement examination;
- graduation ceremony.

Không được mặc định mỗi component là:

- cosmetic lore;
- Narrative Engine;
- department;
- governance node;
- hay infrastructure.

Từng component phải được tái phân loại bằng causal function thực tế.

---

# 9. Faction coverage problem — bài toán thiết kế trung tâm của V1.5

## 9.1. Không thiết kế "một trường cần những khoa gì"

**[CANON-REF]**

Câu hỏi đúng là:

> Những miền trải nghiệm nào đủ phổ biến trong fiction để HIP từ rất nhiều Host Fiction có thể tự chọn một institutional Narrative Engine phù hợp và sinh ra trajectory đáng kể bên trong nó?

V1.5 cần **coverage across fiction**, không phải encyclopedia của trường đại học.

---

## 9.2. Ví dụ đã dùng để khóa principle — không canon hóa tên faction ngoài phần đã xác nhận

Một HIP giả định:

```text
thích học phép thuật
+ tính trầm
+ không thích bạo lực
+ bí mật giỏi võ
```

có thể có lý do chọn một faction về Phép thuật, và có khả năng tham gia faction về Võ kỹ/Nhu quyền.

Điểm cần giữ không phải tên faction cụ thể mà là principle:

```text
HIP state + goals + interests + agency
→ meaningful faction choice
```

Không phải:

```text
attribute → deterministic routing
```

---

# 10. Graduate boundary và invariant outcome

## 10.1. Return invariant

**[CANON-REF — source: `OC Academy.txt`]**

Sau graduation, HIP được trả về đúng original world/reality, không mặc định bị chuyển sang future/past/reality khác.

V1.5 kết thúc tại đây.

---

## 10.2. No default service obligation

**[CANON-REF — source baseline]**

Sau graduation, The Academy không mặc định yêu cầu:

- phục vụ;
- báo cáo;
- trung thành;
- nhiệm vụ;
- duy trì liên lạc.

Exception nếu có phải được externalize riêng.

---

## 10.3. Graduate population

**[CANON-EXISTENCE-ONLY]**

Đã có **rất nhiều HIP tốt nghiệp và trở về world gốc**.

Quy tắc sử dụng:

```text
ĐƯỢC PHÉP:
"Graduate population đã tồn tại."

KHÔNG ĐƯỢC PHÉP:
→ dùng các graduate chưa externalize làm ví dụ
→ suy ra demographic
→ suy ra success rate
→ suy ra loại người họ trở thành
→ suy ra pattern lịch sử
```

### Outcome-neutrality vẫn là invariant tham chiếu riêng

**[CANON-REF]**

The Academy không quyết định graduate sẽ trở thành loại người nào.

---

# 11. Greed, Lust và post-grad overlap

## 11.1. Greed

**[CANON-REF]**

Greed có nhiều role chồng chéo:

```text
Greed --IS_AN--> Narrative Engine
Greed --IS_AN--> Executor of The Academy
```

Greed là trường hợp đặc biệt hơn các Sin khác do bản chất `Greed` của chính hắn.

The Academy không cấm operation đặc thù này vì nó tạo ra lượng entropy lớn.

### Property relation

**[CANON-REF]**

Greed đảm bảo tài sản của HIP.

Không được tự suy ra:

```text
Greed OWNS HIP property
Greed COMMANDS Security Faction
Security Faction DEPENDS_ON Greed
```

Exact relation giữa Greed và Faction An ninh là `UNKNOWN`.

### Post-grad approach

**[CANON-REF]**

Dựa trên thành tích/trajectory hậu tốt nghiệp của HIP, Greed có thể chủ động tiếp cận hoặc không tiếp cận.

Không được universalize cơ chế này cho mọi Executor hoặc mọi Sin.

---

## 11.2. Lust

**[CANON-REF]**

Lust là một Narrative Engine và **thuộc V1.5** theo canon hiện tại.

Exact ontology/role của Lust trong V1.5 vẫn chưa externalize đủ:

- có phải institutional faction hay không: `UNKNOWN`;
- relation với institutional runtime: `UNKNOWN`;
- phase/authority/interface cụ thể: `UNKNOWN`.

Không dùng architecture của Greed, Sloth, Wrath hoặc Chaos để điền phần này.

---

## 11.3. Multiple Narrative Engines can approach one HIP

**[CANON-REF]**

The Academy không cấm nhiều Narrative Engine tiếp cận cùng một HIP.

```text
          HIP
         / | \
        /  |  \
 Engine A Engine B Engine C
```

Không suy ra:

```text
same target → composite engine
co-occurrence → cooperation
co-occurrence → dependency
same HIP → same objective
```

---

## 11.4. External-project confirmation

**[CANON-EXISTENCE-ONLY]**

Đã tồn tại một HIP ở project khác được **Greed và Lust** cùng tiếp cận.

Thông tin này chỉ được phép dùng để xác nhận:

```text
"Trường hợp như vậy đã tồn tại."
```

Không được dùng project/ HIP đó làm dữ liệu tham chiếu, suy ra mechanic, chronology, criteria hoặc relationship chi tiết khi project không được cung cấp trực tiếp.

---

# 12. Legacy lore anchor chưa được khóa lại

## 12.1. Wizard Tower / protected forest

**[LEGACY-LORE / AWAITING CONFIRMATION]**

Lore gốc từng mô tả The Academy như một tháp pháp sư trong một vùng rừng được bảo hộ bởi sức mạnh Meta-Engine; external power/magic không thể can thiệp để cấm Academy lựa chọn HIP.

Hiện tài liệu **không nâng implementation này thành current canon reference**, vì lần khóa canon gần nhất không tái xác nhận nó.

Khi externalize lại cần tách ít nhất hai lớp:

```text
wizard tower / protected forest
= lore implementation candidate

recruitment non-interference / authority protection
= possible causal invariant candidate
```

Cả hai chờ xác nhận riêng.

---

# 13. Narrative Engine philosophy — liên quan đến V2 và cách không áp sai sang V1.5

## 13.1. V2 không chỉ "chọn engine rồi chạy"

**[CANON-REF + source: `Narrative Engine — Core Design Philosophy.md`]**

V2 có một workload trước application:

```text
create / formalize Narrative Engine
→ establish causal identity
→ preserve host independence
→ choose Host Fiction
→ use World Bible as constraint/translation layer
→ choose Target Subject + Context
→ Local Realization
→ Simulation
→ Narrative Instance
```

Narrative Engine không phải story, prompt, trope hoặc fixed plot.

---

## 13.2. Seven Deadly Sins — design rationale

**[CANON-REF — user-confirmed]**

Thất đại tội được chọn làm nền cho nhiều Narrative Engine vì chúng:

- đủ bao hàm;
- có symbolic coverage lớn;
- chạm tới nhiều mặt của đời sống;
- cho phép nhiều Host Fiction ánh xạ vào.

Trong design logic:

```text
broad Sin domain
→ Governor narrows causal meaning / chống trope hóa
→ Catalyst hoặc cơ chế mở tương ứng chống fixed plot line
→ Host + actor agency produce trajectory
```

### Anti-template invariant

Không được biến đây thành universal component schema.

Các Narrative Engine khác nhau **không cần** cùng có:

```text
Governor + Catalyst + Counter + Doctrine + Tool
```

Greed, Sloth, Wrath, Chaos và future engines được phép có internal architectures khác nhau.

---

# 14. Quan hệ đang chồng chéo — phải giữ typed edges

Các overlap sau là nguồn complexity chính và phải được externalize bằng typed graph.

## 14.1. The Academy

Có thể đồng thời xuất hiện trong các graph khác nhau như:

```text
The Academy --PROVIDES--> authority / legitimacy / infrastructure
The Academy --RECRUITS--> HIP
The Academy --CAN_HOST--> institutional runtime
V1.5 --REPRESENTS--> pre-grad institutional causal domain
V2 --REPRESENTS--> post-grad Narrative Engine domain
```

Không collapse toàn bộ thành một parent-child tree.

---

## 14.2. HIP

Một HIP có thể đồng thời là:

- actor được user chọn từ Host Fiction;
- student trong V1.5;
- participant/target của institutional engine;
- peer của các HIP khác;
- graduate;
- post-grad historical actor;
- target của một hoặc nhiều Narrative Engine.

Các role này không đồng nghĩa với nhau.

---

## 14.3. Institutional faction

Một faction có thể là:

```text
Institution
+
Narrative Engine
```

nhưng internal department không tự động kế thừa status này.

---

## 14.4. Teacher / staff

Teacher có thể:

```text
BELONGS_TO Teaching
ACTS_AS Narrative Actor
INTERACTS_WITH HIP
```

`Teacher` không chỉ là exposition NPC.

---

## 14.5. Greed

Greed đồng thời có nhiều type-edge:

```text
Narrative Engine
Executor
property guarantee relation
possible post-grad approach relation
```

Không dùng một relation để suy ra các relation còn lại.

---

## 14.6. Cohort → faction traversal

Một HIP có thể thuộc cohort/class nhưng chọn nhiều faction khác nhau.

```text
HIP --BELONGS_TO / PARTICIPATES_IN--> cohort
HIP --ENTERS / INTERACTS_WITH--> faction
```

Không suy ra:

```text
cohort = faction
faction sequence = dependency
```

---

# 15. Failure modes bắt buộc tránh

## FM-01 — School prior collapse

Sai:

```text
Academy → faculty → department → course → student progression
```

nếu source chưa xác nhận.

V1.5 là causal institutional ecology, không phải trường học thông thường có engine gắn bên ngoài.

---

## FM-02 — Cosmetic interpretation

Không mặc định:

- uniform;
- exam;
- handbook;
- faction;
- lecture hall;
- institution;

chỉ là background hoặc flavor.

Phải kiểm tra causal function trước.

---

## FM-03 — Linear curriculum assumption

Không mặc định mọi HIP đi qua cùng path, cùng thứ tự faction hoặc cùng specialization.

---

## FM-04 — Deterministic routing from character traits

```text
likes magic → Magic faction mandatory
martial skill → Martial faction mandatory
introvert → low-social faction mandatory
```

đều là sai nếu không có canon.

HIP giữ agency.

---

## FM-05 — Actor reads the script

Không actor nào tự biết:

- secret capability;
- hidden host canon;
- future;
- author intent;
- toàn bộ engine architecture;

trừ khi có access mechanism hợp lệ.

---

## FM-06 — Universalize HIP criteria

Không biến legacy recruitment categories hoặc một engine-specific criterion thành định nghĩa HIP.

---

## FM-07 — Faction name = finished engine

Một domain như `Magic`, `Martial Arts`, `Science` chưa tự động là Narrative Engine.

Faction phải có causal identity đủ mạnh để sinh trajectory.

---

## FM-08 — Department explosion

Không biến mọi specialization thành faction/engine cấp Academy chỉ vì nó khác tên.

---

## FM-09 — One template for all engines

Không lấy Greed, Sloth, Wrath, Chaos hoặc V2 component vocabulary để bắt V1.5 factions dùng cùng schema.

---

## FM-10 — V2 back-defines V1.5

Genealogy hoặc formalization muộn không cho phép:

```text
V2 abstraction
→ infer what V1.5 "must really be"
```

---

## FM-11 — V1.5 continues past return-to-origin

Sai:

```text
V1.5 → return → HIP agency → post-grad engine → history
```

Đúng boundary:

```text
V1.5 → return to origin → STOP
```

Post-grad là miền V2.

---

## FM-12 — V1.5 và V2 là hai engine độc lập/đối thủ

Chúng là hai miền formalization của cùng một causal continuum lớn hơn.

---

## FM-13 — Every graduate must invoke V2

Hiện chưa có canon rằng mọi graduate bắt buộc phải bị một Narrative Engine hậu tốt nghiệp tiếp cận.

Giữ `UNKNOWN`.

---

## FM-14 — Multiple engines → composite/dependency

Nhiều Narrative Engine cùng tiếp cận một HIP không tạo composite engine hoặc dependency nếu source không xác nhận.

---

## FM-15 — Generalize Greed privilege

Không suy từ Greed rằng mọi Sin/Executor đều có cùng quyền, property relation hoặc post-grad approach mechanism.

---

## FM-16 — Use existence-only invariant as data

Không dùng graduate population hoặc external-project Greed+Lust case làm reference data.

---

## FM-17 — Security reconstruction becomes canon accidentally

Faction An ninh tồn tại, nhưng mechanism cũ phải được tái định nghĩa. Không canon hóa lại chỉ vì nó hợp lý.

---

## FM-18 — Legacy tower becomes current ontology

Wizard tower/protected forest hiện là legacy lore chờ xác nhận, không phải current architecture invariant.

---

## FM-19 — Fill UNKNOWN with standard academy content

Không tự thêm:

- student council;
- dormitory;
- guild;
- disciplinary board;
- rank system;
- houses;
- faculty senate;
- club structure;

chỉ vì trường học thường có.

---

## FM-20 — Narrative Engine becomes trope or fixed plot

Đặc biệt ở V2:

```text
Engine ≠ trope
Engine ≠ character archetype
Engine ≠ prewritten arc
Engine ≠ prompt
```

---

# 16. Baseline canon hiện tại — bảng khóa nhanh

| Hạng mục | Trạng thái | Nội dung được phép dùng |
|---|---|---|
| HIP criteria-agnostic | CANON-REF | Common evaluation gateway; criteria đến từ context |
| V1.5 boundary | CANON-REF | Pre-grad institutional causality; kết thúc ở return to origin |
| HIP agency | CANON-REF | HIP tự chọn/đáp ứng; engine không chọn outcome |
| Institutional faction | CANON-REF | Có thể là Narrative Engine; tương đương một miền đủ lớn sinh arc |
| Teaching | CANON-REF | Institution + Narrative Engine; teacher có thể là Narrative Actor |
| Consent | CANON-REF | HIP được từ chối |
| Pass | CANON-REF | Tối đa 1 lượt/người; recipient deliberately open |
| Family compensation | CANON-REF | Có nếu family còn và chấp nhận; mechanism deliberately open |
| Biological age | CANON-REF | Không tăng trong Academy |
| World can be selected repeatedly | CANON-REF | Một world có thể có nhiều recruitment cycles |
| Cohort 10 HIP/world | LEGACY-BASE | Dùng làm base redesign, không phải HIP definition |
| 3 worlds/class | LEGACY-BASE | Tối đa 30 HIP/cohort trong lore gốc |
| 10 Academy years = 1 origin year | LEGACY-BASE | Temporal ratio làm base; không suy duration |
| Faction An ninh | CANON-REF existence | Có thật; mechanism phải redefine |
| Greed | CANON-REF | Narrative Engine + Executor; special case |
| Greed property guarantee | CANON-REF | Có relation đảm bảo tài sản; exact interface với Security unknown |
| Greed post-grad approach | CANON-REF | Có thể approach hoặc không theo post-grad achievement/trajectory |
| Multiple NEs approach same HIP | CANON-REF | Được phép; không tạo dependency/composite |
| Lust | CANON-REF | Narrative Engine thuộc V1.5; exact role unknown |
| Many graduates existed | CANON-EXISTENCE-ONLY | Chỉ xác nhận graduate population đã tồn tại |
| Greed + Lust approached one external-project HIP | CANON-EXISTENCE-ONLY | Chỉ xác nhận trường hợp đã tồn tại |
| Wizard tower/protected forest | AWAITING CONFIRMATION | Legacy lore; chưa dùng làm current architecture invariant |

---

# 17. UNKNOWN / chờ externalize

## 17.1. Recruitment

- exact HIP criterion set của V1.5;
- cơ chế phát hiện HIP;
- trigger để một world được chọn;
- trigger để cùng world được chọn lại;
- pass-recipient protocol;
- compensation implementation;
- authority/jurisdiction detail.

## 17.2. Cohort

- class/cohort lifetime;
- relation cohort ↔ faction;
- grouping/subgroup mechanics;
- có giữ 3-world structure trong redesign cuối hay không;
- cách các recruitment cycle khác nhau đồng bộ.

## 17.3. Temporal architecture

- exact spatial ontology;
- relation giữa Academy time và nhiều world khác nhau;
- psychological/experiential aging;
- graduation duration;
- synchronization at return.

## 17.4. Institutional map

- danh sách faction chính thức;
- faction nào đồng thời là Narrative Engine;
- faction nào chỉ là infrastructure/interface;
- values / definitions / criteria của từng faction;
- actor topology;
- activation/exit/failure mode;
- internal departments;
- lecture hall structure;
- cross-faction state propagation;
- concurrency;
- authority conflict.

## 17.5. Teaching

- primitive;
- criterion;
- pedagogy mechanism;
- relation với peer HIP;
- teacher authority;
- output;
- termination/failure.

## 17.6. Faction An ninh

- mandate;
- authority;
- intake procedure;
- treatment of items/capabilities;
- relation với Greed;
- ownership/custody model;
- release/return model;
- failure modes.

## 17.7. Curriculum / exams / placement

- curriculum có phải routing/exposure architecture hay không;
- entrance examination là engine/interface/governance/state transition gì;
- placement examination là gì;
- có path bắt buộc hay không;
- graduation conditions.

## 17.8. Lust

- exact role trong V1.5;
- institutional relation;
- authority;
- phase/interface;
- portability / post-grad relation.

## 17.9. V1.5 → V2 handoff

- có phải mọi graduate đều eligible cho V2 không;
- khi nào Narrative Engine được phép/chọn tiếp cận;
- shared state contract;
- observation relation của The Academy;
- concurrency giữa nhiều Narrative Engine.

---

# 18. Sơ đồ chuẩn V1.5

```text
                           THE ACADEMY V1.5
                   [PRE-GRAD INSTITUTIONAL DOMAIN]

Host Fiction / Original Reality
            │
            │ user selects HIP
            ▼
       HIP Evaluation
      [criteria external]
            │
            ▼
    Academy Recruitment Offer
            │
       ┌────┴────┐
       │         │
     REFUSE    ACCEPT
                  │
                  │ consent / pass / compensation relations
                  ▼
             Academy Entry
                  │
                  ▼
        Cohort / Class Architecture
     [legacy base: up to 30 from 3 worlds]
                  │
                  ▼
       Institutional Engine Ecology
                  │
       ┌──────────┼──────────┐
       ▼          ▼          ▼
   Faction A   Teaching   Faction N
   [NE?]       [NE]       [NE?]
       │          │          │
 departments   teachers    actors
 criteria      peer HIP    local rules
       │          │          │
       └──── HIP traversal ──┘
                  │
        HIP carries changed state
                  │
                  ▼
              Graduation
                  │
                  ▼
          RETURN TO ORIGIN
          =================
             V1.5 ENDS
```

`Faction A/N` chỉ là placeholder.

Không mặc định mọi faction cùng schema hoặc mọi HIP đi cùng route.

---

# 19. Sơ đồ chuẩn V2

## 19.1. V2 design/application layer

```text
             THE ACADEMY V2
          [POST-GRAD DOMAIN]

Create / Formalize Narrative Engine
             │
             ▼
      Causal identity + invariants
             │
             ▼
        Select Host Fiction
             │
             ▼
         Read World Bible
             │
             ▼
   Target Subject + User Context
             │
             ▼
 Narrative Engine × Host Rules
             │
             ▼
        Local Realization
             │
             ▼
          Simulation
             │
             ▼
       Narrative Instance
```

The Academy / Meta-Engine cung cấp governing philosophy, legitimacy, authority, infrastructure và interoperability theo context đã formalize.

## 19.2. Post-grad operational view

```text
Graduate returned to Origin
            │
            ▼
   local life / historical state
            │
     ┌───────┼─────────┐
     ▼       ▼         ▼
 Narrative  Narrative  Narrative
 Engine A   Engine B   Engine C
     │       │         │
     └── interactions ─┘
            │
            ▼
        HIP agency
            │
            ▼
 historical trajectory / possibility
```

Không canon rằng mọi graduate bắt buộc có Narrative Engine active.

---

# 20. Sơ đồ chuẩn V2.5 — mục tiêu thống nhất

**[WORKING GOAL — user-confirmed direction, chưa phải finished specification]**

V2.5 không nên được đọc như hai engine độc lập bị ghép cơ học.

Nó là mục tiêu tái thống nhất **end-to-end causal continuum** của The Academy sau khi hai miền đã được formalize riêng.

```text
                         THE ACADEMY V2.5
                      [UNIFIED CAUSAL CHAIN]

Host Fiction / Original Reality
            │
            ▼
       User selects HIP
            │
            ▼
      HIP evaluation / offer
            │
            ▼
  ╔══════════════════════════════╗
  ║          V1.5 DOMAIN         ║
  ║                              ║
  ║ recruitment / consent        ║
  ║ cohort                       ║
  ║ institutional factions      ║
  ║ peer-HIP exposure           ║
  ║ learning / transformation   ║
  ║ graduation                  ║
  ╚══════════════╤═══════════════╝
                 │
                 ▼
          RETURN TO ORIGIN
        [handoff boundary]
                 │
                 ▼
  ╔══════════════════════════════╗
  ║           V2 DOMAIN          ║
  ║                              ║
  ║ post-grad state              ║
  ║ optional/selective NE access ║
  ║ one or multiple engines      ║
  ║ Local Realization           ║
  ║ HIP agency                  ║
  ║ historical trajectories     ║
  ╚══════════════════════════════╝
```

### V2.5 invariants

```text
V1.5 causal identity must survive the merge.
V2 causal identity must survive the merge.

UNIFICATION
≠ normalization into one engine schema
≠ V2 overwriting V1.5
≠ V1.5 containing all V2 engines
≠ every graduate automatically entering every/any V2 engine
```

Mục tiêu:

```text
complete V1.5 first
→ define clean V1.5 output
→ define V2 input/handoff contract
→ unify without duplicate causal links
```

---

# 21. Mục tiêu phát triển

## Mục tiêu 1 — hoàn chỉnh V1.5

Ưu tiên:

```text
recover / design institutional factions
→ define values / criteria / causal identities
→ define actors
→ define cohort relations
→ define routing / self-selection
→ define cross-faction state
→ define Security
→ define Teaching
→ define exams / curriculum / graduation
→ lock return-to-origin boundary
```

Nguyên tắc làm việc:

```text
remembered paracosm fragment
→ extract node
→ extract typed relation
→ identify causal function
→ separate legacy implementation
→ mark UNKNOWN
→ only then generate PROPOSAL
→ human/paracosm accepts or rejects
```

## Mục tiêu 2 — V2.5

Chỉ sau khi V1.5 đủ ổn định:

```text
V1.5 terminus
+
V2 post-grad entry
→ define handoff
→ remove fragmentation
→ preserve causal non-redundancy
→ unified Academy lifecycle
```

---

# 22. Minimal anti-drift snapshot

Nếu chỉ giữ một block khi mở chat mới:

```text
THE ACADEMY IS A CONTENT-GENERATING META-ENGINE CENTERED ON HIP.

V1.5
= pre-grad institutional causal ecology.
Institutional factions can themselves be Narrative Engines.
HIPs do not follow one universal linear curriculum.
HIP agency and cross-HIP interaction generate trajectories.
V1.5 ends at RETURN TO ORIGIN.

V2
= post-grad Narrative Engine domain.
Creating/formalizing a Narrative Engine is itself part of the work;
the engine is then locally realized through Host Fiction rules.
Multiple Narrative Engines may approach the same HIP.

V2.5
= goal of restoring one end-to-end causal chain from V1.5 + V2
without flattening either architecture.

COMPLEXITY IS RELATIONAL, NOT HIERARCHICAL.
UNKNOWN IS NOT PERMISSION TO INVENT.
EXISTENCE-ONLY CANON MUST NOT BE USED AS REFERENCE DATA.
```

---

# 23. Source provenance

Primary project sources used to anchor this document:

- [The_Academy_V1_5_Architecture_Handoff.md](The_Academy_V1_5_Architecture_Handoff.md)
- [Historical_Influence_Potential.md](../../01_HIP/Historical_Influence_Potential.md)
- [OC Academy.txt](<../../source_archive/Academy_legacy/OC Academy.txt>)
- [modular_engine_concept_anti_drift.md](../../12_ANTI_DRIFT/modular_engine_concept_anti_drift.md)
- [engine_genealogy_and_development_updated.md](../../06_ENGINE_GENEALOGY/engine_genealogy_and_development_updated.md)
- [Narrative Engine — Core Design Philosophy.md](<../../00_META/Narrative Engine — Core Design Philosophy.md>)
- [Greed_II_Core_Interfaces_Consolidated.md](../../source_archive/Greed/Greed_II_Core_Interfaces_Consolidated.md)
- [Sloth_Engine_Working_Draft.md](../../04_NARRATIVE_ENGINES/Sloth/Sloth_Engine_Working_Draft.md)
- [Wrath_Working_Draft.md](../../04_NARRATIVE_ENGINES/Wrath/Wrath_Working_Draft.md)
- [Chaos_Engine_Canon_Specification_v3.md](../../04_NARRATIVE_ENGINES/Chaos/Chaos_Engine_Canon_Specification_v3.md)

Additional current-state architecture and canon locks come from creator confirmations in the current V1.5 reconstruction conversation, especially:

- V1.5/V2 split by pre-grad vs post-grad domain;
- V2.5 unification goal;
- faction-as-major-Narrative-Engine model;
- cohort/world sampling legacy base;
- temporal ratio legacy base;
- biological-age invariant;
- consent/pass/compensation rules;
- repeat recruitment of the same world;
- Security Faction existence + redefinition requirement;
- Greed special overlapping roles;
- multiple Narrative Engines per HIP;
- Lust membership in V1.5;
- existence-only handling of graduate population and external-project Greed+Lust case.

---

# 24. Final rule

> **Không hoàn thiện V1.5 bằng cách hỏi “một trường học nên có gì”. Hãy phục dựng và thiết kế từng institutional faction như một causal Narrative Engine có giá trị, tiêu chí, actor, pressure, interaction và state transition riêng; sau đó cho HIP với agency và state của chính nó đi xuyên một ecology các engine đó cho tới graduation và return to origin.**
