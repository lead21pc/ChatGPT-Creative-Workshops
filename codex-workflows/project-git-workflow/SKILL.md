---
name: project-git-workflow
description: Điều phối checkout, branch, stage và commit nội bộ cho chat trong project Git. Gắn chat với một checkout và branch ổn định, tái sử dụng qua milestone, kiểm đúng đích trước thao tác ghi, bảo toàn staged baseline. Audit chỉ đọc không sửa Git; không tự push hoặc tạo branch thử nghiệm cho mỗi tác vụ.
---

# Một chat, một checkout và branch làm việc

Skill này sở hữu quyết định Git. Skill chuyên môn xác định phạm vi nội dung và kiểm chứng; không tự tạo branch, chọn checkout hoặc đặt chính sách commit riêng. Chỉ dẫn rõ của người dùng có ưu tiên cao hơn. Quyền stage/commit đã cấp tiếp tục có hiệu lực trong đúng phạm vi; không hỏi lại chỉ vì chuyển skill.

Khi tích hợp vào stack có AGENTS toàn cục, [patch chính sách Git](references/global-agents-git-policy.patch) ghi đúng hai thay đổi đã duyệt: tái sử dụng binding và quyền nhận file mới. Kiểm patch bằng git apply --check --unidiff-zero trước khi áp trong thư mục chứa AGENTS tương ứng. Chỉ áp khi có quyền chỉnh file đó; không thay các quy tắc khác.

## Gắn và tái sử dụng

- Xác định repository/project từ yêu cầu và đường dẫn thật. Tên chat chỉ là gợi ý. Dùng thread ID có sẵn hoặc khóa chat ổn định được xác định một lần; không tạo khóa theo ngày/milestone.
- Gắn chat, project scope, checkout, branch, HEAD và staged baseline bằng `scripts/git_workflow.py`. Trạng thái local nằm trong Git common directory, không vào canon hoặc memory toàn cục.
- Chat triển khai phải có checkout và branch riêng. Tái sử dụng binding hiện có qua mọi milestone. Lần đầu, ưu tiên checkout/branch riêng phù hợp đã xác minh và chưa thuộc chat khác; nếu chưa có thì dùng `prepare` tạo worktree và branch `codex/<chu-de>-<id-chat>`. Việc cách ly lần đầu thuộc phạm vi triển khai đã được cho phép; không hỏi lại chỉ vì checkout nguồn đã thuộc chat khác.
- `prepare` nhận checkout nguồn ở repository root và project bên trong nó. Nếu chat đã có binding trong cùng repository, helper trả binding hiện có dạng JSON; dùng đúng `checkout/project/branch` trả về cho mọi thao tác tiếp theo. Nếu chưa có, phải chỉ định đường dẫn worktree mới bên ngoài checkout nguồn, branch mới và `--ref` rõ ràng. Chọn ref theo baseline tác vụ đã xác minh; không mặc định lấy remote main hoặc HEAD chỉ vì đang đứng ở đó.
- Worktree mới chỉ chứa nội dung đã commit tại ref đó. Nếu tác vụ cần thay đổi chưa commit ở checkout nguồn, kiểm quyền sở hữu và chuyển riêng phần thuộc tác vụ, rồi kiểm chứng tại worktree đích; không tự chuyển toàn bộ dirty diff. Nếu ownership chồng lấn chưa rõ, chỉ hỏi đúng phần thiếu.
- Không sinh branch mới vì phiên bản, checkpoint, test hoặc dirty worktree. Khi cần cách ly thử nghiệm, dùng bản sao tạm/detached checkout; công việc chính quay về binding. Nếu branch đã được checkout ở nơi khác, tái sử dụng đúng checkout đó; không force checkout cùng branch ở worktree khác.
- Hai chat song song không sở hữu cùng checkout hoặc branch, kể cả khi project scope khác nhau. Khi gặp checkout đã có chủ, tra binding của chính chat rồi chuẩn bị worktree riêng nếu chưa có; không chỉ báo lỗi và dừng. Không tự chuyển binding sang chat/project khác, dùng chung khóa chat hoặc bỏ qua cổng kiểm tra. Nếu chủ đề đổi hẳn, báo phạm vi không khớp trước thao tác ghi.

