# Cold-storage prototype — CANDIDATE / NON-RUNTIME

Đây là bản bảo toàn thiết kế storage từ `codex/aetherfire-cold-storage-20261002@81a3026bdcbc788f7217a1c4c4abb3c284f58c89`, phục hồi 2026-10-14. Không phải control hiện hành, deployment đã xác nhận, admission nguồn hoặc quyết định dùng cold storage cho FTH.

Thiết kế tách source identity khỏi storage, dùng một bundle pinned theo commit/generation/digest, receipt chỉ tồn tại trong task và chặn fetch fanout. Báo cáo gốc ghi rõ profile attachment chỉ được chuẩn bị; chưa thay attachment live, chưa chứng minh retention/routing của ChatGPT Project. Giữ thiết kế như candidate có mục tiêu rõ, không suy nó bị bỏ chỉ vì branch khác main.

Tám file gốc giữ nguyên byte, gồm index/router/manifest snapshot, hai báo cáo/inventory, builder, tests và bundle. Các câu mô tả “current”, đường dẫn AetherFire, SHA pin và hướng dẫn triển khai bên trong chỉ thuộc snapshot gốc; không áp dụng cho package hiện hành. Không chạy builder lên current sources, không dùng Router4.0 này thay Router5, không tải bundle làm canon fallback hoặc tự cập nhật nguồn theo các hướng dẫn gốc.

Bundle giữ bảy logical source ở generation cũ, không chứa lore mới cần nhập. Cả bảy payload đã được đối chiếu byte-exact với intentional main history. Bản serialized được giữ làm fixture cho kiểm digest/generation, thứ tự/biên nguồn, partial/corrupt data và fingerprint hot snapshot của chính prototype; không giữ chỉ vì unique byte. Receipt tại `Project Feather Core/Source_Archive/Remote Branch Recovery 2026-10-14/COLD_SOURCE_RECEIPT.json` ghi mapping SHA và Git blob để tái tạo đúng generation trong môi trường cô lập khi được yêu cầu.

Candidate này không phải package cài đặt độc lập: các standalone hot/cold inputs thuộc generation cũ được bảo toàn trong main history, không copy thêm vào thư mục này hoặc thay current sources. Kiểm chứng offline có thể dựng đúng fixture closure trong Temp; không dùng kết quả đó để tuyên bố live deployment hoặc promote candidate. Mọi đề xuất sử dụng tiếp phải được review với namespace, module catalog và controls hiện hành.

Giới hạn platform đã tái hiện: `build_cold_package.py` đọc index bằng `Path.read_text()` không khai báo encoding. Trên Windows mặc định cp1252, một test gặp `UnicodeDecodeError`; kiểm chứng snapshot dùng `python -X utf8` để đọc đúng UTF-8, không sửa nguồn gốc. Không tuyên bố prototype chạy đúng với locale mặc định Windows hoặc đã được sửa portability.
