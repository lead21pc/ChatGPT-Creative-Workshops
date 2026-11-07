# Project Cosmic Core (`C2`)

Project fiction cá nhân về đoàn tàu xuyên các world. Repository này là skeleton quản lý đã nhập đúng premise tối thiểu; chưa phải toàn bộ lore tác giả.

## Bản đồ nguồn

| Địa chỉ | Chức năng |
| --- | --- |
| [00](00_C2_CONSOLIDATION_INDEX.md) | Package/reading map và generated Module ID → source catalog |
| [01](01_C2_ACTOR_ORGANIZATION_CATALOG_CURRENT.md) | Actor/organization identity → controlling source |
| [02](02_C2_CAPABILITY_RELIC_CATALOG_CURRENT.md) | Capability/relic → definition owner; khác holder/user |
| [100](100_WORLD_CATALOG_CURRENT.md) | World ID → world owner; không giữ world detail |
| 03 / 04 / 05 | History / quyết định-reconciliation / open issues |
| 06 / 07 | Premise core / provenance-độ chắc chắn; trạng thái chấp nhận là trục riêng |
| 10 / 11 | Rongo / cấu trúc tàu |
| 20 / 21 / 22 | Team 25 và ba slot mở / hai hồ sơ nhân vật riêng |
| 110 / 111 | World 1 persistent truth / campaign briefing knowledge |

`FILE NUMBER != MODULE ID != FICTION ENTITY ID`. Mapping module tường minh trong builder, không suy từ thứ tự filename. Dải chục không là quota; không có source lấp số hoặc scenario chưa được nhập.

## Control và bảo trì

[CI 1.0](Project%20Cosmic%20Core%20CI/C2_CI_v1.0.md) gọi [Router 1.0](Anti-Drift%20Source/C2_Anti_Drift_Source_Router_v1.0.json) cho tác vụ phụ thuộc C2 current state. Router pin đường dẫn active local và chọn trong đúng bốn family: MCA, WIL, Actor Reception, Operational Mission. Router dùng JSON chuẩn để checker chạy bằng Python standard library, không thêm dependency. Applicability vẫn do mô hình đánh giá, không phải suy luận tự động bằng tool.

Control ở `Project Cosmic Core CI/` và `Anti-Drift Source/`; checker ở `tools/`, test ở `tests/`. Chúng cùng manifest/builder/archive nằm ngoài namespace đánh số. `Source_Archive/` giữ lịch sử/provenance khi có, không là current fallback hoặc đầu vào tái dựng lore.

Chạy từ thư mục package `Project Cosmic Core/`:

```powershell
python -B build_consolidation.py --check
python -B build_consolidation.py --check-router
python -B -m unittest discover -s tests -v
git diff --check
```

Sau thay đổi current sources được phép, dùng `python -B build_consolidation.py --write`, rồi `--check`. Chỉ vùng generated module catalog trong 00 và metadata/hash trong MANIFEST được ghi; builder không là lore generator, không infer dependency/ownership hoặc giải OPEN/canon. Catalog admission nằm tường minh trong builder; khi nhận source mới phải cập nhật mapping cùng inventory generated đúng tập được duyệt, không tự nhận từ glob. `--write` từ chối inventory sai/tùy tiện thay vì tự cấp admission.

Manifest băm 16 numbered current files; không băm chính nó/control/tooling. `--check-router` kiểm cấu trúc control, không chứng minh ý nghĩa đúng hoặc mô hình tuân thủ. Test dùng bản sao tạm, không sửa nguồn baseline.

## Trạng thái bằng chứng

Local repository khác live GPT Project deployment. Chỉnh file/commit không tự đồng bộ Project Sources/Library hoặc cài CI. `LIVE VERIFIED: NOT RUN`.

Lore chi tiết, family Anti-Drift bổ sung, scenario, Authoring Pipeline và live deployment/verification giữ ngoài milestone này.
