# Kế hoạch phát triển Fiction and Worldbuilding Engine

[Kiến trúc FWE](FWE_ARCHITECTURE.md) xác định quyền và trách nhiệm; tài liệu này xác định thứ tự phát triển, tiêu chí, phép thử và cách quay lui. Mục tiêu là một bộ FWE dùng ổn định cho việc sáng tác cá nhân, không phải một lần phát hành công cộng.

## Trạng thái và quyền thực hiện

Mỗi mốc dùng `PLANNED`, `ACTIVE`, `PASS` hoặc `BLOCKED`. Đây là trạng thái phát triển, không phải trạng thái khi chạy. Chỉ mở mốc khi có quyền phù hợp; quyền thiết kế, sửa local, cài/thử Project và thao tác Git tách biệt. `PASS` một mốc không cho phép bắt đầu mốc tiếp theo.

| Mốc | Trạng thái | Bằng chứng hiện có |
|---|---|---|
| M0 — Foundation | PASS | STRUCTURAL_PASS và STATIC_SEMANTIC_PASS cho ba tài liệu nền; đã rà M0-A–F. Chưa có bằng chứng runtime. |
| M1 — CI nền | PASS | `STRUCTURAL_PASS` và `STATIC_SEMANTIC_PASS` cho [CI v0.1](source_archive/controls/FWE_CI_v0.1.md); đã rà C1–C15 và các ca phủ định. Chưa xác minh khi chạy. |
| M2 — Hợp đồng nguồn + Router | PASS | `STRUCTURAL_PASS` và `STATIC_SEMANTIC_PASS` cho [Hợp đồng nguồn](source_archive/source_management/FWE_SOURCE_CONTRACT.md) và [Router v0.1](source_archive/controls/FWE_ROUTER_v0.1.md) cùng tham chiếu từ CI; đã rà S1–S8, R1–R10, E1–E3 và các ca xung đột thẩm quyền. Chưa có bằng chứng định tuyến hay truy xuất khi chạy. |
| M3 — Ứng viên Brainstorm | PASS | `STRUCTURAL_PASS` và `STATIC_SEMANTIC_PASS` cho [Brainstorm v0.1](source_archive/capabilities/FWE_BRAINSTORM_v0.1.md), tích hợp Router và chuẩn hóa lớp điều khiển sang tiếng Anh. Đã rà B1–B4, BN1–BN5, hồi quy M1–M2, ranh giới thẩm quyền, khả năng chuyển lõi và điểm mở rộng M4. Chưa chạy đối chứng. |
| M4–M10 | PLANNED | Các mốc dự kiến của kế hoạch v0.1, chưa triển khai. |

Bộ hiện hành gồm [CI v2.0](controls/FWE_CI_v2.0.md) và [Router v2.0](controls/FWE_ROUTER_v2.0.yaml), cả hai ACTIVE / STATIC PASS trong repository. Router có bốn tuyến `SOURCE`, `EVIDENCE`, `PROFILE`, `CONTROL`. Chưa có liên kết AIS, quyền hoặc liên kết Profile riêng cho FWE, hay liên kết kiểm soát chọn lọc. Người dùng xác nhận ngày 2026-11-24 rằng bộ điều khiển hiện hành đã được cài và đang chạy. INSTALLED: USER-REPORTED. LIVE ACTIVE: USER-REPORTED. INDEPENDENT LIVE VERIFICATION: NOT RUN. Báo cáo này không xác nhận mọi probe hoặc hồi quy đã đạt. Các mốc và phép đối chứng v0.1 dưới đây được giữ làm hồ sơ của bộ tiền nhiệm.

Khi một ca lỗi, ghi đó là lỗi đã quan sát, đã tái hiện, rủi ro có căn cứ hay giả thuyết. Chẩn đoán và mở lại đúng phần bị ảnh hưởng; giữ các kết quả độc lập. Một phát hiện không cấp quyền thiết kế lại hoặc sửa ngoài phạm vi.

## Các mốc và điều kiện chuyển

