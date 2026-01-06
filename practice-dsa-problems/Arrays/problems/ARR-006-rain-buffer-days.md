---
problem_id: ARR_RAIN_BUFFER_DAYS__9135
display_id: NTB-ARR-9135
slug: rain-buffer-days
title: "Rain Buffer Days"
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
  - rain-buffer-days
  - searching
  - technical-interview-prep
  - two-pointers
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Rain Buffer Days

## Problem Statement

Given an array `a1..an`, a day `i` is called a **rain buffer day** if:

- `a_i < 0` (rainfall day), and
- `a_{i+1} > 0` and `a_{i+2} > 0` (two positive recovery days)

Count how many rain buffer days exist.

## Input Format

- First line: integer `n`
- Second line: `n` integers `a1 a2 ... an`

## Output Format

- Single integer: count of rain buffer days

## Constraints

- `1 <= n <= 200000`
- `-10^9 <= a_i <= 10^9`

## Clarifying Notes

- Indices `i` with `i+2 > n` cannot be rain buffer days.

## Example Input

```
7
-1 2 3 -4 5 6 7
```

## Example Output

```
2
```

## Solution Stub

### Java

```java
class Solution {
    public int countRainBufferDays(int n, int[] a) {
        // Implement here
        return 0;
    }
}
```

### Python

```python
class Solution:
    def countRainBufferDays(self, n: int, a: list[int]) -> int:
        # Implement here
        return 0
```

### C++

```cpp
class Solution {
public:
    int countRainBufferDays(int n, vector<int>& a) {
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
  countRainBufferDays(n, a) {
    // Implement here
    return 0;
  }
}
```
