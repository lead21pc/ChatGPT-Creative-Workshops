# Project Feather Core (FTH)

Project Feather Core (`FTH`) là project worldbuilding/paracosm cá nhân, phi thương mại. Tác giả phát triển thế giới với sự hỗ trợ của ChatGPT và Codex; nguồn, Custom Instructions (CI), Router và công cụ kiểm tra giúp giữ nhất quán, truy nguyên quyết định và hạn chế sai lệch khi làm việc với mô hình.

**AetherFire là một quốc gia trong FTH, không phải tên thay thế cho toàn project.** FTH có canon, cấu trúc thế giới và thẩm quyền nguồn riêng; phương pháp dùng chung với The Kingdom hoặc Fanfiction Engine không chuyển canon hay kiến trúc giữa các project.

Đọc [SYSTEM_CONTEXT.md](../SYSTEM_CONTEXT.md) trước, rồi dùng [chỉ mục nguồn](00_AETHERFIRE_CONSOLIDATION_INDEX.md) và [sổ vấn đề hiện hành](92_OPEN_ISSUES_CURRENT.md) để chọn tài liệu theo tác vụ. README này chỉ hướng dẫn đọc và bảo trì; thẩm quyền cụ thể nằm trong nguồn và bộ điều khiển liên quan.

## Cách hiểu nguồn và quyết định

Repository ghi lại một phần thế giới của tác giả, không đại diện cho toàn bộ nội dung đã hình thành trong tư duy tác giả hoặc đang có trong ChatGPT Project. Thiếu thông tin trong file chỉ giới hạn kết luận có thể rút ra từ file đó.

Tác giả quyết định canon. Câu hỏi, bản nháp, phương án thiết kế, suy luận, giả định mô phỏng và đầu ra RP giữ đúng trạng thái của chúng cho tới khi có quyết định chấp nhận trong phạm vi rõ ràng. `UNKNOWN`, `DEFERRED` và `CONFLICTED` phải được giữ mở khi chưa đủ căn cứ giải quyết. Lịch sử và tài liệu đã thay thế chỉ phục vụ truy nguyên hoặc đối chiếu được yêu cầu, không dùng làm nguồn dự phòng để lấp canon.

Số đầu tên file là địa chỉ theo miền, không phải thứ bậc thẩm quyền hoặc quan hệ sở hữu trong thế giới. Tương tự, bảng ánh xạ `AFM-*` giúp tìm nguồn; một hàng trong bảng không tự xác lập canon hay quan hệ phụ thuộc.

## Bản đồ tài liệu