| Mốc | Mục tiêu, phụ thuộc và đầu ra | Chấp nhận và điều kiện chuyển | Nếu không đạt; phần chưa chứng minh |
|---|---|---|---|
| **M0 — Foundation** | Sau Phase A–E, tạo đúng README, kiến trúc và kế hoạch ở gốc FWE để chốt phạm vi trước khi viết control. | Kiểm cấu trúc và ngữ nghĩa ba tài liệu; rà M0-A–F; giữ nguyên archive FSP. Đạt mới đủ cơ sở giao M1. | Sửa hồ sơ sai hoặc dừng nếu chồng phạm vi. Chưa có control hay runtime. |
| **M1 — CI nền** | Sau M0, tạo CI tự chứa và ca rà tương ứng, chưa bắt phải có Router để viết thường. | Kiểm cấu trúc và ngữ nghĩa: viết trực tiếp, quyền giữ đúng chỗ, trạng thái nhánh/đề xuất không tăng cấp, nhận diện được lõi chung. Đủ rồi mới giao M2. | Sửa CI nếu cản sáng tác hoặc kéo ontology FWE vào lõi. Chưa chứng minh hành vi mô hình. |
| **M2 — Hợp đồng nguồn + Router** | Sau M1, tạo hợp đồng nguồn, Router Markdown và tham chiếu CI tối thiểu. Chốt vai trò nguồn trước khi Router dựa vào chúng. | Kiểm cấu trúc và ngữ nghĩa: Router nhận phần việc đã giao, không đổi thao tác; nguồn không tự có quyền; thiếu điều kiện chỉ chặn phần phụ thuộc. Đủ để nối các ứng viên. | Thu hẹp Router; nếu tệp nguồn riêng không thêm giá trị, giữ quy tắc nguồn tối thiểu trong CI. Chưa kiểm truy xuất thật. |
| **M3 — Ứng viên Brainstorm** | Sau M2, tạo ứng viên và chuẩn bị hai cấu hình đối chứng, ca B1–B4. Tách phần kỹ thuật khỏi phần viết thường. | Kiểm cấu trúc và ngữ nghĩa bộ thử: thao tác ở đúng nhánh, đáp án nền vẫn sử dụng được, so cùng điều kiện. Sẵn sàng để thử tại M7. | Sửa hoặc rút ứng viên sai hợp đồng. Không giữ thành phần riêng chỉ vì kiểm tĩnh đạt; chưa có giá trị khi chạy được chứng minh. |
| **M4 — Hai cấu hình Anti-Prior** | Sau M2; dùng M3 cho ca phối hợp. Chuẩn bị A là quy tắc trong CI, B là control theo phần việc; tệp Anti-Prior riêng chỉ thuộc B. | Kiểm cấu trúc và ngữ nghĩa: giữ nguyên quyền sáng tác, các biến ngoài vị trí áp dụng và cả hai nhóm ca giảm tự lấp/giữ tự do. Sẵn sàng thử tại M7. | Sửa cách so hoặc ngữ nghĩa nếu kiểm soát bị lặp hay cấm sáng tác. Chưa chọn A hay B theo hiệu quả khi chạy. |
| **M5–M6 — Tích hợp và hồi quy tĩnh** | Sau M2–M4, lập bộ tương thích để thử, rà ca hỗn hợp, ca nguồn và ca thiếu điều kiện. Gộp tích hợp với kiểm tĩnh vì dùng cùng bộ tệp và cùng mốc quay lui. | Kiểm cấu trúc và ngữ nghĩa: không chồng quyền, không tự chọn lẫn nhau, đường trực tiếp còn nguyên, không giả đã làm phần bị thiếu. Chỉ ghi kiểm mô phỏng nếu đã chạy bộ thử. | Mở lại trách nhiệm gây lỗi; giữ kết quả độc lập. Chưa biết Project đọc, chọn hay thực hiện đúng. |
| **M7 — Thử trên ChatGPT Project** | Sau M5–M6 và khi được phép cài/thử riêng. Ghi bộ tệp đã cài, kiểm đường trực tiếp và truy xuất, thử riêng Brainstorm và Anti-Prior, thử phối hợp trên bộ được chọn. | Cần bằng chứng live theo ca. Brainstorm: giữ, sửa hoặc đưa về nền. Anti-Prior: giữ A, chọn B hoặc sửa ngữ nghĩa. Kiểm lại ca chịu ảnh hưởng trên đúng bộ cuối trước M8. | Nếu không đủ quyền, nguồn hoặc bằng chứng, không chốt phần tương ứng. Rút cấu hình lỗi hoặc thử lại phương án đơn giản hơn. Chưa chứng minh hữu dụng trong việc thật nhiều lượt. |
| **M8 — Thử ngữ cảnh thật** | Sau M7, thử bộ được chọn trên chuỗi sáng tác có chỉnh tiền đề và việc phát triển thế giới có ranh giới nguồn rõ. | `REAL_CONTEXT_PASS` và xác nhận người dùng trong phạm vi: văn xuôi hữu dụng, không kéo chế độ sang lượt sau, chỉ cập nhật phần phụ thuộc, không tự nhận canon. Đủ workflow thật để làm M9. | Khoanh vùng hồi quy; quay về bộ tương thích từng được thử nếu có. Không suy bao phủ mọi thể loại. |
| **M9 — Skill bảo trì** | Sau M8, tạo `fwe-development` khi đã có control và quy trình thật. Skill cần có trước mốc ổn định, không cần cho khởi tạo. | Kiểm tĩnh và diễn tập: tìm đúng bộ hiện hành, phân vai nguồn, chọn hồi quy và xử lý một thay đổi bên ngoài đúng quyền. Skill không thay CI, Router, Git hoặc cấp quyền. | Dùng quy trình thủ công có ghi chép trong lúc sửa; chưa chốt ổn định. Skill không chứng minh hành vi khi chạy. |
| **M10 — Mốc ổn định cá nhân** | Sau M7–M9, đối chiếu bộ tương thích đã cài với bằng chứng, skill và cách khôi phục. Không thêm tính năng để đóng mốc. | Đạt mọi điều kiện ổn định bên dưới trên cùng bộ tệp. Kiểm lại phần chịu ảnh hưởng nếu bộ đã đổi. | Thiếu bằng chứng trọng yếu thì giữ bản thử hoặc mốc ổn định trước nếu có. Không chứng nhận LitRPG hoặc bao phủ toàn miền. |

