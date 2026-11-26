# Project Feather Core — Nền công nghệ & kiến trúc dịch vụ hiện hành

> Module ID: `AFM-010`
> Runtime role: `CURRENT_SOURCE`
> Domain / Scope: Nền công nghệ chung của Project Feather Core, kiến trúc terminal/giao diện dịch vụ và mô hình ứng dụng Guest Pass AF đã được chấp nhận.
> Authority boundary: Kiểm soát kiến trúc chức năng chung; Guest Pass/đặt cọc/quy trình khách giữ phạm vi ứng dụng AF. Không xác lập phổ cập toàn thế giới, chuẩn liên quốc gia, backend chung, ownership hoặc implementation chưa chốt.
> Cross-domain owner boundary: AF national engineering/deployment context by `AFM-013`; RF internal canon by `AFM-014`; Global institutions and geopolitics are controlled by `AFM-001`; legal/civic status and shared economic namespaces by `AFM-002`; Undie professions, occupational hardware and Undi by `AFM-003`; detailed aviation and RF airspace by `AFM-008`.
> Load mode: `FULL_FILE`

> **Truth boundary:** the functional architecture below is accepted canon/design direction. Implementation, scale and present rollout remain `UNKNOWN` where unspecified; genealogy does not establish present capabilities.

## 1. Nền công nghệ và ranh giới miền

File này quản lý nền công nghệ/kiến trúc dịch vụ chung của **Project Feather Core**, không thuộc riêng một quốc gia. Việc một kiến trúc được mô tả ở đây không chứng minh mọi nước đã sở hữu, triển khai hoặc dùng chung tiêu chuẩn. Cách AF cưỡng ép compatibility, vai trò Hội đồng Pháp sư và năng lực tổ chức AF thuộc `10_AETHERFIRE_NATIONAL_CANON_CURRENT.md` §4; chi tiết hàng không ở `06_STABLE_AVIATION_RF_AIRSPACE_CURRENT.md`.

Các §§2–3 mô tả kiến trúc chức năng; §§4–8 giữ mô hình ứng dụng khách AF đã được chấp nhận, trong đó primitives kỹ thuật có thể được tham chiếu độc lập nhưng chính sách không tự áp cho quốc gia khác. Mọi cơ chế quốc gia/chuyển giao/triển khai mới cần canon riêng. Nền chung không phải một hệ magic hoàn chỉnh hoặc một hệ thống kỹ thuật phổ cập.

Các capability định danh, xác thực, thanh toán, dữ liệu, bảo trì và dịch vụ có thể được sử dụng qua giao diện chung. Giao diện tương tác không chứng minh một database, một chủ sở hữu, một cơ quan quản trị hay mức phổ cập toàn quốc. Không dùng độ trưởng thành của một hệ chuyên dụng để áp thứ bậc bắt buộc giữa công nghệ nghề nghiệp, dân dụng và chiến lược. Nguồn năng lượng, sản xuất, chi phí và chuỗi cung ứng chưa được xác lập.

## 2. Chuyển giao công nghệ, không chuyển giao địa vị hoặc cưỡng chế

Terminal, thư và thông tin người dùng, giao diện retina có phần tích hợp cơ thể, audio tích hợp xương tai, commission forum và kênh gọi an ninh khẩn cấp có điều kiện là các năng lực đã chốt. Sự tồn tại của chúng không đặt ra nghĩa vụ cấy ghép, nhận dạng hay chịu quyền lệnh cho người hành nghề Undie.

Giao diện dịch vụ khách không xác lập địa vị, nghĩa vụ lao động, hạn chế di chuyển hay điều kiện tín dụng theo nghề. Chuyển giao một chức năng kỹ thuật chỉ có hiệu lực trong phạm vi đã chốt.

## 3. Personal Terminal — kiến trúc chức năng

Personal Terminal là thiết bị cá nhân gắn trên cơ thể nhưng tháo rời được, làm giao diện tới định danh, access, thanh toán và dịch vụ; không phải một smartphone thu nhỏ.

```text
Personal Terminal = Terminal Core + compatible Body Dock
Terminal ≠ identity source of truth ≠ legal status ≠ account ≠ access authority
Shared interface ≠ shared database ≠ shared authority
```

