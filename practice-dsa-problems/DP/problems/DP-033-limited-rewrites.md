---
problem_id: DP_LIMITED_REWRITES__6142
display_id: NTB-DP-6142
slug: limited-rewrites
title: "DP with Limited Rewrites"
difficulty: Medium
difficulty_score: 50
topics:
  - Dynamic Programming
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - dp
  - limited-rewrites
  - memoization
  - optimization
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP with Limited Rewrites

## Problem Statement

You build a sequence of `n` actions. After choosing the action for step `i`, you may rewrite any one of the previous `W` steps to a different action. You may perform at most `K` rewrites total.

Each action `j` yields reward `r_j` for the step it occupies. Maximize total reward.

## Input Format

- First line: integers `n`, `a`, `W`, `K`
- Second line: `a` integers: rewards `r_1..r_a`

## Output Format

- Single integer: maximum total reward

## Constraints

- `1 <= n <= 50`
- `1 <= a <= 6`
- `1 <= W <= n`
- `0 <= K <= 10`

## Clarifying Notes

- A rewrite changes only the action choice, not the step order.

## Example Input

```
3 2 2 1
5 1
```

## Example Output

```
15
```

## Solution Stub

### Java

```java
class Solution {
    public long maxReward(int n, int a, int w, int k, int[] r) {
        // Implement here
        return 0;
    }
}
```

### Python

```python
class Solution:
    def maxReward(self, n: int, a: int, w: int, k: int, r: list[int]) -> int:
        # Implement here
        return 0
```

### C++

```cpp
class Solution {
public:
    long long maxReward(int n, int a, int w, int k, vector<int>& r) {
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
   * @param {number} w
   * @param {number} k
   * @param {number[]} r
   * @return {number}
   */
  maxReward(n, a, w, k, r) {
    // Implement here
    return 0;
  }
}
```
