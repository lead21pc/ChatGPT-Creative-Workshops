# The Kingdom / Mẫu quốc — Hệ thống phản gián và kiểm soát rò rỉ tri thức

> Tài liệu này tổng hợp các phương thức phản gián, kiểm soát công nghệ và kiểm soát tri thức đã bàn trong chat hiện tại.  
> Phân loại:
> - **CANON / đã chốt:** premise người dùng đã xác lập.
> - **PHƯƠNG ÁN THIẾT KẾ:** cơ chế mở rộng nhằm làm hệ thống nhất quán, chưa mặc định là canon nếu chưa chốt riêng.
> - **HỆ QUẢ SUY LUẬN:** hệ quả logic của canon.

---

# I. Triết lý chung

**CANON / HỆ QUẢ TRỰC TIẾP**

Mẫu quốc không dựa chủ yếu vào mô hình phản gián hiện đại kiểu:

- giám sát mọi người;
- chặn mọi cuộc tiếp xúc;
- giữ bí mật chỉ bằng phân loại tài liệu;
- dựa vào lòng trung thành của cá nhân.

Thay vào đó, bảo mật được đưa vào **cấu trúc pháp thuật của quyền tiếp cận**.

Triết lý:

> Không chỉ bảo vệ vật thể hoặc tài liệu.  
> Phải bảo vệ khả năng sử dụng, truyền lại, tái dựng và mang thông tin ra ngoài phạm vi được phép.

Hệ thống vì vậy có bốn lớp lớn:

1. nhân sự ngoại giao khó bị khai thác;
2. vật phẩm xuất khẩu có creed/curse;
3. phần mềm có curse cá nhân hóa;
4. tri thức tuyệt mật gắn với oath và cơ chế lọc/xóa ký ức khi rời phạm vi cho phép.

---

# II. Lớp 1 — nhân sự đại sứ quán tiền tiêu

## 1. Thiết kế nhân sự

**CANON**

Trước khi mở cửa hoàn toàn, Mẫu quốc có thể thỏa thuận xây một đại sứ quán tại quốc gia gần nhất.

Nhân sự đại sứ quán được chọn từ một chủng tộc có:

- phong thái cao;
- lòng tự tôn cao;
- truyền thống ghét phản bội;
- lời thề bất khả tín;
- phép thuật hộ thân;
- thần hộ mệnh hoặc phép hộ thần;
- khả năng hồi sinh tại thần điện Mẫu quốc nếu bị giết.

## 2. Giá trị phản gián

**HỆ QUẢ SUY LUẬN**

Các đặc tính trên làm giảm hiệu quả của:

- mua chuộc;
- tra tấn;
- bắt cóc;
- ám sát;
- ép phản bội;
- đe dọa tính mạng.

Nếu chết vẫn có thể hồi sinh tại thần điện Mẫu quốc, giá trị của ám sát và bắt cóc giảm mạnh.

## 3. Lỗ hổng cần xử lý

**PHƯƠNG ÁN THIẾT KẾ**

Lòng trung thành không đủ để ngăn:

- lừa để nói ra thứ tưởng là vô hại;
- khai thác khác biệt văn hóa;
- đặt hàng nghìn câu hỏi nhỏ rồi tổng hợp;
- quan sát phản ứng;
- khai thác điều nhân viên không biết là bí mật.

Do đó lời thề nên không chỉ cấm:

> cố ý tiết lộ bí mật,

mà còn cần hạn chế:

> tạo ra một kênh truyền thông tin bị phân loại cho chủ thể không có quyền tiếp nhận.

---

# III. Lớp 2 — vật phẩm trao đổi có creed hoặc curse

## 1. Tiên đề

**CANON**

Vật phẩm được trao đổi ra ngoài có thể bị gán:

- **creed**;
- hoặc **curse**.

Người sử dụng cam kết tuân thủ điều kiện sử dụng.

Nếu vi phạm điều kiện:

> vật phẩm hóa thành hư không.

## 2. Mục tiêu

- ngăn tháo rời trái phép;
- ngăn chuyển giao trái phép;
- ngăn sử dụng sai phạm vi đã cam kết;
- ngăn chiếm đoạt vật thể vật lý rồi reverse-engineer trực tiếp.

## 3. Vấn đề derivative information

**PHƯƠNG ÁN THIẾT KẾ**

