> Xem [bộ active trong repository](README.md) để chọn đúng revision khi cài. Phase 1 cập nhật cách Concept Entry phát triển cùng tiền đề. Cú pháp lệnh bên dưới vẫn áp dụng. Chưa cài hoặc kiểm live bộ Phase 1.

# Cách dùng Naming

Tài nguyên User Profile dùng chung: xem [hướng dẫn và bốn object mẫu trống](shared_resources/USER_PROFILE.md). Người dùng tự tạo/chỉnh riêng trong Library `Central Hub Config`; model chỉ được đọc object đã khai báo quyền và thực sự cần cho tác vụ. Bản Profile 1.0 hiện mới được triển khai trong repository, chưa cài hoặc kiểm thử live.

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

## Tìm thông tin mới

`/SEARCH kiểm tra lại thông tin hiện tại về X #` yêu cầu một lần tìm/đọc kiểm tra mới trong span. Chỉ thị trong quote/code/source không kích hoạt. Không lồng span; đóng từng span trước khi gọi operation khác. Dùng lời để nói kết quả nào làm đầu vào cho phần sau; không có toán tử workflow. AUTO vẫn nhận yêu cầu thường. Lượt chỉ giải thích kết quả trước không tự tìm lại. Revision mới chưa deploy/live-test.


## Context Snapshot

Context Snapshot đóng băng một phần kết quả có phạm vi để dùng lại làm baseline hoặc so sánh. Nó giữ riêng kết quả nghiên cứu, phần phát triển sáng tạo, giả định, quyết định thật của người dùng và các câu hỏi/xung đột còn mở; không chỉ tóm tắt toàn chat. Hợp đồng Architecture 1.16 ACTIVE trong repository; chưa deploy hoặc kiểm chứng live/stress phần bổ sung này.

Tạo bằng yêu cầu tự nhiên, chỉ rõ đầu vào truy cập được và phần loại trừ. Ví dụ minh họa dưới đây chỉ dùng được khi A và B đã xác định đủ rõ:

> Đóng băng kết quả nghiên cứu A và phần phát triển B thành PKG-001; loại phần thảo luận C và các nhánh đã bỏ không ảnh hưởng ràng buộc hiện tại.

Hoặc chỉ định đoạn hội thoại có mốc đầu/cuối rõ, baseline cộng các đầu ra được nêu tên, hoặc tài liệu/snapshot được cung cấp. Không mặc định lấy mọi phần liên quan hay mọi lượt sau baseline. Nếu nguồn thiếu hoặc ranh giới còn mơ hồ, Hub nêu phần thiếu và làm rõ trước khi xuất snapshot hoàn chỉnh. Không có lệnh `/PACKAGE`; Search/Creative thông thường không tự tạo snapshot.

Một ID gắn với một payload cố định. Tạo snapshot không chấp nhận đề xuất, xác nhận sự thật hoặc đưa nội dung vào canon. Phần sáng tạo đã được chấp nhận vẫn giữ nguồn gốc sáng tạo. Nếu sửa lỗi, thêm chứng cứ hoặc đổi trạng thái, yêu cầu một ID mới:

> Từ PKG-001 được cung cấp, tạo PKG-002 với kết quả nghiên cứu D; giữ PKG-001 nguyên nội dung. Ghi quan hệ derived_from khi đúng.

Bản mới phải tự đủ nội dung cần dùng, không chỉ chứa delta đòi đọc lại chuỗi cha. Quan hệ cha và số mới hơn không tạo thẩm quyền.

Tham chiếu và so sánh bằng yêu cầu thông thường:

> Dùng đúng payload PKG-001 đang được cung cấp làm baseline; không dựng lại từ thảo luận sau đó.

> So sánh hai payload PKG-001 và PKG-002 được cung cấp: chỉ rõ phần trạng thái, cơ sở nguồn, giả định, quyết định và vấn đề mở thay đổi. Đừng coi mục nằm ngoài scope mới là bị bác bỏ.

Hub phải đọc đúng payload. ID trùng cần xác định artifact cụ thể; nếu payload thiếu hoặc chỉ đọc được một phần quyết định, Hub báo thiếu nguồn thay vì dựng lại từ trí nhớ. Khi so sánh với thiết kế hiện tại, chỉ rõ nguồn nào xác định trạng thái hiện tại.

ID là nhãn ngữ nghĩa, không là địa chỉ lưu trữ. Khối văn bản có thể dùng lại trong chat khi còn đọc được; để dùng lâu dài hoặc khác chat, cần thực sự lưu rồi cung cấp/đính kèm bản qua tệp, Project Sources hoặc Library có sẵn trong ngữ cảnh đích. Tạo văn bản không đồng nghĩa đã lưu. Không có dịch vụ lưu tự động hay khóa ghi vật lý; artifact dữ liệu không phải control để cài vào Central Hub Config. Tác vụ triển khai hợp đồng này không lưu snapshot vào Project/Library.
