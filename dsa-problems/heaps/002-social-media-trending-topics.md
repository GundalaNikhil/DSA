# Social Media Trending Topics

**Problem ID:** HEAP-002
**Display ID:** 85
**Question Name:** Social Media Trending Topics
**Slug:** social-media-trending-topics
**Title:** Top K Trending Hashtags
**Difficulty:** Medium
**Premium:** No
**Tags:** Heap, Hash Table, Counting, Priority Queue

---

**Copyright Notice:** © 2025 NTB DSA Platform. This problem and its description are original content. Unauthorized reproduction or distribution is prohibited.

---

## Problem Description

You are developing a trending topics feature for a social media platform. Given a stream of hashtags used in posts over the last hour, find the K most frequently used hashtags. If two hashtags have the same frequency, return them in lexicographical (alphabetical) order.

## A Simple Scenario (Daily Life Usage)

Think about Twitter's trending section. When millions of users tweet with hashtags like #WorldCup, #Election2024, or #NewMovie, the platform needs to quickly identify which topics are trending right now. If #WorldCup appears 50,000 times and #Sports appears 45,000 times in the last hour, #WorldCup should rank higher. This helps users discover what's popular in real-time.

## Your Task

Write a function that takes an array of hashtags (strings) and an integer K, then returns the K most frequent hashtags. Each hashtag appears one or more times in the array.

Return the answer sorted by frequency from highest to lowest. If two hashtags have the same frequency, sort them alphabetically.

## Why is it Important?

This problem teaches you:

- Combining hash tables with min heaps for efficient counting
- Building a top-K frequency algorithm
- Handling tie-breaking with secondary sorting criteria
- Optimizing for streaming data scenarios
- Trade-offs between time and space complexity

## Examples

### Example 1:

**Input:**
```
hashtags = ["#food", "#travel", "#food", "#tech", "#travel", "#food", "#music"]
k = 2
```

**Output:** `["#food", "#travel"]`

**Explanation:**
- #food appears 3 times
- #travel appears 2 times
- #tech appears 1 time
- #music appears 1 time
Top 2 are #food and #travel.

### Example 2:

**Input:**
```
hashtags = ["#python", "#javascript", "#python", "#java", "#javascript", "#python"]
k = 3
```

**Output:** `["#python", "#javascript", "#java"]`

**Explanation:**
- #python: 3 times
- #javascript: 2 times
- #java: 1 time

### Example 3:

**Input:**
```
hashtags = ["#art", "#design", "#fashion", "#art", "#design", "#art"]
k = 2
```

**Output:** `["#art", "#design"]`

**Explanation:**
- #art: 3 times
- #design: 2 times
- #fashion: 1 time

### Example 4:

**Input:**
```
hashtags = ["#cats", "#dogs", "#birds", "#fish"]
k = 2
```

**Output:** `["#birds", "#cats"]`

**Explanation:** All hashtags appear once. With equal frequency, we sort alphabetically and take first 2: #birds, #cats (alphabetically before #dogs and #fish).

## Constraints

- 1 ≤ hashtags.length ≤ 10^5
- 1 ≤ k ≤ number of unique hashtags
- hashtags[i] consists of lowercase letters and the '#' symbol
- 2 ≤ hashtags[i].length ≤ 50
- All hashtags start with '#'

## Asked by Companies


**Note:** Company names are for illustrative purposes and represent the types of organizations that use similar systems. They do not imply endorsement or partnership.


- Twitter
- Instagram
- TikTok
- Reddit

---

**Disclaimer:** While this problem involves classic computer science algorithms and data structures that are part of common knowledge, all problem descriptions, scenarios, examples, and explanations are original content created specifically for this platform.
