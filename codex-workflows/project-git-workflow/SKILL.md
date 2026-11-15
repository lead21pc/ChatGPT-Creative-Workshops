---
name: project-git-workflow
description: Điều phối Git trên working tree hiện tại, giới hạn READ/WRITE, stage và commit local đúng phạm vi đã kiểm chứng; branch/worktree chỉ là fallback. Kiểm quyền và payload trước push; quyền thường trực chỉ áp cho đích GitHub và nhánh đã được người dùng chỉ định.
---

# Project Git Workflow

## Invariant

`ONE REPOSITORY = ONE SHARED LOCAL WORKING STATE`

Chat hoặc project không sở hữu checkout hay branch. Scope chỉ quyết định nơi được đọc và nơi được ghi.

- `READ`: file hoặc thư mục cần đọc để hiểu dependency, kể cả dirty working-tree state.
- `WRITE`: file hoặc thư mục task được phép sửa, stage và commit.
- Working tree hiện tại là nguồn thật mặc định. Không thay dependency dirty bằng bản ở `HEAD` hay bằng một worktree mới.

## Bắt đầu task

1. Tìm repository gần nhất chứa target. Không `git init` bên trong một repository cha.
2. Ghi baseline: repo root, branch hiện tại, `HEAD`, `git status --short`, staged paths.
3. Khai báo `READ` dependencies và `WRITE` scopes nhỏ nhất đủ dùng.
4. Phân loại dirty state có sẵn. Không sửa, stage hoặc commit thay đổi ngoài `WRITE` scope.
5. Nếu ownership chồng lấn hoặc task cần thay đổi ngoài scope, dừng và xin chỉ dẫn.

Dùng helper chỉ đọc:

```powershell
python scripts/git_workflow.py inspect `
  --path <target> `
  --write-scope <path> `
  --read-path <dependency>
```

`inspect` không tạo registry, binding, branch hoặc worktree.

## Sửa và kiểm chứng

- Đọc trực tiếp file trong working tree hiện tại, kể cả file dirty hoặc untracked trong `READ` scope.
- Chỉ ghi trong `WRITE` scope.
- Chạy build/test/behavioral verification phù hợp trước commit.
- Build pass là điều kiện cần, không tự chứng minh hành vi runtime.

## Stage và checkpoint commit local

Sau khi milestone được kiểm chứng, stage và commit local tự động đúng các file task-owned được liệt kê rõ ràng:

```powershell
python scripts/git_workflow.py commit `
  --path <target> `
  --write-scope <path> `
  --file <task-file> `
  --message <message>
```

Helper phải:

1. từ chối file ngoài `WRITE` scope;
2. từ chối file task đã staged trước khi helper chạy vì ownership không rõ;
3. dùng pathspec literal cho từng file, không dùng `git add -A` hoặc broad staging;
4. bảo toàn staged baseline không thuộc task;
5. chạy `git diff --cached --check`, xem stat và full staged diff của đúng file task;
6. commit bằng explicit path list;
7. xác nhận commit không chứa file ngoài danh sách và staged baseline cũ vẫn còn.

`COMMIT != PUSH`. Helper không có đường dẫn thực thi push.

## Branch và worktree chỉ là fallback

Không tạo branch/worktree chỉ vì chat mới, task mới, version mới hoặc working tree đang dirty.

Chỉ dùng fallback khi có nhu cầu cô lập cụ thể, ví dụ:

- hai thay đổi cần sửa đồng thời cùng file với trạng thái không tương thích;
- thử nghiệm phá vỡ cần sandbox riêng;
- người dùng yêu cầu rõ branch/worktree riêng.

Trước khi tạo fallback, ghi rõ lý do, ref nguồn và cách hợp nhất. Sau khi hợp nhất/đưa commit cần thiết vào shared state, dọn tài nguyên tạm theo yêu cầu riêng. Không tự dọn legacy branches, worktrees hoặc binding trong task khác.

Helper chỉ tạo isolation khi caller gọi tường minh và cung cấp lý do:

```powershell
# Mức 2: đổi current checkout sang branch tạm từ ref đã xác minh
python scripts/git_workflow.py isolate --path <target> --kind branch `
  --branch <temporary-branch> --ref <verified-ref> --reason <concrete-conflict>

# Mức 3: chỉ khi cần hai working state đồng thời
python scripts/git_workflow.py isolate --path <target> --kind worktree `
  --branch <temporary-branch> --ref <verified-ref> --worktree <new-path> `
  --reason <why-two-states-are-required>
```

Lệnh `isolate` không được gọi như bước chuẩn bị mặc định. Branch fallback yêu cầu checkout sạch; worktree path phải chưa tồn tại.

