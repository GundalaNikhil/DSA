---
problem_id: DP_DEFERRED_CONSEQUENCES__6941
display_id: NTB-DP-6941
slug: deferred-consequences
title: "DP with Deferred Consequences"
difficulty: Medium
difficulty_score: 50
topics:
  - Dynamic Programming
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - deferred-consequences
  - dp
  - memoization
  - optimization
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP with Deferred Consequences

## Problem Statement

You have `n` steps and `a` actions. Action `i` gives immediate reward `r_i` and also schedules a deferred penalty `p_i` to be applied exactly `d_i` steps later.

Penalties from multiple actions add up on their scheduled steps. Maximize total reward minus penalties over `n` steps.

## Input Format

- First line: integers `n` and `a`
- Next `a` lines: `r_i d_i p_i`

## Output Format

- Single integer: maximum total score

## Constraints

- `1 <= n <= 50`
- `1 <= a <= 6`
- `0 <= r_i, p_i <= 100`
- `0 <= d_i <= 5`

## Clarifying Notes

- Penalties scheduled beyond step `n` are ignored.
- State tracks pending penalties for the next `max(d_i)` steps.

## Example Input

```
3 2
5 1 3
4 2 2
```

## Example Output

```
9
```

## Solution Stub

### Java

```java
class Solution {
    public long maxScore(int n, int a, int[][] actions) {
        // Implement here
        return 0;
    }
}
```

### Python

```python
class Solution:
    def maxScore(self, n: int, a: int, actions: list[list[int]]) -> int:
        # Implement here
        return 0
```

### C++

```cpp
class Solution {
public:
    long long maxScore(int n, int a, vector<vector<int>>& actions) {
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
   * @param {number[][]} actions
   * @return {number}
   */
  maxScore(n, a, actions) {
    // Implement here
    return 0;
  }
}
```
