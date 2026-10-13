# Residual payload reconciliation — 2026-10-14

Baseline: local `main` tại `461a011639887c9aef58d1637b074b44706e5c7c`. Phạm vi đúng 66 hồ sơ trong `RESIDUAL_INVENTORY.csv`; không merge/cherry-pick lineage và không push.

Đây chỉ là archive lịch sử/provenance. Không file nào ở đây trở thành canon, control hiện hành, đầu vào build hoặc nguồn fallback. Không chạy các diagnostic script đã lưu. Không suy trạng thái live ChatGPT Project từ snapshot này.

## BuildProbe

58 residual: 57 ARCHIVE, 1 DISCARDABLE; RECOVER/CONTAINED/UNKNOWN đều 0. Giữ các gói theo cấu trúc nguồn, không nhập toàn bộ 156 file.

- CI/Router proposals, GitHub experiment, các snapshot trước mở rộng và báo cáo finalization: giữ quyết định và đường thiết kế lịch sử, không khôi phục control cũ.
- Architecture audit: giữ 10 báo cáo, ba diagnostic script và tám evidence file. Evidence được các báo cáo viện dẫn trực tiếp (baseline hashes, static audit, package verifier, sandbox/closure probes); đây là provenance của kết luận tại thời điểm audit, không phải bằng chứng trạng thái hiện tại.
- Revamp package và node-routing feasibility: đề xuất chưa tự mang authority triển khai. Package manifest đi kèm giữ quan hệ thành phần của gói lịch sử.
- `Source_Archive/.gitattributes`: chỉ có rule whitespace cho tên RP cũ, không có nội dung tác giả hoặc cấu hình cần cho current tooling; DISCARDABLE. Nội dung không được cài lại.

98 file BuildProbe còn lại đã contained trong baseline main theo inventory trước reconciliation, không dựa trên ref khác. Inventory 156 file cũ được sửa để loại bỏ suy luận reachable = contained.

## Publish

Nguồn: publish `33d40279de660b604b7d7360fdbbf9461c259309`, promotion `ded0428`; cùng năm blob residual, khác vai trò vận chuyển commit. Ba file CI v2.7, Router v3.3 và README activation được giữ như snapshot control/triển khai lịch sử.

Workflow promotion trùng byte với bản BuildProbe được lưu tại đây: CONTAINED sau reconciliation, không phải đã contained ở baseline. Không tạo bản archive trùng.

`MANIFEST.md` là metadata snapshot cũ, DISCARDABLE. So với `../buildprobe_root_snapshot/MANIFEST.md`, chỉ thiếu note RP và hai mục nguồn được thêm sau, đồng thời dùng hash output `90` cũ. Không có quyết định tác giả riêng cần giữ; inventory vẫn ghi size, SHA-256 và Git blob của metadata bị loại.

## Legacy OC

Ba hồ sơ lấy từ `safety/local-main-before-aetherfire-integration@4fbdedc054165eaf337110dd5c0cda2a273aa2e2`, giữ nguyên byte tại `legacy_oc/`.

- Jack: hồ sơ OC/RP lịch sử và seed ứng viên; không suy ứng viên đã thành canon.
- Sheeplark: hồ sơ avatar/lịch sử; nguồn tự mô tả vai trò avatar hiện hành ở thời điểm ghi. Không kết luận avatar đã retired hay đang hoạt động ở runtime hiện tại.
- Trần Trúc Nhã: hồ sơ OC/RP lịch sử, kết thúc và ứng viên fork; không đưa trở lại active lore.

Authority của ba bản ghi được phân loại HISTORICAL tại đích lưu này; không đồng nghĩa nhân vật bị abandoned, mọi paracosm dùng chung canon, hoặc FTH sở hữu avatar. Archive chung chỉ là vị trí bảo toàn provenance đã được yêu cầu, không chuyển quyền nguồn. Không sửa hoặc diễn giải lại lore.

## Kiểm chứng và ranh giới

63 file archive vật lý và một ánh xạ duplicate được đối chiếu SHA-256 lẫn Git blob với nguồn. Checker replacement không áp dụng: tác vụ bổ sung provenance, không tạo artifact kế nhiệm hay thay thế nguồn active; dùng đúng shared `Source_Archive` đang có, không tạo archive framework mới.

Không xử lý Academy nested repo, không pruning object và không remote mutation. Cleanup ref chỉ được thực hiện sau kiểm chứng payload, dirty state và process; disposition file không tự cấp quyền xóa ref chứa payload khác.

Gate lịch sử ref (không chỉ tip): publish, promotion và safety OC có 0 blob chưa account sau đối chiếu toàn bộ object reachable riêng, payload inventory và main history; SAFE_TO_DELETE. Publish worktree sạch, không có untracked/ignored file và không phát hiện process đang dùng hai thư mục tạm; không chat khác đang active tại đó. BuildProbe được phép bỏ sau khi xác nhận toàn bộ 156 file vẫn khớp inventory.

`pre-source-architecture-refactor` và branch `safety/pre-source-architecture-refactor`: KEEP. Tag vẫn bảo vệ 26 blob ngoài 66 payload này, gồm biến thể manifest/evidence audit và Source Structure Pack. Không phục hồi hoặc loại chúng trong task hiện tại. Các branch không liên quan giữ nguyên; không tạo ref thay thế.
