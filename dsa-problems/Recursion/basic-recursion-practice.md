# Original Recursion & Backtracking Practice Set (16 Questions)

## 1) Dorm Room Paths
- Slug: dorm-room-paths
- Difficulty: Easy
- Problem: Count ways to move from (0,0) to (r-1,c-1) on a grid with only right/down moves and no blocked cells, using pure recursion with memoization.
- Constraints: `1 <= r,c <= 25`.
- Example:
  - Input: `r=2, c=3`
  - Output: `3`

## 2) Lab ID Permutations With No Adjacent Twins
- Slug: lab-id-permutations-no-twins
- Difficulty: Easy-Medium
- Problem: Generate all unique permutations of a string (may have duplicates) such that no two identical characters are adjacent. Return them in lexicographic order.
- Constraints: `1 <= |s| <= 8`.
- Example:
  - Input: `"aab"`
  - Output: `["aba"]`

## 3) Campus Ticket Packs
- Slug: campus-ticket-packs
- Difficulty: Medium
- Problem: Each ticket value `v[i]` comes in packs of size `p[i]`; you must take either 0 or exactly `p[i]` of that value. List all unique combinations reaching exactly `target`.
- Constraints: `1 <= n <= 15`, `1 <= target <= 200`, `1 <= p[i] <= 10`.
- Example:
  - Input: `v=[2,3], p=[2,1], target=7`
  - Output: `[[2,2,3]]`

## 4) Exam Seating Backtrack
- Slug: exam-seating-backtrack
- Difficulty: Medium
- Problem: Place `k` students in `n` seats (1D array) so that any two students are at least `d` seats apart. Count valid arrangements.
- Constraints: `1 <= n <= 15`, `0 <= k <= n`.
- Example:
  - Input: `n=5, k=2, d=2`
  - Output: `3`

## 5) Robot Route With Turns
- Slug: robot-route-turns
- Difficulty: Medium
- Problem: On a grid with obstacles, find any path from start to end with at most `T` turns (direction changes). Return one valid path as a sequence of coordinates or empty if none.
- Constraints: `1 <= r,c <= 8`, `T <= 6`.
- Example:
  - Input: grid `[[0,0,0],[1,1,0],[0,0,0]]`, T=2
  - Output: `[(0,0),(0,1),(0,2),(1,2),(2,2)]`

## 6) Subset Sum Exact Count
- Slug: subset-sum-exact-count
- Difficulty: Medium
- Problem: Determine if there exists a subset of exactly `k` numbers that sums to `target`; return one such subset or empty.
- Constraints: `1 <= n <= 20`, `|arr[i]| <= 10^4`.
- Example:
  - Input: `arr=[4,1,6,2], k=2, target=7`
  - Output: `[1,6]`

## 7) Campus Lights Placement
- Slug: campus-lights-placement
- Difficulty: Medium
- Problem: Given a row of `n` positions, place exactly `k` lights so that any two lights are at least `d` apart. Generate all valid position sets in increasing order.
- Constraints: `1 <= n <= 12`.
- Example:
  - Input: `n=5, k=2, d=2`
  - Output: `[[0,2],[0,3],[1,3],[1,4],[2,4]]`

## 8) Alternating Vowel-Consonant Ladder
- Slug: alternating-vowel-consonant-ladder
- Difficulty: Medium
- Problem: Given start, end, and dictionary, find all shortest ladders where each step changes one letter, stays in dictionary, and the word types must alternate vowel-start and consonant-start. Return all shortest sequences.
- Constraints: `1 <= |word| <= 6`, `dict size <= 3000`.
- Example:
  - Input: start `"eat"`, end `"cot"`, dict `["eat","cat","cot","eot"]`
  - Output: `[["eat","cat","cot"],["eat","eot","cot"]]`

