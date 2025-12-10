# String Compressor

**Problem ID:** TP-005
**Display ID:** 70
**Question Name:** String Compressor
**Slug:** string-compressor
**Title:** String Compression
**Difficulty:** Medium
**Premium:** No
**Tags:** String, Two Pointers, In-place

---

**Copyright Notice:** © 2025 NTB DSA Platform. This problem and its description are original content. Unauthorized reproduction or distribution is prohibited.

---

## Problem Description

Given an array of characters, compress it in-place by replacing consecutive duplicate characters with the character followed by the count. The compressed string should be stored in the input array, and you must return the new length.

## A Simple Scenario (Daily Life Usage)

You're implementing a simple file compression algorithm for text files. Instead of storing "aaabbcccc", you save space by storing "a3b2c4". This is especially useful for large files with many repeated characters, like logs or data exports.

## Your Task

Write a function that compresses a character array in-place and returns the new length after compression. If the compressed version isn't smaller, keep the original.

## Why is it Important?

This problem teaches you:

- In-place string manipulation
- Two-pointer read-write technique
- Character counting and grouping
- Memory-efficient algorithms

## Examples

### Example 1:

**Input:** `chars = ["a","a","b","b","c","c","c"]`
**Output:** `6, chars = ["a","2","b","2","c","3"]`
**Explanation:** The groups are "aa", "bb", and "ccc", which compress to "a2b2c3".

### Example 2:

**Input:** `chars = ["a"]`
**Output:** `1, chars = ["a"]`
**Explanation:** Single character, no compression needed.

### Example 3:

**Input:** `chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]`
**Output:** `4, chars = ["a","b","1","2"]`
**Explanation:** "a" stays as is, "bbbbbbbbbbbb" (12 b's) becomes "b12".

## Constraints

- 1 <= chars.length <= 2000
- chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol
- If a group has length 1, don't add the count
- Must modify the input array in-place with O(1) extra space

## Asked by Companies


**Note:** Company names are for illustrative purposes and represent the types of organizations that use similar systems. They do not imply endorsement or partnership.


- Amazon
- Microsoft
- Google
- Adobe

---

**Disclaimer:** While this problem involves classic computer science algorithms and data structures that are part of common knowledge, all problem descriptions, scenarios, examples, and explanations are original content created specifically for this platform.
