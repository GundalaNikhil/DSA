---
problem_id: MTH_RESOURCE_ALLOCATION_OPTIMIZER__6940
display_id: NTB-MTH-6940
slug: resource-allocation-optimizer
title: "Resource Allocation Optimizer"
difficulty: Medium
difficulty_score: 50
topics:
  - Math Advanced
tags:
  - advanced-math
  - algorithms
  - coding-interviews
  - cryptography
  - data-structures
  - mathadvanced
  - resource-allocation-optimizer
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Resource Allocation Optimizer

## Problem Statement

A system allocates resources in an arithmetic pattern: `a, a+d, a+2d, ..., a+(n-1)d`.
The system requires the total sum to be divisible by `M`. You can add a non-negative integer `x` to every server.

Find the minimum `x >= 0` such that:

```
Σ (i=0 to n-1) (a + i*d + x) ≡ 0 (mod M)
```

## Input Format

- First line: integer `q`.
- Next `q` lines: `a`, `d`, `n`, `M`.

## Output Format

- Minimum `x` for each query. If no such `x` exists, output `-1`.

## Constraints

- `1 <= q <= 2 * 10^5`.
- `0 <= a, d, n <= 10^{18}`.
- `1 <= M <= 10^{18}`.

## Clarifying Notes

- Sum of the progression: $S = n \cdot a + \frac{d \cdot n \cdot (n-1)}{2} + n \cdot x$.
- You are solving for the smallest $x \ge 0$ such that $n \cdot x \equiv -S_0 \pmod M$, where $S_0 = n \cdot a + \frac{d \cdot n \cdot (n-1)}{2}$.

## Example Input

```
2
1 1 4 6
5 3 3 7
```

## Example Output

```
1
6
```

## Solution Stub

```java
import java.util.*;
import java.math.BigInteger;

public class Solution {
    public List<BigInteger> solveMinimumX(int q, long[][] queries) {
        // Your code here
        return new ArrayList<>();
    }
}
```

```python
class Solution:
    def solveMinimumX(self, q: int, queries: list[list[int]]) -> list[int]:
        # Your code here
        return []
```

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    typedef __int128_t int128;
    vector<long long> solveMinimumX(int q, vector<vector<long long>>& queries) {
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
   * @returns {bigint[]}
   */
  solveMinimumX(q, queries) {
    // Your code here
    return [];
  }
}
```
