---
problem_id: MTH_MULTI_SYSTEM_SYNCHRONIZATION__7789
display_id: NTB-MTH-7789
slug: multi-system-synchronization
title: "Multi-System Synchronization"
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
  - multi-system-synchronization
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Multi-System Synchronization

## Problem Statement

Find the smallest non-negative integer `x` that satisfies a system of `k` congruences:

```
x ≡ a1 (mod m1)
x ≡ a2 (mod m2)
...
x ≡ ak (mod mk)
```

The moduli $m_i$ are **not** guaranteed to be pairwise coprime.

## Input Format

- First line: integer `q`.
- For each query:
  - First line: `k`.
  - Next `k` lines: `ai` and `mi`.

## Output Format

- Smallest `x >= 0` or `-1` if no solution exists.

## Constraints

- `1 <= q <= 10^2`.
- `1 <= k <= 10^2`.
- `0 <= ai < mi <= 10^{18}`.
- All $m_i > 0$.

## Example Input

```
2
2
2 6
5 9
2
1 4
2 6
```

## Example Output

```
14
-1
```

## Solution Stub

```java
import java.util.*;
import java.math.BigInteger;

public class Solution {
    public List<BigInteger> solveChineseRemainder(int q, List<List<long[]>> queries) {
        // Your code here
        return new ArrayList<>();
    }
}
```

```python
class Solution:
    def solveChineseRemainder(self, q: int, queries: list[list[list[int]]]) -> list[int]:
        # Your code here
        return []
```

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    typedef __int128_t int128;
    vector<long long> solveChineseRemainder(int q, vector<vector<pair<long long, long long>>>& queries) {
        // Your code here
        return {};
    }
};
```

```javascript
class Solution {
  /**
   * @param {number} q
   * @param {number[][][]} queries
   * @returns {bigint[]}
   */
  solveChineseRemainder(q, queries) {
    // Your code here
    return [];
  }
}
```
