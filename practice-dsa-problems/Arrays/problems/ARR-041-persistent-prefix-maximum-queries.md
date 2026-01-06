---
problem_id: ARR_PERSISTENT_PREFIX_MAXIMUM_QUERIES__9735
display_id: NTB-ARR-9735
slug: persistent-prefix-maximum-queries
title: "Persistent Prefix Maximum Queries"
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
  - persistent-prefix-maximum-queries
  - searching
  - technical-interview-prep
  - two-pointers
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Persistent Prefix Maximum Queries

## Problem Statement

You are given an initial array `a1..an` and must support versioned updates and queries.

- Version `0` is the initial array.
- Each update creates a new version with exactly one element changed.

Operations:

- `U v i x`: create a new version based on version `v` where `a[i] = x`.
- `Q v r`: return the maximum value in prefix `a[1..r]` of version `v`.

Output the answer for every query.

## Input Format

- First line: integers `n` and `q`
- Second line: `n` integers `a1 a2 ... an`
- Next `q` lines: operations `U` or `Q` as described

## Output Format

- For each `Q` operation, output a single integer on its own line

## Constraints

- `1 <= n, q <= 200000`
- `-10^9 <= a_i, x <= 10^9`
- `1 <= i <= n`
- `1 <= r <= n`

## Clarifying Notes

- Updates do not modify earlier versions.
- Version IDs are 0-based and update operations create the next version ID in order.
- The intended data structure is a persistent segment tree.

## Example Input

```
5 4
1 3 -2 4 0
Q 0 3
U 0 2 10
Q 1 4
Q 0 5
```

## Example Output

```
3
10
4
```

## Solution Stub

### Java

```java
class Solution {
    public int[] persistentPrefixMax(int n, int q, int[] a, String[][] operations) {
        // Implement here
        return new int[0];
    }
}
```

### Python

```python
class Solution:
    def persistentPrefixMax(self, n: int, q: int, a: list[int], operations: list[list[str]]) -> list[int]:
        # Implement here
        return []
```

### C++

```cpp
class Solution {
public:
    vector<int> persistentPrefixMax(int n, int q, vector<int>& a, vector<vector<string>>& operations) {
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
  persistentPrefixMax(n, q, a, operations) {
    // Implement here
    return [];
  }
}
```
