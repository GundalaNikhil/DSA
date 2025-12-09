# Plagiarism Detector Lite

**Problem ID:** STR-004
**Display ID:** 9
**Question Name:** Plagiarism Detector Lite
**Slug:** plagiarism-detector-lite
**Title:** Find Longest Common Substring
**Difficulty:** Medium
**Premium:** No
**Tags:** String, Dynamic Programming

## Problem Description

Given two strings, find the length of their longest common substring (consecutive characters that appear in both).

## A Simple Scenario (Daily Life Usage)

You're a teacher checking if two student essays are too similar. If Essay A has "the quick brown fox" and Essay B has "a quick brown cat", the longest matching part is "quick brown " (12 characters). This helps detect if students copied from each other.

## Your Task

Return the length of the longest substring that appears in both strings.

## Why is it Important?

This problem teaches you:

- Dynamic programming fundamentals
- String matching algorithms
- Table-based optimization
- Plagiarism detection basics

## Examples

### Example 1:

**Input:**

```
text1 = "abcdefgh"
text2 = "xyzabcpqr"
```

**Output:** `3`
**Explanation:** "abc" is the longest common substring.

### Example 2:

**Input:**

```
text1 = "helloworld"
text2 = "worldhello"
```

**Output:** `5`
**Explanation:** "world" or "hello" both have length 5.

### Example 3:

**Input:**

```
text1 = "programming"
text2 = "gaming"
```

**Output:** `6`
**Explanation:** "gaming" appears in both.

## Constraints

- 1 ≤ text1.length, text2.length ≤ 500
- Strings contain only lowercase English letters
- Return 0 if no common substring exists

## Asked by Companies

- Turnitin
- Grammarly
- Copyscape
- Scribbr
