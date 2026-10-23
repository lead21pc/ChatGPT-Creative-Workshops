# Sloth — RUNTIME

**Vai trò:** sở hữu cấu trúc vận hành riêng của engine; không phải universal pipeline.
**Trạng thái nguồn:** Working Draft; các mục Stable giữ đúng phạm vi của nguồn. Tái cấu trúc tài liệu không nâng canon, Working, Placeholder hoặc UNKNOWN. Các mô tả signature là cách đọc phân tích bám nguồn, không là quyết định canon mới.

Đọc theo nhu cầu: [identity/signature](ENGINE_CORE.md), [ranh giới Host](HOST_CONTRACT.md), [vận hành](RUNTIME.md), [vùng mở](OPEN_STATE.md), [kiểm chứng bằng bản viết](WRITING_VALIDATION.md). Đây là vai trò tài liệu, không phải các bước thực thi engine.

## Đường đọc vận hành

- [Đối tượng và HIP trong nguồn Sloth](#5-historical-influence-potential).
- [Model tích hợp](#9-integrated-operational-model) và [quan hệ có loại](#10-module-relations).
- Chi tiết [Accommodation](COMPONENTS/Accommodation.md), [Graze](COMPONENTS/Graze.md), [The Gun](COMPONENTS/The_Gun.md).



# 5. Historical Influence Potential

Regressor được xem là một dạng **Historical Influence Potential** rất cao.

Regressor có thể:

- mang kiến thức từ nhiều lần hồi quy;
- thử lại quyết định;
- tối ưu hành động;
- thay đổi chuỗi nhân quả;
- tạo divergence lớn;
- phủ quyết hoặc thay thế trạng thái lịch sử trước đó.

Do đó Sloth không săn Regressor vì họ “xấu” hay vì regression tự thân là tội.

Regressor là đối tượng phù hợp với operation của Sloth vì họ vừa là HIP cao vừa trực tiếp xâm phạm Authority / Seat mà Sloth giữ.

---


# 9. Integrated Operational Model

```text
Entropy Engine
        ↓
Accommodation
        ↓
Regressor / high-HIP anomaly
        ↓
Seat / Authority violation
        ↓
Accountability
        ↓
Sloth must act
        ↓
Graze
        ↓
Minimum necessary interaction
        ↓
The Gun
        ↓
Decisive resolution
        ↓
Duty discharged
        ↓
Return to rest
```

Model này mô tả operation hiện tại.

Nó không phải story arc và không yêu cầu end-state narrative.

---


# 10. Module Relations

```text
Sloth --HAS_COUNTER--> Accountability
Sloth --USES_CATALYST--> Accommodation
Sloth --USES_DOCTRINE--> Graze
Sloth --USES_TOOL--> The Gun
Sloth --HUNTS--> Regressors

Accommodation --ENABLES_CONDITION_FOR--> Regressor
Regressor --QUALIFIES_AS--> High HIP
Regressor --VIOLATES--> Sloth's Seat / Authority

Accountability --CONSTRAINS--> Sloth
Graze --MINIMIZES--> Unnecessary Interaction
The Gun --EXECUTES--> Decisive Resolution
```

---


## Owner của các component

- [Accommodation](COMPONENTS/Accommodation.md): catalyst/interface và paradox sinh điều kiện.
- [Graze](COMPONENTS/Graze.md): doctrine chọn tương tác tối thiểu.
- [The Gun](COMPONENTS/The_Gun.md): tool thực thi.

Các sơ đồ trên giữ nguyên operational model của Sloth, không là pipeline cho engine khác. Khả năng, timing và trigger chưa chốt không được suy từ việc sơ đồ có một mũi tên.
