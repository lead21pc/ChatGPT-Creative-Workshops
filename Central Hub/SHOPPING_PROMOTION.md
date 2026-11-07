# Shopping 1.0 — promotion trong repository

## Cập nhật hiện hành — 2026-11-08

Production baseline CI/Router 1.1, Architecture/Catalog 1.11, Concept core/catalog 1.2, Authoring 0.7, năm control production, Shopping 1.0 và AIS/ImageT: **USER_CONFIRMED_INSTALLED_AND_LIVE / USER_CONFIRMED_LIVE_PASS** theo xác nhận người dùng trong tác vụ này. Không phải Codex tái hiện độc lập; không suy ngày chạy, kết quả từng ca, FULL_FILE/duplicate receipts hoặc Library IDs/locator chưa được cung cấp.

Correction hiện hành: Architecture/Catalog 1.12, Authoring 0.8, Concept core/catalog 1.3, MCA 1.2; CI/Router giữ 1.1. **IMPLEMENTED / STATICALLY VERIFIED; LIVE VERIFICATION OF NEW DELTA: NOT RUN**. Baseline PASS không bị reset. Tác vụ này không deploy.

Contributor Authoring đã retire: mọi `+ CREATIVE` / `+ BRAINSTORM` không activation và không được bỏ suffix để chạy plain Authoring. Creative/Brainstorm vẫn là exact Concept operations độc lập. Kết quả được cung cấp hoặc referenced rõ là ordinary source/context theo Authoring, không phải contributor. Clarification phải hướng dẫn exact call/span mới; không giữ mode, target, preset hay isolation ngầm.

Xem [runtime evidence](RUNTIME_EVIDENCE_CHANGELOG.md). Các phần dưới là lịch sử đúng thời điểm, không là trạng thái production hiện hành hoặc hướng dẫn cài bộ cũ.

## Hồ sơ lịch sử trước correction

Ngày 2026-11-06 (Asia/Bangkok). Baseline `main` tại `6d49cd4ad537353f13afe6772bf0635eb83be308`, trùng `origin/main`, working tree và index sạch.

Shopping là gói thứ sáu trong Architecture và Root Catalog 1.10. Bản 1.10 nối tiếp 1.9 trong cùng dòng 1.x. Router 1.1 chỉ đổi hai pin và mô tả phạm vi binding. CI 1.1 cùng bindings của Technical, Concept Development, Authoring, AIS và ImageT giữ nguyên.

## Artifact cài đặt

Ba file dưới đây chuyển từ [Shopping v1 candidate](candidates/shopping_v1/) sang `ACTIVE/1.0` trong repository, cùng Package ID `HUB-PKG-SHOPPING`.

| File | Module ID | Vai trò |
| --- | --- | --- |
| [HUB-DOM-SHOPPING_v1.0.md](library_modules/HUB-DOM-SHOPPING_v1.0.md) | `HUB-DOM-SHOPPING` | `DOMAIN_CONTROL` |
| [HUB-CATALOG-SHOPPING_v1.0.yaml](library_modules/HUB-CATALOG-SHOPPING_v1.0.yaml) | `HUB-CATALOG-SHOPPING` | `PACKAGE_CATALOG` |
| [HUB-PROC-SHOPPING-SEARCH_v1.0.md](library_modules/HUB-PROC-SHOPPING-SEARCH_v1.0.md) | `HUB-PROC-SHOPPING-SEARCH` | `DOMAIN_PROCEDURE` |

Root Catalog chỉ khai báo entrypoint và Catalog cục bộ. Chứng cứ cung cấp đủ thì closure gồm core và Catalog cục bộ. Khi phạm vi Shopping cần chuẩn bị hoặc diễn giải nghiên cứu bên ngoài, Catalog cục bộ chọn Search. Hub xác định nhu cầu chứng cứ và chọn AIS độc lập. Các ranh giới ProductCandidate/SKU/Offer, HARD/SOFT, priority_order, Category, điều kiện giá và độ phủ giữ nguyên từ candidate.

## Kiểm chứng và lịch sử

Kiểm tra tĩnh và fixture đạt 242/242, gồm 10 ca promotion, 14 ca v1 candidate và 24 ca tiền nhiệm. Các nhóm Hub, Authoring, Concept, AIS và ImageT lần lượt đạt 84, 38, 32, 33 và 7 ca. Test bộ hiện hành kiểm sáu gói. Test lịch sử tiếp tục đọc đúng snapshot năm gói.

Candidate Shopping v0.1/v1 và Authoring 0.7 được giữ nguyên. [Receipt lưu trữ](<Source_archive/Shopping 1.0 promotion 2026-11-06/ARCHIVE_RECEIPT.json>) ghi SHA-256 của Architecture/Catalog 1.9 và Router 1.1 với pin 1.9. Ba bản lưu nguyên byte dành cho đối chiếu và rollback có chủ đích theo cả bộ.

## Trạng thái runtime

**USER-PROVIDED LIVE BEHAVIOR EVIDENCE** áp dụng cho candidate. Người dùng cung cấp kết quả về Offer cố định, HARD UNKNOWN, tách seller/channel, đường không tìm kiếm, tìm giá thực tế, mở rộng storefront, liên kết giá với SKU, tách điều kiện giá, báo độ phủ một phần và tìm lại khi 500 g trở thành HARD. Codex chưa tái hiện các ca đó.

Library installation và Project deployment của bộ 1.10 đều `NOT_PERFORMED`. Binding Shopping là `UNRESOLVED`. Live Hub routing, Shopping Library retrieval và AIS composition trên bộ mới đều `NOT RUN`.

Bước thủ công kế tiếp là cài đúng ba file trên vào Library / `Central Hub Config` và xác minh từng object qua `FULL_FILE`, Module ID, Package ID, vai trò, trạng thái, phiên bản, nội dung, ranh giới trách nhiệm và trùng lặp trong phạm vi Library root.
