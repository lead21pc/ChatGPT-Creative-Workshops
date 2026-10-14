# Source-architecture payload reconciliation — 2026-10-14

Baseline đối chiếu: local main `8436d644a1d5ee5a5981ba80a4cf194b543e3dc8`, sạch, một worktree. Main là baseline kiểm chứng, không tự chứng minh nội dung mới nhất hoặc authority.

`PAYLOAD_INVENTORY.csv` ghi từng content identity: đường dẫn, size, SHA-256, Git blob, ref reachable/tip, first-known commit/parent, commit thay blob, chronology, authority, containment và action. Phạm vi gồm đúng 26 blob đã báo ở vòng trước và hai blob có disposition trước đó để đóng toàn bộ lịch sử safety ref; không phải 28 payload mới.

## Chronology và authority

Safety branch `safety/pre-source-architecture-refactor` và annotated tag `pre-source-architecture-refactor` cùng trỏ commit `dc358c84565960daa3d159fe7b9b4527c58c48b4`, parent `ada784d08ecd15d68908682193aa7eaf74d78e52`. Tag object trước task: `a2b2c386f1386983c37700c0f91da71ac47b4328`.

Common Git ancestor giữa main và safety/current-maintenance là `ce707c198620a823afbca5508e317c14995dd4d7`. Không dùng timestamp/tên branch để suy thứ tự hai lineage. Chuỗi local chứng minh bằng parent links:

`28cdcaa → f4b7780 → c27efd5 → 9f9d1f7 → ada784d → dc358c8 → 34b813c → b5d0855`

Các commit xen giữa được kiểm bằng lịch sử; mũi tên ở chuỗi này biểu thị ancestry, không tuyên bố tất cả đều là direct parent.

| Payload | Chronology | Authority | Containment baseline | Action |
| --- | --- | --- | --- | --- |
| 17 file Source Structure Pack | PARALLEL_DIVERGED | CANDIDATE | NOT-CONTAINED như một bộ tooling | KEEP_CANDIDATE nguyên byte |
| ZIP pack | SAME_STATE_DIFFERENT_PLACEMENT | CANDIDATE về nội dung đóng gói | Expanded pack chưa có ở baseline | DISCARDABLE transport sau khi giữ expanded pack |
| Sáu JSON evidence | SAME_STATE_DIFFERENT_PLACEMENT | HISTORICAL | SEMANTICALLY-CONTAINED | CONTAINED; không nhân bản archive |
| Manifest RP-history `3460991` | PREDECESSOR | SUPERSEDED | SEMANTICALLY-CONTAINED | CONTAINED |
| README default CI `de2f229` | PREDECESSOR | HISTORICAL | NOT-CONTAINED | ARCHIVE nguyên byte |
| Hai blob bổ sung | PREDECESSOR | SUPERSEDED | Đã có disposition tại 8436d64 | Giữ DISCARDABLE; không nhập lại |

Không phát hiện `NEWER_LOCAL + ACCEPTED_NOT_INTEGRATED` trong 26 identity. Đây không phải tuyên bố toàn repository không có accepted work ngoài main.

## Source Structure Pack: giữ candidate, không áp dụng refactor

Pack lần đầu được ghi vào Git tại `dc358c8`, sau header baseline `ada784d`. `34b813c` thêm catalog vào index/PowerShell; `b5d0855` thay archive reconstruction bằng safe Python maintenance. Cả hai descendant giữ nguyên 17 blob pack và ZIP; không có commit phát triển thêm pack trong các refs được chỉ định. Việc giữ nguyên file ở branch không tự là acceptance.

Main có header/owner-boundary, reviewed catalog 17 module, safe maintenance và CI3.3/Router5 được repository ghi là active. Main thiếu bộ template/checklist/worksheet/layout proposal nguyên vẹn. Pack có hướng refactor/layout tùy chọn và mẫu chưa admitted; nó thiếu các admission, tên file, namespace và control mới của main. Hai phía có phạm vi khác nhau: không ghi đè current source bằng pack, cũng không coi catalog hiện hành đã hấp thụ toàn bộ template/migration intent.

Giữ nguyên 17 file tại `Project Feather Core/New Canon and Consideration/AetherFire_Source_Structure_Pack_v1/`. Đây là candidate cấu trúc/non-runtime, không phải current standard đã được chấp nhận hay canon candidate tự động. Nguồn tự ghi `PROPOSAL`, `NON-CANON`, `NON-RUNTIME`, `DO NOT ADMIT`; manifest ghi 16 authored files, không tính chính manifest. Đường dẫn/nội dung AetherFire/Router4 cũ được giữ như bản ghi gốc, không đổi để giả vờ tương thích current namespace. Trước khi dùng hoặc triển khai cần review với current controls; không tự chạy handoff, đổi layout, gán Module ID hay migrate The Kingdom.

