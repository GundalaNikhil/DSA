---
problem_id: GRB_TWO_SAT_AMO__6607
display_id: GRB-013
slug: two-sat-amo
title: "2-SAT with At-Most-One Constraints"
difficulty: Medium
difficulty_score: 60
topics:
  - Graphs
  - 2-SAT
  - Implication Graph
tags:
  - graphs-basics
  - 2-sat
  - implications
  - medium
premium: true
subscription_tier: basic
---

# GRB-013: 2-SAT with At-Most-One Constraints

## 📋 Problem Summary

You are given a boolean formula with two types of constraints:
1.  **2-SAT Clauses:** `(a OR b)`
2.  **At-Most-One (AMO) Groups:** For a given set of variables, at most one can be true.

Determine if the formula is satisfiable and provide a valid assignment.

## 🌍 Real-World Scenario

**Scenario Title:** Conference Scheduling

Imagine you are scheduling talks for a conference.
-   **Variables:** `x_i` means "Talk i is scheduled in Slot A". `¬x_i` means "Talk i is scheduled in Slot B".
-   **2-SAT Constraints:** "Talk 1 and Talk 2 cannot both be in Slot A" -> `(¬x1 OR ¬x2)`. "Talk 3 must be in Slot B or Talk 4 in Slot A" -> `(¬x3 OR x4)`.
-   **AMO Constraints:** "Talks 5, 6, and 7 are by the same speaker, so at most one of them can be in Slot A (if Slot A is the morning session)".
-   Solving this ensures a conflict-free schedule.

