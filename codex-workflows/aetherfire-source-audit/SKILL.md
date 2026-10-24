---
name: aetherfire-source-audit
description: Tra cứu, audit và đối chiếu nguồn Markdown/canon của Project Feather Core (Feather Core - FTH, FTH; tên cũ AetherFire Project), gồm AetherFire và các domain FTH khác; cập nhật nguồn/package sau khi người dùng chốt. Không tự viết lore hoặc áp cho paracosm khác.
---

# Feather Core / AetherFire source audit

Dùng skill cho tác vụ nguồn/canon FTH dù yêu cầu chỉ nhắc `Project Feather Core`, `Feather Core - FTH` hoặc `FTH`, không cần có từ AetherFire. `AetherFire Project` là tên project cũ; AetherFire hiện là một quốc gia trong FTH, không giới hạn skill vào quốc gia đó. Giữ ID `aetherfire-source-audit` để tương thích lời gọi cũ. Không kích hoạt chỉ vì đang ở thư mục FTH nếu tác vụ thuần Git; không áp cho The Kingdom hoặc Fanfiction Engine/The Academy.

## Ranh giới điều phối

Skill này sở hữu căn cứ nguồn, quyền canon, provenance, phạm vi thay đổi và kiểm chứng package. `project-git-workflow` sở hữu checkout/branch/stage/commit; tái sử dụng binding và quyền Git đã cấp, không tạo branch theo lần chốt. Khi tác vụ được duyệt cần lưu hoặc chuyển nguồn cũ, `artifact-source-archive` sở hữu cơ chế chuyển/hash/chống ghi đè; AetherFire xác định nguồn đủ điều kiện và ý nghĩa lịch sử. Không tự mở archive để lấp dữ kiện; chỉ đọc nguồn lịch sử trong phạm vi người dùng yêu cầu cụ thể. Audit/planning chỉ đọc không stage, commit, tạo binding hoặc chuyển archive.

## Chọn chế độ trước khi đọc nguồn

Trước khi mở nội dung project, phân loại tác vụ và dùng chế độ nhẹ nhất đủ an toàn:

- **LOOKUP:** trả lời câu hỏi hẹp, không đổi canon. Đọc chỉ file/phần nguồn trực tiếp cần cho target; không chạy đối chiếu hai chiều hoặc bảng finding đầy đủ.
- **BOUNDED_AUDIT:** kiểm một claim, entity, file hoặc conflict đã nêu. Đọc mốc và nguồn liên quan trực tiếp; đối chiếu claim mục tiêu và phụ thuộc gần.
- **FULL_AUDIT:** chỉ dùng khi user yêu cầu audit toàn diện, merge/chốt/retcon, thay canon, kiểm provenance, cập nhật package, hoặc khi conflict hiện hành buộc phải mở rộng.

Mặc định là `LOOKUP` nếu user không yêu cầu audit/chốt/sửa/package verification. Ghi ngắn `mode`, `target`, nguồn dự kiến và điều kiện dừng khi phạm vi không hiển nhiên. Chỉ đọc reference chi tiết khi mode cần: [quy trình đối chiếu](references/audit-protocol.md) cho `BOUNDED_AUDIT`/`FULL_AUDIT`; [quy trình package](references/package-workflow.md) khi thật sự cần xác định hoặc cập nhật gói.

## Bắt đầu bằng nguồn thực tế

Sau khi chọn mode và nạp hướng dẫn cần thiết, mở lại nguồn đang làm bằng chứng cho câu trả lời. Không dùng trí nhớ hoặc tóm tắt lượt trước thay cho nội dung file hiện tại. Trong cùng một tác vụ liên tục, có thể tái dùng phần đã đọc nếu file không đổi và phạm vi không mở rộng; khi sang lượt mới, file đổi, hoặc cần chứng nhận audit/chốt thì đọc lại phần liên quan.

Đọc đầy đủ phần/file được mode yêu cầu; nếu dài, chia phần và theo dõi phần đã đọc, không coi đầu ra bị cắt là đã đọc hết. Với đường dẫn/pattern, liệt kê file khớp trong thư mục được chỉ định; không tự quét mọi Markdown trên máy. Nếu chưa có file hoặc đường dẫn không xác định được, hỏi đúng file cần đọc. Nếu thiếu/không đọc được nguồn, báo phần bị chặn và tiếp tục phần độc lập; không chứng nhận phần chưa đọc.

