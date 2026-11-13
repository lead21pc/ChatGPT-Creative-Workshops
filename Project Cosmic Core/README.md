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

## Dùng CI trên ChatGPT web

Dán nội dung CI vào phần chỉ dẫn Project không tự tải Router hoặc các source từ máy/GitHub. Cung cấp Router `C2_Anti_Drift_Source_Router_v1.0.json`, bốn control và các current source cần dùng qua Project Sources hoặc file Library được gắn vào chat. Đây là bước cài đặt nguồn, tách khỏi commit/push.

CI yêu cầu tìm Router theo tên tài liệu, xác minh identity/version và đọc đầy đủ; Router chọn nguồn/control tiếp theo qua nguồn thực sự có sẵn. Path tương đối và quy tắc thư mục trong JSON chỉ phục vụ bảo trì local. Tên trùng không đủ xác lập authority; thiếu, mơ hồ hoặc chỉ lấy được một phần tài liệu thì chặn phần phụ thuộc và yêu cầu file. `FULL_FILE` là yêu cầu đọc, không phải bảo đảm backend luôn cung cấp đủ nội dung. Chưa có lần kiểm chứng live nào được thực hiện.

## Thử nghiệm cổng thực thi C2

Harness thử nghiệm trong `tools/runtime_probe.py` nhận đề xuất route và đánh giá ngữ nghĩa qua hai callback. Code giữ quyền mở `PROMPT_EXECUTION`, còn adapter cục bộ trả nội dung file cùng bằng chứng đọc tới EOF. Harness đối chiếu 00/05 và nguồn được chọn với cùng bộ hash trong manifest, kiểm header và mở rộng phụ thuộc theo Router. Bộ hash cố định cho lượt thử, chỉ xác nhận nội dung khớp snapshot và không cấp thẩm quyền canon. CI ngữ nghĩa được caller gắn trước lượt thử. Harness xử lý một lượt phụ thuộc C2 theo chế độ chỉ đọc. Với nguồn stale hoặc thiếu điều kiện quyết định, harness dừng để xem xét, chưa thử nhánh phục hồi của Router.

Từ thư mục C2, chạy bộ test và xuất hai đầu vào cho cùng một tình huống. Đổi `mission` thành `lookup`, `mca` hoặc `reception` để xem các tình huống còn lại.

```powershell
python -B -m unittest discover -s tests -p test_runtime_probe.py -v
python -B -m tests.test_runtime_probe mission packet
python -B -m tests.test_runtime_probe mission raw
```

Hai đầu vào dùng cùng văn bản nguồn, chỉ dẫn hành vi và các Anti-Drift đã chọn. Bản `raw` cho model thấy mã, config, metadata và đề xuất ngữ nghĩa. Bản `packet` chuyển giao kết quả các cổng cùng giới hạn kết luận. Kịch bản dùng callback cố định để kiểm flow, không đánh giá độ chính xác khi model tự chọn nguồn, phân xử conflict hay viết câu trả lời. Cần so A/B bằng cùng model và cùng câu hỏi, chấm độc lập theo thẩm quyền, phạm vi, tri thức actor, trạng thái UNKNOWN và quyền canon. Sau đó mới kiểm native retrieval bằng lượt thực trên host có thể cung cấp bằng chứng đọc. `LIVE VERIFIED: NOT RUN`.
