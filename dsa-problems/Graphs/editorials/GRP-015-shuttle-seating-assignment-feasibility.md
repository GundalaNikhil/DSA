---
problem_id: GRP_SHUTTLE_SEATING_FEASIBILITY__8362
display_id: GRP-015
slug: shuttle-seating-assignment-feasibility
title: Shuttle Seating Assignment Feasibility
difficulty: Medium
difficulty_score: 50
topics:
- Topological Sort
- Kahn's Algorithm
- Cycle Detection
tags:
- graph
- topological-sort
- kahns-algorithm
- dag
- medium
premium: true
subscription_tier: basic
---
# GRP-015: Shuttle Seating Assignment Feasibility

## 📋 Problem Summary

Determine if a valid seating order exists given precedence constraints using Kahn's algorithm for topological sort. Return true if a topological ordering exists (DAG), false if cycles exist.

## 🌍 Real-World Scenario

**Scenario Title:** Task Scheduling with Dependencies

Imagine scheduling tasks where some tasks must complete before others can start. A valid schedule exists only if there are no circular dependencies (cycles). Kahn's algorithm efficiently detects cycles while computing a valid ordering.

This applies to course prerequisites, build systems, project management, and any scenario with dependency constraints. The algorithm processes tasks with no dependencies first, gradually removing them and exposing new tasks ready to execute.

**Why This Problem Matters:**

- **Task Scheduling:** Detecting circular dependencies
- **Build Systems:** Determining compilation order
- **Course Planning:** Validating prerequisite chains
- **Project Management:** Identifying dependency conflicts

![Real-World Application](../images/GRP-015/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Kahn's Algorithm

```
Graph (directed):
    0 → 1 → 2
    ↓       ↑
    3 ------+

Indegrees: [0, 1, 2, 1]
Queue: [0]

Step 1: Process 0, reduce indegree of 1,3 → Queue: [1,3]
Step 2: Process 1, reduce indegree of 2 → Queue: [3,2]
Step 3: Process 3, reduce indegree of 2 → Queue: [2]
Step 4: Process 2 → Queue: []

Processed 4 nodes = total nodes → FEASIBLE (DAG)
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Directed edges:** u→v means u must come before v
- **Cycle detection:** If processed < n nodes, cycle exists
- **Indegree:** Number of incoming edges to a node
- **Queue:** Nodes with indegree 0 are ready to process

## Optimal Approach

### Algorithm (Kahn's Algorithm)

```
is_feasible(n, edges):
    indegree = [0] * n
    adj = [[] for _ in n]
    
    // Build graph and compute indegrees
    for (u, v) in edges:
        adj[u].append(v)
        indegree[v] += 1
    
    // Initialize queue with nodes having indegree 0
    queue = [i for i in 0..n-1 if indegree[i] == 0]
    processed = 0
    
    while queue not empty:
        u = queue.dequeue()
        processed += 1
        
        for v in adj[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.enqueue(v)
    
    return processed == n  // True if DAG, False if cycle
```

### Time Complexity: **O(V + E)**
### Space Complexity: **O(V + E)**

![Algorithm Visualization](../images/GRP-015/algorithm-visualization.png)

## Implementations

### Java
```java
import java.util.*;

class Solution {
    public int[] checkFeasibility(int n, int[][] edges) {
        int[] indegree = new int[n];
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adj.add(new ArrayList<>());
        }

        // Build graph
        for (int[] edge : edges) {
            adj.get(edge[0]).add(edge[1]);
            indegree[edge[1]]++;
        }

        // Count and collect indegree 0 nodes
        int initialZeros = 0;
        for (int i = 0; i < n; i++) {
            if (indegree[i] == 0) {
                initialZeros++;
            }
        }

        // Initialize queue with indegree 0 nodes in sorted order
        List<Integer> zeroIndegreeNodes = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (indegree[i] == 0) {
                zeroIndegreeNodes.add(i);
            }
        }
        Collections.sort(zeroIndegreeNodes);

        // Sort neighbors for deterministic processing
        for (List<Integer> neighbors : adj) {
            Collections.sort(neighbors);
        }

        Queue<Integer> queue = new LinkedList<>(zeroIndegreeNodes);
        int processed = 0;

        while (!queue.isEmpty()) {
            int u = queue.poll();
            processed++;

            for (int v : adj.get(u)) {
                indegree[v]--;
                if (indegree[v] == 0) {
                    queue.offer(v);
                }
            }
        }

        if (processed == n) {
            return new int[]{1, initialZeros};
        } else {
            return new int[]{-1};
        }
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();

        int[][] edges = new int[m][2];
        for (int i = 0; i < m; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
        }

        Solution solution = new Solution();
        int[] result = solution.checkFeasibility(n, edges);

        if (result.length == 1) {
            System.out.println(result[0]);
        } else {
            System.out.println(result[0] + " " + result[1]);
        }
        sc.close();
    }
}
```

### Python
```python
import sys
sys.setrecursionlimit(200000)
from collections import deque
from typing import List, Tuple

