---
problem_id: MTH_CRYPTOGRAPHIC_EQUATION_SOLVER__1155
display_id: NTB-MTH-1155
slug: cryptographic-equation-solver
title: "Cryptographic Equation Solver"
difficulty: Medium
difficulty_score: 50
topics:
  - Math Advanced
tags:
  - advanced-math
  - algorithms
  - coding-interviews
  - cryptographic-equation-solver
  - cryptography
  - data-structures
  - mathadvanced
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Cryptographic Equation Solver

## Problem Statement

Given an odd prime `p`, an exponent `e`, and a value `A`, count the number of solutions to:

```
x² ≡ A (mod p^e)
```

where `0 <= x < p^e`.

## Input Format

- First line: integer `q`.
- Next `q` lines: `p`, `e`, `A`.

## Output Format

- Number of solutions per query.

## Constraints

- `1 <= q <= 2 * 10^5`.
- `p` is an odd prime, `3 <= p <= 10^9`.
- `1 <= e <= 30`.
- `0 <= A < p^e`.

## Example Input

```
3
5 1 4
5 2 4
7 1 3
```

## Example Output

```
2
2
0
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public List<Integer> countSolutions(int q, long[][] queries) {
        // Your code here
        return new ArrayList<>();
    }
}
```

```python
class Solution:
    def countSolutions(self, q: int, queries: list[list[int]]) -> list[int]:
        # Your code here
        return []
```

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> countSolutions(int q, vector<vector<long long>>& queries) {
        // Your code here
        return {};
    }
};
```

```javascript
class Solution {
  /**
   * @param {number} q
   * @param {number[][]} queries
   * @returns {number[]}
   */
  countSolutions(q, queries) {
    // Your code here
    return [];
  }
}
```
