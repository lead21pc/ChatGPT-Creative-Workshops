# Chaos — RUNTIME

**Vai trò:** sở hữu cấu trúc vận hành riêng của engine; không phải universal pipeline.
**Trạng thái nguồn:** nội dung canon theo specification v3 đã được xác nhận; các mục UNKNOWN vẫn mở. Tái cấu trúc tài liệu không nâng canon, Working, Placeholder hoặc UNKNOWN. Các mô tả signature là cách đọc phân tích bám nguồn, không là quyết định canon mới.

Đọc theo nhu cầu: [identity/signature](ENGINE_CORE.md), [ranh giới Host](HOST_CONTRACT.md), [vận hành](RUNTIME.md), [vùng mở](OPEN_STATE.md), [kiểm chứng bằng bản viết](WRITING_VALIDATION.md). Đây là vai trò tài liệu, không phải các bước thực thi engine.

## Đường đọc vận hành

- [Quan hệ composite](#2-kiến-trúc-tổng-thể).
- [Pride/Pleonexia](#3-pride--frontend), [Envy/Encroachment](#4-envy--backend-drive-i), [Gluttony/Volatility](#5-gluttony--backend-drive-ii).
- [Ludopath và giới hạn authority](#6-ludopath--shared-catalyst).
- [Frontend/backend](#7-frontend--backend), [coupling không có thứ tự bắt buộc](#8-cơ-chế-bổ-trợ-của-three-pengs).
- [HIP formation](#9-historical-influence-potential--hip), [điểm tác động so với Entropy](#10-chaos-engine-đối-lập-với-entropy-engine), [minimal model minh họa](#13-minimal-operational-model).



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

## 6.1. Core Function

Chức năng cốt lõi của Ludopath là:

> **biến một claim đang bị tranh chấp thành một cấu trúc có thể chơi được.**

Claim đó có thể liên quan tới:

- giá trị;
- đạo đức;
- phẩm giá;
- identity;
- vị trí;
- authority;
- danh dự;
- tình yêu;
- lòng trung thành;
- hoặc bất kỳ thuộc tính nào đang bị Envy / Encroachment đặt thành vấn đề.

Ludopath không tạo động cơ ban đầu.

Nó lấy pressure đã tồn tại trong Three Pengs và chuyển pressure đó thành:

```text
value / claim
→ stake

person
→ player / subject

choice
→ move

virtue / moral claim
→ test condition

self-image
→ wagered asset

humiliation
→ game feedback

success / failure
→ provisional result
```

Ludopath là lý do những xâm phạm đạo đức, nhục mạ, thử thách và phán xét không chỉ tồn tại như hành vi bạo lực hay thù địch, mà được tái cấu trúc thành:

> **một trò chơi triết lý đầy kiêu ngạo và bệnh hoạn.**

## 6.2. Boundary of Authority

Ludopath **không**:

- chọn target thay cho Envy;
- tạo ra Encroachment;
- trao authority cho Pride;
- tạo ra Pleonexia;
- tạo appetite hoặc continuation pressure cho Gluttony;
- quyết định outcome;
- ép HIP phải chọn một kết quả định sẵn.

Ludopath **có**:

- framing;
- gamification;
- assignment of stakes;
- exposure of choices;
- conversion of values into contestable conditions;
- conversion of intervention into playable form.

Vì vậy Catalyst không thay thế ba Governor.

Nó cung cấp **form of engagement** để ba Governor có thể cùng biểu hiện trong một operation.

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

Ba cơ chế có thể bổ trợ thành một configuration điển hình:

```text
Encroachment
→ marks something as contestable

Pleonexia
→ claims the right to contest it

Ludopath
→ makes the contest playable

Volatility
→ destabilizes closure
```

Đây là coupling nội bộ của Chaos Engine, nhưng **không phải một pipeline bắt buộc tuyệt đối**.

Không canon hóa các suy diễn sau:

```text
Envy must always activate first
→ Pride can only act after Envy
→ Ludopath must always occur after Pride
→ Gluttony makes termination impossible
```

Thay vào đó:

- Envy thường cung cấp **target pressure**;
- Pride thường cung cấp **self-authorized intervention**;
- Ludopath cung cấp **playable form**;
- Gluttony cung cấp **closure instability / continuation pressure**.

Các thành phần có thể phối hợp khác thứ tự tùy state, host và configuration.

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


## Cách đọc sơ đồ

Mục 8 giữ rõ coupling không phải thứ tự kích hoạt bắt buộc. Vì vậy mục 13 là minimal model minh họa đã có nguồn, không tạo prerequisite hoặc universal activation order. Các biến, activation, authority, failure và termination chưa chốt đọc tại [OPEN_STATE](OPEN_STATE.md). Không biến khả năng xâm phạm formation thành thắng mọi HIP hoặc universal power ranking.
