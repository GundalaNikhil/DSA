---
problem_id: DP_CACHE_REPLACEMENT__3086
display_id: NTB-DP-3086
slug: cache-replacement
title: "Cache Replacement Policy DP"
difficulty: Medium
difficulty_score: 50
topics:
  - Dynamic Programming
tags:
  - algorithms
  - cache-replacement
  - coding-interviews
  - data-structures
  - dp
  - memoization
  - optimization
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Cache Replacement Policy DP

## Problem Statement

You are given an access sequence of `n` keys and a cache of capacity `C`. On each access, you may choose which key to evict if the cache is full. A miss costs 1, a hit costs 0. Compute the minimum possible total misses.

## Input Format

- First line: integers `n` and `C`
- Second line: `n` integers: access sequence

## Output Format

- Single integer: minimum possible misses

## Constraints

- `1 <= n <= 200`
- `1 <= C <= 6`
- Keys are 32-bit signed integers

## Clarifying Notes

- Cache state is a set; order does not matter.
- This is an optimal offline policy DP.

## Example Input

```
5 2
1 2 3 2 1
```

## Example Output

```
4
```

## Solution Stub

```java
public class Solution {
    public int minMisses(int n, int C, int[] sequence) {
        // Your code here
        return 0;
    }
}
```

```python
class Solution:
    def minMisses(self, n: int, C: int, sequence: list[int]) -> int:
        # Your code here
        return 0
```

```cpp
class Solution {
public:
    int minMisses(int n, int C, vector<int>& sequence) {
        // Your code here
        return 0;
    }
};
```

```javascript
class Solution {
  minMisses(n, C, sequence) {
    // Your code here
    return 0;
  }
}
```
