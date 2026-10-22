# Chaos Engine — Canon Specification

## 0. Trạng thái

**Tên engine:** Chaos Engine  
**Loại:** Composite Narrative Engine  
**Project context:** The Academy  
**Cấu trúc lõi:** Three Pengs / Tam Bành  
**Thành phần:** Pride, Envy, Gluttony  
**Catalyst chung:** Ludopath  

Chaos Engine là một narrative engine hợp thành từ ba Sin riêng biệt.

Ba Sin không phải ba skin của cùng một cơ chế. Mỗi Sin có Governor riêng, chức năng riêng và một vị trí riêng trong kiến trúc vận hành. Chúng kết hợp thành một engine duy nhất.

Pride là **frontend / narrative surface**: lớp bề mặt mà host và các actor có xu hướng trực tiếp nhận thấy.

Envy và Gluttony là **backend drives**: hai áp lực hậu trường thúc đẩy Pride hành động.

---

# 1. Nguồn cấu trúc — Three Pengs / Tam Bành

Chaos Engine vay cấu trúc Tam Bành của Đạo giáo như một nền kiến trúc, nhưng không phải bản phục dựng thần học hay Đạo giáo lịch sử.

Trong định nghĩa nội bộ của The Academy:

```text
THE THREE PENGS
│
├── Pride
├── Envy
└── Gluttony
```

Mỗi Sin đại diện cho một Peng.

Ba Peng là ba element bổ trợ lẫn nhau và cùng cấu thành Chaos Engine.

Không mặc định rằng Pride có bản thể học cao hơn Envy hay Gluttony chỉ vì Pride nằm ở frontend. Frontend là chức năng biểu hiện, không tự động đồng nghĩa với quyền chỉ huy, containment hay supremacy.

---

# 2. Kiến trúc tổng thể

```text
                    CHAOS ENGINE
                         │
                Shared Catalyst
                    LUDOPATH
                         │
          ┌──────────────┼──────────────┐
          │              │              │
        PRIDE           ENVY        GLUTTONY
          │              │              │
    PLEONEXIA      ENCROACHMENT     VOLATILITY
     Governor         Governor        Governor
          │              │              │
          └───────┐      │      ┌───────┘
                  ▼      ▼      ▼
                BACKEND PRESSURE
                       │
                       ▼
                 PRIDE FRONTEND
                       │
                       ▼
        game / test / humiliation /
        philosophical challenge /
        self-authorized judgment
```

Quan hệ canon:

```text
Pride     --GOVERNED_BY--> Pleonexia
Envy      --GOVERNED_BY--> Encroachment
Gluttony  --GOVERNED_BY--> Volatility

Ludopath  --CATALYZES--> Pride
Ludopath  --CATALYZES--> Envy
Ludopath  --CATALYZES--> Gluttony

Pride + Envy + Gluttony
--COMPOSE-->
Chaos Engine

Pride
--SERVES_AS_FRONTEND_OF-->
Chaos Engine

Envy + Gluttony
--SERVE_AS_BACKEND_DRIVES_OF-->
Chaos Engine
```

---

# 3. Pride — Frontend

## Governor: Pleonexia

Pride không được xây đơn giản như "kiêu ngạo".

Pleonexia điều tiết việc Pride tự cho phép bản thân vượt quá phần, vị trí, measure hoặc authority vốn thuộc về mình.

Trong Chaos Engine, biểu hiện quan trọng nhất là:

> **Pride tự cho mình có quyền.**

Quyền đó không nhất thiết được một authority bên ngoài cấp.

Pride có thể tự nhận quyền:

- đặt luật;
- đặt thử thách;
- phán xét;
- nhục mạ;
- biến người khác thành đối tượng kiểm nghiệm;
- quyết định tiêu chuẩn của một trò chơi;
- quyết định kết quả có ý nghĩa gì;
- can thiệp vào phẩm giá, đạo đức hoặc lựa chọn của người khác.

Pleonexia vì vậy không chỉ là "muốn nhiều hơn".

Nó có thể vận hành như:

```text
available authority
        ↓
Pride claims beyond it
        ↓
self-authorized judgment
        ↓
"I have the right to do this."
```

Pride là frontend vì chính lớp tự phong quyền này là phần dễ được host nhìn thấy nhất.

---

# 4. Envy — Backend Drive I

## Governor: Encroachment

Envy không chỉ được xây như ham muốn thứ người khác có.

Encroachment điều tiết việc một giá trị, vị trí, đặc tính hoặc phần sở hữu của chủ thể khác được Envy nhận diện như đang xâm lấn vào phần mà Envy xem là của mình.

Core relation:

