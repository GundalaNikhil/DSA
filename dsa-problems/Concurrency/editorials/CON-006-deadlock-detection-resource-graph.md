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
---

# Deadlock Detection in Wait-For Graph

## Problem summary

You are given a directed graph representing “who waits for whom”.

Deadlock exists if and only if there is a directed cycle.

So the task reduces to: detect a cycle in a directed graph with up to `10^5` nodes and `2*10^5` edges.

## Why this is a concurrency problem (not just graphs)

In OS / databases, deadlock detection runs periodically:

- Each thread/transaction is a node.
- An edge forms when you wait for a lock held by someone else.

### Correct approaches

### Approach 1: DFS with colors (classic)

Maintain a state per node:

- 0 = unvisited
- 1 = visiting (in recursion stack)
- 2 = done

When DFS explores an edge to a node with state 1, you found a back edge ⇒ cycle ⇒ deadlock.

Complexity: O(n + m).

Important for large input:

- recursion depth can overflow in Java/Python; use iterative DFS or increase recursion limit carefully (still risky).

### Approach 2: Kahn’s algorithm (topological sort)

If the graph is acyclic, it has a topological ordering.

- compute indegree for each node
- push all indegree-0 nodes into queue
- pop and reduce indegrees

If you process all nodes, no cycle.
If some nodes remain, they are in cycles (or reachable only from cycles).

Complexity: O(n + m).
Memory: O(n + m) for adjacency.

This is often easier to implement iteratively and avoids recursion issues.

### Common mistakes

- Using union-find: does not detect cycles in directed graphs.
- Forgetting that the graph can be disconnected.
- Missing large constraints: O(n*m) is impossible here.

## Interview note

If asked “how to find which threads are deadlocked”, you can:

- return nodes that remain unprocessed in Kahn’s algorithm, or
- extract the cycle using parent pointers in DFS.

But this problem only asks for detection, so a boolean is enough.

## Implementations

### Java
```java
import java.util.*;

class Solution {
    public boolean hasDeadlock(int n, List<int[]> edges) {
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        
        int[] inDegree = new int[n];
        for (int[] edge : edges) {
            adj.get(edge[0]).add(edge[1]);
            inDegree[edge[1]]++;
        }
        
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            if (inDegree[i] == 0) {
                queue.offer(i);
            }
        }
        
        int processedCount = 0;
        while (!queue.isEmpty()) {
            int u = queue.poll();
            processedCount++;
            
            for (int v : adj.get(u)) {
                inDegree[v]--;
                if (inDegree[v] == 0) {
                    queue.offer(v);
                }
            }
        }
        
        // If processedCount < n, there is a cycle (deadlock)
        return processedCount < n;
    }
}

public class Main {
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
def has_deadlock(n: int, edges: list[tuple[int, int]]) -> bool:
    # Nodes 1..n
    adj = [[] for _ in range(n + 1)]
    in_degree = [0] * (n + 1)
    
    for u, v in edges:
        adj[u].append(v)
        in_degree[v] += 1
        
    queue = []
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)
            
    processed_count = 0
    while queue:
        u = queue.pop(0)
        processed_count += 1
        
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
                
    return processed_count != n

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
        vector<vector<int>> adj(n);
        vector<int> inDegree(n, 0);
        
        for (const auto& edge : edges) {
            adj[edge.first].push_back(edge.second);
            inDegree[edge.second]++;
        }
        
        queue<int> q;
        for (int i = 0; i < n; i++) {
            if (inDegree[i] == 0) {
                q.push(i);
            }
        }
        
        int processedCount = 0;
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            processedCount++;
            
            for (int v : adj[u]) {
                inDegree[v]--;
                if (inDegree[v] == 0) {
                    q.push(v);
                }
            }
        }
        
        return processedCount < n;
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

