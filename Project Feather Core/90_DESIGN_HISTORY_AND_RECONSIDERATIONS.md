# Project Feather Core — Lịch sử thiết kế

Tài liệu giải thích quá trình thiết kế FTH và các chức năng được giữ qua những lần đổi cấu trúc. Hồ sơ quyết định và nguồn gốc ở [91](91_RECONCILIATION_RECORD.md), việc còn mở ở [92](92_OPEN_ISSUES_CURRENT.md), chi tiết thiết kế đã rút ở [93](93_SUPERSEDED_IDEAS.md). Mỗi mô-đun hiện hành giải thích miền của mình.

## Từ RP tới nhiều tuyến thể chế

FTH phát triển từ RP xoay quanh MC2 và các tương tác xã hội, nghề, quyền lực và an ninh. Việc các lần chơi và ghi chép tập trung vào MC2 và Undie làm những miền này được mô tả sâu sớm hơn. Tác giả vẫn phát triển địa chính trị, thiết chế và nhân quả độc lập ở hậu cảnh. Sai lệch xuất hiện khi người đọc dùng tần suất ngoại hóa làm bằng chứng rằng mọi miền đều phụ thuộc Undie hoặc nhân vật chính.

Một nút khó là nhiều cơ chế cùng đẩy nhân vật về một chuỗi thử thách duy nhất. Càng hoàn thiện các hệ thống ban đầu theo hướng đó, càng ít chỗ để tác nhân có quyết định riêng hoặc thể chế gặp ma sát thực. Cách thiết kế về sau tách các tuyến truyện, giữ chênh lệch về thông tin, quyền và năng lực, rồi chỉ nối các tuyến qua quan hệ có căn cứ. Hướng này vẫn cho phép tương tác nghề, chính trị và thân phận cùng tạo áp lực trong một tuyến. Các miền thế giới và POV hiện do `01` và `04` giữ.

## Civil, Undie và POW

Trong thiết kế ban đầu, cùng một cấu trúc địa vị và nhận diện gánh nhiều chức năng. Nó cung cấp các điểm tiếp xúc giữa những nhóm chịu áp lực khác nhau, tạo đầu mối phản kháng và nối chúng với phân công lao động. Cấu trúc dùng chung kéo các nhóm về cùng một cách vận hành, dù lý do tồn tại khác nhau. Chẳng hạn, gán cùng một công cụ hạ nhục cho POW làm hỏng chức năng cần một số người có chuyên môn và khả năng hành động. Phần có giá trị là khả năng có nhiều nguồn bất mãn, tiếp xúc và hậu quả chính trị độc lập.

Cơ sở Civil sau thiết kế lại giữ nhu cầu ổn định cá nhân và điều phối nhân lực. Đầu vào tự nguyện đi cùng xét năng lực tiếp nhận, nghĩa vụ làm công việc phù hợp sau khi được nhận, và đường khiếu nại hoặc rời đi. Việc dỡ khuôn địa vị cũ cho phép giữ các công cụ vận hành như pool phân công, reserve và phân công lại trong phạm vi tương thích. Sự thay đổi cũng giữ các luật độc lập về POW, Criminal và Yellow. Vòng đời Civil thuộc `11` và phạm vi quyết định ở `91` AF-CR-001–012.

Undie từng vừa là nơi các tuyến thất bại hội tụ, vừa gánh hoạt động nghề và giao diện thị trường. Khi phạm vi nghề và thế giới rộng hơn, việc gắn các vai trò ấy vào một thang địa vị làm một thay đổi cục bộ kéo theo nhiều hệ quả ngoài miền. Thiết kế về sau giữ chuyên môn, môi giới, giao diện công nghệ, di chuyển và phản ứng xã hội có thể khác nhau theo môi trường, trong khi tách nghề khỏi địa vị và cưỡng chế mặc định. Undi giữ yêu cầu công năng và dấu ấn thiết kế mà không cần đồng phục định hạng chung. `13` quản lý nghề, `02` quản lý các chức năng công nghệ được sử dụng qua giao diện riêng.

