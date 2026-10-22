# Fanfiction Engine — Hệ này là gì và được dùng như thế nào?

**Trạng thái:** tài liệu giới thiệu theo mục đích và terminology đã được tác giả xác nhận.
**Phạm vi:** giúp đọc đúng toàn hệ, platform và hai miền vận hành; không thay thế nguồn cơ chế cụ thể hoặc lấp các vùng `UNKNOWN`.

Đọc cùng [Current State](00_META/controls/Fanfiction_Engine_Current_State.md), [Institutional Causality Architecture](02_FANFICTION_ENGINE_ARCHITECTURE/INSTITUTIONAL_CAUSALITY/Institutional_Causality_Architecture.md), [Narrative Engine Causality Architecture](02_FANFICTION_ENGINE_ARCHITECTURE/NARRATIVE_ENGINE_CAUSALITY/Narrative_Engine_Causality_Architecture.md) và nguồn engine/host liên quan.

## 1. Toàn hệ và platform bên trong

**Fanfiction Engine là toàn hệ mô phỏng fanfiction/daydream của tác giả. The Academy là platform nội bộ của hệ đó.**

```text
FANFICTION ENGINE != THE ACADEMY PLATFORM
```

Project trước đây được gọi là The Academy Project. Tên project hiện hành là Fanfiction Engine; tên The Academy tiếp tục được dùng cho platform và các cơ chế trong fiction theo nguồn.

The Academy giúp hợp thức hóa những operation như actor/HIP rời Host Fiction, đi qua môi trường xuyên fiction/reality, tương tác, vắng mặt khỏi timeline rồi quay lại, hoặc những causal transitions khác mà source/configuration cho phép. Platform không tự cấp mọi capability hoặc authority cho mọi actor. Những điều kiện chưa externalize vẫn để `UNKNOWN`.

Host Fiction là fiction nền được chọn cho một lần mô phỏng: tác phẩm có sẵn, fan-created setting hoặc fiction gốc. Host vẫn cung cấp nhân vật, lịch sử, thể chế, metaphysics, magic, technology và các luật cục bộ của nó.

```text
ENGINE APPLIES TO HOST
!= ENGINE CONTAINS HOST

HOST FICTION != SUBSYSTEM OWNED BY FANFICTION ENGINE
```

## 2. Đầu ra chính là thay đổi trạng thái và trajectory

Fanfiction Engine chủ yếu phục vụ mô phỏng trong đầu khi tác giả đọc, xem hoặc chơi một Host Fiction. Đầu ra quan trọng là trạng thái nhân quả mới của actor, quan hệ hoặc target, rồi xem những thay đổi đó tác động thế nào lên diễn tiến của host. Một đoạn văn, chương truyện hay kịch bản có thể biểu đạt kết quả; sinh văn bản không phải đầu ra chính.

Một ví dụ trong cấu hình đầy đủ có thể là:

```text
actor baseline A0
→ trải nghiệm, tri thức, khả năng, quan hệ và lựa chọn mới
→ actor state A1
→ gặp một event trong Host Fiction
→ phản ứng và hệ quả có thể khác baseline
```

A1 vẫn có continuity với A0. Engine thay đổi điều kiện và áp lực; actor giữ agency. Không chọn sẵn kết quả rồi dựng ngược nguyên nhân.

## 3. Hai miền vận hành của cùng hệ

| Tên hiện hành | Nhãn lịch sử |
| --- | --- |
| Institutional Causality | V1.5 |
| Narrative Engine Causality | V2 |
| Academy Revise — working branch | V2.5 |

Các nhãn số cũ ghi lại quá trình phát triển; chúng không đặt thứ tự thực thi hoặc hierarchy hiện hành.

Institutional Causality có thể chạy không cần Narrative Engine Causality. Narrative Engine Causality không cần một graduate hoặc toàn bộ Institutional Causality làm điều kiện tiên quyết. Hai miền có thể kết hợp khi source/configuration cho phép; chi tiết của từng cách kết hợp vẫn phải có nguồn.

```text
COMPOSITION != DEPENDENCY
COMPOSITION != REQUIRED SEQUENCE
LEGACY VERSION NUMBER != EXECUTION ORDER
```

## 4. Institutional Causality

Đây là miền nhân quả thể chế của Fanfiction Engine, vận hành qua The Academy platform và các thành phần theo nguồn: ban, faction, class, Teaching, các institutional mechanisms và tương tác HIP-HIP.

