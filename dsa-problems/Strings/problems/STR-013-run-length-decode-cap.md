---
problem_id: STR_RUN_LENGTH_DECODE_CAP__1013
display_id: STR-013
slug: run-length-decode-cap
title: "Run-Length Decode with Cap"
difficulty: Easy-Medium
difficulty_score: 30
topics:
  - String Manipulation
  - Encoding
  - Parsing
tags:
  - run-length-decoding
  - capping
  - string-parsing
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# STR-013: Run-Length Decode with Cap

## Problem Statement

Given a run-length encoded string (format: "char+count") and an integer `cap`, decode the string but limit any run exceeding `cap` to exactly `cap` occurrences.

## Input Format

- First line: Encoded string `s` (1 ≤ |s| ≤ 10^5)
- Second line: Integer `cap` (1 ≤ cap ≤ 10^4)

## Output Format

- A single string representing the decoded result

## Constraints

- `1 ≤ |s| ≤ 10^5`
- `1 ≤ cap ≤ 10^4`
- Encoded format: character followed by count (digits)

## Example 1

**Input:**

```
a10b2
3
```

**Output:**

```
aaabb
```

**Explanation:**

- "a10" → "aaa" (capped from 10 to 3)
- "b2" → "bb" (no cap needed)

## Example 2

**Input:**

```
x100y50
5
```

**Output:**

```
xxxxxyyyyy
```

**Explanation:**

- Both runs capped to 5

## Notes

- Parse character and following digits
- Apply min(count, cap) for each run
- O(n + output_size) time complexity
