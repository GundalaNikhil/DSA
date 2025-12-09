# Movie Theater Seat Reservation

**Problem ID:** QUE-004
**Display ID:** 27
**Question Name:** Movie Theater Seat Reservation
**Slug:** movie-theater-seat-reservation
**Title:** First Unique Character in Stream
**Difficulty:** Medium
**Premium:** No
**Tags:** Queue, Hash Table, Design

## Problem Description

Given a stream of characters, find the first non-repeating character from the stream at any point in time. You need to implement a class that can add characters to the stream and return the first unique character efficiently.

## A Simple Scenario (Daily Life Usage)

You're managing a movie theater's seat reservation system. Customers request seats by letter (A, B, C, etc.). You need to quickly identify the first available seat that hasn't been requested multiple times. As new requests come in, some seats become popular (requested multiple times) and should be skipped when finding the next unique available seat.

## Your Task

Implement the FirstUnique class:

- `FirstUnique(int[] nums)` - Initializes the object with the stream of numbers
- `int showFirstUnique()` - Returns the value of the first unique integer in the stream. If there is no unique integer, return -1
- `void add(int value)` - Adds an integer to the stream

## Why is it Important?

This problem teaches you:

- Queue and hash map combination
- Stream processing techniques
- Efficient duplicate tracking
- Real-time data structure updates

## Examples

### Example 1:

**Input:**
```
["FirstUnique", "showFirstUnique", "add", "showFirstUnique", "add", "add", "showFirstUnique"]
[[[2,3,5]], [], [5], [], [2], [3], []]
```

**Output:** `[null, 2, null, 2, null, null, -1]`

**Explanation:**
```
FirstUnique firstUnique = new FirstUnique([2,3,5]);
firstUnique.showFirstUnique(); // return 2 (seats: 2 unique, 3 unique, 5 unique)
firstUnique.add(5);            // seats: 2 unique, 3 unique, 5 duplicate
firstUnique.showFirstUnique(); // return 2
firstUnique.add(2);            // seats: 2 duplicate, 3 unique, 5 duplicate
firstUnique.add(3);            // seats: 2 duplicate, 3 duplicate, 5 duplicate
firstUnique.showFirstUnique(); // return -1 (no unique seats available)
```

### Example 2:

**Input:**
```
["FirstUnique", "showFirstUnique", "add", "add", "add", "showFirstUnique"]
[[[7,7,7,7,7,7]], [], [7], [3], [3], []]
```

**Output:** `[null, -1, null, null, null, -1]`

**Explanation:** Seat 7 is always duplicated, seats 3 added twice, no unique seats available.

### Example 3:

**Input:**
```
["FirstUnique", "showFirstUnique", "add", "showFirstUnique"]
[[[809]], [], [809], []]
```

**Output:** `[null, 809, null, -1]`

**Explanation:** Initially seat 809 is unique, after second request it becomes duplicate.

## Constraints

- 1 ≤ nums.length ≤ 10^5
- 1 ≤ nums[i] ≤ 10^8
- 1 ≤ value ≤ 10^8
- At most 50000 calls will be made to showFirstUnique and add

## Asked by Companies

- AMC Theatres
- Regal Cinemas
- Cinemark
- IMAX
