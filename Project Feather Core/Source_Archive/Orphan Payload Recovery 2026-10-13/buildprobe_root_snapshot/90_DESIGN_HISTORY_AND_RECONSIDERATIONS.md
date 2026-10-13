# AetherFire — Design History & Reconsiderations

> Preserved as a separate temporal layer. `DESIGN HISTORY`, `RETIRED`, `SURVIVING LEGACY`, `UNDER CONSIDERATION`, `CURRENT CANON` and `UNKNOWN` retain their original meanings. Nothing in this file becomes current canon merely because it appears here.

## Regional supersession notice — 2026-09-11

- Quad Night and the old four-member-state model are retired.
- Holy State → Matriarch's Lament; T.Gear → Transfusion EasterFire; Trinity Hexagon → district inside ML.
- Old Queen custody, 100 km corridor and Academy-flank relations are orphaned, not silently remapped.
- The AF↔TE treaty and covert-interference pattern survive only in the form stated by the new regional canon; the Holy-State transit chokepoint is retired.
- The former foreign-spy punitive Undie route is removed as a current or reconsideration candidate because it no longer fits the political-centric setting. Archived source and generated history references remain provenance/removal records only; replacement legal/status treatment remains `UNKNOWN`.

## Latest source-state boundary — updated 2026-09-16

- Internal Matriarch's Lament current canon is routed to `70_MATRIARCHS_LAMENT_CURRENT.md`. `10` now retains only its global/cross-domain interface; this is a document-authority split, not a lore retcon.
- RF single-kingdom wording is superseded by the continental-union/member-state ontology now recorded in `10`.
- The former Academy-failure-to-Undie route is removed from both current canon and reconsideration. It survives only inside byte-preserved archived sources as provenance.
- The Academy's six-year model, five-person team, twelve competency blocks, daily rhythm, multi-axis scholarship profile and functional uniform direction are no longer working proposals; they are current canon in `10`.
- MC4 legacy mastery, Fusion and Spear mechanics remain genealogy-only and are not current.
- Trần Trúc Nha's membership and regional role in Matriarch's Lament remain current. Her proposed summoned/cross-world origin, MC4's proposed in-world cross-fiction origin and the other unconfirmed cross-world/cross-time candidates are `UNDER CONSTRUCTION / NOT CURRENT CANON`.
- The `Nguyên Chủ / Nguyên Anh` concept and the `元主 / 元嬰` wordplay remain proposal/design material. They are not assigned to MC2's mother by this integration.

## RP history import boundary — 2026-09-25

- The user-supplied RP-history synthesis is archived byte-exactly. Selected history, inference and proposals enter this file only; its claims have not been independently checked against the original RP transcript.
- A future Undie revamp for Canon 1 and Canon 2, after their V0.5 split, is being designed separately and has not been canonized by this import.

## AetherFire — Design History & Các điểm cân nhắc mang lại

> **Loại tài liệu:** design history / genealogy / refactor log / reconsideration register  
> **Mục đích:** ghi lại các kiến trúc cũ của AetherFire, lý do chúng từng tồn tại, failure mode khiến chúng bị refactor, phần cơ chế nào đã sống sót sang current ontology, và những chi tiết nào đang được cân nhắc mang trở lại.  
> **Không phải:** world bible hiện hành.
>
> **Quy tắc đọc**
>
> - `CURRENT CANON` = canon hiện hành đã được người dùng chốt.
> - `DESIGN HISTORY` = thiết kế cũ từng tồn tại nhưng không mặc định còn hiệu lực.
> - `SURVIVING LEGACY` = cơ chế/pathway cũ vẫn còn sống trong current design, có thể đã đổi interface.
> - `RETIRED` = đã bỏ.
> - `UNDER CONSIDERATION` = đang cân nhắc mang lại; chưa phải canon.
> - `DESIGN ANALYSIS` = kết luận/đánh giá kiến trúc do trợ lý ngoại hóa từ lịch sử đã chốt; không tự biến thành canon.
> - `UNKNOWN` = chưa chốt; không tự lấp.
>
> **Nguyên tắc anti-drift:** genealogy giải thích cơ chế đến từ đâu, không tự định nghĩa ontology hiện tại.

---

## 0. READ FIRST — correction về “Undie-centric”: foreground/interface ≠ tâm của paracosm

**DESIGN HISTORY / USER-CONFIRMED MEMORY MODEL / ANTI-DRIFT PRIORITY**

Một correction quan trọng đối với cách đọc toàn bộ design history này:

> AetherFire **không được người thiết kế lưu trong đầu theo category `Undie`**. Memory index chủ yếu đi theo **ban ngành / institution / actor / site / procedure**, rồi mới tới status mà output của pipeline rơi vào.

Học viện hiện được index dưới node **Hội đồng Pháp sư / site Đông Bắc / đào tạo battlemage / lab / teleport gate / grievance phía Bắc**. Đây là cách index institution/process-first phù hợp với hướng political-centric hiện tại.

Route cũ `Academy failure → Undie` đã bị người dùng xóa khỏi setting hiện hành và khỏi reconsideration layer. Nó không còn là fallback để giải thích cách Học viện xử lý học viên thất bại.

Undie trong nhiều legacy pipeline là:

```text
terminal administrative status
/ failure sink
/ shared endpoint
```

chứ không phải root node sinh ra các institution.

```text
Department A ─┐
Department B ─┼→ Undie
Department C ─┘

≠

Undie
→ Department A/B/C
```

Undie từng rất nổi vì:

- MC2/RP camera bám rất lâu;
- visual/humiliation coding có độ salience cao;
- nhiều pipeline độc lập có thể cùng đổ vào một shared status;
- subsystem được implement sâu.

Nhưng ở **trung tâm chảo lửa chính trị–địa chính trị**, Undie có thể không có quyền quyết định gì đáng kể so với dynasty, True Crown/Raging Fire, long mạch, Mage Council, quân đội, Security/Counterintelligence/Interior, Holy State, Hoa Nguyệt, ba cường quốc phía Bắc và cult.

```text
DEPTH OF IMPLEMENTATION
≠ GLOBAL CENTRALITY

NARRATIVE FOREGROUND
≠ ONTOLOGICAL CENTER

SHARED ENDPOINT
≠ CAUSAL ROOT
```

Do đó mọi cụm từ `Undie-centric` ở các section cũ của file này phải đọc là **RP foreground / shared-interface gravity / implementation coupling**, không phải “cả thế giới được xây quanh Undie”.

---

## 1. Mẫu refactor tổng quát của AetherFire

Qua lịch sử thiết kế, AetherFire thường không thay complexity cũ bằng complexity mới hoàn toàn. Pattern lặp lại là:

```text
legacy mechanism
→ xác định requirement thực sự nó đang giải
→ giữ causal value
→ cắt containment/dependency không cần thiết
→ thay interface
→ giữ lại fossil nếu còn hữu ích
```

Các false coupling từng xuất hiện nhiều lần:

```text
entry = kinship
entry = class/status
humiliation = ontology
red-light subsystem = whole-world gateway
timeline divergence = two live timelines
competency growth = phải bị khóa trong Undie
controlled loophole = chỉ phục vụ adult experience
```

Current architecture phần lớn được hình thành bằng cách tháo các coupling này.

### 1.1 DESIGN ANALYSIS — success-induced architectural debt của mô hình Undie-centric

Một đặc điểm quan trọng của lịch sử AetherFire là kiến trúc Undie-centric cũ **không thất bại vì nó vận hành kém**. Ngược lại, nó từng vận hành quá tốt đối với scope ban đầu.

Một lượng lớn requirement từng được giải bằng cùng một bundle:

```text
Undie / shared Slave core
→ status
→ humiliation
→ uniform
→ mobility
→ barrier
→ transport
→ credit
→ black market
→ POW interface
→ resistance
→ intelligence
→ MC entry
→ magic
→ death handling
```

Điều này tạo hiệu suất local rất cao:

```text
actor cần constraint
+ surveillance
+ social tension
+ black-market access
+ resistance contact
+ financial pressure
→ đưa actor vào shared Slave/Undie architecture
→ nhiều requirement được giải cùng lúc
```

Khi scope của AetherFire mở rộng, chính ưu điểm đó trở thành **coupling debt**:

```text
works well together
≠
must belong together
```

Refactor vì vậy không thể chỉ xóa Undie rồi thiết kế lại từ đầu. Nó phải lần lượt:

```text
legacy mechanism
→ tìm requirement thật
→ tách khỏi old gravity well
→ tạo interface/domain mới
→ giữ causal value nếu còn hữu ích
→ kiểm tra dependency vừa bị đứt
```

Đây là dạng **success-induced architectural debt**: kiến trúc cũ được tối ưu rất tốt cho workload ban đầu, nhưng scope mới vượt assumptions ban đầu nên chi phí decoupling trở nên rất lớn.

Điểm anti-drift:

```text
Undie-centric architecture bị refactor
≠
Undie-centric architecture vốn dở
```

Nó bị tách vì đã trở thành một **gravity well quá hiệu quả ở lớp interface / shared implementation / narrative foreground**, khiến quá nhiều vấn đề độc lập có thể đi qua cùng một lời giải. Điều này **không** có nghĩa các subsystem background được sinh ra chỉ để phục vụ Undie hoặc chỉ có giá trị khi xuất hiện trong narrative Undie.

### 1.2 DESIGN HISTORY — RP/MC2-centric narration ≠ Undie-only ontology

**DESIGN HISTORY / CORRECTION**

Concept gốc là một **project RP xoay quanh MC2/Undie**. Vì vậy narrative foreground và phần được ngoại hóa nhiều nhất thực sự rất Undie-heavy. Tuy nhiên điều đó không có nghĩa toàn bộ world ontology chỉ chạy trên tiên đề Undie.

Cách đọc đúng hơn sau các correction mới nhất:

```text
PRIMARY RP / NARRATIVE AXIS
→ MC2 + Undie + fall-from-grace

SECONDARY STRATEGIC AXIS
→ politics + geopolitics + state + military + religion + trade + security
```

Các background system như:

- Thánh điện / Thánh quốc;
- Hội đồng Pháp sư;
- Nội vụ–An ninh–Phản gián;
- POW specialist activity;
- thương mại / treaty;
- hiến pháp / tư pháp / tố tụng / nhà tù;
- quân đội / True Crown;
- magic-tech infrastructure;
- đối ngoại / biên giới / thuộc địa

đã có causal function riêng và được build đủ sâu để tạo áp lực thật lên narrative. Nhưng ở **RP-era**, chúng chưa được đặt ngang story như một mục tiêu worldbuilding tự thân theo triết lý current project; độ sâu của chúng phần lớn được quyết định bởi việc chúng cần tạo pressure, mở/đóng pathway hoặc phản ứng đáng tin với tuyến MC2.

Quan hệ đúng:

```text
NARRATIVE CENTRALITY
≠
ONTOLOGICAL CENTRALITY
```

Undie từng là:

```text
- narrative focal point mạnh
- shared interface / implementation cho nhiều event
```

nhưng không được suy:

```text
Undie
→ reason-for-existence của mọi subsystem
```

Một analogy do user cung cấp:

> Toàn world giống một bàn đồ ăn; việc người thiết kế thích chọn một món nhất không làm cả bàn được nấu từ chính món đó.

### 1.3 DESIGN HISTORY — core state đã vững từ RP-era

Old AetherFire không đi theo sequence:

```text
adult RP
→ về sau mới thêm serious state/worldbuilding
```

Ngay trong thời RP/Undie-heavy, core setting đã có ở mức đáng kể:

- hiến pháp;
- tư pháp;
- tố tụng;
- nhà tù liên bang;
- cấu trúc nhà nước tuy đơn giản hơn current design;
- thương mại quốc tế;
- hiệp định song phương;
- tôn giáo chính thức;
- Hội đồng Pháp sư;
- internal-security complex;
- quân đội / legitimacy doctrine;
- POW specialists;
- địa chính trị nhiều hướng.

Do đó current refactor không phải quá trình **phát minh chiều rộng từ số 0**, mà là:

```text
old substantial core
→ audit
→ tách false coupling
→ phân rã competence concentration
→ tăng institutional autonomy / asymmetry
→ current architecture
```

### 1.4 DESIGN HISTORY — “strategic adult” chứ không chỉ scene-level adult

Old premise adult/Undie không chỉ tồn tại ở cảnh hoặc aesthetic. Nó từng được nối lên cấp statecraft:

```text
Undie trade
→ treaty / diplomacy

MC2 fertility / Raging Phoenix
→ dynastic politics / legitimacy / bloodline value

Undi visual coding
→ cultural degradation / geopolitical symbolism

Undie resistance
→ intelligence / counterintelligence / security policy
```

Cách nén phù hợp:

> **Old AetherFire là một RP adult-heavy mà adult premise đã được đẩy lên cấp chiến lược.**

Điều này không làm mọi subsystem là adult subsystem; nó chỉ cho thấy foreground adult từng có khả năng chạm trực tiếp vào luật, ngoại giao, succession, security và dynastic politics.

---

## 2. A — MC1 từng là em gái song sinh của MC2

### 2.1 DESIGN HISTORY

MC1 sau isekai từng được thiết kế thành **em gái song sinh của MC2**.

Mục tiêu ban đầu:

```text
giảm gánh nặng giải thích Raging Phoenix / entry
→ buộc MC1 vào hoàng gia ngay lập tức
```

Nhưng solution này tạo nhiều dependency:

```text
ENTRY
=
KINSHIP
=
GENDER
=
POLITICAL STATUS
=
GEOGRAPHY
```

Các vấn đề phát sinh:

1. Tại sao MC1 phải chuyển giới?
2. Nếu tác giả ban đầu là nữ, tại sao vẫn cần cấu trúc song sinh để bind vào thể chế?
3. Nếu fiction cần MC1 có thể đơn phương hành động để thoát thế gọng kìm, tại sao lại tự khóa actor vào hoàng gia?
4. Tại sao MC2/MC1 phải hoạt động quá tập trung ở thủ đô, nơi mọi hoạt động bị giám sát cực mạnh?
5. Tension bị dồn vào một địa chính trị duy nhất.

### 2.2 CURRENT REFACTOR

Current architecture tách:

```text
ENTRY
≠
KINSHIP
≠
LEGITIMACY
≠
GENDER
```

Raging Phoenix đảm nhiệm cross-fiction entry mà không cần MC1 là song sinh MC2.

---

## 3. B — Undie từng là gravity well của toàn setting

### 3.1 DESIGN HISTORY

Undie từng gánh đồng thời:

- sex-work system;
- red-light district;
- illegal activity interface;
- humiliation engine;
- resistance breeding ground;
- intelligence node;
- political node;
- điểm hội tụ của nhiều bộ/ngành;
- gateway của nhiều event.

Nó trở thành:

```text
mọi đường
→ Undie
```

Đây là một **single point of failure về centrality**.

### 3.2 CURRENT REFACTOR

Undie vẫn giữ độ sâu cao nhưng không còn mặc định là nơi mọi subsystem phải đi qua.

Current separation:

```text
Undie ≠ Black Market
Undie ≠ POW
Undie ≠ toàn slave economy
Undie ≠ toàn illegal economy
Undie ≠ toàn politics
```

---

## 4. C — POW và Undie từng là hai nhánh trong một shared Slave system

### 4.1 DESIGN HISTORY — sửa false containment

Cách diễn giải cũ:

```text
POW từng thuộc Undie
```

là **sai ontology**.

Concept gốc đúng hơn là:

```text
LEGACY SLAVE SYSTEM
├─ Undie functional branch
└─ POW functional branch
```

POW và Undie cùng thuộc một **umbrella/category Slave** và dùng chung nhiều phần của visual/admin system, nhưng POW không phải một subclass của Undie.

Quan hệ đúng ở design history:

```text
POW --BELONGED_TO--> legacy Slave system
Undie --BELONGED_TO--> legacy Slave system
POW --INTERACTED_WITH--> Undie
```

Shared infrastructure không chứng minh shared function.

### 4.2 DESIGN HISTORY — full color range, functional code và Undi dùng chung

Legacy Slave system dùng một dải mã màu chung, nhưng màu không chỉ biểu thị một line-job tuyến tính. Nó còn mã hóa:

- function;
- internal role;
- branch;
- phối hợp nhiều mã khi cần.

Undi đã được thiết kế từ trước như một **uniform family của shared Slave system**, sau đó áp cho cả POW.

POW dùng biến thể:

```text
Undi family
+ dual-color code
+ dual-color composition
→ đọc được POW khác Undie thường
```

Do đó genealogy đúng là:

```text
OLD:
Undi = shared Slave-system uniform family

CURRENT:
Undi = Undie-specific uniform
```

Đây là một refactor thật ở cấp visual ontology, không chỉ đổi màu trang phục.

### 4.3 DESIGN HISTORY — forced transition và double-tension engine

Trong concept gốc, POW nam bị ép chuyển giới và bị đẩy vào cùng visual/body humiliation regime của shared Slave system.

