# Archive nguồn The Kingdom

```text
ROLE: HISTORICAL / PROVENANCE ARCHIVE
READ-ONLY AFTER MIGRATION
NOT CURRENT AUTHORITY
NOT FALLBACK
NOT AUTOMATICALLY LOADED
NOT PERMISSION TO RESTORE OLD LORE
```

Archive giữ lịch sử, provenance, so sánh, audit và điều tra recovery khi được yêu cầu rõ. Current root chi phối trạng thái trong scope; archive chỉ là historical evidence. Không sửa historical content sau khi coverage được kiểm tra.

Nếu active source thiếu, giữ UNKNOWN/repository gap; không dùng archive để lấp gap, không reconcile bằng sửa lịch sử hoặc tự phục hồi lore. Chỉ đọc khi user yêu cầu history/provenance/audit/recovery hoặc active source dẫn rõ record cần đối chiếu. Link không chuyển authority.

`sources/`: container đã triết xuất; `law/`: bảy tệp legacy đã bị reset; `handoffs/`: recovery lịch sử; `context/`: analysis/ghi chú; `navigation/`: README/index trước migration; `controls/`: bản trước khi chỉ đổi tên quốc gia. Nhãn ACTIVE/CANON/CURRENT và next-entry trong historical file không là chỉ dẫn đang hoạt động.

Giữ byte-exact kể cả tên giữ chỗ, đường dẫn và link cũ không còn hoạt động sau relocation. Read-only local chỉ là bảo vệ phụ; quy tắc thẩm quyền ở đây mới là chính.
