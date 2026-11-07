# C2 — Danh mục năng lực và relic

> Module ID: `C2M-002`
> Runtime role: `CURRENT_SOURCE`
> Domain / Scope: Định tuyến hệ sức mạnh, capability, spell, technique, relic, divine/sacred artifact, inheritance, energy source và tài sản có identity.
> Authority boundary: Chỉ định tuyến; không là bộ định nghĩa chung hoặc nơi cấp quyền sở hữu.
> Cross-domain owner boundary: Năng lực áp dụng cho A ở `C2M-021`, B ở `C2M-022`; identity tác nhân qua `C2M-001`; world qua `C2M-100`.
> Load mode: `FULL_FILE`

## Trạng thái baseline

Chưa có định nghĩa capability/relic độc lập được nhập và cấp identity riêng. Vì vậy chưa có entry định nghĩa hoặc relic instance trong danh mục này.

Hai nhãn năng lực tối thiểu đã biết được ghi trong hồ sơ [A](21_CHARACTER_25_1_CURRENT.md) và [B](22_CHARACTER_25_2_CURRENT.md); chúng không phải định nghĩa đầy đủ của hệ sức mạnh và không tự tạo capability ID.

## Hợp đồng entry khi có nguồn

Mỗi entry thực có giữ identity, alias nếu có, loại và nguồn định nghĩa theo phạm vi. Nếu có instance/tài sản cụ thể, dẫn riêng tới owner trạng thái instance đã được xác lập; không tự cấp ID hoặc tạo source.

`DEFINITION OWNER != CURRENT HOLDER / USER`.

Nhân vật dùng/mang một relic không khiến nguồn nhân vật sở hữu định nghĩa relic. Quan hệ holder/user có owner riêng theo assertion; nếu chưa chốt, giữ UNKNOWN. Dẫn chéo actor/world chỉ giúp tìm nguồn, không suy dependency hoặc chuyển ownership.
