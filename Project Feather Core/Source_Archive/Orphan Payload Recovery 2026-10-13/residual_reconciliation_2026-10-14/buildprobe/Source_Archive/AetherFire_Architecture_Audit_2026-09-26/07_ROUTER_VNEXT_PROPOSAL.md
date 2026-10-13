# Đề xuất Router vNext

Trạng thái: **PROPOSAL — không thay Router v3.2**. Đây là hợp đồng thuật toán/đọc nguồn, không tuyên bố có Router executable đã cài.

## 1. Bootstrap không phụ thuộc chính registry chưa đọc

Entry point được người dùng/môi trường chỉ định pin một descriptor. CI đọc tối thiểu descriptor version, control binding và compatibility trước khi trao routing cho Router. Descriptor và schema validator không được tự lấy version bằng catalog đang cần validate.

Reader pin một snapshot duy nhất cho cả lượt. Đối với Git, xác nhận commit thật rồi đọc mọi source/control tại commit ấy; blob SHA riêng không phải commit SHA. Đối với bundle local, kiểm generation và digest artifact. Upload thiếu descriptor hoặc lẫn generation: không gọi nó là current package đủ nguồn.

## 2. Phân loại thao tác

`LOOKUP`, `BOUNDED_ANALYSIS`, `SIMULATION`, `DOMAIN_AUDIT`, `STRUCTURAL_CHANGE`, `CANON_MUTATION` là task families định tuyến, không truth statuses. Mutation authorization là trường độc lập, không suy từ task family.

Input chưa rõ chỉ ảnh hưởng candidate selection, không cấp quyền kết luận. Lưu request scope, timeline/POV nếu material và những predicate chưa xác định. Registry search aliases/domain labels chỉ tìm candidate; source authority phải qua accepted binding.

## 3. Thuật toán nạp đề xuất

```text
resolve_entry_point_and_pin_snapshot()
validate_descriptor_controls_schema_features()
classify_operation_scope_authorization_without_conclusions()
discover_candidate_modules_from_catalog_and_search()
verify_candidate_authority_and_source_bindings()

if user_requires_full_read or domain_audit or broad_structural_change:
    choose_full_affected_sources()
else:
    seed_reviewed_target_nodes()

repeat until no new references:
    for each newly touched module:
        add_module_mandatory_context()
    add_node_context_and_required_evidence()
    evaluate_conditions_as_TRUE_FALSE_UNKNOWN()
    add_relevant_interface_facets_and_required_sources()
    add_issue_state_and_decisive_reconciliation_evidence()
    add_required_overlays_and_their_transitive_dependencies()
    validate_refs_roles_revisions_and_scope()

if semantic_mapping_unreviewed_or_stale:
    expand_full_affected_scope_or_block_dependent_conclusion()
read_all_selected_content_and_track_actual_read_coverage()
reconcile_current_claims_unknowns_and_new_sources()
recheck_newly_discovered_dependencies()
verify_decisive_evidence_for_each_material_conclusion()
execute_only_within_verified_boundary()
```

Node/overlay nạp thêm có thể kích hoạt issue/interface khác, nên cần fixed point qua **mọi lớp**, không một pass canon rồi một pass overlay đóng cứng. Router không được kết luận trong khi discovery. Cơ chế này chọn closure theo declarations đã review; source phát hiện edge mới sẽ invalidate completeness receipt và mở rộng lại.

`REQUIRES_EVIDENCE` cycle không làm vòng lặp vô hạn: visited theo ID+revision. Two-way interface không đồng nghĩa authority cycle. Derivation/supersession cycle là validation error theo schema. Điều kiện UNKNOWN không tự bị bỏ; nạp conservatively nếu còn bounded, nếu không block đúng kết luận.

## 4. Khi phải full-read và khi full-read không đủ

Full affected file/module khi user yêu cầu, domain audit, rewrite rộng, dependency/segmentation review chưa có, selector stale, open evidence cần toàn context hoặc impact chưa đủ căn cứ. Full affected domain khi thay boundary/authority/primitive.

Full-read **không chữa** source mất, wrong snapshot, authority conflict chưa resolve, schema semantic không hiểu hoặc missing candidate module. Những tình huống đó phải block dependency, không quay lại lịch sử. Nếu toàn scope vượt khả năng đọc trong lượt, chia công việc bảo toàn scope với receipt hoặc trả kết luận bị giới hạn; không đánh dấu đã đọc toàn bộ chỉ vì tool đã tính hash.

Fallback độc lập registry cache chỉ hợp lệ nếu descriptor và raw source authority bindings còn kiểm được. Nếu mất catalog nhưng module bindings snapshot còn đủ cho câu hỏi hẹp, có thể full-read nguồn đó; structural mutation vẫn blocked. Mất cả bằng chứng authority → chỉ tiếp tục audit filesystem, không trả canon fact.

