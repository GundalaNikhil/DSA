---
problem_id: ARR_SEASONAL_PROFIT_WINDOW__7267
display_id: NTB-ARR-7267
slug: seasonal-profit-window
title: "Seasonal Profit Window"
difficulty: Medium
difficulty_score: 50
topics:
  - Arrays
tags:
  - algorithms
  - array-manipulation
  - arrays
  - coding-interviews
  - data-structures
  - searching
  - seasonal-profit-window
  - technical-interview-prep
  - two-pointers
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Seasonal Profit Window

## Problem Statement

You are given an array `a1..an` of daily profit values (positive or negative). For any subarray, define the **adjusted sum** as:

- If `x >= 0`, contribution is `x`.
- If `x < 0`, contribution is `-ceil(|x| / 2)`.

Your task is to find the maximum adjusted sum over all subarrays of length **at least** `K`.

## Input Format

- First line: integers `n` and `K`
- Second line: `n` integers `a1 a2 ... an`

## Output Format

- Single integer: maximum adjusted sum among all subarrays of length >= `K`

## Constraints

- `1 <= n <= 200000`
- `1 <= K <= n`
- `-10^9 <= a_i <= 10^9`

## Clarifying Notes

- `ceil(|x| / 2)` is computed as `(abs(x) + 1) // 2`.
- The subarray must be contiguous.

## Example Input

```
5 2
3 -4 2 -1 5
```

## Example Output

```
7
```

## Solution Stub

### Java

```java
class Solution {
    public long maxAdjustedSum(int n, int k, int[] a) {
        // Implement here
        return 0;
    }
}
```

### Python

```python
class Solution:
    def maxAdjustedSum(self, n: int, k: int, a: list[int]) -> int:
        # Implement here
        return 0
```

### C++

```cpp
class Solution {
public:
    long long maxAdjustedSum(int n, int k, vector<int>& a) {
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
   * @param {number} k
   * @param {number[]} a
   * @return {number}
   */
  maxAdjustedSum(n, k, a) {
    // Implement here
    return 0;
  }
}
```
