---
problem_id: TRI_SHORTEST_ABSENT_BINARY__7241
display_id: TRI-013
slug: shortest-absent-binary-length-l
title: "Shortest Absent Binary String of Length L"
difficulty: Medium
difficulty_score: 52
topics:
  - Trie
  - Binary String
  - Backtracking
tags:
  - trie
  - binary
  - lexicographic
  - missing-element
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# TRI-013: Shortest Absent Binary String of Length L

## Problem Statement

Given a set of binary strings all of length exactly `L`, find the lexicographically smallest binary string of length `L` that is NOT present in the set. If all possible strings of length `L` are present, return an empty string.

![Problem Illustration](../images/TRI-013/problem-illustration.png)

## Input Format

- First line: two integers `L` (length) and `n` (number of binary strings)
- Next `n` lines: each contains a binary string of length exactly `L`

## Output Format

Return the lexicographically smallest missing binary string of length `L`, or an empty string if all are present.

## Constraints

- `1 <= L <= 20`
- `0 <= n <= 2^L` (set size cannot exceed total possibilities)
- All input strings have length exactly `L`
- Input strings consist only of '0' and '1'
- No duplicate strings in input

## Example

**Input:**

```
2 2
00
01
```

**Output:**

```
10
```

**Explanation:**

All possible binary strings of length 2: `["00", "01", "10", "11"]`

Given set: `{"00", "01"}`

Missing strings: `{"10", "11"}`

Lexicographically smallest missing: `"10"` (comes before "11")

![Example Visualization](../images/TRI-013/example-1.png)

## Notes

- Lexicographic order for binary strings: "00" < "01" < "10" < "11"
- If `n = 2^L`, all possible strings are present, return empty string
- Use a binary trie for efficient missing string detection
- DFS traversal in lexicographic order (explore '0' child before '1' child)

## Related Topics

Trie, Binary String, Lexicographic Order, DFS, Coding Theory

---

## Solution Template

### Java


### Python


### C++


### JavaScript

