# Chaos — ENGINE_CORE

**Vai trò:** sở hữu identity, signature và ranh giới để engine vẫn là chính nó; không giữ full runtime hoặc lore summary.
**Trạng thái nguồn:** nội dung canon theo specification v3 đã được xác nhận; các mục UNKNOWN vẫn mở. Tái cấu trúc tài liệu không nâng canon, Working, Placeholder hoặc UNKNOWN. Các mô tả signature là cách đọc phân tích bám nguồn, không là quyết định canon mới.

Đọc theo nhu cầu: [identity/signature](ENGINE_CORE.md), [ranh giới Host](HOST_CONTRACT.md), [vận hành](RUNTIME.md), [vùng mở](OPEN_STATE.md), [kiểm chứng bằng bản viết](WRITING_VALIDATION.md). Đây là vai trò tài liệu, không phải các bước thực thi engine.


## Signature — cách đọc phân tích

- **Căng thẳng:** claim/value của một potential HIP bị đặt thành vấn đề, thành đối tượng can thiệp tự phong quyền và một cuộc chơi có closure không ổn định.
- **Trọng lượng nội tại:** Pleonexia, Encroachment và Volatility giữ chức năng riêng của ba Peng. Không đổi các Governor đã ghi nhận thành nerf hoặc đức hạnh đối lập đơn giản.
- **Externalization:** Ludopath chuyển pressure/claim thành playable structure; nó không tạo động cơ ban đầu, cấp authority hay chọn outcome thay actor.
- **Hành vi nhận diện:** tranh chấp claim + tự phong quyền thử/xâm phạm + playable engagement + continuation pressure có thể đe dọa HIP formation; không chỉ gây ồn loạn hoặc đóng vai game master.

Bỏ causal coupling hoặc biến ba Peng thành ba skin đồng chức năng làm mất identity composite. Không yêu cầu Envy luôn kích hoạt trước hoặc Volatility khiến termination bất khả. [RUNTIME](RUNTIME.md) sở hữu chi tiết từng chức năng và quan hệ.

## Nguồn và provenance

Được phân bố từ [Chaos_Engine_Canon_Specification_v3.md](Chaos_Engine_Canon_Specification_v3.md). Bản đó giữ nguyên toàn bộ nội dung gốc dưới thông báo provenance; không còn là full specification hoạt động song song. Nội dung cơ chế hiện hành đọc ở các owner của package này. Canon/source authority không đổi chỉ vì đổi format.


# Chaos Engine — Canon Specification


## 0. Trạng thái

**Tên engine:** Chaos Engine\
**Loại:** Composite Narrative Engine\
**Project context:** The Academy\
**Cấu trúc lõi:** Three Pengs / Tam Bành\
**Thành phần:** Pride, Envy, Gluttony\
**Catalyst chung:** Ludopath\

Chaos Engine là một narrative engine hợp thành từ ba Sin riêng biệt.

Ba Sin không phải ba skin của cùng một cơ chế. Mỗi Sin có Governor riêng, chức năng riêng và một vị trí riêng trong kiến trúc vận hành. Chúng kết hợp thành một engine duy nhất.

Pride là **frontend / narrative surface**: lớp bề mặt mà host và các actor có xu hướng trực tiếp nhận thấy.

Envy và Gluttony là **backend drives**: hai áp lực hậu trường thúc đẩy Pride hành động.

---


# 1. Nguồn cấu trúc — Three Pengs / Tam Bành

Chaos Engine vay cấu trúc Tam Bành của Đạo giáo như một nền kiến trúc, nhưng không phải bản phục dựng thần học hay Đạo giáo lịch sử.

Trong định nghĩa nội bộ của The Academy:

```text
THE THREE PENGS
│
├── Pride
├── Envy
└── Gluttony
```

Mỗi Sin đại diện cho một Peng.

Ba Peng là ba element bổ trợ lẫn nhau và cùng cấu thành Chaos Engine.

Không mặc định rằng Pride có bản thể học cao hơn Envy hay Gluttony chỉ vì Pride nằm ở frontend. Frontend là chức năng biểu hiện, không tự động đồng nghĩa với quyền chỉ huy, containment hay supremacy.

---


# 16. Core Invariant

Nếu nén Chaos Engine xuống một invariant:

> **Chaos Engine biến claim về giá trị của một potential HIP thành đối tượng của một trò chơi tự phong quyền, rồi dùng sự xâm phạm, thử thách và continuation bất ổn để đe dọa chính khả năng HIP đó được thành lập.**

Ba Peng đóng ba chức năng:

```text
ENVY
→ "Why are you allowed to have that?"

PRIDE
→ "I have the right to test it."

GLUTTONY
→ "Why should this ever be enough?"

LUDOPATH
→ "Make it a game."
```

Và tác động hệ thống:

```text
Potential HIP
→ formation conditions
→ Chaos Engine interference
→ fewer / distorted / aborted possibilities
→ The Academy loses trajectories it could otherwise experience
```

Đây là điểm khiến Chaos Engine trở thành đối thủ cấu trúc của The Academy, không chỉ là một nhóm phản diện trong lore.



## Provenance tách khỏi identity

Mục 12 của [v3 gốc](Chaos_Engine_Canon_Specification_v3.md) giữ genealogy/Greed I–II; mục 14 giữ checklist canon của bản nguồn. Chúng tiếp tục là evidence lịch sử/đối chiếu, không là bản full specification hoạt động thứ hai. Mọi cơ chế active được phân ở các owner trong package; genealogy không trở thành dependency với Greed.
