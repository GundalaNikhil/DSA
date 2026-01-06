---
problem_id: ARR_ARRAY_GAME_WITH_PENALTIES__9080
display_id: NTB-ARR-9080
slug: array-game-with-penalties
title: "Array Game with Penalties"
difficulty: Medium
difficulty_score: 50
topics:
  - Arrays
tags:
  - algorithms
  - array-game-with-penalties
  - array-manipulation
  - arrays
  - coding-interviews
  - data-structures
  - searching
  - technical-interview-prep
  - two-pointers
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Array Game with Penalties

## Problem Statement

You are given an array `a1..an` and an integer `K`. You start at index 1 with score `a1` and must reach index `n`. From index `i`, you may jump to any `j` such that `1 <= j - i <= K`.

Your score is the sum of values at all visited indices. Negative values reduce the score. Find the maximum possible score to reach index `n`.

## Input Format

- First line: integers `n` and `K`
- Second line: `n` integers `a1 a2 ... an`

## Output Format

- Single integer: maximum achievable score at index `n`

## Constraints

- `1 <= n <= 200000`
- `1 <= K <= n`
- `-10^9 <= a_i <= 10^9`

## Clarifying Notes

- You must start at index 1 and end at index `n`.
- Jumps must always move forward.

## Example Input

```
5 2
1 -5 4 -2 3
```

## Example Output

```
8
```

## Solution Stub

### Java

```java
class Solution {
    public long maxScoreInGame(int n, int k, int[] a) {
        // Implement here
        return 0;
    }
}
```

### Python

```python
class Solution:
    def maxScoreInGame(self, n: int, k: int, a: list[int]) -> int:
        # Implement here
        return 0
```

### C++

```cpp
class Solution {
public:
    long long maxScoreInGame(int n, int k, vector<int>& a) {
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
  maxScoreInGame(n, k, a) {
    // Implement here
    return 0;
  }
}
```