## Push

`REPOSITORY STATE RESOLUTION != USER AUTHORIZATION`; `COMMIT != PUSH`.

Skill này sở hữu quy trình kiểm quyền push; helper chỉ thao tác local, không thực thi push. Với repository thông thường, push cần quyền rõ cho hành động cụ thể: repository/remote đích, source/destination ref, payload và loại thao tác. Quyền sửa/stage/commit hoặc trạng thái Git không thay được quyền xuất bản.

### Ngoại lệ do người dùng cấp: repository chính thức

Người dùng đã cấp quyền thường trực cho push fast-forward thông thường từ local `refs/heads/main` lên `origin` tại `refs/heads/main`, chỉ cho GitHub `lead21pc/ChatGPT-Creative-Workshops`, ID `1361687313`, nhánh mặc định `main`. Quyền này bao phủ các commit local đã kiểm chứng trên `main`, kể cả commit từ task sau hoặc từ nhiều task; không khóa theo SHA/task. Khi đủ điều kiện, được push sau kiểm chứng mà không xin lại quyền từng task hay từng lần push. Chỉ dẫn mới hơn, giới hạn local-only hoặc yêu cầu chỉ đọc vẫn được tôn trọng.

Trước khi áp ngoại lệ:

1. Kiểm đúng repository local, source branch/tip và URL fetch/push **thực tế** của `origin` (kể cả override/rewrite). Chỉ áp nếu đích fetch và push đều resolve về repository GitHub chính thức, không có thêm đích push. Dùng metadata từ GitHub API của chính repository mà URL hiệu lực trỏ tới để đối chiếu đồng thời `full_name`, số `id` và `default_branch`; tên `origin`, URL giống nhau, local project trust hoặc API lookup một repo khác không đủ. Không xác minh được thì không áp ngoại lệ; dùng gate quyền thông thường.
2. Làm mới và xác nhận tip thực tế của remote `main`. Nếu remote có commit riêng hoặc không chứng minh được fast-forward, dừng; không tự merge/rebase/rewrite để push. Kiểm toàn bộ outgoing commits, kể cả tổ tiên chưa xuất bản: chỉ push khi toàn bộ payload đã kiểm chứng và thuộc quyền xuất bản. Giữ nguyên các thay đổi local không liên quan; không stage chúng để push.
3. Kiểm lại đích, tip và payload ngay trước khi chạy. Push trực tiếp đúng một refspec đã kiểm chứng (có thể ghim SHA đã xác nhận từ local `main` làm nguồn), không force, không gửi tag theo, rồi xác minh SHA remote. Nếu ref/payload thay đổi, kiểm lại trước khi thực hiện; không tự đưa commit chưa kiểm chứng lên remote.

Ngoại lệ không bao phủ force push (kể cả `--force-with-lease`), xóa remote ref, nhánh/remote/repository khác, tag, release, PR, thay metadata/URL hay rewrite history. Nó không cấp quyền bỏ qua sandbox, GitHub branch protection hoặc auto-review.

### Gate thông thường và kiểm chứng

- Kiểm working tree/HEAD, URL push thực tế, source/local ref và tip, destination ref, cũng như **toàn bộ** outgoing commits. Không suy từ riêng chữ `push`, default branch, upstream hay tip.
- Nếu quyền chưa bao phủ rõ hành động đã xác định, không phát lệnh push, kể cả dry-run. Xin quyền một lần, nêu đích/URL và SHA thực. Quyền cho tập commit hiện tại không bao phủ commit phát sinh sau đó; quyền cho task cụ thể có thể bao phủ commit tạo sau trong task nhưng không bao phủ tổ tiên ngoài task. Quyền của task cũ không tự truyền sang task mới. Khi quyền đã đủ, không xin lần hai.
- Kiểm lại tip, đích và payload ngay trước khi phát lệnh trực tiếp; xác minh SHA remote sau push. Attempt không phải success.
- Quyền thường trực ở workflow không phải allowlist của nền tảng. Nếu sandbox hoặc auto-review từ chối, báo hành động và lý do theo runtime; không dùng wrapper, alias, subprocess, mã hóa lệnh hoặc đổi transport để né review; không dựng registry quyền giả.

Xem [các ca kiểm quyền push](references/push-authorization-cases.md). Đây là đặc tả hành vi, không phải kết quả chạy model/auto-review.

## Legacy state

Các registry/binding cũ không còn là authority và helper mới bỏ qua chúng. Không xóa chúng tự động; việc kiểm kê hoặc dọn dẹp là task riêng.
