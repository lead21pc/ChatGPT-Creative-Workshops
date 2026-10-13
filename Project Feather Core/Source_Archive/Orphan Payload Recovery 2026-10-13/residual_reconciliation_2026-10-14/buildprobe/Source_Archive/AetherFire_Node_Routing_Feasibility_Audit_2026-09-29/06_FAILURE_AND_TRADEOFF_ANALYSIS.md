# 06 — Failure và đánh đổi

> Ba mô hình dưới đây giải những mức vấn đề khác nhau. Audit không xếp hạng chung; quyết định phải dựa vào kết quả shadow test và chi phí bảo trì thật.

| Tiêu chí | Full-file hiện hành | Markdown node-or-full trung gian | Full registry/schema proposal cũ |
| --- | --- | --- | --- |
| Premise coverage | Cao hơn khi đọc thành công toàn file; còn phụ thuộc model chú ý đủ | Có thể giảm đọc thừa; dễ bỏ qualifier nếu mapping/closure sai; full fallback giới hạn rủi ro | Có thể hỗ trợ static graph/routing phức tạp, nhưng registry có thể lệch nội dung và không bảo đảm model đọc đúng |
| Runtime dependencies | Project instructions + Markdown source | Cùng số loại dependency: instructions + Markdown; thêm contract/index trong file | Thêm registry/parser/descriptor hoặc pipeline phát hành nếu dùng runtime |
| Chi phí người duy trì | Ít metadata, nhiều context mỗi task | Reviewer phải chăm node boundary, header và decisive `REQUIRES` khi nội dung đổi | Nhiều schema, ID, relation và đồng bộ giữa generated artifacts |
| Khi index lỗi | Không có index | Trở về full current file nếu còn đọc được; nếu file thiếu thì block | Tùy thiết kế; nếu registry là đường duy nhất, lỗi có thể chặn routing cả package |
| Kích thước/latency | Có thể cao với `30/90`, nhưng chưa đo runtime | Có thể thấp hơn cho task hẹp **chỉ nếu backend/runtime thực sự đọc được closure** | Có thể tối ưu offline, chưa chứng minh lợi ích Project runtime |
| Tính giải thích được | Đọc tài liệu gốc trọn vẹn | Index đọc được bằng mắt, edge có lý do reviewer | Có thể rõ với máy, khó hơn cho người không chuyên |

## Failure cần gắn với mitigation cụ thể

1. **Node cắt mất priority muộn.** `10` có khối latest-priority lớn đầu file; `30` có visual correction ở nhiều vị trí sâu. Một header ngắn tự viết có thể thiếu ngoại lệ. Mitigation: semantic review từng query class, diff với full read; nếu không rút gọn an toàn, file `FULL_FILE`.
2. **`REQUIRES` suy từ mention.** `10` nhắc ML/aviation hoặc `90` nhắc Undie không đủ chứng minh dependency quyết định. Mitigation: edge cần câu hỏi mẫu, premise cụ thể và reviewer; không chắc → `REVIEW_REQUIRED`/full read.
3. **Stale local index do generated view thay đổi.** `build_consolidation.ps1` ghi trực tiếp `00–92`; marker sửa tay biến mất sau rebuild. Mitigation: pilot trên shadow copy, sau activation sinh/validate marker từ nơi build đúng, kiểm index↔content/span ở mỗi generation. Không yêu cầu giải toàn bộ builder transaction trước pilot shadow.
4. **Backend chỉ trả snippet/search result nhưng model tưởng đã đọc node.** Đây là `UNVERIFIED RUNTIME ASSUMPTION`. Mitigation: test Project thật với prompt buộc trích qualifier ở nhiều vị trí; nếu không kiểm được đầy đủ closure, giữ full-file. Không tuyên bố retrieval guarantee từ local parser.
5. **History tăng authority.** `90` chứa current update lẫn retired/proposal; cắt cluster làm mất nhãn dễ phục hồi route cũ. Mitigation: phase đầu full, về sau status-aware review và test anti-revival riêng.
6. **Record mất addendum.** `91` có addenda mới nhất ở đầu và `AF-CX` ở Part II; một record cũ không đủ khi bị phần trên override. Mitigation: `RECORD_OR_FULL` phải kèm priority/addendum liên quan; nếu không resolve, full.
7. **`92` hook stale hoặc chưa exhaust unknown.** Hook tùy chọn không thay filename và không thay source gate; validator kiểm hook còn tồn tại; unknown ngoài `92` vẫn có thể xuất hiện trong domain file.
8. **Overlay bị tối ưu nhầm.** Control header/open/stop/dependency nằm rải rác. Giữ overlay full-file phase đầu; không mất thời gian tạo node khi chưa thấy bottleneck.
9. **Cross-file closure nổ lớn.** Một câu hỏi đụng `10`, `20`, `30`, `40`, `70` có thể biến node mode thành nhiều edge/đọc gần full. Mitigation: ngưỡng thực dụng “closure rộng/không chứng minh đủ → full file của các owner liên quan”, không cố ép tiết kiệm.
10. **Partial update giữa CI, Router và generated files.** CI hiện phủ định excerpt và Router bắt whole-file. Nếu chỉ thay một mặt, hai control xung đột. Mitigation: mọi activation sau này phát hành như một bộ được kiểm snapshot/pinned, rollback về full-file contract khi một thành phần không khớp.

## Tách bốn track

| Track | Vấn đề | Quan hệ với phase node routing |
| --- | --- | --- |
| A — Runtime source routing | CI/Router contract, local index, closure, fallback, Project shadow test | Trực tiếp. |
| B — Builder/package safety | Đã thấy direct writes trong builder; partial output, replacement miss, code-fence heading transform và package/manifest discrepancy là các finding cũ cần tái hiện riêng trước khi coi là xác nhận mới | Có liên hệ **chỉ** ở chỗ index phải sống qua build và shadow package phải nhất quán. Atomic publication và các bug builder khác là dự án riêng. |
| C — Repository/tooling resolver | Numeric resolver có thể chọn file `DRAFT`; repo CI copy vs installed CI | Không dùng repo resolver để mô tả Project runtime; sửa resolver là việc khác. |
| D — Future mutation/reverse-impact | Biết câu canon đổi ảnh hưởng node nào, owner/interface nào | Không bắt buộc cho read-only node route; chỉ cần trước khi cho phép mutation rộng dựa vào node graph. |

`AetherFire_Architecture_Revamp_Package/` và audit 2026-09-26 là lịch sử proposal. Những registry toàn cục, release descriptor, per-module manifest và interface database của proposal cũ quá nặng cho **phase 1 read routing**. Tuy nhiên builder-aware generation, consistency check và activation gate không phải trang trí: generated views sẽ ghi đè index sửa tay, còn contract CI/Router lệch nhau là failure trực tiếp. Đây là dependency đã chứng minh, không phải lý do để đưa toàn bộ schema cũ vào runtime.
