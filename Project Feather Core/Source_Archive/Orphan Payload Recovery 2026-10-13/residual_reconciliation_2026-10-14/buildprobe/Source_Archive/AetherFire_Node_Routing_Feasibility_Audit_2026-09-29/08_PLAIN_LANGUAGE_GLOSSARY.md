# 08 — Từ điển vận hành

> Chỉ giải các thuật ngữ dùng trong proposal. Những primitive mới đều gắn với failure cụ thể; chưa mục nào được kích hoạt.

## `FULL_FILE` — đọc trọn file

- **Nó là gì?** Mở và đọc toàn bộ Markdown được route.
- **Giải lỗi nào?** Tránh mất ngoại lệ/priority nằm ngoài đoạn được chọn.
- **Vì sao cần bây giờ?** Đây là baseline an toàn hiện hành và đường dự phòng của mọi pilot.
- **Bỏ đi thì sao?** Lỗi index/retrieval có thể biến thành kết luận thiếu premise.
- **Người dùng có phải maintain tay?** Không; chỉ cần biết file nào đang ở mode này.
- **Codex generate/validate được không?** Có thể kiểm file tồn tại và coverage đọc local; không chứng minh runtime tự động.
- **Project runtime có phụ thuộc không?** Có, vì đường đọc trọn file là đường an toàn của contract.

## Mandatory runtime header — phần mở đầu bắt buộc

- **Nó là gì?** Vài dòng ở đầu file nói file này thuộc miền nào, ai có thẩm quyền và không được hiểu sai status/priority nào.
- **Giải lỗi nào?** Ngăn node giữa file bị đọc thiếu ranh giới authority hoặc supersession.
- **Vì sao cần bây giờ?** Node read sẽ không tự mang theo toàn bộ văn cảnh của file.
- **Bỏ đi thì sao?** Một câu đúng cục bộ có thể bị dùng sai miền hoặc nâng lịch sử thành canon.
- **Người dùng có phải maintain tay?** Không nên; Codex/builder có thể đề xuất, nhưng người biết lore phải duyệt ý nghĩa khi nội dung đổi.
- **Codex generate/validate được không?** Có thể sinh/kiểm cấu trúc; không tự chứng minh bản tóm tắt semantic đủ.
- **Project runtime có phụ thuộc không?** Chỉ với file đã bật `NODE_OR_FULL`; file full không cần primitive mới.

## Local routing index — bảng mục lục cục bộ

- **Nó là gì?** Bảng ngay trong file chỉ ID node, phạm vi, dependency quyết định và issue hook.
- **Giải lỗi nào?** Tránh đoán đoạn nào trả lời một câu hỏi hẹp.
- **Vì sao cần bây giờ?** Nếu muốn đọc ít, cần bản đồ cục bộ nhìn được bằng mắt và có thể kiểm bằng máy.
- **Bỏ đi thì sao?** Router chỉ còn tìm từ khóa/heading tùy ý; dùng full-file an toàn hơn.
- **Người dùng có phải maintain tay?** Mục tiêu là không; Codex/builder sinh đề xuất và kiểm, người review boundary.
- **Codex generate/validate được không?** Có thể; semantic mapping vẫn cần review.
- **Project runtime có phụ thuộc không?** Có với `NODE_OR_FULL`; không phải file registry mới.

## Semantic node — nhóm ý nghĩa

- **Nó là gì?** Một cụm nội dung đủ giữ các điều kiện cho một loại câu hỏi; không phải mỗi tiêu đề một node.
- **Giải lỗi nào?** Cho phép đọc ít hơn mà vẫn giữ nguyên causal/authority context.
- **Vì sao cần bây giờ?** Các file như `30` dài, nhưng nhiều tác vụ chỉ chạm một phạm vi hẹp.
- **Bỏ đi thì sao?** Vẫn dùng full-file; mất cơ hội giảm đọc thừa, không mất canon.
- **Người dùng có phải maintain tay?** Không cần đếm/sửa ID thủ công; phải duyệt khi cách nhóm ảnh hưởng meaning.
- **Codex generate/validate được không?** Có thể đề xuất và kiểm marker/span; không tự chứng minh node đủ premise.
- **Project runtime có phụ thuộc không?** Chỉ khi node mode được kích hoạt và Project đọc được node thật.

## `REQUIRES` — cần đọc thêm mới kết luận được

- **Nó là gì?** Một cạnh nói rằng node A thiếu node B thì **không đủ premise** cho class kết luận được nêu.
- **Giải lỗi nào?** Tránh dùng một node đúng nhưng cắt mất điều kiện quyết định ở nơi khác.
- **Vì sao cần bây giờ?** Node hóa tạo rủi ro này; full-file hiện không cần khai báo edge.
- **Bỏ đi thì sao?** Hoặc phải full-file, hoặc dễ trả lời thiếu điều kiện.
- **Người dùng có phải maintain tay?** Không nên; Codex đề xuất edge kèm lý do, reviewer duyệt khi nội dung đổi.
- **Codex generate/validate được không?** Kiểm target tồn tại được; không tự suy edge từ mention/similarity.
- **Project runtime có phụ thuộc không?** Có nếu mode node dùng edge đó; edge lỗi → full-file.

