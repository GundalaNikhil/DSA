---
problem_id: ARR_SPLIT_ARRAY_BALANCED_ENERGY__4665
display_id: NTB-ARR-4665
slug: split-array-balanced-energy
title: "Split Array into Balanced Energy Segments"
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
  - split-array-balanced-energy
  - technical-interview-prep
  - two-pointers
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Split Array into Balanced Energy Segments

## Problem Statement

Given an array `a1..an` and an integer `K`, split the array into exactly `K` non-empty contiguous segments. The **energy** of a segment is the sum of its elements. Your goal is to minimize the maximum segment energy.

Output the minimum possible value of the maximum segment energy.

## Input Format

- First line: integers `n` and `K`
- Second line: `n` integers `a1 a2 ... an`

## Output Format

- Single integer: minimal possible maximum segment sum

## Constraints

- `1 <= n <= 200000`
- `1 <= K <= n`
- `-10^9 <= a_i <= 10^9`

## Clarifying Notes

- All segments must be non-empty and contiguous.
- The optimal split is based on sums, not lengths.

## Example Input

```
5 2
7 2 5 10 8
```

## Example Output

```
18
```

## Solution Stub

### Java

```java
class Solution {
    public long minimizeMaxSegmentEnergy(int n, int k, int[] a) {
        // Implement here
        return 0;
    }
}
```

### Python

```python
class Solution:
    def minimizeMaxSegmentEnergy(self, n: int, k: int, a: list[int]) -> int:
        # Implement here
        return 0
```

### C++

```cpp
class Solution {
public:
    long long minimizeMaxSegmentEnergy(int n, int k, vector<int>& a) {
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
  minimizeMaxSegmentEnergy(n, k, a) {
    // Implement here
    return 0;
  }
}
```
