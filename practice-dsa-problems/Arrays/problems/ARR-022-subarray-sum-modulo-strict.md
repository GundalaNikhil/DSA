---
problem_id: ARR_SUBARRAY_SUM_MODULO_STRICT__6301
display_id: NTB-ARR-6301
slug: subarray-sum-modulo-strict
title: "Subarray Sum Modulo M (Strict)"
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
  - subarray-sum-modulo-strict
  - technical-interview-prep
  - two-pointers
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Subarray Sum Modulo M (Strict)

## Problem Statement

Given an array `a1..an`, an integer `M`, and a minimum length `L`, count how many subarrays have:

- length >= `L`, and
- sum % `M` == 0

## Input Format

- First line: integers `n`, `M`, and `L`
- Second line: `n` integers `a1 a2 ... an`

## Output Format

- Single integer: number of qualifying subarrays

## Constraints

- `1 <= n <= 200000`
- `1 <= M <= 200000`
- `1 <= L <= n`
- `-10^9 <= a_i <= 10^9`

## Clarifying Notes

- Subarrays are contiguous and non-empty.
- Modulo for negative sums should be normalized into `[0, M-1]`.

## Example Input

```
5 3 2
1 2 3 4 1
```

## Example Output

```
3
```

## Solution Stub

### Java

```java
class Solution {
    public long countSubarraysModuloM(int n, int m, int l, int[] a) {
        // Implement here
        return 0;
    }
}
```

### Python

```python
class Solution:
    def countSubarraysModuloM(self, n: int, m: int, l: int, a: list[int]) -> int:
        # Implement here
        return 0
```

### C++

```cpp
class Solution {
public:
    long long countSubarraysModuloM(int n, int m, int l, vector<int>& a) {
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
   * @param {number} l
   * @param {number[]} a
   * @return {number}
   */
  countSubarraysModuloM(n, m, l, a) {
    // Implement here
    return 0;
  }
}
```
