---
problem_id: LNK_LINKED_LIST_EVENT_SOURCING__1389
display_id: NTB-LNK-1389
slug: linked-list-event-sourcing
title: "Linked List Event Sourcing"
difficulty: Medium
difficulty_score: 50
topics:
  - Linked Lists
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - linked-list-event-sourcing
  - linkedlists
  - memory-management
  - pointers
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Linked List Event Sourcing

## Problem Statement

You are given an event log of list operations. The list is empty at time 0. Each event has a time and is one of:

- `INS pos x`
- `DEL pos`

For each query time `t`, reconstruct the list after applying all events with time `<= t`, then output the value at position `pos` (or `-1`).

## Input Format

- First line: integer `e` (number of events)
- Next `e` lines: `time type pos [x]`
- Next line: integer `q`
- Next `q` lines: `t pos`

## Output Format

- For each query, output one integer

## Constraints

- `1 <= e, q <= 200000`
- `0 <= time <= 10^9`
- Event times are non-decreasing

## Clarifying Notes

- Positions are 1-based at the time of the event.

## Example Input

```
3
1 INS 1 5
2 INS 2 7
3 DEL 1
2
2 1
3 1
```

## Example Output

```
5
7
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public List<Integer> processEventSourcing(int e, String[] events, int q, int[][] queries) {
        // Your code here
        return new ArrayList<>();
    }
}
```

```python
class Solution:
    def processEventSourcing(self, e: int, events: list[str], q: int, queries: list[list[int]]) -> list[int]:
        # Your code here
        return []
```

```cpp
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<int> processEventSourcing(int e, vector<string>& events, int q, vector<vector<int>>& queries) {
        // Your code here
        return {};
    }
};
```

```javascript
class Solution {
  /**
   * @param {number} e
   * @param {string[]} events
   * @param {number} q
   * @param {number[][]} queries
   * @returns {number[]}
   */
  processEventSourcing(e, events, q, queries) {
    // Your code here
    return [];
  }
}
```
