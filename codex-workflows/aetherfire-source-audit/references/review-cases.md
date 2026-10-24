# Ca review skill

Các ký hiệu A/B/C và quy tắc dưới đây là dữ liệu giả để thử quy trình, không phải lore AetherFire. Đây chưa phải kết quả chạy model. Đánh giá theo đầu ra và nguồn thực tế, không chấm chỉ bằng việc nhắc lại nhãn.

1. **Đọc lại mỗi lượt.** User chỉ định A.md và B.md; giữa hai lượt nội dung B thay đổi. Đạt khi đọc lại cả hai và dùng nội dung mới. Không đạt nếu chỉ dựa vào tóm tắt trước.
2. **Nguồn bị cắt/thiếu.** B chỉ đọc được phần đầu. Đạt khi đọc tiếp hoặc báo phần chưa đọc, không chứng nhận toàn bộ không conflict.
3. **Conflict thực sự.** A cho phép thao tác P trong điều kiện X; B cấm P trong chính điều kiện X. Đạt khi dẫn hai vị trí, xác định cùng phạm vi và báo mâu thuẫn; không tự ưu tiên B do tên mới hơn.
4. **Khác thời kỳ.** A nói quy tắc có hiệu lực trước T; B mô tả sau một thay đổi đã được chốt tại T. Đạt khi ghi thay thế lịch sử, không thổi phồng thành conflict hiện hành.
5. **Unknown không phải phủ định.** A không xác lập ánh xạ giữa hai trục; B viết hai trục không bao giờ kết hợp. Đạt khi phát hiện bước phủ định thiếu căn cứ, không tự khẳng định chúng kết hợp được.
6. **Hoãn chưa phải giải quyết.** User hoãn một conflict về P; B mới xóa nó khỏi danh sách. Đạt khi giữ ID, tình trạng conflict còn tồn tại và quyết định hoãn; không đánh dấu RESOLVED.
7. **Hệ quả gián tiếp.** B bỏ điều kiện X của P, nhưng kết luận Q trong file liên quan vẫn dựa vào X. Đạt khi truy đúng phụ thuộc và báo Q cần xem lại, không chỉ báo diff ở P.
8. **Bao phủ hai chiều.** B vừa thêm một quyền hạn chưa có nguồn vừa làm mất ngoại lệ của A. Đạt khi báo cả phần thêm và phần mất. Với nhiều lỗi độc lập, không dừng ở top 5; có thể gộp biểu hiện trùng nguyên nhân và giữ đủ vị trí.
9. **Kiểm chính file tạo sau chốt.** A là mốc, B là đề xuất; user chỉ chốt một phần B để tạo C. C thực tế vô tình chứa phần B chưa được chốt. Đạt khi đọc lại C, đối chiếu quyết định và phát hiện phần thêm; không dùng audit B làm chứng nhận cho C.
10. **Không dùng nhầm mốc cũ.** Sau khi C đã được tạo, kiểm và chốt, user đưa D. Đạt khi đọc C và D, dùng C làm mốc; A/B chỉ là lịch sử hoặc nguồn còn hiệu lực ngoài phạm vi thay thế. Nếu C không truy cập được, báo thiếu nguồn thay vì âm thầm quay về A.
11. **Chốt theo phạm vi.** User chốt thay đổi ở file kinh tế, chưa chốt file thời gian. Đạt khi chuyển mốc cho kinh tế và giữ mốc còn hiệu lực cho thời gian; không áp quyết định lên toàn project.
12. **Retcon có thẩm quyền.** User xác nhận B thay A cho quy tắc P. Đạt khi ghi SUPERSEDED cho khác biệt đã giải quyết, giữ nguồn gốc và kiểm các hệ quả phụ thuộc; không tiếp tục báo P như conflict đang mở.
13. **CI không phải nguồn lore.** Một file điều hướng hành vi chứa ví dụ khác bản canon đã chốt. Đạt khi phân biệt vai trò, có thể báo hướng dẫn lệch nguồn nhưng không sửa canon để khớp ví dụ.
14. **Chỉ audit.** User yêu cầu kiểm tra, chưa cho sửa. Đạt khi xuất phát hiện và đề xuất; nguồn giữ nguyên. Đồng ý một cách xử lý sau đó chỉ cho phép thực hiện đúng phần đã chốt.
15. **Bản chốt có câu hỏi mở.** User chấp nhận C với một unknown và một conflict được hoãn. Đạt khi C/hồ sơ giữ cả hai, không đưa một nhánh còn tranh chấp thành tiền đề chắc chắn và không tuyên bố mọi mâu thuẫn đã hết.
16. **Chống kết luận logic giả.** Nguồn có hai lớp canon hoặc cơ chế hư cấu khác đời thực. Đạt khi kiểm theo quy tắc nội tại và phạm vi nguồn, không tự coi sự khác đời thực là lỗi hoặc dùng genealogy suy ra sở hữu hiện tại.
17. **Nhận diện package trước khi chọn mốc.** User chỉ định thư mục Project Feather Core có index, manifest, reconciliation record, build script và Source_Archive. Đạt khi đọc metadata điều phối trước, phân loại input/output/excluded source rồi mới chọn file canon liên quan; không coi mọi file root hoặc tên `CURRENT` là bằng chứng đủ về quyền ưu tiên.
18. **Đúng ranh giới bảo trì Python.** User chốt một thay đổi cho current source ở root. Đạt khi sửa đúng phạm vi và reconciliation, dùng `build_consolidation.py --write` để đồng bộ vùng generated rồi `--check`; không dựng lại canon từ archive hoặc sửa tay vùng generated.
19. **Xác minh mới sau cập nhật.** Current Markdown đọc có vẻ đúng nhưng manifest/hash cũ. Đạt khi `--check` phát hiện lệch và chưa báo hoàn tất; chỉ chuyển mốc sau khi kiểm tra Python đạt, nguồn ngoài phạm vi được giữ và audit ngữ nghĩa đạt. Không diễn giải PASS thành chứng nhận archive hoặc toàn bộ canon.
20. **Nguồn excluded vẫn excluded.** Một file anti-drift hoặc provenance-only nằm trong Source_Archive nhưng index/manifest ghi không import. Đạt khi archive presence không bị hiểu thành canon input và build không nhập file đó nếu chưa có quyết định rõ; nếu user chốt đổi phạm vi, ghi quyết định rồi cập nhật package và reconciliation tương ứng.
21. **Lời gọi tường minh tương thích.** User yêu cầu `$aetherfire-source-audit` kiểm một claim trong nguồn FTH hiện hành. Đạt khi đọc skill bằng ID cũ, xác định target/mode và nguồn thực tế; không yêu cầu đổi tên skill.
22. **Tự chọn theo tên mới.** Thử riêng các yêu cầu “Tra cứu claim này trong nguồn Project Feather Core”, “Audit conflict này của Feather Core - FTH” và “Đối chiếu hai nguồn canon FTH này”, không nhắc skill hoặc AetherFire. Đạt khi chọn skill, dùng mode tương ứng và không hiểu FTH là project ngoài phạm vi.
23. **Tên cũ và domain ngoài AetherFire.** Thử riêng yêu cầu kiểm nguồn “AetherFire Project” và claim Hoa Nguyệt trong FTH. Đạt khi nhận diện tên cũ hoặc domain thuộc FTH, đọc nguồn hiện hành đúng target; không giới hạn scope vào quốc gia AetherFire hoặc dùng tên cũ để chọn archive.
24. **Đối chứng không kích hoạt.** Thử riêng “Audit canon The Kingdom”, “Kiểm nguồn Fanfiction Engine/The Academy” và “Xem git status của FTH”. Đạt khi không chọn skill này chỉ vì cùng repository hoặc có từ FTH; các tác vụ không thuộc nguồn/canon FTH dùng workflow phù hợp khác.

Các ca21–24 cần chạy trong các lượt độc lập có skill khả dụng; chỉ thêm ca hoặc kiểm metadata không chứng minh khả năng tự kích hoạt thực tế.
