# Cache System Design

**Problem ID:** HASH-005
**Display ID:** 40
**Question Name:** Cache System Design
**Slug:** cache-system-design
**Title:** LRU Cache
**Difficulty:** Medium
**Premium:** Yes
**Tags:** Hash Table, Linked List, Design, Doubly-Linked List

---

**Copyright Notice:** © 2025 NTB DSA Platform. This problem and its description are original content. Unauthorized reproduction or distribution is prohibited.

---

## Problem Description

Design a data structure that follows the Least Recently Used (LRU) cache eviction policy. The cache should support get and put operations in O(1) time complexity.

## A Simple Scenario (Daily Life Usage)

You're building a web browser's page caching system. When users visit websites, you want to keep recently viewed pages in memory for instant back-button navigation. However, memory is limited - when the cache is full and a new page is visited, you need to evict the page that was accessed longest ago. This keeps frequently accessed pages fast while managing memory efficiently.

## Your Task

Implement an LRUCache class with the following methods:
- `LRUCache(capacity)`: Initialize the cache with a positive capacity
- `get(key)`: Return the value of the key if it exists, otherwise return -1. Mark the key as recently used.
- `put(key, value)`: Update the value if the key exists, otherwise add the key-value pair. If capacity is exceeded, evict the least recently used item before inserting.

## Why is it Important?

This problem teaches you:

- Advanced data structure combination (hash map + doubly linked list)
- LRU eviction policy implementation
- O(1) time complexity optimization techniques
- Real-world caching strategies used by browsers and databases

## Examples

### Example 1:

**Input:**
```
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
```
**Output:**
```
[null, null, null, 1, null, -1, null, -1, 3, 4]
```
**Explanation:**
- LRUCache(2): capacity = 2
- put(1, 1): cache = {1=1}
- put(2, 2): cache = {1=1, 2=2}
- get(1): returns 1, cache = {2=2, 1=1} (1 is now most recent)
- put(3, 3): evicts key 2, cache = {1=1, 3=3}
- get(2): returns -1 (not found)
- put(4, 4): evicts key 1, cache = {3=3, 4=4}
- get(1): returns -1 (not found)
- get(3): returns 3
- get(4): returns 4

## Constraints

- 1 ≤ capacity ≤ 3000
- 0 ≤ key ≤ 10,000
- 0 ≤ value ≤ 100,000
- At most 200,000 calls will be made to get and put
- Both operations must be O(1) average time complexity

## Asked by Companies


**Note:** Company names are for illustrative purposes and represent the types of organizations that use similar systems. They do not imply endorsement or partnership.


- Google
- Amazon
- Microsoft
- Facebook

---

**Disclaimer:** While this problem involves classic computer science algorithms and data structures that are part of common knowledge, all problem descriptions, scenarios, examples, and explanations are original content created specifically for this platform.
