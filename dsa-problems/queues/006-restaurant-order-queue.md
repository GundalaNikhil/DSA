# Restaurant Order Queue

**Problem ID:** QUE-006
**Display ID:** 29
**Question Name:** Restaurant Order Queue
**Slug:** restaurant-order-queue
**Title:** Design Hit Counter
**Difficulty:** Medium
**Premium:** Yes
**Tags:** Queue, Design, Sliding Window

---

**Copyright Notice:** © 2025 NTB DSA Platform. This problem and its description are original content. Unauthorized reproduction or distribution is prohibited.

---

## Problem Description

Design a hit counter which counts the number of hits received in the past 5 minutes (i.e., the past 300 seconds). Your system should accept a timestamp parameter (in seconds granularity), and you may assume that calls are being made to the system in chronological order. Several hits may arrive at the same timestamp.

## A Simple Scenario (Daily Life Usage)

You're managing a restaurant's online ordering dashboard. You want to display how many orders were placed in the last 5 minutes to help kitchen staff anticipate workload. Every time an order comes in, you record the timestamp and need to quickly show the count of recent orders (last 300 seconds). This helps restaurants adjust their staffing during peak times.

## Your Task

Implement the HitCounter class:

- `HitCounter()` - Initializes the object of the hit counter system
- `void hit(int timestamp)` - Records a hit that happened at timestamp (in seconds). Several hits may happen at the same timestamp
- `int getHits(int timestamp)` - Returns the number of hits in the past 5 minutes from timestamp (i.e., the past 300 seconds)

## Why is it Important?

This problem teaches you:

- Time-window based data structures
- Efficient outdated data cleanup
- Real-time analytics systems
- Space-time complexity tradeoffs

## Examples

### Example 1:

**Input:**
```
["HitCounter", "hit", "hit", "hit", "getHits", "hit", "getHits", "getHits"]
[[], [1], [2], [3], [4], [300], [300], [301]]
```

**Output:** `[null, null, null, null, 3, null, 4, 3]`

**Explanation:**
```
HitCounter counter = new HitCounter();
counter.hit(1);       // order at timestamp 1
counter.hit(2);       // order at timestamp 2
counter.hit(3);       // order at timestamp 3
counter.getHits(4);   // get orders in range [1,4], return 3
counter.hit(300);     // order at timestamp 300
counter.getHits(300); // get orders in range [1,300], return 4
counter.getHits(301); // get orders in range [2,301], return 3
                      // order at timestamp 1 is outside 5-minute window
```

### Example 2:

**Input:**
```
["HitCounter", "hit", "hit", "getHits", "hit", "getHits"]
[[], [1], [100], [200], [250], [300]]
```

**Output:** `[null, null, null, 2, null, 3]`

**Explanation:** All orders within 300-second window at timestamp 300.

### Example 3:

**Input:**
```
["HitCounter", "hit", "hit", "hit", "getHits"]
[[], [100], [200], [300], [350]]
```

**Output:** `[null, null, null, null, 3]`

**Explanation:** At timestamp 350, all orders from 100, 200, 300 are within the 5-minute window (past 300 seconds = [51, 350]).

## Constraints

- 1 ≤ timestamp ≤ 2 * 10^9
- All timestamps will be in chronological order (strictly increasing)
- At most 300 calls will be made to hit and getHits

## Follow-up

What if the number of hits per second could be huge? Does your design scale?

## Asked by Companies


**Note:** Company names are for illustrative purposes and represent the types of organizations that use similar systems. They do not imply endorsement or partnership.


- Uber Eats
- DoorDash
- Grubhub
- Postmates

---

**Disclaimer:** While this problem involves classic computer science algorithms and data structures that are part of common knowledge, all problem descriptions, scenarios, examples, and explanations are original content created specifically for this platform.
