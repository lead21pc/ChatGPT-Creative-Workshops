# C2 — Danh mục năng lực và relic

> Module ID: `C2M-002`
> Runtime role: `CURRENT_SOURCE`
> Domain / Scope: Định tuyến hệ sức mạnh, capability, spell, technique, relic, divine/sacred artifact, inheritance, energy source và tài sản có identity.
> Authority boundary: Chỉ định tuyến; không là bộ định nghĩa chung hoặc nơi cấp quyền sở hữu.
> Cross-domain owner boundary: Năng lực riêng của 25_1 ở `C2M-021`, của 25_2 ở `C2M-022`; thánh tích World 1 ở `C2M-110`; định tuyến tác nhân và thế giới qua `C2M-001`, `C2M-100`.
> Load mode: `FULL_FILE`

## Danh mục

| Mục tra cứu | Loại | Nguồn định nghĩa trong phạm vi đã xác lập |
| --- | --- | --- |
| Cosmic Mage | Nhóm năng lực của 25_1 | [21](21_CHARACTER_25_1_CURRENT.md) |
| Os s5shi | Câu chú riêng của 25_1 | [21](21_CHARACTER_25_1_CURRENT.md) |
| Battle Shaman / Battle Priest | Nhóm năng lực của 25_2 | [22](22_CHARACTER_25_2_CURRENT.md) |
| Thánh tích World 1 | Thánh tích | [110](110_WORLD_001_CURRENT.md) |

Một nguồn có thể sở hữu nhiều định nghĩa trong phạm vi của mình.


## Hợp đồng entry khi có nguồn

Mỗi entry thực có giữ identity, alias nếu có, loại và nguồn định nghĩa theo phạm vi. Nếu có instance/tài sản cụ thể, dẫn riêng tới owner trạng thái instance đã được xác lập; không tự cấp ID hoặc tạo source.

`DEFINITION OWNER != CURRENT HOLDER / USER`.

Nhân vật dùng/mang một relic không khiến nguồn nhân vật sở hữu định nghĩa relic. Quan hệ holder/user có owner riêng theo assertion; nếu chưa chốt, giữ UNKNOWN. Dẫn chéo actor/world chỉ giúp tìm nguồn, không suy dependency hoặc chuyển ownership.
