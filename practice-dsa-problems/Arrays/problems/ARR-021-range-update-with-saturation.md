---
problem_id: ARR_RANGE_UPDATE_WITH_SATURATION__9156
display_id: NTB-ARR-9156
slug: range-update-with-saturation
title: "Range Update with Saturation"
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
  - range-update-with-saturation
  - searching
  - technical-interview-prep
  - two-pointers
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Range Update with Saturation

## Problem Statement

You are given an array `a1..an`, a saturation cap `C`, and `q` range increment operations. Each operation is:

```
L R delta
```

which adds `delta` to all elements in indices `[L, R]` (1-based). After all operations, each element is capped at `C`:

```
final_i = min(C, a_i + total_increment_i)
```

Output the final array.

## Input Format

- First line: integers `n`, `q`, and `C`
- Second line: `n` integers `a1 a2 ... an`
- Next `q` lines: integers `L R delta`

## Output Format

- `n` integers: the final array values

## Constraints

- `1 <= n, q <= 200000`
- `-10^9 <= a_i, delta <= 10^9`
- `-10^9 <= C <= 10^9`
- `1 <= L <= R <= n`

## Clarifying Notes

- Saturation is applied only after all updates are combined.
- `C` can be less than initial values.

## Example Input

```
3 2 5
1 4 2
1 2 3
2 3 2
```

## Example Output

```
4 5 4
```

## Solution Stub

### Java

```java
class Solution {
    public int[] rangeUpdateWithSaturation(int n, int q, int c, int[] a, int[][] queries) {
        // Implement here
        return new int[0];
    }
}
```

### Python

```python
class Solution:
    def rangeUpdateWithSaturation(self, n: int, q: int, c: int, a: list[int], queries: list[list[int]]) -> list[int]:
        # Implement here
        return []
```

### C++

```cpp
class Solution {
public:
    vector<int> rangeUpdateWithSaturation(int n, int q, int c, vector<int>& a, vector<vector<int>>& queries) {
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
   * @param {number} q
   * @param {number} c
   * @param {number[]} a
   * @param {number[][]} queries
   * @return {number[]}
   */
  rangeUpdateWithSaturation(n, q, c, a, queries) {
    // Implement here
    return [];
  }
}
```
