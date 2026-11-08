# Cách dùng Naming

Naming giúp tạo tên, phân tích tên có sẵn, so sánh lựa chọn, điều chỉnh mức quen thuộc và xử lý nghĩa khi cần. Bạn chỉ cần mô tả việc muốn làm, hệ tên và những điều cần giữ nếu chúng quan trọng.

Đây là hướng dẫn sử dụng bản Naming 1.0 trong repository; chưa xác nhận cài đặt hoặc kiểm thử live bản mới.

## Cú pháp

```text
/NAME <instruction> #
/NAME P1 <instruction> #
/NAME P2 <instruction> #
/NAME P3 <instruction> #
```

Viết đúng chữ hoa `/NAME`; cần nội dung yêu cầu và dấu `#` đứng riêng, cách phần trước bằng khoảng trắng hoặc xuống dòng. Có thể đặt lệnh giữa câu hoặc viết nhiều dòng. Lệnh trong trích dẫn hoặc khối mã chỉ là ví dụ, không kích hoạt.

Mỗi lần gọi chỉ áp dụng cho phần giữa `/NAME` và `#`, không bật chế độ kéo dài. Không lồng các lệnh vào nhau. P4, p2, chỉ có preset mà thiếu yêu cầu, hoặc ghép nhiều preset đều không hợp lệ; FIT/DISTINCT/SEMANTIC không phải tên lệnh thay thế.

## Chọn cách làm

| Cách gọi | Khi nào dùng |
| --- | --- |
| `/NAME` | Để Naming thích ứng với yêu cầu; không tự gán preset. |
| `P1` — FIT | Ưu tiên đúng hệ tên và các ràng buộc đã giao. |
| `P2` — DISTINCT | Giữ đúng hệ nhưng tránh lựa chọn quá quen hoặc sáo mòn; không có nghĩa càng hiếm càng tốt. |
| `P3` — SEMANTIC | Khi dạng chữ, cách đọc, nghĩa, từ nguyên, danh hiệu hoặc liên hệ văn hóa thực sự quan trọng. |

Muốn vừa khác biệt vừa phân tích nghĩa, hãy nói cả hai trong yêu cầu; không cần ghép preset.

## Ví dụ

FIT, khi đã cung cấp nhân vật trong ngữ cảnh:

```text
/NAME P1
Đề xuất 8 tên nữ Nhật Bản hiện đại cho nhân vật này. Không cần symbolism.
#
```

DISTINCT, khi setting đã xác định hệ tên:

```text
/NAME P2
Đề xuất 10 tên nam thuộc hệ Latin/châu Âu của setting hiện tại.
Tránh nhóm tên fantasy/LLM quá quen nhưng không tạo tên giả chỉ để nghe lạ.
#
```

SEMANTIC: thay phần trong ngoặc vuông bằng tên muốn phân tích.

```text
/NAME P3
Phân tích cấu trúc và nghĩa của tên này: [tên cần phân tích].
Giữ riêng written form, reading, etymology và liên hệ fiction;
không tự suy personality từ meaning.
#
```

Yêu cầu đủ rõ sẽ được xử lý ngay, không cần một vòng duyệt bắt buộc. Nếu cách hiểu khác nhau có thể làm đổi đáng kể kết quả, Naming sẽ hỏi tập trung vào điểm đó. Bạn cũng có thể yêu cầu “trình cơ sở đặt tên để tôi duyệt trước”. Đây chỉ là cách hiểu chuẩn bị được dùng, không bảo đảm đã nắm hết ý bạn.

Nếu Naming dừng để hỏi hoặc chờ bạn duyệt cơ sở đặt tên, lần gọi hiện tại kết thúc. Lượt sau phải gọi `/NAME` lại; chỉ trả lời “đồng ý” không kích hoạt. Muốn giữ P2, ghi lại P2:

```text
/NAME P2
Dùng basis vừa trình, nhưng giữ nguyên họ hiện có; tiếp tục đề xuất tên.
#
```

## Nghĩa, chứng cứ và quyền chọn của bạn

Câu hỏi phụ thuộc ngôn ngữ, lịch sử hoặc văn hóa thực có thể cần kiểm chứng. Khi thiếu chứng cứ, phần phụ thuộc có thể được để mở thay vì bịa. Một cách phiên âm chưa chắc chỉ tương ứng với một dạng chữ hoặc một nghĩa.

Tên phổ biến không tự là tên xấu. P2 không đồng nghĩa “càng hiếm càng tốt”; cảm giác quen với model không phải số liệu tần suất ngoài đời. P3 không buộc tên phải tượng trưng cho nhân vật. Nghĩa tên không tự trở thành tính cách, và một liên tưởng văn hóa thú vị không tự thành lore.

Bạn vẫn có thể cố ý chọn tên có nghĩa trái với vai trò nhân vật. Naming phải giữ ý định và trạng thái nhân vật đã giao, không sửa nhân vật để hợp với tên.
