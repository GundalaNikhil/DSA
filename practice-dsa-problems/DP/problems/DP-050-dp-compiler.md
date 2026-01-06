---
problem_id: DP_DP_COMPILER__8904
display_id: NTB-DP-8904
slug: dp-compiler
title: "DP Compiler Problem"
difficulty: Medium
difficulty_score: 50
topics:
  - Dynamic Programming
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - dp
  - dp-compiler
  - memoization
  - optimization
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP Compiler Problem

## Problem Statement

You are given `n` DP variables `dp[1..n]` and `m` rules. Each rule defines how to compute a variable from previously computed ones:

```
TYPE i k j1 w1 j2 w2 ... jk wk
```

- `TYPE` is `MIN` or `MAX`.
- The rule sets `dp[i] = min/max(dp[jx] + wx)` over its `k` terms.

You are guaranteed the dependency graph is acyclic and that all `j` indices are less than `i`.

Compute all `dp[i]` and output `dp[n]`.

## Input Format

- First line: integer `n`
- Second line: integer `m`
- Next `m` lines: rules as described
- Last line: integer `dp[1]` (base value)

## Output Format

- Single integer: value of `dp[n]`

## Constraints

- `1 <= n <= 200000`
- `1 <= m <= 200000`
- `1 <= k <= 5`
- `-10^9 <= weights <= 10^9`

## Clarifying Notes

- Any `dp[i]` without a rule is treated as `+infinity` for MIN and `-infinity` for MAX.

## Example Input

```
3
2
MIN 2 1 1 5
MAX 3 1 2 2
0
```

## Example Output

```
7
```

## Solution Stub

### Java

```java
class Solution {
    public long computeDP(int n, int m, String[] rules, long baseDP1) {
        // Implement here
        return 0;
    }
}
```

### Python

```python
class Solution:
    def computeDP(self, n: int, m: int, rules: list[str], baseDP1: int) -> int:
        # Implement here
        return 0
```

### C++

```cpp
class Solution {
public:
    long long computeDP(int n, int m, vector<string>& rules, long long baseDP1) {
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
   * @param {number} m
   * @param {string[]} rules
   * @param {number} baseDP1
   * @return {number}
   */
  computeDP(n, m, rules, baseDP1) {
    // Implement here
    return 0;
  }
}
```
