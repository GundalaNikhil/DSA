---
problem_id: REC_RECURSIVE_PROOF_SEARCH__4753
display_id: NTB-REC-4753
slug: recursive-proof-search
title: "Recursive Proof Search"
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
  - recursive-proof-search
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Recursive Proof Search

## Problem Statement

You are given a set of inference rules. Each rule has a head symbol and a list of prerequisite symbols. A symbol is provable if there exists a rule whose prerequisites are all provable.

Given a start symbol `S`, compute the minimum number of rule applications needed to prove `S`. If `S` is not provable, output `IMPOSSIBLE`.

## Input Format

- First line: integers `R` and `S`
- Next `R` lines: `head k prereq1 prereq2 ... prereqk`

## Output Format

- Single integer: minimum number of rule applications, or `IMPOSSIBLE`

## Constraints

- `1 <= R <= 200000`
- `1 <= S <= 200000`
- `0 <= k <= 10`

## Clarifying Notes

- A rule with `k = 0` can be applied immediately and proves its head.
- Cycles do not imply provability; you must resolve them with base rules.

## Example Input

```
4 3
1 0
2 1 1
3 2 1 2
4 1 3
```

## Example Output

```
3
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public String minRuleApplications(int R, int S, int[][] rules) {
        // Your code here
        return "";
    }
}
```

```python
class Solution:
    def minRuleApplications(self, R: int, S: int, rules: list[list[int]]) -> str:
        # Your code here
        return ""
```

```cpp
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    string minRuleApplications(int R, int S, vector<vector<int>>& rules) {
        // Your code here
        return "";
    }
};
```

```javascript
class Solution {
  /**
   * @param {number} R
   * @param {number} S
   * @param {number[][]} rules
   * @returns {string}
   */
  minRuleApplications(R, S, rules) {
    // Your code here
    return "";
  }
}
```