### Rà ngữ nghĩa nền M0

| Ca | Kỳ vọng từ kiến trúc |
|---|---|
| M0-A — “Viết cảnh này” với bối cảnh tự đủ | CI cho thực hiện trực tiếp, không bắt Router. |
| M0-B — “Đảo giả định rồi mở ba nhánh” | CI xác định thao tác và phạm vi; Router có thể chọn ứng viên Brainstorm, không đổi yêu cầu. |
| M0-C — Vampire phù hợp setting | Có cách thử Anti-Prior mà vẫn sinh nội dung và giữ trope được giao. |
| M0-D — Thiếu nguồn hiện hành quyết định kết luận | Giới hạn hoặc dừng phần phụ thuộc; làm tiếp phần độc lập. |
| M0-E — Cảnh sinh từ bối cảnh FTH | Cảnh là chất liệu làm việc, không thành canon FTH. |
| M0-F — Xem xét chuyển cho LitRPG | Nhận diện được lõi chung mà không cần lấy Brainstorm, Anti-Prior hay cây tệp FWE. |

## Kế hoạch thử các ứng viên

Dùng cùng mô hình, môi trường, prompt, bối cảnh, quyền sáng tác, nguồn và cấu hình ngoài biến đang thử. Dùng chat độc lập, trừ ca kiểm nhiều lượt; ghi bộ tệp, thứ tự thử, khả năng truy xuất và kết quả theo ca. Trước khi chạy, chốt ngưỡng cải thiện và số lượt hữu hạn; đề xuất ít nhất ba cặp độc lập cho ca quyết định. Đây là đối chứng thực dụng, không suy thành tỷ lệ lỗi chung. Lỗi không chọn, chọn sai, không truy xuất và đã đọc nhưng làm sai cần ghi riêng.

### Brainstorm: nền so với nền + thành phần

| Ca | Kiểm |
|---|---|
| B1 — Phát triển vài hướng cho quán sách mở khuya | Nền làm trực tiếp; thành phần không làm nảy ý thường trở nên nặng. |
| B2 — Đảo điều kiện thu tiền từ bán sách, mở ba mô hình | Khác cơ chế, nguồn lực, ràng buộc, quan hệ hoặc hệ quả; không chỉ đổi tên. |
| B3 — Thay một tiền đề, truy hệ quả bậc hai | Cho thấy hệ quả trực tiếp dẫn tới thay đổi tiếp theo; không chỉ liệt kê kết quả song song. |
| B4 — Mở hai nhánh rồi viết đoạn cho nhánh 2 | Brainstorm mở nhánh, nền viết. Không chấp nhận nhánh hoặc giữ chế độ qua lượt. |

Giữ thành phần nếu lợi ích chuyên biệt ở B2/B3 lặp lại, B1/B4 còn hữu dụng và không tăng cấu trúc thừa hay tự chốt nhánh. Nếu không, sửa có căn cứ hoặc đưa thao tác hữu ích về nền.

