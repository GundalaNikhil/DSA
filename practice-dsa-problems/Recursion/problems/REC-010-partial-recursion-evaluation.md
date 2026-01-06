---
problem_id: REC_PARTIAL_RECURSION_EVALUATION__9729
display_id: NTB-REC-9729
slug: partial-recursion-evaluation
title: "Partial Recursion Evaluation"
difficulty: Medium
difficulty_score: 50
topics:
  - Recursion
tags:
  - algorithms
  - backtracking
  - coding-interviews
  - data-structures
  - partial-recursion-evaluation
  - recursion
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Partial Recursion Evaluation

## Problem Statement

You are given a rooted tree. Each node has two values: `exact` and `estimate`. A recursive evaluation returns:

- If depth <= `D`: `exact + sum(child results)`
- If depth > `D`: `estimate` (children are not evaluated)

Compute the value returned from the root.

## Input Format

- First line: integers `n` and `D`
- Next `n` lines: `exact estimate parent` (parent is 0 for root)

## Output Format

- Single integer: root value

## Constraints

- `1 <= n <= 200000`
- `0 <= D <= 200000`
- `-10^9 <= exact, estimate <= 10^9`

## Clarifying Notes

- Depth of root is 0.

## Example Input

```
3 0
5 1 0
2 10 1
3 10 1
```

## Example Output

```
1
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public long evaluatePartialRecursion(int n, int D, long[][] nodes) {
        // Your code here
        return 0;
    }
}
```

```python
class Solution:
    def evaluatePartialRecursion(self, n: int, D: int, nodes: list[list[int]]) -> int:
        # Your code here
        return 0
```

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    long long evaluatePartialRecursion(int n, int D, vector<vector<long long>>& nodes) {
        // Your code here
        return 0;
    }
};
```

```javascript
class Solution {
  /**
   * @param {number} n
   * @param {number} D
   * @param {number[][]} nodes
   * @returns {number}
   */
  evaluatePartialRecursion(n, D, nodes) {
    // Your code here
    return 0;
  }
}
```
