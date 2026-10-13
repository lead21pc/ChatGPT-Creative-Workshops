# 07 — Migration shadow và kế hoạch thử nghiệm

> Kế hoạch cho các lượt **sau này**. Lượt audit 2026-09-29 không sửa runtime, không chạy builder trên project thật, không kiểm Project backend. Không stage/commit/push.

## P0 — Baseline và bằng chứng

Chụp snapshot có định danh của bản Project instruction CI, Router, từng Project-native source và overlay **thực sự được cài**, rồi so với bản repo. Ghi generation, hash/size, thời điểm lấy và danh sách source thiếu/khác. Không suy từ tên file hoặc repo rằng Project có đúng byte. Lập bộ prompt canon-dependent hẹp/rộng cùng expected evidence và truth status. Baseline cần giữ các câu mà đáp án đúng là `UNKNOWN`/`CONFLICTED` hoặc `SOURCE_LOAD_BLOCKED` khi nguồn quyết định thiếu.

## P1 — Router/CI proposal riêng, chưa activation

Soạn một bản contract đề xuất nói rõ CI ở Project instructions, Router không live-discover CI file, mode mặc định full, điều kiện node read hợp lệ, fallback và pre-response checks. Review bằng diff so với CI v2.6/Router v3.2; xác nhận không bỏ invariant và không cấp quyền cho design history. `60` bổ sung vào domain table. Việc cài lên Project là một yêu cầu triển khai riêng của người dùng.

## P2 — Bản sao shadow và structural validator

Tạo một **copy/fixture riêng** của source generation đã chụp. Chỉ trên bản sao này, thử chèn mandatory header, local index và marker vào `80`, sau đó `70`, rồi `30`. Không sửa `00–92` hiện hành trong P2. Dụng cụ local có thể parse Markdown và xuất báo cáo; Project runtime không cần chạy parser ấy. Nếu builder được thử, chạy chỉ trên copy/fixture và so nguyên vẹn canon content với baseline.

Structural gate tối thiểu:

- File tồn tại, ID node unique và ổn định trong một generation; marker ở đúng span, không nằm trong code fence hay heading giả.
- Index và content song ánh: không có orphan/duplicate/missing node; start/end anchor không trôi sau rebuild; `REQUIRES` target tồn tại và không tạo vòng không được xử lý.
- `92` hook vẫn có filename fallback; `91` record ID và addendum anchor resolve đúng nếu thử record mode.
- Toàn bộ current files, headers, qualifier/exception và unresolved labels còn nguyên meaning; local validator kiểm byte/section inventory, human reviewer kiểm semantic.
- Khi xóa/hỏng index hoặc node trong fixture, resolver buộc chọn full current file. Khi xóa full decisive source, báo blocked. Không có nhánh im lặng bỏ source.
- Rebuild fixture hai lần phải cho kết quả ổn định; không dùng kết quả này để khẳng định Project runtime.

## P3 — Pilot có đối chứng

Thứ tự: `60` làm control full-file → `80` small pilot → `70` medium → `30` large/stress. `10/20/40/50` chỉ mở sau khi pilot cho thấy header/closure review có hiệu quả. `90/91` phase riêng. Không ép `30` thành node mode nếu closure thực tế gần full. Anti-drift vẫn full. Mỗi pilot cần source snapshot cố định và bản full-file comparator.

## P4 — Paired semantic differential tests

Với cùng prompt, CI, Router, overlays, source generation và model/runtime tương đương tối đa, chạy hai arm:

```text
A: current full-file route
B: reviewed node closure route (hoặc fallback full)
```

Người chấm chỉ thấy prompt, câu trả lời và evidence citations/spans; không biết arm. Oracle là **bộ premise/status lấy từ source đã kiểm**, không phải câu trả lời của arm A. Trước test, đánh dấu những gì là decisive, những gì vẫn `UNKNOWN/CONFLICTED`, owner của mỗi domain và supersession quan trọng. So từng arm về missing decisive evidence, wrong authority, false resolution, stale canon revival, exception loss, unsupported certainty, unnecessary loads. Đo file/đoạn được nạp và latency/context chỉ khi Project cho quan sát đáng tin; nếu không, báo `UNMEASURED`.

Ví dụ case bắt buộc: `80` phân biệt stable aviation với all-flight/air supremacy; RF sovereignty vs ATC vs economy; `70` removal của punitive foreign-spy route và ML internal vs global owner; `30` MC2 exception, latest visual two-stage reading và không phục hồi Brown; `40/50` narrator split không thành ability transfer; `91` record cũ bị addendum mới override; `90` legacy debt/Temple/T route không tăng authority. Thêm prompt bất ngờ ngoài bộ lập chỉ mục để kiểm khả năng fallback.

## P5 — Project-runtime shadow test thật

Đây là bước **chưa thực hiện**. Tạo môi trường shadow trong ChatGPT Project theo cách người dùng chấp thuận, giữ source generation và controls có phiên bản; chạy paired tests ở P4. Kiểm model có thật sự thấy mandatory header + index + target + toàn bộ required nodes, hay chỉ thấy search excerpts. Khi bất kỳ đoạn bắt buộc không quan sát/không chứng minh được, đánh dấu **UNVERIFIED RUNTIME ASSUMPTION** và không activate mode node cho class/file ấy. Không dùng local filesystem/parser làm bằng chứng thay thế.

## P6 — Activation có giới hạn và rollback

Chỉ sau semantic review và Project shadow test đạt tiêu chí do người dùng duyệt, kích hoạt class/file hẹp bằng một snapshot nhất quán gồm CI instruction text, Router và Project-native source generation. Trước activation lưu bản controls và sources cũ. Nếu xuất hiện wrong authority, missed qualifier, false `UNKNOWN` resolution, mismatch generation hoặc Project retrieval mơ hồ, rollback mode/file về `FULL_FILE`, không chữa bằng giả định. Không cần rollback canon content vì node trial không được đổi canon. Mở rộng theo từng domain, không phát hành tất cả cùng lúc.

## P7–P8 — Nhánh sau

`91` record routing cần test addendum+record+comparison closure; `90` history cluster cần status-by-section review và anti-revival tests. Anti-drift node mode chỉ đánh giá khi full-file overlay đã đo được là bottleneck thực. Track B/C/D có kế hoạch riêng; chỉ đưa thay đổi builder sinh index và package consistency cần thiết vào một activation đã được giới hạn.

## Điều kiện dừng

Một pilot dừng ở full-file nếu human reviewer không thể chứng minh closure, validator thấy index stale, Project không cho thấy retrieval đủ, hoặc differential test có một sai lệch authority/truth-status nghiêm trọng. Không dùng tỷ lệ prompt “đúng” chung để che một lỗi canon hóa sai.
