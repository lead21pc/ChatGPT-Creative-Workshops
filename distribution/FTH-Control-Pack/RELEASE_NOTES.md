# FTH-Control-Pack 0.1.0

## Mục đích

Giữ operation/stage, source authority, unresolved state và authoring stop point trong project dài hạn.

## Bao gồm

README, LICENSE, ba control chính, MCA tùy chọn và tests/SCENARIOS.md. File RELEASE_NOTES.md này cũng nằm trong archive. Onboarding/copy/test/rollback nằm trong [README](README.md).

## Cố ý loại

Toàn bộ lore/canon sources, character/world-state, historical reconciliation contents, Economy, Total War, Undie, RP, candidates và archives.

## Mức áp dụng và delta

Reference và reusable adaptation template; starter/control chỉ dùng sau cấu hình và xác minh. Không production ready. Namespace/output language, source/control/storage bindings và ba vai trò discovery/open-state/reconciliation được tham số hóa; reconciliation cho phép owner/path/mechanism riêng, không đòi file record. MCA giữ body; chỉ đổi title/status/authority hook và peer-owner paragraph. Không runtime migration.

## Kiểm chứng

- SOURCE-DERIVED: nguồn và hashes bên dưới được đối chiếu tại source revision.
- STATICALLY VERIFIED: kiểm inventory, YAML, placeholders, references, license, scope, binding và preservation contracts bằng distribution/tests/test_release_packs.py của repository nguồn.
- REGRESSION VERIFIED: chỉ hồi quy tự động source-preservation và fixture cấu hình; SCENARIOS vẫn SPEC / NOT_RUN bằng model. Không phải behavioral regression PASS.
- PACKAGING VERIFIED: asset được tạo lặp lại và kiểm inventory/bytes sau giải nén; xem quy trình PACKAGING.md trong repository nguồn. Chỉ báo trạng thái đạt sau khi thực sự chạy kiểm.
- LIVE VERIFIED: NOT_RUN; không có portability/deployment trên project khác được chứng minh. PASS của hệ nguồn không chuyển sang pack.

Kết quả local ngày 2026-10-31: suite extraction chạy với `--archives` đạt **17/17**, không skip, gồm kiểm inventory/metadata/CRC và byte sau giải nén. Hồi quy hệ nguồn: Router FTH **28/28**, Hub **178/178**; hai kết quả này chỉ bảo vệ hệ nguồn. Hashes toàn tracked subtree FTH/Hub giữ nguyên. Các tình huống model vẫn NOT_RUN. ZIP cuối được kiểm lại và đối chiếu hai lần tạo theo PACKAGING.md trước commit.

EXTRACTED SUCCESSFULLY != LIVE VERIFIED ON ANOTHER PROJECT.

## Tương thích và provenance

Repository: `lead21pc/chatgpt-ci-worldbuilding`. Source revision: `7dd8ce9ceae77b09b6e20f0c686f41f9b1945807`. Release version 0.1.0 độc lập source versions; không đòi history hoặc các file nguồn để dùng archive. Hashes nhận diện nguồn, không trao canon authority.

| Nguồn | Đường dẫn provenance trong repository nguồn | SHA-256 |
| --- | --- | --- |
| FTH CI 3.4 | `Project Feather Core/Project Feather Core CI/FTH_CI_version_v3.4.md` | `5d5a2f89c15a27d4b4dfb78c6818f194025a47fac13df241c9d368427bb0e79d` |
| FTH Router 5.0 | `Project Feather Core/Anti-Drift Source/FTH_Anti_Drift_Source_Router_v5.0.yaml` | `9d77216267db30a2465e54b6d31fa90f80553ada0106758224be6f61475bb9fa` |
| FTH Pipeline 1.1 | `Project Feather Core/Anti-Drift Source/FTH_Authoring_Pipeline_v1.1.md` | `2290abf544289431cc6188aa683fa940e23eedeff397bb47491a952daf8a9691` |
| FTH MCA 1.2 | `Project Feather Core/Anti-Drift Source/FTH_Anti_Drift_Modular_Concept_Architecture_v1.2.md` | `52d988861fb04b5f3159c3ffbaf1cf0ac6ceb7446b4293271c8b90d4a3e9a6f4` |

## License

Pack thuộc [MIT License](LICENSE) của repository, copyright 2026 lead21pc. Giữ notice khi phân phối. Historical wording không là runtime dependency và không được copy vào pack; README gốc hiện hành được sửa để dẫn đúng MIT. Không sửa historical artifacts.