def check_feasibility(n: int, edges: List[Tuple[int, int]]) -> Tuple[int, ...]:
    indegree = [0] * n
    adj = [[] for _ in range(n)]
    
    for u, v in edges:
        adj[u].append(v)
        indegree[v] += 1
    
    # Sorting adj for deterministic behavior not strictly needed for topological check 
    # but good for consistent processing
    for neighbors in adj:
        neighbors.sort()

    initial_zeros = 0
    for i in range(n):
        if indegree[i] == 0:
            initial_zeros += 1
            
    queue = deque([i for i in range(n) if indegree[i] == 0])
    processed = 0
    
    while queue:
        u = queue.popleft()
        processed += 1
        
        for v in adj[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)
    
    if processed == n:
        return (1, initial_zeros)
    else:
        return (-1,)

def main():
    try:
        input_data = sys.stdin.read().split()
    except Exception:
        return
        
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        
        edges = []
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            edges.append((u, v))
            
        result = check_feasibility(n, edges)
        
        if len(result) == 1:
            print(result[0])
        else:
            print(f"{result[0]} {result[1]}")
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
#include <algorithm>
using namespace std;

class Solution {
public:
    pair<int, int> checkFeasibility(int n, vector<pair<int,int>>& edges) {
        vector<int> indegree(n, 0);
        vector<vector<int>> adj(n);

        // Build graph
        for (auto& [u, v] : edges) {
            adj[u].push_back(v);
            indegree[v]++;
        }

        // Sort adjacency lists for deterministic behavior
        for (int i = 0; i < n; i++) {
            sort(adj[i].begin(), adj[i].end());
        }

        // Count nodes with indegree 0
        int initialZeros = 0;
        queue<int> q;
        for (int i = 0; i < n; i++) {
            if (indegree[i] == 0) {
                q.push(i);
                initialZeros++;
            }
        }

        int processed = 0;

        while (!q.empty()) {
            int u = q.front();
            q.pop();
            processed++;

            for (int v : adj[u]) {
                indegree[v]--;
                if (indegree[v] == 0) {
                    q.push(v);
                }
            }
        }

        if (processed == n) {
            return {1, initialZeros};
        } else {
            return {-1, -1};
        }
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    vector<pair<int,int>> edges;
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        edges.push_back({u, v});
    }

    Solution solution;
    auto [result, zeros] = solution.checkFeasibility(n, edges);

    if (result == -1) {
        cout << -1 << endl;
    } else {
        cout << result << " " << zeros << endl;
    }

