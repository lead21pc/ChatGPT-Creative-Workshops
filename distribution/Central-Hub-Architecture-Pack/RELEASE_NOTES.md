# Central-Hub-Architecture-Pack 0.1.0

## Mục đích

Tổ chức scoped mission contributions và composition, giữ authority của từng owner.

## Bao gồm

README, ARCHITECTURE, LICENSE, CI/Router/root Catalog starter, singleton TECHNICAL và tests/SCENARIOS.md. File RELEASE_NOTES.md này cũng nằm trong archive. Onboarding/copy/test/rollback nằm trong [README](README.md).

## Cố ý loại

Personal Library IDs/read receipts/deployment evidence, migration history, inventory khác, Concept experiments, FTH lore, AIS/ImageT internals.

## Mức áp dụng và delta

Reference và reusable adaptation template; starter/control chỉ dùng sau cấu hình và xác minh. Không production ready. Architecture và Router giữ technical contracts, bỏ personal topology/evidence/history; pins/output/root được tham số hóa. TECHNICAL byte-exact là worked example có thể thay qua Catalog, không là universal dependency. Không runtime migration.

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
| Hub CI 1.1 | `Central Hub/HUB_CI_v1.1.md` | `7bb946874663627060d28e47674decb07ba99f51acbffb6550db98d65746157b` |
| Hub Router 1.1 | `Central Hub/HUB_ROUTER_v1.1.yaml` | `df87682c252d50937a5a7a3e7397253e93a81e0fb63f936f1b51b207e92ee9db` |
| Hub Architecture 1.3 | `Central Hub/HUB_ARCHITECTURE_v1.3.md` | `db52843f5548bc8f32e4778c790d15a3db3ac283bac41037b9d4d3a5487ffd31` |
| Hub Catalog 1.3 | `Central Hub/HUB_PACKAGE_CATALOG_v1.3.yaml` | `03febeb965ca1dab70674bd6a00750a5620624c465d8861f73e06032baf7b732` |
| TECHNICAL 1.0 | `Central Hub/candidates/promotion/HUB-DOM-TECHNICAL_v1.0.md` | `fb42257b74597d5b680e5334cf1a132f04f17eb708a507444da0f3fe4a9f73d4` |

## License

Pack thuộc [MIT License](LICENSE) của repository, copyright 2026 lead21pc. Giữ notice khi phân phối. Historical wording không là runtime dependency và không được copy vào pack; README gốc hiện hành được sửa để dẫn đúng MIT. Không sửa historical artifacts.
