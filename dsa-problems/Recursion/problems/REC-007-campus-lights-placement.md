---
problem_id: REC_CAMPUS_LIGHTS_PLACEMENT__4928
display_id: REC-007
slug: campus-lights-placement
title: "Campus Lights Placement"
difficulty: Medium
difficulty_score: 47
topics:
  - Recursion
  - Backtracking
  - Combinations
tags:
  - recursion
  - backtracking
  - combinations
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# REC-007: Campus Lights Placement

## Problem Statement

A campus walkway has `n` positions labeled `0` to `n-1`. Place exactly `k` lights so that any two lights are at least `d` positions apart (absolute difference >= `d`).

Generate all valid sets of positions in increasing order.

![Problem Illustration](../images/REC-007/problem-illustration.png)

## Input Format

- First line: integers `n`, `k`, and `d`

## Output Format

- Each valid placement on its own line as space-separated positions
- Output `NONE` if no valid placement exists

## Constraints

- `1 <= n <= 12`
- `0 <= k <= n`
- `0 <= d <= n`

## Example

**Input:**

```
5 2 2
```

**Output:**

```
0 2
0 3
1 3
1 4
2 4
```

**Explanation:**

Each listed pair has distance at least 2.

![Example Visualization](../images/REC-007/example-1.png)

## Notes

- Build positions in increasing order to avoid duplicates
- Prune when remaining positions are insufficient
- Track the last chosen position to enforce distance
- Time complexity is exponential in `n`

## Related Topics

Backtracking, Combinatorics, Recursion

---

## Solution Template
### Java


### Python


### C++


### JavaScript