Core chứa xử lý, credential an toàn, liên lạc và giao diện dịch vụ/thanh toán/hiển thị riêng. Core chuyển giữa các mount tương thích; wrist device/bracelet là ví dụ, không phải hình thức duy nhất đã chốt. Credential nối với backend liên quan, không tự tạo quyền pháp lý.

### 3.1 Giữ thiết bị, chống giật và tháo an toàn

- Người đeo hợp lệ có thể xác thực để mở khóa và tháo bình thường; phương thức xác thực còn mở.
- Unexpected detachment/cutting/snatching làm khóa credential của thiết bị, chức năng thanh toán/access trên thiết bị và khả năng đọc thông tin riêng.
- Khi bị mắc vào máy móc/phương tiện hoặc lực nguy hiểm vượt ngưỡng an toàn, Body Dock breakaway và credential khóa. Ngưỡng chưa chốt; chống trộm không được biến thiết bị thành vật trói giữ cơ thể.

Khóa/revoke thiết bị không đồng nghĩa xóa số dư ví, thay đổi legal status hay tước quyền rời đi. Cách tiếp tục xác thực, truy cập dịch vụ và khôi phục quyền sau sự cố vẫn `UNKNOWN`.

### 3.2 Giao diện riêng và theo ngữ cảnh

Hướng thiết kế chấp nhận private retina interface và private audio không cưỡng chế. Giao diện có thể phục vụ định danh, navigation, số dư, xác nhận giao dịch, quyền truy cập, tin nhắn và thông báo dịch vụ/khẩn cấp.

**Chưa chốt cơ chế chuyển từ năng lực retina/bone-integrated audio đã xác lập sang thiết bị khách tháo rời.** Không mặc định khách phải cấy ghép, hoặc đã có một giải pháp không xâm lấn; thành phần cơ thể, đồng thuận, vô hiệu hóa khi tháo/trả/mất và liên kết thiết bị vẫn mở.

Terminal ưu tiên ngữ cảnh: transit ở cổng, mua hàng ở vending, định danh/access ở checkpoint, giấy tờ/thủ tục ở nơi cung cấp dịch vụ. Đây là thiết kế Project Feather Core được chấp nhận tại đây, không nhập ontology, quyền hạn hay implementation từ The Kingdom POT.

## 4. Guest Pass AF và quy trình cấp

> **Phạm vi §§4–8:** mô hình dịch vụ khách AF ở cấp kiến trúc chức năng, không xác nhận rollout hiện tại hoặc chính sách toàn thế giới. Phạm vi này đi cùng mọi bước cấp, ví, đặt cọc, giao dịch và trả/mất thiết bị.

Guest Pass gồm credential định danh tạm thời, access profile tạm thời, service profile và giao diện tới Guest Wallet. Nó không phải legal status/class mới, không đồng nghĩa Citizen/Civil và không tự cấp quyền nhập cảnh/cư trú.

```text
foreign visitor → identity verification → Guest Profile
→ device deposit collected → Guest Terminal issued
→ Guest Pass bound to terminal → Guest Wallet activated
```

Terminal có guest mode với credential/validity/access profile, ví trả trước và hồ sơ đặt cọc riêng. Thẩm quyền cấp, điều kiện nhập cảnh và full access matrix còn mở.

## 5. Ba đối tượng phải tách

| Đối tượng | Chức năng | Không đồng nghĩa |
| --- | --- | --- |
| Device Deposit | Bảo đảm thiết bị; tạo động lực hoàn trả; hoàn khi trả bình thường | Số dư chi tiêu của ví |
| Guest Wallet | Giá trị trả trước cho giao dịch tương thích | Đặt cọc, Credit Score, Credit Line hoặc legal status |
| Access Profile | Quyền truy cập nơi/dịch vụ trong phạm vi được cấp | Tiền, class hoặc social hierarchy |

Guest Wallet dùng biến tài chính riêng. Đơn vị tiền và cách triển khai ví vẫn mở.

## 6. Đặt cọc và ví

### 6.1 Device Deposit

