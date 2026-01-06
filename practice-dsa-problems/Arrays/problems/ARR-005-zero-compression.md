---
problem_id: ARR_ZERO_COMPRESSION__2654
display_id: NTB-ARR-2654
slug: zero-compression
title: "Zero Compression"
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
  - technical-interview-prep
  - two-pointers
  - zero-compression
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Zero Compression

## Problem Statement

Given an array `a1..an`, compress zeros and move them to the end:

1. A **zero block** is a maximal consecutive sequence of zeros in the original array.
2. Remove all zeros, keeping the relative order of non-zero elements.
3. Append exactly one zero for each zero block.

Output the resulting array.

## Input Format

- First line: integer `n`
- Second line: `n` integers `a1 a2 ... an`

## Output Format

- First line: integer `m`, the length of the resulting array
- Second line: `m` integers: the compressed array

## Constraints

- `1 <= n <= 200000`
- `-10^9 <= a_i <= 10^9`

## Clarifying Notes

- The output length can be smaller than `n` when zero blocks exist.
- Non-zero elements remain in their original order.

## Example Input

```
10
1 0 0 2 0 3 0 0 0 4
```

## Example Output

```
7
1 2 3 4 0 0 0
```

## Solution Stub

### Java

```java
class Solution {
    public int[] zeroCompression(int n, int[] a) {
        // Implement here
        return new int[0];
    }
}
```

### Python

```python
class Solution:
    def zeroCompression(self, n: int, a: list[int]) -> list[int]:
        # Implement here
        return []
```

### C++

```cpp
class Solution {
public:
    vector<int> zeroCompression(int n, vector<int>& a) {
        // Implement here
        return {};
    }
};
```

### JavaScript

```javascript
class Solution {
  /**
   * @param {number} n
   * @param {number[]} a
   * @return {number[]}
   */
  zeroCompression(n, a) {
    // Implement here
    return [];
  }
}
```
