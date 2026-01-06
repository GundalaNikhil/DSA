---
problem_id: ARR_MIN_DELETIONS_BITONIC__8377
display_id: NTB-ARR-8377
slug: min-deletions-bitonic
title: "Minimum Deletions to Make Bitonic"
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
  - min-deletions-bitonic
  - searching
  - technical-interview-prep
  - two-pointers
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Minimum Deletions to Make Bitonic

## Problem Statement

Given an array `a1..an`, remove the minimum number of elements so that the remaining sequence is **strictly increasing** and then **strictly decreasing**. The peak element must have at least one element on both sides.

If it is impossible to form such a sequence, output `-1`.

## Input Format

- First line: integer `n`
- Second line: `n` integers `a1 a2 ... an`

## Output Format

- Single integer: minimum deletions, or `-1` if impossible

## Constraints

- `1 <= n <= 200000`
- `-10^9 <= a_i <= 10^9`

## Clarifying Notes

- The final sequence must have length at least 3.
- Strictly increasing means every next element is larger, and strictly decreasing means every next element is smaller.

## Example Input

```
4
1 2 3 2
```

## Example Output

```
0
```

## Solution Stub

### Java

```java
class Solution {
    public int minDeletionsToBitonic(int n, int[] a) {
        // Implement here
        return -1;
    }
}
```

### Python

```python
class Solution:
    def minDeletionsToBitonic(self, n: int, a: list[int]) -> int:
        # Implement here
        return -1
```

### C++

```cpp
class Solution {
public:
    int minDeletionsToBitonic(int n, vector<int>& a) {
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
   * @param {number[]} a
   * @return {number}
   */
  minDeletionsToBitonic(n, a) {
    // Implement here
    return -1;
  }
}
```
