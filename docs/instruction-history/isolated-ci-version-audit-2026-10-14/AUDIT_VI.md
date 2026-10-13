# Audit lịch sử độc lập maintenance/ci-version-audit

Ngày: 2026-10-14. Baseline: `b3ba702a7b724c8ae1491511a617f3875caec65b`.

Branch nguồn: `maintenance/ci-version-audit`, tip `06627ae731fe5d421c9f38f0a528fe61c4872728`. Có 17 commit, 34 file tại tip và 48 blob file duy nhất trong toàn lịch sử. `git merge-base` với baseline trả mã 1 và không có SHA: hai lịch sử không có tổ tiên chung.

## Kết quả

Không phát hiện intent đã được chấp nhận còn thiếu trong CI hiện hành. Recovery chỉ giữ ba trạng thái CI lịch sử có giá trị truy nguyên. Chúng là tài liệu lịch sử, không phải CI hoạt động, đầu vào build hoặc nguồn mặc định. Không nối lịch sử Git.

`INVENTORY.csv` ghi cả 34 file tại tip và 14 trạng thái blob trung gian: đường dẫn nguồn, Git blob, số byte, SHA-256, equivalent trên main hoặc lịch sử main, quan hệ byte/ngữ nghĩa và hành động. Tổng: 28 CONTAINED, 17 SUPERSEDED, 3 UNIQUE_HISTORICAL; UNIQUE_VALID, EXPERIMENTAL còn cần quyết định và UNKNOWN đều bằng 0. SUPERSEDED bao gồm tài liệu successor giữ lại toàn bộ phần cũ rồi mở rộng. Draft v8.0 được giữ như lịch sử thử nghiệm, không được nâng thành accepted CI.

Không blob nào tại tip byte-identical với cây baseline. CONTAINED ở đây không đồng nghĩa byte-exact: phép đối chiếu chuẩn hóa chỉ bỏ BOM UTF-8, đổi CRLF thành LF và bỏ whitespace cuối file. Inventory ghi riêng bản tương đương trong lịch sử main.

## Phân loại nội dung

| Nhóm nguồn | Equivalent | Quan hệ và quyết định |
| --- | --- | --- |
| 15 CI Go/Free v1.0–v6.4.1 | `llm-controls/global-instructions/ChatGPT Go-Free Era/` | CONTAINED: văn bản CI tại tip bằng nhau sau chuẩn hóa xuống dòng/EOF. |
| 9 CI Plus v7.0–v7.5 | `llm-controls/global-instructions/ChatGPT Plus+ Era/` | CONTAINED: văn bản CI tại tip bằng nhau sau chuẩn hóa xuống dòng/EOF. |
| Draft v8.0 | `chatgpt v8.0.txt`, tiếp đó v8.9 | UNIQUE_HISTORICAL: chỉ đoạn LANGUAGE khác bản v8.0 đã chấp nhận; giữ bản trước sửa để truy nguyên. |
| Rationale invariant | `ci_design_rationale_v3_vi_invariant_Outdated_old_kien_truc.md` | CONTAINED: toàn thân tài liệu giữ nguyên; main chỉ bổ sung nhãn lỗi thời trong H1. |
| CHANGELOG EN/VI | `docs/instruction-history/CHANGELOG*.md` | SUPERSEDED bởi bản mở rộng: cả 292 dòng cũ là tiền tố của 577 dòng hiện hành. |
| Changelog Go/Free | `llm-controls/global-instructions/ChatGPT Go-Free Era/Changelog.txt` | SUPERSEDED bởi bản mở rộng: dòng cũ vẫn còn; main bổ sung hai dòng. |
| CI_VERSIONING_AUDIT EN/VI | `docs/instruction-analysis/` | CONTAINED trong lịch sử main; bản hiện hành sửa đường dẫn và nhãn thời điểm, thêm lineage tới v8.9/v6.6. |
| CI_DESIGN_EVOLUTION_AND_DEPLOYMENT_VI | `docs/instruction-analysis/` | CONTAINED trong lịch sử main; bản hiện hành thay mốc v7.4 bằng v8.9 và bổ sung hồ sơ Go/Free v6.6. |
| CI_FAILURE_MODES_AND_CONTROL_MODEL_VI | `docs/instruction-analysis/` | SUPERSEDED: thay mô hình hai invariant ngôn ngữ bằng ba invariant hiện hành, cập nhật trạng thái failure và evidence. Không khôi phục topology đã nghỉ. |
| rule-evolution-matrix.html | `docs/visuals/` cùng tên | SUPERSEDED: main có biểu đồ mở rộng đến v8.2; lịch sử CI và audit văn bản vẫn giữ evidence của các phiên bản cũ. Không có behavior CI riêng cần recovery từ giao diện cũ. |
| Các revision docs/changelog trung gian | Các file tương ứng trên main/lịch sử main | CONTAINED hoặc SUPERSEDED theo từng blob trong CSV; không có normative CI ngoài ba trạng thái được lưu bên dưới. |

