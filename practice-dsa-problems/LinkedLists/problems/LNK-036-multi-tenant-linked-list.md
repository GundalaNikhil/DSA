---
problem_id: LNK_MULTI_TENANT_LINKED_LIST__1472
display_id: NTB-LNK-1472
slug: multi-tenant-linked-list
title: "Multi-Tenant Linked List"
difficulty: Medium
difficulty_score: 50
topics:
  - Linked Lists
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - linkedlists
  - memory-management
  - multi-tenant-linked-list
  - pointers
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Multi-Tenant Linked List

## Problem Statement

A single linked list is shared by multiple tenants. Each node is owned by exactly one tenant. Each tenant has a maximum allowed node count.

Operations:

- `INS t pos x`: insert value `x` for tenant `t` at position `pos`
- `DEL t pos`: delete node at position `pos` if it belongs to tenant `t`
- `COUNT t`: output current node count of tenant `t`

Invalid operations are ignored.

## Input Format

- First line: integers `n` and `T`
- Second line: `n` integers: initial list values
- Third line: `n` integers: tenant ids in order
- Next `T` lines: `limit_t` for each tenant
- Next line: integer `q`
- Next `q` lines: operations

## Output Format

- For each `COUNT`, output one integer

## Constraints

- `1 <= n, q <= 200000`
- `1 <= T <= 200000`

## Clarifying Notes

- Insertions are rejected if they would exceed the tenant's limit.

## Example Input

```
3 2
1 2 3
1 2 1
2
2
3
INS 1 2 9
COUNT 1
```

## Example Output

```
2
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public List<Integer> processMultiTenantList(int n, int T, int[] values, int[] tenantIds, int[] limits, String[] operations) {
        // Your code here
        return new ArrayList<>();
    }
}
```

```python
class Solution:
    def processMultiTenantList(self, n: int, T: int, values: list[int], tenant_ids: list[int], limits: list[int], operations: list[str]) -> list[int]:
        # Your code here
        return []
```

```cpp
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<int> processMultiTenantList(int n, int T, vector<int>& values, vector<int>& tenantIds, vector<int>& limits, vector<string>& operations) {
        // Your code here
        return {};
    }
};
```

```javascript
class Solution {
  /**
   * @param {number} n
   * @param {number} T
   * @param {number[]} values
   * @param {number[]} tenantIds
   * @param {number[]} limits
   * @param {string[]} operations
   * @returns {number[]}
   */
  processMultiTenantList(n, T, values, tenantIds, limits, operations) {
    // Your code here
    return [];
  }
}
```
