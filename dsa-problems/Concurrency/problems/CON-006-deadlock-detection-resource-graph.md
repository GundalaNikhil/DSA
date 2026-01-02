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
    public boolean hasDeadlock(int n, List<int[]> edges) {
        // Implementation here
        return false;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        
        int n = sc.nextInt();
        int m = sc.nextInt();
        
        List<int[]> edges = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            edges.add(new int[]{u, v});
        }
        
        Solution solution = new Solution();
        System.out.println(solution.hasDeadlock(n, edges));
        sc.close();
    }
}
```

### Python

```python
import sys

def has_deadlock(n: int, edges: list[tuple[int, int]]) -> bool:
    # Implementation here
    return False

def main():
    import sys
    # Use generator pattern for robust reading
    def input_gen():
        for line in sys.stdin:
            for token in line.split():
                yield token
    it = input_gen()
    
    try:
        n = int(next(it))
        m = int(next(it))
        edges = []
        for _ in range(m):
            u = int(next(it))
            v = int(next(it))
            edges.append((u, v))
        
        if has_deadlock(n, edges):
            print("DEADLOCK")
        else:
            print("NO DEADLOCK")
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    bool hasDeadlock(int n, vector<pair<int, int>>& edges) {
        // Implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, m;
    if (!(cin >> n >> m)) return 0;
    
    vector<pair<int, int>> edges(m);
    for (int i = 0; i < m; i++) {
        cin >> edges[i].first >> edges[i].second;
    }
    
    Solution solution;
    cout << (solution.hasDeadlock(n, edges) ? "true" : "false") << "\n";
    
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  hasDeadlock(n, edges) {
    // Implementation here
    return null;
  }
}

class Solution {
  hasDeadlock(n, edges) {
    const adj = Array.from({ length: n }, () => []);
    const inDegree = new Int32Array(n).fill(0);
    
    for (const [u, v] of edges) {
      adj[u].push(v);
      inDegree[v]++;
    }
    
    const queue = [];
    for (let i = 0; i < n; i++) {
      if (inDegree[i] === 0) {
        queue.push(i);
      }
    }
    
    let head = 0;
    let processedCount = 0;
    
    while (head < queue.length) {
      const u = queue[head++];
      processedCount++;
      
      for (const v of adj[u]) {
        inDegree[v]--;
        if (inDegree[v] === 0) {
          queue.push(v);
        }
      }
    }
    
    return processedCount < n;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  
  let ptr = 0;
  const n = parseInt(data[ptr++], 10);
  const m = parseInt(data[ptr++], 10);
  
  const edges = [];
  for (let i = 0; i < m; i++) {
    const u = parseInt(data[ptr++], 10);
    const v = parseInt(data[ptr++], 10);
    edges.push([u, v]);
  }
  
  const solution = new Solution();
  console.log(solution.hasDeadlock(n, edges));
});
```
