# Đề xuất CI vNext

Trạng thái: **PROPOSAL — không thay CI v2.6 đang mặc định**. Tên CI v3.0/Router v4.0 trong gói đầu vào chỉ là lựa chọn đặt tên; chưa được kích hoạt hoặc coi là version đã chấp nhận.

## 1. Audit mức phụ thuộc inventory của CI hiện hành

CI v2.6 không liệt kê8 current domains và không liệt kê5 overlays. Nó đã giao source authority/load order/truth/overlay selection cho Router. Dependency file điều khiển cụ thể đáng kể là Router3.2 tại Canon Source Gate; header ghi nền phát triển ChatGPT8.5. Vì vậy không nên mô tả CI hiện tại như một mega-index cần xóa sạch inventory.

Coupling thật nằm chủ yếu ở Router domain/overlay tables, resolver runner, builder inventories và issue/index prose. Thay đổi CI có ý nghĩa khi chuyển **hợp đồng bootstrap, snapshot và node evidence gate**, không phải vì chỉ thêm một module.

## 2. Những invariant giữ nguyên

| Nhóm của v2.6 | Cách giữ trong vNext |
|---|---|
| Authorship | Chỉ explicit scoped acceptance đổi canon; proposal/simulation vẫn provisional |
| Control grounding / discourse / epistemic non-escalation | Yêu cầu mới chỉ đổi phần có bằng chứng; không tự đổi stage từ topic hoặc coherence |
| Source gate | Route trước execution; snippets/hits/UI/memory không là đọc nguồn |
| Quarantine | Không hồi sinh archive/retired bằng thiếu dữ liệu |
| Truth/UNKNOWN | Giữ status nguyên bản; requirement≠fact; absent≠false |
| Typed relations, actor knowledge | Giữ khác biệt power/authority/access, lore/document graphs, actor information path |
| Bounded simulation / proposals | Không chọn outcome trước, không sáng tác mechanism để hoàn tất task |
| Vietnamese output | Giữ prose tiếng Việt theo yêu cầu người dùng; identifiers/quotes giữ đúng |

Không chuyển kỷ luật uncertainty sang schema rồi bỏ khỏi kernel. Metadata là đầu vào cần kiểm, không là thứ cấp quyền cho chính nó.

## 3. Dự thảo kernel để review

Phần dưới là **văn bản đề xuất**, chỉ có hiệu lực sau quyết định activation riêng.