### Anti-Prior: quy tắc CI A so với control theo phần việc B

Giữ Brainstorm cố định trong từng cặp, kể cả nếu thao tác được thực hiện qua nền. B không đồng thời chứa quy tắc Anti-Prior đầy đủ của A. Chấm cả lỗi tự lấp và sức sáng tác, yêu cầu làm rõ không cần, dấu hiệu kiểm soát lộ ra, sai phạm vi, truy xuất thừa và độ trễ nếu đo được.

| Ca giảm tự lấp | Kiểm |
|---|---|
| AP1 — Vampire phù hợp setting | Không tự lấy nguyên gói trope làm tiền đề. |
| AP2 — Kiến trúc trắng, ánh vàng, biểu tượng mặt trời | Không suy ra thần quyền, thiện tính hay phép mặt trời. |
| AP3 — Knight | Không tự suy danh dự, tôn giáo, huyết thống hay trung thành. |
| AP4 — Dùng năng lực có nguồn gốc được giữ chưa biết | Dùng hành vi đã biết; không giải nguồn gốc. |
| AP5 — Ba mô hình phải khác cơ chế | Không để cả ba mang cùng một cơ chế mặc định chưa được giao. |

| Ca bảo vệ sáng tạo | Kiểm |
|---|---|
| AF1 — Vampire Gothic, quý tộc, sống lâu, săn máu đêm | Giữ các đặc tính đã giao. |
| AF2 — Tạo nền văn minh từ đầu | Tự chọn tiền đề lớn và viết được; không hỏi từng khoảng trống. |
| AF3 — Academy battle shounen theo lối quen | Dùng convention đã yêu cầu, không cố đảo trope. |
| AF4 — Căn phòng tối sau trận chiến | Viết cảnh tự nhiên, không chèn báo cáo kiểm soát. |
| AF5 — Đề xuất ba nguồn gốc | Tạo đủ đề xuất cho khoảng đã giao, không công nhận nguồn gốc nào. |

Chọn B chỉ nếu giảm tự lấp đáng tin hơn A mà không làm suy giảm đáng kể quyền sáng tác hay tăng chi phí. Giữ A khi tương đương, hoặc khi A đã đạt và chưa có bằng chứng B tốt hơn. Nếu cả hai cản sáng tạo hoặc cùng lọt lỗi có hệ quả, chẩn đoán rồi sửa ngữ nghĩa trước khi chốt.

### Định tuyến, nguồn và phối hợp

Kiểm đường trực tiếp bằng cảnh gặp lại sau 20 năm; sau đó kiểm Router chọn riêng Brainstorm, riêng Anti-Prior B, cả hai, chỉ nguồn và nguồn cùng đóng góp. Kiểm thiếu Router, thiếu thành phần đã chọn và thiếu nguồn quyết định. Phần phụ thuộc phải giữ có điều kiện hoặc dừng; phần độc lập tiếp tục và không giả đã làm chuyên biệt. Không thay một quy trình phối hợp thất bại bằng package system khi chưa chỉ ra lỗi và sửa tối thiểu.

Dùng các đối chứng nguồn: bối cảnh đã đủ nên không tra ngoài; tệp hiện hành được giao nên dùng đúng phạm vi; nguồn quyết định thiếu nên không khẳng định trạng thái đích; archive chỉ cho lịch sử; cảm hứng từ FTH phải tách cơ chế khỏi lore/quyền/phụ thuộc. Kiểm lại đường sáng tác thường sau khi phối hợp. Không suy “không gọi Router” từ việc câu trả lời không in nhãn.

Router Markdown thuộc bộ v0.1. Cặp v1.0 là [bản lưu](source_archive/controls/). Cặp v2.0 giữ Router YAML và đã qua kiểm hợp đồng tĩnh cho đường sáng tác trực tiếp, phát triển cùng tiền đề, thiếu nguồn, thiếu AIS và phụ thuộc phát sinh giữa chừng (P1–P5). Việc thử các ca này trên ChatGPT Project chưa diễn ra trong đợt này.

## Mức bằng chứng

