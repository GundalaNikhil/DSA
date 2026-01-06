---
problem_id: LNK_PRIORITY_AWARE_LINKED_LIST__2144
display_id: NTB-LNK-2144
slug: priority-aware-linked-list
title: "Priority-Aware Linked List"
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
  - priority-aware-linked-list
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Priority-Aware Linked List

## Problem Statement

Each node has a priority class. You may reorder nodes **only within the same priority class**. Process operations and output the final list.

Operations:

- `MOVE u v`: move node `u` to immediately after node `v`
- `SWAP u v`: swap positions of nodes `u` and `v`

An operation is invalid if it would move a node across priority classes. Invalid operations are ignored.

## Input Format

- First line: integer `n`
- Second line: `n` integers: node values in order
- Third line: `n` integers: priority classes in order
- Fourth line: integer `q`
- Next `q` lines: operations

## Output Format

- One line with the final list values

## Constraints

- `1 <= n, q <= 200000`
- Priority classes are integers in range `1..n`

## Clarifying Notes

- `MOVE` is valid only if `u` and `v` have the same priority.
- `SWAP` is valid only if both nodes share the same priority.

## Example Input

```
4
10 20 30 40
1 2 1 2
2
MOVE 3 1
SWAP 2 4
```

## Example Output

```
10 30 40 20
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public int[] processPriorityList(int n, int[] values, int[] priorities, String[] operations) {
        // Your code here
        return new int[0];
    }
}
```

```python
class Solution:
    def processPriorityList(self, n: int, values: list[int], priorities: list[int], operations: list[str]) -> list[int]:
        # Your code here
        return []
```

```cpp
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<int> processPriorityList(int n, vector<int>& values, vector<int>& priorities, vector<string>& operations) {
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
   * @param {number[]} priorities
   * @param {string[]} operations
   * @returns {number[]}
   */
  processPriorityList(n, values, priorities, operations) {
    // Your code here
    return [];
  }
}
```
