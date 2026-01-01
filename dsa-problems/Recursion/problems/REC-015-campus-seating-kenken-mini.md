---
problem_id: REC_CAMPUS_SEATING_KENKEN_MINI__1579
display_id: REC-015
slug: campus-seating-kenken-mini
title: "Campus Seating KenKen Mini"
difficulty: Medium
difficulty_score: 59
topics:
  - Recursion
  - Backtracking
  - Constraint Satisfaction
tags:
  - recursion
  - backtracking
  - kenken
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# REC-015: Campus Seating KenKen Mini
## Problem Statement
Solve a 4x4 KenKen-like puzzle. Fill digits 1 to 4 so that each row and column contains no repeated digits. Cages are provided with a target value and operation that must be satisfied by the digits in that cage.
Return any valid solution grid, or `NONE` if impossible.
![Problem Illustration](../images/REC-015/problem-illustration.png)
## Input Format
- First line: integer `c` (number of cages)
- Next `c` lines: `target op len r1 c1 r2 c2 ...`
  - `op` is one of `+`, `-`, `*`, `/`, or `=`
  - `len` is the number of cells in the cage
  - coordinates are zero-based
## Output Format
- If solvable, output 4 lines each with 4 integers
- Otherwise output `NONE`
## Constraints
- Grid size is fixed at 4x4
- `1 <= c <= 16`
- All cage cells are within the grid
## Example
**Input:**
```
16
1 = 1 0 0
2 = 1 0 1
3 = 1 0 2
4 = 1 0 3
3 = 1 1 0
4 = 1 1 1
1 = 1 1 2
2 = 1 1 3
2 = 1 2 0
1 = 1 2 1
4 = 1 2 2
3 = 1 2 3
4 = 1 3 0
3 = 1 3 1
2 = 1 3 2
1 = 1 3 3
```
**Output:**
```
1 2 3 4
3 4 1 2
2 1 4 3
4 3 2 1
```
**Explanation:**
Each row and column is a permutation of 1..4, and every single-cell cage matches its target.
![Example Visualization](../images/REC-015/example-1.png)
## Notes
- For `+` and `*`, order does not matter
- For `-` and `/`, use absolute difference or quotient between two values
- Use backtracking with row/column constraints
- Any valid solution is acceptable
## Related Topics
Backtracking, Constraint Satisfaction, Recursion
---
## Solution Template
### Java
### Python
### C++
### JavaScript
