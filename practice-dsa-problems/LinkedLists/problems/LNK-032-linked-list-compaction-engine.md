---
problem_id: LNK_LINKED_LIST_COMPACTION_ENGINE__1513
display_id: NTB-LNK-1513
slug: linked-list-compaction-engine
title: "Linked List Compaction Engine"
difficulty: Medium
difficulty_score: 50
topics:
  - Linked Lists
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - linked-list-compaction-engine
  - linkedlists
  - memory-management
  - pointers
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Linked List Compaction Engine

## Problem Statement

Each node has a label and size. A compaction pass merges consecutive nodes with the same label if their total size does not exceed `S`.

After compaction, merged nodes keep the label and have size equal to the sum. Repeat passes until no more merges are possible. Output the final list.

## Input Format

- First line: integers `n` and `S`
- Next `n` lines: `label size`

## Output Format

- First line: integer `k`, number of nodes after compaction
- Next `k` lines: `label size`

## Constraints

- `1 <= n <= 200000`
- `1 <= S <= 10^9`
- `1 <= size <= 10^9`

## Clarifying Notes

- Merges happen left to right in each pass.
- If a merge occurs, a new pass is started from the beginning.

## Example Input

```
4 6
A 2
A 3
A 2
B 1
```

## Example Output

```
2
A 5
B 1
```
