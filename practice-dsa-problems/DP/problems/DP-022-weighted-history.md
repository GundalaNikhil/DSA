---
problem_id: DP_WEIGHTED_HISTORY__5287
display_id: NTB-DP-5287
slug: weighted-history
title: "DP on Weighted History"
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
  - technical-interview-prep
  - weighted-history
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP on Weighted History

## Problem Statement

You have `n` steps and choose one of `a` actions each step. The reward for choosing action `i` at step `t` is:

```
base_i - w_i * H_i
```

where `H_i` is the exponentially decayed count of past uses of action `i`:

```
H_i(t) = sum_{k < t and action_k = i} alpha^{t-k}
```

You are given `alpha` as a fraction `p/q`. Maximize total reward.

## Input Format

- First line: integers `n`, `a`, `p`, `q`
- Next `a` lines: `base_i w_i`

## Output Format

- Single integer: maximum total reward multiplied by `q^n`

## Constraints

- `1 <= n <= 20`
- `1 <= a <= 5`
- `0 <= p <= q <= 5`
- `0 <= base_i, w_i <= 10`

## Clarifying Notes

- Use exact arithmetic; scale rewards by `q^n` to keep integers.

## Example Input

```
2 1 1 2
4 1
```

## Example Output

```
12
```

## Solution Stub

### Java

```java
class Solution {
    public long maxRewardScaled(int n, int a, int p, int q, int[][] actions) {
        // Implement here
        return 0;
    }
}
```

### Python

```python
class Solution:
    def maxRewardScaled(self, n: int, a: int, p: int, q: int, actions: list[list[int]]) -> int:
        # Implement here
        return 0
```

### C++

```cpp
class Solution {
public:
    long long maxRewardScaled(int n, int a, int p, int q, vector<vector<int>>& actions) {
        // Implement here
        return 0;
    }
};
```

### JavaScript

```javascript
class Solution {
  /**
   * @param {number} n
   * @param {number} a
   * @param {number} p
   * @param {number} q
   * @param {number[][]} actions
   * @return {number}
   */
  maxRewardScaled(n, a, p, q, actions) {
    // Implement here
    return 0;
  }
}
```
