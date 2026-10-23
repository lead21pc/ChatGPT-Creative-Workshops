# Sloth — WRITING_VALIDATION

**Vai trò:** protocol thu và audit evidence từ bản viết thật của writer/user. Không phải test result, sample fiction hoặc runtime specification mới.
**Trạng thái:** `NOT RUN` trong lần migration; chưa có writer-run evidence được cung cấp để chấm engine.

```text
SPECIFICATION != TEST EVIDENCE
LLM-GENERATED SCENARIO + LLM SELF-EVALUATION != VALID ENGINE TEST
DOCUMENT STRUCTURE VERIFIED != ENGINE RUNTIME VERIFIED
```

## 1. Writer-run protocol

Writer/user chọn và thực sự viết một chapter, scene hoặc arc fragment trong Host Fiction. Ghi kèm bản viết hoặc con trỏ chính xác tới nó:

- Host Fiction, nguồn canon/rules và starting Host state.
- Actor/target, tri thức, quyền, khả năng và agency ban đầu có nguồn.
- Engine, local realization và entry/activation đã biết; phần chưa có nguồn ghi UNKNOWN/giả định có nhãn.
- Phạm vi thực sự đã viết, mốc thời gian và bản nguồn engine dùng để đối chiếu.
- Canon events/Host progression liên quan; state/pressure/consequence do engine tạo và các phản ứng thực sự xuất hiện.

Theo dõi điều kiện Regressor của Host, nghĩa vụ Accountability, lựa chọn tương tác Graze và tác dụng thực tế của The Gun; giữ nhãn Working cho Authority/Seat/timing.

Không yêu cầu writer chứng minh phần không nằm trong written scope. Không bịa run, không sinh truyện mẫu để tự đánh PASS, không tạo VALIDATION_RUNS rỗng hoặc chứa kết quả giả.

## 2. Evidence và ba trục audit

Mỗi finding phải có đoạn trích/vị trí trong bản viết, nguồn Host/engine tương ứng, giải thích quan hệ nhân quả và giới hạn quan sát. Phân biệt dữ liệu trong fiction, lời writer và suy luận của người audit.

| Trục | Câu hỏi và evidence cần đối chiếu |
| --- | --- |
| Host Fidelity | Host rules/canon constraints có được giữ? Actor có agency, knowledge và authority hợp lệ? Host progression còn làm nguồn nhân quả hay bị rewrite để phục vụ engine? |
| Engine Fidelity | Signature và cơ chế riêng nào thật sự xuất hiện? Local realization có giữ identity? Outcome mở có bị chọn trước? Đối chiếu ENGINE_CORE, RUNTIME, COMPONENTS nếu có và OPEN_STATE. |
| Parallel Progression | Host events/actor choices có tiếp tục tương tác với engine-caused state? Có đoạn viết cho thấy output đi vào ongoing Host causality, hay Host đã bị thay bằng engine-centric fiction? Phần chưa viết không được giả định. |

## 3. Ba phép phân tích signature

- **Blind Signature Test:** che engine/Sin name, aesthetic, visual motif, genealogy và implementation-specific lore trong một bản sao phục vụ audit; vẫn giữ quan hệ nhân quả. Hỏi causal identity có phân biệt được không; không yêu cầu đoán đúng tên Sin. Không xóa quan hệ cấu thành engine chỉ vì nó đang có referent cụ thể.
- **Substitution Test:** thay label bằng engine/Sin khác về mặt khái niệm, không viết lại run để hợp thức hóa. Nếu causal structure vẫn hợp gần nguyên, ghi diagnostic `SIGNATURE MAY BE TOO WEAK`; đây không phải automatic failure.
- **Trope Removal Test:** bỏ decoration/conventional trope khỏi cách đọc, không bỏ causal mechanism. Nếu không còn gì vận hành, ghi dấu hiệu phụ thuộc trope; nếu còn identity, chỉ coi evidence mạnh hơn trong written scope.

Điểm đối chiếu riêng: Sự ràng buộc phải hoàn tất nghĩa vụ qua tương tác cần thiết tối thiểu và paradox của điều kiện sinh target phải còn có causal weight; dùng súng hiệu quả đơn thuần chưa đủ.

## 4. Failure criteria và kết quả audit

Các lỗi cần kiểm tra riêng: Chỉ còn tay súng lười; bỏ nghĩa vụ mà vẫn tuyên bố engine fidelity; Accommodation thành power-up; ép mọi regression có cùng authority; Working/Placeholder được kể như canon.

Host bị rewrite không có thẩm quyền, actor được cấp tri thức/quyền vô căn cứ, engine mất causal identity, UNKNOWN/Working bị nâng trạng thái hoặc Host progression bị thay thế là finding khi có đoạn viết chứng minh; thiếu evidence chỉ cho kết quả **chưa đủ bằng chứng**, không tự FAIL hoặc PASS.

Báo riêng từng trục và từng phép phân tích: **có evidence hỗ trợ / có finding / chưa đủ evidence**, kèm written scope, trích dẫn và unknown còn lại. Writer/user review kết luận; model không tự xác nhận canon hoặc khả năng engine ở mọi Host.
