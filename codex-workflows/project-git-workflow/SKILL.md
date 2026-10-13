---
name: project-git-workflow
description: Điều phối Git theo một shared local working state cho mỗi repository. Dùng working tree hiện tại làm nguồn thật, giới hạn thao tác bằng READ/WRITE scope, tự stage và commit local đúng file thuộc task sau khi kiểm chứng; branch/worktree chỉ là fallback khi có nhu cầu cô lập cụ thể. Push luôn cần yêu cầu riêng.
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

Không push, tag, release, sửa remote metadata hoặc mở PR nếu người dùng chưa yêu cầu rõ. Khi được yêu cầu push, xác nhận remote, destination branch và commit payload trước khi chạy.

## Legacy state

Các registry/binding cũ không còn là authority và helper mới bỏ qua chúng. Không xóa chúng tự động; việc kiểm kê hoặc dọn dẹp là task riêng.
