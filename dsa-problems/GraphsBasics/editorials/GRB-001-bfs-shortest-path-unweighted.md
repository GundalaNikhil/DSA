---
problem_id: GRB_BFS_SHORTEST_PATH_UNWEIGHTED__4821
display_id: GRB-001
slug: bfs-shortest-path-unweighted
title: "BFS Shortest Path in Unweighted Graph"
difficulty: Easy
difficulty_score: 25
topics:
  - Graphs
  - BFS
  - Shortest Path
tags:
  - graphs-basics
  - bfs
  - shortest-path
  - easy
premium: true
subscription_tier: basic
---

# GRB-001: BFS Shortest Path in Unweighted Graph

## 📋 Problem Summary

Find the shortest distance from a source node to all other nodes in an undirected, unweighted graph using BFS. The challenge is efficiently exploring the graph level by level to guarantee shortest paths.

## 🌍 Real-World Scenario

**Scenario Title:** Social Network Friend Recommendations

Imagine you're building a feature for a social networking app like LinkedIn or Facebook. When a user views someone's profile, you want to show how they're connected: "2nd degree connection" or "3rd degree connection."

Think of each person as a node and each friendship as an edge. If Alice wants to see how she's connected to David, you need to find the shortest chain of friendships between them. For example: Alice → Bob → Charlie → David would be a 3rd degree connection (3 edges away).

This exact problem comes up in social networks (friend suggestions), professional networks (find shortest introduction path), network routing (find minimum hops between servers), and even in games (shortest path for a character to reach a destination on a grid).

**Why This Problem Matters:**

- **LinkedIn "How you're connected"**: Shows the shortest introduction path
- **Network packet routing**: Find minimum number of hops between routers
- **Game AI pathfinding**: Character movement on unweighted grids
- **Friend recommendation systems**: Suggest people who are 2-3 connections away

