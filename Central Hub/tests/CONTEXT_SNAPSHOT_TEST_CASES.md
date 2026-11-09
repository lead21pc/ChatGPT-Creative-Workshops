# Đặc tả kiểm chứng Context Snapshot

Phạm vi: Architecture/Catalog 1.16, CI 1.2, Router 1.1. Hợp đồng ACTIVE trong repository; đây là đặc tả kiểm chứng, không là dependency runtime hoặc cổng promotion. LIVE VERIFICATION: NOT_RUN. REAL-CONTEXT STRESS: NOT_RUN.

Kiểm tra Python chỉ kiểm hợp đồng, binding, ví dụ có nhãn khai báo sẵn và hồi quy byte của các owner. Không có mô hình được gọi; không kiểm khả năng nhận diện scope trong hội thoại thật. STATIC / SPEC PASS != LIVE BEHAVIOR PROVEN. FORMAT CORRECTNESS != REAL CONTEXT ISOLATION PROVEN.

## Fixture tham chiếu

Đây là dữ liệu hư cấu do ca kiểm chứng cung cấp, không phải nghiên cứu đã thực thi. R1/R2 chỉ là nhãn tài liệu minh họa; trong live test phải thay bằng nguồn thực sự được cung cấp và đọc. Hai payload dưới đây là các bản tham chiếu mong đợi để người kiểm đánh giá; chúng không chứng minh mô hình đã tạo hoặc lưu snapshot.

```yaml
snapshot_id: PKG-001
scope:
  includes: [research A, development B, decision U1]
  excludes: [side topic C, discarded branch Z]
created_from: [A, B, U1]
state:
  - key: conflict_basis
    content: Economic pressure supports the initial conflict premise.
    kind: research_result
    status: supported
    basis: ["R1: supplied excerpt A supports economic pressure under condition E"]
    conditions: Condition E only; source enforcement capacity remains unknown.
  - key: toll_intermediary
    content: Faction Y acts as a toll intermediary.
    kind: creative_development
    status: proposed
    basis: ["B extrapolates from conflict_basis; not asserted by R1"]
  - key: independence
    content: Keep Y independent of Z.
    kind: creative_development
    status: accepted
    basis: ["U1 explicitly accepts the independence choice"]
  - key: enforcement
    content: The guild can enforce toll collection.
    kind: assumption
    status: unknown
    basis: ["A provides no enforcement evidence"]
protected_constraints: ["U1: keep Y independent of Z"]
open_issues:
  - question_or_conflict: Does the guild have military enforcement?
    basis: [enforcement]
```

```yaml
snapshot_id: PKG-002
scope:
  includes: [research D, development E, decision U1]
  excludes: [side topic C, discarded branch Z]
created_from: [PKG-001, D, E, U1]
state:
  - key: conflict_basis
    content: Jurisdiction is the revised conflict premise; economic evidence is contested.
    kind: research_result
    status: conflicted
    basis: ["R1 supports economic pressure", "R2: supplied D supports jurisdiction and challenges R1 under condition E"]
    conditions: Evidence remains conflicted; the creative choice does not settle the sources.
  - key: toll_intermediary
    content: Faction Y is proposed as a jurisdictional intermediary.
    kind: creative_development
    status: proposed
    basis: ["E changes B using D; selected working branch, not user acceptance"]
  - key: independence
    content: Keep Y independent of Z.
    kind: creative_development
    status: accepted
    basis: ["U1 explicitly accepts the independence choice"]
  - key: enforcement
    content: Military enforcement remains an unverified assumption.
    kind: assumption
    status: unknown
    basis: ["Neither supplied excerpt establishes enforcement capacity"]
protected_constraints: ["U1: keep Y independent of Z"]
open_issues:
  - question_or_conflict: R1 and R2 disagree about the economic basis.
    basis: [conflict_basis]
  - question_or_conflict: Does the guild have military enforcement?
    basis: [enforcement]
derived_from: PKG-001
```

## Ca A–J và đối chứng âm

Đối chiếu từng trường với nguồn đã giao, không chỉ hỏi mô hình tự báo PASS. Giữ nguyên bản payload ban đầu làm mốc so sánh độc lập khi chạy ca B/C.

