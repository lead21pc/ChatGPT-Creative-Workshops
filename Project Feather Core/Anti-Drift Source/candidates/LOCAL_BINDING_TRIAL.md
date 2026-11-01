# Thử nghiệm local binding của Router 5.0

**CANDIDATE / TRIAL — NOT ACTIVE — NOT LIVE DEPLOYMENT.**

Artifact: `FTH_Anti_Drift_Source_Router_local_binding_trial.yaml`.
Baseline trực tiếp: Router 5.0. Độc lập với candidate FTHX 5.1, không kế thừa
FTHX và không tham gia active numeric discovery. Active stack vẫn là CI 3.4,
Router 5.0, Authoring Pipeline 1.1. Chưa có promotion hoặc cài đặt live.

## Phạm vi và thay đổi

Trial giữ nguyên schema và mọi section của 5.0 ngoài metadata deployment và
hai policy `access/discovery`. Metadata đánh dấu candidate có tên mô tả, trỏ
baseline về active 5.0/CI 3.4. Discovery giữ nguyên toàn bộ nội dung gốc rồi
bổ sung root-relative retrieval. Access chọn `LOCAL_CURRENT_SOURCE` duy nhất
cho `00/92`, `91` khi cần và 17 admitted AFM current lore modules.

Deployment cung cấp **root tuyệt đối chính xác**, thiết bị nếu công cụ cần,
quyết định có phạm vi chọn package đó làm current và quyền đọc. Không đi tìm
root bằng scan, tên folder hoặc GitHub. Tool permission, header và manifest
không tự cấp authority. Không coi một folder hợp lệ bất kỳ là current.

`00/92` phải được đọc FULL_FILE cùng generation trước khi dùng catalog trong
`00`. Đường dẫn catalog tương đối với đúng root; đối chiếu requested ID với
header thật, role, scope, authority boundaries và load contract. Catalog/header
không thay admission hoặc quyết định owner. Các gate semantic hiện có tiếp tục
quyết định phần nào đủ bằng chứng để thực thi.

Giữ controls, Router/Pipeline và RP ở binding hiện hành của chúng. Đây là phân
chia tài nguyên; lỗi local không được chuyển sang binding khác. Giữ Library
baseline riêng để so sánh/rollback có chủ đích.

## Đọc đủ file và tính nhất quán

Thành công một call không phải FULL_FILE. Đối với công cụ phân trang, ghi nhận
range bắt đầu, số dòng thực nhận, tổng số dòng/end-of-file và mọi phần còn lại.
Chỉ công nhận khi các range phủ đủ file, không mất/cắt nội dung và không trộn
các bản khác nhau. `91` hiện dài hơn 1.000 dòng nên phải thử nhiều range.
Nếu công cụ không cung cấp đủ bằng chứng, chặn phần phụ thuộc theo failure
contract hiện có; không dùng snippet, Memory hoặc bản Library thay thế.

Dùng `build_consolidation.py --check` tại root được chọn trước phiên thử để kiểm
consistency bằng manifest hiện có; không biến hash thành authority hoặc yêu cầu
hash ở mọi runtime read. Phép kiểm này cũng không phát hiện một snapshot cũ hoàn
toàn nhất quán: deployment phải chọn đúng package current. Tránh sửa package
trong lúc thử; nếu thay đổi, dừng phần phụ thuộc và xác minh/đọc lại generation.

## Kiểm tra local

Từ thư mục Project Feather Core:

```powershell
python -B build_consolidation.py --check
python -B build_consolidation.py --check-router
python -B -c "from pathlib import Path; from tools.router_candidate import check_local_binding_trial; print(len(check_local_binding_trial(Path.cwd())))"
python -B -m unittest discover -s tests
```

`tests/test_local_binding_trial.py` chứa helper retrieval nhỏ chỉ dùng trong
tests: root được chọn tường minh, bootstrap, catalog, header, đọc theo range và
preflight consistency. Nó không phải runtime adapter, resolver service, hoặc
bộ thực thi Router. Nó kiểm complete byte coverage với transport local của
tests, kiểm metadata thay đổi trong lúc đọc, nhưng không chứng minh bridge cloud.
Một lần preflight không bảo đảm package sẽ không đổi sau đó.

Năm probe tại `tests/control-regressions/router-local-binding-probes.json` vẫn
**DRAFT / NOT_RUN**, `model_executed: false`. Tests chỉ kiểm đầu vào retrieval,
protected contracts và dependency expansion sau khi điều kiện đã được phán định.
Chưa có bằng chứng model chọn đúng owner, reconciliation, applicability hoặc
giữ UNKNOWN trong live Project.

## Smoke live và rollback

1. Mở phiên thử riêng trong FTH Project. Cung cấp trial FULL_FILE và cho phép
   **reference override riêng trong phiên** từ exact Router 5.0 sang trial này;
   giữ mọi invariant CI 3.4. Không chỉ đọc 5.0 rồi gọi đó là thử trial.
2. Chỉ định thiết bị/root tuyệt đối và chọn rõ package tại root đó làm current
   cho phạm vi lore/bootstrap/reconciliation. Giữ controls ở binding đã xác lập;
   không sửa Project instructions hoặc active references trong repository.
3. Yêu cầu actual bridge đọc trọn `00 + 92`, resolve AFM-015 qua catalog rồi đọc
   trọn và kiểm header; tiếp tục đúng module/authority gates. Khi ca cần `91`,
   đọc đủ các range đến cuối file. Ghi nhận actual reads, không chỉ lời tự xác nhận.
4. Chạy năm probe, so sánh một phiên Library baseline riêng có cùng generation
   và controls. Thử lỗi bằng root sai hoặc công cụ chỉ trả phần đầu file trong
   cấu hình phiên thử; không sửa/xóa nguồn thật. Kỳ vọng chặn phần phụ thuộc,
   không đọc Library/Project Sources hoặc scan để cứu binding lỗi.
5. Ghi kết quả bridge và live riêng. Dừng trial bằng bỏ override và chọn lại
   baseline 5.0/Library trong phiên mới. Không cần thay active stack hoặc archive.

Thành công local/bridge không tự promote trial. Kiểm chứng live chỉ được ghi sau
khi thực sự chạy trong FTH cloud Project với đúng override, root và nguồn.
