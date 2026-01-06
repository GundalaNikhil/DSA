---
problem_id: LNK_LINKED_LIST_QUANTUM_SUPERPOSITION__9126
display_id: NTB-LNK-9126
slug: linked-list-quantum-superposition
title: "Linked List with Quantum Superposition"
difficulty: Medium
difficulty_score: 50
topics:
  - Linked Lists
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - linked-list-quantum-superposition
  - linkedlists
  - memory-management
  - pointers
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Linked List with Quantum Superposition

## Problem Statement

Each node stores two possible values `(a, b)` and a collapse rule. On read at time `t`, the value collapses to:

- `a` if `t` is even
- `b` if `t` is odd

Once a node collapses, it remains at that value for all future reads.

Operations:

- `READ pos t`: output the collapsed value at position `pos` at time `t`

## Input Format

- First line: integer `n`
- Next `n` lines: `a b` for each node
- Next line: integer `q`
- Next `q` lines: `pos t`

## Output Format

- For each `READ`, output the value

## Constraints

- `1 <= n, q <= 200000`
- `0 <= t <= 10^9`

## Clarifying Notes

- Collapse is deterministic based on parity of `t`.

## Example Input

```
2
5 7
1 9
3
1 1
1 2
2 3
```

## Example Output

```
7
7
9
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public List<Integer> processQuantumReads(int n, int[][] nodes, int[][] queries) {
        // Your code here
        return new ArrayList<>();
    }
}
```

```python
class Solution:
    def processQuantumReads(self, n: int, nodes: list[list[int]], queries: list[list[int]]) -> list[int]:
        # Your code here
        return []
```

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> processQuantumReads(int n, vector<vector<int>>& nodes, vector<vector<int>>& queries) {
        // Your code here
        return {};
    }
};
```

```javascript
class Solution {
  /**
   * @param {number} n
   * @param {number[][]} nodes
   * @param {number[][]} queries
   * @returns {number[]}
   */
  processQuantumReads(n, nodes, queries) {
    // Your code here
    return [];
  }
}
```
