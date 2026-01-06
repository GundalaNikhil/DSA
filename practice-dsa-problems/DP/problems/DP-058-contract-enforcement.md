---
problem_id: DP_CONTRACT_ENFORCEMENT__4266
display_id: NTB-DP-4266
slug: contract-enforcement
title: "DP with Contract Enforcement"
difficulty: Medium
difficulty_score: 50
topics:
  - Dynamic Programming
tags:
  - algorithms
  - coding-interviews
  - contract-enforcement
  - data-structures
  - dp
  - memoization
  - optimization
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP with Contract Enforcement

## Problem Statement

Some actions create contracts that must be fulfilled within `D` steps. A contract requires you to take a specific action type within that window or pay penalty `P`.

Maximize total reward minus penalties.

## Input Format

- First line: integers `n`, `a`, `D`, `P`
- Next `a` lines: `reward_i creates_contract` (0/1)

## Output Format

- Single integer: maximum total score

## Constraints

- `1 <= n <= 50`
- `1 <= a <= 6`
- `0 <= reward_i <= 50`
- `0 <= D <= 5`
- `0 <= P <= 50`

## Clarifying Notes

- A contract requires taking the same action type that created it.
- Multiple contracts can overlap and are tracked separately.

## Example Input

```
3 2 2 4
5 1
2 0
```

## Example Output

```
11
```

## Solution Stub

### Java

```java
class Solution {
    public long maxScore(int n, int a, int d, int p, int[][] actions) {
        // Implement here
        return 0;
    }
}
```

### Python

```python
class Solution:
    def maxScore(self, n: int, a: int, d: int, p: int, actions: list[list[int]]) -> int:
        # Implement here
        return 0
```

### C++

```cpp
class Solution {
public:
    long long maxScore(int n, int a, int d, int p, vector<vector<int>>& actions) {
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
   * @param {number} d
   * @param {number} p
   * @param {number[][]} actions
   * @return {number}
   */
  maxScore(n, a, d, p, actions) {
    // Implement here
    return 0;
  }
}
```
