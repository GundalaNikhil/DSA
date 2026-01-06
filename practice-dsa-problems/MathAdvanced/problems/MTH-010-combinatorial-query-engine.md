---
problem_id: MTH_COMBINATORIAL_QUERY_ENGINE__9056
display_id: NTB-MTH-9056
slug: combinatorial-query-engine
title: "Combinatorial Query Engine"
difficulty: Medium
difficulty_score: 50
topics:
  - Math Advanced
tags:
  - advanced-math
  - algorithms
  - coding-interviews
  - combinatorial-query-engine
  - cryptography
  - data-structures
  - mathadvanced
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Combinatorial Query Engine

## Problem Statement

Compute `C(n, k) mod M`, where `M` can be any composite number.

## Input Format

- First line: integer `q`.
- Next `q` lines: `n`, `k`, `M`.

## Output Format

- One integer per query.

## Constraints

- `1 <= q <= 10^2`.
- `0 <= k <= n <= 10^{18}`.
- `2 <= M <= 10^6`.

## Clarifying Notes

- $C(n, k) = \frac{n!}{k!(n-k)!}$.
- $M$ is not necessarily prime.

## Example Input

```
2
5 2 12
10 3 1000
```

## Example Output

```
10
120
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public List<Long> computeCombinations(int q, long[][] queries) {
        // Your code here
        return new ArrayList<>();
    }
}
```

```python
class Solution:
    def computeCombinations(self, q: int, queries: list[list[int]]) -> list[int]:
        # Your code here
        return []
```

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    vector<long long> computeCombinations(int q, vector<vector<long long>>& queries) {
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
  computeCombinations(q, queries) {
    // Your code here
    return [];
  }
}
```
