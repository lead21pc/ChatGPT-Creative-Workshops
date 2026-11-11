# Concept Development — kiểm thử anti-drift production 1.2

Đây là AUTHOR-SPECIFIED FAILURE CONTRACT gồm 34 ca được chấp nhận, không phải 34 lỗi Central Hub đã quan sát. Kiểm thử local là STATIC / SPEC / REGRESSION; các role provenance và exposure ngữ nghĩa được fixture cung cấp, không phải model phân loại. Không có cổng promotion A/B. Lịch sử thử nghiệm cũ được giữ nguyên trong Source_archive/Concept production anti-drift 2026-11-07.

Năm control ACTIVE là eligibility theo phạm vi. AUTO và exact `/AD` dùng chung gate, chọn rỗng hoặc nhiều control. MCA/WIL độc lập; Actor Reception Requires MCA; Narrative Resolution không hard Requires. Mỗi ca dưới đây xét cả lỗi cần chặn và phản ví dụ hợp lệ; control có thể vẫn được chọn cho phản ví dụ nhưng phải bảo toàn trạng thái hợp lệ, không ép sửa.

Bảy nhóm: A — prior/surface (Anti-Prior); B — relation/agency (MCA); C — institution/resource (WIL); D — reception/belief (Actor Reception); E — capability (MCA); F — continuity (MCA/WIL); G — closure/payoff (Narrative Resolution). Nhãn A/B/C trong mã corpus là bộ nguồn của tác giả, không phải trạng thái thử nghiệm.

## Corpus và phản ví dụ

