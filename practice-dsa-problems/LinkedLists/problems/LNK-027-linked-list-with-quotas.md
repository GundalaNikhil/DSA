---
problem_id: LNK_LINKED_LIST_WITH_QUOTAS__2568
display_id: NTB-LNK-2568
slug: linked-list-with-quotas
title: "Linked List with Quotas"
difficulty: Medium
difficulty_score: 50
topics:
  - Linked Lists
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - linked-list-with-quotas
  - linkedlists
  - memory-management
  - pointers
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Linked List with Quotas

## Problem Statement

Each segment has insertion and deletion quotas. Once a quota is exhausted, further operations of that type in the segment are rejected.

Operations:

- `INS s pos x`
- `DEL s pos`
- `COUNT s`

## Input Format

- First line: integers `n` and `S`
- Second line: `n` integers: node values
- Third line: `n` integers: segment ids in order
- Next `S` lines: `ins_quota del_quota`
- Next line: integer `q`
- Next `q` lines: operations

## Output Format

- For each `COUNT`, output the current size of segment `s`

## Constraints

- `1 <= n, q <= 200000`
- `1 <= S <= n`

## Clarifying Notes

- Quotas count only successful operations.
- Invalid operations are ignored.

## Example Input

```
3 1
5 6 7
1 1 1
1 1
3
INS 1 2 9
INS 1 3 8
COUNT 1
```

## Example Output

```
4
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public List<Integer> processQuotaList(int n, int S, int[] values, int[] segmentIds, int[][] quotas, String[] operations) {
        // Your code here
        return new ArrayList<>();
    }
}
```

```python
class Solution:
    def processQuotaList(self, n: int, S: int, values: list[int], segment_ids: list[int], quotas: list[list[int]], operations: list[str]) -> list[int]:
        # Your code here
        return []
```

```cpp
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<int> processQuotaList(int n, int S, vector<int>& values, vector<int>& segmentIds, vector<vector<int>>& quotas, vector<string>& operations) {
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
   * @param {number[][]} quotas
   * @param {string[]} operations
   * @returns {number[]}
   */
  processQuotaList(n, S, values, segmentIds, quotas, operations) {
    // Your code here
    return [];
  }
}
```
