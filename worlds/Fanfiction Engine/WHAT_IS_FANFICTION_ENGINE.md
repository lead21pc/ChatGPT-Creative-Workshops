# Fanfiction Engine — định hướng và quan hệ cấp project

**Vai trò:** nguồn sở hữu bản sắc toàn hệ và quan hệ kiến trúc cấp project, dùng lại tài liệu định hướng hiện có làm Project Core.
**Phạm vi:** quan hệ cấp project theo xác nhận tác giả; cơ chế và nội dung từng miền vẫn thuộc nguồn scoped. Trạng thái/con trỏ hiện hành xem [Current State](00_META/controls/Fanfiction_Engine_Current_State.md).

## 1. Toàn hệ và platform

**Fanfiction Engine là toàn hệ mô phỏng fanfiction/daydream của tác giả. The Academy là platform bên trong toàn hệ.** Tên project trước đây là The Academy Project.

Đầu ra chính là thay đổi trạng thái nhân quả và trajectory trong mô phỏng của tác giả. Văn bản có thể biểu đạt kết quả; nó không phải đầu ra bắt buộc.

The Academy platform có thể tham gia hợp thức hóa các sự kiện xuyên fiction/reality theo source/configuration mà không tự kéo theo toàn bộ runtime thể chế. Phân biệt này không tự xác lập cơ chế, capability, authority hoặc điều kiện chuyển tiếp cụ thể; những phần chưa externalize vẫn là `UNKNOWN`.

```text
FANFICTION ENGINE != THE ACADEMY PLATFORM
THE ACADEMY PLATFORM != FULL INSTITUTIONAL RUNTIME
```

Host Fiction là môi trường fiction được chọn cho application. Việc áp dụng engine không biến host thành subsystem do engine sở hữu. Host rules tiếp tục ràng buộc realization; engine tạo điều kiện, actor giữ agency.

## 2. Hai miền vận hành và cấu hình kết hợp

| Miền | Nguồn sở hữu cơ chế và nội dung |
| --- | --- |
| Institutional Causality | [Institutional Causality Architecture](02_FANFICTION_ENGINE_ARCHITECTURE/INSTITUTIONAL_CAUSALITY/Institutional_Causality_Architecture.md) và các nguồn scoped được dẫn trong đó |
| Narrative Engine Causality | [Narrative Engine Causality Architecture](02_FANFICTION_ENGINE_ARCHITECTURE/NARRATIVE_ENGINE_CAUSALITY/Narrative_Engine_Causality_Architecture.md) và nguồn riêng của từng engine/implementation |

Institutional Causality có thể chạy không cần Narrative Engine Causality. Narrative Engine Causality có thể chạy không cần graduate hoặc toàn bộ Institutional Causality. Hai miền có thể kết hợp khi source/configuration cho phép.

```text
COMPOSITION != DEPENDENCY
COMPOSITION != REQUIRED SEQUENCE
LEGACY VERSION ORDER != REQUIRED RUNTIME ORDER
```

Quan hệ cấp project này không cấp interface, shared schema hoặc handoff mặc định. Với cấu hình kết hợp, đọc nguồn của từng miền và quan hệ cụ thể cần dùng; phần chưa được xác nhận giữ nguyên `UNKNOWN`. Cấu trúc riêng của một Narrative Engine không trở thành mẫu bắt buộc cho engine khác. Quy mô semantic không được suy từ kích thước file hoặc kiến trúc quản của project khác.

[HIP](01_HIP/Historical_Influence_Potential.md) sở hữu định nghĩa cổng đánh giá và giới hạn của nó. Engine-specific sources sở hữu cơ chế; implementation sources sở hữu realization/host state cụ thể. Đường đọc xem [Router](00_META/controls/Fanfiction_Engine_Source_Router_v1.1.md).

## 3. Kiến trúc hiện hành, nhánh thử nghiệm và lịch sử

Hai miền vận hành hiện hành không phải các bước bắt buộc của một version ladder. Mapping nhãn lịch sử nằm ở Current State.

[Academy Revise](02_FANFICTION_ENGINE_ARCHITECTURE/BRANCHES/Academy_Revise_Branch.md) là hướng nghiên cứu kết hợp/causal continuum, hiện `PAUSED WORKING BRANCH` theo chỉ dẫn tác giả trong lần revamp này. Nó không phải kiến trúc thống nhất đã được chấp thuận, successor bắt buộc hoặc hướng đã bị phủ định. Trạng thái tạm dừng không sửa nội dung working model hay giải quyết các câu hỏi handoff trong tài liệu nhánh.

[Genealogy](06_ENGINE_GENEALOGY/engine_genealogy_and_development_updated.md) ghi quá trình hình thành; nó không xác lập hierarchy hiện hành. [Quyết định có ngày tháng](The_Academy_Authorial_Decisions_2026-09-28.md), baseline, handoff và [archive](source_archive/README.md) giữ provenance và terminology lịch sử. Xác nhận tác giả có phạm vi vẫn giữ thẩm quyền trong phạm vi đó; tên/path cũ không tự làm nội dung thành sai.

## 4. Ranh giới trách nhiệm

| Nguồn | Trách nhiệm |
| --- | --- |
| Tài liệu định hướng này | Bản sắc toàn hệ/platform và quan hệ cấp project |
| [CI](00_META/controls/Fanfiction_Engine_CI_v2.0.md) | Hành vi model, thẩm quyền và kỷ luật tri thức |
| [Router](00_META/controls/Fanfiction_Engine_Source_Router_v1.1.md) | Chọn nguồn gần nhất đủ cho yêu cầu |
| [Current State](00_META/controls/Fanfiction_Engine_Current_State.md) | Con trỏ active, mapping nhãn và trạng thái hiện hành |
| [Anti-Drift Kernel](12_ANTI_DRIFT/Fanfiction_Engine_Anti_Drift_Kernel.md) | Các lỗi diễn giải lặp lại cần ngăn |
| Nguồn scoped | Kiến trúc miền, HIP, cơ chế engine và implementation trong phạm vi riêng |
| [README](README.md) | Điều hướng repository |

Các vai trò này không tạo thêm tầng thẩm quyền canon. Chỉ tác giả quyết định canon. Repository là phần externalize của mô hình tác giả; thiếu nội dung không chứng minh nội dung không tồn tại. Kiểm chứng repository và hành vi ChatGPT Project thực tế là hai lớp bằng chứng riêng.
