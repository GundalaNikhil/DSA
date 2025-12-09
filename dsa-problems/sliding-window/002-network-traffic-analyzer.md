# Network Traffic Analyzer

**Problem ID:** SW-002
**Display ID:** 73
**Question Name:** Network Traffic Analyzer
**Slug:** network-traffic-analyzer
**Title:** Longest Substring Without Repeating Characters
**Difficulty:** Medium
**Premium:** No
**Tags:** Sliding Window, Hash Table, String

## Problem Description

You are given a string representing network packet IDs. Find the length of the longest substring where all packet IDs (characters) are unique, representing the maximum transmission window without packet duplication.

## A Simple Scenario (Daily Life Usage)

Imagine you're monitoring network traffic for Amazon's servers. Each character represents a packet ID, and you need to find the longest sequence of packets without any duplicates to optimize the transmission window. For example, in "abcabcbb", the longest unique sequence is "abc" with length 3, which tells you the optimal window size for this connection.

## Your Task

Write a function that takes a string of packet IDs and returns the length of the longest substring without repeating characters.

## Why is it Important?

This problem teaches you:

- Variable-size sliding window technique
- Hash table for tracking seen elements
- Optimizing network transmission protocols
- Real-time data stream analysis

## Examples

### Example 1:

**Input:** `packets = "abcabcbb"`
**Output:** `3`
**Explanation:** The longest substring without repeating characters is "abc", with length 3.

### Example 2:

**Input:** `packets = "bbbbb"`
**Output:** `1`
**Explanation:** The longest substring is "b", with length 1.

### Example 3:

**Input:** `packets = "pwwkew"`
**Output:** `3`
**Explanation:** The longest substring is "wke", with length 3. Note that "pwke" is not valid because it's not a substring.

### Example 4:

**Input:** `packets = ""`
**Output:** `0`
**Explanation:** Empty string has no characters.

## Constraints

- 0 <= packets.length <= 5 * 10^4
- packets consists of English letters, digits, symbols, and spaces
- Each character represents a unique packet ID

## Asked by Companies

- Amazon
- Google
- Microsoft
- Facebook
