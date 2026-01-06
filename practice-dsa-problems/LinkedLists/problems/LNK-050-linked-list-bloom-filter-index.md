---
problem_id: LNK_LINKED_LIST_BLOOM_FILTER_INDEX__6425
display_id: NTB-LNK-6425
slug: linked-list-bloom-filter-index
title: "Linked List with Bloom Filter Index"
difficulty: Medium
difficulty_score: 50
topics:
  - Linked Lists
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - linked-list-bloom-filter-index
  - linkedlists
  - memory-management
  - pointers
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Linked List with Bloom Filter Index

## Problem Statement

You are given a linked list and a Bloom filter configuration with `k` hash functions. For each query value `x`, the Bloom filter reports whether `x` may be present. If the filter reports present, you must verify by traversing the list.

Output whether `x` is truly present, and count how many false positives occur.

Hash function `i` is:

```
h_i(x) = (a_i * x + b_i) mod M
```

The Bloom filter bitset is given as a binary string of length `M`.

## Input Format

- First line: integers `n`, `k`, `M`
- Second line: `n` integers: list values
- Third line: binary string of length `M`
- Next `k` lines: `a_i b_i`
- Next line: integer `q`
- Next `q` lines: query values `x`

## Output Format

- For each query, output `true` or `false`
- Last line: total number of false positives

## Constraints

- `1 <= n, q <= 200000`
- `1 <= k <= 10`
- `1 <= M <= 200000`
- Values are 32-bit signed integers

## Clarifying Notes

- A false positive occurs when the Bloom filter reports present but the value is not in the list.

## Example Input

```
3 2 10
1 5 9
1000100001
1 0
2 1
3
5
7
9
```

## Example Output

```
true
false
true
1
```
