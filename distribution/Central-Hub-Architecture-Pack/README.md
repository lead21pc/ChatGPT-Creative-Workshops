# Central Hub Architecture Pack 0.1.0

Kiến trúc tham chiếu và starter tùy chọn cho một Hub điều phối nhiều capability theo mission: chọn phần đóng góp cần thiết, giữ authority trong scope được giao và kết hợp kết quả mà không để một package chiếm toàn mission. Nó giải việc chọn control theo topic/thói quen, trộn quyền giữa module và coi routing như chế độ tồn tại lâu dài.

Đây không phải SaaS/framework, executable router, ontology chung hoặc bản sao deployment cá nhân. Người chỉ muốn nguyên tắc có thể đọc README và Architecture mà không cài. Project đơn giản chưa cần nhiều capability không buộc dùng Hub.

## Hình dạng tổng thể

```text
                          MISSION
                             |
                           HUB CI
                             |
                           ROUTER
                             |
                    ROOT PACKAGE CATALOG
                             |
                 package set theo current task
                             |
                         ENTRYPOINT
                       /            \
                 singleton      nhiều module chọn riêng
                     |               |
                     |         LOCAL CATALOG (khi cần)
                     |            /       \
                     |         MODULE 1  MODULE 2
                     |            \       /
                     +------ scoped contributions
                                   |
                            HUB COMPOSITION
                                   |
                              MISSION RESULT
```

CI giữ operation/stage/truth/state, quyền hành động, nhu cầu kiểm chứng và giải thích. Router chọn package/module set có phạm vi và kiểm dependency/read/composition. Architecture sở hữu hợp đồng kỹ thuật chung. Catalog chỉ khai inventory/applicability/binding, không cấp authority hoặc chạy module. Module giữ behavior chuyên biệt; platform mới thực hiện retrieval/tool. Composition xảy ra sau khi các artifact được chọn đã qua kiểm binding/read và chỉ trong scope được giao.

## Fork/Copy what?

| Nếu bạn muốn | Hãy lấy |
| --- | --- |
| Chỉ nguyên tắc Hub | README + [Architecture](ARCHITECTURE.md) |
| Dựng Hub tối thiểu | [CI](starter/hub-ci.md) + [Router](starter/hub-router.yaml) + Architecture + [root Catalog](starter/root-catalog.yaml) + một singleton |
| Học package/module design | Architecture + [TECHNICAL worked example](starter/packages/HUB-DOM-TECHNICAL_v1.0.md) |
| Tích hợp Library | Binding/resolution trong Architecture và Router; không cần personal IDs từ hệ nguồn |
| Chỉ học routing | Đọc phần routing; không cần clone toàn repository |

Minimum runtime gồm bốn file hạ tầng và một singleton. [SCENARIOS](tests/SCENARIOS.md), release notes và README là tài liệu, không cài làm runtime control. Local catalog, package thứ hai, pipeline và công cụ đều tùy nhu cầu; pack không kèm chúng.

## Quick Start

1. Lưu bộ cũ để rollback; chọn dùng TECHNICAL hoặc thay bằng singleton của bạn theo mục dưới.
2. Thay `{{OUTPUT_LANGUAGE}}` trong CI. Thay mọi `{{LIBRARY_ROOT}}` trong Router, root Catalog và Architecture bằng cùng một root Library thực tế. Các token chỉ là chỗ thay văn bản, không tự nội suy.
3. Giữ exact extracted stack 0.1.0: `hub-ci.md`, `hub-router.yaml`, `ARCHITECTURE.md`, `root-catalog.yaml`. Cài CI vào Project Instructions; ba core source vào Project Sources bằng đúng tên mà references sử dụng. Vị trí thư mục trong ZIP không tự là runtime locator.
4. Cài singleton vào Library root đã chọn. Xác lập đúng identity, artifact version, headers/body và FULL_FILE. IDs nội bộ có thể null nếu đường root-scoped resolution thật đáp ứng hợp đồng; không bịa ID, không dùng local file thay Library.
5. Sau cấu hình/cài bộ tương thích, đổi status của core Architecture, Router và root Catalog từ ADAPTATION_TEMPLATE sang ACTIVE; đổi cả `contracts.architecture.status` và `contracts.root_catalog.status` trong Router sang ACTIVE; bật `active` ở Router/Catalog và `runtime_ready` ở Catalog. Giữ mọi version/pin 0.1.0 khớp. Những thay đổi này chỉ khai sẵn sàng, không chứng minh retrieval hoặc live PASS. Example artifact ACTIVE/1.0 không tự kích hoạt.
6. Dò token bằng lệnh dưới, parse hai YAML, thử SCENARIOS với actual reads. Bắt đầu một package; chỉ thêm package thứ hai khi có use case thật. Chỉ thêm local catalog khi nhiều module selectable khiến direct entrypoint không đủ.

