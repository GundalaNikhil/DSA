---
problem_id: MTH_PRODUCT_TIMELINE_OPTIMIZER__1534
display_id: NTB-MTH-1534
slug: product-timeline-optimizer
title: "Product Launch Timeline Optimizer"
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
  - product-timeline-optimizer
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Product Launch Timeline Optimizer

## Problem Statement

To produce product `N`, a company needs machinery that can collectively handle all prime power factors of `N`. Machine type `i` is available starting from day `i`.

Find the earliest day `t` such that `N` divides `LCM(1, 2, ..., t)`.

If no such `t` exists within the bound `t <= 10^7`, output `-1`.

## Input Format

- First line: integer `q`.
- Next `q` lines: integer `N`.

## Output Format

- For each query, output the minimum `t` or `-1` if infeasible.

## Constraints

- `1 <= q <= 2 * 10^5`.
- `1 <= N <= 10^{12}`.
- Search bound: `t <= 10^7`.

## Clarifying Notes

- `LCM(1, 2, ..., t)` is the least common multiple of all integers from 1 to `t`.
- `N` divides `LCM(1, ..., t)` if and only if for every prime power $p^e$ that divides $N$, $p^e \le t$.

## Example Input

```
4
1
12
64
9999999967
```

## Example Output

```
1
4
8
-1
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public List<Integer> findEarliestDay(int q, long[] N_values) {
        // Your code here
        return new ArrayList<>();
    }
}
```

```python
class Solution:
    def findEarliestDay(self, q: int, n_values: list[int]) -> list[int]:
        # Your code here
        return []
```

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> findEarliestDay(int q, vector<long long>& n_values) {
        // Your code here
        return {};
    }
};
```

```javascript
class Solution {
  /**
   * @param {number} q
   * @param {number[]} n_values
   * @returns {number[]}
   */
  findEarliestDay(q, n_values) {
    // Your code here
    return [];
  }
}
```
