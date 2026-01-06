---
problem_id: DP_STORAGE_TIERING__3040
display_id: NTB-DP-3040
slug: storage-tiering
title: "Storage Tiering DP"
difficulty: Medium
difficulty_score: 50
topics:
  - Dynamic Programming
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - dp
  - memoization
  - optimization
  - storage-tiering
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Storage Tiering DP

## Problem Statement

You have `n` items and `t` time steps. Each item can be on fast or slow storage. Access cost per step is given for each item. Moving an item between tiers costs `M`.

Find the minimum total cost.

## Input Format

- First line: integers `n`, `t`, `M`
- Next `t` lines: `n` integers: access cost if item is on slow tier at that time (fast tier cost is 0)

## Output Format

- Single integer: minimum total cost

## Constraints

- `1 <= n <= 10`
- `1 <= t <= 50`
- `0 <= M <= 10^6`
- `0 <= costs <= 10^6`

## Clarifying Notes

- Initial placement is all on slow tier.
- Moving cost applies per item per move.

## Example Input

```
2 2 3
5 1
1 4
```

## Example Output

```
5
```

## Solution Stub

```java
public class Solution {
    public long minStorageCost(int n, int t, int M, int[][] accessCosts) {
        // Your code here
        return 0;
    }
}
```

```python
class Solution:
    def minStorageCost(self, n: int, t: int, M: int, accessCosts: list[list[int]]) -> int:
        # Your code here
        return 0
```

```cpp
class Solution {
public:
    long long minStorageCost(int n, int t, int M, vector<vector<int>>& accessCosts) {
        // Your code here
        return 0;
    }
};
```

```javascript
class Solution {
  minStorageCost(n, t, M, accessCosts) {
    // Your code here
    return 0;
  }
}
```
