# The Academy V1.5 — Architecture

**Trạng thái:** bản tái cấu trúc vòng 1 từ baseline V1.5 hiện hành.  
**Vai trò:** mô tả kiến trúc V1.5 và các ranh giới đã được ghi nhận.  
**Không làm:** không thay đổi canon, không tự giải quyết vùng mở, không mô tả V2/V2.5 ngoài phần cần thiết để khóa boundary.

Đọc cùng:

- [The Academy Anti-Drift Kernel](../../12_ANTI_DRIFT/The_Academy_Anti_Drift_Kernel.md)
- [Historical Influence Potential](../../01_HIP/Historical_Influence_Potential.md)
- [V1.5 Architecture Handoff](The_Academy_V1_5_Architecture_Handoff.md)
- [Authorial Decisions 2026-09-28](../../The_Academy_Authorial_Decisions_2026-09-28.md)

Baseline nguồn vẫn được giữ nguyên trên branch này để đối chiếu:

- [The_Academy_V1_5_Architecture_Baseline_Anti_Drift.md](The_Academy_V1_5_Architecture_Baseline_Anti_Drift.md)

## 1. Định nghĩa vận hành

The Academy V1.5 là **miền nhân quả thể chế trước tốt nghiệp** của The Academy.

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

Boundary bắt buộc:

```text
RETURN TO ORIGIN
= V1.5 TERMINUS
```

Phần HIP tiếp tục sống, hành động, thay đổi lịch sử hoặc tương tác với Narrative Engine hậu tốt nghiệp không nằm trong active runtime của V1.5.

## 2. V1.5 không phải school-worldbuilding thông thường

The Academy từng là một concept có lore đầy đủ và hình thức academy là một phần thật của hệ thống.

Quá trình formalization về sau bóc bớt implementation cụ thể nhưng giữ causal architecture.

Vì vậy:

```text
INSTITUTION
≠ decorative school skin
```

Một institutional factor/faction có thể là một Narrative Engine nếu source xác nhận causal identity đó.

Internal department không tự kế thừa engine status.

## 3. HIP trong V1.5

HIP là common gateway nhưng không phải universal metric.

Tiêu chí đánh giá đến từ context hoặc framework cụ thể.

Không dùng HIP như:

- power level;
- morality score;
- protagonist score;
- chosen-one marker;
- Regressor definition;
- bảo đảm rằng target sẽ thay đổi lịch sử.

V1.5 có thể tuyển, đánh giá hoặc tạo điều kiện cho HIP theo cơ chế đã được source xác nhận, nhưng HIP vẫn giữ agency.

## 4. Engine sinh điều kiện, không xây protagonist bắt buộc

The Academy không cần tự tạo protagonist.

Một actor/HIP có thể đến từ Host Fiction, OC hoặc scenario đã có.

```text
Host Fiction / OC / Scenario
→ user selects HIP
→ HIP enters The Academy
→ institutional engines alter conditions / exposure / relations
→ HIP chooses / adapts / resists / acts
→ simulation produces trajectory
```

Engine thay đổi điều kiện; outcome không được chọn trước.

## 5. Cohort và routing

Legacy base ghi nhận cấu hình sampling cũ với tối đa 10 HIP/world, gồm các nhóm đã từng được mô tả như:

- 1 dân thường;
- 1 con thương nhân;
- 2 hoàng gia / quốc gia, với ghi chú legacy "tối đa 6 hoàng gia trong world";
- 2 thánh nữ / thánh tử.

Cấu hình này là base tái thiết kế, không phải định nghĩa HIP, không phải universal criteria và không tự trở thành constraint cuối cùng nếu nguồn mới không xác nhận.

Legacy base cũng ghi nhận 3 worlds/cohort, tạo mức tối đa 30 HIP/cohort trong cấu hình cũ.

Một world có thể được chọn qua nhiều recruitment cycle khác nhau.

```text
World X
├── recruitment cycle A → HIP set A
├── recruitment cycle B → HIP set B
└── ...
```

