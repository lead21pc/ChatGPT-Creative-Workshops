---
name: artifact-source-archive
description: Tạo artifact mới hoặc version kế nhiệm từ file cũ; sau khi kiểm chứng bản mới, bắt buộc chuyển mọi predecessor đã bị thay thế vào một source_archive phù hợp và tạo archive nếu chưa có. Dùng checker cấp nhóm để tránh nhiều archive phân mảnh trong cùng artifact root. Nguồn đã lưu chỉ đọc và không được dùng lại nếu người dùng chưa yêu cầu cụ thể. Không kích hoạt cho tác vụ chỉ đọc, audit, version song song vẫn hoạt động hoặc sửa tại chỗ không tạo bản thay thế.
---

# Lưu nguồn cũ sau khi tạo artifact mới

Áp dụng khi tạo artifact mới từ file cũ để đối chiếu, sao chép hoặc thay thế, kể cả khi yêu cầu chỉ nêu version kế nhiệm mà không nhắc lại file tiền nhiệm. Chuyển các predecessor đã bị thay thế vào archive sau khi bản mới hoàn tất và được kiểm chứng; giữ bản mới ở vị trí làm việc. Chỉ dẫn cụ thể của người dùng về nguồn, đích và việc giữ nhiều version cùng hoạt động có ưu tiên cao hơn skill, nhưng phải đổi phân loại sang version song song thay vì tuyên bố replacement đã hoàn tất.

Skill này chỉ sở hữu thao tác lưu file, hash và tính chỉ đọc. Skill chuyên môn xác định nguồn nào được phép chuyển, ý nghĩa provenance/canon và quyết định thay thế; không suy canon từ archive. `project-git-workflow` sở hữu mọi thao tác Git và binding. Audit/planning chỉ đọc không chuyển file dù skill archive được chọn cùng lúc.

## Archive gate bắt buộc

- Khi artifact mới được xác định là version kế nhiệm hoặc bản thay thế đang hoạt động, tác vụ không được báo `COMPLETE` và không được coi promotion đã hoàn tất cho đến khi mọi predecessor thuộc phạm vi thay thế đã được lưu byte-exact vào `source_archive` phù hợp.
- Nếu chưa có archive phù hợp, phải tạo đúng một `source_archive` cho nhóm artifact. Không được bỏ qua chỉ vì yêu cầu không nhắc lại thao tác archive.
- Nếu tạo archive, chuyển file, sửa tham chiếu hoặc kiểm chứng hash bị chặn, giữ an toàn cả bản mới và bản cũ, báo `BLOCKED` cùng trạng thái thực tế, và không tuyên bố replacement đã hoàn tất.
- Nếu predecessor vẫn phải là nguồn hoạt động hoặc hai version phải cùng tồn tại, phân loại là version song song. Không áp archive gate cho đến khi có quyết định replacement rõ ràng.

Skill này chỉ sở hữu thao tác lưu file, hash và tính chỉ đọc. Skill chuyên môn xác định nguồn nào được phép chuyển, ý nghĩa provenance/canon và quyết định thay thế; không suy canon từ archive. `project-git-workflow` sở hữu mọi thao tác Git và binding. Audit/planning chỉ đọc không chuyển file dù skill archive được chọn cùng lúc.

## Xác định nguồn và đích

- Ghi rõ ánh xạ predecessor → artifact mới, thư mục gốc của tác vụ, artifact root và phạm vi bản mới thay thế. Không gom các file khác chỉ vì cùng thư mục hoặc có tên gần giống.
- Chỉ chuyển bản tiền nhiệm hoặc file tham chiếu cũ thuộc phạm vi lưu trữ đã yêu cầu. Không chuyển template, thư viện, asset hoặc nguồn dùng chung còn là phụ thuộc hoạt động của bản mới hay tác vụ khác. Nếu chưa rõ việc chuyển có làm mất nguồn đang cần hay không, giữ file và hỏi đúng phần chưa rõ.
- Xác định semantic membership trước khi xét đường dẫn: chỉ các predecessor đã được xác nhận thuộc cùng phạm vi replacement mới tạo thành một nhóm. Cùng thư mục không tự chứng minh cùng nhóm; khác thư mục con không tự chứng minh khác nhóm.
- Với mỗi nhóm, chạy `python -B scripts/check_archive_group.py --task-root <task-root> --artifact-root <artifact-root> --source <predecessor> [--source <predecessor> ...]` trước khi tạo archive hoặc chuyển file. Checker chỉ đọc và chỉ xác minh layout/phạm vi; nó không quyết định semantic membership.
- Tìm tên `source_archive` không phân biệt hoa/thường. `Source_Archive`, `SOURCE_ARCHIVE` và `source_archive` là cùng một tên; giữ nguyên cách viết của thư mục đang có.
- Nếu checker trả `PASS_SHARED`, dùng archive chung đã có tại artifact root. Nếu trả `PASS_CREATE_ONE`, tạo đúng đích `<artifact-root>/source_archive` mà checker nêu; không tạo archive cạnh từng nguồn.
- Nếu checker trả `BLOCKED`, dừng archive cho nhóm. Không tự chọn giữa nhiều candidate, không tạo thêm archive để né archive lồng nhau hoặc tên bị file chiếm, và không quét ngoài task root.
- Nếu nguồn đã nằm trong archive, giữ nguyên nó. Quyền đọc nguồn archive không tự cho phép sửa hoặc chuyển nó ra thành nguồn hoạt động.

