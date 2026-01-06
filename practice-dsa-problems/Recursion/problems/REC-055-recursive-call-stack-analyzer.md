---
problem_id: REC_RECURSIVE_CALL_STACK_ANALYZER__3244
display_id: NTB-REC-3244
slug: recursive-call-stack-analyzer
title: "Recursive Call Stack Analyzer"
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
  - recursive-call-stack-analyzer
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Recursive Call Stack Analyzer

## Problem Statement

You are given a call graph of functions. Each function has a frame size `f[i]`. Calls are either normal or tail calls. A tail call reuses the current frame size instead of pushing a new frame.

Starting from entry function `S`, compute the maximum stack usage possible along any call path.

## Input Format

- First line: integers `n`, `m`, and `S`
- Next `n` lines: `f[i]`
- Next `m` lines: `u v type` where `type` is `N` (normal) or `T` (tail)

## Output Format

- Single integer: maximum possible stack usage

## Constraints

- `1 <= n <= 200000`
- `0 <= m <= 300000`
- `0 <= f[i] <= 10^9`

## Clarifying Notes

- The call graph is a DAG.
- A tail call replaces the current frame size with the callee's frame size.

## Example Input

```
3 2 1
5
3
7
1 2 N
2 3 T
```

## Example Output

```
12
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public long maxStackUsage(int n, int m, int S, long[] frameSizes, List<Object[]> calls) {
        // Your code here
        return 0;
    }
}
```

```python
class Solution:
    def maxStackUsage(self, n: int, m: int, S: int, frame_sizes: list[int], calls: list[list[str]]) -> int:
        # Your code here
        return 0
```

```cpp
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    long long maxStackUsage(int n, int m, int S, vector<long long>& frameSizes, vector<pair<int, pair<int, char>>>& calls) {
        // Your code here
        return 0;
    }
};
```

```javascript
class Solution {
  /**
   * @param {number} n
   * @param {number} m
   * @param {number} S
   * @param {number[]} frameSizes
   * @param {Array<[number, number, string]>} calls
   * @returns {number}
   */
  maxStackUsage(n, m, S, frameSizes, calls) {
    // Your code here
    return 0;
  }
}
```
