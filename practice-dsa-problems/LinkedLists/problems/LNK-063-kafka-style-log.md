---
problem_id: LNK_KAFKA_STYLE_LOG__6088
display_id: NTB-LNK-6088
slug: kafka-style-log
title: "Kafka-Style Log"
difficulty: Medium
difficulty_score: 50
topics:
  - Linked Lists
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - kafka-style-log
  - linkedlists
  - memory-management
  - pointers
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Kafka-Style Log

## Problem Statement

The list is an append-only log of records `(key, value, time)`. Compaction keeps only the latest record per key.

Operations:

- `APPEND key value time`
- `COMPACT`: remove older records per key
- `READ offset`: output record at position `offset`, or `-1` if out of range

## Input Format

- First line: integer `q`
- Next `q` lines: operations

## Output Format

- For each `READ`, output `key value time` or `-1`

## Constraints

- `1 <= q <= 200000`
- Keys and values are 32-bit signed integers

## Clarifying Notes

- `offset` is 1-based.
- After compaction, order of remaining records is preserved.

## Example Input

```
5
APPEND 1 10 1
APPEND 1 20 2
COMPACT
READ 1
READ 2
```

## Example Output

```
1 20 2
-1
```
