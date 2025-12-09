# Prefix and Suffix Search

**Problem ID:** TRIE-005
**Display ID:** 94
**Question Name:** Prefix and Suffix Search
**Slug:** word-filter-search
**Title:** Prefix and Suffix Search
**Difficulty:** Hard
**Premium:** Yes
**Tags:** Trie, String, Design, Hash Table

## Problem Description

Design a special dictionary that allows you to search for words using both a prefix and a suffix simultaneously. Given multiple matching words, return the one with the largest weight (index). This enables advanced filtering where you need to match both the beginning and ending of words.

## A Simple Scenario (Daily Life Usage)

You're building an advanced file search feature for Dropbox or Google Drive. Users want to find files like "project_report_2024.pdf" by searching for files that start with "project" AND end with "2024.pdf". Or imagine searching code files: you want to find functions that start with "get" and end with "Service" (like "getUserService", "getPaymentService"). This two-way matching makes search much more powerful than simple prefix matching.

## Your Task

Implement the `WordFilter` class:

- `WordFilter(words)`: Initialize the system with a list of words. Each word has a weight equal to its index in the array.
- `search(prefix, suffix)`: Return the largest weight of a word that has both the given prefix and suffix. If no word matches both conditions, return -1.

## Why is it Important?

This problem teaches you:

- Advanced trie techniques combining prefix and suffix trees
- Efficient dual-constraint searching
- Weight/priority tracking in data structures
- Complex string matching algorithms used in search engines

## Examples

### Example 1:

**Input:**
```
["WordFilter", "search", "search", "search"]
[[["apple", "application", "apply", "append"]], ["app", "le"], ["app", "ly"], ["app", "end"]]
```
**Output:**
```
[null, 0, 2, 3]
```
**Explanation:**
- Initialize with 4 words: apple(0), application(1), apply(2), append(3)
- search("app", "le") → "apple" matches (starts with "app", ends with "le") → weight 0
- search("app", "ly") → "apply" matches → weight 2
- search("app", "end") → "append" matches → weight 3

### Example 2:

**Input:**
```
["WordFilter", "search", "search", "search"]
[[["hello", "help", "helpful", "shell"]], ["hel", "l"], ["hel", "ul"], ["sh", "ll"]]
```
**Output:**
```
[null, 2, 2, 3]
```
**Explanation:**
- hello(0), help(1), helpful(2), shell(3)
- search("hel", "l") → both "helpful" and "shell" end with "l", but only "helpful" starts with "hel" → weight 2
- search("hel", "ul") → "helpful" matches → weight 2
- search("sh", "ll") → "shell" matches → weight 3

### Example 3:

**Input:**
```
["WordFilter", "search", "search"]
[[["code", "decode", "encode", "unicode"]], ["code", "de"], ["", "code"]]
```
**Output:**
```
[null, 2, 3]
```
**Explanation:**
- code(0), decode(1), encode(2), unicode(3)
- search("code", "de") → "encode" starts with "" (prefix of everything) but we want "code" prefix. Only "encode" works (actually starts with "e" not "code"), wait - let me reconsider: "decode" starts with "de" not "code", "encode" starts with "en" not "code". Actually no words match. Let me fix:
- search("code", "de") → "encode" matches (starts with "", ends with "de") - wait, "encode" ends with "e" not "de". Let me reconsider: prefix="code" means starts with "code". Only "code" itself starts with "code", and it ends with "code" not "de". So answer is actually encode(2) if it starts with "" not "code". I need to fix this example.

Let me provide a corrected example:

**Input:**
```
["WordFilter", "search", "search", "search"]
[[["getUser", "getUserData", "getProduct", "updateUser"]], ["get", "er"], ["get", "Data"], ["up", "User"]]
```
**Output:**
```
[null, 0, 1, 3]
```
**Explanation:**
- getUser(0), getUserData(1), getProduct(2), updateUser(3)
- search("get", "er") → "getUser" matches → weight 0
- search("get", "Data") → "getUserData" matches → weight 1
- search("up", "User") → "updateUser" matches → weight 3

## Constraints

- 1 <= words.length <= 10,000
- 1 <= words[i].length <= 10
- words[i] consists of lowercase English letters
- 1 <= prefix.length, suffix.length <= 10
- prefix and suffix consist of lowercase English letters
- At most 10,000 calls will be made to search
- Searching should be done in O(L) time where L is the length of the word

## Asked by Companies

- Elasticsearch
- Algolia
- Google
- Microsoft