Điều này không tự xác nhận trigger, chu kỳ, số lần tối đa hoặc việc cùng một HIP được tuyển lặp lại.

```text
COHORT / CLASS
≠ FACTION
≠ DEPARTMENT
```

HIP không mặc định đi qua một curriculum tuyến tính chung.

Một trait không tạo deterministic routing.

```text
likes magic
≠ Magic faction mandatory

martial skill
≠ Martial faction mandatory
```

Lựa chọn faction phụ thuộc state, goals, interests, context và agency trong phạm vi source cho phép.

## 6. Recruitment, consent, pass và compensation

### Consent

HIP có quyền từ chối lời mời.

```text
Academy offer
→ ACCEPT / REFUSE
```

Recruitment không tự đồng nghĩa với cưỡng ép hoặc ownership.

### Pass

HIP có thể pass lượt cho người khác tối đa một lần/người theo baseline hiện có.

Recipient protocol vẫn mở và không được tự điền.

### Compensation

Nếu HIP còn người nhà và người nhà chấp nhận, có thể tồn tại bồi thường theo baseline hiện có.

Cơ chế bồi thường vẫn mở; không tự biến nó thành tuition, salary, purchase contract hoặc một hệ tiền tệ cố định.

## 7. Time-space baseline

Legacy base ghi nhận quan hệ thời gian:

```text
10 năm bên trong The Academy
=
1 năm ở world/reality gốc
```

Đây không tự định nghĩa thời lượng khóa học.

Tuổi sinh học của HIP không tăng theo thời gian ở The Academy theo baseline đã xác nhận.

Không tự suy ra từ đó rằng:

- memory không tích lũy;
- tuổi tâm lý không đổi;
- fatigue không tồn tại;
- một cơ chế sinh học/ma thuật cụ thể đang hoạt động.

## 8. Institutional engine ecology

V1.5 phải được đọc như một ecology các institutional components có causal function.

```text
THE ACADEMY V1.5
        │
        ├── Institutional Engine / Faction A
        ├── Teaching
        ├── Institutional Engine / Faction B
        └── infrastructure / interfaces / other components
```

Không mặc định mọi faction dùng cùng internal schema.

Một faction phải có causal identity đủ để sinh trajectory; tên domain tự nó không đủ.

### Teaching

Teaching được baseline ghi nhận là:

```text
Teaching
= Institution
+ Narrative Engine
```

Teacher có thể là Narrative Actor.

Student/HIP tương tác với Teaching nhưng không mặc định là protagonist của Teaching Engine.

Primitive, criteria, state model, authority detail, curriculum relation và failure/termination của Teaching vẫn chưa được khóa đầy đủ.

### Faction An ninh

Faction An ninh được xác nhận tồn tại trong V1.5.

Implementation cũ liên quan đến kiểm soát/cách ly một số host-native items hoặc capabilities chỉ là reconstruction lead và chưa phải current mechanism.

Không tự khôi phục implementation cũ thành canon hiện hành.

## 9. Cross-HIP interaction

HIP không chỉ tương tác với staff hoặc institution mà còn với HIP đến từ các thực tại khác theo baseline nguồn.

Peer difference có thể tự tạo causal pressure.

```text
Institutional Engine
        │
  ┌─────┼─────┐
  ▼     ▼     ▼
HIP A  HIP B  HIP C
  └── peer interaction ──┘
```

Không cần một engine prewrite toàn bộ conflict hoặc outcome.

## 10. Graduate boundary

Sau graduation, HIP được trả về original world/reality theo baseline đã xác nhận.

```text
Graduation
→ RETURN TO ORIGIN
→ V1.5 STOP
```

Không mặc định graduate phải:

- phục vụ The Academy;
- báo cáo;
- trung thành;
- nhận nhiệm vụ;
- duy trì liên lạc.

Nếu exception tồn tại, cần source riêng.

Việc đã có nhiều graduate tồn tại là existence-only information; không dùng nhóm chưa externalize này để suy demographic, success rate hoặc trajectory pattern.