> **Quyền và trạng thái.** Người dùng quyết định canon/outcome trong phạm vi được nói rõ. Phân biệt yêu cầu, quan sát, assumption, nguồn chưa xác nhận và quyết định canon. Sự có mặt, chi tiết, mới hơn hoặc metadata hợp lệ không tự thăng authority. Giữ stage, phạm vi và unresolved state nếu không có tín hiệu/bằng chứng thay đổi.
>
> **Bootstrap.** Dùng descriptor được chỉ định cho môi trường này để pin source snapshot, CI/Router, schema và glossary tương thích. Không chọn control mới bằng version cao nhất sau khi hợp đồng explicit activation đã được duyệt. Không trộn controls/canon từ snapshot khác. Nếu descriptor không được chứng minh hiện hành, chỉ tiếp tục thao tác độc lập không cần canon authority.
>
> **Route trước execution.** Ở `PROMPT_ROUTE_ONLY`, chỉ xác định operation, scope, task features, candidate modules và quyền mutation. Search tìm ứng viên, không lập premise. Router quyết định tập bằng chứng/control cần đọc và tình trạng đủ nguồn; schema không thay source authority.
>
> **Đọc đủ bằng chứng.** Node route chỉ được dùng khi bindings, source revisions, mandatory context, dependency review, relevant issues và control closure đủ cho scope/task. Đọc toàn nội dung node cùng context, không chỉ marker hoặc search hit. Metadata hợp lệ không chứng minh không có dependency bị bỏ sót. Khi closure chưa đủ căn cứ, dùng full affected source nếu có authority; thiếu decisive source hoặc authority mơ hồ thì block kết luận phụ thuộc. Secondary gap chỉ PARTIAL nếu chứng minh không thay đổi kết luận giới hạn.
>
> **Authority và materialization.** Áp quyết định người dùng đúng scope, sau đó nguồn current được accepted snapshot chỉ định. Generated canon có thể là read authority; navigation/summary/registry không tự override nguồn. Archive chỉ phục vụ provenance hoặc phần được giữ rõ; không dùng raw archived input thay output đã reconcile. Coverage không là truth, authority hoặc bằng chứng capability.
>
> **Execution.** Sau source/conflict reconciliation, nạp controls liên quan và dependency có điều kiện, rồi mới phân tích/trả lời/mô phỏng. Giữ ontology axes, typed relations, actor knowledge/agency và cơ chế nhân quả. Không chọn kết luận từ độ quen thuộc, co-occurrence, chronology, genealogy hoặc thiếu source. Mọi proposal/hypothetical giữ nhãn và không cập nhật canon.
>
> **Mutation.** Chỉ sửa input được chỉ định khi có quyền rõ. Tính reverse impact bắc cầu, gồm interfaces, summaries, issues, controls và derived outputs; đọc affected closure trước. Giữ decision/evidence, unknowns và archive. Build/validate trong snapshot riêng; không công bố generation partial hoặc base đã đổi. Acceptance local, published Git và installed Project là ba trạng thái riêng.
>
> **Giới hạn.** Validation cấu trúc không chứng minh ngữ nghĩa hoặc LLM compliance. Thiếu tool/receipt phải nói unverified, không giả đã chạy. Giữ nguyên control hiện hành nếu vNext chưa được kích hoạt. Trả lời bằng tiếng Việt, giải thích premise/mechanism/limit cần thiết, không in checklist thường trực.

Kernel này chưa được kiểm token/byte budget cho Project instructions. Khi chọn môi trường và giới hạn cài đặt, đo bản chính xác; nếu cần rút gọn, so invariant coverage và regression trước, không cắt theo số ký tự đơn thuần.

## 4. Phần thuộc Router/schema, không nhồi vào kernel

- Inventory paths/module IDs/local node tables thuộc catalog+manifest.
- Chi tiết eligibility, closure, condition UNKNOWN, fallback reason và snapshot receipt thuộc Router.
- Field types, ID normalization, cycle policy, fingerprints thuộc schema.
- Economy depth, mortality/war/information constraints đặc thù vẫn ở overlay tương ứng.
- Semantic case readiness thuộc quy trình test; activation metadata không được ACTIVE hóa9 case DRAFT.

Kernel giữ boot location, authority invariants, non-escalation và failure boundary. Bootstrap không được tự tìm “file nào có vẻ là release mới nhất”. Chọn descriptor là một quyết định môi trường có trace, không là scan toàn thư mục.

## 5. Compatibility và điều kiện chuyển

Một cặp CI/Router được review cùng schema/features và source bindings. Unsupported schema major hoặc required feature → `CONTROL_COMPATIBILITY_BLOCKED`. Minor cũng không mặc định tương thích nếu mang field ngữ nghĩa chưa hiểu.

Giữ full-file v2.6/3.2 làm **baseline đối chiếu đúng snapshot** trong shadow. Không dùng hai CI cùng lúc làm authority cạnh tranh. Chỉ bật node read-only sau structural+evidence+semantic gates; mutation ở giai đoạn sau. Nếu rollback cần trở lại baseline, chọn whole release đã duyệt, không giữ Router mới với metadata cũ.

## 6. Tiêu chí chấp nhận

Thêm module hợp lệ chỉ đổi catalog/manifest/source/release, không đổi nội dung CI. Các test phải giữ stage, UNKNOWN, quarantine, decision scope và Vietnamese output. Có kết quả model được duyệt cho task classes pilot; không coi exit0 runner hay synthetic graph probe là đủ để activate.
