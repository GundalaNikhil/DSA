# Search Autocomplete System

**Problem ID:** TRIE-001
**Display ID:** 90
**Question Name:** Search Autocomplete System
**Slug:** autocomplete-search-engine
**Title:** Search Autocomplete System
**Difficulty:** Medium
**Premium:** No
**Tags:** Trie, Design, String, Data Stream

---

**Copyright Notice:** © 2025 NTB DSA Platform. This problem and its description are original content. Unauthorized reproduction or distribution is prohibited.

---

## Problem Description

Design a search autocomplete system that suggests the top 3 most frequently searched queries that start with a given prefix. The system should track search history and update frequencies in real-time.

## A Simple Scenario (Daily Life Usage)

You're building the search bar for an e-commerce website like Amazon. When users type "lap", they should immediately see suggestions like "laptop", "laptop charger", and "laptop bag" based on what other customers frequently search for. This helps users find products faster and improves the shopping experience. The more a term is searched, the higher it should rank in suggestions.

## Your Task

Implement the `AutocompleteSystem` class:

- `AutocompleteSystem(sentences, times)`: Initialize with historical search data where `sentences[i]` was searched `times[i]` times
- `input(c)`:
  - If `c` is a character, add it to the current search query and return the top 3 suggestions
  - If `c` is '#', save the current query to history (increment its frequency by 1) and reset the search
  - Return an empty list if no matching suggestions exist

Top 3 ranking rules:
1. Higher frequency comes first
2. If frequencies are equal, lexicographically smaller sentence comes first

## Why is it Important?

This problem teaches you:

- Implementing trie data structure for efficient prefix matching
- Combining trie with frequency tracking
- Real-time query suggestion algorithms
- Handling streaming input for interactive systems

## Examples

### Example 1:

**Input:**
```
["AutocompleteSystem", "input", "input", "input", "input"]
[[["laptop", "laptop charger", "laptop bag", "phone", "phone case"], [5, 3, 2, 8, 4]], ["l"], ["a"], ["p"], ["#"]]
```
**Output:**
```
[null, ["laptop", "laptop charger", "laptop bag"], ["laptop", "laptop charger", "laptop bag"], ["laptop", "laptop charger", "laptop bag"], []]
```
**Explanation:**
- Initialize with search history
- "l" matches: laptop(5), laptop charger(3), laptop bag(2)
- "la" still matches same three items
- "lap" still matches same three items
- "#" saves "lap" as a new search and resets

### Example 2:

**Input:**
```
["AutocompleteSystem", "input", "input", "input", "input", "input"]
[[["coffee", "coffee maker", "tea"], [10, 5, 3]], ["c"], ["o"], ["f"], ["f"], ["#"]]
```
**Output:**
```
[null, ["coffee", "coffee maker"], ["coffee", "coffee maker"], ["coffee", "coffee maker"], ["coffee", "coffee maker"], []]
```
**Explanation:**
- "c" matches: coffee(10), coffee maker(5)
- "co" matches: coffee(10), coffee maker(5)
- "cof" matches: coffee(10), coffee maker(5)
- "coff" matches: coffee(10), coffee maker(5)
- "#" saves "coff" with frequency 1

## Constraints

- 1 <= sentences.length <= 100
- 1 <= sentences[i].length <= 100
- 1 <= times[i] <= 50
- `c` is a lowercase English letter, space ' ', or '#'
- sentences[i] consists of lowercase English letters and spaces
- At most 5000 calls will be made to `input`

## Asked by Companies


**Note:** Company names are for illustrative purposes and represent the types of organizations that use similar systems. They do not imply endorsement or partnership.


- Google
- Bing
- DuckDuckGo
- Amazon

---

**Disclaimer:** While this problem involves classic computer science algorithms and data structures that are part of common knowledge, all problem descriptions, scenarios, examples, and explanations are original content created specifically for this platform.
