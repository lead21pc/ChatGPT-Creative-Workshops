# Wrath — RUNTIME

**Vai trò:** sở hữu cấu trúc vận hành riêng của engine; không phải universal pipeline.
**Trạng thái nguồn:** Working Draft / Hybrid Narrative Engine–Entity; portability chưa chốt. Tái cấu trúc tài liệu không nâng canon, Working, Placeholder hoặc UNKNOWN. Các mô tả signature là cách đọc phân tích bám nguồn, không là quyết định canon mới.

Đọc theo nhu cầu: [identity/signature](ENGINE_CORE.md), [ranh giới Host](HOST_CONTRACT.md), [vận hành](RUNTIME.md), [vùng mở](OPEN_STATE.md), [kiểm chứng bằng bản viết](WRITING_VALIDATION.md). Đây là vai trò tài liệu, không phải các bước thực thi engine.

## Đường đọc vận hành

- [Si và vòng truy vấn](#2-si), [quan hệ với Forsaken](#3-governor--forsaken).
- [Trước/sau Si](#4-trước-si-và-sau-si), [failure state](#5-wrath-như-failure-state), [Silence](#6-silence).
- [Condition vs Fact](#9-condition-vs-fact), [minimal model](#18-minimal-operational-model).

Các diễn giải về tính epistemic/conditional, paradox Silence và quan hệ primitive vẫn mang nhãn Working tại OPEN_STATE. Việc các đoạn nguồn trình bày chúng bằng câu khẳng định không nâng nhãn Working đó. Host-specific referent của Deus đọc ở HOST_CONTRACT.



# 1. Core Concept

Wrath không bắt đầu bằng cơn giận.

Core của Wrath nằm trong câu:

> **Si Deus me relinquit...**

Trong đó, phần quan trọng nhất là:

> **Si**

`Si` giữ toàn bộ mệnh đề ở trạng thái điều kiện.

Nó ngăn:

> **Deus me relinquit**

trở thành một kết luận chắc chắn.

Do đó, Wrath được giữ trong một quá trình truy vấn liên tục:

```text
Si...

↓

Tại sao?

↓

Quan sát

↓

Chiêm nghiệm

↓

Xem xét lại

↓

Tại sao?

↓

Tiếp tục truy vấn
```

Khi quá trình này còn hoạt động, Wrath chưa hoàn toàn trở thành **Wrath**.

---


# 2. Si

## Định nghĩa

**Si** là stabilizer của Wrath.

Nó không phải Governor.

Nó cũng không phải một virtue counter trực tiếp với Wrath.

Vai trò của nó là duy trì:

> **conditionality**

và từ đó duy trì khả năng:

> **questioning / reconsideration / inquiry**

---

## Chức năng

`Si` ngăn Wrath đóng một câu hỏi chưa có đáp án thành một sự thật tuyệt đối.

Nó giữ lại khoảng cách giữa:

```text
Có khả năng Deus đã forsake ta.
```

và:

```text
Deus đã forsake ta.
```

Khoảng cách đó chính là vùng hoạt động của stabilizer.

---

## Perpetual Motion

Wrath được giữ trong một perpetual motion của:

> **“Tại sao?”**

Không phải vì Wrath không đau.

Không phải vì Wrath không giận.

Mà vì chừng nào vẫn còn:

> **Si**

thì vẫn còn một khả năng khác.

Do đó:

```text
Pain
≠
Wrath
```

Thay vào đó:

```text
Pain

↓

Si

↓

Why?

↓

Reconsider

↓

Why?

↓

Reconsider
```

Wrath bị trì hoãn bởi chính quá trình chiêm nghiệm.

---


# 3. Governor — Forsaken

## Định nghĩa

Governor của Wrath là:

> **Forsaken**

Trong context này, `Forsaken` không chỉ có nghĩa thông thường là “bị bỏ rơi”.

Nó giữ sắc thái:

- bị ruồng bỏ;
- bị một thực thể có quan hệ nền tảng quay lưng;
- bị cắt khỏi một mối liên kết vốn có trọng lượng;
- bị bỏ lại trong im lặng mà không nhận được lời giải thích.

Forsaken mang cả trọng lượng:

- relational;
- existential;
- theological;
- ontological.

---

## Quan hệ với Si

Forsaken không hoạt động độc lập với Si trong Wrath.

Nếu bỏ `Si` khỏi hệ thống và chỉ còn:

> **Deus me relinquit.**

thì Forsaken trở thành một **state / fact**.

Nó không còn tạo ra engine dynamics.

Không còn:

- uncertainty;
- inquiry;
- reconsideration;
- stabilization;
- transition.

Do đó:

> **Si là điều kiện làm Forsaken có ý nghĩa như Governor của Wrath.**

---


# 4. Trước Si và Sau Si

Core concept có hai phía.

## Trước Si

Trước khi Wrath đi đến một kết luận, `Si` buộc nó phải hỏi:

> **Tại sao?**

Đây là phía chiêm nghiệm.

Nó giữ Wrath khỏi việc:

- quy kết ngay lập tức;
- biến đau khổ thành phán quyết;
- biến sự im lặng thành bằng chứng tuyệt đối;
- hành động như thể interpretation đã là truth.

Có thể biểu diễn:

```text
Stimulus / Pain / Silence

↓

Si

↓

Why?

↓

Inquiry

↓

Reconsideration

↓

Stabilized Wrath
```

---

## Sau Si

Mặt còn lại xuất hiện khi `Si` không còn giữ được mệnh đề ở trạng thái điều kiện.

Khi đó:

> **Si Deus me relinquit...**

không còn là:

> Nếu Deus bỏ rơi ta...

mà bị Wrath tiếp nhận như:

> **Deus đã bỏ rơi ta.**

Từ đây Forsaken không còn là possibility.

Nó trở thành certainty.

```text
Collapse of Si

↓

Forsaken accepted as truth

↓

Betrayal

↓

Anger

↓

Grief

↓

Wrath
```

Wrath ở đây bao gồm:

- tức giận;
- phẫn nộ;
- đau khổ;
- cảm giác bị phản bội;
- cảm giác bị Deus ruồng bỏ;
- phản ứng trước sự im lặng kéo dài của Deus.

---


# 5. Wrath như Failure State

Wrath không phải default state của entity.

Nó là một **failure state**.

Failure không có nghĩa là engine bị hỏng về mặt thiết kế.

Nó có nghĩa:

> quá trình giữ câu hỏi mở đã thất bại.

Pipeline:

```text
Pain

↓

Si

↓

Why?

↓

No answer

↓

Why?

↓

No answer

↓

Why?

↓

No answer

↓

Si collapses

↓

Forsaken becomes certainty

↓

Wrath
```

Vì vậy cơn thịnh nộ không phải primitive đầu tiên.

Nó là kết quả sau khi một tiến trình nhận thức không còn giữ được trạng thái mở.

---


# 6. Silence

## Vai trò

Sự im lặng của Deus là một thành phần quan trọng trong quá trình này.

Nếu Deus trả lời rõ:

```text
Ta không bỏ rơi ngươi.
```

Wrath có dữ liệu mới.

Nếu Deus trả lời:

```text
Ta bỏ rơi ngươi.
```

Wrath cũng có một đáp án.

Nhưng:

```text
Deus remains silent.
```

không giải quyết mệnh đề.

Nó giữ:

> **Si**

tiếp tục chạy.

---

## Paradox của Silence

Silence vừa giúp stabilizer tồn tại, vừa có thể làm nó suy kiệt.

```text
Silence

→ chưa xác nhận Forsaken

nhưng đồng thời

Silence

→ không cung cấp lý do để loại Forsaken
```

Do đó Wrath có thể tiếp tục:

> **Tại sao?**

trong thời gian rất dài.

Nếu quá trình này cuối cùng sụp đổ, chính sự im lặng có thể bị tái diễn giải thành bằng chứng của Forsaken.

---


# 8. Deus Me Relinquit

## Relinquit

`Relinquit` thuộc động từ Latin:

> **relinquere**

Trong câu:

> **Si Deus me relinquit**

`relinquit` là:

- present;
- active;
- indicative;
- third-person singular.

Nghĩa gần:

- leaves;
- abandons;
- forsakes.

Bản tiếng Anh giữ sắc thái phù hợp nhất:

> **If God forsakes me...**

---

## Forsake

`Forsake` được chọn vì nó không chỉ có nghĩa “rời đi”.

Nó gợi:

- ruồng bỏ;
- đoạn tuyệt;
- bỏ một mối quan hệ vốn đáng lẽ phải được duy trì;
- sắc thái tôn giáo và bi kịch.

Trong Wrath, sắc thái này cần thiết vì hành động của Deus không được Wrath hiểu như một sự vắng mặt bình thường.

Nó được cảm nhận như:

> **betrayal through abandonment.**

---


# 9. Condition vs Fact

Đây là một distinction bắt buộc.

## Conditional State

```text
Si Deus me relinquit...
```

Nghĩa:

> Nếu Deus forsake ta...

Chưa có kết luận.

Engine còn chạy.

---

## Concluded State

```text
Deus me relinquit.
```

hoặc về mặt nghĩa hoàn thành:

```text
Deus has forsaken me.
```

Nghĩa:

> Deus đã forsake ta.

Lúc này không còn điều kiện.

Không còn `Si`.

Không còn stabilizer.

---

## Hệ quả

Bỏ `Si` không đơn giản là bỏ một từ Latin.

Nó làm thay đổi loại mệnh đề:

```text
conditional proposition
→
asserted proposition
```

Đó chính là transition quan trọng nhất của Wrath.

---


# 18. Minimal Operational Model

```text
              DEUS
                │
                │ silence / action / non-response
                ▼
      Si Deus me relinquit...
                │
                ▼
               SI
          [Stabilizer]
                │
       keeps condition open
                │
                ▼
            Inquiry
          "Tại sao?"
                │
        ┌───────┴────────┐
        │                │
  Reconsideration     Collapse
        │                │
        │                ▼
        │            FORSAKEN
        │            [Governor]
        │                │
        └──── loop       ▼
                        WRATH
                   [Failure State]
```

---


## Giới hạn diễn giải và trạng thái

Các phần Silence và ý nghĩa relational/ontological ở trên giữ nguyên mô tả nguồn; các cách diễn giải được chính draft gắn Working vẫn thuộc [OPEN_STATE](OPEN_STATE.md). Việc chuyển phần không nâng độ chắc chắn. Trigger collapse, hồi phục của Si và end-state vẫn chưa chốt. Failure state trong fiction không tự chứng minh lỗi thiết kế của engine.
