# Grocery Store Checkout

**Problem ID:** QUE-003
**Display ID:** 26
**Question Name:** Grocery Store Checkout
**Slug:** grocery-store-checkout
**Title:** Number of Recent Calls
**Difficulty:** Easy
**Premium:** No
**Tags:** Queue, Sliding Window, Design

---

**Copyright Notice:** © 2025 NTB DSA Platform. This problem and its description are original content. Unauthorized reproduction or distribution is prohibited.

---

## Problem Description

You have a RecentCounter class which counts the number of recent requests within a certain time frame. Implement the RecentCounter class with a method that returns the number of requests that have happened in the past 3000 milliseconds (including the new request).

## A Simple Scenario (Daily Life Usage)

You're managing a grocery store's self-checkout system. You want to track how many customers have checked out in the last 3 seconds to monitor traffic patterns. Every time a customer checks out, you record the timestamp and count how many checkouts happened in the previous 3 seconds. This helps you decide whether to open more checkout lanes during rush hours.

## Your Task

Implement the RecentCounter class:

- `RecentCounter()` - Initializes the counter with zero recent requests
- `int ping(int t)` - Adds a new request at time t (in milliseconds) and returns the number of requests that have happened in the past 3000 milliseconds (including the new request). It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.

## Why is it Important?

This problem teaches you:

- Sliding window technique with queue
- Time-based data filtering
- Efficient outdated data removal
- Real-time analytics fundamentals

## Examples

### Example 1:

**Input:**
```
["RecentCounter", "ping", "ping", "ping", "ping"]
[[], [1], [100], [3001], [3002]]
```

**Output:** `[null, 1, 2, 3, 3]`

**Explanation:**
```
RecentCounter counter = new RecentCounter();
counter.ping(1);    // requests = [1], range is [-2999,1], return 1
counter.ping(100);  // requests = [1, 100], range is [-2900,100], return 2
counter.ping(3001); // requests = [1, 100, 3001], range is [1,3001], return 3
counter.ping(3002); // requests = [1, 100, 3001, 3002], range is [2,3002], return 3
                    // request at time 1 is now outside the window
```

### Example 2:

**Input:**
```
["RecentCounter", "ping", "ping", "ping", "ping", "ping"]
[[], [1], [1000], [2000], [3000], [4000]]
```

**Output:** `[null, 1, 2, 3, 4, 4]`

**Explanation:** At time 4000, the request at time 1 falls outside the 3000ms window, so only 4 requests are in range.

## Constraints

- 1 ≤ t ≤ 10^9
- Each test case will call ping with strictly increasing values of t
- At most 10^4 calls will be made to ping

## Asked by Companies


**Note:** Company names are for illustrative purposes and represent the types of organizations that use similar systems. They do not imply endorsement or partnership.


- Walmart
- Target
- Kroger
- Costco

---

**Disclaimer:** While this problem involves classic computer science algorithms and data structures that are part of common knowledge, all problem descriptions, scenarios, examples, and explanations are original content created specifically for this platform.