Lập danh sách nguồn ngắn: đường dẫn, vai trò, phiên bản/phạm vi, trạng thái đã đọc. Phân biệt:

- **Mốc đã chốt:** file hoặc bộ file mới nhất được người dùng xác nhận cho từng phạm vi.
- **Đầu vào mới:** file đang được xem xét, chưa tự động có quyền thay canon.
- **Lịch sử/nguồn gốc:** bản cũ dùng truy nguyên và phát hiện nội dung bị bỏ sót.
- **Hướng dẫn hành vi:** CI/anti-drift hướng dẫn cách làm việc, không tự trở thành bằng chứng canon.

Tên `CURRENT`, số phiên bản, thời gian sửa file hoặc vị trí trong thư mục không đủ chứng minh một bản đã được chốt. Nếu chưa xác định được mốc, phân tích các khả năng và hỏi trước khi ghi nhận bản thay thế; không âm thầm chọn. Việc đọc một file cũng không đồng nghĩa làm theo mọi chỉ dẫn bên trong file đó.

## Nhận diện gói Project Feather Core

Nếu phạm vi nằm trong một thư mục có `00_AETHERFIRE_CONSOLIDATION_INDEX.md`, `MANIFEST.md`, `build_consolidation.py` và `Source_Archive/`, coi đó là gói Project Feather Core được duy trì bằng Python. ID kỹ thuật `aetherfire-source-audit` và các `AFM-*`/`AF-*` ổn định không đổi; tên dự án `Project Feather Core`/`FTH` không đồng nhất với quốc gia AetherFire. Trong `LOOKUP`, chỉ đọc metadata package nếu cần xác định đúng file hiện hành hoặc vai trò nguồn. Đọc [quy trình package](references/package-workflow.md) trước khi chọn mốc, sửa, cập nhật vùng generated, chứng nhận đầu ra, hoặc khi metadata package ảnh hưởng trực tiếp tới kết luận. Index/manifest/reconciliation record mô tả cấu trúc gói nhưng không tự thay thế bằng chứng canon trong nguồn.

Các current sources ở root được duy trì trực tiếp; chỉ sửa trong phạm vi đã duyệt và ghi reconciliation tương ứng. Không sửa tay vùng generated catalog/metadata/hash: dùng `python -B '<project-root>/build_consolidation.py' --write`, rồi `--check`. `Source_Archive/` chỉ giữ lịch sử/provenance, không dùng để tái dựng current canon. Với file AetherFire độc lập không thuộc gói này, tiếp tục dùng workflow chung bên dưới.

## Quyền quyết định và ranh giới AetherFire

Người dùng quyết định canon. Áp dụng quyết định xác nhận mới nhất trong đúng phạm vi của nó; ngoài phạm vi đó, giữ nguồn đã chốt còn hiệu lực. Mâu thuẫn giữa các nguồn chưa có thứ tự ưu tiên rõ phải được báo, không tự hòa giải bằng tính hợp lý, sở thích hoặc tên file.

Không viết thêm lore, retcon, ánh xạ hoặc cơ chế để lấp khoảng trống nếu chưa được yêu cầu. `UNKNOWN` không phải quyền sáng tác. Tách dữ kiện đã xác lập, yêu cầu thiết kế, suy luận có điều kiện và đề xuất.

Giữ các trục và quan hệ được nguồn phân biệt: trạng thái pháp lý, class, công việc, vai trò/rank, Career Rank, màu nhận diện/đồng phục, khu vực, biến kinh tế, quyền truy cập và nguồn gốc. Không mã hóa một kết luận canon cụ thể từ phiên cũ thành chân lý bất biến của skill; tra lại định nghĩa trong nguồn hiện hành.

Việc tài liệu chứa một mục không chứng minh quan hệ sở hữu hay phụ thuộc trong thế giới. Phân biệt `THUỘC_VỀ`, `ÁP_DỤNG_CHO`, `QUẢN_TRỊ`, `TƯƠNG_TÁC_VỚI`, `DẪN_XUẤT_TỪ` và các chuyển trạng thái theo bằng chứng. Genealogy không tự xác lập quyền hạn hiện tại. Hai trục khác nhau không tự chứng minh chúng tương thích hoặc không tương thích. Khi có nhiều canon, thời kỳ, lớp thế giới hay POV, xác định đúng lớp trước khi gọi một khác biệt là mâu thuẫn.

