---
problem_id: DP_RUNTIME_STATE_INFERENCE__8408
display_id: NTB-DP-8408
slug: runtime-state-inference
title: "DP with Runtime State Inference"
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
  - runtime-state-inference
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP with Runtime State Inference

## Problem Statement

You traverse `n` steps. There are `s` possible hidden modes. At step `i`, you choose an action `a`. The system deterministically reveals the current mode based on `(i, a)` using a table, and the next mode is fixed. You then gain reward `R[i][mode]`.

Maximize total reward.

## Input Format

- First line: integers `n`, `s`, `a`
- Next `n` lines: `s` integers: rewards `R[i][1..s]`
- Next `n` lines: `a` integers: reveal table `mode(i, action)` (1..s)

## Output Format

- Single integer: maximum total reward

## Constraints

- `1 <= n <= 200`
- `1 <= s <= 10`
- `1 <= a <= 10`

## Clarifying Notes

- Mode revealed at step `i` is also the mode used for reward at step `i`.

## Example Input

```
2 2 2
5 1
2 4
1 2
2 1
```

## Example Output

```
9
```

## Solution Stub

### Java

```java
class Solution {
    public long maxReward(int n, int s, int a, int[][] rewards, int[][] revealTable) {
        // Implement here
        return 0;
    }
}
```

### Python

```python
class Solution:
    def maxReward(self, n: int, s: int, a: int, rewards: list[list[int]], revealTable: list[list[int]]) -> int:
        # Implement here
        return 0
```

### C++

```cpp
class Solution {
public:
    long long maxReward(int n, int s, int a, vector<vector<int>>& rewards, vector<vector<int>>& revealTable) {
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
   * @param {number[][]} rewards
   * @param {number[][]} revealTable
   * @return {number}
   */
  maxReward(n, s, a, rewards, revealTable) {
    // Implement here
    return 0;
  }
}
```