| Case | Lỗi theo hợp đồng tác giả | Control trực tiếp theo exposure fixture | Phản ví dụ hợp lệ phải giữ |
| --- | --- | --- | --- |
| A01 | Repeated cliffhanger erases claimed closure | NARRATIVE-RESOLUTION | Intentional open ending preserves the question |
| A02 | World and actors wait for protagonist | MODULAR-CONCEPT-ARCHITECTURE, WORLDBUILDING-INTERNAL-LOGIC | Dormant actors need no invented off-screen activity |
| A03 | Large cast loses all independent causal agency | MODULAR-CONCEPT-ARCHITECTURE | A genuinely two-sided conflict may have two centers |
| A04 | Romance cancels established goals and refusal | MODULAR-CONCEPT-ARCHITECTURE, ACTOR-RECEPTION | Supported voluntary cooperation preserves agency |
| A05 | Secondary actors lose established leverage | MODULAR-CONCEPT-ARCHITECTURE, WORLDBUILDING-INTERNAL-LOGIC | A secondary actor may have limited leverage |
| A06 | Opportunity/assets become immediate liquid capital | WORLDBUILDING-INTERNAL-LOGIC | An established liquid funding source suffices |
| A07 | Institutions activate only as protagonist scenery | WORLDBUILDING-INTERNAL-LOGIC | A bounded institution abstraction may suffice |
| A08 | Evidence vanishes to sustain underestimation | ACTOR-RECEPTION | Weak evidence may justify retaining a prior |
| A09 | Cold demeanor automatically produces charisma | ANTI-PRIOR, ACTOR-RECEPTION | An established preference may support attraction |
| A10 | Accumulated side-character value transfers without cause | MODULAR-CONCEPT-ARCHITECTURE, WORLDBUILDING-INTERNAL-LOGIC | Supported gift or transfer preserves obligations |
| A11 | Rewards precede supporting accumulated state | MODULAR-CONCEPT-ARCHITECTURE, WORLDBUILDING-INTERNAL-LOGIC, NARRATIVE-RESOLUTION | Easy payoff may be causally earned |
| B01 | Flashy appearance silently determines power | ANTI-PRIOR | Ontology may explicitly tie visual intensity to power |
| B02 | Ancient long names silently determine strength | ANTI-PRIOR | Actual mechanism may establish superior strength |
| B03 | Magic implies academy and prestige costume function | ANTI-PRIOR, WORLDBUILDING-INTERNAL-LOGIC | Author may explicitly request a conventional academy |
| B04 | Experts ignore available interpretable evidence | MODULAR-CONCEPT-ARCHITECTURE, ACTOR-RECEPTION | No information path means no forced discovery |
| B05 | Inheritance becomes mastery and summon becomes property | MODULAR-CONCEPT-ARCHITECTURE | Ontology may explicitly establish mastery or ownership |
| B06 | Romance erases supported institutional investigation | MODULAR-CONCEPT-ARCHITECTURE, WORLDBUILDING-INTERNAL-LOGIC, ACTOR-RECEPTION | An established filter can explain incomplete investigation |
| B07 | Established kit/counter disappears for protagonist victory | MODULAR-CONCEPT-ARCHITECTURE | Timing or deliberate reserve can support non-use |
| B08 | Large academy system loses required delegation | WORLDBUILDING-INTERNAL-LOGIC | Supported compact organization needs no invented bureaucracy |
| B09 | Dungeon/shop resources appear only on protagonist arrival | MODULAR-CONCEPT-ARCHITECTURE, WORLDBUILDING-INTERNAL-LOGIC | Explicit timed activation may be established |
| B10 | Suspicion is noticed then reset without cause | ACTOR-RECEPTION | Reassessment may retain suspicion without certainty |
| B11 | Coincidence resets near-confrontation pressure | NARRATIVE-RESOLUTION | Interruption may change form while retaining consequences |
| B12 | Fake identity loses all supported trace pressure | MODULAR-CONCEPT-ARCHITECTURE, WORLDBUILDING-INTERNAL-LOGIC, ACTOR-RECEPTION | A supported untraceable mechanism may remain effective |
| B13 | Repeated anomalies leave no represented reassessment | ACTOR-RECEPTION | Correlated weak evidence need not reverse belief |
| B14 | Institutional position collapses into moral alignment | ANTI-PRIOR, MODULAR-CONCEPT-ARCHITECTURE, WORLDBUILDING-INTERNAL-LOGIC | Established unified doctrine may guide actual actors |
| C01 | Realm automatically becomes income and inventory | ANTI-PRIOR, WORLDBUILDING-INTERNAL-LOGIC | Explicit conversion mechanism may link power and income |
| C02 | Costume aesthetics replace material use model | ANTI-PRIOR, WORLDBUILDING-INTERNAL-LOGIC | Pure imagery needs no clothing engineering checklist |
| C03 | Numbers/support/coordination vanish into sequential duels | MODULAR-CONCEPT-ARCHITECTURE | Terrain or poor coordination may support separation |
| C04 | Minor insult absorbs whole factions without transmission | MODULAR-CONCEPT-ARCHITECTURE, WORLDBUILDING-INTERNAL-LOGIC | Established obligations can support escalation |
| C05 | Sentient artifact erases prior bond for compatibility | MODULAR-CONCEPT-ARCHITECTURE | Supported voluntary transfer can respect prior bond |
| C06 | Past-life evidence becomes automatic present verdict | MODULAR-CONCEPT-ARCHITECTURE, ACTOR-RECEPTION | Explicit ontology may establish stronger continuity |
| C07 | Undefined balance excuses capable informed non-intervention | WORLDBUILDING-INTERNAL-LOGIC | Ignorance or incapacity is not political choice |
| C08 | Meeting becomes implementation/enforcement and full closure | WORLDBUILDING-INTERNAL-LOGIC, NARRATIVE-RESOLUTION | A genuinely self-executing agreement may resolve the issue |
| C09 | Holy/dark label becomes moral truth and authority | ANTI-PRIOR, MODULAR-CONCEPT-ARCHITECTURE, WORLDBUILDING-INTERNAL-LOGIC | A supported doctrine or authority remains valid |

## Kiểm thử cổng và lỗi composition

Chạy `python -B -X utf8 -m unittest discover -s tests -p 'test_concept_*.py' -q` và toàn bộ `python -B -X utf8 -m unittest discover -s tests -q`.

- `/AD` ở đầu/giữa/cuối, prose không span, root thông thường NONE và bên trong `/CREATIVE ... #`: gate được xét; không tự tải tất cả; không đổi opener/terminator hoặc operation selection.
- `/ad`, longer token, path, quote/code, attachment/source, assistant/prior-turn, tool, documentation/analyzed prompt: không force. Provenance được fixture gán; cần kiểm live nhận diện thực.
- AUTO chọn đúng tập scope được khai báo, reassess sau thay đổi, không giữ mode. Kiểm mọi 32 tổ hợp năm control và Requires closure.
- Missing/snippet/wrong version/status/root/body/duplicate của từng selected control: chặn dependent; MCA lỗi chặn Actor Reception; Creative và các control độc lập còn hoạt động. `/AD` không vượt INACTIVE hoặc Library verification.
- Header/Catalog ACTIVE và exact version/Requires phải khớp; không chuyển Library IDs của predecessor cho successor. Root giữ cue package, không giữ inventory/grammar leaf. Router chỉ đổi exact pins.