Hồ sơ gồm guest ID, terminal ID, đồng tiền, số tiền danh nghĩa, nơi/thời gian cấp và refund entitlement. Deposit không chuyển thành giá trị chi tiêu ví. Khi thiết bị được trả bình thường, hoàn đúng số tiền danh nghĩa trong đồng tiền ghi lúc cấp. Con số `500` của nguồn là ví dụ, không phải mức đặt cọc canon.

Quy tắc này tách deposit khỏi quy đổi để chi tiêu; không chứng minh toàn bộ vấn đề ngoại hối/quyết toán đã được giải quyết. Hạ tầng quyết toán và mức đặt cọc theo đồng tiền/quốc gia còn mở.

### 6.2 Guest Wallet

Ví vận hành theo `load value → spend → reload`. Miền sử dụng gồm transit, vending, ordinary retail, thực phẩm/nhu yếu phẩm và dịch vụ được chấp thuận tương thích; QR/tap là giao diện thanh toán. Danh sách này không chứng minh mọi nhà cung cấp đã tham gia hoặc mọi khách có cùng access.

Đơn vị tiền ví và xử lý số dư chưa dùng khi rời đi vẫn `OPEN`. Trả terminal không tự hoàn số dư ví.

## 7. Giao dịch và quyền riêng tư tối thiểu

QR biểu diễn payment request: recipient, amount, transaction reference, expiry và metadata tùy chọn; không chứa tiền lưu trữ có thể chuyển nhượng. Terminal hiển thị riêng người nhận/số tiền/mục đích/hạn; khách xác nhận; payment backend xử lý giao dịch.

Vending công bố dữ liệu sản phẩm/dịch vụ; người dùng chọn và xác nhận qua terminal; backend trả `PAYMENT_OK`; máy cấp hàng. Máy chỉ nhận claims cần thiết như `PAYMENT_OK`, `AGE/ACCESS_OK`, `ITEM_PERMISSION_OK`, không tự nhận toàn bộ identity/status/legal history, Credit Score hoặc Contribution Points. Quy tắc này không tự xác lập luật privacy/data-retention quốc gia.

## 8. Trả thiết bị, hoàn đặt cọc và mất thiết bị

### 8.1 Return Machine

Trong luồng trả bình thường: xác minh terminal ID, nhận thiết bị, đóng Guest Pass session/revoke credential của thiết bị, sanitize local/private data, đưa hardware vào reissue pool và authorize deposit refund.

`Terminal accepted + refund entitlement recorded/authorized` là một giao dịch trả hoàn chỉnh. Không được để máy giữ terminal nhưng mất quyền hoàn đặt cọc. Nếu khâu giao tiền thất bại, claim vẫn khôi phục được qua terminal khác hoặc quầy có nhân viên. Quyền claim không đồng nghĩa đã nhận tiền thành công.

Thứ tự chi tiết giữa trả thiết bị, revoke Guest Pass và hoàn tất exit/checkpoint chưa chốt. Không mặc định khách có thể qua mọi cổng sau revoke; cơ chế xác thực không cần terminal và duy trì quyền đi ra phải được xác định trước khi mô tả quy trình chi tiết là hoàn chỉnh.

### 8.2 Lost/damaged terminal

Báo mất dẫn đến revoke credential thiết bị cũ; thiết bị cũ không còn dùng để thanh toán/access. Có thể cấp thiết bị thay thế và bind lại Guest Profile. Thu deposit mới và giữ deposit cũ theo điều kiện trả thiết bị là **candidate accounting**, không phải chính sách đã chốt. Hạch toán mất/hỏng, số dư ví và phục hồi quyền truy cập còn mở.

## 9. Ranh giới triển khai

Thiết kế chức năng chưa xác lập việc triển khai từng thiết bị, chuẩn, backend, thẩm quyền, chi phí hay mức phổ cập. `92` giữ danh mục AF-TECH-001 và AF-TECH-002.

`01` kiểm soát giao diện thế giới; `10` giữ hồ sơ quốc gia AF, `12` giữ chính trị/thể chế; `11` kiểm soát status và economic namespaces; `13` kiểm soát nghề Undie, phần cứng nghề còn mở và Undi; `06` kiểm soát aviation. Các unknown hiện có trong những miền này vẫn có hiệu lực; module này không thay quyền sở hữu nội bộ của chúng.
