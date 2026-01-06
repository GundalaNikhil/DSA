---
problem_id: REC_RECURSIVE_TIME_BUDGETS__6891
display_id: NTB-REC-6891
slug: recursive-time-budgets
title: "Recursive Time Budgets"
difficulty: Medium
difficulty_score: 50
topics:
  - Recursion
tags:
  - algorithms
  - backtracking
  - coding-interviews
  - data-structures
  - recursion
  - recursive-time-budgets
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Recursive Time Budgets

## Problem Statement

You are given a rooted tree. Each node has:

- processing time `t`
- exact value `v`
- estimated value `e`
- time budget `b` for its subtree

A recursive evaluation processes children in increasing node index order. It keeps track of the exact time spent in the subtree.

Define `Eval(node)` returning `(timeUsed, value)`:

- Start with `timeUsed = t[node]` and `value = v[node]`.
- For each child in order:
  - Compute `Eval(child)` to get `(ct, cv)`.
  - If `timeUsed + ct <= b[node]`, include the exact child: `timeUsed += ct`, `value += cv`.
  - Otherwise include the estimate only: `value += e[child]` (time does not increase).

Compute the root `value`.

## Input Format

- First line: integer `n`
- Next `n` lines: `t v e b parent` (parent is 0 for root)

## Output Format

- Single integer: root value

## Constraints

- `1 <= n <= 200000`
- `0 <= t <= 10^6`
- `-10^9 <= v, e <= 10^9`
- `0 <= b <= 10^12`

## Clarifying Notes

- Exact time is computed even if the child is later replaced by its estimate.
- Budgets are local to each node; exceeding a child's budget only affects that child.

## Example Input

```
4
2 5 1 6 0
3 4 2 5 1
1 3 2 3 1
2 6 0 4 2
```

## Example Output

```
12
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public long calculateTimeBudgetedValue(int n, long[][] nodes) {
        // Your code here
        return 0;
    }
}
```

```python
class Solution:
    def calculateTimeBudgetedValue(self, n: int, nodes: list[list[int]]) -> int:
        # Your code here
        return 0
```

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    long long calculateTimeBudgetedValue(int n, vector<vector<long long>>& nodes) {
        // Your code here
        return 0;
    }
};
```

```javascript
class Solution {
  /**
   * @param {number} n
   * @param {number[][]} nodes
   * @returns {number}
   */
  calculateTimeBudgetedValue(n, nodes) {
    // Your code here
    return 0;
  }
}
```
