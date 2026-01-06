---
problem_id: ARR_ARRAY_TRANSFORMATION_LIMITED_SWAPS__6072
display_id: NTB-ARR-6072
slug: array-transformation-limited-swaps
title: "Array Transformation with Limited Swaps"
difficulty: Medium
difficulty_score: 50
topics:
  - Arrays
tags:
  - algorithms
  - array-manipulation
  - array-transformation-limited-swaps
  - arrays
  - coding-interviews
  - data-structures
  - searching
  - technical-interview-prep
  - two-pointers
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Array Transformation with Limited Swaps

## Problem Statement

You are given two arrays `A` and `B` of length `n` and an integer `K`. In one operation, you may swap two **adjacent** elements in `A`. Determine whether you can transform `A` into `B` using at most `K` adjacent swaps.

If the transformation is possible within `K` swaps, output `YES`. Otherwise, output `NO`.

## Input Format

- First line: integers `n` and `K`
- Second line: `n` integers `A1 A2 ... An`
- Third line: `n` integers `B1 B2 ... Bn`

## Output Format

- `YES` or `NO`

## Constraints

- `1 <= n <= 200000`
- `0 <= K <= 10^12`
- `-10^9 <= A_i, B_i <= 10^9`

## Clarifying Notes

- If `A` and `B` do not have the same multiset of values, the answer is `NO`.
- Adjacent swap count is the minimum number required to match the ordering.

## Example Input

```
4 1
1 2 1 3
1 1 2 3
```

## Example Output

```
YES
```

## Solution Stub

### Java

```java
class Solution {
    public boolean canTransform(int n, long k, int[] a, int[] b) {
        // Implement here
        return false;
    }
}
```

### Python

```python
class Solution:
    def canTransform(self, n: int, k: int, a: list[int], b: list[int]) -> bool:
        # Implement here
        return False
```

### C++

```cpp
class Solution {
public:
    bool canTransform(int n, long long k, vector<int>& a, vector<int>& b) {
        // Implement here
        return false;
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
   * @param {number[]} b
   * @return {boolean}
   */
  canTransform(n, k, a, b) {
    // Implement here
    return false;
  }
}
```
