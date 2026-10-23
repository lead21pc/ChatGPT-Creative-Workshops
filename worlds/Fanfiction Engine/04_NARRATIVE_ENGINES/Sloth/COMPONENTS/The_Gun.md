# Sloth — The_Gun

Owner của cơ chế component theo nguồn. Phần operational chi tiết được giữ nguyên; Working/Placeholder vẫn giữ trạng thái. [Runtime tích hợp](../RUNTIME.md), [vùng mở](../OPEN_STATE.md). Không áp component này cho engine khác.


# 8. Tool — The Gun

## 8.1. Trạng thái

**The Gun** là primary tool của Sloth.

Tên gọi cố ý generic.

Engine định nghĩa ý nghĩa của tool; tên không cần mỹ miều.

## 8.2. Design Philosophy

The Gun tồn tại để cung cấp:

> **the shortest path between obligation and completion.**

Nó được chọn không phải vì tính hiện đại hay thẩm mỹ.

Nó được chọn vì phù hợp với operational philosophy của Sloth.

## 8.3. Vì sao là súng ngắn

Một khẩu súng ngắn hỗ trợ:

- minimal commitment;
- immediate execution;
- short engagement time;
- giảm nhu cầu áp sát;
- giảm số hành động cần thiết;
- hỗ trợ decisive action ngay khi Graze tạo ra cơ hội.

The Gun phù hợp với mục tiêu “dứt nợ”:

```text
Observe
→ Graze
→ Fire
→ Duty discharged
```

## 8.4. Quan hệ với Graze

Graze tạo cơ hội.

The Gun kết thúc nhiệm vụ.

```text
Graze
= Doctrine / interaction strategy

The Gun
= Tool / execution instrument
```

## 8.5. Quan hệ với Accountability

Accountability buộc Sloth phải hành động.

The Gun giảm chi phí thực thi trách nhiệm đó xuống mức tối thiểu có thể.

```text
Accountability
→ cannot ignore the debt

Graze
→ minimize unnecessary interaction

The Gun
→ discharge the debt
```

---


## Chi tiết bổ sung từ nguồn component riêng

# The Gun (Working Draft)

## Status

Primary tool of Sloth.

## Design Philosophy

The Gun is intentionally generic. The engine defines its meaning, not
the name.

## Purpose

Provide the shortest path between obligation and completion.

## Why a Gun?

-   Minimal commitment.
-   Immediate execution.
-   Short engagement time.
-   Supports rapid duty completion.

## Relationship with Graze

Graze creates the opportunity. The Gun finishes the task.

Typical flow: Observe -\> Graze -\> Fire -\> Duty discharged

## Relationship with Accountability

Accountability requires Sloth to act. The Gun minimizes the cost of
fulfilling that responsibility.


Các mục chưa chốt/Future Development của bản component được giữ tại [OPEN_STATE](../OPEN_STATE.md); chúng không trở thành yêu cầu phải triển khai.
