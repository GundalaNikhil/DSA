---
problem_id: DP_MEMORY_BUDGET__7443
display_id: NTB-DP-7443
slug: memory-budget
title: "DP with Memory Budget"
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
  - memory-budget
  - optimization
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP with Memory Budget

## Problem Statement

You have `n` steps and `a` actions. Each action adds a value `v_i`. The DP state is the current sum. After each step, you may keep at most `K` states; all others are discarded. The objective is to maximize the final sum after `n` steps given optimal pruning.

## Input Format

- First line: integers `n`, `a`, `K`
- Second line: `a` integers: values `v_1..v_a`

## Output Format

- Single integer: maximum reachable sum after `n` steps

## Constraints

- `1 <= n <= 60`
- `1 <= a <= 10`
- `1 <= K <= 2000`
- `-10^6 <= v_i <= 10^6`

## Clarifying Notes

- If multiple states have the same sum, keep only one.

## Example Input

```
3 2 2
5 -1
```

## Example Output

```
15
```

## Solution Stub

### Java

```java
class Solution {
    public long maxFinalSum(int n, int a, int k, int[] values) {
        // Implement here
        return 0;
    }
}
```

### Python

```python
class Solution:
    def maxFinalSum(self, n: int, a: int, k: int, values: list[int]) -> int:
        # Implement here
        return 0
```

### C++

```cpp
class Solution {
public:
    long long maxFinalSum(int n, int a, int k, vector<int>& values) {
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
   * @param {number} k
   * @param {number[]} values
   * @return {number}
   */
  maxFinalSum(n, a, k, values) {
    // Implement here
    return 0;
  }
}
```