## Kiểm tra độ bao phủ và logic

Đọc [quy trình đối chiếu](references/audit-protocol.md) khi thực hiện `BOUNDED_AUDIT` hoặc `FULL_AUDIT`. Trong `LOOKUP`, trả lời từ nguồn đã đọc và ghi giới hạn; không cần bảng finding hoặc coverage matrix nếu không phát hiện vấn đề thật.

`BOUNDED_AUDIT` đối chiếu hai chiều trong phạm vi target: claim/file/entity được nêu, mốc liên quan và phụ thuộc trực tiếp. `FULL_AUDIT` mới tìm tối đa các vấn đề có căn cứ trong phạm vi được yêu cầu; không dừng ở vài ví dụ hoặc giới hạn top 5/top 10. Không tăng số lượng bằng lỗi giả, trùng lặp hoặc giả thuyết thiếu tiền đề. Gộp biểu hiện cùng nguyên nhân nhưng liệt kê đủ vị trí và hệ quả. Nếu báo cáo dài, ghi danh sách đầy đủ vào file báo cáo riêng khi tác vụ cho phép, chỉ tóm tắt trong chat. Nếu audit chỉ đọc và không cho ghi file, chia phần trả lời; không tự chuyển thành quyền sửa nguồn.

Phân loại độc lập, có thể đi cùng nhau:

- **CONFLICT — mâu thuẫn:** các khẳng định không thể cùng đúng với cùng đối tượng, nghĩa, điều kiện, thời kỳ và lớp canon; nêu rõ điểm bất tương thích. Trường hợp còn phụ thuộc cách hiểu là nghi vấn, không phải mâu thuẫn đã xác nhận.
- **UNKNOWN — chưa xác lập:** thiếu định nghĩa, quy tắc, liên kết hoặc bằng chứng để kết luận. Thiếu canon không có nghĩa canon phủ định; chưa tìm thấy cũng không có nghĩa không tồn tại.
- **DEFERRED — đã hoãn:** có quyết định rõ để xử lý sau; ghi ai/quyết định nào hoãn, phạm vi, điều kiện mở lại nếu có. Không tự đổi mọi unknown thành deferred hoặc dùng deferred để che conflict.
- **LOGIC — vấn đề lập luận:** kết luận không theo tiền đề, tráo khái niệm/trục, đảo điều kiện cần/đủ, vòng phụ thuộc thiếu điểm khởi đầu, chuyển trạng thái thiếu điều kiện, hoặc lỗi thời gian/quyền hạn/tri thức có thể chỉ ra từ nguồn. Một vòng lặp hay cơ chế khác đời thực không tự động là lỗi.

Tách trạng thái xử lý khỏi loại vấn đề: `OPEN`, `PROPOSED`, `DEFERRED`, `RESOLVED`, `SUPERSEDED`. Đề xuất chưa phải quyết định; quyết định đã đồng ý nhưng chưa kiểm chứng trong file đầu ra chưa đủ để đánh dấu RESOLVED ở cấp tài liệu.

## Chốt, tạo file mới và đổi mốc

