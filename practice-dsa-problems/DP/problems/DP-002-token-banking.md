---
problem_id: DP_TOKEN_BANKING__7563
display_id: NTB-DP-7563
slug: token-banking
title: "DP with Token Banking"
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
  - token-banking
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP with Token Banking

## Problem Statement

You have `n` steps and a token balance. At each step you choose one action. Some actions generate tokens, and some consume tokens. In addition, there are `p` power actions that can be used at most once each and require tokens to activate.

Maximize total reward after exactly `n` steps.

## Input Format

- First line: integers `n`, `b`, `a`, `p`
- Second line: `a` lines for normal actions: `reward token_delta`
- Next `p` lines for power actions: `reward token_cost`

## Output Format

- Single integer: maximum total reward

## Constraints

- `1 <= n <= 200`
- `0 <= b <= 50`
- `1 <= a <= 10`
- `0 <= p <= 10`
- `-10^9 <= reward <= 10^9`
- `-10 <= token_delta <= 10`
- `0 <= token_cost <= 50`

## Clarifying Notes

- Token balance must stay between 0 and `b`.
- Power actions can be used at most once each.

## Example Input

```
3 5 2 1
4 1
2 0
10 3
```

## Example Output

```
16
```

## Solution Stub

### Java

```java
class Solution {
    public long maxReward(int n, int b, int a, int p, int[][] normalActions, int[][] powerActions) {
        // Implement here
        return 0;
    }
}
```

### Python

```python
class Solution:
    def maxReward(self, n: int, b: int, a: int, p: int, normalActions: list[list[int]], powerActions: list[list[int]]) -> int:
        # Implement here
        return 0
```

### C++

```cpp
class Solution {
public:
    long long maxReward(int n, int b, int a, int p, vector<vector<int>>& normalActions, vector<vector<int>>& powerActions) {
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
   * @param {number} b
   * @param {number} a
   * @param {number} p
   * @param {number[][]} normalActions
   * @param {number[][]} powerActions
   * @return {number}
   */
  maxReward(n, b, a, p, normalActions, powerActions) {
    // Implement here
    return 0;
  }
}
```