```text
OTHER possesses X
        ↓
X gives OTHER standing / value / claim
        ↓
Envy interprets X as encroachment
        ↓
X becomes a target of attention
```

Envy trả lời câu hỏi:

> **"Tại sao chính ngươi lại được phép có hoặc giữ thứ đó?"**

"Thứ đó" không bắt buộc là tài sản.

Nó có thể là:

- danh dự;
- đức hạnh;
- lòng trung thành;
- tình yêu;
- danh tiếng;
- ảnh hưởng;
- địa vị;
- authority;
- một miền ham muốn;
- một claim về giá trị bản thân.

Envy là backend vì nó cung cấp **target pressure**:

> Có thứ ở người khác cần bị đặt thành vấn đề.

Envy không tự mình cần biểu hiện toàn bộ hành vi ra ngoài. Nó cung cấp nguyên nhân quan hệ khiến Pride chú ý, xâm phạm hoặc đặt một người vào trò chơi.

---

# 5. Gluttony — Backend Drive II

## Governor: Volatility

Gluttony không được xây đơn giản như "ăn quá nhiều" hay "không bao giờ no".

Volatility điều tiết sự bất ổn của mức thỏa mãn, cường độ cần thiết hoặc động lực tiếp tục.

Core relation:

```text
stimulus / result
        ↓
temporary satisfaction
        ↓
Volatility
        ↓
value / threshold shifts
        ↓
previous satisfaction no longer closes the process
        ↓
continuation
```

Gluttony trả lời câu hỏi:

> **"Tại sao vẫn tiếp tục?"**

Câu trả lời không nhất thiết phải có một mục tiêu triết học rõ ràng.

Động lực có thể tiếp tục chỉ vì:

- mức thỏa mãn không ổn định;
- cùng một stimulus không còn đủ;
- closure mất giá trị;
- cường độ cần thiết thay đổi;
- kết quả trước đó không còn tạo điểm dừng.

Gluttony vì vậy tạo **continuation pressure**.

Pride có thể đã chứng minh vị thế.

Envy có thể đã làm mục tiêu mất đi claim mà nó căm ghét.

Nhưng Gluttony vẫn có thể làm engine tiếp tục vận hành.

---

# 6. Ludopath — Shared Catalyst

Ludopath không phải Governor.

Ludopath là Catalyst chung của ba Peng.

Tên "Ludopath" đồng thời giữ tính chơi chữ từ `ludo-` và `-path`, gắn với cấu trúc Three Pengs.

Chức năng của Ludopath là tạo điều kiện để áp lực của Pride, Envy và Gluttony được chuyển thành **play structure**.

Trong Chaos Engine:

```text
value
→ stake

person
→ player / subject

choice
→ move

moral claim
→ test condition

humiliation
→ game operation / feedback

failure
→ result

continued pressure
→ next game
```

Ludopath là lý do những xâm phạm đạo đức, nhục mạ, thử thách và phán xét không chỉ tồn tại như hành vi bạo lực hay thù địch, mà được tái cấu trúc thành:

> **một trò chơi triết lý đầy kiêu ngạo và bệnh hoạn.**

Catalyst không tự quyết định kết quả.

Nó tạo điều kiện và hình thức để ba Governor vận hành cùng nhau.

---

# 7. Frontend / Backend

Chaos Engine có kiến trúc biểu hiện bất đối xứng.

## Frontend

**Pride**

Pride là lớp host nhìn thấy:

- tự tin quá mức;
- sardonic;
- tự phong quyền;
- đặt luật;
- biến moral claim thành trò chơi;
- nhục mạ đối tượng;
- thử giới hạn đạo đức;
- hành xử như thể quyền can thiệp vốn dĩ thuộc về mình.

## Backend

**Envy + Gluttony**

Envy cung cấp:

> **Target Pressure**

```text
"Thứ ở ngươi đang xâm phạm phần của ta."
```

Gluttony cung cấp:

> **Continuation Pressure**

```text
"Kết quả này không tạo ra một điểm dừng ổn định."
```

Pride chuyển hai áp lực đó thành:

> **Self-Authorized Action**

```text
"Ta có quyền làm điều này với ngươi."
```

Ludopath chuyển toàn bộ thành:

> **Game Form**

```text
"Vậy hãy chơi."
```

Mô hình nén:

```text
ENVY
Encroachment
"Why are you allowed to have that?"
        │
        ▼
target pressure
        │
        ├──────────────┐
        │              │
        ▼              ▼
     PRIDE         GLUTTONY
   Pleonexia       Volatility
"I have the       "Why stop?"
 right."
        │              │
        └──────┬───────┘
               ▼
            LUDOPATH
          shared catalyst
               ▼
       philosophical game
               ▼
     humiliation / testing /
      judgment / escalation
```