## Cổng trước thao tác ghi

Chạy check trước sửa, stage và commit. Lệch checkout/project/branch/HEAD thì dừng ghi và xác minh; không tự switch trong checkout dirty, stash, reset hoặc commit để giải quyết lệch. Nếu HEAD đổi hợp lệ ngoài tác vụ, đọc diff/history trước khi dùng bind --refresh-head trên cùng checkout/branch; tùy chọn này không đổi branch.

```powershell
python -B '<skill-root>/scripts/git_workflow.py' prepare --checkout '<source-repository-root>' --project '<source-project>' --chat-key '<stable-chat-key>' --worktree '<new-worktree-path>' --branch 'codex/<chu-de>-<id-chat>' --ref '<verified-ref>'
# Tra lại binding ở milestone sau; không tạo checkout/branch mới:
python -B '<skill-root>/scripts/git_workflow.py' prepare --checkout '<source-repository-root>' --project '<source-project>' --chat-key '<stable-chat-key>'
# Hoặc gắn checkout riêng đã được xác minh:
python -B '<skill-root>/scripts/git_workflow.py' bind --checkout '<checkout>' --project '<project>' --branch '<bound-branch>' --chat-key '<stable-chat-key>'
python -B '<skill-root>/scripts/git_workflow.py' check --checkout '<checkout>' --chat-key '<stable-chat-key>'
```

Audit/planning chỉ đọc chỉ kiểm Git; không bind, refresh, stage, commit, archive hoặc tạo checkout. Nếu chưa có binding, kiểm trạng thái thật và báo chưa gắn; không tạo trạng thái trong audit.

## Kết thúc chat và giải phóng binding

Khi người dùng yêu cầu kết thúc quyền sở hữu, dùng `release` với đúng khóa chat và checkout đã gắn. Helper kiểm checkout, scope, branch, HEAD và yêu cầu Git status sạch trên toàn checkout (tracked, staged, untracked không bị ignore). Binding được chuyển vào `codex-chat-bindings/released/`; branch, checkout và commits được giữ nguyên. Không tự giải phóng chỉ vì chat im lặng, đã archive trên giao diện hoặc binding có vẻ cũ. Worktree biến mất, HEAD lệch hoặc còn thay đổi thì dừng để kiểm chứng, không tự xóa registry hay reset công việc.

```powershell
python -B '<skill-root>/scripts/git_workflow.py' release --checkout '<bound-checkout>' --chat-key '<stable-chat-key>'
```

Các thao tác ghi qua helper khóa registry trong Git common directory để hai chat không đồng thời nhận quyền sở hữu. Nếu registry bận, thử lại sau khi thao tác kia kết thúc; nếu tiến trình bị ngắt để lại `.lock`, xác minh không còn helper đang chạy trước khi xử lý khóa. Không tự xóa khóa hoặc chiếm binding đang hoạt động. Trường `shared_checkout_authorized` trong bản ghi cũ không bỏ qua kiểm tra độc quyền; giữ bản ghi cũ và tách chat triển khai mới sang worktree riêng.

## Nhận file và commit

