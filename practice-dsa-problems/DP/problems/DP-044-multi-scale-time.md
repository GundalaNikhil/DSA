---
problem_id: DP_MULTI_SCALE_TIME__6209
display_id: NTB-DP-6209
slug: multi-scale-time
title: "DP on Multi-Scale Time"
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
  - multi-scale-time
  - optimization
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP on Multi-Scale Time

## Problem Statement

You have `n` steps grouped into blocks of size `K` (n is divisible by K). At the start of each block, you choose a slow action `s` that sets a multiplier `m_s` for the entire block. Each step in the block chooses a fast action `f` with base reward `r_f`. The reward for a step is `m_s * r_f`.

Maximize total reward.

## Input Format

- First line: integers `n`, `K`, `S`, `F`
- Second line: `S` integers: multipliers `m_s`
- Third line: `F` integers: rewards `r_f`

## Output Format

- Single integer: maximum total reward

## Constraints

- `1 <= n <= 200`
- `1 <= K <= n`, `n % K == 0`
- `1 <= S, F <= 10`
- `-10 <= m_s, r_f <= 10`

## Clarifying Notes

- Multipliers and rewards can be negative.

## Example Input

```
4 2 2 2
2 -1
3 1
```

## Example Output

```
8
```

## Solution Stub

### Java

```java
class Solution {
    public long maxReward(int n, int k, int s, int f, int[] multipliers, int[] fastRewards) {
        // Implement here
        return 0;
    }
}
```

### Python

```python
class Solution:
    def maxReward(self, n: int, k: int, s: int, f: int, multipliers: list[int], fastRewards: list[int]) -> int:
        # Implement here
        return 0
```

### C++

```cpp
class Solution {
public:
    long long maxReward(int n, int k, int s, int f, vector<int>& multipliers, vector<int>& fastRewards) {
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
   * @param {number} k
   * @param {number} s
   * @param {number} f
   * @param {number[]} multipliers
   * @param {number[]} fastRewards
   * @return {number}
   */
  maxReward(n, k, s, f, multipliers, fastRewards) {
    // Implement here
    return 0;
  }
}
```