Mục tiêu thiết kế không phải biến POW thành sex worker. Mục tiêu là khuếch đại bất mãn:

```text
POW humiliation
→ resentment ↑

Undie humiliation
→ resistance tension ↑
```

Hai nguồn tension được cố ý đặt cạnh nhau:

```text
POW resentment
+
Undie resistance
→ contact probability ↑
→ liên lạc phản kháng ↑
→ rescue / extraction / escape network ↑
→ xung đột hệ thống ↑
```

Đây là **double tension**: hai population có grievance khác nhau nhưng được thiết kế để dễ tạo cross-group conflict và liên kết cứu thoát.

Cách diễn giải cũ kiểu:

```text
humiliation
→ resistance
→ state quan sát network
```

chỉ mô tả được một phần. Design function rộng hơn là **conflict-generation architecture**, không chỉ intelligence bait.

### 4.4 FAILURE MODE — shared humiliation method phá function POW

Khi POW được tách ra để audit như một subsystem riêng, câu hỏi xuất hiện:

```text
shared grievance
≠
shared humiliation method
```

POW không cần mặc chung Undi, bị forced transition hoặc chịu cùng body regime với Undie để có:

- mất autonomy;
- mất chủ quyền cá nhân/chính trị;
- resentment;
- động lực phản kháng;
- lý do liên kết với mạng chống chế độ.

Đặc biệt POW có thể là elite specialist, quý tộc, bearer của niche skill, rare magic hoặc bloodline mà ngay Citizen/elite AetherFire cũng không có.

Với POW quý tộc nam, body/status/dynasty có thể tạo bundle giá trị:

```text
cơ thể
+ địa vị
+ dòng họ
+ khả năng duy trì nòi giống
+ huyết thống
+ succession value
```

Trong khi old implementation lại có thể:

```text
forced transition
+ sterilization
→ cooperation incentive ↓
→ dynastic / bloodline value ↓
→ exchange value ↓
→ resentment / escape incentive ↑
```

Nó tạo contradiction:

```text
STATE WANTS:
retain rare POW utility

nhưng OLD POLICY:
destroys part of the asset it wants to exploit
```

Ở cấp chiến lược, policy kiểu này còn có thể tăng backlash: elite đối phương có thêm lý do chống đến cùng, giảm incentive đầu hàng/trao đổi và tăng retaliation pressure.

Đây là ví dụ điển hình:

```text
dramatic engine tốt
+
institutional engine kém
```

### 4.5 SURVIVING DESIGN FUNCTION — giữ double tension, bỏ forced coupling

Phần causal đáng giữ từ design cũ là:

```text
POW grievance
+
Undie grievance
→ có khả năng giao nhau
→ network / rescue / information flow / resistance
```

Nhưng không cần giữ:

```text
shared Undi
forced transition
sterilization
```

Hai group có thể tạo grievance từ ontology riêng rồi gặp nhau tại resistance interface.

### 4.6 CURRENT REFACTOR

Current POW có pipeline quân sự/phản gián riêng.

```text
public status = POW
internal security category = Slave
```

Nhãn Slave ở current backend không tự kéo POW vào Civil/Criminal/Undie ontology.

Điểm chống drift:

```text
legacy shared Slave umbrella
≠
current POW belongs to Undie
```

## 5. D — MC3 từng đi vào Fiction 1 qua Undie

### 5.1 DESIGN HISTORY

MC3 từng được thiết kế theo Canon 1 để hợp thức hóa entry vào Fiction 1 bằng Undie.

Lý do local:

- entry dễ;
- collar tạo constraint;
- route chuyển giới cưỡng chế;
- phạm vi hoạt động ngắn;
- subject bị quản lý chặt.

### 5.2 FAILURE MODE

Requirement thật của MC3:

```text
ENTRY
+ CONSTRAINT
+ INFORMATION LIMIT
+ REASON TO INTERACT WITH WORLD
```

Nhưng implementation cũ biến thành:

```text
ENTRY
= UNDIE

CONSTRAINT
= COLLAR

BODY CHANGE
= FORCED TRANSITION

GEOGRAPHY
= UNDIE RANGE

SOCIAL POSITION
= UNDIE
```

Canon 1 còn có master-control khiến subject càng minh bạch và bị khóa chặt.

Đây là mismatch:

```text
actor cần tác động trajectory
vs
host subsystem được thiết kế để subject dễ đọc/dễ quản
```

### 5.3 CURRENT REFACTOR

MC3 đi vào Fiction 1 qua V0.5 + POC + Raging Phoenix alternate.

```text
ENTRY
≠ CLASS
```

---

## 6. E — MC3, Proof of Concept và genealogy V0.5 / V1.0 / 5 năm

### 6.1 DESIGN HISTORY — role MC3 cũ

MC3 ban đầu là editor/proofreader/co-author nhưng **role chưa rõ**.

Proof of Concept hiện tại chưa tồn tại nguyên khối như bây giờ.

Phần legacy đã có từ concept cũ:

- Simulation Park / commercial fiction experience ở Fiction 0;
- một ability thao tác **perception**;
- V0.5 / V1.0;
- khoảng 5 năm divergence.

### 6.2 DESIGN HISTORY — mô hình hai live timeline song song [RETIRED]

Một architecture cũ từng tổ chức V0.5/V1.0/5 năm như:

```text
timeline hiện tại
→ MC1 lo

timeline lệch 5 năm trước
→ MC3 lo

hai dòng chạy song song
```

#### Failure mode

```text
event mới ở A
→ phải propagate sang B
→ retcon B
→ có thể retcon ngược A
→ continuity cost tăng mạnh
```

Metafiction vốn đã phải bảo toàn pathway cho event; duy trì hai persistent live timeline làm complexity tăng mà không tạo đủ giá trị tương ứng.

### 6.3 CURRENT STORY ARCHITECTURE — same V0.5, two continuation modes

Current architecture không dùng hai persistent live timeline độc lập.

Có **một shared V0.5 source** nhưng sau đó xảy ra hai operation khác loại:

```text
WRITE(V0.5)
→ MC1 hoàn thiện nửa còn lại
→ V1.0 / Canon 1

LIVE(V0.5, HOPE, MC3, actors, institutions, time)
→ khoảng 5 năm historical accumulation
→ current Canon 2
```

Do đó:

```text
V1.0
≠
V0.5 + 5 năm
```

V1.0 là **authored completion**; 5 năm là **lived historical accumulation**.

MC1 sau khi hoàn thiện V1.0 còn dùng Fictionize để stress-test nó. Canon 1 vì vậy vừa là authored trajectory, vừa là realized Fictionize scenario/reference model.

Trong khi đó Canon 2 là persistent live history từ V0.5 sau HOPE.

### 6.4 CURRENT STORY ARCHITECTURE — divergence rồi intersection

Clash #1:

```text
V0.5
→ POC / HOPE
→ Fictionize × POC clash
→ Raging Phoenix alternate
→ MC3 vào Fiction 1
→ live divergence bắt đầu
```

Clash #2 xảy ra về sau khi:

```text
MC1 đang stress-test V1.0 / Canon 1
+
Canon 2 đã tích lũy ~5 năm history
→ hai pathway đi vào vùng overlap
→ Fictionize × POC clash #2
→ MC2 gọi MC1 bằng Raging Phoenix
→ MC1 bị kéo ngang vào current Fiction 1
```

Điểm chống drift:

```text
OVERLAP
≠
MERGE
```

Canon 1 và Canon 2 không trở thành cùng một world-state.

### 6.5 DESIGN HISTORY / META-GENEALOGY — lịch sử redesign trở thành cấu trúc bên trong fiction

Outside/design history:

```text
V0.5
→ old V1.0 / Canon 1 architecture từng là active core
→ project được redesign / metafictionalize
→ Canon 1 trở thành legacy/reference trong current project
→ Canon 2 là current active design
```

Inside/meta-canon:

```text
same V0.5
→ MC1 authors + realizes V1.0
→ MC3/HOPE tạo live divergence
→ 5 năm history
→ pathways overlap tại clash #2
```

Hai graph này có cấu trúc tương đồng nhưng **không phải cùng ontology**.

Điểm quan trọng:

```text
DESIGN-HISTORY LEGACY STATUS
≠
META-CANON INVALIDITY
```

Canon 1 có thể là legacy/reference ở cấp authorial design nhưng vẫn là authored + Fictionize-realized trajectory trong story ontology.

### 6.6 SURVIVING LEGACY — Proof of Concept

Current POC là refactor/convergence của:

```text
editor role
+ Simulation Park
+ pathway/trajectory concern
+ perception manipulation legacy
```

Trong Fiction 1, perception manipulation được giữ lại như interface actor-level của POC.

## 7. F — MC1 từng bị khóa status giống MC2

### 7.1 DESIGN HISTORY

MC1 cũ cũng bị dính status, bị giam/cô lập trong khu riêng.

Loop local rất mạnh:

```text
làm nghĩa vụ Undie
→ sinh hoạt
→ trình diện hệ thống
→ chỉ có vài giờ rảnh trước khi ngủ
→ dùng thư viện
→ vào fiction con
→ phải quay lại đúng lúc
→ che giấu anomaly
```

Tension cục bộ tốt vì mỗi lần MC1 dùng Fictionize đều phải cân:

```text
training gain
vs
absence time
vs
collar signal loss
vs
scrutiny
vs
sleep
```

### 7.2 FAILURE MODE

Dù MC1 mạnh đến đâu:

```text
capability ↑
→ collar vẫn cưỡng chế
→ geography vẫn lock
→ anomaly dễ bị phát hiện
```

Kết quả:

```text
power progression ↑
agency thực tế ≈ không tăng tương ứng
```

Undie lại trở thành gateway bắt buộc của pathway MC1.

### 7.3 SURVIVING LEGACY

Phần sống sót sang current design:

```text
library
→ fiction con
→ time-ratio training
→ competency growth
→ anomaly/secrecy risk
```

Phần bị bỏ:

```text
MC1 MUST_BELONG_TO Undie
```

---

## 8. G — Human patrol, fake Undie và tiền thân của Yellow

### 8.1 DESIGN HISTORY

Concept gốc có **cảnh vệ con người tuần tra liên tục**.

Red/Pink gần như không thể ra khỏi red-light district nếu không có quyền.

Một số Citizen nữ tìm cảm giác mạnh bằng cách:

- mua collar giả;
- mua Undi trôi nổi;
- dùng mực giả;
- cosplay như Undie.

Human patrol tồn tại để kiểm tra ambiguity mà visual/collar giả tạo ra.

Yellow bắt đầu như một sanction tự nhiên cho:

```text
Citizen giả Undie
→ bị phát hiện
→ Yellow
```

### 8.2 SURVIVING LEGACY

Current Yellow vẫn giữ genealogy counter-impersonation:

- giả dạng nô lệ gây rối;
- control device jailbreak/bất hợp pháp;
- các vi phạm công cộng đã chốt;
- first offense → Yellow;
- repeat → Red vĩnh viễn + quota ×2.

Fake collar/fake marking cũng sống sót trong black-zone logic.

### 8.3 UNDER CONSIDERATION

Đang cân nhắc mang lại:

#### Human patrol

Có thể phục hồi patrol con người trong current geography rộng hơn.

**Chưa chốt:**

- phạm vi tuần tra;
- thẩm quyền;
- relation với camera/drone/android;
- role chống giả mạo;
- bribery/corruption;
- procedural check.

#### Geography

Có cân nhắc mở rộng enforcement ra ngoài Undie quarter thay vì giữ lỗi cũ:

```text
Undie problem
→ MUST occur inside red-light district
```

---

## 9. H — Black market gốc

### 9.1 DESIGN HISTORY

Black market gốc đã có concept:

```text
controlled loophole
```

nhưng chức năng chủ yếu là:

```text
hack collar
→ bán trải nghiệm slave/Undie cho Citizen
```

Nó gần với một **experiential loophole market**.

### 9.2 CURRENT EVOLUTION

Current black market mở rộng thành:

- collar bypass;
- mobility;
- identity fraud;
- corruption;
- resistance logistics;
- counterintelligence;
- foreign intelligence;
- elite interests.

Core legacy còn nguyên:

```text
state biết loophole
+
không triệt hoàn toàn
```

---

## 10. I — Undie mobility và barrier gốc

### 10.1 DESIGN HISTORY

Undie gốc không bị khóa tuyệt đối trong red-light district.

Họ có thể làm việc ở nhiều nơi được phép, trừ:

- hoàng cung;
- nghị viện;
- một số cơ quan đặc biệt;
- các khu bị hạn chế khác.

Về function, Undie gần với **gái gọi di động**:

```text
khách gọi
→ Undie được dispatch
→ đi tới điểm làm việc
```

### 10.2 Barrier gốc

Barrier là một **màn xanh** nằm giữa các tường thành/nội khu.

```text
Undie tới barrier
→ kiểm mã cho phép

có mã hợp lệ
→ cho qua

không có / sai mã
→ chặn
→ báo động
```

Original requirement:

```text
mobility rộng
+
selective access
→ permissioned geography
```

### 10.3 UNDER CONSIDERATION

Đang cân nhắc mang lại một phần original use case của barrier.

Chưa chốt:

- barrier có còn gắn mạnh với Undie mobility hay không;
- có áp rộng cho nhiều status;
- cách cấp mã;
- relation với current collar/AI/android.

---

## 11. J — Giao thông công cộng và giao thông riêng cho Undie

### 11.1 DESIGN HISTORY

Concept gốc có:

```text
public transport
+
Undie-specific transport
```

Giao thông riêng ưu tiên route tới:

- nhà riêng sĩ quan;
- thành viên nội các;
- cư dân có tiền;
- khách có khả năng trả cao.

### 11.2 Economic loop

```text
khách gọi
→ Undie đi lại
→ Undie tự ứng chi phí di chuyển
→ làm việc
→ nhận công
→ khấu trừ chi phí
→ tip tùy khách
```

Net income có thể âm nếu:

```text
transport + consumables + other costs
>
payment + tip
```

Điều này chứng minh performance đã là core từ rất sớm.

---

## 12. K — Credit score, credit money, multiplier và chi phí cá nhân

### 12.1 DESIGN HISTORY

Concept gốc đã tách:

```text
credit money
≠
credit score
```

Money phục vụ cashflow/consumption.

Score phục vụ performance/progression/eligibility.

### 12.2 Pricing legacy

Các hệ số từng có:

```text
Red / Scarlet thường
→ ×1.5

hoạt động nhóm
→ ×2

tip
→ tính riêng
```

Không suy các hệ số này còn current canon.

### 12.3 Consumables / advance

Undie tự trả đồ vệ sinh cá nhân.

Nếu thiếu:

```text
mượn trước
→ khấu trừ sau
```

Điều này tạo:

```text
operating cost
+
advance
+
future deduction
```

và khả năng negative carry.

---

## 13. L — Illegal prostitution pathway của MC2

### 13.1 SURVIVING LEGACY / CURRENT PATHWAY

Đây là một pathway cũ **từ concept gốc đến current architecture gần như không đổi**.

```text
MC2 đi đường bất hợp pháp
→ không được bảo vệ tương đương hệ hợp pháp
→ tăng khả năng bị quỵt / bạo lực / lạm dụng
→ muốn liên lạc kháng chiến nhiều hơn
→ tiếp xúc channel rủi ro hơn
→ nhà nước dựng kháng chiến giả
→ trap
→ tuyệt vọng
→ chết tâm
```

Pathway không tồn tại chỉ để tạo dark scene.

Causal spine:

```text
incentive
→ lựa chọn
→ exposure
→ risk
→ adaptation
→ state exploitation
→ psychological collapse
```

### 13.2 Function của illegal market

Trade-off:

```text
LEGAL
→ protection / governance / health / enforcement
→ cost + constraint cao hơn

ILLEGAL
→ flexibility / contact / upside cao hơn
→ protection thấp hơn
→ abuse/default risk cao hơn
```

---

## 14. M — Thuốc kích thích

### 14.1 DESIGN HISTORY / RETIRED

Concept gốc từng đặt nặng stimulant để:

- tăng hiệu suất;
- tăng chịu đựng;
- kéo dài workload.

### 14.2 Lý do bỏ

Không phải vì lý do đạo đức.

Lý do thiết kế:

```text
performance problem
→ stimulant
```

là solution quá dễ, quá lười và giống patch chữa cháy.

Nó shortcut các bài toán đáng lẽ phải được giải qua:

- scheduling;
- specialization;
- customer fit;
- pricing;
- workload;
- transport;
- recovery;
- occupational choice.

### 14.3 UNDER CONSIDERATION

Đang cân nhắc mang lại **hệ gái gọi riêng**.

Chưa chốt:

- nó có phải subsystem Undie không;
- rank nào dùng;
- dispatch authority;
- transport;
- payment;
- safety;
- access;
- geography.

---

## 15. N — State credit, black credit và shop gốc