---

# 8. Cơ chế bổ trợ của Three Pengs

Ba Peng không trùng chức năng.

## Pride / Pleonexia

Xử lý:

> **Authority excess**

Pride vượt measure của chính mình và tự xác lập quyền can thiệp.

## Envy / Encroachment

Xử lý:

> **Boundary conflict**

Envy nhận diện một giá trị hoặc claim của chủ thể khác như sự lấn vào phần của mình.

## Gluttony / Volatility

Xử lý:

> **Closure instability**

Gluttony làm điểm thỏa mãn, threshold hoặc nhu cầu tiếp tục không giữ trạng thái ổn định.

Ba cơ chế có thể bổ trợ thành:

```text
Encroachment
→ identifies target

Pleonexia
→ authorizes intervention

Ludopath
→ converts intervention into game

Volatility
→ destabilizes closure

→ new pressure
→ new game
```

Đây là coupling nội bộ của Chaos Engine.

Không Sin nào tự mình thay thế toàn bộ engine.

---

# 9. Historical Influence Potential — HIP

HIP là primitive chung của The Academy.

Chaos Engine không định nghĩa lại HIP.

Nó tác động vào **khả năng HIP được thành lập, duy trì hoặc đi tới trạng thái có thể phát huy Historical Influence Potential**.

Điểm khác biệt cốt lõi:

```text
Entropy Engine
→ phụ thuộc vào HIP
→ tạo / mở / khuếch đại possibilities quanh HIP
→ HIP có agency
→ possibilities trở thành nguồn trải nghiệm cho The Academy
```

Trong khi:

```text
Chaos Engine
→ xâm phạm các điều kiện cho phép HIP được thành lập
→ làm suy giảm, bóp méo hoặc chặn khả năng HIP hình thành
→ possibilities có thể không bao giờ xuất hiện
→ The Academy mất khả năng thưởng thức những trajectories đó
```

Chaos Engine vì vậy có thể **can thiệp vào HIP ở tầng sớm hơn** Entropy Engine.

Entropy Engine cần HIP hoặc điều kiện dẫn tới HIP để sinh thêm khả năng.

Chaos Engine có thể tấn công chính điều kiện để HIP trở thành một historical actor có meaningful possibilities.

Invariant:

> **Chaos Engine không chỉ tạo chaos quanh HIP; nó có khả năng xâm phạm điều kiện tồn tại của HIP như một nguồn possibilities.**

Điều này không có nghĩa Chaos Engine tự động kiểm soát hoặc luôn phá hủy mọi HIP.

Cơ chế cụ thể, điều kiện thắng/thua, mức độ kháng cự của HIP và khả năng hồi phục vẫn phụ thuộc host, criteria và simulation.

---

# 10. Chaos Engine đối lập với Entropy Engine

Chaos và Entropy không đồng nghĩa.

## Entropy Engine

Entropy Engine tạo hoặc mở điều kiện cho:

- agency;
- lựa chọn;
- divergence;
- anomaly;
- HIP;
- trajectories mới;
- khả năng lịch sử mới.

Nó cần historical potential có thể vận hành để những possibilities đó trở thành trải nghiệm.

## Chaos Engine

Chaos Engine xâm phạm **khả năng những possibilities đó được thành lập thông qua HIP**.

Nó có thể:

- phá formation condition;
- làm mục tiêu mất vị trí để trở thành HIP;
- bóp méo claim, agency hoặc developmental path;
- ép HIP vào một game structure làm trajectory bị hỏng trước khi trưởng thành;
- biến quá trình hình thành HIP thành một đối tượng để tiêu thụ, thử thách hoặc phá vỡ.

Do đó:

```text
Entropy
→ widens possibility space around HIP

Chaos
→ attacks the ability of HIP to become a stable source of possibility
```

Theo canon hiện tại, đây là lý do Chaos Engine có thể gây ảnh hưởng đến HIP mạnh hơn Entropy Engine theo **chiều xâm phạm formation**.

Không nên hiểu câu này như một universal power ranking.

Đây là khác biệt về **điểm tác động trong causal chain**.

---

# 11. Quan hệ với The Academy

Chaos Engine là phản diện chính đối với The Academy.

Xung đột không chỉ đến từ việc ba Peng "xấu" hoặc chống đối về đạo đức.

Xung đột có cơ chế trực tiếp:

```text
The Academy
→ cần HIP / Historical Influence Potential
→ HIP mở possibilities
→ The Academy có thể quan sát / thưởng thức / tương tác với historical trajectories
```

