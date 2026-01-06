---
problem_id: REC_RECURSIVE_CHECKSUM_VALIDATION__8669
display_id: NTB-REC-8669
slug: recursive-checksum-validation
title: "Recursive Checksum Validation"
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
  - recursive-checksum-validation
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Recursive Checksum Validation

## Problem Statement

You are given a rooted tree. Each node has a value `v` and a coefficient `coef`. Define a checksum recursively:

- For a leaf: `chk = (v * coef) mod M`
- For an internal node: `chk = (v * coef + sum(child chk)) mod M`

You are given a target checksum `T`. Determine if the root checksum equals `T`.

## Input Format

- First line: integers `n`, `M`, `T`
- Next `n` lines: `v coef parent` (parent is 0 for root)

## Output Format

- Print `YES` if the root checksum equals `T`, otherwise `NO`.

## Constraints

- `1 <= n <= 200000`
- `2 <= M <= 10^9 + 7`
- `0 <= T < M`
- `-10^9 <= v <= 10^9`
- `-10^9 <= coef <= 10^9`

## Clarifying Notes

- Use modular arithmetic for every addition and multiplication.
- Negative values are allowed; apply modulo normalization.

## Example Input

```
3 100 42
5 3 0
2 7 1
1 11 1
```

## Example Output

```
YES
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public String validateChecksum(int n, long M, long T, long[][] nodes) {
        // Your code here
        return "";
    }
}
```

```python
class Solution:
    def validateChecksum(self, n: int, M: int, T: int, nodes: list[list[int]]) -> str:
        # Your code here
        return ""
```

```cpp
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    string validateChecksum(int n, long long M, long long T, vector<vector<long long>>& nodes) {
        // Your code here
        return "";
    }
};
```

```javascript
class Solution {
  /**
   * @param {number} n
   * @param {number} M
   * @param {number} T
   * @param {number[][]} nodes
   * @returns {string}
   */
  validateChecksum(n, M, T, nodes) {
    // Your code here
    return "";
  }
}
```