### 15.1 DESIGN HISTORY

Concept gốc từng có:

- tín dụng nhà nước;
- tín dụng đen;
- Undie dùng **status làm collateral**;
- vay để đầu tư vào shop/body/earning capacity.

Shop gốc lớn hơn mini-custom hiện tại.

Các hạng mục từng có:

- phẫu thuật thẩm mỹ;
- mỹ trang cao cấp;
- body upgrades;
- các can thiệp nhằm nhắm customer segment cụ thể.

### 15.2 Economic logic

```text
loan
→ investment
→ attractiveness / customer fit / earning capacity
→ revenue
→ repay
```

### 15.3 Default

Nếu không trả được:

```text
default
→ debt assigned
→ subject bị gán cho một service/master nhất định
→ master set rate riêng
→ set pay riêng
→ có thể không có tip
→ đủ nợ mới được rời
```

Đây là một **debt-bondage subregime**.

### 15.4 PARTIAL CURRENT REVIVAL — legacy package không được phục hồi nguyên khối

**CURRENT CANON UPDATE — 2026-09-08:** revamp mới đã phục hồi một tập con có giới hạn:

```text
Undie internal Credit Line
→ chỉ dùng cho nhóm high-risk/high-reward shop đã nêu
→ status có thể làm collateral
→ default có thể đưa subject tới private red-light facility
→ facility quyết định giờ làm/pay tới khi trả xong
→ work time ≤ 16h/day
→ basic wage ≤ 20% minimum-wage range của nghề tương ứng
```

Phần này **không** tự phục hồi:

- black credit;
- full body-upgrade shop;
- toàn bộ legacy master-service/rate/tip implementation;
- mọi hạng mục, công thức hoặc authority không được revamp source xác nhận.

Vì vậy genealogy ở 15.1–15.3 được giữ, nhưng nhãn “toàn bộ retired” đã stale. Các điểm vẫn cần audit/giữ `UNKNOWN`:

- underwriting;
- valuation;
- collateral legality;
- default rule;
- assignment authority;
- dispute;
- exit;
- black-credit interface;
- centrality risk.

---

## 16. O — Death disposal gốc

### 16.1 DESIGN HISTORY

Concept cực hà khắc:

```text
Undie chết vì lao lực / bạo lực / tín dụng đen
→ trung tâm xử lý
→ phân rã phần hữu cơ
→ dùng làm phân bón
→ xương thiêu chung
→ hũ tượng trưng
→ gửi người thân nếu còn
→ nguyên nhân công khai: "tai nạn"
```

Đây là:

```text
death
→ material disposal
→ administrative closure
→ information suppression
```

### 16.2 FAILURE MODE

Nếu áp quá tuyệt đối, nó có thể thành:

```text
abuse
→ death
→ paperwork
→ disappear
```

tức một information sink quá mạnh.

---

## 17. O2 — Alternate tử tuất và tiền thân của current death benefit

### 17.1 DESIGN HISTORY

Vì O quá hà khắc, từng có alternate:

```text
Undie chết
→ xương cốt/hài cốt thiêu riêng
→ trả nguyên vẹn về gia đình
→ bồi thường
→ mức bồi thường theo vai trò lao động
```

Nhưng alternate cũ vẫn phân biệt nguồn người.

Một nhóm được hưởng treatment O2; Undie ngoại tỉnh từng vẫn có thể bị xử lý theo O cũ.

### 17.2 CURRENT CANON — source population

Current logic đã đổi.

Undie chủ yếu lấy nguồn từ **dân bên ngoài/ngoại quốc xin vào**, và Civil Slave cũng chủ yếu lấy nguồn từ population ngoại lai tương tự.

Do đó tử tuất current không phải hai chế độ tách rời:

```text
Civil death benefit
vs
Undie death benefit
```

mà có genealogy chung:

```text
FOREIGN / OUTSIDE POPULATION
→ voluntary intake
→ Civil
→ death benefit
```

và:

```text
FOREIGN / OUTSIDE POPULATION
→ Undie
hoặc
→ Civil → Undie
→ death benefit
```

Citizen AetherFire gần như không chủ động xung phong làm Undie dù route pháp lý có thể tồn tại.

### 17.3 Provenance exception

Trong vận hành hằng ngày:

```text
background/provenance
→ phần lớn không phải classification chính
```

Nhưng ở tử tuất:

```text
foreign provenance
→ có thể trở lại relevant
→ family/remains/compensation interface
```

Đây là một exception có function cụ thể, không mâu thuẫn với việc background bị vô hiệu hóa trong operational classification thường ngày.

---


## 18. P — Route mất status gốc của MC2: fiancé / nobles / identity intervention

### 18.1 DESIGN HISTORY

Một implementation cũ của fall-from-grace có chuỗi:

```text
MC2 từ chối nhượng bộ
→ hôn phu liên lạc, nói có cách đảo ngược tình thế
→ MC2 lén ra ngoài
→ hôn phu + nhóm quý tộc liên kết
→ xóa / thay đổi identity presentation
→ đổi tóc + mắt
→ đeo collar
→ dùng phép ngăn MC2 nói ra sự thật
→ đẩy MC2 vào Civil Slave
```

Trong architecture này, **actor gây cú rơi ban đầu** là hôn phu + quý tộc liên kết, thông qua betrayal, identity intervention và magic.

### 18.2 DESIGN FUNCTION

Requirement cốt lõi mà implementation này giải:

```text
Princess / Citizen MC2
→ mất protection + identity legibility
→ bị hệ thống đọc như Civil Slave
→ fall-from-grace bắt đầu
```

Nó tạo betrayal tension rất trực tiếp, nhưng gắn quá nhiều requirement vào một personal conspiracy.

### 18.3 CURRENT REFACTOR

Current route đã đổi sang:

```text
Princess / Citizen
→ fraudulent “voluntary” paperwork / status stripping
→ Civil Slave
→ MC2 tự chọn Civil → Undie
```

Thiết kế chuyển từ:

```text
personal betrayal
→ status collapse
```

sang:

```text
institutional political conflict
→ fraudulent status machinery
→ status collapse
```

Không tự mang các yếu tố cũ như fiancé betrayal, đổi tóc/mắt hoặc anti-truth spell vào current canon.

Điểm chống drift:

```text
P = DESIGN HISTORY
≠ current motive của fiancé
```

---

## 19. Q — Magic system gốc từng bị hút vào Undie gravity well

### 19.1 DESIGN HISTORY — magic centered around Undie

Concept gốc có một magic architecture mà nhiều implementation quan trọng xoay quanh shared Slave/Undie core.

Ví dụ nổi bật là **anti-mind-break magic** áp bắt buộc lên Undie nhằm kéo dài khả năng chịu đựng tâm lý và duy trì performance.

Cần tách nó khỏi mục M:

```text
M — stimulant
→ physical endurance / workload shortcut

Q — anti-mind-break magic
→ psychological breakdown resistance / performance continuity
```

Hai mechanism giải hai failure mode khác nhau.

### 19.2 DESIGN HISTORY — magic như glue/patch

Magic legacy còn xuất hiện ở route P:

- anti-truth / không thể nói ra sự thật;
- identity/body presentation intervention;
- các phép dùng để bảo đảm state mong muốn của pathway.

Pattern cũ thường gần:

```text
desired institutional/story state
→ magic implementation
→ guarantee state
```

Điều này rất hiệu quả để giữ local causal chain ngắn, nhưng dễ biến magic thành **glue/patch** nối các mechanism vốn nên có ontology riêng.

### 19.3 FAILURE MODE

Khi Undie đã là gravity well, magic bị hút theo:

```text
Undie centrality
→ magic implementation centrality
→ nhiều problem khác nhau dùng chung một magical shortcut
```

Khi current design tách POW, MC entry, status law và các subsystem khác khỏi Undie, các magic implementation cũ không còn tự động có lý do tồn tại.

### 19.4 CURRENT STATUS

Full current magic system hiện **deferred / chưa được khôi phục từ genealogy cũ**.

Không tự restore:

- anti-mind-break magic;
- anti-truth magic;
- identity-change magic;
- các spell chỉ tồn tại để guarantee old pathway.

Điểm chống drift:

```text
old magic implementation
= design history

current magic ontology
= separate unresolved subsystem
```

---

## 20. R — Thánh điện / Thánh quốc: counter-immoral institution

### 20.1 DESIGN HISTORY

Concept cũ có **Thánh điện** là tôn giáo chính thức của đế quốc, với:

- Thánh nữ;
- linh mục;
- giáo dân;
- Holy Guard;
- hệ phép thuật **Creed**;
- thánh tích và chức năng bảo vệ liên quan.

Thánh điện hoạt động như một **counter-immoral force** đối với chế độ Undie/shared Slave regime.

Thánh nữ công khai phản đối chế độ ngay bên trong đế quốc, thường xuyên:

- tổ chức biểu tình ôn hòa;
- vận động cải thiện đời sống Undie;
- tạo moral/public pressure đối với chính quyền.

### 20.2 DESIGN FUNCTION — vì sao đế quốc không cưỡng chế dẹp ngay

Đế quốc có lý do thực dụng để không xóa Thánh điện khỏi bàn chơi:

```text
Thánh điện
→ Creed magic
→ social pacification / xoa dịu dân chúng
→ bảo vệ một số yếu nhân
→ bảo vệ thánh tích
→ legitimacy tôn giáo
```

Do đó nhà nước chịu tension:

```text
MUỐN:
giảm opposition

NHƯNG CẦN:
Creed capability + social legitimacy + protection functions
```

Điều này tạo cost thật cho repression thay vì cho Thánh điện blanket immunity.

### 20.3 DESIGN HISTORY — covert link với Thánh quốc

Thánh điện nội địa còn có liên kết ngầm với một **Thánh quốc** bên ngoài và thường xuyên tuồn thông tin nội bộ sang đó.

Thánh quốc:

- ở sát biên giới;
- có vị trí cửa ngõ cho nhiều giao dịch thương mại;
- là tuyến lớn của đoàn hành hương;
- ảnh hưởng các đoàn người di chuyển/nhập tịch vào AetherFire.

Trong genealogy nơi Civil Slave và Undie có nguồn lớn từ population bên ngoài, Thánh quốc trở thành một **upstream gatekeeper/influence node** đối với dòng người đi vào.

Quan hệ đúng:

```text
Holy State
INFLUENCES / CAN_GATE
migration + pilgrimage + trade flows
```

không tự suy:

```text
Holy State
OWNS / CONTROLS ALL
Civil / Undie intake
```

### 20.4 DESIGN VALUE

R tạo một opposition institution có thể hoạt động công khai và hợp pháp một phần:

```text
Undie internal resistance
≠
religious public opposition
```

Thánh điện vẫn có thể tự tồn tại nếu bỏ Undie khỏi equation nhờ:

- religion;
- followers;
- Creed;
- Holy Guard;
- holy sites/relics;
- pilgrimage;
- foreign relation.

Do đó:

```text
Temple CAN_RUN_WITHOUT Undie
Temple INTERACTS_STRONGLY_WITH Undie
```

Đây là module độc lập hơn nhiều legacy bị hút vào Undie gravity well.

### 20.5 RECONSIDERATION STATUS

**UNDER CONSIDERATION — user đang cân nhắc mang lại.**

Nếu tái nhập cần giữ UNKNOWN ở:

- jurisdiction của Holy Guard;
- exact Creed capabilities;
- boundary giữa public opposition và sedition;
- exact leverage của Holy State lên migration/trade;
- mức độ intelligence leakage và counterintelligence response.

### 20.6 PROVENANCE ONLY — Holy State infiltration / T counteraction; punitive Undie endpoint removed

**DESIGN HISTORY / PROVENANCE ONLY — punitive Undie endpoint removed 2026-09-16**

Trong một số event của concept gốc, Thánh quốc không chỉ gây sức ép ngoại giao mà còn triển khai **lực lượng gián điệp/covert personnel** vào AetherFire.

Pathway cũ:

```text
Holy State
→ cử lực lượng gián điệp
→ liên lạc với Thánh điện nội địa
→ giả dạng giáo dân / tùy tùng của Thánh nữ
→ thâm nhập vào mạng xã hội–tôn giáo hợp pháp
→ tuyên truyền dưới vỏ bọc hoạt động ôn hòa
```

Mục tiêu là khai thác chính vùng hợp pháp mà Thánh điện đang có:

```text
peaceful religious activity
+ public legitimacy
+ entourage / follower access
→ covert influence cover
```

#### T phát hiện và công khai xử lý

Legacy T không chỉ bắt hoặc thủ tiêu bí mật mạng infiltrator. Trong event này, T **công khai quy kết** lực lượng đó đã:

- vi phạm hiến pháp;
- xâm phạm chủ quyền AetherFire;
- lợi dụng hoạt động tôn giáo ôn hòa làm vỏ bọc cho foreign covert action.

Causal function:

```text
T detects foreign penetration
→ public attribution
→ constitutional / sovereignty framing
→ exemplary punishment
→ foreign network bị bóc khỏi cover
```

#### Legacy sanction: cưỡng chế xuống Undie

Trong old implementation, T **đơn phương cưỡng chế các infiltrator xuống Undie**.

Function của sanction khi đó là:

```text
covert operative
→ identity/status destruction
→ public humiliation
→ exemplary deterrence
```

Undie vì vậy xuất hiện ở endpoint của event như một **public sanction / humiliation interface** của old shared Slave architecture.

Điều này không có nghĩa toàn bộ R2 được thiết kế để phục vụ narration Undie. Engine phía sau là:

```text
Holy State foreign policy
→ covert intelligence
→ religious social cover
→ T counterintelligence
→ sovereignty enforcement
→ public signaling
→ Temple deterrence
→ diplomatic / institutional consequences
```

#### Hai target của thông điệp

Target trực tiếp:

```text
foreign infiltrators
```

Target gián tiếp:

```text
Holy Temple
```

T dùng event để dằn mặt Thánh điện rằng:

```text
peaceful domestic opposition
≠ automatic security target

nhưng

foreign covert penetration through Temple networks
→ security / sovereignty threshold crossed
```

Vì vậy R2 tạo một boundary politics quan trọng giữa:

- dissent/advocacy hợp pháp;
- foreign interference;
- intelligence penetration;
- sovereignty enforcement.

#### UNKNOWN về knowledge/complicity của Thánh nữ

Chưa được chốt:

- Thánh nữ biết mạng gián điệp hay không;
- biết một phần hay hoàn toàn không biết;
- Thánh điện ở cấp tổ chức chủ động phối hợp tới đâu;
- mức nào là rogue/foreign-controlled network.

Không tự suy complicity chỉ từ việc infiltrator giả dạng giáo dân hoặc tùy tùng.

#### REMOVAL RECORD — 2026-09-16

Old sanction:

```text
foreign spy
→ forced punitive Undie transfer
```

xung đột với current Undie ontology đã đặt trọng tâm mạnh ở voluntary intake/consent và không dùng Undie như criminal-sexual punishment route.

Các function chính trị dưới đây chỉ được giữ để đọc design genealogy; chúng không phải đề xuất tái nhập R2 hoặc punitive Undie endpoint:

```text
SURVIVING DESIGN FUNCTION
= detect infiltration
+ public attribution
+ sovereignty enforcement
+ exemplary deterrence
+ indirect warning to Temple

OLD IMPLEMENTATION
= forced Undie sanction
→ không tự động phục hồi
```

Quyết định 2026-09-16 xóa toàn bộ foreign-spy punitive Undie route khỏi current canon và reconsideration vì nó không còn phù hợp với hướng political-centric của setting. Exact legal/status treatment thay thế cho spy giữ `UNKNOWN`; Criminal Slave → Undie vẫn bị cấm.

### 20.7 R3 — Holy State purist diplomacy, “terror welfare” và Undie treaty diplomacy

**DESIGN HISTORY / USER-PROVIDED STATE**

Tên là Thánh quốc nhưng external behavior trong old concept không được đọc như một “holy good-state”. Thánh quốc theo một đường ngoại giao **purist**, đồng thời dùng mô hình được user gọi là **terror welfare** đối với ba quốc gia nằm sát AetherFire.

Cấu trúc pressure cũ:

```text
Holy State
→ purity / moral superiority claim
→ welfare / patronage
+ intimidation / coercive pressure
→ neighboring states chịu ảnh hưởng
```

Ba quốc gia này dần không chịu được sự đạo đức giả/coercion của Thánh quốc và muốn ngả sang, thậm chí xin làm **chư hầu của AetherFire** thay vì tiếp tục chịu sức ép của Thánh quốc.

Điểm khởi đầu của quá trình này là **hiệp định mua bán Undie song phương** đã tồn tại trong old concept.

Causal role của hiệp định không chỉ là commerce:

```text
Undie bilateral trade agreement
→ legal / diplomatic channel
→ repeated state-to-state transaction
→ institutional familiarity / predictability
→ geopolitical alignment pressure
```

Điểm anti-drift:

```text
neighbor chooses AetherFire
≠
AetherFire morally better
```

Nó phản ánh strategic preference giữa các patron/regime khác nhau và perception rằng AetherFire có thể transactional/predictable hơn một Thánh quốc purist-coercive.

**DESIGN ANALYSIS:** current Foreign Affairs interest in exporting/replicating Undie abroad có structural resemblance với old treaty-diplomacy instinct, nhưng causal genealogy trực tiếp chỉ được coi là xác nhận nếu user chốt.

---

### 20.8 DESIGN HISTORY — học thuyết Thánh quốc cũ và nguồn tên Matriarch's Lament

**Lời kể lịch sử của người dùng, chưa phục hồi:** Thánh quốc thời RP cũ thờ Nữ thần Sự sống. Học thuyết của họ không công nhận lựa chọn tự nguyện bán dâm của phụ nữ là hợp lệ, nên diễn giải Undie như bằng chứng có cấu trúc ép buộc phía sau và nhiều lần tổ chức “giải cứu”. AetherFire xem các hành động đó là can thiệp vào nội bộ và chủ quyền. Đây là genealogy của tranh chấp tôn giáo, quyền lựa chọn và chủ quyền, không phải học thuyết được gán cho Matriarch's Lament hiện hành.

**Lời kể lịch sử của người dùng, chưa phục hồi:** `Matriarch's Lament` là tên từng có trong lore cũ. Bản cũ gắn tên này với một thánh nữ sáng lập: người xuyên thế giới cùng thế giới gốc với MC1 và MC3, esper có năng lực thanh tẩy cấp 7, về sau bị một tác nhân được gọi là AetherFire ám toán. Việc tên được dùng lại hiện nay không phục hồi tiểu sử hay sự kiện ám toán đó. Vị sáng lập này là một node riêng; **không đồng nhất với Trần Trúc Nha**.

**Chưa xác định:** thời điểm vị sáng lập sống, lập quốc và bị ám toán; tác nhân “AetherFire” là nhà nước hiện hành hay tiền thân; quan hệ giữa vụ ám toán với học thuyết chống Undie hoặc Total War cũ. Tuổi đời hiện hành của Matriarch's Lament và AetherFire không đủ để tự giải quyết niên đại này. Tuyến gián điệp nước ngoài → Undie trừng phạt ở §20.6 vẫn đã bị loại bỏ; lời kể về RP cũ không mở lại tuyến ấy.

Nguồn: `Source_Archive/aetherfire_rp_cu_ba_truc_lich_su_va_de_xuat.md`, mục 4; đây là bản thuật lại và phân tích, không phải biên bản RP độc lập.

## 21. S — Hội đồng Pháp sư: contingency institution và technical-magical power center

### 21.1 DESIGN HISTORY — political role

Concept cũ có **Hội đồng Pháp sư** với địa vị rất cao bên trong hệ thống chính trị.

Role mặc định của họ gần như trung lập:

```text
politics thường nhật
→ hạn chế can thiệp

policy đe dọa sự tồn tại / continuity của magical system
→ Hội đồng can thiệp
```

Họ không phải một đảng chính trị thông thường.

Nguồn leverage của họ là **technical-magical indispensability**.

### 21.2 DESIGN HISTORY — Neo Fantasy magic × technology integration

AetherFire cũ đã dùng logic Neo Fantasy trong đó:

```text
magic
×
technology
→ integrated infrastructure
```

Hội đồng Pháp sư cung cấp/giám sát magical implementation cho:

- hạ tầng;
- cơ cấu hành chính;
- xây dựng;
- magical security;
- seal/containment systems;
- các implementation nơi phép và công nghệ hòa vào nhau.

Do đó họ không chỉ là một “wizard guild” hay combat faction.

### 21.3 DESIGN HISTORY — artifact / thần khí / grimoire custody

Họ chuyên trách:

- quản lý;
- bảo quản;
- phong ấn;
- nghiên cứu;
- lưu trữ;
- chuẩn bị contingency

đối với:

- thần khí;
- artifact;
- grimoire;
- vật thể/tri thức bị corruption hoặc nguy hiểm.

Doctrine thiên về:

```text
classify
→ isolate
→ seal
→ preserve
→ reuse later if necessary
```

thay vì mặc định hủy.

### 21.4 DESIGN HISTORY — counter-force của Thánh điện

Thánh điện và Hội đồng Pháp sư không phải hai đảng mirror-image mà là hai doctrine khác nhau.

Thánh điện:

```text
unpure / corruption
→ mặc định moral danger
→ purge / destroy / sanctify bias
```

Hội đồng Pháp sư:

```text
corruption
→ risk + information + potential capability
→ contain / seal / preserve / contingency
```

Trục conflict:

```text
PURITY-FIRST
vs
CONTINGENCY-FIRST
```

Một bên hỏi gần với:

> “Thứ này có nên được phép tồn tại không?”

Bên kia hỏi gần với:

> “Nếu nó tồn tại, phải containment thế nào và có lúc nào cần dùng lại không?”

Đây là conflict doctrine/epistemology, không chỉ tranh ghế chính trị.

### 21.5 S2 — POW là elite specialists của Hội đồng Pháp sư

S là mảnh giải thích function cũ của POW.

Trong concept gốc:

```text
CATEGORY: Slave
├─ các population bị trị thông thường
└─ POW
    → elite specialist population
```

POW nằm **trên/ở cấp elite trong administrative category Slave nhưng không phải slave theo nghĩa Civil/Undie**.

Phải tách ba trục:

```text
ADMINISTRATIVE:
controlled under Slave umbrella

SOCIAL / FUNCTIONAL:
elite specialist

STRATEGIC:
high-value knowledge / capability asset
```

Hội đồng Pháp sư là institutional consumer/custodian quan trọng của POW expertise.

POW có thể mang:

- niche magic;
- rare bloodline;
- foreign grimoire tradition;
- artifact-handling method;
- seal technique;
- engineering knowledge;
- military magic;
- các capability mà Citizen hoặc elite AetherFire không có.

Theo design history đã chốt, **nhiều thành tựu lớn của Hội đồng Pháp sư có nguồn từ POW specialist**.

Causal function:

```text
foreign specialist capture
→ POW specialist pool
→ Mage Council absorbs / implements knowledge
→ magical engineering / artifact control / infrastructure advances
→ state capability ↑
```

POW vì vậy là một **knowledge-import engine**, không phải ordinary labor pool.

### 21.6 C + S combined failure — double tension tự phá specialist function

Khi ghép mục C và S, contradiction của old design hiện rõ:

```text
POW = rare elite specialist

nhưng

POW = bị kéo vào Undie-derived body/visual humiliation regime
```

Old implementation tăng drama nhưng giảm:

- cooperation incentive;
- dynastic/bloodline value;
- exchange value;
- specialist retention;
- legitimacy của việc dùng POW như expert.

Vì vậy refactor hợp lý không phải bỏ POW tension mà là:

```text
giữ POW grievance / conflict potential
→ thay nguồn tension theo ontology riêng của POW
→ bảo toàn specialist utility
```

### 21.7 CURRENT / RECONSIDERATION STATUS

**PARTIAL RESTORATION CONFIRMED.** Hội đồng Pháp sư không còn ở trạng thái “chỉ đang cân nhắc mang lại”. Current canon đã xác nhận ít nhất:

- Hội đồng Pháp sư tồn tại như một actor/institution hiện hành;
- Hội đồng là actor quan trọng trong coercive magic-tech integration của AetherFire;
- có hai chi nhánh lớn, gồm chi nhánh nội địa AF và chi nhánh Đông Bắc phía sau núi lửa;
- chi nhánh/site Đông Bắc có Học viện Phép thuật và khu nghiên cứu cơ thể người bên dưới;
- subjects nghiên cứu đến từ Elf, Thú Nhân, Long tộc phía Bắc;
- cult tận thế khai thác `fake POW → specialist` interface của Hội đồng, không thuộc Học viện.

Các phần legacy **chưa được tự động phục hồi toàn bộ** chỉ vì core institution đã trở lại. Vẫn giữ `UNKNOWN / UNDER CONSIDERATION` cho các trục chưa có chốt mới như:

```text
exact artifact/grimoire custody
+ full magical governance authority
+ exact current relation với POW specialist pool ngoài Y1
+ toàn bộ political neutrality doctrine cũ
+ exact jurisdiction giữa hai chi nhánh
```

Current POW architecture vẫn phải giữ distinction:

```text
public status = POW
internal security category = Slave
specialist role = separate
```

Không được suy `Mage Council exists` → `mọi POW thuộc Mage Council`.

---

## 22. T — Cụm Nội vụ–An ninh–Phản gián: practical security complex

### 22.1 DESIGN HISTORY — một tổ chức chung, nhiều tên ban/ngành

Trong concept gốc, **Bộ Nội vụ, Bộ An ninh và phản gián không phải ba institution độc lập hoàn toàn**. Chúng là các ban/ngành chức năng khác nhau bên trong **một tổ chức an ninh nội bộ chung**.

Quan hệ đúng ở design history:

```text
shared internal-security organization
├─ Interior-labelled functions
├─ Security-labelled functions
└─ Counterintelligence-labelled functions
```

Tên ban khác nhau biểu thị miền chức năng; không được đọc ngược thành ba power center tách biệt trong legacy architecture.

### 22.2 DESIGN HISTORY — lực lượng và công cụ vận hành

Tổ chức này từng sử dụng một hỗn hợp nhân lực và asset rất rộng:

- mật vụ;
- double agents;
- lính đánh thuê;
- spec ops;
- clone homunculus;
- các cá nhân được nuôi dưỡng trong lab;
- các cá nhân được chỉnh sửa bộ gen để mạnh hơn mức bình thường.

Đây không phải một line-job duy nhất mà là một **operational pool dị thể**, dùng asset khác nhau tùy loại rủi ro, địa bàn và đối tượng.

### 22.3 DESIGN HISTORY — Mage Council cung cấp hạ tầng

Hội đồng Pháp sư cung cấp một phần hạ tầng và capability cho tổ chức an ninh này theo tiêu chí:

> **“thà cẩn thận còn hơn bỏ sót.”**

Các interface cũ gồm:

```text
Mage Council
→ magical infrastructure / seals / countermeasure / specialist support
→ Internal-Security complex
```

Điều này không biến Hội đồng Pháp sư thành một nhánh của an ninh. Hai module độc lập tương tác vì an ninh cần countermeasure trước threat phép thuật mà automation thuần không xử lý chắc chắn.

### 22.4 DESIGN HISTORY — trung tâm giám sát tự động và lớp trực phép thuật

Legacy surveillance stack có:

- android và robot chạy chương trình cưỡng chế/tuần tra;
- camera và drone có AI;
- trung tâm giám sát tự động;
- lớp pháp sư đế quốc trực điều hành khi xuất hiện threat phép thuật.

Failure mode mà lớp pháp sư xử lý là các pháp sư của quốc gia đối địch dùng phép để:

- lẻn qua lớp giám sát thông thường;
- che giấu hiện diện;
- bypass hoặc làm sai lệch các hệ tự động;
- tạo intrusion mà camera/drone/robot không tự giải nghĩa được.

Causal separation:

```text
automation
→ baseline detection / monitoring / enforcement

foreign hostile magic
→ anomaly / bypass risk

Imperial mage operators
→ magical interpretation / countermeasure / live intervention
```

Không được suy AI tự có đầy đủ khả năng diễn giải mọi threat phép thuật.

### 22.5 DESIGN HISTORY — xử lý phản kháng và lớp “tai nạn / lao lực”

Trong death-handling legacy đã nói ở mục O, một phần đáng kể các trường hợp Undie chết được công bố/ghi nhận dưới nhãn **“tai nạn”** hoặc **“lao lực”** thực chất liên quan tới tổ chức này.

Theo chốt mới nhất, **khoảng 50% các vụ mang lý do lao lực trong lớp trường hợp này** là hậu quả của việc tổ chức an ninh xử lý khi hành động phản kháng của Undie gây **hiệu ứng lan vượt quá mức regime cho phép**.

Causal function cũ:

```text
Undie resistance action
→ spillover vượt ngưỡng chấp nhận
→ internal-security intervention
→ subject bị loại bỏ / chết
→ administrative cover: accident / overwork
```

Đây là **DESIGN HISTORY**, không tự import sang current death-benefit canon. Current O2/death-benefit architecture đã thay đổi và không được đọc như tiếp tục che phủ mặc định theo cơ chế này.

### 22.6 DESIGN HISTORY — cơ cấu nhân lực an ninh nội bộ

Legacy organization dùng nhiều nguồn nhân lực khác nhau:

#### Quý tộc và tướng lĩnh

Có **quý tộc và tướng lĩnh thực sự** trong core security structure.

Điểm cần giữ đúng là quý tộc được cân nhắc vì **thành tích/chính danh đã chứng minh**, không phải chỉ vì cha truyền con nối.

```text
noble status alone
≠ automatic security authority

recognized achievement / legitimacy
→ can justify high-trust placement
```

#### Quân chính quy

Một phần nhân lực đến từ quân chính quy, cung cấp trained force và interface với hệ quân sự.

#### Elite từ các công hội tự do

Các elite của free guild có thể làm việc theo **hợp đồng**, không mặc định trở thành permanent state personnel.

#### Lính đánh thuê tự do

Mercenary lực lượng tự do đặc biệt hữu dụng ở:

- thành phố vệ tinh;
- thuộc địa;
- các vùng xa nơi bộ máy trung ương không phủ dày.

#### Civil Slave

Civil Slave tham gia **nhiệm vụ hạ tầng** của hệ an ninh. Điều này không tự đồng nghĩa Civil có authority phản gián/spec-ops; cần tách labor/infrastructure contribution khỏi command/enforcement authority.

### 22.7 DESIGN FUNCTION — “phần thực dụng” của bộ máy

Module T được build để xử lý những xung đột mà các ban ngành khác có thể **đẹp và hợp thức trên giấy tờ nhưng không đủ năng lực giải quyết trong vận hành thực tế**.

Chức năng cốt lõi của nó là một operational integration layer giữa:

```text
policy
+ intelligence
+ coercion
+ covert action
+ magical countermeasure
+ contracted capability
+ remote-territory security
+ infrastructure support
```

Điểm mạnh của legacy design là **pragmatism**: khi formal bureaucracy không đủ, tổ chức này có sẵn nhiều loại actor và interface để đóng khoảng trống triển khai.

### 22.8 DESIGN VALUE / FAILURE RISKS

#### Giá trị

T tạo được một institutional answer cho các bài toán:

- ai xử lý threat nằm giữa police / military / intelligence;
- ai phản ứng khi automation gặp hostile magic;
- ai vận hành counterintelligence và double-agent network;
- ai có thể dùng capability hợp đồng bên ngoài state payroll;
- ai phủ security ở satellite/colony;
- ai xử lý resistance spillover mà public-facing institution không muốn chạm trực tiếp.

#### Failure risks nếu mang lại

Legacy này cũng có nguy cơ trở thành một **universal dirty-work solver** nếu phạm vi không được giới hạn. Cần đặc biệt giữ riêng:

```text
capability
≠ authority

covert capacity
≠ unlimited jurisdiction

Mage Council support
≠ Mage Council subordination

Civil infrastructure work
≠ Civil security mandate
```

Nếu mọi xung đột khó đều được giải bằng “an ninh xử lý”, module T sẽ tạo một gravity well mới thay cho Undie.

### 22.9 RECONSIDERATION STATUS

**DESIGN HISTORY + UNDER CONSIDERATION.**

User đang cân nhắc mang module T trở lại vì đây là một trong những phần thực dụng nhất của concept cũ và từng được thiết kế để xử lý khoảng cách giữa **formal institutional appearance** và **operational reality**.

Chưa tự chốt current ontology, exact authority, chain of command, legal mandate, relation với current Nội vụ/phản gián hoặc mức nào của legacy covert toolkit còn sống.

### 22.10 DESIGN HISTORY — T như counter-infiltration + counter-extraction institution

R2 không phải event duy nhất cho thấy T hoạt động ở boundary. Old T còn xử lý các nỗ lực **giải cứu / extraction** quanh MC2.

MC2 trong RP-era thường xuyên là rescue/intervention target. Hôn phu có tham gia một số attempt và từng cử lực lượng đi cứu, nhưng correction mới nhất xác nhận anh ta **chỉ là một trong các ứng viên/actor quanh MC2**, không phải rescuer trung tâm duy nhất. Actor có motive cứu MC2 thật sự mạnh còn thuộc đồng thời:

```text
Army
+ left-wing royal faction
```

Causal function của T trong các event này:

```text
observe repeated intervention pattern
→ infer likely extraction surface
→ prepare denial / interception / ambush
```

Một legacy event cực đoan dùng trạng thái thai nghén của MC2 như bait để kéo lực lượng cứu tới, trong khi T đã chuẩn bị phục kích sẵn.

