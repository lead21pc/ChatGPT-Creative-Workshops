# The Academy V2 — Architecture

**Trạng thái:** bản kiến trúc độc lập được tách từ các nguồn V2 hiện có trong repository.  
**Vai trò:** mô tả miền formalization/application của Narrative Engine mà không dùng V1.5 làm container và không biến V2 thành bản thay thế V1.5.  
**Không làm:** không xác lập capability engine-specific, không tự quyết định mode của engine chưa được xác nhận, không mô tả V2.5 như successor bắt buộc.

Đọc cùng:

- [Narrative Engine — Core Design Philosophy](../../00_META/Narrative%20Engine%20%E2%80%94%20Core%20Design%20Philosophy.md)
- [The Academy Anti-Drift Kernel](../../12_ANTI_DRIFT/The_Academy_Anti_Drift_Kernel.md)
- [The Academy Current Repository State](../../00_META/controls/The_Academy_Current_State.md)
- [Authorial Decisions 2026-09-28](../../The_Academy_Authorial_Decisions_2026-09-28.md)

## 1. Định nghĩa vận hành

V2 là miền nơi Narrative Engine được formalize/chọn và áp dụng vào một fiction cụ thể.

Luồng chuẩn:

```text
Meta Engine
    ↓
Narrative Engine selection / formalization
    ↓
Host Fiction
+ World Bible
+ Target Subject
+ User Context
    ↓
Local Realization
    ↓
Simulation
    ↓
Narrative Instance
```

Narrative Engine tồn tại như một cơ chế có causal identity và invariants riêng; nó không đồng nhất với story được sinh ra từ một lần áp dụng.

## 2. Meta Engine và Narrative Engine

Meta Engine cung cấp governing philosophy, nguyên tắc và ranh giới để Narrative Engine được hiểu và áp dụng.

```text
META ENGINE
→ establishes governing framework

NARRATIVE ENGINE
→ selected/formalized mechanism
→ applied under that framework
```

Điều này không tự biến mọi Narrative Engine thành subsystem thường trực của một hierarchy duy nhất. Quan hệ cụ thể vẫn phải theo source.

## 3. Narrative Engine

Narrative Engine là reusable narrative mechanism.

Một engine có thể định nghĩa các phần như:

- causal identity;
- invariants;
- operating principles;
- conditions;
- pressures;
- transformations;
- states;
- interfaces;
- actors;
- tools;
- failure/termination conditions;
- narrative consequences.

Danh sách này không phải schema bắt buộc.

```text
GREED ≠ SLOTH ≠ WRATH ≠ CHAOS ≠ LUST
```

Các engine được phép có kiến trúc nội bộ khác nhau.

## 4. Host Fiction

Host Fiction là môi trường fiction nơi engine được áp dụng.

```text
ENGINE ≠ HOST
HOST ≠ ENGINE IMPLEMENTATION
```

Engine không sở hữu Host Fiction chỉ vì được áp dụng vào đó.

Host Fiction có thể là:

- existing fiction;
- fan-created setting;
- original fiction;
- context khác được source/engine hỗ trợ.

## 5. World Bible

World Bible cung cấp luật vận hành cục bộ của Host Fiction.

Các rule về:

- metaphysics;
- ontology;
- magic;
- technology;
- institutions;
- history;
- social systems;
- character constraints;
- capability limits;

được dùng làm constraint và translation layer khi engine được hiện thực hóa cục bộ.

```text
Narrative Engine × Host Rules
→ Local Realization
```

Không tự import external world model nếu Host Fiction đã có rule tương ứng.

## 6. Target Subject và context

Target Subject được chọn cho từng application.

Nó có thể là một character, group, institution, relationship, social structure, situation hoặc target khác nếu engine/source hỗ trợ.

```text
TARGET
= application-specific

TARGET
≠ permanently owned protagonist of engine
```

User context có thể thêm điều kiện cho application nhưng không tự sửa engine canon.

## 7. Local Realization

Local Realization là hình thức engine có thể vận hành sau khi được diễn giải qua rule của Host Fiction.

```text
ENGINE IDENTITY
+ HOST RULES
→ LOCAL REALIZATION
```

