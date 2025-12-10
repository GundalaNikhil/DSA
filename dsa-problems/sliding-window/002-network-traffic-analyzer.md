# Network Traffic Analyzer

**Problem ID:** SW-002
**Display ID:** 73
**Question Name:** Network Traffic Analyzer
**Slug:** network-traffic-analyzer
**Title:** Longest Substring Without Repeating Characters
**Difficulty:** Medium
**Premium:** No
**Tags:** Sliding Window, Hash Table, String

---

**Copyright Notice:** © 2025 NTB DSA Platform. This problem and its description are original content. Unauthorized reproduction or distribution is prohibited.

---

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

**Input:** `packets = "p1p2p3p1p4p5"`
**Output:** `6`
**Explanation:** The longest substring without repeating packets is "p2p3p1p4p5", with length 6.

### Example 2:

**Input:** `packets = "aaaaaaa"`
**Output:** `1`
**Explanation:** All packets are duplicates, so longest unique sequence is "a", with length 1.

### Example 3:

**Input:** `packets = "netw0rkpacket"`
**Output:** `10`
**Explanation:** The longest substring is "tw0rkpace" or "w0rkpacket", with length 10.

### Example 4:

**Input:** `packets = ""`
**Output:** `0`
**Explanation:** Empty string has no packets to analyze.

## Constraints

- 0 <= packets.length <= 5 * 10^4
- packets consists of English letters, digits, symbols, and spaces
- Each character represents a unique packet ID

## Asked by Companies


**Note:** Company names are for illustrative purposes and represent the types of organizations that use similar systems. They do not imply endorsement or partnership.


- Amazon
- Google
- Microsoft
- Facebook

---

**Disclaimer:** While this problem involves classic computer science algorithms and data structures that are part of common knowledge, all problem descriptions, scenarios, examples, and explanations are original content created specifically for this platform.
