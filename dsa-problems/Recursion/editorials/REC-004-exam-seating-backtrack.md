---
title: Exam Seating Backtrack
slug: exam-seating-backtrack
difficulty: Medium
difficulty_score: 44
tags:
- Recursion
- Backtracking
- Combinatorics
problem_id: REC_EXAM_SEATING_BACKTRACK__6392
display_id: REC-004
topics:
- Recursion
- Backtracking
- Combinatorics
---
# Exam Seating Backtrack - Editorial

## Problem Summary

You need to place `k` students in a row of `n` seats. The constraint is that any two students must have at least `d` empty seats between them. You need to find the total number of valid arrangements.


## Constraints

- `1 <= n <= 15`
- `0 <= k <= n`
- `0 <= d <= n`
## Real-World Scenario

Think of **Social Distancing** in a movie theater or a waiting room. To prevent the spread of germs, people cannot sit directly next to each other. If the rule is "keep 2 seats empty between people", how many ways can you seat 3 people in a row of 10 chairs?

Another example is **Planting Trees**. You want to plant saplings in a row, but their roots need space to spread. You must leave at least `d` meters (units) of soil between any two saplings.

## Problem Exploration

### 1. The Constraint
If student A is at index `i` and student B is at index `j` (where `i < j`), the number of empty seats between them is `j - i - 1`.
The condition "at least `d` empty seats" translates to:
`j - i - 1 >= d`
`j - i >= d + 1`
`j >= i + d + 1`

This means if we place a student at index `i`, the next student can only be placed at index `i + d + 1` or greater.

### 2. Recursive Structure
We can define a function `count(index, students_left)`:
-   `index`: The current seat we are considering (or the earliest seat we *can* consider).
-   `students_left`: How many more students we need to place.

At each step, we have two choices for the current `index`:
1.  **Place a student here**: We use 1 student. The next available seat becomes `index + d + 1`.
2.  **Leave this seat empty**: We don't use a student. The next available seat is `index + 1`.

### 3. Base Cases
-   If `students_left == 0`: We have successfully placed everyone. This counts as 1 valid arrangement.
-   If `index >= n`: We ran out of seats. If `students_left > 0`, this path is invalid (return 0).

## Approaches

### Approach 1: Pure Backtracking
We implement the recursive logic described above.
`solve(index, k) = solve(index + d + 1, k - 1) + solve(index + 1, k)`
-   First term: Place student at `index`.
-   Second term: Skip `index`.

-   **Complexity**: Roughly related to combinations `binomNK`. With `N <= 15`, this is very small and runs instantly.

### Approach 2: Dynamic Programming / Memoization
If `N` were larger (e.g., 1000), we would see overlapping subproblems. For example, skipping seat 0 then seat 1 leads to state `(2, k)`, same as skipping seat 0 and placing at 1 (if constraints allowed) might lead to similar future states.
We can memoize `(index, k)`.
Given `N <= 15`, memoization is not strictly necessary but good practice.

### Approach 3: Combinatorics (Math)
We can transform this into a standard combination problem.
We have `k` students and `n` seats.
We need to place `k-1` blocks of `d` empty seats between the students.
Total fixed "empty" seats = `(k - 1) * d`.
Remaining seats available for free distribution = `n - (k - 1) * d`.
Let `M = n - (k - 1) * d`.
We are now placing `k` students in `M` effective slots.
The answer is `binomMk`.
-   *Check*: Example `5 2 2`. `n=5, k=2, d=2`.
    -   Fixed empty seats = `(2-1)*2 = 2`.
    -   `M = 5 - 2 = 3`.
    -   `binom32 = 3`. Correct.
-   *Note*: The problem asks for a recursive solution (implied by "Backtrack" in title and tags), so we will implement Approach 1/2. But Approach 3 is the `O(1)` optimal solution.

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)
**Input:** `5 2 2` (5 seats, 2 students, 2 empty seats between)

1.  `solve(0, 2)`
    -   Place at 0: Need `solve(0 + 2 + 1, 1)` -> `solve(3, 1)`
        -   `solve(3, 1)`:
            -   Place at 3: Need `solve(3 + 2 + 1, 0)` -> `solve(6, 0)` -> Returns 1. (Valid: 0, 3)
            -   Skip 3: Need `solve(4, 1)`
                -   Place at 4: Need `solve(7, 0)` -> Returns 1. (Valid: 0, 4)
                -   Skip 4: Need `solve(5, 1)` -> Returns 0.
            -   `solve(3, 1)` returns `1 + 1 = 2`.
    -   Skip 0: Need `solve(1, 2)`
        -   Place at 1: Need `solve(1 + 2 + 1, 1)` -> `solve(4, 1)`
            -   Place at 4: Need `solve(7, 0)` -> Returns 1. (Valid: 1, 4)
            -   Skip 4: Need `solve(5, 1)` -> Returns 0.
            -   `solve(4, 1)` returns 1.
        -   Skip 1: Need `solve(2, 2)`
            -   Place at 2: Need `solve(5, 1)` -> Returns 0.
            -   Skip 2: Need `solve(3, 2)` -> Returns 0 (not enough space).
    -   `solve(0, 2)` returns `2 + 1 = 3`.

**Output:** `3`.

## Proof of Correctness

The recursive function explores the two fundamental choices at each step (occupy or skip).
-   The transition `idx + d + 1` enforces the constraint that if a seat is occupied, the next `d` seats must be empty.
-   The base case `k=0` correctly identifies a valid arrangement.
-   The base case `idx >= n` correctly identifies an invalid path (ran out of space).
Since these cover all possibilities and constraints, the sum of leaf nodes returning 1 is the total count.

## Interview Extensions

1.  **What if the seats are arranged in a circle?**
    -   We can fix the first student at position 0, solve the linear problem for the rest, then account for the wraparound constraint (last student vs first student). Or iterate through all possible starting positions for the first student (up to `d+1` positions is enough due to symmetry) and solve linear.

2.  **What if students are distinct (order matters)?**
    -   Multiply the result by `k!`.

3.  **Optimize for large N?**
    -   Use the combinatorial formula `binomn - (k-1)dk`.

### Common Mistakes

-   **Off-by-one in gap**: Using `idx + d` instead of `idx + d + 1`. The problem says `d` *empty* seats, so the next student is at `d+1` distance.
-   **Base case ordering**: Checking `idx >= n` before `k == 0`. If `idx == n` and `k == 0`, it's a valid solution (last student placed exactly at end). Checking bounds first might return 0 incorrectly.

## Related Concepts

-   **Backtracking**: Choice exploration.
-   **Combinations with Repetition/Constraints**: Stars and Bars variations.