## `NODE_OR_FULL` — thử node, không chắc thì đọc trọn

- **Nó là gì?** Mode cho file pilot: chỉ dùng node closure khi đủ điều kiện, còn lại full current file.
- **Giải lỗi nào?** Ngăn lỗi node routing thành lỗi toàn Project.
- **Vì sao cần bây giờ?** Đây là cách thêm tối ưu hóa mà giữ baseline an toàn.
- **Bỏ đi thì sao?** Chỉ còn full-file hoặc node-only rủi ro; full-file vẫn hoàn toàn hoạt động.
- **Người dùng có phải maintain tay?** Không; mode nên hiện rõ và ít thay đổi.
- **Codex generate/validate được không?** Kiểm quy tắc fallback local được; cần test Project để xác minh hành vi thật.
- **Project runtime có phụ thuộc không?** Chỉ với file đã kích hoạt mode này; Project không cần parser/service ngoài Markdown.

## `RECORD_OR_FULL` — hồ sơ cụ thể hoặc trọn file

- **Nó là gì?** Biến thể dành riêng cho `91`: đọc addendum/priority và record quyết định, hoặc cả file khi rộng/không rõ.
- **Giải lỗi nào?** Giảm đọc các conflict record không liên quan mà không bỏ override mới.
- **Vì sao cần bây giờ?** Chưa cần ở phase đầu; cấu trúc AF-CX cho thấy có thể thử sau.
- **Bỏ đi thì sao?** `91` tiếp tục full-file, an toàn hơn nhưng tốn đọc hơn.
- **Người dùng có phải maintain tay?** Không; reviewer chỉ duyệt mapping/addendum khi pilot.
- **Codex generate/validate được không?** Parse ID và kiểm anchor được; priority quyết định vẫn cần semantic review.
- **Project runtime có phụ thuộc không?** Chỉ nếu mode này được kích hoạt ở phase sau.

## `REVIEW_REQUIRED` — cần người xem lại

- **Nó là gì?** Nhãn trong quy trình local khi chưa chứng minh node boundary hoặc `REQUIRES`.
- **Giải lỗi nào?** Chặn việc phỏng đoán dependency rồi đưa vào Project.
- **Vì sao cần bây giờ?** Mentions và semantic dependency rất dễ bị nhầm trong corpus nhiều miền.
- **Bỏ đi thì sao?** Dễ có edge giả hoặc tình trạng “có vẻ ổn” không ai chịu trách nhiệm.
- **Người dùng có phải maintain tay?** Không thường xuyên; chỉ các quyết định lore/authority còn mơ hồ mới cần người dùng.
- **Codex generate/validate được không?** Có thể phát hiện ứng viên và lập report; không tự biến nó thành `REQUIRES`.
- **Project runtime có phụ thuộc không?** Không. Nó là cờ của audit local; runtime dùng full-file cho vùng chưa review.

## Source generation — một lứa source nhất quán

- **Nó là gì?** Bộ `00–92` được sinh/cài từ cùng một đầu vào ở một mốc xác định.
- **Giải lỗi nào?** Tránh index, file canon và Router thuộc những mốc khác nhau nhưng bị coi như đồng bộ.
- **Vì sao cần bây giờ?** Shadow comparison chỉ có nghĩa nếu hai arm dùng cùng nguồn.
- **Bỏ đi thì sao?** Sai lệch version có thể bị nhầm là tác động của node routing.
- **Người dùng có phải maintain tay?** Chỉ cần xác nhận bộ nào được cài/rollback; Codex có thể ghi inventory.
- **Codex generate/validate được không?** Có thể ghi hash/size và so source snapshot.
- **Project runtime có phụ thuộc không?** Không cần đọc một registry generation mới; consistency vẫn cần cho phép thử và activation.

## Closure — tập đoạn phải đọc đủ

- **Nó là gì?** Header + index + node hỏi tới + mọi node `REQUIRES` đã duyệt.
- **Giải lỗi nào?** Tránh dùng riêng đoạn đích khi điều kiện quyết định nằm ở đoạn khác.
- **Vì sao cần bây giờ?** Đó là nghĩa cụ thể của một node read hợp lệ.
- **Bỏ đi thì sao?** Node mode trở thành excerpt mode và vi phạm source gate.
- **Người dùng có phải maintain tay?** Không; chỉ cần reviewer duyệt các quan hệ quyết định.
- **Codex generate/validate được không?** Có thể tính tập ID và phát hiện target thiếu; semantic đủ hay không vẫn phải review.
- **Project runtime có phụ thuộc không?** Có, nếu bật node mode; phải đọc thật toàn closure hoặc fallback full-file.