Local Realization không tự sửa causal identity của engine.

Nếu host rule và engine requirement xung đột mà source không cung cấp cách giải:

```text
preserve incompatibility / UNKNOWN
≠ silently rewrite host
≠ silently rewrite engine
```

## 8. Narrative Instance

Narrative Instance là story/output của một configuration cụ thể.

```text
ENGINE
≠ LOCAL REALIZATION
≠ NARRATIVE INSTANCE
```

Cùng một engine có thể tạo realization và story rất khác khi:

- Host Fiction khác;
- World Bible khác;
- Target Subject khác;
- context khác;
- combination với engine khác khác;
- actor choices khác.

Sự khác biệt của output không tự chứng minh engine identity đã thay đổi.

## 9. Agency và outcome

Narrative Engine cung cấp causal pressures, conditions, interfaces và possibilities theo source.

Actor không mặc định là output thụ động.

```text
engine changes conditions
→ actors perceive / choose / adapt / resist / act
→ outcome remains simulation-dependent unless canon fixes it
```

Không preselect open endpoint.

## 10. Nhiều Narrative Engine trong cùng application

Nhiều engine có thể cùng xuất hiện hoặc cùng tiếp cận một target nếu source/configuration cho phép.

Điều đó không tự tạo:

```text
COMPOSITE
DEPENDENCY
PARENT-CHILD HIERARCHY
SHARED GOAL
SHARED AUTHORITY
```

Composite chỉ tồn tại khi source xác nhận composition, như trường hợp Chaos Engine.

## 11. V1.5 boundary

V1.5 và V2 là hai miền formalization khác nhau của The Academy; chúng không tự thay thế nhau.

```text
V1.5
= pre-grad institutional causal domain

V2
= Narrative Engine formalization/application domain
```

Không dùng V2 để suy ngược V1.5 "thật ra phải có" component hay schema nào.

Trong Academy lifecycle đã ghi nhận, các vận hành hậu return-to-origin nằm ngoài active runtime V1.5. Điều này không tự chứng minh mọi V2 application đều cần một graduate V1.5.

## 12. Engine mode hiện hành

Mode của từng engine phải lấy từ nguồn/xác nhận riêng.

Theo current repository state đã externalize:

- Sloth: V2;
- Wrath: V2;
- Chaos: V2.

Không dùng ba xác nhận này để gán mode cho Greed, Lust hoặc future engine.

## 13. Failure modes cần tránh

### 13.1. Engine → trope

Narrative Engine không được collapse thành một trope, character archetype, prompt hoặc fixed plot.

### 13.2. Host → subsystem của engine

Việc engine được áp dụng vào host không biến host thành subsystem thường trực.

### 13.3. Implementation → engine identity

Actor, weapon, interface hoặc local lore cụ thể không tự trở thành invariant phổ quát.

### 13.4. One-template collapse

Không ép mọi engine vào cùng component schema.

### 13.5. V2 → successor hierarchy

Version number và genealogy không tự tạo ladder:

```text
V1.5 → V2
```

không được hiểu là deprecation hoặc ontological replacement nếu source không nói vậy.

## 14. Sơ đồ chuẩn

```text
                  THE ACADEMY V2
          [NARRATIVE ENGINE APPLICATION]

              Meta Engine
                  │
                  ▼
       Select / Formalize Engine
                  │
                  ▼
          Causal Identity
             + Invariants
                  │
                  ▼
      Host Fiction + World Bible
                  │
          Target + Context
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

## 15. Provenance

Bản này tái cấu trúc nội dung đã tồn tại trong:

- [Narrative Engine — Core Design Philosophy](../../00_META/Narrative%20Engine%20%E2%80%94%20Core%20Design%20Philosophy.md);
- phần V2 của baseline V1.5 cũ;
- [The_Academy_CI_v2.0.md](../../00_META/controls/The_Academy_CI_v2.0.md);
- [The_Academy_Authorial_Decisions_2026-09-28.md](../../The_Academy_Authorial_Decisions_2026-09-28.md).

File này không supersede engine-specific source và không cấp capability mới cho engine.
