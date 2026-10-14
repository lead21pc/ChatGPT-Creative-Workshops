# Remote cleanup và reconciliation — 2026-10-14

Baseline: local/main/GitHub main `431e8cc6285a7329cb5e92f101159c62c8ba0756`. Origin: `https://github.com/lead21pc/chatgpt-ci-worldbuilding.git`. Không dùng tuổi/tên branch để quyết định authority. Không merge whole branch, không tạo local task branch, không đổi current lore hoặc controls.

## Phạm vi và nguồn

| Branch nguồn | SHA đã audit | Identity chưa chứng minh ở vòng trước |
| --- | --- | --- |
| Invariant-System | `93d6e1083cb0fbed5691d064d8e9fd2b5f7898a7` | 72 |
| codex/aetherfire-cold-storage-20261002 | `81a3026bdcbc788f7217a1c4c4abb3c284f58c89` | 8 |
| maintenance/ci-version-audit | `06627ae731fe5d421c9f38f0a528fe61c4872728` | 18 |

`INVENTORY.csv` bao phủ từng content identity: size, SHA-256, Git blob, tip/history, first-known commit/parent, commit thay blob, chronology, authority, main relation và action. Không coi 98 identity là 98 missing semantic payload.

## Invariant-System — 72 identity

| Logical group | Số lượng | Chronology / authority | Main relation và action |
| --- | --- | --- | --- |
| Fixture revisions | 33 | PREDECESSOR / SUPERSEDED | CONTAINED: toàn bộ scenario, operation, protected distinction, forbidden conversion và lifecycle giữ nguyên; chỉ provenance/control paths/SHA metadata khác. |
| Manifest generations | 13 | PREDECESSOR / SUPERSEDED | SUPERSEDED: metadata của source generation tương ứng; note/archive inventory được main giữ, không nhập hash cũ. |
| README/control documentation | 9 | PREDECESSOR / SUPERSEDED | CONTAINED bởi contract/successor, current activation và các bản rollback được main giữ. Không dùng ghi chú candidate cũ để phủ định promotion đã chấp nhận. |
| Source/reconciliation/routing snapshots | 6 | PREDECESSOR / SUPERSEDED | CONTAINED: bảy nguyên tắc Hoa Nguyệt, tách20–23 và namespace được main hấp thụ; không thay canon bằng predecessor. |
| Regression runners | 3 | PREDECESSOR / SUPERSEDED | CONTAINED: main giữ core và hỗ trợ hosted paths/YAML/Pipeline; không phục hồi đường dẫn local cũ. |
| Glossary | 2 | PREDECESSOR / SUPERSEDED | CONTAINED: definitions giữ nguyên; thuật ngữ Git Test Branch được thay bằng Project Git Workflow. |
| System context | 2 | PREDECESSOR / SUPERSEDED | CONTAINED: main giữ toàn bộ authoring/evidence boundary và thêm organization/author-background guardrails. |
| Skill draft | 1 | PREDECESSOR / SUPERSEDED | CONTAINED: main giữ nguyên body, thêm coordination boundary; tip draft còn exact với main. |
| Structure-lock policies | 2 | PREDECESSOR / HISTORICAL | ARCHIVE nguyên byte ở shared `codex-workflows/Source_Archive/remote_structure_policy_2026-10-14/`. |
| CI3.1 header predecessor | 1 | PREDECESSOR / SUPERSEDED | SUPERSEDED: toàn bộ body trùng main3.1; chỉ H1 `ChatGPT 8.8 temp language` được sửa thành `ChatGPT 8.8 base`. Không có behavior bị thiếu. |

Tổng: 56 CONTAINED, 14 SUPERSEDED, 2 ARCHIVE. Không phát hiện accepted work cần active integration. Chronology dựa trên parent/content evolution và first-known object changes, không dựa trên mtime.

### Chín file tại tip

- `91`: main chỉ thêm section provenance xuất bản; source phần còn lại được giữ đầy đủ.
- Glossary: chỉ còn khác biệt Git Test Branch → Project Git Workflow.
- Manifest: chỉ khác hai hash91/92 theo snapshot; không phải nguồn authority.
- Regression README: main giữ các probe/giới hạn và thêm six main-only fixtures, parser/path correction, active3.3/5.0; source còn mô tả candidate/baseline cũ.
- `capability_availability.json`, `unknown_invention.json`: scenario/lifecycle giữ nguyên, khác path/control metadata.
- Runner: main giữ core, dùng upstream path hiện có và hỗ trợ YAML/Pipeline; không có thuật toán được chấp nhận bị bỏ.
- Root README và SYSTEM_CONTEXT: main giữ project/country boundary, nội dung giải thích và thêm guardrails/layout; nguồn dùng các path trước relocation.