## 5. Failure codes và hành vi

| Code | Điều kiện | Hành vi |
|---|---|---|
| CONTROL_COMPATIBILITY_BLOCKED | Cặp CI/Router/schema/features không tương thích | Không execution phụ thuộc controls đó |
| SNAPSHOT_MISMATCH | File khác generation/hash | Không trộn; reload đúng snapshot hoặc block |
| STRUCTURE_LOAD_BLOCKED | Required ID/manifest/semantic field không resolve | Block affected closure; không tự sửa metadata |
| SOURCE_LOAD_BLOCKED | Thiếu decisive evidence/authority | Block kết luận đó, tiếp tục phần độc lập |
| SOURCE_LOAD_PARTIAL | Gap secondary đã chứng minh không đổi kết luận giới hạn | Nêu gap, không canon-complete |
| FULL_READ_REQUIRED | Node index/review không đủ | Mở rộng đọc current authoritative source |
| AUTHORITY_REVIEW_REQUIRED | Scope owner/transfer không được chứng minh | Không tự chọn theo version/time/path |
| IMPACT_UNVERIFIED | Consumer metadata chưa đủ | Không claim impact complete; mở rộng audit trước mutation |
| SUMMARY_REVIEW_REQUIRED | Owner revision thay đổi | Không dùng summary làm decisive premise |

Các mã là đề xuất control, không thêm lifecycle canon. Không trả cả checklist cho mọi câu hỏi; chỉ giải thích blocker/giới hạn material.

## 6. Receipt có thể kiểm lại

Receipt cần: request scope/task family; snapshot+controls+schema revisions; seeds; closure IDs+revisions; lý do nạp từng edge/mandatory context; bytes/sections đã đọc thực; issue refs; unresolved predicates; fallback đã dùng; các conclusion bị block/partial; validation tooling+result.

Receipt là audit artifact theo task, không thành source authority hoặc kho telemetry. Không cần log lâu dài mọi cuộc hội thoại. Hash chỉ xác nhận identity của dữ liệu; không chứng minh model đã đọc/hiểu hoặc đoạn source đủ nghĩa.

## 7. Ví dụ shadow trên repository thật

| Task | Định tuyến cũ hiện hành | Đề xuất sau review | Boundary phải giữ |
|---|---|---|---|
| Tra identity MC4 |00+92+60;10 khi Academy doctrine material | Whole-file node60; issue025/026/028 khi material; node10 context nếu cần | Không kéo legacy Tainted Cosmos thành current powers |
| Hỏi Creed quorum và relic loan có cùng thủ tục không |00+92+70+91 relevant |70§7/9 + mandatory context + AF-ML-005; thêm source theo evidence | Không suy cùng số3 là cùng procedure |
| Quyền RF mở tuyến bay |00+92+80+10+91 relevant |80§4/7/10 + RF authority context10 + AF-AV-002/AF-OPEN-016 | RF union/member-state allocation còn UNKNOWN |
| White đổi status khi nào |00+92+30+20+91 relevant | Node boundary White/status, điều kiện/unknown đi kèm | Không cắt qualifier “cho đến khi transition hoàn tất” |
| Retcon aviation premise đã được chấp thuận | Full affected domains | Reverse impact80→10/91/92/TotalWar/case/recipe; rồi full affected source | Không đánh dấu tests ACTIVE hoặc quyết định những unknown không liên quan |

Các tập node trên là ứng viên thiết kế, **chưa đủ để nạp node ngoài full-read rule hiện hành**. Marker/edge map phải được review trước activation; hiện chưa có số đo tiết kiệm context đáng tin cho các route này.

## 8. Authority transfer và canon mutation

Router đọc quyết định scope cụ thể, tính reverse closure bắc cầu rồi mới giao cho editor thực hiện. Decision canon không mặc nhiên cho major restructure; structural follow-up có thể được ghi riêng, nhưng không publish gói bị lệch. Nếu user chỉ duyệt một claim, không dùng transaction để đóng issue lân cận.

Canon mới từ proposal đi qua admission: unconfirmed source → scoped acceptance → immutable provenance → editable binding/recipe đúng scope → output+reconciliation/issues+views → validation → accepted-local → published khi được phép. Không dùng registration thành promotion.

## 9. Quy tắc mở rộng

Router hiểu record types và edge semantics, không biết danh sách quốc gia/module cụ thể. Module mới dùng primitive hiện có chỉ thêm dữ liệu. New relation **trong lore** không tự là schema primitive mới; chỉ thêm edge semantic khi failure không thể biểu diễn bằng read/authority/derivation/interface contracts sẵn có và đã qua review.
