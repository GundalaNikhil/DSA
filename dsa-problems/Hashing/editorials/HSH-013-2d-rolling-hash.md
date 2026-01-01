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
---

# HSH-013: 2D Rolling Hash for Matrix Match

## 📋 Problem Summary

You are given a large matrix `A` (`N x M`) and a smaller pattern matrix `B` (`P x Q`).
Determine if `B` exists as a submatrix within `A`.

## 🌍 Real-World Scenario

**Scenario Title:** Image Recognition

Think of finding a specific icon (like a "Save" button) on a screenshot of a desktop.
- The screenshot is a large grid of pixels (Matrix A).
- The icon is a small grid of pixels (Matrix B).
- You want to find the coordinates where the icon appears.
- 2D Hashing allows scanning the image efficiently without comparing every pixel repeatedly.

![Real-World Application](../images/HSH-013/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: 2D Hashing

Matrix B (2x2):
```
1 2
3 4
```

**Step 1: Row Hashing**
Hash each row of B individually (using Base `B_1`).
- Row 0: Hash([1, 2]) = `H_R0`
- Row 1: Hash([3, 4]) = `H_R1`

**Step 2: Column Hashing**
Hash the column of row hashes (using Base `B_2`).
- Col Hash: Hash([`H_R0, H_R1`]) = `H_Final`

**Scanning Matrix A:**
1. Compute rolling hashes for all rows of A (window size `Q`).
   - This creates a temporary matrix of row hashes.
2. Compute rolling hashes for columns of this temporary matrix (window size `P`).
3. Compare result with `H_Final`.

### Key Concept: Separable Hashing

A 2D hash can be computed by hashing rows first, then hashing the resulting columns.
`H(A) = sum_i=0^P-1 sum_j=0^Q-1 A[i][j] * B_1^P-1-i * B_2^Q-1-j`.
This allows us to use the rolling hash technique in two dimensions sequentially.

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** Matrix A (`N x M`), Matrix B (`P x Q`).
- **Output:** Boolean.
- **Constraints:** `N, M <= 1000`. Values up to `10^9`.
- **Time Limit:** 2000ms. `O(NM)` is required. Naive `O(NMPQ)` is too slow (`10^12` ops).

## Naive Approach

### Intuition

For every top-left position `(i, j)` in A, check if the submatrix matches B.

### Time Complexity

- **O(N * M * P * Q)**: In worst case.

## Optimal Approach

### Key Insight

Use **Rabin-Karp** extended to 2D.
1. **Precompute Row Hashes:** For each row in A, compute rolling hashes of length `Q`. Store in `rowHashes[N][M-Q+1]`.
2. **Compute Column Hashes:** For each column in `rowHashes`, compute rolling hashes of length `P`.
3. **Compare:** The result corresponds to the hash of a `P x Q` submatrix. Compare with B's hash.

### Algorithm

1. Calculate hash of B (`H_B`).
   - Hash rows of B -> `tempB`.
   - Hash `tempB` column -> `H_B`.
2. Hash rows of A.
   - For each row `i`, compute rolling hashes of window size `Q`.
   - Store in `H[i][j]` (hash of `A[i][j dots j+Q-1]`).
3. Hash columns of `H`.
   - For each column `j`, compute rolling hashes of window size `P`.
   - Result `Final[i][j]` is hash of submatrix at `(i, j)`.
4. If any `Final[i][j] == H_B`, return true.

### Time Complexity

- **O(NM)**: Each cell visited constant times.

### Space Complexity

- **O(NM)**: To store intermediate hashes. Can be optimized to `O(M)` if processing row-by-row carefully.

![Algorithm Visualization](../images/HSH-013/algorithm-visualization.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
A (3x3), B (2x2).
A: `[[1,2,3], [4,5,6], [7,8,9]]`
B: `[[5,6], [8,9]]`

**B Hash:**
- Row 0 (5,6): `5B_1 + 6`.
- Row 1 (8,9): `8B_1 + 9`.
- Final: `(5B_1+6)B_2 + (8B_1+9)`.

**A Row Hashes (Window 2):**
- Row 0: `[1,2]`, `[2,3]`
- Row 1: `[4,5]`, `[5,6]`
- Row 2: `[7,8]`, `[8,9]`

**A Col Hashes (Window 2):**
- Col 0: `[Row0[0], Row1[0]]` -> `[1,2]` then `[4,5]`. No match.
- Col 1: `[Row0[1], Row1[1]]` -> `[2,3]` then `[5,6]`.
  - Next window: `[Row1[1], Row2[1]]` -> `[5,6]` then `[8,9]`.
  - This matches B! Return true.

## ✅ Proof of Correctness

### Invariant
The 2D hash uniquely (with high probability) represents the submatrix content.
The rolling hash correctly updates row hashes horizontally and column hashes vertically.

## 💡 Interview Extensions

- **Extension 1:** Count occurrences of B in A.
  - *Answer:* Increment counter instead of returning true.
- **Extension 2:** Find largest square submatrix appearing twice.
  - *Answer:* Binary search on size + 2D hashing.

### Common Mistakes to Avoid

1. **Order of Hashing**
   - ❌ Wrong: Hashing all cells in one giant polynomial.
   - ✅ Correct: Row-then-Column or Column-then-Row structure preserves 2D spatial relationships.
2. **Base Choice**
   - ❌ Wrong: Same base for rows and columns.
   - ✅ Correct: Different bases minimize collisions (e.g., `[1, 2], [3, 4]` vs `[1, 3], [2, 4]`).

## Related Concepts

- **Aho-Corasick 2D:** For multiple patterns.
- **Quadtrees:** For sparse matrices.