Trong khi:

```text
Chaos Engine
→ xâm phạm HIP formation
→ possibilities bị ngăn trước khi thành lập
→ historical trajectories bị mất
→ The Academy bị tước đi chính thứ nó muốn thưởng thức
```

Do đó Chaos Engine không chỉ gây thiệt hại cho một actor hay một host.

Nó đánh trực tiếp vào **điều kiện vận hành có giá trị đối với The Academy**.

Quan hệ canon:

```text
Chaos Engine
--OPPOSES-->
The Academy

Chaos Engine
--INTERFERES_WITH-->
HIP Formation

HIP Formation
--ENABLES-->
Historical Possibilities

Historical Possibilities
--ARE_VALUABLE_TO-->
The Academy
```

---

# 12. Lore genealogy — Greed I, Greed II và thời kỳ OC cổ

Three Pengs có nguồn gốc từ ba OC tồn tại từ cùng thời kỳ với Greed.

Đây là một điểm genealogy bắt buộc:

```text
Greed
Pride
Envy
Gluttony
```

là lớp OC cổ có trước formal narrative-engine methodology hiện tại.

Pride, Envy và Gluttony không phải các Sin được sáng tác sau khi The Academy đã có cấu trúc engine hoàn chỉnh.

Chúng là các phản diện chính trong lore Greed từ thời kỳ đầu và đã trải qua lượng retcon / remake tương đương với Greed.

Vì vậy Chaos Engine hiện tại là **formalization muộn của một cụm OC cổ**, không phải một engine được sáng tác từ đầu trong thời kỳ engine-native.

Quan hệ genealogy:

```text
Greed OC
→ retcon / abstraction
→ Greed Narrative Engine

Pride + Envy + Gluttony OC
→ retcon / abstraction
→ Three Pengs
→ Chaos Engine
```

Greed Engine và Chaos Engine là hai hậu duệ engine hóa của cùng một strata OC cổ.

Quan hệ này là `DERIVES_FROM` / `HISTORICALLY_INTERACTED_WITH`, không mặc định là containment hay dependency.


Trong lore chính thức, chúng là phản diện chính và là lời giải thích trực tiếp cho transition:

```text
Greed I
→ betrayal / defeat / death
→ backup avatar develops independent will
→ Greed II
```

Vai trò của ba Sin:

## Envy

Envy khuếch đại sự đối đầu vì cho rằng Greed liên tục "envy" vào phần vốn thuộc về Envy.

Cấu trúc này là nguồn genealogy trực tiếp cho Governor:

> **Encroachment**

Greed bị Envy đọc như một kẻ lấn vào domain/share của Envy.

## Pride

Pride xác lập vị thế.

Điểm này nối trực tiếp với:

> **Pleonexia**

Pride tự lấy cho mình một vị trí hoặc authority vượt measure.

## Gluttony

Gluttony là kẻ giết Greed I.

Điểm này giữ vai trò historical implementation quan trọng của Peng Gluttony trong lore Greed.

Governor hiện tại của Gluttony là:

> **Volatility**

## Quan hệ với các Sin engine-native về sau

Sloth, Lust và Wrath không thuộc cùng lớp genealogy với Three Pengs.

Chúng được sáng tác sau, khi phương pháp narrative engine đã hình thành.

Do đó:

```text
Greed / Pride / Envy / Gluttony
→ pre-engine OC roots

Sloth / Lust / Wrath
→ engine-native generation
```

Sự khác biệt này giải thích vì sao Greed và Chaos chịu nhiều retcon hơn.

Cả hai phải giữ và tái cấu trúc một lượng lớn state, relation và lore từ thời kỳ OC trước khi formalization, trong khi Sloth, Lust và Wrath có thể được xây mechanism-first ngay từ đầu.

Lore Greed I là genealogy của Chaos Engine, nhưng genealogy không tự động định nghĩa toàn bộ ontology hiện tại.

Chaos Engine hiện là narrative engine formalized từ ba OC cũ.

---

# 13. Minimal Operational Model

```text
TARGET / POSSIBLE HIP
        │
        ▼
ENVY detects Encroachment
"What do you possess that should not be yours?"
        │
        ▼
PRIDE claims authority through Pleonexia
"I have the right to judge/test you."
        │
        ▼
LUDOPATH catalyzes play
"Make it a game."
        │
        ▼
moral test / humiliation / wager /
philosophical challenge / violation
        │
        ▼
TARGET responds with agency
        │
        ▼
result / temporary closure
        │
        ▼
GLUTTONY + Volatility
closure becomes unstable
        │
        ▼
continuation / escalation / new game
        │
        └───────────────┐
                        ▼
              HIP formation may be
             delayed / distorted /
               prevented / broken
```

