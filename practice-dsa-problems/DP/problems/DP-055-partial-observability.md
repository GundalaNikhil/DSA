---
problem_id: DP_PARTIAL_OBSERVABILITY__2803
display_id: NTB-DP-2803
slug: partial-observability
title: "DP with Partial Observability"
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
  - partial-observability
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP with Partial Observability

## Problem Statement

There are `s` hidden modes. You maintain a belief distribution over modes. At each step you choose an action; each action has a deterministic observation function that reveals a symbol depending on the current mode. You are given the transition matrix for modes.

Compute the maximum expected reward over `n` steps.

## Input Format

- First line: integers `n`, `s`, `a`, `o`
- Second line: `s` integers: initial probabilities scaled by 1000
- Next `a` blocks:
  - `s` integers: reward per mode
  - `s` integers: observation symbol per mode (0..o-1)
- Next `s` lines: `s` integers: transition probabilities scaled by 1000

## Output Format

- Single integer: maximum expected reward scaled by 1000^n

## Constraints

- `1 <= n <= 10`
- `1 <= s <= 6`
- `1 <= a <= 4`
- `1 <= o <= 6`

## Clarifying Notes

- Use exact arithmetic with scaled probabilities.

## Example Input

```
1 2 1 2
500 500
10 0
0 1
1000 0
0 1000
```

## Example Output

```
5000
```

## Solution Stub

### Java

```java
class Solution {
    public long maxExpectedRewardScaled(int n, int s, int a, int o, int[] initialProbs, int[][][] actions, int[][] transitions) {
        // Implement here
        return 0;
    }
}
```

### Python

```python
class Solution:
    def maxExpectedRewardScaled(self, n: int, s: int, a: int, o: int, initialProbs: list[int], actions: list[list[list[int]]], transitions: list[list[int]]) -> int:
        # Implement here
        return 0
```

### C++

```cpp
class Solution {
public:
    long long maxExpectedRewardScaled(int n, int s, int a, int o, vector<int>& initialProbs, vector<vector<vector<int>>>& actions, vector<vector<int>>& transitions) {
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
   * @param {number} o
   * @param {number[]} initialProbs
   * @param {number[][][]} actions
   * @param {number[][]} transitions
   * @return {number}
   */
  maxExpectedRewardScaled(n, s, a, o, initialProbs, actions, transitions) {
    // Implement here
    return 0;
  }
}
```