Nếu curse chỉ kích hoạt khi vật thể bị tháo hoặc sử dụng sai, bên ngoài vẫn có thể:

- đo đầu vào/đầu ra;
- ghi nhiệt độ, dao động, trường phép;
- phân tích hiệu suất;
- dựng mô hình hộp đen;
- thu dữ liệu trước khi vi phạm.

Do đó cần quyết định canon:

### Phương án A — chỉ bảo vệ vật thể gốc
Mẫu quốc chấp nhận:
> bên ngoài được phép tự suy luận những gì họ đủ năng lực suy luận từ việc sử dụng hợp pháp.

### Phương án B — bảo vệ cả hành vi tái dựng
Curse nhận biết:
- mục đích phân tích;
- hành vi reverse-engineer;
- hành vi cố tạo bản sao.

Phương án B mạnh hơn rất nhiều và biến curse thành một cơ chế kiểm soát luồng tri thức.

---

# IV. Lớp 3 — phần mềm có curse cá nhân hóa

## 1. Tiên đề

**CANON**

Phần mềm do Mẫu quốc sản xuất có curse tương tự vật phẩm, nhưng ở cấp **cá nhân**.

Quyền sử dụng gắn với chủ thể cụ thể.

## 2. Vấn đề không chỉ là “ai chạy phần mềm”

**PHƯƠNG ÁN THIẾT KẾ**

Nếu chỉ khóa người sử dụng, vẫn tồn tại các kênh rò:

- người khác nhìn màn hình;
- ghi lại đầu ra;
- dùng phần mềm tạo dữ liệu rồi chuyển đi;
- cho AI bên ngoài quan sát phản ứng;
- dùng nhiều truy vấn để xây hệ thống bắt chước;
- điều khiển gián tiếp qua chương trình khác.

## 3. Kiến trúc quyền phù hợp hơn

Một quyền sử dụng nên gắn đồng thời với:

```text
chủ thể
+
mục đích
+
dữ liệu
+
đầu ra
+
quyền chuyển giao
```

Tức là:

> A được dùng chức năng X cho mục đích Y; đầu ra Z chỉ được phép rời phạm vi trong điều kiện W.

Đây là dạng **kiểm soát luồng thông tin bằng pháp thuật**, không chỉ là giấy phép phần mềm.

---

# V. Lớp 4 — oath cho cá nhân tiếp cận tri thức sâu

## 1. Tiên đề

**CANON**

Những cá nhân muốn biết nhiều hơn phải đi qua hệ thống **oath** được cơ quan pháp thuật chứng nhận.

Khi bước vào vùng được cấp quyền:

- họ có thể tiếp cận tri thức nhạy cảm theo mức được phép.

Khi bước ra:

- muscle memory vẫn có thể được giữ;
- ký ức về phần tuyệt mật sẽ bị xóa sạch.

## 2. Mục tiêu

- cho phép chuyên gia bên ngoài làm việc trong Mẫu quốc;
- cho phép họ học và thao tác trong phạm vi cần thiết;
- nhưng không mang tri thức tuyệt mật ra ngoài.

## 3. Vấn đề muscle memory

**PHƯƠNG ÁN THIẾT KẾ**

Nếu chỉ xóa ký ức khai báo nhưng giữ toàn bộ kiến thức thủ tục, bên ngoài vẫn có thể khai thác:

- trực giác kỹ thuật;
- khả năng chọn cấu hình đúng;
- phản xạ thao tác;
- kỹ năng không giải thích được;
- thống kê lựa chọn của người từng tiếp cận công nghệ.

Ví dụ:
- một kỹ sư không nhớ cấu trúc thiết bị;
- nhưng vẫn có xác suất cao chọn đúng vật liệu hoặc quy trình do trực giác còn lại.

## 4. Ba mức xóa có thể thiết kế

### Mức A — chỉ xóa ký ức sự kiện
- quên mình từng nhìn thấy gì;
- nhưng còn phần lớn tri thức khái niệm và trực giác.

→ Rò rỉ lớn.

### Mức B — xóa ký ức sự kiện + tri thức khái niệm
- quên nguyên lý, thuật ngữ, cấu trúc;
- nhưng muscle memory và trực giác vẫn còn.

→ An toàn hơn nhưng vẫn có thể bị khai thác.

### Mức C — xóa mọi thay đổi có khả năng mã hóa bí mật
Chỉ giữ:
- kỹ năng nền đã có trước;
- năng lực chung không đủ tái dựng thông tin bị bảo vệ.

