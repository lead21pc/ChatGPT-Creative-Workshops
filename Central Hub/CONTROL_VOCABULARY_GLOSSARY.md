# Từ vựng kiểm soát Central Hub

Vai trò: MAINTENANCE / INTERPRETATION REFERENCE. Tài liệu hỗ trợ bảo trì và diễn giải, không có thẩm quyền runtime; không phải Router, schema, validator, default runtime read, dependency, operation registry, grammar owner hay ontology. Hợp đồng của chủ sở hữu quyết định hành vi. Nếu có xung đột, sửa glossary cho khớp hợp đồng hiện hành.

`A != B` nghĩa là không tự động tương đương hoặc suy ra nhau; không cấm mọi quan hệ có căn cứ giữa A và B.

| Thuật ngữ | Nghĩa và chủ sở hữu trong phạm vi này |
| --- | --- |
| SEARCH operation | `/SEARCH <instruction> #`; AIS_PIPELINE_v1.2.md sở hữu cú pháp và nghĩa vụ thực thi hiện tại. |
| AIS RESEARCH mode | Mục đích thu thập, so sánh, tổng hợp trong AIS; không tự đồng nghĩa độ sâu hoặc sản phẩm Deep Research. |
| Shopping Search procedure | Chuẩn bị yêu cầu thương mại và diễn giải kết quả trả về; không gọi công cụ hoặc chọn AIS. |
| Operation | Hoạt động được giao trong tác vụ; không tự trở thành một package/module riêng. |
| Package | Ranh giới trách nhiệm và giao diện được Root chọn. |
| Module | Artifact có trách nhiệm cụ thể trong giao diện được khai báo. |
| Pipeline | Quy trình điều phối công cụ được giao; không sở hữu toàn bộ tác vụ. |
| REQUIRES | Dependency cứng do module khai báo theo Architecture; khác luồng đầu vào của một tác vụ. |
| Task-local input dependency | Chỉ thị dùng đầu ra này làm đầu vào cho phần việc kia; không chuyển quyền sở hữu hoặc tự tạo REQUIRES. |
| # | Dấu đóng span độc lập theo hợp đồng của operation; không phải toán tử kết hợp. |
| Selection / tool execution | Chọn package không chứng minh thao tác bên ngoài đã xảy ra. |
| Fresh search / prior evidence reuse | Thao tác kiểm tra mới liên quan khác việc dùng lại bằng chứng cũ; kết quả không đổi không chứng minh thiếu thao tác mới. |
| Evidence / acceptance | Bằng chứng hỗ trợ thông tin không tự chấp thuận thiết kế/canon hoặc cấp quyền hành động cho bên nhận. |

Các operation khác đang được chấp thuận: `/CREATIVE`, `/BRAINSTORM`, `/DEBATE`, `/NAME` thuộc Concept core/catalog 1.5; `/AUTHOR` thuộc Authoring 0.8 với cú pháp dòng đầu riêng. `/AD` là cue xét applicability theo lượt, không phải operation span. Glossary không định nghĩa thêm cú pháp hoặc toán tử và không phải nguồn đọc runtime bắt buộc.
