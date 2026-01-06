---
problem_id: LNK_RATE_LIMITED_LINKED_LIST__7810
display_id: NTB-LNK-7810
slug: rate-limited-linked-list
title: "Rate-Limited Linked List"
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
  - rate-limited-linked-list
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Rate-Limited Linked List

## Problem Statement

Each node has a cooldown `C` (global). Any modification to a node is allowed only if at least `C` time units have passed since its last modification.

Each operation provides a timestamp `t`.

Operations:

- `SET pos x t`: set value at position `pos` to `x` if cooldown allows
- `DEL pos t`: delete node at position `pos` if cooldown allows
- `GET pos`: output value at position `pos` or `-1`

If a modification is blocked by cooldown, it is ignored.

## Input Format

- First line: integers `n` and `C`
- Second line: `n` integers: list values
- Third line: integer `q`
- Next `q` lines: operations

## Output Format

- For each `GET`, output one integer

## Constraints

- `1 <= n, q <= 200000`
- `0 <= C <= 10^9`
- Timestamps are non-decreasing

## Clarifying Notes

- Deleting a node counts as a modification to that node.
- After deletion, the node is gone and cooldown is irrelevant.

## Example Input

```
3 5
1 2 3
4
SET 2 9 1
SET 2 8 3
GET 2
SET 2 7 7
```

## Example Output

```
9
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public List<Integer> processRateLimitedList(int n, int C, int[] values, String[] operations) {
        // Your code here
        return new ArrayList<>();
    }
}
```

```python
class Solution:
    def processRateLimitedList(self, n: int, C: int, values: list[int], operations: list[str]) -> list[int]:
        # Your code here
        return []
```

```cpp
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<int> processRateLimitedList(int n, int C, vector<int>& values, vector<string>& operations) {
        // Your code here
        return {};
    }
};
```

```javascript
class Solution {
  /**
   * @param {number} n
   * @param {number} C
   * @param {number[]} values
   * @param {string[]} operations
   * @returns {number[]}
   */
  processRateLimitedList(n, C, values, operations) {
    // Your code here
    return [];
  }
}
```