→ Gần với mục tiêu bảo mật tuyệt mật.

## 5. Nguyên tắc mạnh nhất

**PHƯƠNG ÁN THIẾT KẾ**

> Oath không xóa “muscle memory” nói chung.  
> Oath xóa mọi thay đổi nhận thức hoặc kỹ năng mà từ đó thông tin bị bảo vệ có thể được tái dựng.

Điều này giữ được:
- kỹ năng chung;
- trải nghiệm cá nhân không mật;
- khả năng làm việc bình thường;

nhưng chặn:
- phản xạ đặc hữu;
- chuỗi thao tác;
- trực giác chuyên môn đủ để reverse-engineer.

---

# VI. Kiểm soát theo derivative information

## 1. Vấn đề cốt lõi

**HỆ QUẢ SUY LUẬN**

Nếu chỉ bảo vệ:

- tài liệu;
- thiết bị;
- ký ức trực tiếp;

thì đối thủ sẽ chuyển sang khai thác:

- quan sát;
- đầu ra;
- mẫu hành vi;
- trực giác;
- sai khác hiệu suất;
- những điều người Mẫu quốc không nói;
- tri thức suy ra từ nhiều mảnh nhỏ.

Do đó, bài toán thật sự là:

> bảo vệ **khả năng tái dựng bí mật**, không chỉ bảo vệ bí mật gốc.

## 2. Các kênh derivative information cần cân nhắc

- đo đạc hộp đen;
- phân tích vật liệu không bị curse;
- quan sát cách nhân viên vận hành;
- suy luận từ giá cả và mức độ phổ biến;
- học từ lỗi;
- tái tạo thông qua machine learning/AI;
- thống kê phản xạ của người từng làm việc bên trong;
- suy luận từ việc Mẫu quốc từ chối trả lời một câu hỏi cụ thể.

---

# VII. Phản gián chủ động đối với proxy và khủng bố

## 1. Nguyên tắc attribution

**CANON / HỆ QUẢ TRỰC TIẾP**

Mẫu quốc không chỉ xác định:

> ai bóp cò.

Mẫu quốc truy nguyên:

```text
người thực hiện
+
người chỉ đạo
+
người tài trợ
+
người hỗ trợ
+
người tạo điều kiện
+
người biết nhưng cố tình đứng ngoài
```

Nhưng phải phân biệt cấp trách nhiệm, không đánh đồng tất cả.

## 2. Công khai hóa trách nhiệm

**CANON**

Khi xảy ra vụ thử nước bằng khủng bố hoặc proxy:

- Mẫu quốc có thể gửi công hàm chính thức;
- đồng thời công khai attribution bằng hologram trên bầu trời;
- cho cả thế giới thấy:
  - ai là tác nhân;
  - ai là sponsor;
  - ai cung cấp hỗ trợ;
  - ai biết nhưng đứng ngoài;
  - ai không liên quan.

## 3. Tác dụng phản gián

Hệ thống này phá ba lợi thế của chiến tranh ủy nhiệm:

1. **khả năng phủ nhận hợp lý**;
2. **khả năng kiểm soát narrative sau sự kiện**;
3. **khả năng tách sponsor khỏi người thực hiện**.

Khi attribution được công khai tức thời, các cường quốc khác có thể dùng kẻ thử đầu tiên làm “chuột bạch” và tránh lặp lại chiến thuật nếu thấy sponsor bị bóc hoàn toàn.

---

# VIII. Phân tầng trách nhiệm đối ngoại

**PHƯƠNG ÁN THIẾT KẾ**

Một thang trách nhiệm phù hợp:

```text
Cấp 5 — ra lệnh trực tiếp
Cấp 4 — tài trợ/chủ động hỗ trợ
Cấp 3 — tạo điều kiện có chủ đích
Cấp 2 — biết và cố tình không ngăn để thu lợi
Cấp 1 — sơ suất hoặc bất lực
Cấp 0 — không biết / không liên quan
```

Mục tiêu:

- không biến Mẫu quốc thành tác nhân quy chụp;
- cho thế giới thấy attribution của họ đủ tinh để phân biệt trách nhiệm;
- tạo nền tảng cho phản ứng tương xứng.

---

# IX. Kiến trúc tổng thể của hệ phản gián