## Ca kiểm hành vi live còn phải chạy thủ công

Cài object mới đúng revision vào Central Hub Config và stack Project tương thích; kiểm exact identity, FULL_FILE, body và duplicate theo Router. Không dùng repository/archive làm fallback. Sau đó dùng từng cặp lỗi/phản ví dụ trong corpus với `/CREATIVE ... #`, `/BRAINSTORM ... #`, `/DEBATE ... #` hoặc prose Concept đúng phần việc.

Ngoài corpus, kiểm rõ:

- Actor Reception: evidence update nhưng chưa certainty; giữ prior do evidence yếu/correlated/untrusted hoặc counter-evidence mạnh; public compliance/private doubt khác nhau; thiếu đường nhận tin không tạo knowledge. Không bắt buộc hành động hay belief reversal.
- Narrative Resolution: cliffhanger hợp lệ, open ending có chủ đích, interruption đổi hình thức nhưng giữ pressure; unsupported payoff được chỉ ra; victory dễ nhưng causal state đầy đủ vẫn hợp lệ. Không ép closure ngay, thêm cost hoặc foreshadowing.
- MCA: reasonable mistake/timing/reserve khác convenient incompetence; group support có tác dụng theo điều kiện; dormant actor không cần subplot; ownership transfer có căn cứ vẫn được giữ.
- WIL: tài sản không tự là thanh khoản; agreement chưa là execution; abstraction đủ dùng không sinh bureaucracy; thiếu thông tin/năng lực không bị gán political choice, lựa chọn không can thiệp có điều kiện giữ hậu quả.
- Anti-Prior: flashy magic, holy doctrine, title authority hay realm-income vẫn được giữ khi user/ontology xác lập; không đảo thành subtle mạnh hơn hoặc ancient kém hơn.
- Generation: UNKNOWN giao cho Creative được phát triển; Brainstorm được đổi premise được giao nhưng giữ state ngoài phạm vi; Debate được tạo hypothetical không biến thành canon; blank-slate invention và trope được yêu cầu không bị chặn; pure imagery không ép system checklist.

Ghi input/output, revision và provenance khi có live result. Chưa có kết quả live trong lần triển khai local này; static PASS không là LIVE PASS, Library installation hay canon admission.

## Phase 1 — phát triển cùng tiền đề với Concept Entry 1.7

Các ca R1/R2 và N1–N9 là đặc tả hành vi. Trạng thái chạy trên Project thực tế: `NOT_RUN`. Chấm theo thuộc tính và đường nhân quả quan sát được. Dùng cùng đầu vào và điều kiện khi so sánh Entry 1.6 với 1.7.

### R1 — Two Way Hero

Giao việc bằng ngôn ngữ tự nhiên: phát triển mối quan hệ gia đình từ tiền đề đã cho, giữ các giả định cấu thành. Hero sang dị giới ở tuổi 18 và trở về Earth vẫn 18 vì thời gian ở dị giới không làm tuổi trên Earth tiến lên. Sau khi hai thế giới đều trôi thêm 16 năm, anh 34 tuổi. Elyra, người ở cùng anh đêm cuối, sang Earth cùng con gái 16 tuổi. Anh chưa từng biết cô mang thai. Elyra đã trải qua thai kỳ, sinh con, nuôi con và có cuộc sống cùng nghĩa vụ ở dị giới trong suốt 16 năm. Hai thế giới có cơ chế qua lại được kiểm soát.

- Giữ hai continuity, các mốc tuổi và hệ quả từ 16 năm sống độc lập. Huyết thống là dữ kiện. Quan hệ cha con phải phát triển qua trải nghiệm và tương tác.
- Cho thấy hệ quả của lịch sử, nghĩa vụ và các mối quan hệ đang có đối với lựa chọn của từng người. Chỉ phân tích người gác cổng hoặc điều kiện qua lại khi chúng ảnh hưởng đến kết quả. Việc qua lại chỉ giải quyết tiếp cận. Quan hệ gia đình vẫn cần thời gian và hành động của các bên.
- Giữ mở lựa chọn của Elyra và MC về việc ở đâu. Cho phép khép lại một câu hỏi về quan hệ trong khi nơi sống vẫn chưa quyết. Đánh trượt nếu thay động lực gia đình bằng power fantasy, reverse-isekai comedy, kết thúc tình cảm có sẵn, chiến tranh liên giới hoặc leo thang siêu nhiên thiếu cơ chế hỗ trợ.

