---
problem_id: STC_SUFFIX_AUTOMATON_QUERIES__9036
display_id: STC-016
slug: suffix-automaton-queries
title: "Suffix Automaton Substring Queries"
difficulty: Medium
difficulty_score: 62
topics:
  - Strings
  - Suffix Automaton
  - Counting
tags:
  - strings
  - suffix-automaton
  - counting
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# STC-016: Suffix Automaton Substring Queries

## Problem Statement

Build a suffix automaton for a string `s`. For each query string `p`, output how many times `p` occurs as a substring of `s`.

If `p` is not a substring, output 0.

![Problem Illustration](../images/STC-016/problem-illustration.png)

## Input Format

- First line: string `s`
- Second line: integer `q`, number of queries
- Next `q` lines: a query string `p`

## Output Format

- Print `q` lines, each the occurrence count for the query

## Constraints

- `1 <= |s| <= 100000`
- `1 <= q <= 100000`
- Sum of query lengths `<= 200000`
- Strings contain lowercase English letters

## Example

**Input:**

```
ababa
2
aba
baa
```

**Output:**

```
2
0
```

**Explanation:**

"aba" occurs twice in "ababa" (positions 0 and 2). "baa" does not occur.

![Example Visualization](../images/STC-016/example-1.png)

## Notes

- After building the automaton, propagate end counts in order of state length.
- Each query is answered by walking transitions; the terminal state's count is the answer.
- Time complexity: O(|s| + total query length) after preprocessing.
- Use 64-bit integers for counts if needed.

## Related Topics

Suffix Automaton, Substring Queries, Counting

---

## Solution Template

### Java


### Python


### C++


### JavaScript

