---
problem_id: ARR_MIN_OPS_EQUALIZE_PREFIXES__7666
display_id: NTB-ARR-7666
slug: min-ops-equalize-prefixes
title: "Minimum Operations to Equalize Prefixes"
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
  - min-ops-equalize-prefixes
  - searching
  - technical-interview-prep
  - two-pointers
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Minimum Operations to Equalize Prefixes

## Problem Statement

You are given an array `a1..an` and a target value `T`. You may apply the following operations:

1. `INC i`: increment all elements in prefix `[1..i]` by 1.
2. `ROT i`: rotate the prefix `[1..i]` left by 1 (cyclic shift).

Your goal is to make every prefix sum equal to `i * T` for all `i = 1..n`. This is equivalent to making every element equal to `T`.

Find the minimum number of operations required. If it is impossible, output `-1`.

## Input Format

- First line: integers `n` and `T`
- Second line: `n` integers `a1 a2 ... an`

## Output Format

- Single integer: minimum number of operations, or `-1` if impossible

## Constraints

- `1 <= n <= 200000`
- `-10^9 <= a_i, T <= 10^9`

## Clarifying Notes

- Only increments are allowed; values can never decrease.
- If any `a_i > T`, the answer is `-1`.

## Example Input

```
4 3
3 3 3 3
```

## Example Output

```
0
```

## Solution Stub

### Java

```java
class Solution {
    public long minOpsToEqualize(int n, int t, int[] a) {
        // Implement here
        return -1;
    }
}
```

### Python

```python
class Solution:
    def minOpsToEqualize(self, n: int, t: int, a: list[int]) -> int:
        # Implement here
        return -1
```

### C++

```cpp
class Solution {
public:
    long long minOpsToEqualize(int n, int t, vector<int>& a) {
        // Implement here
        return -1;
    }
};
```

### JavaScript

```javascript
class Solution {
  /**
   * @param {number} n
   * @param {number} t
   * @param {number[]} a
   * @return {number}
   */
  minOpsToEqualize(n, t, a) {
    // Implement here
    return -1;
  }
}
```
