---
problem_id: DP_HYSTERESIS__9709
display_id: NTB-DP-9709
slug: hysteresis
title: "DP with Hysteresis"
difficulty: Medium
difficulty_score: 50
topics:
  - Dynamic Programming
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - dp
  - hysteresis
  - memoization
  - optimization
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP with Hysteresis

## Problem Statement

A system has two modes: OFF and ON. It has a level `L` that changes with actions. You can turn ON only if `L >= A`, and can turn OFF only if `L <= B` (with `B < A`). Each step you choose an action that changes `L` by `delta` and yields reward `r`.

Start in OFF with `L = 0`. Maximize total reward in `n` steps.

## Input Format

- First line: integers `n`, `A`, `B`
- Second line: integer `a` (number of actions)
- Next `a` lines: `delta r`

## Output Format

- Single integer: maximum total reward

## Constraints

- `1 <= n <= 200`
- `0 <= B < A <= 50`
- `-10 <= delta <= 10`
- `-10^9 <= r <= 10^9`
- Level is capped in `[0, 50]` for DP.

## Clarifying Notes

- Mode switching does not consume a step; it can occur after applying the action if thresholds allow.

## Example Input

```
3 3 1
2
2 5
-1 0
```

## Example Output

```
10
```

## Solution Stub

### Java

```java
class Solution {
    public long maxReward(int n, int aThreshold, int bThreshold, int numActions, int[][] actions) {
        // Implement here
        return 0;
    }
}
```

### Python

```python
class Solution:
    def maxReward(self, n: int, aThreshold: int, bThreshold: int, numActions: int, actions: list[list[int]]) -> int:
        # Implement here
        return 0
```

### C++

```cpp
class Solution {
public:
    long long maxReward(int n, int aThreshold, int bThreshold, int numActions, vector<vector<int>>& actions) {
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
   * @param {number} aThreshold
   * @param {number} bThreshold
   * @param {number} numActions
   * @param {number[][]} actions
   * @return {number}
   */
  maxReward(n, aThreshold, bThreshold, numActions, actions) {
    // Implement here
    return 0;
  }
}
```
