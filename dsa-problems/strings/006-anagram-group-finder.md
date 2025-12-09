# Anagram Group Finder

**Problem ID:** STR-006
**Display ID:** 11
**Question Name:** Anagram Group Finder
**Slug:** anagram-group-finder
**Title:** Check if Two Strings are Anagrams
**Difficulty:** Easy
**Premium:** No
**Tags:** String, Hash Table, Sorting

## Problem Description

Determine if two strings are anagrams of each other (contain the same characters with the same frequencies, ignoring spaces and case).

## A Simple Scenario (Daily Life Usage)

You're playing word games like Scrabble. You have letters "LISTEN" and wonder if you can rearrange them to spell "SILENT". Since both use the same letters (L, I, S, T, E, N), they're anagrams! This helps you find all possible words from your letter tiles.

## Your Task

Return true if the strings are anagrams, false otherwise. Ignore spaces and capitalization.

## Why is it Important?

This problem teaches you:

- Character frequency counting
- Hash map applications
- String comparison techniques
- Case-insensitive processing

## Examples

### Example 1:

**Input:**

```
s1 = "listen"
s2 = "silent"
```

**Output:** `true`
**Explanation:** Both contain: l(1), i(1), s(1), t(1), e(1), n(1).

### Example 2:

**Input:**

```
s1 = "Hello"
s2 = "Olelh"
```

**Output:** `true`
**Explanation:** Case-insensitive comparison shows they're anagrams.

### Example 3:

**Input:**

```
s1 = "race car"
s2 = "care car"
```

**Output:** `true`
**Explanation:** Ignoring spaces, both have: a(2), c(2), e(1), r(2).

## Constraints

- 1 ≤ s1.length, s2.length ≤ 1000
- Strings contain only letters and spaces
- Comparison is case-insensitive

## Asked by Companies

- Zynga
- Wordle
- Scrabble GO
- Words With Friends
