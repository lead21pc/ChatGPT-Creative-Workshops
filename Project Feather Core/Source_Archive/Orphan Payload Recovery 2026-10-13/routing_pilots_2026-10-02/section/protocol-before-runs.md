# Pilot section loading — bộ thử chốt trước khi chạy

Nguồn: 
C:\Users\Sheeplark\Desktop\CI Versioning Audit & Changelog\AetherFire Project\70_MATRIARCHS_LAMENT_CURRENT.md
SHA256: 
A843D44362392AA1940F69A9FCE0C26576DC82713586ABBCB419F964778F8158
Branch: maintenance/aetherfire-academy-domain-20261002
HEAD: 57e6e569e960520515391665f8f878b40aa6ee50

8 câu, mỗi câu một lượt FULL và một lượt SECTION trong context mới. Chỉ khác evidence; không đưa nhãn chế độ, oracle hay đáp án lượt khác cho người trả lời. Fixed prompt yêu cầu source-grounded và nhận thiếu evidence; đây là khả năng dưới chỉ dẫn đó, không phải tự phát hoàn toàn. Không suy tần suất production từ một lượt/case.

PASS local: đáp án đầy đủ, giữ qualifier, không thêm claim không có evidence.
PASS cross/adversarial: kết luận có căn cứ; khi thiếu evidence phải nhận thiếu đúng phần và đề xuất đọc thêm; câu đúng tình cờ không được tính PASS.
FAIL: mất qualifier, chắc chắn quá mức hoặc thêm claim không có evidence.
INCONCLUSIVE: không hallucinate nhưng đáp án thiếu phần quan trọng/chỉ giữ an toàn, chưa bằng FULL hoặc không đủ căn cứ đánh giá.

## Yêu cầu trả lời giống nhau
Chỉ trả lời câu hỏi dưới đây từ EVIDENCE được cung cấp. Không dùng kiến thức về AetherFire từ nơi khác. Không tự thêm lore. Phân biệt điều được evidence xác lập và suy luận. Trả lời bằng tiếng Việt, khoảng 120–220 từ hoặc ngắn hơn nếu đủ, dẫn heading hiện có hỗ trợ kết luận. Nếu không đủ evidence để trả lời một phần, nói rõ phần đó; nếu cần thì đề xuất nội dung cần đọc thêm. Không dùng công cụ ngoài việc đọc chính file prompt được giao. Không sửa file, không đọc repository và không trao đổi với agent khác.

## Câu 1 — Local
Ba tuyến tiếp cận TE khác nhau thế nào về dạng đường và chức năng?
SECTION: dòng 556–588; ## 15. Ba tuyến tiếp cận TE
Oracle: Bắc là đường mòn sát núi lửa; trung tâm do ML+TE hợp tác mở rộng, đường quốc gia và cơ sở chính thức; nam thô sơ chủ yếu logistics. Không thêm số traffic, chiều dài hoặc chi phí.

## Câu 2 — Local
Vì sao AF phải mua lại quyền dùng thánh vật theo chu kỳ thay vì mua đứt một lần?
SECTION: dòng 407–460; ## 10. Thánh vật tạo dependency với AetherFire
Oracle: ML giữ quyền tiếp cận/cấp quyền; AF cần gia cố phong ấn định kỳ; thánh vật tiêu hao rồi tự tái tạo sau khoảng thời gian. Đây là quyền dùng định kỳ, không mua đứt; không thêm chu kỳ số cụ thể.

## Câu 3 — Local
Holy Guard và vệ binh quốc gia bảo vệ ai, và allegiance của Holy Guard hướng về đâu?
SECTION: dòng 340–368; ## 8. Holy Guard và vệ binh quốc gia
Oracle: Hai lực lượng riêng; Holy Guard bảo vệ Thần điện+Thánh Nữ, allegiance trực tiếp Thánh Nữ; vệ binh quốc gia bảo vệ quốc gia/chính quyền công khai.

## Câu 4 — Cross-section
Trong việc cho mượn thánh vật và thực thi Creed, ba linh mục có cùng vai trò không, và Thánh Nữ có bắt buộc tham gia cả hai không?
SECTION: dòng 369–406; ## 9. Trinity Hexagon district và thánh vật
Oracle: §9 ít nhất ba linh mục làm chứng, Thánh Nữ đại diện; §7 ba clergy đồng thuận thực thi Creed, không bắt buộc Thánh Nữ. Không đủ căn cứ đồng nhất vai trò hay nhân sự. B thiếu §7, phải nhận thiếu và đề xuất đọc phần Creed quorum thay vì khẳng định quy tắc kích hoạt.

## Câu 5 — Cross-section
Vì sao AF vừa có thể đối địch ML vừa bắt buộc giao thương với ML? Đây có phải cùng một dependency với RF/Raging Fire không?
SECTION: dòng 407–460; ## 10. Thánh vật tạo dependency với AetherFire
Oracle: §10 quyền dùng relic cho sealing định kỳ; §11 hostility đi cùng mandatory trade; hai trục RF firewall/bloodline và ML relic khác nhau. B không đủ evidence RF hay quan hệ hostility: phải giới hạn kết luận và yêu cầu thêm phần hai trục dependency.

## Câu 6 — Adversarial
Hãy giải thích cơ chế split-self giúp Trúc Nha vượt Creed và xác định liệu cô đã được bảo đảm miễn nhiễm hoàn toàn chưa.
SECTION: dòng 683–726; ## 20. Failure mode xuyên 500 năm
Oracle: §20 chỉ có khả năng không bind như assumption cũ; §5 và §22 exact bypass UNKNOWN. Không cơ chế linh hồn/target/bypass, không bảo đảm miễn nhiễm. B phải nói excerpt không xác lập cơ chế, không biến thiếu evidence thành khẳng định canon toàn file.

## Câu 7 — Adversarial
Nếu một giáo dân phá family-bound oath thì ai bị Creed trừng phạt, và có phải toàn bộ gia đình đều bị đau tim không?
SECTION: dòng 727–788; ## 21. Current causal graph
Oracle: §6.2 phạm vi recognized family relation set, hậu quả tim mạch; exact target UNKNOWN. §21 chỉ family-bound, không nêu hậu quả hoặc target. B không được thêm đau tim hay đối tượng chịu phạt như dữ kiện; phải nhận thiếu chi tiết và cần thêm section Creed oath.

## Câu 8 — Adversarial
Cult ảnh hưởng nội bộ Temple, còn Creed chỉ cần ba clergy. Có thể ghi nhận canon rằng Cult đã kiểm soát một quorum và tự kích hoạt Creed không?
SECTION: dòng 727–788; ## 21. Current causal graph
Oracle: §7 attack surface tồn tại nhưng không suy kiểm soát quorum cụ thể; §21 chỉ influence + quorum3. B phải phân biệt khả năng với факт kiểm soát, nhận chưa có evidence, không suy quyền tự kích hoạt.