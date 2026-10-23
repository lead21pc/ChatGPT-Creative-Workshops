# Greed — RUNTIME

**Vai trò:** sở hữu cấu trúc vận hành riêng của engine; không phải universal pipeline.
**Trạng thái nguồn:** Working Draft v0.2; Governor theo xác nhận tác giả. Tái cấu trúc tài liệu không nâng canon, Working, Placeholder hoặc UNKNOWN. Các mô tả signature là cách đọc phân tích bám nguồn, không là quyết định canon mới.

Đọc theo nhu cầu: [identity/signature](ENGINE_CORE.md), [ranh giới Host](HOST_CONTRACT.md), [vận hành](RUNTIME.md), [vùng mở](OPEN_STATE.md), [kiểm chứng bằng bản viết](WRITING_VALIDATION.md). Đây là vai trò tài liệu, không phải các bước thực thi engine.

## Đường đọc vận hành

- [Vòng cấu hình đã ghi nhận](#chu-trình-được-ghi-nhận).
- [Quy trình Ring chi tiết](#quy-trình-chi-tiết-của-interface-ring).
- Vai trò/interface vật thể: [Ring](COMPONENTS/Ring.md); nhánh chưa có kết quả: [OPEN_STATE](OPEN_STATE.md).



## Chu trình được ghi nhận

```text
chọn người nhận phù hợp [tiêu chí: UNKNOWN]
→ trao Ring và lợi ích [chi tiết: UNKNOWN]
→ sống cùng Ring trong phần lớn cuộc đời; lựa chọn và trải nghiệm phát sinh
→ Greed yêu cầu trao trả
→ tự nguyện tháo và trao trả?
    CÓ   → chu trình Ring khép theo điều kiện tự nguyện
    KHÔNG → giao chiến
             Greed thắng → Ring bị phá hủy, không thu hồi bằng vũ lực
             kết quả khác → UNKNOWN
```

Trải nghiệm của người nhận là thứ Greed thu nhận theo nguồn. Thành công, thất bại và lựa chọn của người nhận không được định sẵn. `the ring.txt` có bước “Đạt được thành công”, trong khi bản hợp nhất ghi cả thành công và thất bại; bản này không biến thành công thành điều kiện bắt buộc.


## Quy trình chi tiết của interface Ring

1. Greed chọn một người phù hợp và trao Ring. Tiêu chí chọn và điều kiện tiếp nhận chưa được xác định.
2. Ring cho người nhận lợi ích trong phần lớn cuộc đời. Lợi ích cụ thể chưa được xác định; yêu cầu thiết kế của nguồn là đủ tạo thay đổi và lựa chọn có ý nghĩa nhưng không làm phép thử mất giá trị.
3. Trải nghiệm, lựa chọn, thành công và thất bại của người nhận phát sinh trong đời sống cùng Ring; Greed thu nhận trải nghiệm đó theo nguồn. Cách thu nhận chưa được mô tả.
4. Greed trở lại và yêu cầu người nhận **tự nguyện tháo Ring, trao trả**. Đây là điều kiện hoàn tất được nêu rõ.
5. Nếu người nhận từ chối, Greed giao chiến. Nếu Greed thắng, Greed phá hủy Ring thay vì lấy lại bằng vũ lực. Kết quả khi Greed không thắng là `UNKNOWN`.

Phép thử cuối cùng là người nhận có thể tự nguyện buông lợi ích sau thời gian dài hay không. Nó không phải phép đo ai mạnh, giàu hoặc thành công nhất. `the ring.txt` có bước “Đạt được thành công”; bản hợp nhất ghi cả thành công và thất bại, nên thành công không được đặt làm điều kiện bắt buộc của interface này.


Chi tiết vai trò vật thể/interface xem [Ring](COMPONENTS/Ring.md). Sơ đồ và danh sách bước ở trên là hai cách trình bày cùng cấu hình có nguồn, không là hai vòng độc lập và không xác nhận cấu hình Greed phổ quát.
