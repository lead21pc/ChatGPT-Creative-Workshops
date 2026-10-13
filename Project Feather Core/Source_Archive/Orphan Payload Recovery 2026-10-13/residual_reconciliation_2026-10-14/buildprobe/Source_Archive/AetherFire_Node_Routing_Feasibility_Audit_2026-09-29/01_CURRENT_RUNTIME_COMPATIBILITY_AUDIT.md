# 01 — Khả năng tương thích với runtime hiện hành

> Trạng thái: **AUDIT / PROPOSAL**, ngày 2026-09-29. Không phải canon, không phải hợp đồng runtime đã kích hoạt. Không thay đổi `UNKNOWN / OPEN / DEFERRED / CONFLICTED`.

## Ranh giới bằng chứng và baseline

- Git root: `C:/Users/Sheeplark/Desktop/CI Versioning Audit & Changelog`; branch `codex/aetherfire-architecture-audit-20260926`; HEAD `f4b7780ac3090dd486cde9bdbe6340ca10cdd9c1`. Worktree đã bẩn trước audit; không thay đổi các mục có sẵn.
- Người dùng xác nhận **CI v2.6 đã cài trực tiếp vào ChatGPT Project instructions** và các Markdown `00–92`, Router v3.2, anti-drift overlays đã cài thành Project-native sources. Bản `AetherFire CI/AetherFire_CI_version_v2.6.md` trong repo chỉ là bản tham chiếu để phân tích, không chứng minh byte của instruction setting hoặc trạng thái upload hiện tại.
- Đã đọc bản tham chiếu CI, Router, 5 active overlays, `00` và toàn bộ `10–92` tại root. Repo xác minh nội dung Markdown và builder; không cho thấy cách backend ChatGPT Project truy xuất đoạn file. Mọi cam kết về truy xuất node/range là **UNVERIFIED RUNTIME ASSUMPTION**. [Tài liệu OpenAI về Projects](https://learn.chatgpt.com/docs/projects) mô tả Project instructions và uploaded files dùng chung cho các chat, không quy định bảo đảm truy xuất đúng node/range.

## Đường chạy phải dùng

```text
Project instruction đã chứa CI
→ CI gọi Router trong Project-native sources
→ Router chọn Markdown 00, 92, current-domain, 91 nếu liên quan
→ đối chiếu conflict/UNKNOWN và source gate
→ nạp overlay đúng domain và dependency của overlay
→ PROMPT_EXECUTION
```

Đây là mô hình runtime do người dùng cung cấp, **khác** mô hình resolver nằm trong Router bản repo. `Router → discover CI file → chọn numeric latest` tại Router v3.2 dòng 5–47 và 56–57 là một contract repo-centric; không được dùng làm mô tả live Project. `AetherFire CI/README.md` cũng phân biệt phát hành file repo với cập nhật ChatGPT Project.

## Vì sao kiến trúc hiện nay có thể hoạt động bằng Markdown

CI v2.6 là văn bản instruction trong Project. Nó giữ invariant về ngôn ngữ, phản hồi theo chức năng lượt nói, không chốt sớm và source gate ngay trong instructions; phần canon-dependent ở dòng 29–35 ủy quyền source authority, load order, truth status và overlay selection cho Router. Không có schema/registry bắt buộc để diễn giải các câu này. Khi làm canon-dependent work, CI yêu cầu đọc Router trước, chỉ route trong `PROMPT_ROUTE_ONLY`, rồi mới tuân thủ controls. Câu “filenames, excerpts, hits, summaries, memory, prior answers, and UI are not reads” là một phần quan trọng của gate; không thể đơn thuần gọi đoạn node là “đã đọc” theo contract hiện hành.

Router v3.2 là instruction contract viết bằng prose Markdown. Dòng 51–85 định nghĩa `PROMPT_ROUTE_ONLY → source read → reconciliation → overlay → PROMPT_EXECUTION`, chặn kết luận khi thiếu nguồn quyết định và giới hạn `SOURCE_LOAD_PARTIAL` cho khoảng trống thứ cấp thật sự. Dòng 139 trở đi định tuyến theo **file/domain**, luôn đọc `00` và `92`, đọc các current files bị tác động, dùng entry `91` khi quyết định conflict, rồi nạp overlay sau source gate. Dòng 81 yêu cầu đọc **toàn bộ mọi routed file**, theo nhiều đoạn liên tục khi file dài. Quy tắc này giảm nguy cơ cắt mất ngoại lệ nằm xa tiêu đề, priority bổ sung và mệnh đề phủ định.

Router có quyền điều phối nguồn và trạng thái sự thật; overlay chỉ điều khiển cách suy luận trong scope. Dòng 159–187 của Router đòi resolve overlay theo version/status, nạp các dependency control theo quan hệ bắc cầu, và không cho overlay sửa hierarchy/canon. `Mortality…` kế thừa `Modular…`, thêm `Total War…` khi conflict/war/extraction liên quan; `Worldbuilding…` có interface với `Economy…`. Các active overlay có header type, phạm vi, loại trừ, kế thừa authority, điều kiện kích hoạt và điều kiện mở/dừng; giữ `FULL_FILE` ở phase đầu là hợp lý vì chúng là control contract, không phải lore dài cần tối ưu.

| Active overlay | Header/activation đã xác minh | Open/stop và phụ thuộc cần bảo toàn |
| --- | --- | --- |
| `Interface_Economy_State_Stabilization_v1.1` | Local anti-drift config cho economy–institution interface; kế thừa CI/Router, không tạo canon | `MUST_OPEN` khi tầng ẩn có thể đổi kết luận; `MAY_STOP` khi điều kiện task-local được giải ở độ sâu cần thiết; không mở full economy model theo mặc định. |
| `Modular_Concept_Architecture_v1.0` | Post-source-gate architecture/simulation overlay; chỉ chạy sau route, source và reconciliation | Mở đúng distinction ảnh hưởng branch/compatibility; giữ module autonomy và typed relation, không áp fixed universal schema. |
| `Mortality_Relationship_Plot_Immunity_v1.1` | Simulation/narrative-causality overlay; kế thừa Router và Modular | Không chọn survival/death theo importance; nạp Total War có điều kiện khi operational conflict thuộc scope. |
| `Total_War_RP_v1.1` | Simulation-control cho war/crisis/conflict theo scope, kế thừa control layer | Không bịa authority/resource/path để chạy simulation; thu hẹp scope không giảm causal rigor. |
| `Worldbuilding_Internal_Logic_v1.1` | Design-time system-coherence overlay, không tạo canon | Với economy/labor/trade/logistics thì route Economy overlay; Economy kiểm `MUST_OPEN`/`MAY_STOP` trong miền của nó. |

## Vai trò thực tế của `00–92`

| File | Vai trò đã thấy trong repo | Hệ quả routing |
| --- | --- | --- |
| `00` | Chỉ mục **và** ranh giới semantic/supersession chung; 143 dòng | `FULL_FILE`; chỉ thêm bảng domain→file→mode nếu sau này cần, không thay semantics. |
| `10–80` | Current-domain generated views, có authority và cross-domain boundary ở đầu hoặc trong các phần sau | Có thể thử node theo từng domain; không đồng nhất kích thước với mức an toàn. |
| `90` | Design history/reconsideration, 4060 dòng, trộn nhãn current/retired/under consideration ở cấp mục | Chưa nên route theo “history cluster” đơn giản; nguy cơ hồi sinh legacy cao. |
| `91` | Control/evidence record, 640 dòng; addenda đầu file, Part I summary và Part II `AF-CX-001..019` | Có hình dạng record nhưng priority đầu file và bảng cuối cũng có thể quyết định; thử `RECORD_OR_FULL` sau. |
| `92` | Open-issue/control ledger, 105 dòng; ID, state, required baseline và link `91` | `FULL_FILE`; hook node chỉ là bổ sung, không thay tên file fallback. |

`60` chỉ 68 dòng nên `FULL_FILE` rõ ràng. `80` 427 dòng là ứng viên pilot nhỏ. `70` 873 dòng là pilot vừa. `30` 4163 dòng là stress case: nhiều thay đổi/ngoại lệ nằm sâu trong Part IV, không thể coi bốn Part là bốn node độc lập.

## Thuộc tính không được phá

1. CI invariant và source gate vẫn ở Project instructions; metadata trong file không được thay vai trò này.
2. Route không được thành kết luận. Chỉ execution sau khi premise và overlay thật sự sẵn sàng.
3. `00` và `92` vẫn là ngữ cảnh toàn cục đọc đầy đủ; `91` không được mất priority/addendum mới nhất.
4. Node không phải một authority mới. Current canon, issue status và reconciliation precedence không đổi; `UNKNOWN` không bị suy thành `FALSE` hoặc được giải tự động.
5. Khi không chứng minh được closure, đọc toàn bộ **current file** liên quan; khi chính source quyết định thiếu, báo `SOURCE_LOAD_BLOCKED` theo gate hiện hành. Không biến fallback thành tuyên bố đã đọc khi backend chỉ trả excerpt.
6. Overlay phải có mặt và được nạp nguyên file theo dependency/scope; thiếu overlay bắt buộc vẫn block đúng operation.

## Giới hạn xác minh

Đã xác minh cấu trúc local và prose contract bản repo, chưa xác minh byte của các bản đã cài trong Project, behavior truy xuất Project, chi phí token/latency hay chất lượng trả lời của model trong Project. Những điều đó cần shadow test ở tài liệu `07`.