![Real-World Application](../images/GRB-013/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Implication Graph:**
Clause `(A OR B)` is equivalent to:
-   `¬A => B` (If A is false, B must be true)
-   `¬B => A` (If B is false, A must be true)

**AMO Constraint:** `{x1, x2, x3}`
-   If `x1` is true, `x2` must be false (`x1 => ¬x2`).
-   If `x1` is true, `x3` must be false (`x1 => ¬x3`).
-   If `x2` is true, `x3` must be false (`x2 => ¬x3`).
-   ...and so on for all pairs.

**Graph Structure:**
Nodes `1..N` (True literals) and `N+1..2N` (False literals).
Edges represent implications.
If `x` and `¬x` are in the same Strongly Connected Component (SCC), it's **UNSAT**.

### Algorithm Steps

1.  **Build Graph:**
    -   Nodes `1..N` represent `x_i`. Nodes `N+1..2N` represent `¬x_i`.
    -   For each clause `(a OR b)`: Add edges `¬a -> b` and `¬b -> a`.
    -   For each AMO group `{v1, v2, ..., vk}`: Add edges `vi -> ¬vj` for all pairs `(i, j)`.
2.  **Find SCCs:** Use Tarjan's or Kosaraju's algorithm.
3.  **Check Satisfiability:**
    -   For every `i`, if `SCC[x_i] == SCC[¬x_i]`, return **UNSAT**.
4.  **Construct Assignment:**
    -   If `SCC[x_i] > SCC[¬x_i]` (in topological order), set `x_i = true`.
    -   Else `x_i = false`.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Literals:** Input uses `1..N` and `-1..-N`. Map `-i` to node `N+i`.
-   **AMO Size:** Sum of group sizes is small (200,000), but naive pairwise edges for a large group is O(K^2).
    -   **Optimization:** For large groups, O(K^2) is too slow. We need the **Commander Variable** or **Prefix/Suffix** optimization.
    -   **Note:** The problem statement says "Total size of all groups <= 200,000". This refers to sum of K. If one group has K=200,000, K^2 edges is 4*10^10, which will cause TLE.
    -   **Optimization Required:** We must use auxiliary variables to encode AMO in O(K) edges.

### AMO Optimization (Prefix/Suffix Method)
For group `{x1, ... xk}`, we want `xi -> ¬xj` for all `i != j`.
Introduce prefix variables `p1...pk`.
-   `pi` implies "at least one of x1...xi is true".
-   `pi -> pi+1`
-   `xi -> pi`
-   `pi-1 -> ¬xi` (If any of 1..i-1 is true, xi must be false).
Total edges: O(K).

## Naive Approach

### Intuition

Add pairwise edges for AMO constraints.

### Time Complexity

-   **O(N + M + Σ K^2)**: Worst case O(N^2). Fails for large groups.

## Optimal Approach (2-SAT + AMO Optimization)

Use auxiliary variables to reduce AMO constraints to linear size.

### Prefix Optimization Logic
For group `x1, ..., xk`:
Create `k` prefix nodes `P1, ..., Pk`.
1.  **Definition:** `Pi` is true if any of `x1...xi` is true.
2.  **Chain:** `P1 -> P2 -> ... -> Pk`. (If prefix i is true, prefix i+1 is true).
3.  **Variable to Prefix:** `xi -> Pi`. (If xi is true, prefix i is true).
4.  **Exclusion:** `Pi-1 -> ¬xi`. (If prefix i-1 is true, xi must be false).

This enforces that if `xi` is true, `Pi` becomes true, which forces `Pi+1...Pk` true. Also `Pi-1` being true forces `xi` false. This ensures at most one `x` is true.

### Time Complexity

-   **O(N + M + Σ K)**: Linear in input size.

### Space Complexity

-   **O(N + M + Σ K)**.

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
2 1
1 2
1
2 1 2
```
**Clauses:** `(1 OR 2)`
**AMO:** `{1, 2}`

**Graph Construction:**
-   Clause: `¬1 -> 2`, `¬2 -> 1`.
-   AMO (Prefix `P1, P2` for `1, 2`):
    -   `1 -> P1`
    -   `2 -> P2`
    -   `P1 -> P2`
    -   `P1 -> ¬2`

**Implications:**
-   If `1` is True:
    -   `1 -> P1` (True)
    -   `P1 -> ¬2` (True) -> `2` is False.
    -   Clause `1 OR 2` is satisfied (True OR False).
    -   Consistent.
-   If `2` is True:
    -   `2 -> P2` (True)
    -   From clause: `¬1 -> 2`.
    -   From AMO: `P1 -> ¬2`. Contrapositive `2 -> ¬P1`.
    -   `¬P1 -> ¬1`. So `2 -> ¬1`.
    -   Consistent.

**Result:** `SAT`. Assignment `1 0` or `0 1`.

## ✅ Proof of Correctness

The prefix optimization correctly encodes "At Most One":
-   If `xi` is true, `Pi` is true.
-   `Pi` implies `Pj` for all `j > i`.
-   `Pj-1` implies `¬xj`.
-   So if `xi` is true, `Pi` is true -> `Pi+1` true -> ...
-   Also `Pi` true implies `¬xi+1` true.
-   Thus `xi` true forces all subsequent `x` to be false.
-   Topological sort on SCC graph guarantees a valid truth assignment if no contradictions exist.

## 💡 Interview Extensions (High-Value Add-ons)

-   **3-SAT:** NP-Complete. 2-SAT is P.
-   **Max 2-SAT:** Finding assignment satisfying *maximum* clauses is NP-Hard.
-   **Commander Variable:** Another AMO optimization using a tree structure.

### Common Mistakes to Avoid

1.  **O(K^2) Edges:** Naively adding edges for every pair in an AMO group will TLE.
2.  **Indexing:** Mapping `¬x` to `x + N` requires careful offset management, especially with auxiliary variables.
3.  **SCC Order:** In Kosaraju's algorithm, components are found in reverse topological order. Higher component ID indicates earlier position in topological order. When `comp[x] > comp[¬x]`, variable `x` is upstream of `¬x`, implying `x -> ¬x`. To avoid contradiction (True -> True), set `x` to False. The correct assignment is `comp[x] > comp[¬x] ? 0 : 1`.