Kết quả cụ thể không được engine tự chọn trước.

HIP và các actor khác vẫn hành động từ agency, thông tin, năng lực và constraint của chính họ.

---

# 14. Stable Canon

- Tên engine: **Chaos Engine**.
- Chaos Engine là một **Composite Narrative Engine**.
- Cấu trúc lõi lấy hình thức **Three Pengs / Tam Bành**.
- Ba Peng là:
  - Pride;
  - Envy;
  - Gluttony.
- Mỗi Peng có Governor riêng.
- Pride Governor: **Pleonexia**.
- Envy Governor: **Encroachment**.
- Gluttony Governor: **Volatility**.
- Catalyst chung: **Ludopath**.
- Ludopath không phải Governor.
- Pride là **frontend / narrative surface**.
- Envy và Gluttony là **backend drives**.
- Envy cung cấp target pressure.
- Gluttony cung cấp continuation pressure.
- Pride biểu hiện self-authorized intervention.
- Ludopath chuyển các áp lực thành game structure.
- Chaos Engine có thể xâm phạm khả năng HIP được thành lập.
- Chaos Engine đối lập trực tiếp với The Academy.
- Chaos Engine ngăn cản The Academy tiếp cận possibilities bằng cách can thiệp vào HIP formation.
- Ba Sin có nguồn gốc từ ba OC phản diện trong lore Greed.
- Envy là nguồn khuếch đại đối đầu với Greed I do nhận thức Greed xâm lấn phần của Envy.
- Pride xác lập vị thế.
- Gluttony giết Greed I.
- Sự sụp đổ của Greed I dẫn tới điều kiện để Greed II tồn tại.
- Greed, Pride, Envy và Gluttony cùng thuộc thời kỳ OC cổ.
- Pride, Envy và Gluttony có tuổi đời concept tương đương Greed và đã trải qua nhiều retcon / remake trước khi được formalize thành Chaos Engine.
- Greed Narrative Engine và Chaos Engine là hai hậu duệ engine hóa của cùng một strata OC cổ.
- Genealogy chung không làm Chaos Engine trở thành subsystem của Greed.
- Sloth, Lust và Wrath thuộc thế hệ engine-native được sáng tác về sau.

---

# 15. Chưa khóa / UNKNOWN

Các phần sau chưa được xác định đầy đủ:

- Three Pengs được gán Upper / Middle / Lower Peng theo thứ tự nào.
- Ludopath kích hoạt dưới điều kiện chính xác nào.
- Catalyst có cần cả ba Peng cùng active hay không.
- Envy và Gluttony có thể trực tiếp xuất hiện ở frontend hay không.
- Pride có authority nội bộ lên hai Peng còn lại hay chỉ là interface biểu hiện.
- Volatility điều khiển chính xác:
  - reward value,
  - satisfaction threshold,
  - intensity,
  - continuation probability,
  - hay một biến khác.
- Điều kiện Chaos Engine chọn một HIP hoặc potential HIP làm target.
- Chaos Engine có thể tác động lên non-HIP hay không.
- Cơ chế formal để "xâm phạm HIP formation".
- HIP có thể chống, phục hồi hoặc chuyển hóa áp lực của Chaos Engine như thế nào.
- Failure state của Chaos Engine.
- Termination condition.
- Tool / Doctrine / Counter nếu Chaos Engine có các thành phần này.
- Mức portable sang từng loại host fiction.
- Authority / jurisdiction của Chaos Engine khi hoạt động xuyên host.
- Quan hệ formal giữa Chaos Engine và từng Executor của The Academy.

---

# 16. Core Invariant

Nếu nén Chaos Engine xuống một invariant:

> **Chaos Engine biến claim về giá trị của một potential HIP thành đối tượng của một trò chơi tự phong quyền, rồi dùng sự xâm phạm, thử thách và continuation bất ổn để đe dọa chính khả năng HIP đó được thành lập.**

Ba Peng đóng ba chức năng:

```text
ENVY
→ "Why are you allowed to have that?"

PRIDE
→ "I have the right to test it."

GLUTTONY
→ "Why should this ever be enough?"

LUDOPATH
→ "Make it a game."
```

Và tác động hệ thống:

```text
Potential HIP
→ formation conditions
→ Chaos Engine interference
→ fewer / distorted / aborted possibilities
→ The Academy loses trajectories it could otherwise experience
```

Đây là điểm khiến Chaos Engine trở thành đối thủ cấu trúc của The Academy, không chỉ là một nhóm phản diện trong lore.