**UNKNOWN / terminology conflict phải giữ:** user mô tả event này bằng cụm “cố tình làm lỗi trong quá trình triệt sản khiến cô có thai”, nhưng sau đó xác nhận systemic Undie policy của cùng old era là **tránh thai phép thuật có thời hạn**, không phải irreversible sterilization. Exact relationship giữa event-specific manipulation và policy chung chưa được ngoại hóa; không tự reconcile.

Từ R2 + các rescue event, doctrine cũ của T có thể nén ở cấp design function:

```text
foreign penetration
→ counter-infiltration

external rescue / extraction
→ counter-extraction
```

T đặc biệt nhạy với các actor cố xuyên strategic boundary mà state muốn giữ.

### 22.11 FAILURE MODE — competence singularity bóp chết narrative headroom

Lý do cốt lõi T hiện bị giữ ở `UNDER CONSIDERATION` không phải vì capability của nó thiếu hợp lý, mà vì legacy organization **quá hiệu quả**.

Nó gom gần một node:

```text
knowledge
+ surveillance
+ intelligence analysis
+ authority
+ covert capability
+ execution
```

Vì vậy causal chain dễ trở thành:

```text
detect
→ understand
→ decide
→ intercept
→ neutralize
```

quá nhanh, làm chết pathway/checkpoint trước khi chúng có headroom phát triển.

Current refactor chủ động tách legacy T thành ít nhất ba power center khác nhau:

```text
Bộ Nội vụ
Bộ An ninh
Bộ Phản gián
```

Mục tiêu không phải làm nhà nước kém thông minh mà phân tán:

```text
SEES
≠ UNDERSTANDS
≠ HAS AUTHORITY
≠ DECIDES
≠ CAN EXECUTE
```

Từ đó sinh ra:

- bất đối xứng thông tin;
- overlap jurisdiction;
- mandate conflict;
- withholding;
- decision latency;
- turf conflict;
- khác biệt giữa immediate enforcement và long-game intelligence.

Đây là **narrative headroom bằng institutional structure**, không phải plot armor do incompetence.

Nếu legacy T được mang lại, hướng refactor hợp lý về mặt history/reconsideration là:

```text
restore functions / capabilities selectively
≠
restore competence concentration nguyên khối
```

---

## 23. U — RP-era origin, strategic-goon phase và failure mode dẫn tới cải cách

### 23.1 DESIGN HISTORY — nguồn gốc project RP

AetherFire ban đầu là một **project roleplay xoay quanh Undie/MC2**. Theo user-provided provenance, giai đoạn khoảng **tháng 2–3/2026** project được phát triển nhiều trên Gemini trong thời kỳ user quan sát guardrail của model còn lỏng và model thường chủ động mở rộng nội dung.

Phần mô tả hành vi/version của Gemini là **USER-PROVIDED PROVENANCE**, không được coi là verified product history nếu chưa kiểm tra nguồn ngoài.

Điểm genealogy quan trọng hơn:

```text
MC2 / Undie RP foreground
→ là origin format

không đồng nghĩa

world core chỉ có Undie
```

### 23.1A DESIGN HISTORY — Undie ban đầu và lý do subsystem lan rộng

**Lời kể lịch sử của người dùng:** ở giai đoạn RP đầu, Undie được hình dung là mại dâm cao cấp với người tham gia về nguyên tắc tự nguyện, chưa phải nô lệ hay nô lệ tình dục. RP quanh dịch vụ này nhanh chóng lặp lại; câu hỏi thiết kế chuyển sang phản ứng của xã hội và thế giới, kéo theo luật, tiền công, điều kiện sống, chợ đen, thuế, du lịch, ngoại giao, tôn giáo và phản gián. Đây là giai đoạn thiết kế cũ, không phủ nhận các giai đoạn về sau đã viết Undie theo mô hình khác.

**Suy luận của bản tổng hợp RP:** vai trò làm điểm chạm cho nhiều miền có thể giải thích vì sao subsystem Undie trở nên dày hơn chức năng ban đầu. Đây là cách đọc genealogy, không phải nguyên nhân đã được kiểm chứng độc lập.

**Ranh giới hiện hành:** người dùng dự định thiết kế lại Undie cho cả Canon 1 và Canon 2 sau điểm tách nhánh V0.5, rồi chốt riêng. Ý định đó đang được cân nhắc; mục lịch sử này không sửa ontology, tình trạng pháp lý hay niên đại của hai canon.

Nguồn: `Source_Archive/aetherfire_rp_cu_ba_truc_lich_su_va_de_xuat.md`, mục 2–3; bản thuật lại, không phải biên bản RP độc lập.

### 23.2 DESIGN HISTORY — MC1 và MC3 lúc đó mới là proto-concepts

Trong early RP era, MC1 và MC3 **mới bắt đầu thành hình và chưa có role rõ ràng**.

Không được project ngược current meta architecture về giai đoạn này:

```text
current MC1 = Fictionize author/operator
current MC3 = POC trajectory actor/editor
V0.5 / V1.0 / clash architecture
```

đều là các lớp phát triển/refactor sau.

Cách đọc đúng:

```text
old MC2 + AetherFire core
→ chín trước

MC1 / MC3
→ proto-formed later into current metafiction roles
```

### 23.3 DESIGN HISTORY — old Undie reproductive regime và MC2 trophy-wife phase

Old Undie regime **chưa dùng irreversible sterilization** như current ontology. Biện pháp chung là:

```text
temporary magical contraception
```

Do đó fertility vẫn có thể trở lại và giữ strategic/dynastic value.

Sau khi MC2 đạt trạng thái **dead-heart**, narrative cũ đi vào một phase khác:

```text
before dead-heart
→ break resistance

after dead-heart
→ exploit remaining value
```

MC2 từng đi tới **trophy-wife phase** trong tầng quý tộc cao. Function không chỉ là status display mà còn liên quan việc sinh hậu duệ mang **Raging Phoenix**.

MC2 lúc đó đồng thời có:

- royal legitimacy;
- Raging Phoenix bloodline;
- fertility;
- dynastic value;
- symbolic/status value.

Vì vậy old trophy-wife route là một giao điểm của adult foreground với dynastic/state politics.

##### CURRENT CANON UPDATE — MC2 là ngoại lệ sinh sản

Latest canon **không** phục hồi old reproductive regime cho toàn bộ Undie. Quy tắc hiện tại phải tách:

```text
Undie thông thường
→ triệt sản bắt buộc, không đảo ngược

MC2
→ ngoại lệ do nhà nước cố ý tạo
→ không bị triệt sản
→ dùng tránh thai phép thuật tạm thời
→ fertility / Raging Phoenix reproductive value được giữ lại
```

Do đó:

```text
old temporary-contraception regime for all Undie
≠ current ontology

current MC2 exception
DERIVES_FROM / echoes old design logic
nhưng chỉ áp lên MC2
```

Động cơ current đã được user xác nhận ở tầng chiến lược: MC2 là bearer của huyết hệ Raging Phoenix mẫu hệ và có giá trị chính danh/sinh sản đặc biệt; nhà nước **cố ý** không áp vô sinh vĩnh viễn lên cô. Exact medical/magical protocol ngoài việc tránh thai tạm thời giữ `UNKNOWN`.

## 23.4 DESIGN HISTORY — True Crown, mẫu hệ và Raging Phoenix seal

Old AetherFire được xây trên **long mạch**. Dưới long mạch tồn tại một **thực thể cổ xưa có khả năng gây tận thế**. Dòng máu **Raging Phoenix** theo mẫu hệ giữ vai trò phong ấn thực thể này.

Causal architecture cũ:

```text
long mạch
→ existential strategic site

ancient entity
→ apocalypse risk

Raging Phoenix maternal bloodline
→ seal continuity

True Crown
→ legitimacy gắn với continuity của bloodline / seal
```

Do đó mẫu hệ không được đọc như một claim rằng xã hội AetherFire tôn trọng phụ nữ nói chung. Nó là một **succession/legitimacy requirement gắn với existential function**.

Điểm anti-drift:

```text
Undie regime
≠
contradiction với matrilineal True Crown
```

Hai thứ nằm trên hai trục status/function khác nhau.

### 23.5 DESIGN HISTORY — quân đội, True Crown và các rescue actor quanh MC2

Quân đội old era là **phe chủ chiến**, không phải kháng chiến. Doctrine loyalty của họ:

```text
Army
→ oath to True Crown

không phải

Army
→ blanket loyalty to entire royal family
```

Vì vậy:

```text
Royal Family
≠ True Crown
```

Một actor thật sự muốn cứu MC2 thuộc đồng thời quân đội và **hoàng thất cánh tả**. Điều này không suy rằng toàn Army = left-wing royal faction; chỉ actor đó nằm trên cả hai graph.

Hôn phu của MC2 chỉ là **một trong các ứng viên/actor cạnh tranh quanh cô**. Anh ta có tham gia một số rescue pressure nhưng không được over-centralize thành nguồn cứu duy nhất.

### 23.6 DESIGN HISTORY — old geopolitical pressure cooker

Old AetherFire có một trục chính trị–địa chính trị mạnh song song với MC2 narrative.

AetherFire nằm ở vị trí trung tâm và trên long mạch. Các pressure vector lớn:

```text
WEST
→ nền/vùng văn hóa lấy cảm hứng Trung Hoa
→ nguồn visual tradition bị old Undi cố ý vay rồi bôi xấu / hạ nghĩa biểu tượng

NORTH
→ các bộ tộc thường xuyên quấy rối

EAST
→ Holy State
→ religion / trade / pilgrimage / espionage / purist coercion

SOUTH
→ apocalypse cults
+ ngoại tộc / nhà ngoại MC2
```

Old Undi vì vậy từng có một lớp **cultural-geopolitical humiliation**: visual language của phía tây được AetherFire recontextualize vào regime Undie với mục đích bôi xấu. Đây là **DESIGN HISTORY**, không tự import motive này sang current Undi canon.

### 23.7 DESIGN HISTORY — nội bộ old AetherFire là nhiều vector cạnh tranh

Các actor/faction đồng thời tạo pressure:

- quân đội / True Crown;
- royal factions;
- quý tộc trong nước tranh giành MC2;
- anh em hoàng gia tranh sự sủng ái của MC2;
- nhà ngoại MC2 vận động hành lang, kích cánh hữu phá ngang politics nội bộ;
- tư nhân opportunistic “đục nước béo cò”;
- T;
- Thánh điện;
- Hội đồng Pháp sư;
- kháng chiến;
- cult tận thế.

Old resistance có thật nhưng motive chủ yếu gần:

```text
terror / disruption / destabilization
```

chứ chưa có political program/phương án thay thế rõ như current resistance.

Cult tận thế còn khống chế tinh thần MC2 để dùng cô như một interface/trigger liên quan mục tiêu tận thế. Exact magical mechanism giữ `UNKNOWN`.

Nhà ngoại MC2 có influence thông qua lobbying và kích hoạt cánh hữu, nhưng không được suy họ **control toàn bộ cánh hữu** nếu chưa có source cụ thể hơn.

### 23.8 DESIGN HISTORY — MC2 là convergence node, nhưng không phải reason-for-existence của world

Old MC2 hội tụ nhiều resource/function:

```text
royal legitimacy
+ Raging Phoenix
+ seal relevance
+ fertility
+ dynastic value
+ symbolic value
```

Vì vậy nhiều actor có motive độc lập để:

- cứu;
- sở hữu;
- kiểm soát;
- cưới;
- khai thác;
- bảo vệ;
- dùng MC2 làm trigger.

Điều này giải thích MC2-centric narrative mà không cần suy “mọi faction tồn tại chỉ vì MC2”.

### 23.9 CORE FAILURE MODE — complexity không cứu được narrative một chiều

Vấn đề cốt lõi của old AetherFire **không phải thiếu chiều rộng hay chiều sâu**. Nó có cả hai. Failure mode nằm ở **narrative geometry**.

Trước dead-heart:

```text
MC2 state / choice / rescue / capture
→ còn làm đổi pathway
```

Sau dead-heart, các faction đã tích đủ momentum để chuyển sang:

```text
TOTAL WAR
```

Dù MC2 còn hiện diện hay không, nhiều phe vẫn tiếp tục đánh nhau vì:

- lực lượng;
- alliance;
- geography;
- logistics;
- ideology;
- resource;
- accumulated grievance.

Khi đó MC2 từ actor dần thành **completed trigger**, và fiction chuyển từ MC-driven narrative sang thứ user gọi là **statistical fiction**:

```text
force distribution
+ resources
+ alliances
+ attrition
→ macro outcome
```

World autonomy tự nó không phải lỗi. Lỗi là:

```text
WORLD AUTONOMY
→ CHARACTER CAUSAL LEVERAGE ≈ 0
```

Đây là lý do cải cách quan trọng hơn các vấn đề “goon”, complexity hay Undie centrality.

### 23.10 CURRENT DESIGN DIRECTION — chia narrative, phân rã faction và giữ headroom

**CURRENT DESIGN DIRECTION — user-confirmed direction, chưa tự coi mọi implementation cụ thể là canon.**

Hướng mới là chia narrative thành **ít nhất ba trục/narrative line**, thay vì để toàn bộ world hội tụ vào một dominant funnel.

Các faction/legacy module có khả năng được mang lại sẽ được:

```text
legacy faction / complex
→ phân rã thành actor/institution nhỏ hơn
→ giữ function đáng giá
→ tạo dependency có điều kiện
+ đối kháng / cạnh tranh
+ bất đối xứng thông tin
+ khác biệt mandate / authority
```

Mục tiêu:

```text
INTERDEPENDENCE
+ OPPOSITION
→ pathway headroom
```

Không phục hồi mô hình một super-node đủ knowledge + authority + capability để tự giải quyết mọi conflict.

Về framing thể loại:

```text
ARC 1
→ vẫn giữ một phần adult theme

PHẦN CÒN LẠI
→ thuần chính trị / institutional / geopolitical narrative
```

Adult theme vì vậy trở thành **bounded thematic domain**, không còn là premise áp lên toàn bộ map.

Direction mới giải trực tiếp core failure:

```text
OLD:
complex world
→ one narrative funnel
→ dead-heart
→ total war
→ statistical fiction

NEW:
multiple narrative axes
→ decomposed institutions
→ interdependence + conflict
→ information/authority asymmetry
→ actors retain causal leverage
→ ending can exist without middle being pre-solved
```

---

### 23.11 DESIGN HISTORY / INFERENCE / PROPOSAL — ba trục và vòng phản hồi RP cũ

**Lịch sử do người dùng kể, được bản tổng hợp sắp xếp thành ba trục:** (1) MC2 và đời sống Undie là camera RP trực tiếp; (2) bộ máy AetherFire phải giải thích, quản lý và phản ứng với hệ quả; (3) các nước ngoài phản ứng qua kinh tế, văn hóa, tôn giáo, tình báo và quân sự. Cách phân trục là công cụ phân tích, không phải sơ đồ thể chế canon.

**Suy luận:** một hành động của nhân vật đòi hỏi thể chế phản ứng; phản ứng đó tạo hệ quả quốc tế; sức ép quốc tế lại buộc thể chế thích nghi và tác động ngược lên nhân vật. Vòng lặp giúp giải thích vì sao các mắt xích cục bộ có thể hợp nhân quả dù điểm đầu và kết quả Total War nghe lệch tông. Nó không chứng minh mọi xung đột cũ đều bắt nguồn từ Undie hoặc bắt buộc dẫn tới chiến tranh.

**Đề xuất để cân nhắc:** nếu tái dùng genealogy, tách ngòi nổ RP khỏi nền lợi ích và điều kiện cho phép leo thang; giữ đường hạ nhiệt qua thương lượng, thông tin không đầy đủ, giới hạn thẩm quyền, chia rẽ nội bộ, chi phí chiến tranh và hậu cần. Tránh buộc mọi trục hội tụ vào một người hoặc một subsystem. Không đề xuất nào ở đây tự trở thành quy tắc canon.

Nguồn: `Source_Archive/aetherfire_rp_cu_ba_truc_lich_su_va_de_xuat.md`, mục 9–11, 16–17. Các mục về dead-heart và Total War đã có trong §23.8–23.10 nên không lặp lại.

## 24. V — Hoa Nguyệt / Tây quốc: đối trọng văn minh, dark foundation và hai triết lý phép thuật

### 24.1 CURRENT CANON + DESIGN HISTORY — vị trí và căn tính quốc gia

Tên chính thức đã có từ concept cũ và vẫn được giữ trong canon hiện tại:

> **Hoa Nguyệt**

`Tây quốc` là shorthand địa lý từ góc nhìn AetherFire, không phải tên chính thức.

AetherFire cố ý đảo trực giác địa lý ngoài đời: các cảm hứng Trung Hoa và Nhật Bản được hợp nhất thành **một quốc gia ở phía tây AetherFire**. Hanfu, Kimono/Yukata và các truyền thống thị giác tương ứng thuộc hệ quốc phục/văn hóa của Hoa Nguyệt.

