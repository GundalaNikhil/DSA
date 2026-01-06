---
problem_id: TRI_LONGEST_DICTIONARY_CHAIN_SUFFIX_VALIDATED__2116
display_id: NTB-TRI-2116
slug: longest-dictionary-chain-suffix-validated
title: "Longest Dictionary Chain with Suffix Validation"
difficulty: Medium
difficulty_score: 50
topics:
  - Tries
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - efficient-search
  - longest-dictionary-chain-suffix-validated
  - prefix-trees
  - technical-interview-prep
  - tries
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Longest Dictionary Chain with Suffix Validation

## Problem Statement

You are given a dictionary `D` of words and a set `S` of valid suffix roots. A dictionary word `w` is **suffix-valid** if every suffix of `w` is contained in `S`.

A **chain** is a sequence of dictionary words `w1, w2, ..., wk` such that:

- Each `wi` is suffix-valid.
- For every `i > 1`, `wi` is formed by appending exactly one character to the end of `w(i-1)`.

Your task is to find the maximum possible chain length.

## Input Format

- First line: integers `n` and `m`
- Next `n` lines: dictionary words
- Next `m` lines: suffix root words

## Output Format

- Single integer: maximum chain length

## Constraints

- `1 <= n, m <= 200000`
- `1 <= word length <= 50`
- All words contain only lowercase English letters

## Clarifying Notes

- A suffix of `w` is any string `w[j..end]` for `1 <= j <= |w|`.
- A word can be in the chain only if **all** of its suffixes exist in `S`.
- The intended approach uses one trie for dictionary traversal and one trie for suffix validation.

## Example Input

```
5 10
a
ab
abc
abcd
bcd
a
b
c
d
ab
bc
cd
abc
bcd
abcd
```

## Example Output

```
4
```
