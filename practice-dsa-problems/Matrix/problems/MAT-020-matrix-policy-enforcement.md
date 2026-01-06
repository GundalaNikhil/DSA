---
problem_id: MAT_MATRIX_POLICY_ENFORCEMENT__9206
display_id: NTB-MAT-9206
slug: matrix-policy-enforcement
title: "Matrix Policy Enforcement"
difficulty: Medium
difficulty_score: 50
topics:
  - Matrix
tags:
  - 2d-arrays
  - algorithms
  - coding-interviews
  - data-structures
  - grids
  - matrix
  - matrix-policy-enforcement
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Matrix Policy Enforcement

## Problem Statement

You are given a matrix and a list of policies. Each policy applies to all `2 x 2` blocks:

- `SUM_LE X`: the sum of the 2 x 2 block must be `<= X`
- `HAS_ZERO`: the 2 x 2 block must contain at least one zero

Report all violations.

## Input Format

- First line: integers `n`, `m`, `p`
- Next `n` lines: `m` integers (matrix)
- Next `p` lines: policies (either `SUM_LE X` or `HAS_ZERO`)

## Output Format

- First line: integer `v`, number of violations
- Next `v` lines: `policy_id r c` where `r, c` are the top-left indices of the violating 2 x 2 block

## Constraints

- `2 <= n, m <= 500`
- `1 <= p <= 200000`
- `-10^9 <= matrix values <= 10^9`

## Clarifying Notes

- Policy ids are 1-based in input order.
- Output violations in increasing `policy_id`, then increasing `r`, then `c`.

## Example Input

```
2 3 2
1 2 3
4 0 6
SUM_LE 6
HAS_ZERO
```

## Example Output

```
1
1 1 2
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public static class Violation {
        public int policyId, r, c;
        public Violation(int policyId, int r, int c) {
            this.policyId = policyId;
            this.r = r;
            this.c = c;
        }
    }

    public List<Violation> findViolations(int n, int m, int p, int[][] matrix, List<String> policies) {
        // Your code here
        return new ArrayList<>();
    }
}
```

```python
class Violation:
    def __init__(self, policy_id: int, r: int, c: int):
        self.policy_id = policy_id
        self.r = r
        self.c = c

class Solution:
    def findViolations(self, n: int, m: int, p: int, matrix: list[list[int]], policies: list[str]) -> list[Violation]:
        # Your code here
        return []
```

```cpp
#include <vector>
#include <string>

using namespace std;

struct Violation {
    int policyId, r, c;
};

class Solution {
public:
    vector<Violation> findViolations(int n, int m, int p, vector<vector<int>>& matrix, vector<string>& policies) {
        // Your code here
        return {};
    }
};
```

```javascript
class Violation {
  constructor(policyId, r, c) {
    this.policyId = policyId;
    this.r = r;
    this.c = c;
  }
}

class Solution {
  /**
   * @param {number} n
   * @param {number} m
   * @param {number} p
   * @param {number[][]} matrix
   * @param {string[]} policies
   * @returns {Violation[]}
   */
  findViolations(n, m, p, matrix, policies) {
    // Your code here
    return [];
  }
}
```
