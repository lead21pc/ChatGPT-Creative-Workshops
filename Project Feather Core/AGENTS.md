# FTH — Điểm vào host local

Khi người dùng chọn gói FTH này làm workspace cho phiên, thư mục chứa tệp này là root FTH được cấu hình. Mọi đường dẫn bên dưới tương đối với root đó, không phụ thuộc CWD của lệnh. Bản sao bất kỳ cùng tên không tự trở thành nguồn hiện hành.

Tệp này chỉ nối host vào Path B đã được chọn; không là CI, Router, chủ nguồn/canon, nơi lưu trạng thái hoặc bộ chọn phiên bản.

## Bộ điều khiển được ghim

| Thành phần | Đường dẫn tại root FTH |
| --- | --- |
| CI | `Project Feather Core CI/FTH_CI_version_v3.5.md` |
| Router | `Anti-Drift Source/FTH_Anti_Drift_Source_Router_v6.0.yaml` |
| Pipeline | `Anti-Drift Source/FTH_Authoring_Pipeline_v1.1.md` |
| Anti-Drift | `Anti-Drift Source/` |

Trước công việc phụ thuộc FTH, đọc CI ở trên bằng `FULL_FILE`. CI quyết định khi nào phải đọc Router hoặc Pipeline; không tự vào Router cho thao tác chỉ dựa trên đầu vào mà CI cho phép làm độc lập. Không quét các phiên bản để chọn bộ mới nhất.

Với công việc cần trạng thái FTH hiện hành, theo CI vào Router 6.0 và dùng chính root này làm `LOCAL_CURRENT_SOURCE`. Các reference CI, Router, Pipeline và thư mục Anti-Drift ở bảng là binding filesystem của controls cho host local; Router giữ quyền chọn overlay và mở phụ thuộc. Giữ hợp đồng đọc của controls và nguồn; chỉ dùng lại nội dung đã đọc khi còn đầy đủ và phù hợp trong ngữ cảnh. Nếu compact/resume làm mất căn cứ cần thiết, đọc lại trước phần phụ thuộc.

Thiết lập entry không yêu cầu nạp toàn lore, mọi Anti-Drift, hồ sơ `90/91/92/93` hoặc archive. Khi vào Router, tuân bootstrap và việc chọn nguồn/controls theo tác vụ của chính Router. `FTH_SYSTEM_CONTEXT.md` chỉ để định hướng khi hữu ích, không cung cấp hành vi runtime còn thiếu. Path A vẫn là đường đối chiếu riêng, không phải fallback của Path B.

## Nguồn và quyền thao tác

```text
LOCAL FILE EXISTS != AUTHORIZED CURRENT SOURCE
CLIENT CAN SEARCH REPOSITORY != ROUTER MAY USE REPOSITORY SEARCH AS FALLBACK
TOOL ACCESS != WRITE AUTHORITY
CONTENT DEVELOPMENT != REPOSITORY MUTATION
CANON ACCEPTANCE != FILE WRITE
FILE WRITE != COMMIT
COMMIT != PUSH
```

Quyền filesystem chỉ cho truy cập. Khi thiếu nguồn hiện hành quyết định, áp dụng failure contract của Router; không cứu bằng GitHub, Git history, bản gần giống, thư mục khác, root khác, Memory, phản hồi cũ, Library/Project Sources, `90/93` hoặc `Source_Archive`. Giữ đường đọc lịch sử tường minh của Router; lịch sử không thành nguồn current hoặc phụ thuộc mô-đun. Bảo trì repository được phép riêng vẫn theo phạm vi tác vụ, khác với dùng nguồn canon lúc chạy.

Brainstorm, mô phỏng, thiết kế, thảo luận hoặc chấp nhận một ý tưởng canon không tự cho phép sửa file. Chỉ ghi khi tác vụ thực sự yêu cầu cập nhật trong phạm vi được cấp. Quyền ghi không tự cấp quyền commit; commit không tự cấp quyền push. Tôn trọng quyền rõ đã cấp cho tác vụ hoặc quyền thường trực còn áp dụng đúng phạm vi; không thêm vòng xin phép lại. Thẩm quyền tác giả và nguồn vẫn do CI/Router giữ.

RP chỉ bật theo điều kiện riêng; binding local của lore không chuyển portrayal từ Library sang repository. Thiếu portrayal bắt buộc thì chặn phần phụ thuộc, không thay bằng fixture, bản sao Git, archive hoặc nguồn gần giống.

Instruction này ràng buộc cách agent sử dụng nguồn; không bảo đảm chặn indexing, discovery hoặc liệt kê thư mục do host tự thực hiện. `HOST I/O != ROUTER-AUTHORIZED MODEL USE`. Tự nạp entry và tuân thủ live phải được kiểm riêng trên host thực tế.
