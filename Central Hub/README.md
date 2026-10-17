# Central Hub

Trạng thái: triển khai local chính thức. Chưa deploy vào ChatGPT Project; chưa stage, commit hoặc push.

[Hub CI](HUB_CI_v1.0.md) kế thừa ngữ nghĩa ChatGPT v9.0; [Hub Router](HUB_ROUTER_v1.0.yaml) chọn riêng domain, capability và tool pipeline theo từng phần task. Chat/support/viết thông thường vẫn do Hub CI làm trực tiếp. Domain và capability không tự kích hoạt nhau hoặc công cụ.

AIS là pipeline nghiên cứu; ImageT là controller ảnh có Ready Gate active theo xác nhận của người dùng trong task migration. Metadata nguồn cũ ghi candidate không phản ánh xác nhận này. Preference humanoid vẫn thử nghiệm, inactive, chỉ nhận full text trực tiếp khi được chọn riêng cho một operation.

Trong deployment tương lai, chỉ Hub CI ở Project instructions; Hub Router và control được chọn ở Project Sources. Đường dẫn repository dùng để kiểm local, không thay cho nguồn runtime. Tệp test và archive không phải control runtime. Task này không thực hiện deployment.

[Báo cáo migration](MIGRATION_REPORT.md) ghi nguồn, mapping, hashes và bằng chứng kiểm tra. [Các ca Hub](tests/HUB_ROUTE_TEST_CASES.md) là đặc tả, không chứng minh hành vi model. [Source_archive](Source_archive/README.md) chỉ giữ lịch sử; không fallback hoặc tự rollback.
