---
problem_id: CON_DEADLOCK_WFG__7D1C
display_id: CON-006
slug: deadlock-detection-resource-graph
title: "Deadlock Detection in Wait-For Graph"
difficulty: Medium
difficulty_score: 57
topics:
  - Concurrency
  - Deadlocks
  - Graphs
  - Cycle Detection
tags:
  - concurrency
  - deadlock
  - graph
  - cycle-detection
  - medium
premium: true
subscription_tier: basic
time_limit: 3000
memory_limit: 256
---

# Deadlock Detection in Wait-For Graph

## Problem Statement

In a database or OS, you can model lock waiting as a **wait-for graph**:

- Each node is a thread/transaction.
- A directed edge `A -> B` means: “A is waiting for a resource held by B”.

A **deadlock** exists if and only if the graph contains a **cycle**.

Given snapshots of a wait-for graph, detect whether a deadlock is present (cycle exists).

## Input Format

- First line: integers `n m` (nodes, edges)
- Next `m` lines: edges `u v` meaning `u` waits for `v`

Nodes are labeled `1..n`.

## Output Format

Print:

- `DEADLOCK` if a cycle exists
- `NO DEADLOCK` otherwise

## Constraints

- `1 <= n <= 10^5`
- `0 <= m <= 2*10^5`
- Graph can be disconnected

## Examples

### Example 1

**Input:**
```
2 2
1 2
2 1
```

**Output:**
```
DEADLOCK
```

### Example 2

**Input:**
```
4 3
1 2
2 3
3 4
```

**Output:**
```
NO DEADLOCK
```

## Related Topics

Concurrency, Deadlocks, Graph Cycle Detection

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public boolean hasDeadlock(int n, int[][] edges) {
        // Implement cycle detection (DFS / Kahn's algorithm)
        return false;
    }
}
```

### Python

```python
def has_deadlock(n: int, edges: list[tuple[int, int]]) -> bool:
    # Implement cycle detection (DFS / Kahn)
    return False
```

