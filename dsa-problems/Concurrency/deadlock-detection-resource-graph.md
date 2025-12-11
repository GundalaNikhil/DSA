---
unique_problem_id: concurrency_006
display_id: CONCURRENCY-006
slug: deadlock-detection-resource-graph
version: 1.0.0
difficulty: Medium
topic_tags:
  - Concurrency
  - Deadlock Detection
  - Graph Algorithms
  - Cycle Detection
  - Wait-For Graph
---

# Deadlock Detection in Resource Graph

## Problem Description

Given snapshots of a wait-for graph (threads/processes and their waiting relationships), detect cycles to identify deadlocks. A cycle in the wait-for graph indicates a deadlock.

## Examples

- Example 1:
  - Input: Edges A→B, B→A (A waits for B, B waits for A)
  - Output: **Deadlock detected** - Cycle: A → B → A

- Example 2:
  - Input: Edges A→B, B→C, C→D
  - Output: **No deadlock** - Linear chain, no cycle

- Example 3:
  - Input: Edges A→B, B→C, C→A, D→E
  - Output: **Deadlock detected** - Cycle: A → B → C → A (D→E is separate, no cycle there)

## Constraints

- Number of nodes (threads/processes) <= 10^5
- Number of edges (wait relationships) <= 10^5

## Function Signatures

### Java
```java
import java.util.*;

class Solution {
    public boolean detectDeadlock(int n, int[][] edges) {
        // Implementation here
    }
    
    public List<Integer> getDeadlockCycle(int n, int[][] edges) {
        // Implementation here
    }
}
```

### Python
```python
from typing import List, Tuple, Optional

def detect_deadlock(n: int, edges: List[Tuple[int, int]]) -> bool:
    """
    Detect if a deadlock exists in the wait-for graph.
    
    Args:
        n: Number of nodes (threads/processes)
        edges: List of (waiter, waited_for) edges
    
    Returns:
        True if a cycle (deadlock) exists
    """
    pass

def get_deadlock_cycle(n: int, edges: List[Tuple[int, int]]) -> Optional[List[int]]:
    """Return the cycle if deadlock exists, else None."""
    pass
```

### C++
```cpp
#include <vector>
using namespace std;

class Solution {
public:
    bool detectDeadlock(int n, const vector<pair<int,int>>& edges) {
        // Implementation here
    }
    
    vector<int> getDeadlockCycle(int n, const vector<pair<int,int>>& edges) {
        // Implementation here
    }
};
```

## Input Format

The input will be provided as:
- First line: Integer n (number of nodes)
- Following lines: Edges in format "A B" meaning A waits for B

### Sample Input
```
3
A B
B C
C A
```

## Hints

Use DFS with three-color marking (white=unvisited, gray=in-progress, black=done). A cycle exists if we encounter a gray node during DFS.

## Quiz

### Question 1
How is a deadlock represented in a wait-for graph?

A) A node with no outgoing edges  
B) A cycle in the directed graph  
C) A node with many incoming edges  
D) A disconnected component

**Correct Answer:** B

**Explanation:** A cycle means A waits for B waits for C waits for A... None can proceed, hence deadlock.

### Question 2
What is the time complexity of cycle detection using DFS?

A) O(n)  
B) O(n + e) where e is the number of edges  
C) O(n²)  
D) O(e²)

**Correct Answer:** B

**Explanation:** DFS visits each node and edge once, giving O(n + e).

### Question 3
In the three-color algorithm, what does a gray node signify?

A) The node has been fully processed  
B) The node is on the current DFS path (in progress)  
C) The node has never been visited  
D) The node is in a cycle

**Correct Answer:** B

**Explanation:** Gray nodes are currently on the DFS stack. Encountering a gray node means we've found a back edge, indicating a cycle.

### Question 4
How can deadlocks be prevented at runtime?

A) Detect and kill one thread in the cycle  
B) Use deadlock prevention algorithms (ordering, timeouts)  
C) Ignore them  
D) Both A and B

**Correct Answer:** D

**Explanation:** Both detection+recovery (kill a thread) and prevention (resource ordering, lock timeouts) are valid strategies.
