---
problem_id: STC_AHO_CORASICK_COOLDOWN__1658
display_id: STC-015
slug: aho-corasick-cooldown-scoring
title: "Aho-Corasick With Cooldown Scoring"
difficulty: Medium
difficulty_score: 60
topics:
  - Strings
  - Aho-Corasick
  - Dynamic Programming
tags:
  - strings
  - aho-corasick
  - dp
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# STC-015: Aho-Corasick With Cooldown Scoring

## Problem Statement

You are given `k` patterns, each with an integer score, and a text `t`. While scanning `t`, you may choose a subset of pattern occurrences to collect their scores.

If you choose an occurrence that ends at position `r`, then the next chosen occurrence must start at position `>= r + G + 1` (a cooldown of `G` characters after the end).

Return the maximum total score you can collect.

![Problem Illustration](../images/STC-015/problem-illustration.png)

## Input Format

- First line: integer `k`
- Next `k` lines: a pattern string `p_i` and an integer score `w_i`
- Next line: integer `G`
- Last line: text string `t`

## Output Format

- Single integer: maximum total score

## Constraints

- `1 <= k <= 100000`
- `1 <= |t| <= 200000`
- Sum of pattern lengths `<= 200000`
- `0 <= w_i <= 1000000`
- `0 <= G <= 1000`
- All strings contain lowercase English letters

## Example

**Input:**

```
2
ab 5
b 2
1
abb
```

**Output:**

```
5
```

**Explanation:**

Matches are "ab" at [1,2] with score 5 and "b" at [2,2] and [3,3] with score 2. Taking "ab" ends at 2, and cooldown `G=1` blocks any chosen match starting at 3, so the best total is 5.

![Example Visualization](../images/STC-015/example-1.png)

## Notes

- Use Aho-Corasick to list all occurrences (end index, start index, score).
- Sort or bucket occurrences by end index for DP transitions.
- This is weighted interval scheduling with a cooldown gap.
- Use 64-bit integers for the DP values.

## Related Topics

Aho-Corasick, Pattern Matching, Dynamic Programming

---

## Solution Template

### Java


### Python


### C++


### JavaScript

