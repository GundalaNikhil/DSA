# Word Break Dictionary

**Problem ID:** DP-005
**Display ID:** 46
**Question Name:** Word Break Dictionary
**Slug:** word-break-dictionary
**Title:** Word Break
**Difficulty:** Medium
**Premium:** No
**Tags:** Dynamic Programming, String, Hash Table, Trie, Memoization

## Problem Description

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

## A Simple Scenario (Daily Life Usage)

Imagine you're building a spell-checker or autocorrect system. Sometimes people type words without spaces (like "iloveprogramming"). You need to figure out if this can be broken into valid dictionary words: "i love programming" or "i love program ming". Your dictionary contains words like ["i", "love", "programming"]. This helps text editors and messaging apps understand and correct user input!

## Your Task

Write a function that takes a string and a dictionary of words, then determines whether the string can be completely segmented into dictionary words. Words can be reused multiple times.

## Why is it Important?

This problem teaches you how to:

- Apply dynamic programming to string problems
- Use memoization to avoid redundant computations
- Break down strings into valid components
- Understand overlapping subproblems
- Optimize substring matching algorithms

## Examples

### Example 1:

**Input:** `s = "leetcode", wordDict = ["leet", "code"]`
**Output:** `true`
**Explanation:** Return true because "leetcode" can be segmented as "leet code".

### Example 2:

**Input:** `s = "applepenapple", wordDict = ["apple", "pen"]`
**Output:** `true`
**Explanation:** Return true because "applepenapple" can be segmented as "apple pen apple". Note that you are allowed to reuse a dictionary word.

### Example 3:

**Input:** `s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]`
**Output:** `false`
**Explanation:** There is no way to segment "catsandog" into valid dictionary words.

### Example 4:

**Input:** `s = "cars", wordDict = ["car", "ca", "rs"]`
**Output:** `true`
**Explanation:** Return true because "cars" can be segmented as "car s" or "ca rs".

## Constraints

- 1 ≤ s.length ≤ 300
- 1 ≤ wordDict.length ≤ 1000
- 1 ≤ wordDict[i].length ≤ 20
- s and wordDict[i] consist of only lowercase English letters
- All the strings of wordDict are unique

## Asked by Companies

- Google
- Amazon
- Facebook
- Microsoft