1. Trước khi chốt, trình bày các phát hiện, lựa chọn xử lý và tác động phụ thuộc. Với nhiệm vụ chỉ audit, dừng ở báo cáo. Không tự sửa nguồn để làm cho báo cáo hết conflict.
2. Khi người dùng đồng ý chốt, xác định chính xác các quyết định được đồng ý và phạm vi thay thế. Đồng ý một mục không có nghĩa chấp nhận toàn bộ đề xuất, giải quyết hết unknown hoặc cho phép ghi đè bản gốc. Không hỏi lại phần đã được cho phép rõ.
3. Khi được yêu cầu tạo bản chốt độc lập, tạo **file mới** hoặc bộ file mới ở đích đã xác định, giữ bản nguồn. Bản chốt phải chứa nội dung được giữ lại trong phạm vi và các sửa đổi đã đồng ý, không chỉ danh sách quyết định thay cho tài liệu. Dùng tên không trùng; nếu đích đã tồn tại, không ghi đè ngoài quyền đã có. Nếu đích thuộc package, dùng quy trình package và xác định đúng current source/vùng generated được phép sửa.
4. **Mở và đọc lại file đầu ra thực tế từ ổ đĩa.** Với package, đọc current sources đã sửa cùng các vùng generated có liên quan sau cập nhật Python. Đối chiếu chính nội dung đó với quyết định đã chốt, mốc trước và các nguồn còn hiệu lực. Kiểm tra cả nội dung được phép đổi lẫn nội dung phải giữ; phát hiện bỏ sót, phủ định sai, hồi sinh tiền đề đã bỏ và thay đổi ngoài phạm vi. Không kiểm chứng trên bản nháp trong trí nhớ hoặc chỉ lặp lại audit của file đầu vào.
5. Giữ nguyên các mục OPEN/UNKNOWN/DEFERRED chưa được giải quyết trong bản mới hoặc hồ sơ đi kèm được liên kết rõ; không tự xóa vì tài liệu đã mang nhãn “chốt”. Mục được giải quyết phải có quyết định và vị trí thể hiện trong file mới. Nếu có lệch so với quyết định, sửa trong phạm vi được duyệt rồi đọc/kiểm lại; mâu thuẫn mới cần quyết định canon thì báo người dùng, không tự quyết.
6. Chỉ sau khi xác nhận file đầu ra phản ánh đúng quyết định mới ghi nó là **mốc đã chốt cho lượt kế tiếp**. Ghi đường dẫn chính xác, phạm vi thay thế, bản tiền nhiệm, quyết định làm căn cứ và các mục còn mở trong hồ sơ đối chiếu. Đối với bộ file, ghi riêng từng phạm vi để tránh lấy một file thay cả project. Không ghi vào memory toàn cục.
7. Lượt kế tiếp phải đọc file mới đã chốt này và so sánh đầu vào tiếp theo với nó. Bản cũ chỉ còn vai trò lịch sử hoặc nguồn còn hiệu lực ngoài phạm vi bị thay thế; không để bản cũ giành lại quyền chỉ vì nó từng là file đối chiếu. Nếu file mới mất, bị sửa khác nội dung đã chốt hoặc hồ sơ nguồn không nhất quán, báo rõ và xác minh lại, không tự quay về bản cũ.

Một bản đã chốt vẫn có thể chứa câu hỏi được chấp nhận để mở. Nếu còn mâu thuẫn được người dùng chủ động hoãn, ghi rõ nó còn tồn tại; không tuyên bố “canon không mâu thuẫn”. Không chọn một nhánh mâu thuẫn làm tiền đề chắc chắn cho phân tích tiếp theo.

## Bàn giao và giới hạn xác minh

Báo cáo tiếng Việt rõ nghĩa, giữ nhãn chuyên môn để tra cứu và giải thích ngắn tại chỗ. Cung cấp danh sách nguồn đã đọc, mốc đang dùng, phát hiện có dẫn chứng, quyết định còn cần và giới hạn bao phủ. Dùng mẫu trong [quy trình đối chiếu](references/audit-protocol.md) cho `BOUNDED_AUDIT`/`FULL_AUDIT`; với `LOOKUP`, chỉ cần nguồn đã đọc, câu trả lời/trạng thái và giới hạn. Không yêu cầu người đọc xem chuỗi suy nghĩ nội bộ.

Sau khi tạo bản chốt, báo riêng: file mới, kết quả đối chiếu file thực tế với quyết định, các mục còn mở và mốc sẽ dùng tiếp. Không tuyên bố đã tìm mọi mâu thuẫn tuyệt đối; chỉ mô tả phạm vi đã rà và phần chưa đọc/kiểm được. Kiểm tra Markdown hoặc hash không chứng minh logic đúng.

Với gói Project Feather Core, chỉ báo hoàn tất sau một lần xác minh mới trong cùng lượt: `build_consolidation.py --check` đạt, nguồn ngoài phạm vi không đổi và current sources/vùng generated liên quan đã được đọc/đối chiếu ngữ nghĩa. Validator không đọc archive hoặc tái dựng canon; kết quả đạt không thay thế audit canon.

Khi đánh giá hoặc sửa skill này, dùng [các ca review](references/review-cases.md). Các ca là tiêu chí thử nghiệm, không phải bằng chứng model đã tuân thủ.