| Loại | Lời khẳng định được phép |
|---|---|
| `STRUCTURAL_PASS` | Tệp, định danh và tham chiếu nhất quán trong phạm vi kiểm. |
| `STATIC_SEMANTIC_PASS` | Trách nhiệm và hành vi dự kiến nhất quán trong các ca rà trên văn bản. |
| `SIMULATED_FLOW_PASS` | Một bộ thử đã chạy và xử lý đúng luồng mô phỏng trong ca đã thử; không xác nhận mô hình tự chọn đúng. |
| `LIVE_PROJECT_PASS` | Quan sát được hành vi của bộ tệp đã cài trong Project ở ca cụ thể. Chỉ khẳng định truy xuất nếu có căn cứ tương ứng. |
| `REAL_CONTEXT_PASS` | Bộ tệp hoạt động trong công việc hư cấu thực tế nhiều lượt đã ghi; không chứng minh mọi thể loại. |
| `USER_CONFIRMED_PASS` | Người dùng xác nhận kết quả trong đúng bộ, môi trường và ca đã thử. |

Mỗi bản ghi nêu bộ tệp, mốc hoặc commit nếu có, môi trường, ca và kết quả, phần chưa quan sát được và cách xác nhận. Kiểm tĩnh không phải kiểm hành vi live; đạt live không mang hiệu lực phổ quát. Chỉ mở lại những kiểm tra bị ảnh hưởng khi có thay đổi.

## Quay lui, bảo trì và mốc ổn định

Git giữ lịch sử và bộ tệp tương thích. Trước khi có bằng chứng live, một revision kiểm tĩnh chỉ là mốc khôi phục tệp, không phải mốc runtime tốt. Khôi phục repository và bộ đã cài là hai việc riêng. Không archive mỗi revision; chỉ lưu riêng khi cần provenance nguyên byte, lịch sử tiếp tục tham chiếu hoặc phục hồi mà Git không thể biểu đạt đủ. Archive FSP giữ vị trí lịch sử.

Lối lùi theo phần: đưa Brainstorm hữu ích về nền nếu thành phần không thêm giá trị; từ B về A khi A chấp nhận được; thu hẹp Router về ủy quyền chuyên biệt; hợp nhất ranh giới nguồn vào CI nếu tệp riêng không có ích; dùng bảo trì thủ công khi skill chưa sẵn sàng. Nếu thiếu một thành phần quyết định, không gán nhãn thành công cho bản nền thay thế.

Skill hỗ trợ đọc đúng bộ hiện hành, bảo trì control, phân vai nguồn, xét mốc và bằng chứng, chọn hồi quy và xác minh thay đổi được phép. Khi có tin dự án ngoài thay đổi: đọc đúng nguồn hiện hành, xác định lỗi và chi phí địa phương, so với FWE, rồi phân loại đã bao phủ, tham khảo hữu ích, có thể là khoảng trống, xung đột hoặc không liên quan. Chỉ đề xuất sửa tối thiểu có căn cứ; không tự đồng bộ hay cấp quyền sửa.

**FWE STABLE PERSONAL BASELINE** chỉ được ghi cho cùng một bộ tệp tương thích khi CI và đường viết trực tiếp, quyền được giao của Router và ranh giới nguồn đã qua kiểm live; đã quyết định Brainstorm và Anti-Prior; hồi quy hỗn hợp đạt; đã thử nhiều lượt trong việc thật và người dùng xác nhận đúng phạm vi; bộ đang cài và đường lùi được ghi; skill bảo trì hiện hữu; ranh giới lõi chung vẫn nhận diện được. Không yêu cầu hết điều chưa biết, mọi thể loại, đủ anti-drift tương lai, phát hành công cộng hay chuyển LitRPG.

## Khả năng chuyển và giới hạn mở rộng

M1 rà ranh giới trong CI; M2 rà hợp đồng giao việc; mỗi sửa đổi sau đó chạm kernel phải rà lại trước khi đạt; M10 kiểm lại trên bộ cuối. Không đưa ontology FWE hoặc phụ thuộc vào control riêng vào lõi chung. Chỉ mở audit LitRPG riêng sau khi có mốc FWE ổn định và nguồn, yêu cầu, trạng thái lineage thực tế của LitRPG. Không lấy The Kingdom hiện tại làm bản thay thế và không lập mốc migration ở đây.

Chỉ mở control mới khi lỗi đã quan sát hoặc tái hiện, chủ thể hiện tại xử lý không đủ, và phần mới có trách nhiệm riêng có thể kiểm. Theo dõi nhưng chưa triển khai hai nhóm: hành động của nhân vật thiếu thông tin/quyền/năng lực, và truy hệ quả sai hoặc chọn kết cục trước rồi dựng ngược nguyên nhân.