Input dự kiến của pack là quyết định tác giả và yêu cầu nguồn/module; output là tài liệu draft/reviewed admission sau quyết định riêng. Retained state hiện tại chỉ gồm proposal/template/sample. Phụ thuộc khai báo là Router4 header contract và reviewed `00`/path updates; failure gate là không admission/di chuyển khi authority hoặc closure chưa rõ. Nó giải quyết nguy cơ gộp taxonomy thành owner, copy nguyên implementation giữa world và di chuyển đường dẫn khi chưa reconcile. Current main giữ nhiều invariant này nhưng chưa chứa bộ authoring tooling; bảo toàn candidate không phải thêm runtime architecture.

ZIP có đúng 17 member file, mọi path/byte trùng expanded tree; không có member riêng. Không giữ ZIP chỉ vì container có unique byte.

## Provenance đã contained và historical README

Sáu JSON tại safety ref và các bản archive main ở `residual_reconciliation_2026-10-14/buildprobe/Source_Archive/AetherFire_Architecture_Audit_2026-09-26/evidence/` có cùng giá trị JSON và toàn bộ text sau chuẩn hóa EOL/EOF; không có khác biệt dữ liệu. Không gọi chúng byte-contained: Git blob và hash raw khác do biểu diễn dòng.

Manifest `3460991` lần đầu tại `2d6652d`, bị thay tại `34b813c`. So với `../buildprobe_root_snapshot/MANIFEST.md`, mọi note/hash row đều giữ nguyên; bản archive main chỉ thêm dòng hash `internal_first_worldbuilding_core_philosophy.md`. Không có quyết định riêng bị thiếu. Snapshot metadata cũ không được tái cài thành manifest active.

README `de2f229` lần đầu tại `28cdcaa`: ghi default CI2.6/Router3.2 và cô lập cặp GitHub-only2.7/3.3. `9f9d1f7` thay default bằng3.0/4.0; main hiện ghi CI3.3/Router5. Giữ snapshot2.6 tại `control_baseline_2026-09-25/README.md`, chỉ cho provenance. Không dùng instruction bên trong để thay current controls hoặc chứng minh live deployment.

## Ref mapping và cleanup gate

| Ref | Nội dung bảo vệ / trạng thái sau account |
| --- | --- |
| Safety branch + tag | Cùng tree/history; toàn bộ payload đã contained, giữ candidate/archive hoặc có disposition. SAFE_TO_DELETE sau commit/hash/process gate |
| architecture-audit | Không còn content identity chưa account trong toàn bộ reachable history; HISTORICAL_REF_OPTIONAL, không xóa trong task này |
| github-only-experiment | Không còn content identity chưa account; HISTORICAL_REF_OPTIONAL, không xóa |
| module-header-migration | Không còn content identity chưa account; HISTORICAL_REF_OPTIONAL, không xóa |
| rp-history | Không còn content identity chưa account; HISTORICAL_REF_OPTIONAL, không xóa |
| current-maintenance | REF_STILL_REQUIRED: còn bốn blob ngoài safety inventory (index, hai manifest version, PowerShell catalog builder); không disposition tự động |
| module-catalog | REF_STILL_REQUIRED: ba trong bốn blob trên; không xóa |
| namespace | REF_STILL_REQUIRED: 53 raw/text-normalized identities ngoài inventory này; khác byte chưa chứng minh unique semantic value hay chronology/authority. Không mở rộng audit hoặc cleanup |

Các con số ngoài safety inventory là upper bound cần đối chiếu semantic, không phải số lỗi hoặc số accepted work bị thiếu. Evidence ref đầy đủ được lưu ngoài tracked artifact của task. Không tạo report toàn repository.

Safety branch/tag chỉ được bỏ khi mọi payload của chúng đã được account, working tree sạch, không worktree/process/chat đang dùng ref và không UNKNOWN chronology/authority trong nhóm. Xóa ref không xóa Git object; không chạy gc/prune. Các ref liên quan giữ nguyên theo bảng, không tạo ref thay thế.

## Kiểm chứng và giới hạn

18 file được bảo toàn mới (17 candidate + một historical README) phải khớp size/SHA-256/Git blob với nguồn. Candidate và archive không nằm trong current file allowlist của `build_consolidation.py`; kiểm package/router và regression tests xác nhận current contract không đổi. Replacement checker không áp dụng: không tạo successor/thay thế nguồn active, chỉ giữ candidate và historical record tại shared archive hiện có.

Không sửa lore, controls active hoặc current package metadata. Không đụng Academy preserved repo, không push/remote mutation và không prune. Acceptance/deployment live chưa được chứng minh; candidate chưa được promote. UNKNOWN trong safety inventory là 0, không suy UNKNOWN ngoài scope thành resolved.