Hai policy archive là snapshot của `5cabf15` và `887068a`; lock bị gỡ rõ ràng tại `8dd6ba0`. Đổi tên thành `AGENTS_structure_lock_<commit>.md` chỉ để tránh tự nạp thành AGENTS hiện hành; nội dung không đổi và không có hiệu lực. Không sửa root AGENTS hoặc reinstatement hai-affirmation policy.

## Cold storage — 8 identity

Chronology `EXPERIMENTAL_SIDE_PATH`, authority `CANDIDATE`, action `KEEP_CANDIDATE` cho trọn component có ranh giới. Chuỗi `98d563a → e2b2485 → 81a3026` phát triển package rồi pin/reuse contract; không trở thành current-main Router5. Báo cáo gốc phân biệt prepared target với live attachment update chưa thực hiện. Không suy newer/accepted từ commit publication, cũng không ép candidate thành obsolete để cleanup.

Bảo toàn tám file tại `Project Feather Core/New Canon and Consideration/AetherFire_Cold_Storage_Prototype_2026-10-02/`, có status document riêng. Giữ nguyên index/router/manifest bindings và tooling/report; không chạy chúng trên current package. Package là serialized fixture của bảy payload đã BYTE_CONTAINED trong main history. `COLD_SOURCE_RECEIPT.json` ghi original bytes/SHA, main blob và captured manifest; không tạo authority mới từ bundle.

Input của prototype là generation bảy cold sources cùng chín hot fingerprints; output là bundle pinned; retained state chỉ có task-local load receipt, không cache xuyên chat. Failure behavior chặn wrong ref/hash/generation, partial/corrupt/missing/duplicate payload và fetch fanout. Giá trị riêng là contract storage và bằng chứng kiểm generation; không có accepted current behavior được phục hồi hoặc deployment được suy ra.

## CI version audit — 18 identity

Không đồng nhất remote với local theo tên. Đã xác minh actual remote tip đúng `06627ae` và toàn bộ 48 blob của lịch sử độc lập khớp inventory tại `docs/instruction-history/isolated-ci-version-audit-2026-10-14/INVENTORY.csv`, kể cả SHA-256 và size cho 18 identity đang xét.

Kết quả subset: 17 SUPERSEDED, 1 CONTAINED. Changelog được successor mở rộng; Go/Free note vẫn được giữ; rationale/audit có successor hoặc main history; failure model có topology mới; visualization có revised rule-state matrix và evidence văn bản hiện hành. DOM renderer không phải behavior CI riêng, không archive chỉ vì unique byte. Ba CI snapshot có giá trị đã được main giữ từ recovery trước, không copy lại. Không có accepted rationale hoặc normative CI mới cần nhập.

## Verification và remote gate

Mười file gốc được giữ mới (8 candidate + 2 retired policies) phải khớp SHA-256, size và Git blob. Archive/candidate nằm ngoài direct current-source allowlist và active control resolution. Không có artifact replacement active; replacement checker không áp dụng. Dùng đúng existing candidate/shared archive, không tạo archive framework.

Prototype được kiểm read-only bằng manifest/body digest và main-history mapping; offline test closure được dựng riêng từ đúng original main blobs, không dùng current canon làm giả generation cũ. Package/Router/current unit tests chỉ chứng minh cấu trúc và regression scope, không chứng minh model hoặc deployment.

Chạy prototype dưới locale Windows cp1252 đã tái hiện `UnicodeDecodeError` do index reader không chỉ định encoding; đây là giới hạn của snapshot, không phải regression current package. Lượt kiểm lại dùng `python -X utf8`, giữ nguyên mọi source byte và ghi điều kiện này trong candidate status. Không sửa portability hoặc suy UTF-8-mode PASS thành default-locale PASS.

Năm branch SAFE đã xóa ở giai đoạn1 sau khi HEAD khớp audit trước. Ba branch còn lại chỉ được xóa sau khi recovery đã commit/push lên main, UNKNOWN bằng0, lịch sử không còn payload chưa account, remote main/branch HEAD không đổi ngoài publication được phép. Không force push, không object pruning, không tạo ref thay thế.

Academy remote `academy-restructure-phase-1@941d9f81a85ed30a38457b0783acd377f166d04c` và preserved Academy repository ngoài scope, không audit/xóa/import. Main là baseline repo chính, không phải authority của Academy.
