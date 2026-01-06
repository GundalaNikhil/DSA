---
problem_id: STR_PERSISTENT_STRING_EDITOR__2047
display_id: NTB-STR-2047
slug: persistent-string-editor
title: "Persistent String Editor"
difficulty: Medium
difficulty_score: 50
topics:
  - Strings
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - pattern-matching
  - persistent-string-editor
  - string-manipulation
  - strings
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Persistent String Editor

## Problem Statement

You are given an initial string `s` (version 0). Each edit creates a new version.

Operations:

- `INS v pos c`: create a new version by inserting character `c` into version `v` at position `pos` (1-based, before the current character at `pos`; if `pos = length+1`, append).
- `DEL v pos`: create a new version by deleting the character at position `pos` in version `v`.
- `GET v pos`: output the character at position `pos` in version `v`, or `-1` if out of range.

Versions created by `INS` or `DEL` are numbered 1, 2, 3, ... in the order the operations appear.

## Input Format

- First line: string `s`
- Second line: integer `q`
- Next `q` lines: one operation per line

## Output Format

- For each `GET`, output the character or `-1` on its own line

## Constraints

- `1 <= |s| <= 200000`
- `1 <= q <= 200000`
- Total length across all versions <= 400000
- Strings contain only lowercase English letters

## Clarifying Notes

- All indices are 1-based.
- The intended solution uses a persistent rope or persistent treap.

## Example Input

```
abc
4
INS 0 2 x
GET 1 2
DEL 1 3
GET 2 3
```

## Example Output

```
x
c
```
