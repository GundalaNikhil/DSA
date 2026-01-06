---
problem_id: LNK_LINKED_LIST_AUDIT_TRAIL__5755
display_id: NTB-LNK-5755
slug: linked-list-audit-trail
title: "Linked List with Audit Trail"
difficulty: Medium
difficulty_score: 50
topics:
  - Linked Lists
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - linked-list-audit-trail
  - linkedlists
  - memory-management
  - pointers
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Linked List with Audit Trail

## Problem Statement

You are given a log of timestamped updates to a list. For each query `(pos, t)`, report the value at position `pos` at time `t`.

Operations:

- `SET pos x t`
- `INS pos x t`
- `DEL pos t`
- `QUERY pos t`

Times are non-decreasing.

## Input Format

- First line: integer `n`
- Second line: `n` integers: initial list values at time 0
- Third line: integer `q`
- Next `q` lines: operations

## Output Format

- For each `QUERY`, output the value or `-1` if out of range at time `t`

## Constraints

- `1 <= n, q <= 200000`
- `0 <= t <= 10^9`

## Clarifying Notes

- Updates at time `t` are visible to queries with the same `t`.

## Example Input

```
2
7 8
3
SET 1 5 1
QUERY 1 1
QUERY 2 1
```

## Example Output

```
5
8
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public List<Integer> processAuditTrail(int n, int[] values, String[] operations) {
        // Your code here
        return new ArrayList<>();
    }
}
```

```python
class Solution:
    def processAuditTrail(self, n: int, values: list[int], operations: list[str]) -> list[int]:
        # Your code here
        return []
```

```cpp
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<int> processAuditTrail(int n, vector<int>& values, vector<string>& operations) {
        // Your code here
        return {};
    }
};
```

```javascript
class Solution {
  /**
   * @param {number} n
   * @param {number[]} values
   * @param {string[]} operations
   * @returns {number[]}
   */
  processAuditTrail(n, values, operations) {
    // Your code here
    return [];
  }
}
```