## 9) Expression Target With One Negation Flip
- Slug: expression-target-one-flip
- Difficulty: Medium
- Problem: Given digits string `s` and target `T`, insert `+` or `-` or concatenate to form expressions evaluating to `T`, but you may also choose exactly one operand chunk to negate without using an operator (a unary flip applied to a chosen concatenated number). Use at most `c` binary operators total. Multiplication is NOT allowed. Return all valid expressions.
- Constraints: `1 <= |s| <= 10`, `0 <= c <= 9`, `-10^9 <= T <= 10^9`; no leading zeros in any chunk unless the chunk is exactly "0".
- Example:
  - Input: `s="1203", T=0, c=2`
  - Output: `["1+-203", "12-12+0"]` (first uses the unary flip on chunk 203)

## 10) Restore Matrix With Upper Bounds
- Slug: restore-matrix-upper-bounds
- Difficulty: Medium
- Problem: Given row sums, column sums, and a matrix of per-cell upper bounds `u[i][j]`, construct any non-negative integer matrix satisfying all sums and bounds, or return empty if impossible.
- Constraints: `1 <= r,c <= 6`, sums up to `20`, `0 <= u[i][j] <= 20`.
- Example:
  - Input: rowSums `[3,4]`, colSums `[4,3]`, bounds `[[2,3],[3,4]]`
  - Output: `[[2,1],[2,2]]`

## 11) Campus Course Ordering
- Slug: campus-course-ordering
- Difficulty: Medium
- Problem: Given `n` courses and prerequisites, return all possible topological orderings (all valid course sequences).
- Constraints: `1 <= n <= 8`, edges <= 15.
- Example:
  - Input: `n=3`, prereq `[(0,1),(0,2)]`
  - Output: `[[0,1,2],[0,2,1]]`

## 12) Knight Tour With Blocked Cells
- Slug: knight-tour-blocked
- Difficulty: Medium
- Problem: On an `n x n` board (n<=5) with some blocked cells that cannot be visited, find a knight’s path starting at (0,0) visiting all unblocked cells exactly once, or state none exists.
- Constraints: `1 <= n <= 5`, blocked count < n^2.
- Example:
  - Input: `n=4`, blocked={(1,1)}
  - Output: A valid path covering 15 cells

## 13) Palindrome Partition with Minimum Count
- Slug: palindrome-partition-min-count
- Difficulty: Medium
- Problem: Partition string into palindromic substrings of length at most `L` using the minimum possible number of substrings. Return all partitions achieving that minimum.
- Constraints: `1 <= |s| <= 12`, `1 <= L <= |s|`.
- Example:
  - Input: `s="aab", L=2`
  - Output: `[["aa","b"]]`

## 14) Target Sum With Limited Negations
- Slug: target-sum-limited-negations
- Difficulty: Medium
- Problem: Given `nums` and integer `K`, assign each number either `+` or `-` sign, but at most `K` numbers may be negated (given `K <= n`). Count assignments equaling `target`.
- Constraints: `1 <= n <= 20`, `|nums[i]| <= 20`.
- Example:
  - Input: `nums=[1,2,3], K=1, target=2`
  - Output: `2` (assignments: [+1,+2,-3], [-1,+2,+3])

## 15) Campus Seating KenKen Mini
- Slug: campus-seating-kenken-mini
- Difficulty: Medium
- Problem: Solve a 4x4 KenKen-like puzzle: fill digits 1-4 so rows/cols have no repeats, and given cages with target and operation (+,-,*,/) must be satisfied. Return one solution or state impossible.
- Constraints: 4x4 grid; cages <= 8.
- Example:
  - Input: cages with targets/ops provided
  - Output: A valid filled grid

## 16) Lexicographic Gray Code
- Slug: lexicographic-gray-code
- Difficulty: Medium
- Problem: Generate an `n`-bit Gray code sequence in lexicographic order (not the usual reflected order). Each consecutive pair differs by 1 bit; sequence is sorted lexicographically.
- Constraints: `1 <= n <= 12`.
- Example:
  - Input: `n=2`
  - Output: `["00","01","11","10"]`
