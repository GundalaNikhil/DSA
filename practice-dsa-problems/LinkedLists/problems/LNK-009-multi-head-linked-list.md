---
problem_id: LNK_MULTI_HEAD_LINKED_LIST__8801
display_id: NTB-LNK-8801
slug: multi-head-linked-list
title: "Multi-Head Linked List"
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
  - multi-head-linked-list
  - pointers
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Multi-Head Linked List

## Problem Statement

You maintain one linked list but have `h` different head pointers into it. Operations can use any head, and mutations affect all heads consistently.

Operations:

- `HEAD i p`: set head `i` to point to node at position `p` (1-based from current global head)
- `DEL i`: delete the node currently pointed by head `i`
- `INS i x`: insert value `x` immediately before the node pointed by head `i`
- `PRINT i`: print list values starting from head `i`

If `DEL` removes a node that is the current position of other heads, those heads move to the next node (or null).

## Input Format

- First line: integers `n` and `h`
- Second line: `n` integers: initial list values
- Third line: integer `q`
- Next `q` lines: operations

## Output Format

- For each `PRINT`, output the list from that head

## Constraints

- `1 <= n, h, q <= 200000`
- Total length across all prints <= 200000

## Clarifying Notes

- If a head points to null, `PRINT` outputs an empty line.

## Example Input

```
4 2
1 2 3 4
4
HEAD 2 3
PRINT 1
DEL 2
PRINT 1
```

## Example Output

```
1 2 3 4
1 2 4
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public List<List<Integer>> processMultiHead(int n, int h, int[] values, String[] operations) {
        // Your code here
        return new ArrayList<>();
    }
}
```

```python
class Solution:
    def processMultiHead(self, n: int, h: int, values: list[int], operations: list[str]) -> list[list[int]]:
        # Your code here
        return []
```

```cpp
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<vector<int>> processMultiHead(int n, int h, vector<int>& values, vector<string>& operations) {
        // Your code here
        return {};
    }
};
```

```javascript
class Solution {
  /**
   * @param {number} n
   * @param {number} h
   * @param {number[]} values
   * @param {string[]} operations
   * @returns {number[][]}
   */
  processMultiHead(n, h, values, operations) {
    // Your code here
    return [];
  }
}
```
