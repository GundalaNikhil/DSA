---
problem_id: ARR_DISTINCT_UNTIL_REPEAT__4461
display_id: NTB-ARR-4461
slug: distinct-until-repeat
title: "Distinct Until Repeat"
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
  - distinct-until-repeat
  - searching
  - technical-interview-prep
  - two-pointers
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Distinct Until Repeat

## Problem Statement

Given an array `a1..an`, find the length of the longest prefix that contains no repeated values. The prefix ends right before the first duplicate appears.

## Input Format

- First line: integer `n`
- Second line: `n` integers `a1 a2 ... an`

## Output Format

- Single integer: length of the prefix before the first duplicate

## Constraints

- `1 <= n <= 200000`
- `-10^9 <= a_i <= 10^9`

## Clarifying Notes

- If the entire array has all distinct values, output `n`.

## Example Input

```
5
5 1 3 5 2
```

## Example Output

```
3
```

## Solution Stub

### Java

```java
class Solution {
    public int longestDistinctPrefix(int n, int[] a) {
        // Implement here
        return 0;
    }
}
```

### Python

```python
class Solution:
    def longestDistinctPrefix(self, n: int, a: list[int]) -> int:
        # Implement here
        return 0
```

### C++

```cpp
class Solution {
public:
    int longestDistinctPrefix(int n, vector<int>& a) {
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
   * @param {number[]} a
   * @return {number}
   */
  longestDistinctPrefix(n, a) {
    // Implement here
    return 0;
  }
}
```
