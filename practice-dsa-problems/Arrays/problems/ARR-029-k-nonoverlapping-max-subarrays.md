---
problem_id: ARR_K_NONOVERLAPPING_MAX_SUBARRAYS__6606
display_id: NTB-ARR-6606
slug: k-nonoverlapping-max-subarrays
title: "K Non-Overlapping Max Subarrays"
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
  - k-nonoverlapping-max-subarrays
  - searching
  - technical-interview-prep
  - two-pointers
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# K Non-Overlapping Max Subarrays

## Problem Statement

Given an array `a1..an` and an integer `K`, choose exactly `K` non-overlapping, non-empty subarrays to maximize the total sum of their elements.

## Input Format

- First line: integers `n` and `K`
- Second line: `n` integers `a1 a2 ... an`

## Output Format

- Single integer: maximum total sum using exactly `K` subarrays

## Constraints

- `1 <= n <= 200000`
- `1 <= K <= n`
- `-10^9 <= a_i <= 10^9`

## Clarifying Notes

- Subarrays must be contiguous and cannot overlap.
- You must select exactly `K` subarrays.

## Example Input

```
5 2
1 2 -1 2 3
```

## Example Output

```
8
```

## Solution Stub

### Java

```java
class Solution {
    public long kMaxNonOverlappingSubarrays(int n, int k, int[] a) {
        // Implement here
        return 0;
    }
}
```

### Python

```python
class Solution:
    def kMaxNonOverlappingSubarrays(self, n: int, k: int, a: list[int]) -> int:
        # Implement here
        return 0
```

### C++

```cpp
class Solution {
public:
    long long kMaxNonOverlappingSubarrays(int n, int k, vector<int>& a) {
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
  kMaxNonOverlappingSubarrays(n, k, a) {
    // Implement here
    return 0;
  }
}
```