## Tạo, kiểm chứng và chuyển

1. Đọc các nguồn đang được phép dùng; xác nhận replacement hay version song song; lập ánh xạ predecessor → artifact mới và các nhóm artifact root.
2. Chạy checker cho từng nhóm và lưu kết quả đích duy nhất. Không tạo bản mới nếu quan hệ replacement hoặc đích archive còn mơ hồ đến mức có thể chuyển sai nguồn.
3. Tạo bản mới ở đường dẫn khác, giữ nguyên file nguồn trong lúc tạo. Tuân thủ quy tắc Git của tác vụ khi có sửa repository.
4. Kiểm chứng artifact đã ghi ra đĩa: nội dung theo yêu cầu, định dạng mở được, các kiểm tra liên quan đạt, các liên kết hoặc phụ thuộc còn hoạt động. Nếu bản mới lỗi hoặc chưa hoàn tất, giữ nguyên vị trí nguồn cũ.
5. Sau khi kiểm chứng đạt, tự thực hiện lưu trữ trong phạm vi đã xác định; không hỏi lại quyền chuyển mà người dùng đã cấp qua quy tắc này. Kiểm tra tham chiếu hoạt động tới nguồn cũ trước khi chuyển; nếu việc sửa tham chiếu sẽ vượt phạm vi tác vụ, giữ nguồn và báo phần cần quyết định.
6. Giữ byte-exact nội dung nguồn cũ. Ghi SHA-256 trước chuyển và kiểm SHA-256 ở đích sau chuyển. Kiểm tra đường dẫn tuyệt đối đã resolve nằm trong nguồn/đích được phép; không đi qua symlink hoặc junction sang thư mục ngoài phạm vi.
7. Không ghi đè file archive trùng tên. Nếu tên đích đã tồn tại, tạo tên không trùng bằng hậu tố thời gian và bộ đếm khi cần; giữ phần mở rộng. Không tự xóa hay gộp bản đã có, kể cả hash giống nhau.
8. Chỉ bỏ bản cũ khỏi vị trí làm việc sau khi bản archive được xác nhận đúng hash. Dùng thao tác file với đường dẫn literal; nếu thao tác thất bại, giữ các bản còn lại và báo trạng thái thực tế. Không xóa thư mục nguồn hoặc file không thuộc tác vụ.
9. Kiểm lại artifact mới, tham chiếu chịu ảnh hưởng và archive group: mọi predecessor đã thay thế phải vắng khỏi vùng hoạt động, có bản đúng hash trong cùng đích archive đã chọn, và không phát sinh archive thứ hai cho nhóm. Báo đường dẫn bản mới, nguồn đã chuyển, đích archive, kết quả kiểm chứng và phần còn bị chặn nếu có.

## Archive chỉ đọc và không hoạt động

- Đây là ranh giới hành vi, không phải yêu cầu đổi ACL hay thuộc tính read-only của hệ điều hành. Cho phép thêm nguồn cũ mới vào archive theo quy trình trên; không sửa, chuẩn hóa, đổi tên hoặc xóa các file đã lưu trước đó nếu chưa có yêu cầu rõ.
- Không dùng nội dung archive làm nguồn mặc định, fallback, tiền đề, mốc hiện hành, đầu vào build hoặc căn cứ khôi phục nội dung đã thay thế. Không tự đọc lại nó ở lượt sau; việc bản mới thiếu dữ kiện không mở quyền dùng archive.
- Chỉ đọc hoặc sử dụng nguồn archive khi người dùng chỉ định rõ file, nhóm nguồn hoặc phạm vi lịch sử cần đối chiếu/khôi phục. Yêu cầu chung như “tiếp tục”, “kiểm tra lại” hoặc “tạo bản mới” không tự cấp quyền dùng archive.
- Yêu cầu đối chiếu lịch sử chỉ cấp quyền trong tác vụ đó; không tái kích hoạt bản cũ. Chỉ khôi phục nó thành nguồn hoạt động khi người dùng yêu cầu rõ việc khôi phục và phạm vi thay thế.
- Khi cần dữ kiện chỉ có trong archive nhưng chưa có quyền sử dụng, nêu dữ kiện còn thiếu và hỏi quyền cho đúng nguồn; không âm thầm dùng trí nhớ của nguồn cũ để vượt ranh giới này.
