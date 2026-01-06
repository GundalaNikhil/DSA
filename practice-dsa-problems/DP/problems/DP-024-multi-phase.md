---
problem_id: DP_MULTI_PHASE__8869
display_id: NTB-DP-8869
slug: multi-phase
title: "Multi-Phase DP"
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
  - multi-phase
  - optimization
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Multi-Phase DP

## Problem Statement

There are three phases. Each phase has its own action set and rewards. You start in phase 1 and may move to the next phase only if a condition is met.

- Phase 1: actions A, condition: total reward in phase 1 >= X
- Phase 2: actions B, condition: number of actions in phase 2 >= Y
- Phase 3: actions C

You must perform exactly `n` actions. Maximize total reward.

## Input Format

- First line: integers `n`, `X`, `Y`
- Next line: integer `a` then `a` rewards for phase 1 actions
- Next line: integer `b` then `b` rewards for phase 2 actions
- Next line: integer `c` then `c` rewards for phase 3 actions

## Output Format

- Single integer: maximum total reward

## Constraints

- `1 <= n <= 100`
- `0 <= X, Y <= 1000`
- `1 <= a, b, c <= 6`
- `-10^9 <= reward <= 10^9`

## Clarifying Notes

- Phase transitions are optional; you may end in any phase after `n` actions.

## Example Input

```
3 5 1
1 5
1 3
1 4
```

## Example Output

```
12
```

## Solution Stub

### Java

```java
class Solution {
    public long maxReward(int n, int x, int y, int[] phase1, int[] phase2, int[] phase3) {
        // Implement here
        return 0;
    }
}
```

### Python

```python
class Solution:
    def maxReward(self, n: int, x: int, y: int, phase1: list[int], phase2: list[int], phase3: list[int]) -> int:
        # Implement here
        return 0
```

### C++

```cpp
class Solution {
public:
    long long maxReward(int n, int x, int y, vector<int>& phase1, vector<int>& phase2, vector<int>& phase3) {
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
   * @param {number} x
   * @param {number} y
   * @param {number[]} phase1
   * @param {number[]} phase2
   * @param {number[]} phase3
   * @return {number}
   */
  maxReward(n, x, y, phase1, phase2, phase3) {
    // Implement here
    return 0;
  }
}
```