| Vị trí | Vai trò |
| --- | --- |
| [00 — Chỉ mục nguồn](00_AETHERFIRE_CONSOLIDATION_INDEX.md) | Thứ tự đọc, ranh giới miền và ánh xạ mã nguồn sang đường dẫn. |
| Các file `01–06` tại root | Miền chung/xuyên quốc gia: thế giới, công nghệ, metafiction, narrator/POV, căn tính MC4, hàng không/không phận. |
| Các file `10–14` tại root | Hồ sơ AetherFire và các miền chuyên biệt: địa vị/lao động, chính trị/an ninh, Undie và Học viện. |
| Các file `20–23` tại root | Hồ sơ Hoa Nguyệt, văn hóa/ngôn ngữ/trang phục, quốc hiệu/biểu tượng, địa lý/giao thương/đối ngoại. |
| [30 — RF](30_RF_NATIONAL_CANON_CURRENT.md) và [40 — Matriarch's Lament](40_MATRIARCHS_LAMENT_CURRENT.md) | Hồ sơ riêng của từng miền và các giao diện đã được nguồn xác lập. |
| [90 — Lịch sử thiết kế](90_DESIGN_HISTORY_AND_RECONSIDERATIONS.md) | Lịch sử, phương án và nội dung xem xét lại; đọc theo trạng thái được khai báo. |
| [91 — Bản ghi hòa giải](91_RECONCILIATION_RECORD.md) | Quyết định, phạm vi thay thế, nguồn gốc và xung đột liên quan. |
| [92 — Vấn đề hiện hành](92_OPEN_ISSUES_CURRENT.md) | Câu hỏi mở và các trạng thái chưa được chốt. |
| [MANIFEST.md](MANIFEST.md) | Cấu trúc gói, vùng metadata được tạo bằng công cụ và hash của nguồn hiện hành. |
| [Project Feather Core CI/](Project%20Feather%20Core%20CI/) | Chỉ dẫn hành vi của project và kho lưu các phiên bản tiền nhiệm. |
| [Anti-Drift Source/](Anti-Drift%20Source/) | Source Router, Authoring Pipeline và các bộ quy tắc chống sai lệch theo tác vụ. |
| [RP Module/](RP%20Module/) | Bộ điều khiển RP v0.1 phục vụ thử nghiệm local; có điều kiện bật riêng. |
| [Source_Archive/](Source_Archive/) | Lưu nguyên liệu lịch sử/nguồn gốc; không phải đầu vào tái dựng nguồn hiện hành. |
| [tests/](tests/) | Kiểm tra bảo trì gói và các phép kiểm điều khiển trong repository. |
| [tools/legacy/](tools/legacy/) | Công cụ bảo trì cũ; điểm vào bảo trì hiện hành là `build_consolidation.py`. |

Các nguồn đánh số tại root được duy trì trực tiếp. Công cụ bảo trì kiểm tên và vị trí của chúng; không coi chúng là đầu ra tạm có thể xóa rồi tái tạo từ archive.

## Bộ điều khiển hiện hành

Trạng thái dưới đây được khai báo trong các file local, không phải xác nhận cấu hình đang cài trong ChatGPT Project.

| Thành phần | Bản local | Trách nhiệm |
| --- | --- | --- |
| CI | [FTH CI 3.4](Project%20Feather%20Core%20CI/FTH_CI_version_v3.4.md), khai báo nền ChatGPT 8.9 | Hành vi, thao tác/giai đoạn được yêu cầu, quyền tác giả và điều kiện vào Router/Pipeline. CI tự chứa quy tắc cần dùng; khai báo nền không tạo thêm phụ thuộc đọc lúc chạy. |
| Source Router | [FTH Router 5.0](Anti-Drift%20Source/FTH_Anti_Drift_Source_Router_v5.0.yaml) | Định tuyến nguồn/thẩm quyền, điều kiện nạp, phụ thuộc, hòa giải và lựa chọn quy tắc chống sai lệch. |
| Authoring Pipeline | [Pipeline 1.1](Anti-Drift%20Source/FTH_Authoring_Pipeline_v1.1.md) | Biến đổi đầu vào theo thao tác được yêu cầu: rút hạt nhân ý tưởng, phân rã thành phần, so sánh, bản địa hóa hoặc đề xuất triển khai; giữ đúng điểm dừng. |

Theo hợp đồng CI, tác vụ phụ thuộc trạng thái FTH hiện hành phải đọc đầy đủ Router và qua các bước nạp nguồn/kiểm tra liên quan trước khi thực hiện. Router yêu cầu đọc đầy đủ `00` và `92` khi khởi đầu; đọc `91` khi xung đột, thay thế, ưu tiên, nguồn gốc hoặc phụ thuộc có thể quyết định tác vụ. Sau đó chọn nguồn theo miền cần xử lý và hợp đồng nạp của Router.

Pipeline chỉ áp dụng khi yêu cầu có thao tác biến đổi thuộc phạm vi của nó; tra cứu, audit hoặc RP thông thường không tự kích hoạt Pipeline. Bộ quy tắc chống sai lệch được chọn theo tác vụ qua Router, không nạp tất cả chỉ vì cùng thư mục. Thay đổi được chấp nhận phải được ghi vào nguồn hiện hành và bản ghi quyết định phù hợp trong đúng phạm vi được phép.

CI tiền nhiệm và Router 4.4 đã được lưu trong archive điều khiển. Pipeline 1.0 còn ở thư mục trực tiếp để phục vụ quay lui; sự hiện diện của nó không làm thay đổi bản 1.1 được CI hiện hành chỉ định.

## RP v0.1: bản nền thử nghiệm local

[RP Router 0.1](RP%20Module/FTH_RP_Router_v0.1.yaml) chọn, định vị và kiểm nguồn hướng dẫn thể hiện nhân vật; [RP Runtime 0.1](RP%20Module/FTH_RP_Runtime_v0.1.md) điều khiển phân vai, tri thức nhân vật, nhịp lượt và tính liên tục của cảnh trong chat hiện tại. Hai thành phần sử dụng các bước kiểm tra nguồn/điều khiển FTH có sẵn và không có quyền chốt canon hoặc giải quyết điều chưa rõ.

Chỉ bật khi người dùng yêu cầu rõ module RP và cả hai file điều khiển đã được đọc đầy đủ (`FULL_FILE`). Một yêu cầu RP thông thường không tự bật bản thử nghiệm này. Khi tắt, module không thêm yêu cầu nguồn hay điều khiển vào luồng FTH thông thường.

Danh mục trong RP Router hiện là `catalog: []`; chưa có vị trí Library của nguồn RP nào được xác nhận trong danh mục. Nguồn thể hiện nhân vật dùng lúc chạy phải có vị trí Library và phạm vi sử dụng đã được xác nhận, được đọc đầy đủ và kiểm header theo Router. Bản sao repository, fixture và Memory không thay thế được nguồn đó. Nhân vật không có nguồn RP áp dụng hoặc bắt buộc có thể dùng yêu cầu người dùng, ngữ cảnh chat và nguồn thế giới đã qua định tuyến; nguồn bắt buộc bị thiếu vẫn chặn phần thể hiện phụ thuộc.

Đầu ra cảnh giữ trạng thái phi canon cho tới khi tác giả chấp nhận rõ. Tính liên tục trong chat không tạo kho trạng thái xuyên chat; tài liệu local và phép kiểm cấu trúc chưa chứng minh truy xuất Library hay hành vi RP thực tế.

## Bảo trì và kiểm chứng

Từ thư mục `Project Feather Core`, chạy kiểm tra chỉ đọc:

```powershell
python -B build_consolidation.py --check
```

Công cụ kiểm header, ánh xạ catalog, tham chiếu chéo và hash nguồn hiện hành. `--write` chỉ cập nhật vùng catalog được tạo bằng công cụ trong `00` và vùng metadata/hash tương ứng trong manifest; chỉ dùng khi thay đổi được phép cần đồng bộ các vùng này, rồi chạy lại `--check`. Công cụ không tái dựng lore từ archive hoặc tự phê duyệt canon. File PowerShell đồng hành vẫn được giữ tại root.

Đọc [hướng dẫn kiểm hồi quy điều khiển](tests/control-regressions/README.md) trước khi dùng runner. Phân biệt trạng thái case, neo nguồn, kiểm tra cấu trúc, thử ngữ nghĩa và bằng chứng chạy thực tế; kết quả cấu trúc không tự kích hoạt case hay chứng minh mô hình tuân thủ.

Chỉnh file, commit Git, đồng bộ Library, cài chỉ dẫn vào ChatGPT Project và quan sát hành vi thực tế là các bước riêng. Chỉ báo đã kiểm chứng đúng lớp bằng chứng đã thực hiện; kết quả kiểm tra repository không xác nhận các bước còn lại.