```powershell
python -c "from pathlib import Path; import re,sys; paths=[Path('ARCHITECTURE.md'),*Path('starter').rglob('*')]; bad=[str(p) for p in paths if p.is_file() and re.search(r'\{\{[A-Z_]+\}\}',p.read_text(encoding='utf-8'))]; print('Unresolved placeholders:',bad); sys.exit(bool(bad))"
```

## Thay TECHNICAL bằng singleton của bạn

CENTRAL HUB ARCHITECTURE != TECHNICAL.
TECHNICAL = INCLUDED WORKED EXAMPLE.

Bạn có thể dùng example nguyên trạng hoặc thay nó. Giữ core selector/composer của Hub, chỉ sửa root Catalog entry: Package ID, entrypoint Module ID, Runtime role, Status, artifact Version, applicability và Library location/binding. Cung cấp module có headers khớp, scope và responsibility boundary rõ; `local_catalog: null`, Requires chỉ khi có hard dependency thật. Cài/xác minh module thay thế qua cùng Library contract. Không phải sửa Router algorithm hoặc tạo role mới nếu role hiện có diễn đạt đủ trách nhiệm.

Đổi example sang một package tóm tắt tài liệu, chẳng hạn, cần khai applicability và body của package đó; không đổi mọi package thành REASONING_PROFILE. Tên prefix không xác định role. Không giữ quyền hoặc dependency của TECHNICAL nếu module thay thế không sở hữu chúng.

TECHNICAL body được giữ byte-exact từ nguồn. Nó nhắc AIS để cấm self-activation, không yêu cầu AIS tồn tại. Starter không đăng ký AIS/ImageT/Concept Development; nếu cần package chưa có, báo unresolved/block phần phụ thuộc, không tự khám phá. Thêm package sau này là quyết định riêng, không phải điều kiện cài example.

## Ranh giới composition và binding

PARTICIPATION != AUTHORITY. PACKAGE MEMBERSHIP != SEMANTIC CONTAINMENT. CATALOG ENTRY != ACTIVATION. REFINES != REQUIRES. COMPLEMENTS != REQUIRES. ROUTING != ONTOLOGY. CAPABILITY != AUTHORIZATION.

Refines chỉ tinh chỉnh matched responsibility, giữ base coverage bên ngoài. Complements là đóng góp độc lập. Chỉ explicit accepted Requires tạo hard closure; thiếu/cycle chặn dependent portion. Không suy dependency từ mention hoặc membership.

Một package có một runtime binding. Starter dùng Library-only singleton: không repository/local filesystem/Project Sources/Memory/archive fallback. Root Catalog chưa có locator không có nghĩa được phép thay nguồn. Phải có một identity path thực được xác minh trước execution; search hit/header/snippet không là FULL_FILE. Xem hợp đồng đầy đủ trong Architecture và Router.

## Test và rollback

Thử [SCENARIOS](tests/SCENARIOS.md) bằng fixture tổng hợp trước workload thật; ghi model/surface/revision, actual reads, scope, kết quả và giới hạn. Ca kiểm tra có thể thay TECHNICAL bằng singleton khác mà không sửa core. Static/spec tests không chạy model hoặc chứng minh Library retrieval. Bộ test repository nguồn được mô tả trong PACKAGING.md; đọc/copy pack không đòi dependency test đó.

Rollback là chủ động gỡ bộ mới và khôi phục bộ CI/Router/Architecture/Catalog/module bindings tương thích đã lưu, rồi kiểm lại. Không coi Library failure là lệnh rollback tự động; không upload history làm control hoặc chỉnh lore để làm test đạt.

## Xuất xứ, evidence và license

Derived from `lead21pc/chatgpt-ci-worldbuilding` revision `7dd8ce9ceae77b09b6e20f0c686f41f9b1945807`: CI/Router 1.1, Architecture/root Catalog 1.3, TECHNICAL 1.0. Pack là reference architecture khác current personal deployment. Không có personal Library IDs, read receipts, migration history, Concept Development experiments hoặc pipeline internals.

Xem [release notes](RELEASE_NOTES.md). SOURCE-DERIVED, STATICALLY VERIFIED, REGRESSION VERIFIED, PACKAGING VERIFIED và LIVE VERIFIED được báo riêng. Không kế thừa PASS của hệ cá nhân; chưa kiểm live portability trên project khác. Không gọi production ready.

Pack thuộc [MIT License](LICENSE), không là sản phẩm OpenAI chính thức hoặc bảo đảm hành vi của ChatGPT. Giữ copyright/license khi phân phối.