![Real-World Application](../images/GRB-001/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Graph Structure

```
Social Network Example:

        0 (Alice)
       / \
      /   \
     1     3
   (Bob) (Diana)
    |
    |
    2
  (Charlie)

Edges (friendships):
- Alice ↔ Bob
- Alice ↔ Diana
- Bob ↔ Charlie

Distance from Alice (node 0):
- To Alice (0): 0 steps
- To Bob (1): 1 step (direct friend)
- To Charlie (2): 2 steps (through Bob)
- To Diana (3): 1 step (direct friend)

Legend:
Numbers = Node IDs (people)
Lines = Edges (friendships)
Distance = Number of edges in shortest path
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- The graph is **undirected**: if there's an edge (u, v), you can go from u to v AND from v to u
- Node numbering starts from **0** (not 1)
- Output format: print distances to nodes in order 0, 1, 2, ..., n-1 (not in any special order)
- If a node is unreachable from source, output **-1** for that node

Common interpretation mistake:

- ❌ **Wrong**: Output only distances to reachable nodes
- ✅ **Correct**: Output distances to ALL n nodes (use -1 for unreachable)

### Why BFS Works for Shortest Path

In an **unweighted graph**, BFS explores nodes level by level:

- Level 0: source node (distance 0)
- Level 1: all neighbors of source (distance 1)
- Level 2: all nodes 2 edges away (distance 2)
- And so on...

The first time BFS visits a node, it's via the shortest path!

### Why Naive DFS is Wrong

DFS explores deeply first, so it might find a long path to a node before finding the shortest path. BFS guarantees shortest path by exploring closer nodes first.

## Naive Approach

### Intuition

Try all possible paths from source to each node using DFS/recursion, keep track of the shortest one found.

### Algorithm

1. For each target node, use DFS to explore all paths from source
2. Keep track of minimum path length seen for each node
3. Return the minimum distances

### Time Complexity

- **O(V! × E)** in the worst case — trying all possible paths is exponential

### Space Complexity

- **O(V)** for recursion stack

### Why This Works

It explores all possibilities and picks the minimum, so correctness is guaranteed.

### Limitations

- **Exponentially slow** for large graphs
- Doesn't exploit the property that first visit = shortest path in unweighted graphs
- Violates constraints (n ≤ 100,000 would timeout)

## Optimal Approach

### Key Insight

BFS explores nodes in increasing order of distance from source. The moment BFS visits a node for the first time, we've found the shortest path to it! No need to explore other paths.

### Algorithm

1. Create an adjacency list from the edge list
2. Initialize distance array with -1 (unvisited)
3. Set distance[s] = 0 and add source to queue
4. While queue is not empty:
   - Dequeue current node u
   - For each neighbor v of u:
     - If v is unvisited (distance[v] == -1):
       - Set distance[v] = distance[u] + 1
       - Enqueue v
5. Return distance array

### Time Complexity

- **O(V + E)** — each node and edge processed once

### Space Complexity

- **O(V + E)** for adjacency list and O(V) for queue and distance array

### Why This Is Optimal

BFS visits each node at most once and examines each edge at most twice (once from each endpoint). This is the minimum possible since we must examine all reachable parts of the graph.

![Algorithm Visualization](../images/GRB-001/algorithm-visualization.png)
![Algorithm Steps](../images/GRB-001/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public int[] shortestPath(int n, int[][] edges, int s) {
        // Build adjacency list
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adj.add(new ArrayList<>());
        }
        for (int[] edge : edges) {
            int u = edge[0], v = edge[1];
            adj.get(u).add(v);
            adj.get(v).add(u); // Undirected graph
        }

        // Initialize distances to -1 (unvisited)
        int[] dist = new int[n];
        Arrays.fill(dist, -1);

        // BFS
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(s);
        dist[s] = 0;

        while (!queue.isEmpty()) {
            int u = queue.poll();
            for (int v : adj.get(u)) {
                if (dist[v] == -1) { // Not visited yet
                    dist[v] = dist[u] + 1;
                    queue.offer(v);
                }
            }
        }

        return dist;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int s = sc.nextInt();

        int[][] edges = new int[m][2];
        for (int i = 0; i < m; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
        }

        Solution solution = new Solution();
        int[] result = solution.shortestPath(n, edges, s);

        for (int i = 0; i < n; i++) {
            System.out.print(result[i]);
            if (i < n - 1) System.out.print(" ");
        }
        System.out.println();
        sc.close();
    }
}
```

### Python

```python
from collections import deque

def shortest_path(n: int, edges: list, s: int) -> list:
    # Build adjacency list
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)  # Undirected graph

    # Initialize distances to -1 (unvisited)
    dist = [-1] * n

    # BFS
    queue = deque([s])
    dist[s] = 0

    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if dist[v] == -1:  # Not visited yet
                dist[v] = dist[u] + 1
                queue.append(v)

    return dist

def main():
    n, m, s = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append([u, v])

    result = shortest_path(n, edges, s)
    print(' '.join(map(str, result)))

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
    vector<int> shortestPath(int n, vector<vector<int>>& edges, int s) {
        // Build adjacency list
        vector<vector<int>> adj(n);
        for (auto& edge : edges) {
            int u = edge[0], v = edge[1];
            adj[u].push_back(v);
            adj[v].push_back(u); // Undirected graph
        }

        // Initialize distances to -1 (unvisited)
        vector<int> dist(n, -1);

        // BFS
        queue<int> q;
        q.push(s);
        dist[s] = 0;

        while (!q.empty()) {
            int u = q.front();
            q.pop();
            for (int v : adj[u]) {
                if (dist[v] == -1) { // Not visited yet
                    dist[v] = dist[u] + 1;
                    q.push(v);
                }
            }
        }

        return dist;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, s;
    cin >> n >> m >> s;

    vector<vector<int>> edges(m, vector<int>(2));
    for (int i = 0; i < m; i++) {
        cin >> edges[i][0] >> edges[i][1];
    }

    Solution solution;
    vector<int> result = solution.shortestPath(n, edges, s);

    for (int i = 0; i < n; i++) {
        cout << result[i];
        if (i < n - 1) cout << " ";
    }
    cout << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  shortestPath(n, edges, s) {
    // Build adjacency list
    const adj = Array.from({ length: n }, () => []);
    for (const [u, v] of edges) {
      adj[u].push(v);
      adj[v].push(u); // Undirected graph
    }

    // Initialize distances to -1 (unvisited)
    const dist = new Array(n).fill(-1);

    // BFS
    const queue = [s];
    dist[s] = 0;
    let front = 0;

    while (front < queue.length) {
      const u = queue[front++];
      for (const v of adj[u]) {
        if (dist[v] === -1) {
          // Not visited yet
          dist[v] = dist[u] + 1;
          queue.push(v);
        }
      }
    }

    return dist;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  let ptr = 0;
  const [n, m, s] = data[ptr++].split(" ").map(Number);
  const edges = [];
  for (let i = 0; i < m; i++) {
    edges.push(data[ptr++].split(" ").map(Number));
  }

  const solution = new Solution();
  const result = solution.shortestPath(n, edges, s);
  console.log(result.join(" "));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

Use the sample:

- n = 4 nodes (0, 1, 2, 3)
- Edges: (0,1), (1,2), (0,3)
- Source s = 0

We maintain:

- **dist[]** = array storing shortest distance to each node
- **queue** = BFS queue processing nodes level by level

Initialize:

- dist = [-1, -1, -1, -1] (all unvisited)
- queue = [0]
- dist[0] = 0

Now iterate:

| Step | Queue  | Current | Neighbors | Action                            |        dist[] |
| ---: | :----: | ------: | --------- | --------------------------------- | ------------: |
|    1 |  [0]   |       0 | 1, 3      | Visit 1 & 3                       | [0, 1, -1, 1] |
|    2 | [1, 3] |       1 | 0, 2      | Visit 2 (skip 0, already visited) |  [0, 1, 2, 1] |
|    3 | [3, 2] |       3 | 0         | Skip 0 (already visited)          |  [0, 1, 2, 1] |
|    4 |  [2]   |       2 | 1         | Skip 1 (already visited)          |  [0, 1, 2, 1] |
|    5 |   []   |       - | -         | Queue empty, done                 |  [0, 1, 2, 1] |

Answer is `0 1 2 1`.

![Example Visualization](../images/GRB-001/example-1.png)

## ✅ Proof of Correctness

### Invariant

When BFS dequeues a node u, dist[u] contains the shortest path distance from s to u.

### Why the approach is correct

**Base case**: dist[s] = 0 is correct (distance to itself).

**Inductive step**: Assume all nodes at distance ≤ k from s have correct distances. When we process a node u at distance k, we explore its neighbors. Any unvisited neighbor v must be at distance k+1 (since the graph is unweighted). BFS explores nodes level by level, so v cannot be reached via a shorter path.

Therefore, the first time we visit any node is via the shortest path.

## 💡 Interview Extensions (High-Value Add-ons)

- **Path Reconstruction**: Modify to return actual shortest path, not just distance (store parent array)
- **Multiple Sources**: Find shortest distance to nearest source from multiple starting points (multi-source BFS)
- **Weighted Graphs**: What if edges have weights? (Use Dijkstra's algorithm instead)
- **Bidirectional BFS**: Start BFS from both source and target, meet in middle (faster for single target)
- **0-1 BFS**: Special case where edges have weight 0 or 1 (use deque instead of queue)

## Common Mistakes to Avoid

1. **Forgetting Undirected Edges**

   - When building adjacency list, add edge in both directions
   - ❌ Wrong: `adj[u].add(v)` only
   - ✅ Correct: `adj[u].add(v)` AND `adj[v].add(u)`

2. **Not Checking if Already Visited**

   - Must check `dist[v] == -1` before enqueueing neighbor
   - ❌ Wrong: Adding already-visited nodes to queue (infinite loop or wrong distances)
   - ✅ Correct: Only enqueue if `dist[v] == -1`

3. **Using DFS Instead of BFS**

   - DFS doesn't guarantee shortest path in unweighted graphs
   - ❌ Wrong: Depth-first exploration
   - ✅ Correct: Breadth-first (level-by-level) exploration

4. **Wrong Initial Distance**

   - Must initialize dist[s] = 0 before starting BFS
   - ❌ Wrong: Leaving dist[s] = -1 initially
   - ✅ Correct: Set dist[s] = 0 before queue loop

5. **Array Index Out of Bounds**
   - Ensure node IDs are within [0, n-1]
   - Handle edge cases: n=1, no edges, disconnected graph

## Related Concepts

- BFS (Breadth-First Search)
- Graph Traversal
- Queue Data Structure
- Adjacency List Representation
- Dijkstra's Algorithm (weighted version)
- Multi-Source BFS
- Level-Order Traversal (similar concept in trees)
