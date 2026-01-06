---
problem_id: LNK_LINKED_LIST_READ_REPLICAS__3497
display_id: NTB-LNK-3497
slug: linked-list-read-replicas
title: "Linked List with Read Replicas"
difficulty: Medium
difficulty_score: 50
topics:
  - Linked Lists
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - linked-list-read-replicas
  - linkedlists
  - memory-management
  - pointers
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Linked List with Read Replicas

## Problem Statement

You have a primary linked list and `R` read-only replicas. Updates are applied to the primary immediately and to each replica after a fixed delay `D` (in time units).

Operations:

- `SET pos x t`: update primary at time `t`
- `GET r pos t`: read from replica `r` at time `t`

A replica reflects all primary updates with `time <= t - D`.

## Input Format

- First line: integers `n`, `R`, `D`
- Second line: `n` integers: initial list values
- Third line: integer `q`
- Next `q` lines: operations

## Output Format

- For each `GET`, output the value at `pos` in replica `r`

## Constraints

- `1 <= n, q <= 200000`
- `1 <= R <= 10`
- Timestamps are non-decreasing

## Clarifying Notes

- If `t < D`, replicas show the initial state.

## Example Input

```
3 1 5
1 2 3
3
SET 2 9 3
GET 1 2 6
GET 1 2 7
```

## Example Output

```
2
9
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public List<Integer> processReadReplicas(int n, int R, int D, int[] initialValues, String[] operations) {
        // Your code here
        return new ArrayList<>();
    }
}
```

```python
class Solution:
    def processReadReplicas(self, n: int, R: int, D: int, initial_values: list[int], operations: list[str]) -> list[int]:
        # Your code here
        return []
```

```cpp
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<int> processReadReplicas(int n, int R, int D, vector<int>& initialValues, vector<string>& operations) {
        // Your code here
        return {};
    }
};
```

```javascript
class Solution {
  /**
   * @param {number} n
   * @param {number} R
   * @param {number} D
   * @param {number[]} initialValues
   * @param {string[]} operations
   * @returns {number[]}
   */
  processReadReplicas(n, R, D, initialValues, operations) {
    // Your code here
    return [];
  }
}
```