### Các yêu cầu địa phương từng bị gộp vào nghề

Barrier và giao thông riêng từng giải bài toán cho người hành nghề di chuyển rộng trong khi giữ những điểm đến có quyền truy cập riêng. Chi phí di chuyển và vật tư làm cho giờ làm, giá dịch vụ và thu nhập thực có thể lệch nhau. Một thiết kế mặc định dùng thuốc kích thích để tăng hiệu suất làm yếu chính bài toán lịch làm, chuyên môn, khách phù hợp và hồi phục. Chức năng kinh tế có thể được xem xét riêng khi nó ảnh hưởng lựa chọn trong một cơ chế đã xác lập.

Chợ đen bắt đầu từ một kẽ hở dịch vụ nằm ngoài kênh chính thức. Giá trị thiết kế là chỗ mà một kênh linh hoạt hơn có thể đổi lấy rủi ro, mức bảo vệ và quyền quy trách nhiệm khác. Một phương án xử lý tử vong cũ đẩy quá xa theo hướng xóa dấu vết qua thủ tục, khiến bạo lực và trách nhiệm mất đường đi tới người có thể phản ứng. Những yêu cầu về thông tin, điều tra và hậu quả gia đình còn ý nghĩa độc lập với cách xử lý cũ.

## Tuyến MC2 và hai cách hiện thực hóa

Các tuyến tiền nhiệm từng thử dùng thay đổi địa vị làm đường đưa MC2 ra khỏi trung tâm quyền lực, rồi dùng môi trường mới tạo rủi ro, quan hệ và quyền tiếp cận. Điều đáng giữ là lựa chọn của nhân vật có thể thay đổi nơi cô tiếp cận thông tin, người bảo trợ và các áp lực. Khi cơ chế cũ chọn sẵn phần giữa, các thiết chế trở thành các trạm đẩy cô qua đúng một kết cục. Tuyến Học viện duy trì sự tách khỏi trung tâm cung đình trong một miền có chức năng riêng. Việc cô có thể tiếp xúc Undie về sau còn là câu hỏi riêng. `03`, `12` và `14` giữ các mệnh đề đã chốt trong phạm vi của mình.

Ở tuyến MC1, ý tưởng dùng quan hệ song sinh từng giảm gánh nặng giải thích việc đi vào thế giới. Nó đồng thời buộc lối vào gắn với huyết thống, địa vị hoàng gia và địa điểm. Một cách triển khai khác cho MC1 dùng thư viện và fiction lồng nhau dưới nhiều hạn chế tạo căng thẳng cục bộ, nhưng khả năng tiến bộ ít làm tăng quyền tự quyết khi cả tuyến vẫn bị khóa. Thiết kế hiện hành giữ việc tiếp cận fiction lồng nhau ở phạm vi năng lực đã chốt. Với MC3, bài toán là lối vào có giới hạn về thông tin và đủ lý do tương tác. Gắn toàn bộ điều kiện vào nghề và cơ chế kiểm soát người khiến một tác nhân cần tác động quỹ đạo trở nên quá dễ dự đoán đối với hệ chủ.

Mô hình hai dòng song song từng giúp phác ra hai quỹ đạo phát triển, nhưng làm mờ điểm xuất phát chung và hai cách thế giới được hiện thực hóa. Thiết kế về sau dùng bản thảo làm tổ tiên nhân quả chung, giữ khác biệt giữa viết tiếp và lịch sử sống, rồi đặt điểm giao vào một điều kiện cụ thể. Proof of Concept vẫn có vai trò mở khả năng trong cấu trúc ấy. Ý đồ hài và bi kịch theo POV tiếp tục ở `04`. Việc một lần sửa thiết kế được phản chiếu trong cấu trúc fiction là phần lịch sử sáng tác. Trình tự và sự kiện trong fiction vẫn do `03` kiểm soát.

