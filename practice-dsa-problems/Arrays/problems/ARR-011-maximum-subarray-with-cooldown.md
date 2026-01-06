---
problem_id: ARR_MAXIMUM_SUBARRAY_WITH_COOLDOWN__9389
display_id: NTB-ARR-9389
slug: maximum-subarray-with-cooldown
title: "Maximum Subarray with Cooldown"
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
  - maximum-subarray-with-cooldown
  - searching
  - technical-interview-prep
  - two-pointers
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Maximum Subarray with Cooldown

## Problem Statement

You are given an array `a1..an` and an integer `X`. You may select one or more non-overlapping subarrays. If you select a subarray that ends at index `r`, the next selected subarray must start at index `r + X + 1` or later (cooldown of `X` elements).

Find the maximum total sum of selected subarrays. You must select at least one subarray.

## Input Format

- First line: integers `n` and `X`
- Second line: `n` integers `a1 a2 ... an`

## Output Format

- Single integer: maximum total sum under the cooldown rule

## Constraints

- `1 <= n <= 200000`
- `0 <= X <= n`
- `-10^9 <= a_i <= 10^9`

## Clarifying Notes

- Subarrays must be contiguous and non-overlapping.
- The cooldown applies between any two consecutive chosen subarrays.

## Example Input

```
6 1
4 -1 3 -2 5 -1
```

## Example Output

```
11
```

## Solution Stub

### Java

```java
class Solution {
    public long maxSubarrayWithCooldown(int n, int x, int[] a) {
        // Implement here
        return 0;
    }
}
```

### Python

```python
class Solution:
    def maxSubarrayWithCooldown(self, n: int, x: int, a: list[int]) -> int:
        # Implement here
        return 0
```

### C++

```cpp
class Solution {
public:
    long long maxSubarrayWithCooldown(int n, int x, vector<int>& a) {
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
   * @param {number[]} a
   * @return {number}
   */
  maxSubarrayWithCooldown(n, x, a) {
    // Implement here
    return 0;
  }
}
```