Các thành phần này có thể đóng vai causal filters hoặc nguồn tạo áp lực/trạng thái độc lập theo source. Một tên faction không tự chứng minh rằng nó là Narrative Engine. HIP không xoay quanh một protagonist trung tâm; khác biệt giữa các HIP cũng có thể tạo hệ quả mà không cần staff hay engine viết sẵn xung đột.

Cấu hình đầy đủ đã externalize gồm:

```text
HIP selection / recruitment / consent khi applicable
→ The Academy
→ institutional engines / Teaching / peer-HIP interaction
→ choices, exposure, adaptation
→ graduation
→ RETURN TO ORIGIN
```

Trong cấu hình đó, return to origin kết thúc miền vận hành thể chế trước tốt nghiệp; các operation hậu return được xét riêng. Sơ đồ không buộc mọi lần dùng Institutional Causality phải đi trọn một school arc hay transformation pipeline.

Trong một configuration, The Academy cùng Institutional Causality cũng có thể cung cấp lời giải thích nhân quả/platform cho historical absence hoặc timeline skip. Cơ chế và điều kiện cụ thể vẫn theo source; không tự bổ sung cho trường hợp chưa externalize.

## 5. Narrative Engine Causality

Đây là miền định nghĩa/formalization và áp dụng Narrative Engine vào một host, target và context cụ thể.

```text
Narrative Engine definition / formalization
+ Host Fiction
+ World Bible / host rules
+ target / context
→ Local Realization
→ simulation
→ changed causal state / trajectory; possible Narrative Instance
```

Một application có thể chạy độc lập khi source/configuration cho phép. Target không bắt buộc là graduate của Institutional Causality. Áp lực engine có thể thay đổi điều kiện, quan hệ hoặc trajectory mà không đi qua toàn bộ quá trình học tại The Academy.

World Bible ràng buộc những gì có thể xảy ra trong host. Cùng engine có thể hiện thực hóa rất khác trong những host khác nhau, nhưng không tự đổi causal identity hoặc xóa host rules. Không ép Greed, Sloth, Wrath, Chaos, Lust hay engine tương lai vào một mẫu chung.

## 6. HIP và agency

Historical Influence Potential (`HIP`) là cổng đánh giá mở dùng tiêu chí từ context. HIP không tự định nghĩa potential, influence, significance hay qualification; không phải power level, morality score, protagonist marker hoặc bảo đảm rằng target sẽ thay đổi lịch sử.

Actor chỉ dùng thông tin, khả năng và authority mà nguồn/trạng thái mô phỏng cho phép. Engine có thể tạo điều kiện; actor có thể lựa chọn, thích nghi, chống lại hoặc tạo hệ quả ngoài dự kiến.

## 7. Academy Revise

[Academy Revise](02_FANFICTION_ENGINE_ARCHITECTURE/BRANCHES/Academy_Revise_Branch.md) tiếp tục là `WORKING BRANCH`. Nó nghiên cứu cách kết hợp hai miền mà vẫn giữ causal identity riêng. Nó không phải giai đoạn thứ ba bắt buộc, successor theo số version hoặc sự thống nhất ontology đã được chấp thuận.

## 8. Cách dùng và giới hạn nguồn

Một session có thể bắt đầu từ actor, target, điều kiện hoặc câu hỏi trong Host Fiction. Tác giả chọn miền/engine phù hợp, áp dụng những quy tắc đã có nguồn, rồi tiếp tục mô phỏng state và hệ quả trong đầu. Host Fiction cung cấp phần lớn hình ảnh, thoại, setting và event; không cần tái sản xuất toàn bộ thành văn bản.

Repository là phần được externalize của mô hình tác giả. Nội dung chưa được ghi ra không đồng nghĩa không tồn tại; model thiếu nguồn không được tự hoàn thiện graph. Genealogy, quyết định có ngày tháng và archive giữ terminology của thời điểm chúng được ghi. Dùng Current State để ánh xạ tên hiện hành.

Các từ engine, module, interface và architecture giữ nghĩa trong nguồn của project; không tự nhập một kiến trúc software hoặc hierarchy vào hệ. Trạng thái repository và hành vi ChatGPT Project khi chạy là hai lớp bằng chứng riêng.
