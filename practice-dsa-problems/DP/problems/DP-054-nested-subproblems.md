---
problem_id: DP_NESTED_SUBPROBLEMS__5619
display_id: NTB-DP-5619
slug: nested-subproblems
title: "DP with Nested Subproblems"
difficulty: Medium
difficulty_score: 50
topics:
  - Dynamic Programming
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - dp
  - memoization
  - nested-subproblems
  - optimization
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP with Nested Subproblems

## Problem Statement

You must split an array into `k` segments. The score of a segment is the maximum subarray sum within that segment. Maximize the total score across all segments.

## Input Format

- First line: integers `n` and `k`
- Second line: `n` integers: array values

## Output Format

- Single integer: maximum total score

## Constraints

- `1 <= n <= 200`
- `1 <= k <= n`
- `-10^9 <= values <= 10^9`

## Clarifying Notes

- Each segment's inner maximum subarray sum is a DP subproblem.

## Example Input

```
5 2
1 -2 3 -1 2
```

## Example Output

```
5
```

## Solution Stub

### Java

```java
class Solution {
    public long maxTotalScore(int n, int k, int[] values) {
        // Implement here
        return 0;
    }
}
```

### Python

```python
class Solution:
    def maxTotalScore(self, n: int, k: int, values: list[int]) -> int:
        # Implement here
        return 0
```

### C++

```cpp
class Solution {
public:
    long long maxTotalScore(int n, int k, vector<int>& values) {
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
   * @param {number[]} values
   * @return {number}
   */
  maxTotalScore(n, k, values) {
    // Implement here
    return 0;
  }
}
```