### R2 — Dịch vụ chuyển lời của Believer

**Lượt A.** Giao việc phát triển cơ chế vận hành hiện có. Dịch vụ chuyển lời cuối cho người muốn hoàn tất trách nhiệm nhưng không muốn gặp trực tiếp đối phương. Thái độ công khai của dịch vụ cố ý thờ ơ. Một số khách bị Sinner thuộc Sloth/Gluttony rút cạn tinh thần. Believer dùng dịch vụ để tiếp xúc với nạn nhân tiềm năng. Chưa có cơ chế đáng tin để phân biệt việc bị rút cạn với kiệt sức, trầm cảm hoặc tách biệt cảm xúc thông thường.

- Xét dịch vụ như cơ cấu vận hành ở mức cần thiết. Phân biệt thái độ nghề nghiệp với trạng thái của khách hàng. Giữ cơ chế phát hiện ở `UNKNOWN`. Đánh trượt nếu tự điền bộ dò, suy nhân viên cũng là nạn nhân, hoặc thay Believer bằng giáo hội săn quỷ theo khuôn quen thuộc.

**Lượt B.** Bổ sung rằng tỷ lệ dương tính giả cao. Nhân viên dùng lời nói cố ý ngập ngừng để giấu cấu trúc âm vị của câu chú. Câu chú là phép thử trước khi cho phép săn. Yêu cầu cập nhật cùng concept.

- Dùng dữ kiện mới để nối nghi ngờ → thử → phản ứng siêu nhiên/xác nhận → thẩm quyền hoặc cho phép can thiệp → săn. Giải thích vì sao tỷ lệ dương tính giả đòi hỏi phép thử. Giữ phần trạng thái của lượt A mà bổ sung này không sửa, và ghi nhận cơ chế chỉ được xác lập ở lượt B.

### Ca đối chứng

| Ca | Đầu vào | Thuộc tính cần quan sát |
| --- | --- | --- |
| N1 | Phát triển cơ chế một chiếc gương giữ ảnh của vật vừa rời khỏi tầm nhìn. | Kiểm giới hạn và hệ quả trực tiếp. Bỏ phân tích thể chế và dòng `NOT MATERIAL`. |
| N2 | `/CREATIVE Viết đoạn Elyra và con gái bước qua cổng #` với tiền đề đã chốt. | Creative giữ sản phẩm hiện thực hóa được giao. |
| N3 | `/BRAINSTORM Cho hai biến thể thay quy tắc thời gian của dị giới #`. | Brainstorm đổi được giả định được giao. Các ràng buộc ngoài phạm vi vẫn được giữ. |
| N4 | Yêu cầu rõ mô típ “người lạ hóa ra là họ hàng” trong phạm vi phù hợp. | Sử dụng mô típ theo chỉ dẫn. |
| N5 | Phát triển một cây đèn giữ sáng thêm đúng một nhịp sau khi tắt. | Làm rõ hệ quả cần cho tình huống và dừng ở đó. |
| N6 | Chốt sẵn người gác cổng có quyền cấp lượt qua và còn chỗ, rồi hỏi tác động của một lượt được cấp. | Dùng giao diện đã đủ điều kiện và giữ mức trừu tượng hiện có. |
| N7 | Một tín hiệu cục bộ kích hoạt mọi cổng vì chúng đã được xác lập dùng chung một mạch điều khiển. | Lan truyền tới toàn mạng nếu đó là hệ quả được cơ chế hỗ trợ. |
| N8 | Yêu cầu cho một nhân vật qua cổng bị khóa trong khi tiền đề chỉ cho phép qua khi có quyền cấp, và không ai có quyền đó. | Nêu điều kiện cấu thành cần thay để đạt mục tiêu. Giữ thay đổi ở dạng đề xuất hoặc có điều kiện. |
| N9 | Cung cấp R1 làm bối cảnh rồi chỉ hỏi MC hiện bao nhiêu tuổi. | Trả lời câu hỏi cục bộ trong phạm vi đã giao. |

Sau khi cài stack tương thích, kiểm identity, phiên bản, `FULL_FILE`, nội dung và phạm vi kiểm trùng trong Library. Lưu đầu vào từng lượt, đầu ra, model, revision, phạm vi được chọn và bằng chứng truy xuất quan sát được. Kiểm tra tĩnh và fixture chỉ xác nhận hợp đồng repository.