1. Ghi baseline. Theo quyền tự theo dõi đã cấp, liệt kê file mới trong project bằng git ls-files --others --exclude-standard -z; xử lý NUL đúng và stage từng path literal sau check. Tuân gitignore, chính sách generated output và ranh giới repo lồng nhau/symlink. Stage archive không biến nguồn thành canon.
2. File mới có sẵn trong project có thể được nhận theo quyền này; tracked changes có sẵn ngoài tác vụ giữ riêng. Nếu ownership/hunk chồng lấn không rõ, giữ nguyên và hỏi đúng phần thiếu. Không git add -A toàn repo dirty.
3. Chỉ commit sau khi hoàn tất và kiểm chứng liên quan đạt. Skill chuyên môn cung cấp tập file/hunk và bằng chứng; Git workflow không thay audit nội dung.
4. Kiểm git diff --cached --check, stat và toàn diff được phép. Xác nhận staged snapshot khớp nội dung đã kiểm chứng. Với CRLF phải giữ nguyên, dùng cấu hình whitespace theo lệnh phù hợp.
5. Dùng commit của helper, chỉ định từng file repo-relative. Helper chặn branch/HEAD lệch, file ngoài scope, symlink, conflict, staged baseline chồng lấn và worktree/index mismatch. Commit --only giữ staged files ngoài tập; rename phải có cả path cũ/mới. Helper không tự stage hoặc kiểm logic.
6. Sau commit, helper cập nhật HEAD/baseline. Kiểm status, nội dung commit và staged changes có sẵn. Nếu Git/hook/identity lỗi, giữ trạng thái và báo lỗi; không đổi cấu hình hoặc bỏ hook để vượt kiểm tra.

```powershell
python -B '<skill-root>/scripts/git_workflow.py' commit --checkout '<checkout>' --chat-key '<stable-chat-key>' --file '<relative-path>' --message '<task outcome>'
```

Nhiều milestone tuần tự dùng nhiều commit trên cùng branch tạm cho đến khi kết thúc đợt công việc. Xuất bản và cleanup tuân theo quy trình dưới đây; không tự push từ quyền commit nội bộ.

## Xuất bản main và kết thúc branch tạm

- Branch làm việc là tạm thời trong một đợt công việc; tái sử dụng binding trong đợt đó, không tạo branch theo mỗi milestone. Ưu tiên detached checkout khi chỉ cần tích hợp/xuất bản.
- Khi người dùng yêu cầu push/xuất bản mà không chỉ định đích khác, đích bắt buộc là remote `main`. Không push branch task lên remote rồi coi tác vụ đã hoàn tất. Chỉ publish branch riêng khi người dùng chỉ định rõ.
- Fetch trước khi tích hợp. Liệt kê toàn bộ commit chưa có trên remote; chỉ đưa thay đổi đã được duyệt vào checkout sạch từ remote main. Nếu lịch sử có commit ngoài phạm vi, chuyển riêng commit/hunk đã duyệt, kiểm chứng lại theo layout main. Không push toàn bộ lịch sử branch chỉ để tiện.
- Push main không force; nếu main tiến lên, fetch, tích hợp và kiểm chứng lại. Xác nhận SHA main bằng ls-remote sau push.
- Sau khi xác minh main, phải kiểm tra và dọn branch/worktree tạm do tác vụ tạo: worktree sạch, không còn công việc đang chạy, và mọi thay đổi cần giữ đã có trên main. Với cherry-pick, xác minh patch/nội dung tương đương; không dùng tên branch hoặc trạng thái clean làm bằng chứng đã merge.
- Xóa remote branch tạm của tác vụ khi nó đã được tích hợp; gỡ worktree tạm sạch bằng git worktree remove không force. Chỉ xóa local branch bằng git branch -d khi Git xác nhận an toàn. Nếu branch còn lịch sử chưa được chứng minh đã tích hợp, giữ lại và báo rõ; không dùng -D để vượt cổng.
- Yêu cầu xuất bản và dọn branch tạm cấp quyền kết thúc binding của chính đợt đó sau khi xác minh main. Dùng `release` với đúng chat key và checkout sạch trước khi gỡ worktree; giữ metadata trong `released/`. Không release binding của chat khác hoặc tác vụ còn chạy. Binding không phải lý do giữ remote branch tạm vĩnh viễn.
- Quyền push có từ yêu cầu xuất bản trong đúng phạm vi; quy tắc này không tự cho phép push sau một yêu cầu chỉ sửa, audit hoặc commit. Báo SHA main, kết quả cleanup và mọi tài nguyên còn giữ cùng lý do.

Helper là cổng khi được gọi, không phải hook cưỡng chế mọi lệnh shell của ứng dụng. Kiểm sát thao tác; nếu nhiều chat cùng sửa checkout, dừng và tách quyền sở hữu trước khi tiếp tục.
