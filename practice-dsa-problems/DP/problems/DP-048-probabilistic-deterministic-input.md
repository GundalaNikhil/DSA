---
problem_id: DP_PROBABILISTIC_DETERMINISTIC_INPUT__5797
display_id: NTB-DP-5797
slug: probabilistic-deterministic-input
title: "DP with Probabilistic but Deterministic Input"
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
  - probabilistic-deterministic-input
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP with Probabilistic but Deterministic Input

## Problem Statement

You have `n` steps and `s` states. From state `i`, choosing action `a` moves to state `j` with probability `p/q` (given as integers). Each transition yields reward `r`.

Compute the maximum expected total reward starting from state 1.

## Input Format

- First line: integers `n`, `s`, `a`, `q`
- Next `a` lines: `from to p r` (probability is `p/q`)

## Output Format

- Single integer: maximum expected reward multiplied by `q^n`

## Constraints

- `1 <= n <= 20`
- `1 <= s <= 20`
- `1 <= a <= 100`
- `0 <= p <= q <= 10`
- `-10^6 <= r <= 10^6`

## Clarifying Notes

- Use exact arithmetic; scale by `q^n`.

## Example Input

```
2 2 2 2
1 2 1 5
1 1 1 1
```

## Example Output

```
12
```

## Solution Stub

### Java

```java
class Solution {
    public long maxExpectedRewardScaled(int n, int s, int a, int q, int[][] transitions) {
        // Implement here
        return 0;
    }
}
```

### Python

```python
class Solution:
    def maxExpectedRewardScaled(self, n: int, s: int, a: int, q: int, transitions: list[list[int]]) -> int:
        # Implement here
        return 0
```

### C++

```cpp
class Solution {
public:
    long long maxExpectedRewardScaled(int n, int s, int a, int q, vector<vector<int>>& transitions) {
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
   * @param {number} s
   * @param {number} a
   * @param {number} q
   * @param {number[][]} transitions
   * @return {number}
   */
  maxExpectedRewardScaled(n, s, a, q, transitions) {
    // Implement here
    return 0;
  }
}
```