## Ba blob được giữ byte-exact

| Đích trong thư mục này | Nguồn / thời điểm | Git blob / SHA-256 |
| --- | --- | --- |
| `chatgpt_v7.3_before_product_verification.txt` | `40eaca9`, `ChatGPT Plus+ Era/chatgptv7.3.txt`; được `cc325bd` bổ sung kiểm chứng sản phẩm | `d2d5c7f74d3d32ef465fea6d235616867d922e98` / `fb269ab55f4932b3efab25c5bc2a715537f9b1ddd272000f39e7a8096dad6a3d` |
| `chatgpt_v7.4.1_before_language_unification.txt` | `2ad2c2b`, `ChatGPT Plus+ Era/v7.4.1.txt`; được `7045510` hợp nhất quy tắc ngôn ngữ | `2de92f733f8069840b9a8e28333668a7d46410b3` / `3780fd289a9b9b574aee7eb7fa57db2655b2f742d95fb994921993e353fd2b2d` |
| `chatgpt_v8.0_draft_before_language_revision.txt` | `06627ae`, `ChatGPT Plus+ Era/chatgpt v8.0 draft.txt` | `25aa18cafb542551ca92f3b3759596308c46ef2d` / `7ecc6288e971fc791db01753e8818d6f884354c48d478f1e4990e2fa73c469ea` |

v7.3 trước sửa thiếu đoạn kiểm chứng năng lực sản phẩm/runtime; successor trên main bổ sung trực tiếp. Candidate v7.4.1 trước sửa đặt quy tắc thuật ngữ ở khối kỹ thuật/phi kỹ thuật; successor chuyển và hợp nhất ở khối ngôn ngữ. Draft v8.0 có ngoại lệ thuật ngữ mềm hơn; successor thay bằng quy tắc ngôn ngữ khác, được changelog hiện hành ghi nhận. Những khác biệt này giải thích các bước thiết kế, không cung cấp invariant accepted bị mất.

## Verification và giới hạn

- Ba file được trích trực tiếp bằng `git cat-file blob`, không qua chuyển mã hoặc chuẩn hóa; SHA-256 và Git blob đích phải trùng nguồn.
- CSV bao phủ đủ 48 blob và 34 hàng tại tip; mọi hàng có phân loại và equivalent hoặc đích recovery.
- Dùng `docs/instruction-history/` hiện có. Không có artifact replacement mới và không di chuyển predecessor khỏi vùng hoạt động nên checker replacement của artifact-source-archive không áp dụng.
- Chỉ thêm tài liệu lịch sử; không sửa Global CI, Project CI, FTH, AetherFire, orphan archive hoặc Git workflow. Không có kiểm chứng runtime mới.
- Remote main trước task: `c59080c1a9caf6e5130c16cfde9a7bb13ca58570`.

Kết luận cleanup: `SAFE_TO_DELETE_AFTER_FINAL_CLEANUP`, sau khi các file recovery đã được commit và kiểm chứng. Kết luận này chỉ bao phủ nội dung tracked trong lịch sử branch, không cấp quyền xóa resource hoặc thay thế kiểm tra dirty/untracked ở task cleanup. Task này không xóa branch, worktree, binding hoặc Temp và không push.
