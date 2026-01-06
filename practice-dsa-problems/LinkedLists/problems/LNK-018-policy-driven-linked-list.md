---
problem_id: LNK_POLICY_DRIVEN_LINKED_LIST__3698
display_id: NTB-LNK-3698
slug: policy-driven-linked-list
title: "Policy-Driven Linked List"
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
  - pointers
  - policy-driven-linked-list
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Policy-Driven Linked List

## Problem Statement

Nodes belong to segments. You are given per-segment operation limits: maximum insertions and deletions allowed. Process operations and reject any that would violate limits.

Operations:

- `INS s pos x`: insert value `x` at position `pos` within segment `s`
- `DEL s pos`: delete node at position `pos` within segment `s`
- `COUNT s`: output current size of segment `s`

## Input Format

- First line: integers `n` and `S`
- Second line: `n` integers: node values
- Third line: `n` integers: segment ids in order
- Fourth line: `S` lines: `max_ins max_del` for each segment
- Fifth line: integer `q`
- Next `q` lines: operations

## Output Format

- For each `COUNT`, output one integer

## Constraints

- `1 <= n, q <= 200000`
- `1 <= S <= n`

## Clarifying Notes

- Insert/delete counters are per segment and include only successful operations.
- Invalid operations are ignored.

## Example Input

```
4 2
1 2 3 4
1 1 2 2
1 0
1 1
3
INS 1 2 9
DEL 2 1
COUNT 2
```

## Example Output

```
1
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public List<Integer> processPolicyList(int n, int S, int[] values, int[] segmentIds, int[][] limits, String[] operations) {
        // Your code here
        return new ArrayList<>();
    }
}
```

```python
class Solution:
    def processPolicyList(self, n: int, S: int, values: list[int], segment_ids: list[int], limits: list[list[int]], operations: list[str]) -> list[int]:
        # Your code here
        return []
```

```cpp
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<int> processPolicyList(int n, int S, vector<int>& values, vector<int>& segmentIds, vector<vector<int>>& limits, vector<string>& operations) {
        // Your code here
        return {};
    }
};
```

```javascript
class Solution {
  /**
   * @param {number} n
   * @param {number} S
   * @param {number[]} values
   * @param {number[]} segmentIds
   * @param {number[][]} limits
   * @param {string[]} operations
   * @returns {number[]}
   */
  processPolicyList(n, S, values, segmentIds, limits, operations) {
    // Your code here
    return [];
  }
}
```