Hoa Nguyệt là một trong các quốc gia đối địch của AetherFire.

**UNKNOWN:** exact Hán tự của chữ “Hoa” chưa được user chốt trong source này. Không tự canonize `花`, `華` hay một chữ khác chỉ từ âm đọc.

### 24.2 CURRENT CANON — nhân quyền, hiệp khách và căn tính phép thuật

Hoa Nguyệt hiện tại:

- tôn trọng quyền con người;
- tồn tại truyền thống **đại hiệp / nam hiệp / nữ hiệp** đi khắp thế giới hành hiệp nghĩa;
- coi phép thuật phải có căn tính gắn với truyền thống huyền học phương Đông;
- võ thuật và phép thuật gắn chặt với căn tính, tố chất và mức hòa hợp của người sử dụng.

Quan hệ đúng:

```text
martial art
+ magic
+ aptitude
+ identity
+ tradition
→ compatibility / harmony
```

Không tự suy hiệp khách là cơ quan nhà nước, quân đội hay tình báo Hoa Nguyệt. Exact relation giữa hiệp khách và state authority giữ `UNKNOWN`.

### 24.3 CURRENT CANON — AetherFire là coercive integration, không phải harmony integration

AetherFire vẫn là Neo Fantasy tích hợp công nghệ và phép thuật ở cấp output/hạ tầng, nhưng mechanism/philosophy mới được user xác nhận là **cưỡng ép compatibility** nhiều hơn hòa hợp tự nhiên.

```text
AetherFire:
magic + technology
→ nếu không tương thích tự nhiên
→ engineering / interface / coercive integration
→ buộc chúng chạy cùng
```

Hội đồng Pháp sư là một actor quan trọng giúp thực hiện integration này.

Một phần Thánh điện cũng tham gia/thỏa hiệp khi có lợi ích phù hợp; điều đó không có nghĩa Thánh điện từ bỏ doctrine hay hoàn toàn đồng ý với Hội đồng Pháp sư.

```text
DOCTRINAL CONFLICT
≠ ZERO COOPERATION
```

Đối lập Hoa Nguyệt–AetherFire vì vậy không chỉ là geopolitical rivalry mà còn là hai philosophy khác nhau về magic:

```text
Hoa Nguyệt
→ identity / aptitude / harmony / tradition

AetherFire
→ implementation / engineering / forced compatibility
```

### 24.4 DESIGN HISTORY + CURRENT SYMBOLISM — Undi như cultural degradation

Genealogy/current symbolism của Undi phải đọc thêm một lớp:

```text
Hoa Nguyệt
→ Hanfu + Kimono/Yukata là national-cultural dress

AetherFire
→ vay silhouette / motif
→ tái mã hóa thành Undi
→ cố ý bôi xấu / hạ nghĩa biểu tượng của đối thủ
```

Vì vậy Undi vừa là class/status readability trong AetherFire, vừa mang lớp **geopolitical-cultural humiliation** đối với Hoa Nguyệt.

Không được giảm relation này thành “AetherFire dùng đồ ngoại lai vì sexy”.

### 24.5 CANON — “Hoa” là tên đẹp che một dark founding referent

Hoa Nguyệt **tự đặt** chữ/tên “Hoa” cho mình. “Hoa” không chỉ là mỹ từ thơ mộng.

Canon được user xác nhận:

```text
thí nghiệm lên cơ thể người
→ cơ thể bị chia thành các phần đồng đều
→ hình học tổng thể thành “Hoa”

phần tâm của Hoa
→ Lục Kì Nhân
→ sáu vị thánh nhân

linh hồn của sáu người
→ làm trấn
→ trấn quốc đại trận của Hoa Nguyệt
```

Do đó current human-rights orientation của Hoa Nguyệt **không** được suy thành một lịch sử lập quốc sạch.

```text
CURRENT ETHICS
≠ INNOCENT FOUNDATION
```

Cũng không tự suy current harmony doctrine là hậu quả trực tiếp của founding experiment nếu user chưa xác nhận causal link đó.

### 24.6 DESIGN HISTORY — tên AetherFire và intended semantic field

**USER-PROVIDED REAL-WORLD INSPIRATION / UNVERIFIED IN THIS FILE**

User cho biết `Aether` trong tên AetherFire được lấy cảm hứng từ *Grim Dawn*, nơi theo trải nghiệm/diễn giải của user nó là nguồn năng lượng dạng lửa có tính hủy diệt và gây dị biến cho người chịu ảnh hưởng.

Intended semantic field của tên AetherFire từ rất sớm là:

```text
hỏa ngục
+ trầm luân
+ hủy diệt
+ dị biến
```

Điểm genealogy đáng giữ:

```text
AetherFire
→ dark meaning nằm ngay trên tên

Hoa Nguyệt
→ tên bề mặt thơ/mỹ
→ dark founding referent nằm bên dưới
```

Đây là design contrast, không tạo moral ranking sạch giữa hai quốc gia.

---

### 24.7 DESIGN HISTORY — dòng tiền, kế vị và bất đối xứng quân sự trong RP cũ

**Lời kể lịch sử của người dùng:** ma sát Hoa Nguyệt–AetherFire có từ thời chợ đen. Một bộ phận công dân Hoa Nguyệt lén sang AetherFire dùng dịch vụ Undie, tạo dòng người và tiền xuyên biên giới. AetherFire dùng nguồn thu này khi thiếu vốn; một số lãnh đạo Hoa Nguyệt thấy lợi ích kinh doanh và nhà nước cũng hưởng thuế liên quan. Chỉ trích về lương và điều kiện sống của Undie có thể đi cùng lợi ích kinh tế đó. Tính hợp pháp, cơ chế thuế và tỷ lệ thu chính xác vẫn chưa xác định.

**Lời kể lịch sử của người dùng:** một Thái tử Hoa Nguyệt bí mật sang AetherFire rồi đột tử; lý do công bố là “lao lực”. Sau đó AetherFire cáo buộc Thái tử kế nhiệm là con của tiên đế với người hầu, trái với phả hệ chính thức. Tính đúng sai và bằng chứng của cáo buộc chưa được xác nhận. **Suy luận:** khi một người kế vị chết trên đất AetherFire rồi nước này công kích chính danh người kế nhiệm, tranh chấp chuyển từ sự cố ngoại giao sang vấn đề kế vị; sự kiện đơn lẻ không đủ để suy ra chiến tranh tất yếu.

**Lời kể lịch sử của người dùng:** thế đối trọng cũ đặt khoa học–phép thuật AetherFire cạnh ưu thế đại trận của Hoa Nguyệt. Sau dead-heart, MC2/Raging Phoenix bị AetherFire khai thác như tài sản chiến lược, làm lệch tính toán sức mạnh trong RP cũ. Thời điểm chính xác và năng lực tác chiến không đủ rõ để ánh xạ vào canon hiện hành.

Nguồn: `Source_Archive/aetherfire_rp_cu_ba_truc_lich_su_va_de_xuat.md`, mục 5–8. Những quan hệ kinh tế, triều đại và quân sự này là genealogy; không cập nhật Hoa Nguyệt hay MC2 trong current canon.

## 25. W — Tam cường phương Bắc, long mạch và chiến tranh bị khóa bởi lợi ích tồn vong

### 25.1 CURRENT CANON — ba cường quốc phương Bắc

Phía bắc AetherFire có ít nhất ba cường quốc phi nhân loại thường xuyên đánh xuyên biên giới AetherFire.

#### Elf

Elf là **một quốc gia thống nhất**, không phân chia chính trị dựa trên sắc tộc và không lấy kỳ thị sắc tộc làm nguyên lý tổ chức.

```text
Elf
→ con của Thần Cây
→ một polity thống nhất
→ sức mạnh khác nhau theo năng lực
```

Không tự suy khác biệt năng lực = caste/hierarchy chính trị nếu chưa có canon.

#### Thú Nhân

Thú Nhân là **một đại quốc thống nhất**, không phải mặc định là tập hợp các bộ lạc rời.

#### Long tộc

Long tộc là một cường quốc và bao gồm ít nhất:

```text
Vrouvre
Dragon
```

Exact biological/political relation giữa Vrouvre và Dragon giữ `UNKNOWN`.

### 25.2 CURRENT CANON — vì sao ba cường quốc chưa chọc thủng AetherFire

Việc AetherFire chưa bị xuyên thủng **không** được giải thích bằng việc ba nước phía Bắc yếu.

Các ràng buộc user đã xác nhận gồm:

- xung đột chính trị;
- xung đột sắc tộc/chủng tộc ở cấp liên-group/liên-quốc gia;
- địa chính trị;
- lợi ích không đồng nhất;
- cấu trúc long mạch và các chức năng phong ấn/rào chắn sâu hơn.

Quan hệ anti-drift:

```text
cùng là kẻ thù của AetherFire
≠ tự động là đồng minh chiến lược hoàn chỉnh của nhau
```

### 25.3 CURRENT CANON — Raging Phoenix và hàng rào thủy tổ

AetherFire nằm trên long mạch. Dưới long mạch có thực thể cổ xưa có khả năng gây tận thế; dòng Raging Phoenix của hoàng tộc giữ chức năng trấn áp/phong ấn liên quan tới cấu trúc này.

Song song, **thủy tổ của ba tộc phía Bắc** có chức năng tạo/duy trì một **rào chắn chủng tộc đối với các chủng tộc không phải con người**.

Phải giữ riêng:

```text
Raging Phoenix lineage
→ suppression / seal function

progenitors of northern three peoples
→ non-human racial-barrier function
```

**UNKNOWN:** exact metaphysical relation giữa hai lớp, phạm vi địa lý, target chính xác của barrier, và việc chúng có cùng một grand formation hay không. Không tự hợp nhất thành một mechanism duy nhất.

### 25.4 CURRENT CANON — Raging Phoenix truyền theo mẫu hệ và chỉ truyền cho con gái

Raging Phoenix:

```text
maternal lineage
→ truyền qua dòng mẹ
→ chỉ truyền cho con gái
```

MC2 vì vậy là một bottleneck vừa về chính danh vừa về continuity huyết hệ.

### 25.5 CURRENT CANON — motive của quý tộc đối với MC2

Động cơ cốt lõi của các quý tộc muốn bẻ MC2 không chỉ là humiliation hoặc loại bỏ một claimant.

Họ muốn:

```text
bẻ agency của MC2
→ kiểm soát / nhân giống huyết hệ của cô
→ dùng MC2 làm nguồn chính danh cho quyền cai trị AetherFire
→ tạo con gái mang Raging Phoenix
→ tạo các nhánh hậu duệ có legitimacy
```

Điểm chính trị là biến MC2 từ một claimant độc lập thành **dynastic reproductive anchor** cho faction khác.

Một **thuyết âm mưu** tối hơn tồn tại trong setting:

```text
con đầu lòng là con gái
→ giấu khỏi public succession
→ nuôi riêng
→ tiếp tục nhân giống nhánh đó
```

Canon ở đây là **sự tồn tại của thuyết âm mưu**; không tự suy kế hoạch này đã được thực thi thành công, cũng không tự bịa mechanism đảm bảo giới tính con đầu lòng.

### 25.6 CURRENT CANON — lobbying của nhà ngoại MC2 có structural stake

Nhà ngoại MC2 liên tục lobbying và tác động cánh hữu nội bộ không phải một complication ngẫu nhiên.

Họ có stake trực tiếp vào:

```text
MC2
→ maternal lineage
→ Raging Phoenix continuity
→ True Crown legitimacy
→ regional / existential seal value
```

Exact mix giữa tình thân, quyền lợi gia tộc, kiểm soát lineage và chiến lược địa chính trị giữ theo actor-specific evidence; không tự flatten thành một motive duy nhất.

### 25.7 CANON 1 — ngai vàng, dynastic export và cái chết của MC2

Canon 1 được làm rõ thêm:

```text
MC2 nhượng bộ
→ quý tộc ép/đưa cô lên ngôi
→ dùng ngai để hợp thức hóa lineage quanh cô
→ sinh hậu duệ
→ gửi/kết hôn hậu duệ như bàn đẩy chính trị
→ tạo các nhánh huyết thống tiếp tục có tính hợp pháp
→ các quốc gia con người lo ảnh hưởng quý tộc AetherFire quá lớn
→ hợp lực/thủ tiêu MC2
→ MC2 chết / martyr
→ tuyến hôn phu bùng lên như hệ quả
→ tiến tới collapse của AetherFire theo Canon 1
```

Do đó tuyến hôn phu trong Canon 1 không phải nguyên nhân đầu tiên của toàn bộ crisis; nó là một **downstream consequence** của dynastic competition + foreign balancing + cái chết của MC2.

### 25.8 CURRENT CANON — Clash #1 phá pathway nhưng không xóa strategic value của MC2

Sau Clash #1, MC2 lệch khỏi quỹ đạo Canon 1 và đi tới current Undie pathway. Nhưng các primitive chiến lược của cô không biến mất:

```text
MC2 còn sống
+ Raging Phoenix
+ True Crown legitimacy
+ maternal reproductive continuity
→ foreign rivals vẫn theo dõi cô chặt
```

Không cần các quốc gia đối địch biết `Canon 1/Canon 2`; surveillance của họ có thể xuất phát hoàn toàn từ thông tin địa chính trị nội sinh.

### 25.9 CURRENT CANON — MC2.1 là một HOPE pathway do MC3 gài từ Fiction 0

MC2.1 phò tá MC2 là một **HOPE pathway** mà MC3 đã gài từ Fiction 0.

Điểm anti-drift:

```text
Hoa Nguyệt / hiệp khách ecology
→ đã có ontology riêng để host MC2.1

MC3 / POC / HOPE
→ tạo hoặc mở causal pathway để MC2.1 có thể đi vào quỹ đạo phò tá MC2
```

Không được suy:

```text
MC3 tạo ra Hoa Nguyệt để chứa MC2.1
```

hoặc:

```text
HOPE pathway → MC2.1 mất agency / buộc phải cứu MC2
```

MC2.1 vẫn là actor có agency riêng; pathway tạo khả năng/giao điểm, không tự chọn mọi hành động hay outcome.

### 25.10 CURRENT CANON — ý nghĩa của Clash #1; Clash #2 giữ UNKNOWN khác loại

Clash #1 **không phải ngẫu nhiên**.

AetherFire từ root là một grimdark architecture, không có một “hope faction” sạch để HOPE chỉ việc nối vào. MC3 đưa `HOPE` từ Fiction 0 vào như một possibility-value ngoại lai đối với trajectory đang có.

```text
existing grimdark trajectory
×
MC3 / POC injects HOPE
→ Clash #1
→ divergence / pathways mới
```

`HOPE` ở đây:

```text
= possibility that things can go differently
≠ guaranteed good outcome
≠ utopia
≠ moral faction
```

Clash #2 đã được user xác nhận là **một kiểu khác Clash #1**. Exact thematic/mechanical nature của Clash #2 hiện `UNKNOWN` và sẽ được xác nhận sau; không tự dựng symmetry kiểu HOPE/anti-HOPE hay mirror inversion.

---

## 25A. X — Raging Fire, hidden genealogy và knowledge war

### 25A.1 CURRENT CANON — Raging Fire là lineage gốc; Raging Phoenix là tên bị AetherFire đặt lệch

Mẹ MC2 thuộc **huyết hệ hoàng tộc Raging Fire bên trong liên hiệp RF ở phía Nam**. `Raging Fire` là tên/căn tính gốc của lineage. Khi lineage đi vào hệ AetherFire, AetherFire đổi `Fire` thành `Phoenix` vì không muốn `Fire` của một vương tộc khác cạnh tranh/đè semantic identity của `Fire` trong `AetherFire`.

```text
Raging Fire
→ original lineage name

Raging Phoenix
→ AetherFire-assigned/reinterpreted name
```

`Fire` trong Raging Fire có nghĩa **tái sinh bên trong ngọn lửa**, không đồng nhất semantic field với `Fire` của AetherFire.

### 25A.2 CURRENT CANON — parentage thật của MC2 và Queen hiện tại

MC2 **không phải con ruột của vị vua AetherFire đã bỏ trốn**.

Mẹ MC2 đã mang thai trước khi vào hoàng gia AetherFire. Cha ruột MC2 về sau được chốt là **Hoàng tử thứ 9** của hoàng gia một quốc gia thành viên rank thấp hơn trong RF, đồng thời là chồng thật của mẹ MC2.

Sau succession struggle tại quốc gia thành viên nơi Prince 9 xuất thân:

```text
anh em đoạt vị
→ Prince 9 bị giết
→ mẹ MC2 đang mang thai
→ bị gả đi để che giấu pregnancy
→ về sau đi vào hoàng gia AetherFire
```

Quan hệ giam giữ cũ phụ thuộc Quad Night đã bị orphan. Current custodian của Hoàng hậu/mẹ MC2 giữ `UNKNOWN`; không tự chuyển bà sang ML hoặc TE.

