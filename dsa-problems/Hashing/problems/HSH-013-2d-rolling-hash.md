---
problem_id: HSH_2D_ROLLING_HASH__5849
display_id: HSH-013
slug: 2d-rolling-hash
title: "2D Rolling Hash for Matrix Match"
difficulty: Medium
difficulty_score: 60
topics:
  - Hashing
  - 2D Arrays
  - Pattern Matching
tags:
  - hashing
  - 2d-array
  - matrix
  - pattern-matching
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HSH-013: 2D Rolling Hash for Matrix Match

## Problem Statement

Given a matrix `A` (size `n × m`) and a smaller matrix `B` (size `p × q`), determine if `B` appears as a submatrix in `A` using 2D rolling hash.

![Problem Illustration](../images/HSH-013/problem-illustration.png)

## Input Format

- First line: two integers `n m` (dimensions of matrix A)
- Next `n` lines: `m` space-separated integers (matrix A)
- Next line: two integers `p q` (dimensions of matrix B)
- Next `p` lines: `q` space-separated integers (matrix B)

## Output Format

- Single word: `true` if B is found in A, `false` otherwise

## Constraints

- `1 <= p <= n <= 1000`
- `1 <= q <= m <= 1000`
- `0 <= A[i][j], B[i][j] <= 10^9`

## Example

**Input:**

```
3 3
1 2 3
4 5 6
7 8 9
2 2
5 6
8 9
```

**Output:**

```
true
```

**Explanation:**

Matrix A (3×3):

```
1 2 3
4 5 6
7 8 9
```

Matrix B (2×2):

```
5 6
8 9
```

B appears in A starting at position (1, 1).

![Example Visualization](../images/HSH-013/example-1.png)

## Notes

- Compute 2D hash for matrix B
- Use 2D rolling hash to check all possible positions in A
- Hash function: combine row hashes with polynomial hash
- Time complexity: O(n × m)
- Space complexity: O(n × m)

## Related Topics

2D Hashing, Matrix Pattern Matching, Rolling Hash, Rabin-Karp 2D

---

## Solution Template

### Java


### Python


### C++


### JavaScript

