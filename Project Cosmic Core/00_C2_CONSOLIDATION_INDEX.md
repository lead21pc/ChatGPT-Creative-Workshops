# Project Cosmic Core — Consolidation Index

## Phạm vi package

C2 là project fiction cá nhân. Current sources được duy trì trực tiếp. Module admission là quyết định quản lý package, không tự phê duyệt mọi assertion lore. Catalog row không tạo canon, authority, admission hoặc dependency.

## Địa chỉ, identity và thứ tự đọc

`FILE NUMBER != MODULE ID != FICTION ENTITY ID`.

Module ID được cấp tường minh trong builder; giữ ổn định khi đổi tên/số/sắp file. Dải chục world là cách nhóm địa chỉ, không là quota vĩnh viễn; chưa thiết kế overflow. Không tạo file lấp 08/09, scenario trống hoặc World 2.

Với tác vụ phụ thuộc C2 current state: CI gọi Router; đọc đầy đủ 00 và [05](05_OPEN_ISSUES_CURRENT.md), rồi [04](04_RECONCILIATION_RECORD.md) khi provenance/conflict/supersession/priority/owner transition có thể quyết định tác vụ. Chọn owner theo scope, không theo số kề nhau; baseline chỉ FULL_FILE.

| Địa chỉ | Vai trò và boundary |
| --- | --- |
| 01 | Actor/organization catalog: identity → owner; không sao chép profile. |
| 02 | Capability/relic catalog: definition owner khác holder/user; chưa có định nghĩa độc lập được nhập. |
| 03 / 04 / 05 | History / quyết định-reconciliation / open state; không là current lore fallback. |
| 06 / 07 | Premise tối thiểu / nguồn gốc-độ chắc chắn; chấp nhận là trục riêng. |
| 10 / 11 | Rongo / cấu trúc tàu; tổ chức khác cấu trúc vật lý. |
| 20 / 21 / 22 | Team composition, slot mở 25_3–25_5 / hai hồ sơ nhân vật riêng. Team 25 khác toa 25. |
| 100 | World catalog: World ID → world owner; không chứa world detail. |
| 110 / 111 | Persistent world truth / campaign briefing-mission knowledge. Scenario chưa tạo. |

## Control và bảo trì

CI ở `Project Cosmic Core CI/`; Router và đúng bốn family Anti-Drift ở `Anti-Drift Source/`. Router chọn theo tác vụ, không nạp mọi file. Control/tooling/manifest/tests/tools/archive không chiếm số nguồn.

`Source_Archive/` chỉ lịch sử/provenance, không là fallback hoặc đầu vào dựng lại current. Manifest và builder không chốt canon; --write chỉ cập nhật vùng generated allowlisted. Local repository khác live GPT Project deployment.

## Persistent state và carryover

World owner giữ world truth/state bền; briefing giữ thông tin/lệnh/kỳ vọng được cấp; scenario khi có giữ event/branch state. Chỉ consequence được tác giả chấp nhận mới cập nhật từng actual controlling owner bị ảnh hưởng theo scope/mốc; ghi quyết định ở 04, giữ open state ở 05. Character holder không sở hữu định nghĩa relic; world updated không đồng nghĩa actor updated.

<!-- BEGIN GENERATED MODULE CATALOG -->
## Runtime Module Catalog

> Derived routing index only. A row grants no canon authority, automatic
> admission, or dependency. Check the source header and package state before
> using a module. This table does not change the reading order above.

| Module ID | Current source path (relative to Project Cosmic Core/) |
| --- | --- |
| `C2M-001` | `01_C2_ACTOR_ORGANIZATION_CATALOG_CURRENT.md` |
| `C2M-002` | `02_C2_CAPABILITY_RELIC_CATALOG_CURRENT.md` |
| `C2M-006` | `06_C2_PREMISE_CORE_CURRENT.md` |
| `C2M-007` | `07_C2_PREMISE_PROVENANCE_CURRENT.md` |
| `C2M-010` | `10_RONGO_CURRENT.md` |
| `C2M-011` | `11_TRAIN_STRUCTURE_CURRENT.md` |
| `C2M-020` | `20_TEAM_25_TAIYI_ZHENREN_CURRENT.md` |
| `C2M-021` | `21_CHARACTER_25_1_CURRENT.md` |
| `C2M-022` | `22_CHARACTER_25_2_CURRENT.md` |
| `C2M-100` | `100_WORLD_CATALOG_CURRENT.md` |
| `C2M-110` | `110_WORLD_001_CURRENT.md` |
| `C2M-111` | `111_WORLD_001_CAMPAIGN_01_BRIEFCASE_CURRENT.md` |

<!-- END GENERATED MODULE CATALOG -->