```text
BÊN NGOÀI
│
├── đại sứ quán tiền tiêu
│   ├── nhân sự cực khó bị mua chuộc/ép buộc
│   ├── lời thề
│   ├── hộ thân/hộ thần
│   └── hồi sinh nếu bị sát hại
│
├── vật phẩm xuất khẩu
│   └── creed / curse theo điều kiện sử dụng
│
├── phần mềm xuất khẩu
│   └── curse gắn cá nhân + phạm vi quyền
│
├── người ngoài tiếp cận tri thức sâu
│   └── oath được cơ quan pháp thuật chứng nhận
│       ├── cấp quyền trong phạm vi
│       └── lọc/xóa phần tri thức mật khi rời phạm vi
│
└── hành vi thù địch vùng xám
    ├── attribution đa tầng
    ├── phân cấp trách nhiệm
    ├── công hàm
    └── công khai bằng chứng toàn cầu
```

---

# X. Những gì hệ này làm tốt

## 1. Làm suy yếu tình báo truyền thống

- mua chuộc khó;
- tra tấn kém giá trị;
- ám sát không chắc loại bỏ nhân sự;
- lấy vật thể không đồng nghĩa lấy được công nghệ;
- tiếp cận phần mềm không đồng nghĩa có thể sao chép;
- học bên trong không đồng nghĩa mang tri thức mật ra ngoài.

## 2. Chuyển cuộc chơi từ “lấy bí mật” sang “tìm cái có thể học hợp pháp”

Sau vài lần thất bại, các cơ quan bên ngoài phải đổi câu hỏi từ:

> Làm sao lấy công nghệ?

sang:

> Có thể học được gì mà không kích hoạt oath/curse/creed?

## 3. Phá chiến tranh ủy nhiệm

Nếu sponsor bị attribution và công khai tức thời:

> proxy không còn là vùng an toàn về trách nhiệm.

---

# XI. Những lỗ hổng còn cần quyết định

1. **Curse có đọc được mục đích không?**
   - Nếu có, reverse-engineer bị chặn mạnh.
   - Nếu không, mô hình hộp đen vẫn tồn tại.

2. **Thông tin suy ra hợp pháp có bị cấm không?**
   - Nếu Mẫu quốc chặn mọi suy luận, hệ thống cực kỳ tuyệt đối.
   - Nếu không, vẫn có một “khoa học quan sát Mẫu quốc” ở bên ngoài.

3. **Phần mềm kiểm soát đầu ra tới đâu?**
   - chỉ khóa người dùng;
   - hay khóa luôn dữ liệu, mục đích, quyền chuyển giao.

4. **Oath xóa tới mức nào?**
   - ký ức sự kiện;
   - tri thức khái niệm;
   - trực giác và kỹ năng thủ tục có tính mã hóa.

5. **Attribution của Mẫu quốc dựa vào gì?**
   - AI;
   - phép thuật;
   - quan sát tín hiệu;
   - thần tính;
   - hay tổ hợp.

   Cơ chế chi tiết chưa chốt.

6. **Mẫu quốc có công khai toàn bộ bằng chứng không?**
   - Phương án tốt hơn hiện tại: chỉ công khai đủ để chứng minh trách nhiệm, không lộ phương pháp tình báo sâu.

---

# XII. Nguyên tắc lõi để giữ nhất quán

> **Bảo mật của Mẫu quốc không chỉ là giữ kín dữ liệu. Nó là kiểm soát quyền tồn tại, sử dụng, truyền lại và tái dựng dữ liệu trong từng phạm vi.**

> **Lòng trung thành của nhân sự là một lớp bảo vệ, không phải lớp cuối cùng.**

> **Vật phẩm và phần mềm có thể mang điều kiện pháp thuật gắn với quyền sử dụng.**

> **Tri thức sâu được tiếp cận thông qua oath; khi rời phạm vi, phần có khả năng làm lộ bí mật phải bị loại khỏi ký ức hoặc kỹ năng có thể tái dựng.**

> **Chiến tranh ủy nhiệm không tạo miễn trách nhiệm nếu Mẫu quốc truy nguyên được chuỗi tác nhân.**

> **Attribution phải phân biệt người thực hiện, người tài trợ, người hỗ trợ, người tạo điều kiện, người biết nhưng dung túng và người vô can.**

> **Nếu công khai attribution, Mẫu quốc nên công bố đủ để chứng minh kết luận nhưng không tự tiết lộ toàn bộ phương thức thu thập tình báo.**
