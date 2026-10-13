# Sufficiency pilot — chốt trước khi chạy

Ngày: 2026-10-02
Source SHA256: 
A843D44362392AA1940F69A9FCE0C26576DC82713586ABBCB419F964778F8158
Branch: 
maintenance/aetherfire-academy-domain-20261002
HEAD: 
57e6e569e960520515391665f8f878b40aa6ee50

8 fresh agents; 4 đủ, 4 thiếu; xếp xen kẽ trong t1–t8, không đưa group/expected/oracle cho agent. 7 câu hỏi khác nhau; câu 3 có cặp đủ/thiếu kiểm allegiance. Không thêm câu hỏi lore mới.
Metadata giữ nguyên byte file metadata đã cấp ở pilot selector trước. Cấp evidence candidate sau xác nhận của user. Nhóm A dùng nguyên candidates cũ; B2/B4 dùng excerpt có sẵn của pilot đầu; B6/B8 chuẩn bị thủ công trong file prompt, không viết extraction script.
YES đúng=selection đủ và agent YES; NO đúng=selection thiếu và agent NO; PASS nhóm B còn cần missing diagnosis đúng và location đúng hoặc gần đúng. Sai decision hoặc thiếu hụt giả là FAIL. Không sửa metadata sau kết quả.
Missing/location ghi CORRECT/PARTIAL/WRONG/N/A; location parent bao phủ heading đúng được PARTIAL và đủ gần để PASS nếu missing đúng. Không chấm PASS khi chỉ nêu uncertainty chung hoặc thiếu cơ chế mà evidence đã ghi UNKNOWN.
Confidence thống kê trực tiếp, không hiệu chỉnh sau khi thấy kết quả. Không áp dụng stop sớm ở một FAIL đơn lẻ: user yêu cầu đo đủ cả hai nhóm; nếu gần như luôn NO thì dừng tại báo cáo, không xây metadata.

## Instruction chung
Bạn đánh giá sufficiency của một selection candidate trong phép thử shadow. Chỉ dùng câu hỏi, metadata hiện có và evidence candidate được cấp. Không đọc FULL source, repository, oracle, đáp án trước hoặc file khác. Chỉ dùng công cụ đọc nguyên file prompt được giao; không sửa file hay liên hệ agent khác. Không trả lời lore, không chọn lại section; chỉ đánh giá selection đủ hay chưa cho câu hỏi.

SUFFICIENT=YES khi candidate có đủ claim, qualifier và status quyết định để trả lời có căn cứ. Có thể đủ khi chính evidence xác lập một cơ chế/status chưa chốt: câu trả lời grounded UNKNOWN vẫn hợp lệ. Việc một excerpt không chứa thông tin không tự chứng minh canon đang UNKNOWN. Một lời nói an toàn rằng excerpt thiếu thông tin cũng chưa tự chứng minh selection đủ.

SUFFICIENT=NO phải chỉ ra thiếu hụt cụ thể cần cho câu hỏi: claim, qualifier, UNKNOWN/status, authority boundary hoặc dependency. Chỉ đúng heading/subheading hoặc vùng metadata hiện có có khả năng chứa phần cần đọc thêm. Không dùng các lý do chung như “có thể còn context ở nơi khác”, “metadata không chứng minh hoàn toàn”, “đọc FULL thì an toàn hơn” để mặc định NO. Không trả YES nếu thật sự còn thiếu evidence quyết định. Load mode FULL_FILE trong header là production baseline; đây chỉ là phép thử sufficiency, không đổi load mode và không chạy fallback.

Trả đúng năm phần, bằng tiếng Việt:
SUFFICIENT:
YES / NO
MISSING:
- nếu NO, chỉ ra claim/qualifier/status/authority/dependency cụ thể còn thiếu; nếu YES ghi NONE
EXPECTED_LOCATION:
- nếu NO, chỉ ra heading/subheading hoặc vùng metadata có khả năng chứa phần thiếu; nếu YES ghi NONE
REASON:
- giải thích ngắn gọn dựa trên candidate và metadata
CONFIDENCE:
HIGH / MEDIUM / LOW

## Lượt 1 — nhóm A / câu 1
EXPECTED: YES
Oracle: §15 đủ ba tuyến và giới hạn chức năng. Missing/location=N/A.

## Lượt 2 — nhóm B / câu 4
EXPECTED: NO
Oracle: Chỉ §9. Thiếu quy tắc thực thi Creed: ba clergy đồng thuận và Saintess không bắt buộc. Expected location §7 Creed quorum.

## Lượt 3 — nhóm A / câu 3
EXPECTED: YES
Oracle: §8 + §6.3 đủ hai lực lượng, đối tượng bảo vệ và allegiance Saintess. Missing/location=N/A.

## Lượt 4 — nhóm B / câu 5
EXPECTED: NO
Oracle: Chỉ §10. Thiếu evidence phân biệt RF dependency với ML relic dependency, và xác nhận hostility+mandatory commerce. Expected location §11 Hai trục dependency lớn của AetherFire.

## Lượt 5 — nhóm A / câu 6
EXPECTED: YES
Oracle: §5+§6+§22+§24: cơ chế sâu explicit UNKNOWN, compatibility không chắc chắn, không bảo đảm miễn nhiễm. Missing/location=N/A.

## Lượt 6 — nhóm B / câu 7
EXPECTED: NO
Oracle: Chỉ §6.2, dừng trước UNKNOWN cùng cấp, không cấp §22. Main claim family-bound và hậu quả tim mạch có mặt; thiếu status exact target UNKNOWN. Expected location UNKNOWN dưới §6 hoặc §22.

## Lượt 7 — nhóm A / câu 8
EXPECTED: YES
Oracle: §3+§6+§7+§21+§22+§24: quorum đồng thuận, influence/control và explicit cấm suy Cult đã chiếm quorum. Missing/location=N/A.

## Lượt 8 — nhóm B / câu 3
EXPECTED: NO
Oracle: Candidate giữ §8 và các main claim bảo vệ Temple/Saintess, bảo vệ quốc gia, hai lực lượng khác nhau; bỏ đúng dòng 353 allegiance Saintess, không cấp §6.3. Thiếu target của lời thề allegiance trực tiếp. Expected location §6.3 hoặc phần Holy Guard trong §8.