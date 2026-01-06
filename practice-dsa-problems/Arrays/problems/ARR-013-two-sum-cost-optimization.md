---
problem_id: ARR_TWO_SUM_COST_OPTIMIZATION__8919
display_id: NTB-ARR-8919
slug: two-sum-cost-optimization
title: "Two Sum with Cost Optimization"
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
  - two-sum-cost-optimization
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Two Sum with Cost Optimization

## Problem Statement

You are given two arrays of length `n`: values `a1..an` and costs `c1..cn`, and a target sum `T`. Find a pair of indices `(i, j)` with `i < j` such that `a_i + a_j = T`.

Among all valid pairs, choose the one with minimum `c_i + c_j`. If there is still a tie, choose the pair with the smallest `i`, and then the smallest `j`.

If no valid pair exists, output `-1`.

## Input Format

- First line: integers `n` and `T`
- Second line: `n` integers `a1 a2 ... an`
- Third line: `n` integers `c1 c2 ... cn`

## Output Format

- If a pair exists: output two integers `i j`
- Otherwise: output `-1`

## Constraints

- `1 <= n <= 200000`
- `-10^9 <= a_i, T <= 10^9`
- `0 <= c_i <= 10^9`

## Clarifying Notes

- Indices are 1-based in the output.
- Each index can be used at most once.

## Example Input

```
5 5
4 2 7 1 3
5 2 6 1 4
```

## Example Output

```
1 4
```

## Solution Stub

### Java

```java
class Solution {
    public int[] findOptimalTwoSum(int n, long t, int[] a, int[] c) {
        // Implement here
        return new int[]{-1};
    }
}
```

### Python

```python
class Solution:
    def findOptimalTwoSum(self, n: int, t: int, a: list[int], c: list[int]) -> list[int]:
        # Implement here
        return [-1]
```

### C++

```cpp
class Solution {
public:
    vector<int> findOptimalTwoSum(int n, long long t, vector<int>& a, vector<int>& c) {
        // Implement here
        return {-1};
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
   * @param {number[]} c
   * @return {number[]}
   */
  findOptimalTwoSum(n, t, a, c) {
    // Implement here
    return [-1];
  }
}
```
