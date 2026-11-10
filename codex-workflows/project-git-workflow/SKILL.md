---
name: project-git-workflow
description: Điều phối Git theo một shared local working state cho mỗi repository. Dùng working tree hiện tại làm nguồn thật, giới hạn thao tác bằng READ/WRITE scope, tự stage và commit local đúng file thuộc task sau khi kiểm chứng; branch/worktree chỉ là fallback khi có nhu cầu cô lập cụ thể. Push cần quyền xuất bản rõ đích và phạm vi commit; không suy quyền từ trạng thái Git.
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

`PUSH REQUIRES EXPLICIT ACTION-SCOPED AUTHORIZATION.`
`REPOSITORY STATE RESOLUTION != USER AUTHORIZATION`; `COMMIT != PUSH`; `PUSH != GENERIC PERMISSION TO REMOTE EGRESS`.

Skill này sở hữu quy trình kiểm quyền push chung; helper hiện chỉ làm việc local, không thực thi push. Quyền sửa/stage/commit local không tự cấp quyền xuất bản.

Trước mỗi push:

1. Kiểm tra working tree/HEAD và trạng thái remote liên quan. Xác định remote cùng URL push thực tế, source/local ref và tip, destination remote ref, cùng toàn bộ commit sẽ được xuất bản so với trạng thái đích. Tính cả commit tổ tiên chưa có ở đích, không chỉ tip hoặc file của task. Chưa đủ dữ kiện để xác định đích/payload thì chưa push.
2. Đối chiếu hành động đã xác định với quyền người dùng hiện hành: đúng repository/remote đích, source ref, destination ref, tập commit hoặc phạm vi task được cho phép, và loại thao tác. Git state đã biết không phải quyền của người dùng; không diễn giải riêng chữ `push` thành quyền `main → origin/main` cho payload tự suy ra.
3. Nếu quyền chưa bao phủ rõ đích và payload, **không phát lệnh push**, kể cả dry-run. Đưa một câu xin quyền cụ thể rồi chờ xác nhận, ví dụ: “Bạn cho phép push các commit `A`, `B` hiện có trên local `main` lên `origin/main` (`<URL đã kiểm tra>`) chứ?” Dùng SHA thực đã kiểm tra, không placeholder. Nếu payload được nêu theo tập “toàn bộ commit local hiện tại”, giữ rõ mốc/tip và tập commit tại thời điểm xin quyền. Không hỏi lại remote/branch như dữ kiện chưa biết; câu hỏi xin quyền phải nêu chính hành động đã xác định, không chỉ “confirm push”.
4. Khi quyền đã đủ rõ, dùng ngay trong đúng phạm vi, **không xin xác nhận lần hai**. Ví dụ “push các commit local hiện tại trên main lên origin/main” bao phủ tập hiện có lúc cấp quyền. “Sửa task này, commit rồi push thay đổi của task này từ main lên origin/main” có thể bao phủ commit của task tạo sau đó; không hỏi lại chỉ vì SHA chưa tồn tại lúc cấp quyền. Vẫn đối chiếu payload cuối: commit ngoài task hoặc tổ tiên chưa được cho phép không tự được bao phủ.
5. Ngay trước khi thực hiện, kiểm lại source tip, destination và payload với quyền đã nhận. Nếu đích/phạm vi thay đổi, chỉ phần vượt quyền cần xin lại; không tự thêm commit phát sinh sau một quyền đã chốt tập hiện tại. Phát lệnh push trực tiếp thể hiện đúng remote và ref/payload đã được cho phép; không để source ref dịch chuyển làm publish thêm commit. Kiểm kết quả và SHA remote sau push; attempt không phải success.

Quyền cho commit A không bao phủ B mới phát sinh, ref/remote khác, force-push, tag, release, PR hay sửa remote metadata. Wording cấp phạm vi task tương lai rõ ràng là ngoại lệ có chủ đích cho commit của đúng task, không là quyền thường trực. Quyền của task cũ không truyền sang task mới; xác nhận “có” chỉ có nghĩa trong phạm vi hành động cụ thể đang được hỏi.

Tôn trọng auto-review: nếu bị từ chối, báo hành động/lý do và xin phần quyền còn thiếu. Không dùng wrapper, alias, Python/subprocess, mã hóa lệnh hoặc đổi transport để né kiểm duyệt. Helper không thay được user authorization; không thêm permission registry hoặc persistent approval system.

Các ca regression và cách đánh giá nằm ở [references/push-authorization-cases.md](references/push-authorization-cases.md). Chúng là đặc tả hành vi, không phải bằng chứng đã chạy model/auto-review.

## Legacy state

Các registry/binding cũ không còn là authority và helper mới bỏ qua chúng. Không xóa chúng tự động; việc kiểm kê hoặc dọn dẹp là task riêng.
