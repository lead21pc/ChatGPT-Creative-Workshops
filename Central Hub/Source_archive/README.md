# Lưu nguồn lịch sử của migration

ARCHIVE != RUNTIME SOURCE

ARCHIVE != FALLBACK

ARCHIVE != LATEST VERSION

ARCHIVE PRESENCE != ACTIVATION

Chỉ dùng để xem lịch sử, đối chiếu, audit hoặc rollback có đích do người dùng chỉ định. Không router/control nào được tự đọc archive để bù nguồn thiếu, tự phục hồi hoặc chọn bản mới nhất. Chỉ đọc về governance; không sửa bytes đã lưu nếu chưa có chỉ dẫn rõ.

Migration giữ toàn bộ bytes của ba cây nguồn cũ. Các thư mục archive cũ được đặt tên `historical_sources` bên trong lịch sử để toàn Hub có một root Source_archive. Mapping đường dẫn cũ, đích và SHA-256 nằm trong `ARCHIVE_RECEIPT.json`; receipt là bằng chứng tệp, không phải registry hoặc authority runtime. Tài liệu cũ có thể chứa liên kết/metadata của kiến trúc đã nghỉ; không dùng chúng như chỉ dẫn hiện hành.
