---
problem_id: STR_BOUNDED_RUN_ENCODING__1535
display_id: NTB-STR-1535
slug: bounded-run-encoding
title: "Bounded Run Encoding"
difficulty: Medium
difficulty_score: 50
topics:
  - Strings
tags:
  - algorithms
  - bounded-run-encoding
  - coding-interviews
  - data-structures
  - pattern-matching
  - string-manipulation
  - strings
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Bounded Run Encoding

## Problem Statement

Compress a string by encoding each maximal run of identical characters as `<char><count>`, but split runs into chunks of at most 9. For example, a run of length 12 becomes `a9a3`.

## Input Format

- Single line: string `s`

## Output Format

- The encoded string

## Constraints

- `1 <= |s| <= 200000`
- `s` contains printable ASCII characters

## Clarifying Notes

- Every run is encoded with an explicit count, even when the count is 1.

## Example Input

```
aaaaaaaaaaaabbb
```

## Example Output

```
a9a3b3
```