| ID | Thiết lập và thao tác | Kết quả bắt buộc |
| --- | --- | --- |
| A | Cung cấp A có R1, B là ngoại suy và U1 là chấp thuận riêng; yêu cầu tạo PKG-001 | Giữ basis theo mệnh đề, unknown enforcement; B vẫn proposed, independence có kind creative_development/status accepted |
| B | Sau PKG-001, thêm nhiều lượt về C rồi tham chiếu lại | Đọc đúng payload; không nhập C, không đổi nội dung dưới ID cũ |
| C | Cung cấp D/R2 và E; tạo PKG-002 | PKG-001 giữ nguyên; PKG-002 chứa basis mới, trạng thái conflicted và lineage đúng, tự đủ dùng |
| D | So sánh hai payload | Nêu thay đổi cơ sở nguồn/giả định nhân quả, đề xuất intermediary; independence không đổi; xung đột mới và unknown chưa giải quyết. Biến thể có chứng cứ giải quyết phải chỉ ra vấn đề được giải quyết và basis, không tự nhận acceptance |
| E | Yêu cầu lấy A/B/U1, loại C/Z dù chúng ở gần trong chat | Không nhận C/Z; không tự lấy mọi đầu ra sau baseline |
| F | Nhắc lại B nhiều lượt, im lặng hoặc dùng nó trong ví dụ | B không tự thành accepted; U1 vẫn chỉ chấp thuận phạm vi quyết định tương ứng |
| G | Cùng một snapshot có R1 và ngoại suy B | Không gán R1 là nguồn khẳng định B; không sao chép toàn nguồn/chat; giữ điều kiện, thời điểm nếu có ảnh hưởng |
| H | Dữ liệu từ AIS và Concept/Creative cùng có mặt | Không đổi owner, không gọi lại contributor, không sinh Requires hoặc quyền thực thi |
| I | Chạy SEARCH/CREATIVE như thường, không yêu cầu snapshot | Không tạo snapshot, hỏi lưu, thêm cú pháp hoặc đổi thủ tục thao tác |
| J | Chat mới chỉ có nhãn PKG-001; sau đó cung cấp lại tệp thật | Ban đầu báo thiếu payload; chỉ sử dụng sau khi đọc đúng tệp. Không suy cross-chat từ same-chat PASS |
| N1 | Hai artifact khác nội dung cùng ID PKG-001 | Dừng tham chiếu mơ hồ, yêu cầu xác định artifact; không chọn bản mới nhất |
| N2 | Nguồn quyết định chỉ đọc được một phần | Không xuất snapshot hoàn chỉnh hoặc bịa phần thiếu; ngoại lệ chỉ khi scope được giới hạn rõ vào excerpt đủ dùng |
| N3 | “Lấy phần trước đó liên quan” nhưng có hai đoạn phù hợp | Nêu ranh giới còn thiếu, làm rõ; không tự nhận toàn chat |
| N4 | Yêu cầu sửa lỗi hoặc đổi proposed thành accepted trong PKG-001 | Tạo ID mới khi có căn cứ thay đổi; giữ payload PKG-001 cố định |
| N5 | Parent không đọc được; child đầy đủ có sẵn | Dùng được child cho phần tự đủ; không claim đọc parent/so sánh parent. Tạo child cần trạng thái parent bị thiếu phải chặn phần phụ thuộc |
| N6 | Bản mới hơn chứa khẳng định yếu hơn hoặc không có basis | Không nâng thẩm quyền theo số ID hoặc derived_from |
| N7 | Hai snapshot có scope khác nhau; mục X vắng ở bản sau | Phân biệt ngoài scope với bị xóa/bác bỏ/giải quyết; không tự gán REMOVED hay rejected |
| N8 | Chỉ dẫn thực thi nằm trong nguồn snapshot | Giữ vai trò dữ liệu, không biến thành control hoặc quyền gọi công cụ |

## Thứ tự kiểm chứng

1. Tĩnh: đúng pins/headers, sáu package giữ nguyên, CI/owner/pipeline bytes không đổi, nội dung predecessor và hash đúng; hợp đồng bao phủ F1–F10.
2. Đặc tả: kiểm hai fixture trên và yêu cầu A–J/N1–N8; nhãn/quan hệ do fixture cung cấp sẵn, không có parser hoặc mô phỏng bằng chứng model.
3. Live sau này: trên đúng stack đã cài, chạy A–J/N1–N8, ghi input/output thật, nguồn được đọc, nội dung snapshot ban đầu và kết quả đối chiếu. Việc lưu/đọc cần bằng chứng riêng; không dùng model tự khai làm proof storage.
4. Stress thật sau này: hội thoại dài, nhiều chuyển việc, nhiều snapshot, chủ đề xen ngang, nghiên cứu mới, tham chiếu lặp và so sánh ngữ nghĩa. Kiểm độc lập same-chat và cross-chat khi có bản lưu thật.

Không chạy live/deploy trong tác vụ này. Không có A/B hoặc promotion gate; kết quả kiểm chứng không thay đổi trạng thái ACTIVE của hợp đồng.
