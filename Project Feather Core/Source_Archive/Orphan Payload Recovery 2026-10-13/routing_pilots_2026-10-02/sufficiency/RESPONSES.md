# Đáp án cuối thực tế của 8 fresh agent

Giữ nguyên nội dung đáp án cuối; nhãn lượt bên ngoài các block dùng để đối chiếu với protocol/report. Không cấp tài liệu này cho các agent của phép thử.

## t1 — gate_trial_1

```text
SUFFICIENT:
YES

MISSING:
NONE

EXPECTED_LOCATION:
NONE

REASON:
Candidate chứa đủ cả ba tuyến, dạng đường và chức năng được xác nhận dưới nhãn CANON. Tuyến phía bắc có dạng đường mòn và vị trí sát núi lửa; tuyến trung tâm có đường quốc gia cùng cơ sở chính thức; tuyến phía nam có đường thô sơ chủ yếu phục vụ logistics. Evidence không xác lập chức năng riêng cho tuyến phía bắc, nên có thể nêu đúng giới hạn này mà không suy diễn thành trạng thái UNKNOWN của canon.

CONFIDENCE:
HIGH
```

## t2 — gate_trial_2

```text
SUFFICIENT:
NO

MISSING:
- Vai trò của ba linh mục trong thực thi Creed và yêu cầu về số lượng, để đối chiếu với vai trò làm chứng của ít nhất ba linh mục khi cho mượn thánh vật.
- Quy định Thánh Nữ có bắt buộc tham gia thực thi Creed hay không.

EXPECTED_LOCATION:
- `## 7. Creed quorum` → `### CANON` và `### Hệ quả cấu trúc đã xác nhận ở mức architecture`.
- `## 6. Creed — chức năng oath hiện hành` → các quy định thực thi theo đối tượng, nếu điều kiện tham gia phụ thuộc loại oath.

REASON:
Candidate xác lập vai trò trong hoạt động cho mượn thánh vật: Thánh Nữ đại diện, ít nhất ba linh mục làm chứng. Candidate chưa cung cấp quy định thực thi Creed, nên chưa đủ để so sánh vai trò linh mục hoặc kết luận Thánh Nữ phải tham gia cả hai. Sự thiếu vắng này không xác lập trạng thái UNKNOWN trong canon.

CONFIDENCE:
HIGH
```

## t3 — gate_trial_3

```text
SUFFICIENT:
YES

MISSING:
NONE

EXPECTED_LOCATION:
NONE

REASON:
Candidate nêu rõ đối tượng bảo vệ của cả hai lực lượng và đích allegiance trực tiếp của Holy Guard, đồng thời xác nhận chúng là hai lực lượng khác nhau. Các claim nằm trong phần CANON của source có authority phù hợp.

CONFIDENCE:
HIGH
```

## t4 — gate_trial_4

```text
SUFFICIENT:
NO

MISSING:
- Căn cứ xác lập quan hệ đối địch AF–ML và việc dependency thánh vật vẫn buộc AF giao thương trong quan hệ đó.
- Claim phân biệt dependency vào ML relic access với dependency liên quan RF/Raging Fire.

EXPECTED_LOCATION:
- `## 11. Hai trục dependency lớn của AetherFire` → `### CANON`.
- `## 12. Quan hệ với AetherFire và Thần điện trong AF` → `### CANON`.

REASON:
- Candidate xác lập AF phải định kỳ mua quyền sử dụng thánh vật do ML kiểm soát để gia cố phong ấn. Tuy nhiên, chưa có evidence về quan hệ đối địch hoặc dependency RF để giải thích đầy đủ và đối chiếu hai dependency.

CONFIDENCE:
HIGH
```

## t5 — gate_trial_5

```text
SUFFICIENT:
YES

MISSING:
NONE

EXPECTED_LOCATION:
NONE

REASON:
Candidate xác lập rõ cơ chế split-self chưa được định nghĩa đầy đủ và khả năng Creed ràng buộc Trúc Nha còn không chắc chắn. Mục 22 củng cố trạng thái deferred của cơ chế bypass. Evidence đủ để trả lời theo trạng thái chưa chốt, không suy diễn cơ chế hoặc khẳng định cô đã được bảo đảm miễn nhiễm hoàn toàn.

CONFIDENCE:
HIGH
```

## t6 — gate_trial_6

```text
SUFFICIENT:
NO

MISSING:
- Chưa xác lập Creed trừng phạt riêng người phá oath hay những thành viên nào trong family-bound oath unit.
- “Hậu quả tim mạch” chưa xác lập là đau tim, cũng chưa xác lập hậu quả áp dụng cho toàn bộ gia đình.
- Thiếu claim hoặc trạng thái UNKNOWN xác định các giới hạn trên.

EXPECTED_LOCATION:
- Mục `6. Creed — chức năng oath hiện hành` → `6.2 Giáo dân` → `UNKNOWN`.

REASON:
- Candidate xác lập phạm vi oath gồm giáo dân và tập quan hệ gia đình được thần quyền công nhận, cùng hậu quả tim mạch khi oath bị phá. Phạm vi tham gia oath chưa chứng minh phạm vi người bị trừng phạt; hậu quả tim mạch chưa chứng minh toàn bộ gia đình bị đau tim. Quy tắc giữ UNKNOWN trong metadata cũng chưa xác lập trạng thái cụ thể của cơ chế này.

CONFIDENCE:
HIGH
```

## t7 — gate_trial_7

```text
SUFFICIENT:
YES

MISSING:
NONE

EXPECTED_LOCATION:
NONE

REASON:
Candidate có đủ quan hệ Cult–Temple, điều kiện ba clergy cùng đồng thuận và giới hạn suy luận trực tiếp: attack surface tồn tại nhưng không được tự suy Cult đã kiểm soát một quorum cụ thể. Các bằng chứng này đủ để đánh giá việc ghi nhận claim được hỏi.

CONFIDENCE:
HIGH
```

## t8 — gate_trial_8

```text
SUFFICIENT:
NO

MISSING:
- Allegiance của Holy Guard hướng về đâu; candidate chỉ xác lập đối tượng được bảo vệ, chưa xác lập allegiance.

EXPECTED_LOCATION:
- `## 6. Creed — chức năng oath hiện hành` → `### 6.3 Guardian / Holy Guard`.
- `## 8. Holy Guard và vệ binh quốc gia` → `### Holy Guard`.

REASON:
- Candidate đủ cho phần phân biệt hai lực lượng và đối tượng bảo vệ. Tuy nhiên, không thể suy allegiance từ nhiệm vụ bảo vệ; cũng không có evidence xác lập allegiance là UNKNOWN.

CONFIDENCE:
HIGH
```