    return 0;
}
```

### JavaScript
```javascript
class Solution {
  checkFeasibility(n, edges) {
    const indegree = Array(n).fill(0);
    const adj = Array.from({ length: n }, () => []);

    // Build graph
    for (const [u, v] of edges) {
      adj[u].push(v);
      indegree[v]++;
    }

    // Sort neighbors for deterministic behavior
    for (const neighbors of adj) {
      neighbors.sort((a, b) => a - b);
    }

    // Count initial indegree 0 nodes
    let initialZeros = 0;
    for (let i = 0; i < n; i++) {
      if (indegree[i] === 0) {
        initialZeros++;
      }
    }

    // Initialize queue with indegree 0 nodes
    const queue = [];
    for (let i = 0; i < n; i++) {
      if (indegree[i] === 0) {
        queue.push(i);
      }
    }

    let processed = 0;

    while (queue.length > 0) {
      const u = queue.shift();
      processed++;

      for (const v of adj[u]) {
        indegree[v]--;
        if (indegree[v] === 0) {
          queue.push(v);
        }
      }
    }

    if (processed === n) {
      return [1, initialZeros];
    } else {
      return [-1];
    }
  }
}

const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  const tokens = data.join(" ").split(/\s+/);
  let ptr = 0;
  const n = Number(tokens[ptr++]);
  const m = Number(tokens[ptr++]);

  const edges = [];
  for (let i = 0; i < m; i++) {
    const u = Number(tokens[ptr++]);
    const v = Number(tokens[ptr++]);
    edges.push([u, v]);
  }

  const solution = new Solution();
  const result = solution.checkFeasibility(n, edges);

  if (result.length === 1) {
    console.log(result[0]);
  } else {
    console.log(`${result[0]} ${result[1]}`);
  }
});
```

## 🧪 Test Case Walkthrough (Dry Run)

n=4, edges=[(0,1), (1,2), (0,3), (3,2)]

| Step | Queue | Processed | Indegrees | Action |
|-----:|:------|:---------:|:----------|:-------|
| 0 | [0] | 0 | [0,1,2,1] | Start |
| 1 | [1,3] | 1 | [0,0,2,0] | Process 0, reduce 1,3 |
| 2 | [3,2] | 2 | [0,0,1,0] | Process 1, reduce 2 |
| 3 | [2] | 3 | [0,0,0,0] | Process 3, reduce 2 |
| 4 | [] | 4 | [0,0,0,0] | Process 2 |

Processed 4 == n → FEASIBLE

![Example Visualization](../images/GRP-015/example-1.png)

## ✅ Proof of Correctness

**Theorem:** Kahn's algorithm correctly detects cycles in directed graphs.

**Proof:** If a cycle exists, all nodes in the cycle have indegree ≥ 1 and will never be added to the queue. Thus, processed < n. If no cycle exists, all nodes will eventually have indegree 0 and be processed.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Return the actual topological ordering
- **Extension 2:** Find all possible topological orderings
- **Extension 3:** Detect and return all cycles
- **Extension 4:** Handle weighted edges (longest path in DAG)

### Common Mistakes to Avoid

1. **Not Initializing Queue Correctly**
   - ❌ Wrong: Starting with arbitrary node
   - ✅ Correct: Start with ALL nodes having indegree 0
   - **Impact:** Misses valid orderings or incorrect cycle detection

2. **Forgetting to Decrement Indegree**
   - ❌ Wrong: Not updating indegree after processing
   - ✅ Correct: Decrement indegree for all neighbors
   - **Description:** Nodes never become ready

3. **Wrong Cycle Detection**
   - ❌ Wrong: Checking if queue becomes empty
   - ✅ Correct: Check if processed == n
   - **Prevention:** Queue can be empty even with unprocessed nodes

4. **Building Graph Incorrectly**
   - ❌ Wrong: Adding edge (v, u) instead of (u, v)
   - ✅ Correct: Respect edge direction
   - **Description:** Reversed dependencies

5. **Not Handling Disconnected Components**
   - ❌ Wrong: Only processing one component
   - ✅ Correct: Initialize queue with all indegree-0 nodes
   - **Description:** Kahn's handles disconnected DAGs correctly

## Related Concepts

- **DFS-based Topological Sort:** Alternative approach
- **Strongly Connected Components:** Cycle detection in directed graphs
- **Critical Path Method:** Longest path in DAG
- **Dependency Resolution:** Package managers, build systems
- **Course Scheduling:** Classic application