### 25A.3 CURRENT CANON — trait ẩn của hoàng tộc Raging Fire

Hoàng tộc mang huyết hệ Raging Fire có một trait ẩn:

```text
bearer phù hợp
+ điều kiện phù hợp
+ tâm hồn thuần khiết
+ chết trong lửa
→ tái sinh thành bán thần
→ có thể đạt cấp super-weapon
```

Exact trigger, cách kiểm soát, xác suất, ritual và quan hệ kỹ thuật giữa trait thật này với ritual Canon 1 giữ `UNKNOWN` nếu user chưa khóa riêng.

### 25A.4 X2 CURRENT CANON — AetherFire biết lineage “có gì đó khác”, nhưng state knowledge bị phân mảnh

AetherFire biết Raging Fire có một tính chất vượt ngoài phần seal/barrier mà họ đã nhận biết. Họ muốn nghiên cứu sâu hơn nhưng chi phí rất lớn, nên **MC2 trở thành trường hợp mà nhà nước cố tình dùng để nghiên cứu/khai thác**.

Information architecture:

```text
Cult tận thế
→ cung cấp information cho state

Counterintelligence
→ có lý do nghi ngờ information/provenance

Security
→ được Raging Fire tiếp cận trước
→ cố tình lấp liếm / làm mờ information

field agents
→ truyền lại picture không rõ ràng

Army
→ ủng hộ True Crown
→ cố tình thả một số mật vụ RF đi vào
→ đồng thời gây khó/chống Bộ Nội vụ
```

Do đó các statement cũ có vẻ contradict nhau có thể phản ánh **different institutional knowledge states**, không phải omniscient canon tự mâu thuẫn.

```text
STATE KNOWLEDGE
≠ TRUE ONTOLOGY

Security picture
≠ Counterintelligence picture
≠ Interior picture
≠ Army picture
```

### 25A.5 X3/X4 CURRENT CANON — MC2.2 là hidden half-brother, không chỉ “hôn phu”

Prince 9 cũng là cha của **MC2.2**, hôn phu MC2 trong Canon 1. Hai người là **anh em cùng cha khác mẹ về huyết thống**, nhưng genealogy bị che giấu có chủ ý bên trong RF; exact responsible actor giữ `UNKNOWN`.

Mẹ MC2.2 là **Hoàng hậu của vị vua đã giết Prince 9**.

```text
Prince 9
├─ với mẹ MC2   → MC2
└─ với mẹ MC2.2 → MC2.2
```

MC2 và MC2.2 không biết sự thật trong phần lớn trajectory liên quan trước revelation.

Trong Canon 1, revelation này gắn với trajectory nơi MC2.2 lật vua của quốc gia thành viên nơi Prince 9 xuất thân/đăng cơ tại quốc gia đó; sau khi biết MC2 là em gái cùng cha khác mẹ và đã chết, anh ta tiếp tục lật luôn AetherFire. Không được flatten thành một romance-revenge đơn giản: dynastic purge, hidden kinship, succession và state power đều nằm trong causal chain.

### 25A.6 X5 OPEN DESIGN PROBLEM — collision MC2/MC2.2 trong current trajectory

**NOT CANON / OPEN DESIGN PROBLEM**

User đã chỉ ra collision risk: nếu current MC2 đang là Undie trong khi MC2.2 tiến gần một RF succession event, reveal quá sớm có thể làm hai narrative hút vào nhau và tái tạo failure mode cũ.

Chưa có resolution được user chốt. Một analysis candidate từng được nêu là tách bằng ba loại constraint:

```text
information access
+ political authority/cost
+ operational reach
```

và để MC2.1 giữ local HOPE pathway trong khi MC2.2 chạy geopolitical/dynastic pathway. Đây chỉ là **PROPOSAL/analysis**, không được đưa sang canon nếu user chưa nhận.

---

## 25B. Y — Mage Council Đông Bắc, human experimentation và political-security pressure

### 25B.1 CURRENT CANON — hai chi nhánh Hội đồng Pháp sư

Hội đồng Pháp sư có hai chi nhánh lớn đã được xác nhận:

```text
Mage Council
├─ chi nhánh bên trong AetherFire
└─ chi nhánh chếch Đông Bắc
   → phía sau một núi lửa
   → có Học viện Phép thuật
   → bên dưới có nghiên cứu trên cơ thể người
```

Nguồn đối tượng nghiên cứu cơ thể người là người từ ba cường quốc phía Bắc:

- Elf;
- Thú Nhân;
- Long tộc.

Đây là một **grievance/casus-belli nền** giải thích vì sao ba cường quốc không “tự nhiên” muốn ăn thua đủ với AetherFire.

### 25B.2 Y1 CURRENT CANON — cult không thuộc Học viện

Correction quan trọng:

```text
Cult BELONGS_TO Academy = FALSE
```

Cult tận thế **giả dạng POW**, và Hội đồng Pháp sư sử dụng các POW apparent đó làm **specialist**.

```text
Cult member
→ fake POW identity
→ Mage Council specialist interface
```

Do đó cult khai thác một interface hợp pháp/hữu ích của Council thay vì cần tồn tại như một department chính thức của Học viện. Exact mức Hội đồng biết provenance thật và exact scope infiltration giữ `UNKNOWN` nếu chưa chốt.

### 25B.3 CURRENT CANON / TEMPORAL PLACEMENT UNKNOWN — Y có trước khi Canon 1/Canon 2 được tách theo overlap model

Concept Y được tạo khi Canon 1 và Canon 2 vẫn được người thiết kế nghĩ như **một trục**, trước mô hình authored-vs-lived overlap hiện tại.

User đã xác nhận **nội dung Y là canon**, nhưng chưa quyết định gắn từng event/site-state của Y vào chronology overlap như thế nào.

Do đó:

```text
Y CONTENT = CANON
EXACT PLACEMENT RELATIVE TO DIVERGENCE = UNKNOWN
```

Không tự ép toàn bộ Y vào riêng Canon 1 hoặc riêng Canon 2.

## 25C. Z / AA — Quad Night, strategic geography và Học viện như forward node

### 25C.1 PARTIALLY SUPERSEDED 2026-09-11 — AetherFire age survives; old east geometry retired

AetherFire không phải một đế quốc cổ tồn tại tự nhiên từ vô thủy. Nó mới được lập khoảng **200 năm**, ban đầu từ một **hiệp ước phong ấn thủy tổ của ba cường quốc phía Bắc**, cấu trúc bằng liên minh chính trị và kết hôn.

Current geography/dependency:

```text
North
→ 3 great powers
→ RF-blood firewall
→ crystal-pillar maintenance network dưới AF

South / across ocean
→ Raging Fire
→ AF phải trả chi phí + nhượng bộ chính trị/thương mại
→ maritime route bị Seaborne đe dọa
→ exchange phụ thuộc mạnh vào air route

West
→ Hoa Nguyệt
→ bilateral Silk Road / trade treaty
→ political tension CAN_RUN_WITH economic trade

East/right
→ old 100 km / Quad Night geometry is orphaned
→ exact current map between AF, ML and TE = UNKNOWN
```

Seaborne là sinh vật tương tự kraken và rất khó giết. Exact ecology/number/territorial behavior giữ `UNKNOWN` ngoài phần đã nêu.

### 25C.2 SUPERSEDED 2026-09-11 — 100 km corridor và các buffer micro-polity

Hành lang AF↔Quad Night không phải vùng hoang tuyệt đối. Nhánh chính có nhà nghỉ/dịch vụ, trong khi khu vực xung quanh thường xuyên có cướp.

Bên trong hành lang có các cộng đồng/bộ tộc nhỏ tự phong chủ quyền, trước đây từng được nói như các “quốc gia nhỏ” ghét kiểu đạo đức giả/terror-welfare của Quad Night/Holy State và nghiêng về AF. Latest externalization làm rõ chúng hoạt động như **thuộc địa/buffer dưới quyền AF**, phục vụ:

- giao thương;
- road security;
- buffer geopolitics.

Một polity ở đoạn gần Quad Night chiếm khoảng 50 km còn lại. Exact subdivision của toàn 100 km chưa chốt và không tự điền.

### 25C.3 SUPERSEDED 2026-09-11 — Quad Night alliance ontology

`Quad Night` là tên chính thức của liên minh gồm bốn quốc gia. “Thánh quốc” khi chỉ toàn khối phải hiểu là **Quad Night**, không phải Holy State đơn lẻ.

1. **Holy State:** republic; Holy Temple đại diện quốc gia; coercive one-religion social order với public humiliation/pressure lên người không theo.
2. **Matriarchal member state:** phản đối Undie của AF nhưng anti-male discrimination rất cao; reproductive model gần Amazon myth.
3. **T.Gear:** tourism/entertainment/business/shopping-heavy state, outsource phần lớn heavy labor cho robot/android; cạnh tranh AF về luxury/entertainment.
4. **Trinity Hexagon:** small artifact-reserve state; thần khí/magical objects bound mạnh với địa lý và nhiều khi với bloodline; flag = triangle inside hexagon.

Quad Night được lập ra **chủ yếu để bảo vệ Trinity Hexagon**.

### 25C.4 SUPERSEDED 2026-09-11 — Queen custody under Quad Night

Mẹ MC2/Queen bị **Quad Night** tạm giữ, không cố định ở Holy State. Khi cần, bà được luân phiên chuyển địa điểm để chống espionage và rescue/extraction.

Holy State và matriarchal member state hiểu bà là strategic asset. T.Gear không quan tâm nhiều, nhưng chính openness của một state thiên về tourism/business làm nó là nơi rất tệ để giữ yếu nhân. Trinity Hexagon còn nguy hiểm hơn vì nhiều artifact phản ứng với bloodline và Queen mang Raging Fire royal blood.

Canonical constraint:

```text
Queen is easy enough to kill
BUT
Quad Night must not kill her
```

Lý do là strategic value + lineage uncertainty; đây là institutional constraint, không phải invulnerability. Exact artifact reaction nếu Queen bước vào Trinity Hexagon giữ `UNKNOWN`.

### 25C.5 PARTIALLY SUPERSEDED 2026-09-11 — legacy treaty route and surviving covert pattern

T.Gear là quốc gia đã/đang mua bán/chuyển nhượng Undie với AF. Treaty song phương gồm cả:

```text
institutional model transfer
+
actual cross-border Undie reassignment/transfer
```

Trade phải transit qua Holy State. Holy State thù địch AF; T.Gear vì economic interest gây sức ép, đe dọa đóng border và chặn một phần rear access/cửa sau tới Trinity Hexagon.

Holy State còn thường xuyên đi vào T.Gear, giả dạng/đón đầu thương vụ rồi giải phóng Undie tại chỗ, không mang về nước, sau đó frame AF hoặc Hoa Nguyệt. Vì vậy trong genealogy cũ/current politics:

```text
anti-Undie moral rhetoric
CAN_RUN_WITH
covert sabotage + false attribution
```

Undie ở đây là một **trade/diplomatic interface**, không phải causal center của geopolitics.

### 25C.6 DESIGN HISTORY / CANON GENEALOGY — Học viện được đặt để chọc flank Quad Night

Học viện Đông Bắc trong concept/canon gốc được đặt **ngay sau sườn Quad Night** để tạo một forward pressure node; nếu “chọc” thì phía T.Gear là hướng phù hợp nhất vì độ mở xã hội–kinh tế cao.

Bộ Ngoại giao AF cố che đậy site. Quad Night hoặc không biết nó tồn tại, hoặc biết quá ít để hiểu thật sự nó là gì. Exact current awareness chưa chốt.

Điểm này quan trọng vì Học viện không sinh ra do Undie. Core của nó là:

```text
magic academy
+ specialist production
+ body research
+ forward geopolitical placement
+ state concealment
```

Legacy Undie sink của failed students chỉ là local disposal interface.

### 25C.7 DESIGN HISTORY / CANON GENEALOGY — Z3 sabotage products và deliberate signature

Legacy academy students tạo các thí nghiệm từ cư dân Elf/Thú Nhân/Long tộc rồi **thả trở lại bên trong ba quốc gia để phá hoại**. Experimental products mang một **signature** có chủ ý để đối phương biết nguồn.

Vì vậy grievance phía Bắc không chỉ là “AF bắt người nghiên cứu”:

```text
people taken
→ experimented on
→ converted into sabotage products
→ released back into their own states
→ signature makes attribution deliberate
→ national/security grievance compounds
```

Đây là một lý do trực tiếp khiến tam cường muốn “ăn thua đủ” với AF.

### 25C.8 DESIGN HISTORY / SITE PROPERTY — Z4 teleport gate là intentional security hole

Bên trong Học viện có teleport gate trực tiếp về AF; destination là **một quận cô lập trong thủ đô** chứa các lực lượng tinh nhuệ nhất.

Strength và vulnerability là cùng một interface:

```text
AF use:
forward node ↔ capital logistics

failure mode:
academy compromised
→ gate bypasses territorial defense depth
→ attackers reach capital directly
```

Nếu Elf + Thú Nhân + Long tộc tạm gác thù riêng và đạt operational consensus, họ có thể thả cảm tử qua gate. Việc destination có elite forces là mitigation, không xóa vulnerability vì survival của suicide force không phải objective.

Exact gate authorization/activation/control rules và exact post-divergence status giữ `UNKNOWN`.

### 25C.9 CURRENT CANON — cult infiltration predates MC3

Cult trà trộn vào POW-specialist system từ rất sớm và **đã vào bên trong AF trước khi MC3 bị kéo vào Fiction 1**.

```text
cult penetration
→ shared pre-divergence state
≠ HOPE-created event
```

Điểm này phải giữ khi tách Canon 1 / Canon 2: Clash #1 không tạo ra infiltration; nó chỉ diễn ra trên một world đã có lỗ hổng đó.

### 25C.10 DESIGN ANALYSIS — vì sao externalization chính trị đến muộn hơn Undie

User xác nhận paracosm phần lớn được giữ **thuần trong đầu**, index theo institution/process chứ không phải một cross-cutting encyclopedia. Vì vậy việc tập trung nhiều tháng vào Undie không chứng minh Undie quan trọng hơn các trục chính trị. Undie dễ externalize hơn vì nó là một subsystem có boundary rõ và từng là RP foreground; ngược lại geopolitics hiện lộ ra bao gồm đồng thời:

```text
founding pact
+ RF dependency
+ northern great powers
+ Quad Night alliance cohesion
+ Trinity Hexagon artifact security
+ T.Gear commerce
+ Holy State covert action
+ buffer colonies
+ Mage Council academy
+ cult penetration
+ teleport-gate vulnerability
```

Đây là **lý do workload nhận thức cao**, không phải bằng chứng project thiếu architecture. Khi externalize, phải giữ institution-first graph và không kéo mọi node quay về Undie chỉ vì Undie có nhiều source chi tiết.

## 26. Những cơ chế cũ đã sống sót gần như nguyên vẹn

- MC2 → illegal prostitution → higher risk → resistance contact → fake resistance trap → despair/dead-heart.
- Library/nested-fiction training của MC1.
- V0.5/V1.0/5-year divergence, nhưng representation đổi từ dual-live-timeline sang same-source / authored-vs-lived continuation + later overlap.
- Perception manipulation của MC3.
- Controlled loophole của black market.
- Fake collar/fake Undie exploit.
- Yellow genealogy từ impersonation.
- Performance pressure.
- Separation credit money / score-like progression variable.
- Permissioned geography/barrier concept ở cấp nguyên lý.
- Foreign-source population và death-benefit genealogy.

---

## 27. Những cơ chế đã bị bỏ vì khóa pathway quá mạnh

- MC1 là song sinh MC2.
- MC3 entry qua Undie.
- False containment “POW thuộc Undie”; old shared Slave umbrella đã được tách.
- POW dùng shared Undi + forced transition/sterilization như humiliation implementation.
- MC1 bắt buộc sống như Undie để dùng thư viện.
- Hai persistent live timelines chạy song song.
- Undie là gateway của gần như mọi subsystem.
- Stimulant như performance shortcut.
- Full legacy debt-bondage/shop-body-upgrade regime chưa được phục hồi; chỉ bounded internal Credit Line + current default caps đã được canon mới xác nhận.
- O death disposal cực đoan không phải current default.

---

## 28. Register — Các điểm đang cân nhắc / có thể revisit

> Mỗi mục giữ **status riêng**. Chỉ những mục ghi rõ `UNDER CONSIDERATION` mới được hiểu là user đang cân nhắc mang lại; `DESIGN HISTORY` không tự trở thành proposal/current canon.

### 28.1 Human patrol

Nguồn: G.

Có thể mang lại patrol con người để xử lý:

- ambiguity;
- fake status/fake collar/fake Undi;
- kiểm tra trực tiếp;
- các case automation chưa đủ;
- corruption/bribery possibility nếu sau này chốt.

**UNKNOWN:** exact authority và relation với automated enforcement.

### 28.2 Barrier với original mobility use case

