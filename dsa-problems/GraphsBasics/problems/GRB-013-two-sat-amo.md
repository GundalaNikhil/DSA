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
time_limit: 2000
memory_limit: 256
---
# GRB-013: 2-SAT with At-Most-One Constraints
## Problem Statement
You are given a 2-SAT formula with `n` boolean variables `x1..xn`. Each clause is of the form `(a OR b)` where `a` and `b` are literals. Additionally, you are given several **at-most-one** constraints: within each subset, at most one variable can be true.
Determine whether the formula is satisfiable and, if it is, output one valid assignment.
![Problem Illustration](../images/GRB-013/problem-illustration.png)
## Input Format
- First line: integers `n` and `m`
- Next `m` lines: two integers `a` and `b` (literals, negative means negation)
- Next line: integer `g`, number of at-most-one groups
- Next `g` lines: integer `k` followed by `k` variable indices (1-based)
Literals use integers from `1..n` for `xi` and `-i` for `¬xi`.
## Output Format
- If unsatisfiable: print `UNSAT`
- If satisfiable: print `SAT` and then a line of `n` integers (0/1) for `x1..xn`
## Constraints
- `1 <= n <= 100000`
- `0 <= m <= 200000`
- Total size of all groups `<= 200000`
## Example
**Input:**
```
2 1
1 2
1
2 1 2
```
**Output:**
```
SAT
1 0
```
**Explanation:**
Clause `(x1 OR x2)` and at-most-one `{x1,x2}` allow either variable to be true.
![Example Visualization](../images/GRB-013/example-1.png)
## Notes
- Encode each clause into an implication graph.
- Encode at-most-one constraints with pairwise implications.
- Use SCC to solve 2-SAT and produce an assignment.
## Related Topics
2-SAT, Implication Graph, SCC
---
## Solution Template
### Java
### Python
### C++
### JavaScript
