---
problem_id: REC_RECURSIVE_FAULT_INJECTION__1411
display_id: NTB-REC-1411
slug: recursive-fault-injection
title: "Recursive Fault Injection"
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
  - recursive-fault-injection
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Recursive Fault Injection

## Problem Statement

You are given a rooted tree. Each node has a primary value `v` and a backup value `b`. A list of fault-injected nodes is provided; these nodes must use their backup value.

A node is considered faulty if it uses its backup value. Each node also has a fault tolerance limit `T`: if more than `T` faulty nodes appear in its subtree, the entire subtree fails and contributes `0`.

Compute the final value of the root.

## Input Format

- First line: integers `n` and `F`
- Second line: `F` integers, the fault-injected node indices
- Next `n` lines: `v b T parent` (parent is 0 for root)

## Output Format

- Single integer: root value

## Constraints

- `1 <= n <= 200000`
- `0 <= F <= n`
- `-10^9 <= v, b <= 10^9`
- `0 <= T <= 200000`

## Clarifying Notes

- Fault counts are local to each subtree.
- If a subtree fails, it contributes `0` and is not counted as faulty for its parent.

## Example Input

```
4 1
3
5 1 1 0
2 2 0 1
7 0 0 1
3 3 1 2
```

## Example Output

```
7
```
