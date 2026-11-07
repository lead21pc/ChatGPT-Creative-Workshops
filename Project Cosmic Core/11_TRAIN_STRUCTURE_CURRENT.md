# C2 — Cấu trúc đoàn tàu

> Module ID: `C2M-011`
> Runtime role: `CURRENT_SOURCE`
> Domain / Scope: Đoàn tàu, loại toa và định tuyến cấu trúc vật lý.
> Authority boundary: Giữ cấu trúc tàu; không tự thiết lập sơ đồ tổ chức, quyền chỉ huy hoặc ý thức của tàu.
> Cross-domain owner boundary: Rongo ở `C2M-010`; composition của Team 25 ở `C2M-020`; world ở `C2M-110`.
> Load mode: `FULL_FILE`

## Cấu trúc tối thiểu

Identity tra nguồn: `TRAIN`. Đoàn tàu xuyên các world, có nhiều loại toa, trong đó có residential/team carriage. Chưa nhập full topology, cơ chế xuyên world, năng lực vận tải hoặc giới hạn vận hành.

`CARRIAGE_25` có Carriage ID `25`; quan hệ của Team 25 với toa này được ghi ở [20](20_TEAM_25_TAIYI_ZHENREN_CURRENT.md). Cùng số không có nghĩa team chính là toa, sở hữu toa hoặc có toàn quyền trên toa.

`TRAIN STRUCTURE != ORGANIZATION STRUCTURE`.

Không mặc định tàu là actor có ý thức. Thay đổi cấu trúc được chấp nhận cập nhật owner này; không tự cập nhật tri thức của mọi người trên tàu.