## Công nghệ và quyền lực thể chế

Một số giao diện định danh, dữ liệu và dịch vụ được phát triển sớm trong bối cảnh nghề. Việc giữ được chức năng khi đổi môi trường sử dụng cho phép phát triển thiết bị và dịch vụ khách qua quy trình riêng. Các khả năng dùng chung không mang theo hạn chế địa vị, cơ quan quản lý hoặc phạm vi triển khai cùng chúng. Cách này cũng bảo toàn khác biệt giữa nền công nghệ chung và việc AF triển khai theo năng lực tổ chức của mình.

Hội đồng Pháp sư và cụm an ninh từng được dùng để nối năng lực chuyên môn với bảo trì hạ tầng, bảo vệ lợi ích và phản ứng trước nhiều nguồn áp lực. Một cơ quan quá bao trùm khiến những câu hỏi về thông tin, quyền và khả năng hành động biến mất khỏi thiết kế. Việc mô tả tách cơ quan, site, miền chuyên môn và các nguồn quyền giúp giữ ma sát thể chế. Học viện còn giữ chức năng đào tạo và nhánh nhân vật độc lập với các lần đổi bản đồ khu vực. `10`, `12` và `14` phân công nội dung hiện hành theo phạm vi ấy.

## Khu vực, Creed và các phụ thuộc

Việc bỏ Quad Night làm mất căn cứ của một số đường đi, cách bảo hộ và vị trí chiến lược. Chức năng đối trọng vùng, thương mại giữa các bên đối địch và can thiệp có thể tiếp tục qua những quan hệ được chốt riêng. Tương tự, bỏ nền tu tiên RF tháo các giả định về phân tầng sức mạnh và không phận mà vẫn cho phép giữ liên hiệp, huyết hệ và quan hệ phụ thuộc đã có căn cứ độc lập. Hai quá trình này cho thấy cần lần đúng hệ quả phụ thuộc khi đổi một tiền đề thiết kế.

Trong thiết kế cũ, Thánh điện tạo sức ép công khai từ một vị thế mà chính quyền vẫn cần đến vì chính danh tôn giáo, bảo vệ và thánh vật. Giữ được chi phí và điều kiện của việc trấn áp giúp một đối trọng có thể tồn tại mà không cần miễn trừ tuyệt đối. Điều này cũng giải thích vì sao phản đối tôn giáo và kháng chiến nội bộ có vai trò khác nhau.

Creed từng gộp chức năng xác minh, tiếp cận và cưỡng hành. Một lỗi thiết kế là phản đối hoặc vi phạm có thể biến thành cơ chế trừng phạt tự động ở quy mô xã hội, qua đó thay cho quyết định của tác nhân và thiết chế. Khung thay thế giữ vai trò làm chứng, quyền tiếp cận có điều kiện và khả năng gây áp lực qua phân bổ ân điển. Các quyết định và hậu quả diễn ra qua thẩm quyền và nguồn lực cụ thể. Vai trò mở Saint's Fresh có căn cứ riêng. Chi tiết hiện hành thuộc `40`, với phạm vi thay thế ở `91` và các câu hỏi triển khai ở `92`.

## Hoa Nguyệt

Thiết kế Hoa Nguyệt phát triển theo hướng một đối trọng có căn tính, triết lý phép thuật và nền hình thành riêng. Căn tính được bộc lộ qua cách trình diện trong nước và đối ngoại, trong khi hình ảnh đẹp và dark foundation có thể cùng tồn tại. Việc ghi riêng văn hóa, biểu tượng và giao thương giúp truy đúng điều kiện của mỗi miền. Các thay đổi về tên, mẫu nguồn và phạm vi chấp nhận được ghi ở `91`, còn nội dung hiện hành thuộc `20–23`.
