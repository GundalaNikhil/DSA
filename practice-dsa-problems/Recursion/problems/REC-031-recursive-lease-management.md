---
problem_id: REC_RECURSIVE_LEASE_MANAGEMENT__1587
display_id: NTB-REC-1587
slug: recursive-lease-management
title: "Recursive Lease Management"
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
  - recursive-lease-management
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Recursive Lease Management

## Problem Statement

You are given a rooted tree. Each node uses a resource type `r` and has a renewal cost `cost`. Each resource type has a fixed lease length `L[r]` (in depth units).

When you enter a node at depth `d`, the resource `r` is valid if it was last renewed at depth `t` with `t + L[r] >= d`. You may renew a resource at any node that uses it, paying that node's `cost`, which sets the last renewal depth to `d`.

For every root-to-leaf path, you must ensure that the resource at each node is valid. Find the minimum total renewal cost required to validate the entire tree (each subtree can choose its own renewal decisions).

## Input Format

- First line: integers `n` and `R`
- Second line: `R` integers `L[1..R]`
- Next `n` lines: `r cost parent` (parent is 0 for root)

## Output Format

- Single integer: minimum total renewal cost

## Constraints

- `1 <= n <= 2000`
- `1 <= R <= 6`
- `1 <= L[r] <= 10`
- `0 <= cost <= 10^9`

## Clarifying Notes

- Renewal decisions are independent per subtree because recursion state is copied for each child.
- If a resource is expired at a node, renewal at that node is mandatory.

## Example Input

```
5 2
2 1
1 5 0
2 3 1
1 4 1
2 2 2
1 1 2
```

## Example Output

```
7
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public long minRenewalCost(int n, int R, int[] L, int[][] nodes) {
        // Your code here
        return 0;
    }
}
```

```python
class Solution:
    def minRenewalCost(self, n: int, R: int, L: list[int], nodes: list[list[int]]) -> int:
        # Your code here
        return 0
```

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    long long minRenewalCost(int n, int R, vector<int>& L, vector<vector<int>>& nodes) {
        // Your code here
        return 0;
    }
};
```

```javascript
class Solution {
  /**
   * @param {number} n
   * @param {number} R
   * @param {number[]} L
   * @param {number[][]} nodes
   * @returns {number}
   */
  minRenewalCost(n, R, L, nodes) {
    // Your code here
    return 0;
  }
}
```