Nguồn: I.

Có thể phục hồi logic:

```text
mobile Undie
→ cần permission code
→ barrier kiểm access
```

nhưng không nhất thiết barrier tồn tại **chỉ vì Undie**.

**UNKNOWN:** current scope.

### 28.3 Hệ gái gọi riêng

Nguồn: M.

Có thể phục hồi concept:

```text
dispatch
+ private destination
+ transport
+ payment
+ access
+ safety boundary
```

Chưa chốt ontology.

### 28.4 Geography rộng hơn cho Undie mobility/enforcement

Nguồn: G/I.

Có cân nhắc rời lỗi cũ:

```text
Undie
→ chỉ có red-light district
```

và cho phép activity/access rộng hơn theo permission.

**UNKNOWN:** rank nào, zone nào, exception nào.


### 28.5 Thánh điện / Thánh quốc

Nguồn: R + R2 + R3.

**UNDER CONSIDERATION** — user đang cân nhắc mang lại một module tôn giáo–địa chính trị gồm:

- Thánh điện nội địa;
- Thánh nữ / clergy / giáo dân;
- Holy Guard;
- Creed;
- public peaceful opposition;
- Holy State external anchor;
- trade / pilgrimage / migration leverage;
- Holy State covert infiltration / propaganda network;
- T counterintelligence response và sovereignty signaling;
- purist diplomacy / “terror welfare” đối với các nước sát AetherFire;
- bilateral Undie treaty như diplomatic opening;
- neighboring-state alignment / vassalage pressure.

Giá trị chính:

```text
moral legitimacy
+ public opposition
+ magical/social utility
+ border geopolitics
+ migration gatekeeping pressure
+ lawful-dissent vs foreign-interference boundary
+ public counterintelligence signaling
+ treaty diplomacy / transactional legitimacy
+ regional patronage competition
```

**SUPERSEDED / REMOVED — 2026-09-16:** foreign spy / infiltrator không còn punitive Undie route riêng. Archived implementation là provenance-only; không được dùng làm fallback cho xử lý gián điệp.

**UNKNOWN:** exact jurisdiction, Creed capabilities, intelligence interface, migration leverage, mức complicity của Thánh điện/Thánh nữ và current sanction nếu R2 được tái nhập.

### 28.6 Hội đồng Pháp sư

Nguồn: S + V + Y/Y1.

**PARTIAL CURRENT CANON + PARTIAL UNDER CONSIDERATION.**

Đã phục hồi/chốt:

```text
Mage Council exists
+ coercive magic-tech implementation role
+ internal AF branch
+ northeastern branch behind volcano
+ magic academy
+ body-research facility
+ northern-subject grievance
+ cult fake-POW specialist exploit
```

Chưa tự phục hồi toàn bộ legacy S:

```text
full contingency doctrine scope
+ exact artifact/grimoire custody
+ exact current POW specialist governance
+ political neutrality limits
+ full jurisdiction / mandate
```

Do đó register này không còn được đọc là “Mage Council chưa canon”; chỉ **các legacy capability chưa chốt** mới còn ở trạng thái cân nhắc/UNKNOWN.

### 28.7 Cụm Nội vụ–An ninh–Phản gián

Nguồn: T.

**UNDER CONSIDERATION** — user đang cân nhắc mang lại **function/capability** của legacy security complex, nhưng old organizational unity hiện là một failure mode lớn.

Các legacy capability đáng cân nhắc:

```text
intelligence / double agents / spec ops
+ mercenary + guild-elite contracts
+ clone homunculus / lab-enhanced personnel
+ automated surveillance
+ Mage Council magical countermeasure support
+ satellite / colony security coverage
+ Civil infrastructure labor
+ counter-infiltration
+ counter-extraction
```

Current design direction ưu tiên **phân rã** chúng qua Nội vụ / An ninh / Phản gián và các interface liên quan để tạo asymmetry, mandate conflict và headroom thay vì phục hồi một competence singularity nguyên khối.

**UNKNOWN:** exact current jurisdiction, chain of command, legal oversight, phân bổ capability giữa ba bộ, và phần nào của covert toolkit sẽ được phục hồi.

### 28.8 Hướng multi-narrative / phân rã faction

Nguồn: U + current design direction.

**CURRENT DESIGN DIRECTION** — không phải một faction cụ thể mà là nguyên tắc áp cho các legacy faction có khả năng được mang lại.

```text
ít nhất 3 narrative line
+ legacy faction decomposition
+ conditional interdependence
+ opposition / competition
+ information asymmetry
+ authority / mandate separation
→ causal headroom
```

Không mặc định mọi legacy faction đều sẽ trở lại. Chỉ các module được user chọn mới được tái nhập; khi tái nhập ưu tiên **giữ function/capability đáng giá nhưng tránh phục hồi monolith/competence concentration cũ**.

Framing mới:

```text
Arc 1
→ vẫn có adult theme có giới hạn

phần còn lại
→ political / institutional / geopolitical focus
```

**UNKNOWN:** ba narrative line cụ thể là gì, faction nào được phân bổ cho từng line, điểm giao giữa các line, và exact adult-theme boundary trong Arc 1.

---

## 29. Những thứ KHÔNG được tự coi là “đang cân nhắc mang lại”

Trừ khi có chốt mới, các legacy sau chỉ là **DESIGN HISTORY**, không phải proposal hiện tại:

- forced status MC1/MC3 trong Undie;
- master-control của Canon 1;
- shared Undi/dual-color POW implementation;
- forced transition/sterilization của POW;
- stimulant;
- anti-mind-break magic và các magic patch cũ;
- O death disposal;
- full legacy state/black-credit package; bounded internal Credit Line hiện đã current;
- body-upgrade shop đầy đủ;
- exact legacy debt assignment/master service; không đồng nhất với current private-facility default có giới hạn;
- exact multiplier ×1.5 / ×2;
- exact legacy travel economics;
- exact legacy dedicated-transport implementation.

---

## 30. Cây genealogy nén

```text
EARLY SYSTEMIC ADULT / SHARED SLAVE CORE
│
├─ Shared Slave umbrella
│  ├─ Undie branch
│  │  ├─ performance
│  │  ├─ transport
│  │  ├─ barrier
│  │  ├─ pricing / tips / consumables
│  │  ├─ credit / black market / debt
│  │  ├─ humiliation / resistance
│  │  └─ death handling
│  │
│  └─ POW branch
│     ├─ elite specialist function
│     ├─ shared Undi family + dual-color code [retired]
│     ├─ forced transition/body humiliation [retired]
│     ├─ double-tension with Undie resistance [legacy function]
│     └─ Mage Council specialist pipeline [design history]
│
├─ MC1
│  ├─ twin-MC2 branch [retired]
│  ├─ status-bound Undie branch [retired]
│  └─ library → nested fiction [survives]
│
├─ MC2 fall
│  ├─ fiancé/nobles identity intervention + anti-truth magic [retired P]
│  ├─ illegal prostitution → higher risk → fake resistance trap [survives L]
│  └─ current institutional fraudulent status route
│
├─ MC3 / Meta
│  ├─ Undie-entry branch [retired]
│  ├─ editor/proofreader role
│  ├─ perception ability [survives]
│  ├─ Simulation Park concept
│  │   → current POC
│  └─ timeline architecture
│      ├─ dual persistent live timelines [retired]
│      └─ same V0.5
│          ├─ WRITE → V1.0 → Fictionize stress-test / Canon 1
│          └─ LIVE + HOPE → 5y Canon 2
│              → later pathway overlap / clash #2
│
├─ Magic legacy [Q]
│  ├─ anti-mind-break Undie spell [retired/not current]
│  ├─ anti-truth / identity glue [retired/not current]
│  └─ current full magic system [deferred]
│
├─ Religion [R / R2]
│  ├─ Temple / Saintess / clergy / Holy Guard / Creed
│  ├─ public anti-Undie moral opposition
│  ├─ Holy State
│  │   → trade / pilgrimage / migration / intelligence leverage
│  └─ R2 covert conflict
│      ├─ Holy State spies → worshipper / Saintess-retinue cover
│      ├─ propaganda under peaceful religious cover
│      ├─ T detection → public sovereignty attribution
│      └─ forced Undie sanction [legacy implementation; current-incompatible unless reconfirmed]
│      [UNDER CONSIDERATION]
│
├─ Mage Council [S]
│  ├─ political neutrality by default
│  ├─ magic-tech infrastructure
│  ├─ artifact / divine artifact / grimoire custody
│  ├─ seal / preserve / contingency doctrine
│  ├─ counter-force to Temple purity doctrine
│  └─ POW specialist knowledge-import engine
│      [UNDER CONSIDERATION]
│
├─ Internal Security Complex [T]
│  ├─ Interior / Security / Counterintelligence once unified
│  ├─ agents / double agents / spec ops / mercenaries
│  ├─ clone homunculus / lab-enhanced personnel
│  ├─ automated surveillance center
│  ├─ Mage Council magical countermeasure interface
│  ├─ counter-infiltration + counter-extraction
│  ├─ guild elites / regular military / noble commanders
│  ├─ satellite-colony mercenary coverage
│  ├─ Civil infrastructure support
│  └─ competence singularity [failure]
│      → current split: Interior / Security / Counterintelligence
│      [FUNCTIONS UNDER CONSIDERATION; OLD UNITY NOT AUTO-RESTORED]
│
├─ RP / Strategic-goon era [U]
│  ├─ MC2/Undie primary narrative axis
│  ├─ politics/geopolitics secondary axis
│  ├─ constitution / judiciary / procedure / federal prison
│  ├─ bilateral Undie treaty diplomacy
│  ├─ temporary magical contraception [old Undie]
│  ├─ MC2 dead-heart → trophy-wife / Raging Phoenix dynastic exploitation
│  ├─ True Crown / maternal Raging Phoenix seal / dragon-vein existential role
│  ├─ Army pro-war + oath to True Crown
│  ├─ geopolitical pressure cooker N/W/E/S
│  ├─ MC1/MC3 only proto-formed
│  └─ dead-heart → total war → statistical-fiction failure
│
├─ Hoa Nguyệt / Tây quốc [V]
│  ├─ official name: Hoa Nguyệt
│  ├─ China+Japan-inspired western civilization
│  ├─ human-rights orientation + wandering xia ecology
│  ├─ identity/aptitude/harmony magic philosophy
│  ├─ dark “Hoa” founding geometry + Lục Kì Nhân soul-anchor array
│  ├─ Undi as cultural/geopolitical degradation
│  └─ contrast: AetherFire coercive magic-tech integration
│
├─ Northern great powers [W]
│  ├─ unified Elf state / children of Tree God
│  ├─ unified Beastfolk great power
│  ├─ Dragon great power: Vrouvre + Dragon
│  ├─ repeated border war without simple breakthrough
│  ├─ progenitor non-human racial barrier
│  ├─ Raging Phoenix maternal/daughter-only continuity
│  ├─ MC2 as legitimacy + reproductive strategic bottleneck
│  ├─ Canon 1 dynastic export → foreign elimination → fiancé activation
│  └─ current MC2.1 = HOPE pathway planted by MC3
│

├─ Regional geopolitics / Quad Night / Academy [Z / AA]
│  ├─ AF founded ~200y from northern progenitor-seal political/marriage pact
│  ├─ RF-blood firewall + underground crystal pillar maintenance
│  ├─ AF↔RF ocean separation + Seaborne → air-route dependency
│  ├─ AF↔Hoa Nguyệt Silk Road despite political tension
│  ├─ AF↔Quad Night ~100km corridor + buffer colonies/micro-polities
│  ├─ Quad Night alliance
│  │  ├─ Holy State
│  │  ├─ matriarchal state
│  │  ├─ T.Gear
│  │  └─ Trinity Hexagon artifact reserve
│  ├─ Queen rotating strategic custody under Quad Night
│  ├─ AF↔T.Gear Undie transfer treaty + Holy State sabotage/false attribution
│  ├─ Northeast Academy as forward pressure node [legacy/current integration partly unresolved]
│  ├─ northern-body experimentation → sabotage releases + signature
│  ├─ teleport gate → isolated elite capital district / suicide-force failure mode
│  └─ cult infiltration through fake POW predates MC3
│
├─ Current redesign direction
│  ├─ at least 3 narrative axes
│  ├─ decompose legacy factions
│  ├─ interdependence + opposition
│  ├─ information / authority asymmetry
│  └─ adult theme bounded mainly to Arc 1; later arcs political
│
├─ Yellow
│  └─ fake-Undie enforcement genealogy [survives]
│
├─ Black market
│  └─ controlled experience loophole
│      → current systemic leak
│
└─ Death system
   ├─ O material-disposal model [retired]
   ├─ O2 family/remains/compensation alternate
   └─ current foreign-source death-benefit logic
```

## 31. Kết luận thiết kế

History hiện cho thấy AetherFire không đi theo mô hình:

```text
cheap smut
→ sau đó mới thêm serious worldbuilding
```

Mà gần hơn với:

```text
RP adult/Undie-heavy
+ state/legal/political core đã substantial
+ adult premise được nối lên cấp chiến lược
→ world pressure cooker rất rộng
→ nhưng narrative geometry vẫn hội tụ mạnh vào MC2
→ dead-heart checkpoint
→ total war / statistical fiction
→ refactor để trả causal leverage lại cho actor và institution
```

Điểm quan trọng nhất:

> **Current architecture không phủ nhận genealogy cũ; nó cố giữ các mechanism có causal value nhưng loại bỏ competence concentration, false containment và narrative funnel khiến world tự giải câu chuyện thay cho nhân vật.**

### 31.0 DESIGN ANALYSIS — institution-first memory và vì sao Undie từng bị overread

Latest externalization cho thấy một source-of-drift quan trọng: transcript từng làm Undie trông như hub vì user nói nhiều về nó và MC2 đi xuyên nó, trong khi internal paracosm memory thực tế được index theo institution/process.

Khi nhiều institution cùng dùng một shared terminal status, một LLM đọc theo keyword có thể đảo causal direction:

```text
A/B/C → Undie
```

thành:

```text
Undie → A/B/C
```

Đây là lỗi ontology. Future source/audit phải ưu tiên **originating institution** trước cross-cutting category.

### 31.1 DESIGN ANALYSIS — hai loại debt khác nhau

Lịch sử hiện cho thấy ít nhất hai loại architectural debt:

#### A. Success-induced coupling debt

```text
Undie/shared Slave implementation
→ giải quá nhiều requirement hiệu quả
→ interface centrality quá cao
→ false coupling
```

#### B. Narrative-convergence debt

```text
world/faction complexity ↑
→ momentum tích lũy
→ dead-heart threshold
→ total war basin
→ MC causal leverage ↓
```

Loại B mới là **core reason của cải cách narrative**. Complexity tự nó không cứu được một story nếu mọi pathway cuối cùng đổ vào cùng một statistical endgame.

### 31.2 DESIGN ANALYSIS — pattern sau P/Q/R/S/T/U/V/W

Các bổ sung mới làm rõ hơn quá trình phát triển:

```text
1. RP / STRATEGIC-ADULT CORE
MC2/Undie là foreground; politics/geopolitics là trục thứ hai.
State/legal/security/religion/trade core đã khá vững.

2. HIGH-EFFICIENCY SHARED IMPLEMENTATION
Undie/shared Slave interfaces giải rất nhiều requirement.
T security complex gom competence cực mạnh.

3. CONVERGENCE FAILURE
Sau dead-heart, faction momentum tự đẩy world vào total war.
Narrative chuyển sang statistical fiction.

4. DECOUPLING / DOMAIN RECOVERY
POW trả về specialist ontology.
MC entry trả về metafiction.
Magic tách khỏi patch role.
T phân rã thành nhiều institution.
R/S/T được xét lại theo function chứ không restore monolith.

5. CURRENT MULTI-NARRATIVE DIRECTION
Ít nhất ba narrative line.
Factions vừa phụ thuộc vừa đối kháng.
Knowledge/authority/capability không hội tụ một node.
Adult theme được giới hạn chủ yếu quanh Arc 1.
Các phần sau thiên về political / institutional / geopolitical fiction.
```

Một cách nén current refactor philosophy:

```text
PRESERVE CAPABILITY
≠ PRESERVE ORGANIZATIONAL CONCENTRATION

PRESERVE CONFLICT ENGINE
≠ PRESERVE OLD HUMILIATION / BODY IMPLEMENTATION

WORLD AUTONOMY
≠ CHARACTER IRRELEVANCE

ENDING EXISTS
≠ MIDDLE PRE-SOLVED
```

Đích của refactor không phải làm setting ít phức tạp hơn hay “ít goon” vì tự thân hai thứ đó không phải failure. Đích là tạo một world đủ tự trị để hoạt động, nhưng đủ phân tán về information, authority, motive và capability để **actor vẫn có thể thay đổi pathway** thay vì chỉ đứng nhìn các thống kê lực lượng hội tụ vào total war.