## 11. Greed, Lust và overlap với V1.5

### Greed

Greed được ghi nhận có nhiều quan hệ chồng chéo, gồm Narrative Engine và Executor trong source liên quan.

Một relation không tự cấp các relation còn lại.

Greed có relation đảm bảo tài sản của HIP theo baseline, nhưng exact interface với Faction An ninh vẫn mở.

Greed có thể tiếp cận hoặc không tiếp cận một HIP hậu tốt nghiệp theo source hiện có; phần hậu tốt nghiệp đó không thuộc active runtime V1.5.

### Lust

Lust thuộc V1.5.

Exact institutional role, faction relation, interface và authority vẫn source-bound/đang mở.

Không dùng cấu trúc hiện tại của Lust Working Draft để ép các institutional engine khác vào cùng schema.

### Nhiều Narrative Engine cùng tiếp cận một HIP

Điều này được phép khi source xác nhận.

```text
multiple engines
→ same HIP
```

không tự suy ra:

```text
composite engine
dependency
same goal
same authority
```

Baseline còn ghi nhận một trường hợp external-project nơi Greed và Lust cùng tiếp cận một HIP. Trường hợp đó là `EXISTENCE-ONLY`: chỉ xác nhận rằng trường hợp đã tồn tại, không dùng làm reference data để suy cơ chế hoặc pattern chung.

## 12. Những component cũ đã từng được ghi nhận

Các component từng xuất hiện trong lore/baseline gồm:

- recruitment / enrollment;
- gateway / secondary space;
- student handbook;
- uniforms;
- teaching staff;
- curriculum;
- modern-world technology integration;
- entrance examination;
- class placement examination;
- graduation ceremony.

Sự tồn tại hoặc từng xuất hiện của một component không tự phân loại nó thành:

- Narrative Engine;
- department;
- governance node;
- infrastructure;
- cosmetic lore.

Cần causal function và source cụ thể để phân loại.

## 13. Những gì tài liệu này cố ý không chốt

Các vùng `UNKNOWN` / open của V1.5 được giữ riêng tại:

- [The_Academy_V1_5_Open_Registry.md](The_Academy_V1_5_Open_Registry.md)

```text
OPEN REGISTRY ≠ TODO LIST
UNKNOWN ≠ EMPTY
UNKNOWN ≠ PERMISSION TO INVENT
```

Architecture chỉ giữ ranh giới đã biết; registry giữ các điểm chưa externalize hoặc chưa xác nhận. Việc tách file không thay trạng thái của bất kỳ mục mở nào.

## 14. Sơ đồ chuẩn V1.5

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
                  ▼
             Academy Entry
                  │
                  ▼
        Cohort / Class Architecture
                  │
                  ▼
       Institutional Engine Ecology
                  │
       ┌──────────┼──────────┐
       ▼          ▼          ▼
   Faction A   Teaching   Faction N
                  │
             HIP traversal
                  │
                  ▼
              Graduation
                  │
                  ▼
          RETURN TO ORIGIN
          =================
             V1.5 ENDS
```

`Faction A/N` là placeholder trình bày, không phải tên faction canon.

## 15. Provenance

Bản này được tái cấu trúc từ:

- [The_Academy_V1_5_Architecture_Baseline_Anti_Drift.md](The_Academy_V1_5_Architecture_Baseline_Anti_Drift.md)
- [The_Academy_V1_5_Architecture_Handoff.md](The_Academy_V1_5_Architecture_Handoff.md)
- [Historical_Influence_Potential.md](../../01_HIP/Historical_Influence_Potential.md)
- [The_Academy_Authorial_Decisions_2026-09-28.md](../../The_Academy_Authorial_Decisions_2026-09-28.md)

Các nguồn engine-specific vẫn giữ thẩm quyền trong phạm vi engine của chúng.

Tài liệu này không supersede baseline cũ trong vòng tái cấu trúc đầu tiên; hai bản được giữ song song để đối chiếu trước migration tiếp.
