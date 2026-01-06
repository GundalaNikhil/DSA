---
problem_id: ARR_OFFLINE_QUERIES_MOS_MODIFICATIONS__8242
display_id: NTB-ARR-8242
slug: offline-queries-mos-modifications
title: "Offline Queries with Mo's and Modifications"
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
  - offline-queries-mos-modifications
  - searching
  - technical-interview-prep
  - two-pointers
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Offline Queries with Mo's and Modifications

## Problem Statement

You are given an array `a1..an` and `q` operations of two types:

- `U i x`: update `a[i] = x`
- `Q l r`: query the range `[l, r]`

For a query, define the score of a range as:

```
score = sum( value * (frequency)^2 ) over all distinct values in the range
```

You must output the score for each query in the order they appear. All operations are known in advance, and the intended solution uses Mo's algorithm with modifications.

## Input Format

- First line: integers `n` and `q`
- Second line: `n` integers `a1 a2 ... an`
- Next `q` lines: operations `U` or `Q` as described

## Output Format

- For each `Q` operation, output the score on its own line

## Constraints

- `1 <= n, q <= 200000`
- `-10^9 <= a_i, x <= 10^9`
- `1 <= l <= r <= n`

## Clarifying Notes

- The score uses the current array state after applying all prior updates.
- Distinct values may be large; coordinate compression is allowed.

## Example Input

```
5 5
1 2 1 3 2
Q 1 5
U 2 1
Q 1 3
U 5 1
Q 3 5
```

## Example Output

```
15
9
9
```

## Solution Stub

### Java

```java
class Solution {
    public long[] offlineMoQueries(int n, int q, int[] a, String[][] operations) {
        // Implement here
        return new long[0];
    }
}
```

### Python

```python
class Solution:
    def offlineMoQueries(self, n: int, q: int, a: list[int], operations: list[list[str]]) -> list[int]:
        # Implement here
        return []
```

### C++

```cpp
class Solution {
public:
    vector<long long> offlineMoQueries(int n, int q, vector<int>& a, vector<vector<string>>& operations) {
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
   * @param {number[]} a
   * @param {string[][]} operations
   * @return {number[]}
   */
  offlineMoQueries(n, q, a, operations) {
    // Implement here
    return [];
  }
}
```
