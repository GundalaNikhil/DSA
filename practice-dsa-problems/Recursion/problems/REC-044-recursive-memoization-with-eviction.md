---
problem_id: REC_RECURSIVE_MEMOIZATION_WITH_EVICTION__5562
display_id: NTB-REC-5562
slug: recursive-memoization-with-eviction
title: "Recursive Memoization with Eviction"
difficulty: Medium
difficulty_score: 50
topics:
  - Recursion
tags:
  - algorithms
  - backtracking
  - coding-interviews
  - data-structures
  - recursion
  - recursive-memoization-with-eviction
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Recursive Memoization with Eviction

## Problem Statement

You are given a recursive function:

- `F(0) = A0`
- `F(1) = A1`
- `F(x) = F(x-1) + F(x-2) + C[x]` for `x >= 2`

You will answer a sequence of queries `Q`. For each query `x`, compute `F(x)` using memoization with an LRU cache of size `M`.

Count how many times `F(x)` is computed on a cache miss (including base cases). Output the total number of cache misses across all queries, and then the query answers modulo `1,000,000,007`.

## Input Format

- First line: integers `Q`, `M`
- Second line: integers `A0` and `A1`
- Third line: integer `N` (maximum index for `C`)
- Fourth line: `N+1` integers `C[0..N]` (values for `C[0]` and `C[1]` are ignored)
- Fifth line: `Q` integers `x1..xQ`

## Output Format

- First line: total cache misses
- Second line: `Q` integers, the results for each query modulo `1,000,000,007`

## Constraints

- `1 <= Q <= 200000`
- `1 <= M <= 200000`
- `0 <= N <= 200000`
- `0 <= x <= N`
- `0 <= A0, A1, C[i] <= 10^9`

## Clarifying Notes

- The cache stores computed values `F(x)`; LRU order updates on every access.
- A cache miss occurs when a needed `F(x)` is not stored and must be computed.

## Example Input

```
3 2
1 2
5
0 0 3 1 4 2
3 4 3
```

## Example Output

```
5
8 13 8
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public static class Result {
        public long cacheMisses;
        public long[] queryAnswers;
        public Result(long cacheMisses, long[] queryAnswers) {
            this.cacheMisses = cacheMisses;
            this.queryAnswers = queryAnswers;
        }
    }

    public Result evaluateWithLRUCache(int Q, int M, long A0, long A1, int N, long[] C, int[] x) {
        // Your code here
        return null;
    }
}
```

```python
class Solution:
    def evaluateWithLRUCache(self, Q: int, M: int, A0: int, A1: int, N: int, C: list[int], x: list[int]) -> tuple[int, list[int]]:
        # Your code here
        return 0, []
```

```cpp
#include <vector>

using namespace std;

struct Result {
    long long cacheMisses;
    vector<int> queryAnswers;
};

class Solution {
public:
    Result evaluateWithLRUCache(int Q, int M, long long A0, long long A1, int N, vector<long long>& C, vector<int>& x) {
        // Your code here
        return {0, {}};
    }
};
```

```javascript
class Solution {
  /**
   * @param {number} Q
   * @param {number} M
   * @param {number} A0
   * @param {number} A1
   * @param {number} N
   * @param {number[]} C
   * @param {number[]} x
   * @returns {{cacheMisses: number, queryAnswers: number[]}}
   */
  evaluateWithLRUCache(Q, M, A0, A1, N, C, x) {
    // Your code here
    return { cacheMisses: 0, queryAnswers: [] };
  }
}
```
