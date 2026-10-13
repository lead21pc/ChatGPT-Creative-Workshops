# AetherFire — Module Header Migration Report

> Trạng thái: báo cáo migration cấu trúc local, ngày 2026-09-29. Không phải canon source, Project runtime source hay bằng chứng rằng CI/Router đã được cài vào ChatGPT Project.

## Phạm vi và baseline

- Git root: `C:/Users/Sheeplark/Desktop/CI Versioning Audit & Changelog`.
- Baseline trước khi sửa: branch `codex/aetherfire-architecture-audit-20260926`, HEAD `f4b7780ac3090dd486cde9bdbe6340ca10cdd9c1`; tám current lore files không có thay đổi Git. Các mục dirty khác được giữ nguyên.
- Branch thực hiện: `codex/aetherfire-module-header-migration-20260929`; không commit, push hoặc upload.
- Control đã đọc đầy đủ trước migration: `AetherFire CI/AetherFire_CI_version_v3.0.md` và `Anti-Drift Source/AetherFire_Anti_Drift_Source_Router_v4.0.md`. Router v4.0 chấp nhận `FULL_FILE` mặc định và legacy bridge khi `00` chưa có module catalog. File control local hiện diện không chứng minh đã triển khai vào Project.
- Chỉ chèn visible Markdown header ngay sau H1 trong tám current lore files `10`–`80`. Không sửa `00`, `90`–`92`, CI, Router, overlay, builder, archive cũ, source đầu vào hoặc test infrastructure.

## Snapshot rollback trước migration

- Path: `Source_Archive/Old Structure Lore/pre_module_header_2026-09-29/`.
- Manifest: `SNAPSHOT_MANIFEST.md` trong snapshot; ghi ngày, lý do, SHA-256, byte size và hướng dẫn thay file để rollback.
- Trước khi sửa active files, đã `COPY` đủ tám file vào thư mục mới, kiểm count = 8 và SHA-256/size từng cặp trùng nhau. **Snapshot verification: PASS.** Không move hoặc tái dựng file active.

| Active file | Module ID | SHA-256 trước migration (snapshot) | SHA-256 sau migration |
| --- | --- | --- | --- |
| `10_WORLD_INSTITUTIONS_GEOPOLITICS_CURRENT.md` | `AFM-001` | `01999C6249DCADEE01600BCA930480DC1B349ABF35FF72B628B6F2CE63B86266` | `82CC0066C787127FE1247F5B0528B9BDA34F0EDAA1D5085A3BB4E147C3B2CBA5` |
| `20_STATUS_CIVIL_LABOR_CURRENT.md` | `AFM-002` | `DAC6BCCEBD3DBE900D539C02A56AAAA11FBEE7AD948362F6CF1A7F1F5F5E0924` | `B6A7C7E03D4BC6FB90AE60F4A8D91676A6EE704975101A96ACA5540E6944286B` |
| `30_UNDIE_SYSTEM_CURRENT.md` | `AFM-003` | `09E04C8B15D7F0DD5C76FE71DFF963BC955B5863EEA68045395C875811F1659D` | `74B4EA2CC862E902F2424792CBAB23A0C9D9D8C42FBC57625664C760AE8225BB` |
| `40_METAFICTION_CANON_TIMELINE_CURRENT.md` | `AFM-004` | `27E485328031751858C2758B8A76EB09ED85248452AC6F380694D8A4159767D1` | `DA091979531883C282D1F1F16D006D0FEF786BCFFB7BC4F98A6DDEFDC6ECC1C6` |
| `50_NARRATORS_POV_AND_HUMOR_CURRENT.md` | `AFM-005` | `213BF2B5E258BD1E83F6AAA966B2F40F92EFE0C56A292E5883B187E1087D53FC` | `FB560B5B17C5B357A2772736DA9310C0F0549F6058A231D7E9D62B066EF7FB99` |
| `60_MC4_IDENTITY_CURRENT.md` | `AFM-006` | `2B11C4846788A607B311854E0667E2A918F55E07F648A9DC70ED0C3A8187B088` | `0DAA2D8FA67677899A96BB1450B0DA01534430CBF2C87A338A91285591E20745` |
| `70_MATRIARCHS_LAMENT_CURRENT.md` | `AFM-007` | `C6E68E05E75AEA82CAB85FC2A8FC5E1F433D3A04589227E88786F86101D13D88` | `A843D44362392AA1940F69A9FCE0C26576DC82713586ABBCB419F964778F8158` |
| `80_STABLE_AVIATION_RF_AIRSPACE_CURRENT.md` | `AFM-008` | `CA5DDC126B5862ACBFFC71067ADB048F265EBAB5D053468E0627363DC216677C` | `AD809C5C47E7786AB2DF30BBE3B8F4102D90F9E470816D1C130B9C3600DA298C` |

## Kiểm chứng sau migration

- **Structural validation: PASS.** Đúng tám Module ID `AFM-001`–`AFM-008`, không trùng; mỗi header có đúng sáu trường được yêu cầu, `Runtime role: CURRENT_SOURCE` và `Load mode: FULL_FILE`. H1 và filename không đổi. Không thêm `MODULE_REQUIRES`, `NODE_REQUIRES`, local index, node marker, coverage hoặc generation metadata.
- **Lore preservation: PASS.** Từng active file được so ở mức byte với snapshot: giữ nguyên prefix gồm H1, bỏ duy nhất block header mới tại vị trí sau H1, rồi so toàn bộ byte còn lại với archive. Cả tám cặp khớp tuyệt đối; do đó semantic headers cũ, lore body, truth status, thứ tự mục, UTF-8 không BOM và LF đều được bảo toàn. Không có `MIGRATION_CONTENT_DRIFT`.
- **Git diff: PASS.** Diff chỉ gồm block sáu trường và dòng trống sau H1 trong từng file; `git diff --check` trên tám file không báo lỗi. Không có thay đổi ngoài phạm vi trong diff task-owned.
- **Rollback fixture: PASS.** Với mỗi file, copy bản active đã migration vào thư mục tạm, thay bằng archive copy cùng tên, rồi kiểm hash fixture trở về đúng SHA-256 trước migration; hash của active migrated file vẫn giữ nguyên. Không rollback active tree thật. Fixture tạm đã xóa sau phép thử.

## `REVIEW_REQUIRED` và giới hạn

- Không thêm hard dependency. Các ranh giới chủ sở hữu `AFM-005` ↔ `AFM-004`, `AFM-006` ↔ `AFM-001`/`AFM-004`, `AFM-007` ↔ `AFM-001`/`AFM-003`/`AFM-004`, `AFM-008` ↔ `AFM-001` chỉ là **ứng viên cần review theo task class**, không tự biến thành `MODULE_REQUIRES` từ mention hoặc cross-reference.
- `BUILDER_PERSISTENCE_REVIEW_REQUIRED`: current lore files là generated views; builder hiện có thể ghi đè header trong lần regenerate sau. Task này không sửa hoặc chạy builder trên active tree.
- `00` chưa có module catalog theo phạm vi task; Router v4.0 có legacy `FULL_FILE` bridge. Migration local không chứng minh Project đã cài CI 3.0/Router 4.0 hoặc upload tám file mới. Không kiểm hành vi ChatGPT Project runtime trong task này.
- Không bắt đầu phase node routing/catalog. Không commit, push, merge, tag hoặc release.
