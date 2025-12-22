---
problem_id: AGR_EULERIAN_TRAIL_DIRECTED__4836
display_id: AGR-007
slug: eulerian-trail-directed
title: "Eulerian Trail With Directed Edges"
difficulty: Medium
difficulty_score: 48
topics:
  - Graphs
  - Eulerian Path
  - DFS
tags:
  - advanced-graphs
  - eulerian
  - hierholzer
  - medium
premium: true
subscription_tier: basic
---

# AGR-007: Eulerian Trail With Directed Edges

## 📋 Problem Summary

Find a path in a directed graph that visits every edge exactly once. If the path starts and ends at the same vertex, it's an **Eulerian Circuit**. If they are different, it's an **Eulerian Trail**.

## 🌍 Real-World Scenario

**Scenario Title:** The Efficient Mail Carrier

A mail carrier must deliver mail to houses along one-way streets.
-   **Goal:** Traverse every street (edge) exactly once to minimize wasted time.
-   **Constraint:** Streets are one-way.
-   **Problem:** Can they plan such a route? If so, where must they start?

![Real-World Application](../images/AGR-007/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Graph:**
```
    (0) --> (1)
     ^       |
     |       v
    (3) <-- (2) --> (4)
```
-   **Degrees:**
    -   0: in=1, out=1
    -   1: in=1, out=1
    -   2: in=1, out=2 (Start candidate? out > in)
    -   3: in=1, out=1
    -   4: in=1, out=0 (End candidate? in > out)
-   **Trail:** `2 -> 4` (stuck).
-   **Wait:** `2->0->1->2->4`.
-   **Start Node:** 2 (`out = in + 1`).
-   **End Node:** 4 (`in = out + 1`).

### Algorithm: Hierholzer's Algorithm

1.  **Check Existence:**
    -   Calculate `in` and `out` degrees for all nodes.
    -   Count nodes where `out != in`.
    -   **Case 1 (Circuit):** All `out == in`. Start anywhere (with edges).
    -   **Case 2 (Trail):** Exactly one node `S` has `out = in + 1`, exactly one node `E` has `in = out + 1`, all others `out == in`. Start at `S`.
    -   **Case 3 (Impossible):** Any other degree configuration.
2.  **Check Connectivity:** The graph (ignoring isolated vertices) must be weakly connected. Hierholzer's naturally checks this: if the resulting path length != M+1, it's disconnected.
3.  **Construct Path:**
    -   Start DFS from `S`.
    -   Follow edges, marking them as used (or removing from adjacency list).
    -   When stuck (no outgoing edges), add node to `path`.
    -   Backtrack.
    -   Result is `path` reversed.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **M=0:** A graph with no edges has an Eulerian trail of length 1 (just the node). Output `YES` and any node.
-   **Output Format:** `YES` followed by the sequence of nodes.
-   **Edge Removal:** Efficiently remove edges. `adj[u].pop()` is O(1). Using an index pointer `ptr[u]` is cleaner.

## Naive Approach

### Intuition

Backtracking (Try all paths).

### Time Complexity

-   **Exponential**: `O(N!)`. Impossible for N=100,000.

## Optimal Approach (Hierholzer's)

### Time Complexity

-   **O(N + M)**: Each edge visited once.

### Space Complexity

-   **O(N + M)**: Adjacency list and recursion stack.

## Implementations

### Java

```java
import java.util.*;

class Solution {
    private List<Deque<Integer>> adj;
    private List<Integer> trail;

    public int[] eulerTrail(int n, int[][] edges) {
        int m = edges.length;
        if (m == 0) return new int[]{0};

        int[] in = new int[n];
        int[] out = new int[n];
        adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayDeque<>());

        for (int[] e : edges) {
            out[e[0]]++;
            in[e[1]]++;
            adj.get(e[0]).add(e[1]);
        }

        int startNode = -1;
        int endNode = -1;
        int diffCount = 0;

        for (int i = 0; i < n; i++) {
            if (out[i] == in[i] + 1) {
                if (startNode != -1) return null; // More than one start
                startNode = i;
                diffCount++;
            } else if (in[i] == out[i] + 1) {
                if (endNode != -1) return null; // More than one end
                endNode = i;
                diffCount++;
            } else if (in[i] != out[i]) {
                return null; // Invalid degree
            }
        }

        if (diffCount == 0) {
            // Circuit: find first node with edges
            for (int i = 0; i < n; i++) {
                if (out[i] > 0) {
                    startNode = i;
                    break;
                }
            }
        } else if (diffCount != 2) {
            return null;
        }

        if (startNode == -1) return null; // Should not happen if m > 0

        trail = new ArrayList<>();
        dfs(startNode);

        if (trail.size() != m + 1) return null; // Disconnected components

        int[] res = new int[trail.size()];
        for (int i = 0; i < trail.size(); i++) {
            res[i] = trail.get(trail.size() - 1 - i);
        }
        return res;
    }

    private void dfs(int u) {
        Deque<Integer> neighbors = adj.get(u);
        while (!neighbors.isEmpty()) {
            int v = neighbors.poll();
            dfs(v);
        }
        trail.add(u);
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[][] edges = new int[m][2];
        for (int i = 0; i < m; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
        }

        Solution solution = new Solution();
        int[] trail = solution.eulerTrail(n, edges);
        if (trail == null) {
            System.out.print("NO");
        } else {
            StringBuilder sb = new StringBuilder();
            sb.append("YES\n");
            for (int i = 0; i < trail.length; i++) {
                if (i > 0) sb.append(' ');
                sb.append(trail[i]);
            }
            System.out.print(sb.toString());
        }
        sc.close();
    }
}
```

### Python

```python
import sys

# Increase recursion depth
sys.setrecursionlimit(300000)

def euler_trail(n: int, edges: list[tuple[int, int]]):
    m = len(edges)
    if m == 0:
        return [0]
        
    in_deg = [0] * n
    out_deg = [0] * n
    adj = [[] for _ in range(n)]
    
    for u, v in edges:
        out_deg[u] += 1
        in_deg[v] += 1
        adj[u].append(v)
        
    start_node = -1
    end_node = -1
    diff_count = 0
    
    for i in range(n):
        if out_deg[i] == in_deg[i] + 1:
            if start_node != -1: return None
            start_node = i
            diff_count += 1
        elif in_deg[i] == out_deg[i] + 1:
            if end_node != -1: return None
            end_node = i
            diff_count += 1
        elif in_deg[i] != out_deg[i]:
            return None
            
    if diff_count == 0:
        for i in range(n):
            if out_deg[i] > 0:
                start_node = i
                break
    elif diff_count != 2:
        return None
        
    if start_node == -1: return None
    
    trail = []
    
    def dfs(u):
        while adj[u]:
            v = adj[u].pop()
            dfs(v)
        trail.append(u)
        
    dfs(start_node)
    
    if len(trail) != m + 1:
        return None
        
    return trail[::-1]

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        edges = []
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            edges.append((u, v))
            
        trail = euler_trail(n, edges)
        if trail is None:
            sys.stdout.write("NO")
        else:
            sys.stdout.write("YES\n" + " ".join(map(str, trail)))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <deque>

using namespace std;

class Solution {
    vector<vector<int>> adj;
    vector<int> trail;

    void dfs(int u) {
        while (!adj[u].empty()) {
            int v = adj[u].back();
            adj[u].pop_back();
            dfs(v);
        }
        trail.push_back(u);
    }

public:
    vector<int> eulerTrail(int n, const vector<pair<int, int>>& edges) {
        int m = edges.size();
        if (m == 0) return {0};

        vector<int> in(n, 0), out(n, 0);
        adj.assign(n, vector<int>());

        for (const auto& e : edges) {
            out[e.first]++;
            in[e.second]++;
            adj[e.first].push_back(e.second);
        }

        int startNode = -1;
        int endNode = -1;
        int diffCount = 0;

        for (int i = 0; i < n; i++) {
            if (out[i] == in[i] + 1) {
                if (startNode != -1) return {};
                startNode = i;
                diffCount++;
            } else if (in[i] == out[i] + 1) {
                if (endNode != -1) return {};
                endNode = i;
                diffCount++;
            } else if (in[i] != out[i]) {
                return {};
            }
        }

        if (diffCount == 0) {
            for (int i = 0; i < n; i++) {
                if (out[i] > 0) {
                    startNode = i;
                    break;
                }
            }
        } else if (diffCount != 2) {
            return {};
        }

        if (startNode == -1) return {};

        dfs(startNode);

        if (trail.size() != m + 1) return {};

        reverse(trail.begin(), trail.end());
        return trail;
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
    vector<int> trail = solution.eulerTrail(n, edges);
    if (trail.empty()) {
        cout << "NO";
    } else {
        cout << "YES\n";
        for (int i = 0; i < (int)trail.size(); i++) {
            if (i) cout << ' ';
            cout << trail[i];
        }
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  eulerTrail(n, edges) {
    const m = edges.length;
    if (m === 0) return [0];

    const inDeg = new Int32Array(n).fill(0);
    const outDeg = new Int32Array(n).fill(0);
    const adj = Array.from({ length: n }, () => []);

    for (const [u, v] of edges) {
      outDeg[u]++;
      inDeg[v]++;
      adj[u].push(v);
    }

    let startNode = -1;
    let endNode = -1;
    let diffCount = 0;

    for (let i = 0; i < n; i++) {
      if (outDeg[i] === inDeg[i] + 1) {
        if (startNode !== -1) return null;
        startNode = i;
        diffCount++;
      } else if (inDeg[i] === outDeg[i] + 1) {
        if (endNode !== -1) return null;
        endNode = i;
        diffCount++;
      } else if (inDeg[i] !== outDeg[i]) {
        return null;
      }
    }

    if (diffCount === 0) {
      for (let i = 0; i < n; i++) {
        if (outDeg[i] > 0) {
          startNode = i;
          break;
        }
      }
    } else if (diffCount !== 2) {
      return null;
    }

    if (startNode === -1) return null;

    const trail = [];
    // Iterative DFS to avoid stack overflow
    const stack = [startNode];
    
    // Hierholzer's iterative:
    // Maintain current path. If node has edges, push to stack and take edge.
    // If no edges, pop from stack and add to trail.
    
    // stack = [start]
    // while stack:
    //   u = stack[-1]
    //   if adj[u]:
    //     v = adj[u].pop()
    //     stack.push(v)
    //   else:
    //     trail.push(stack.pop())
    
    while (stack.length > 0) {
        const u = stack[stack.length - 1];
        if (adj[u].length > 0) {
            const v = adj[u].pop();
            stack.push(v);
        } else {
            trail.push(stack.pop());
        }
    }

    if (trail.length !== m + 1) return null;

    return trail.reverse();
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
  
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const m = parseInt(data[idx++], 10);
  const edges = [];
  for (let i = 0; i < m; i++) {
    const u = parseInt(data[idx++], 10);
    const v = parseInt(data[idx++], 10);
    edges.push([u, v]);
  }

  const solution = new Solution();
  const trail = solution.eulerTrail(n, edges);
  if (trail === null) {
    console.log("NO");
  } else {
    console.log("YES");
    console.log(trail.join(" "));
  }
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
3 3
0 1
1 2
2 0
```
**Degree Check:**
-   0: in=1, out=1
-   1: in=1, out=1
-   2: in=1, out=1
-   All equal. Circuit. Start at 0.

**Hierholzer:**
1.  Stack: `[0]`.
2.  Top 0. Has edge `0->1`. Pop. Stack: `[0, 1]`.
3.  Top 1. Has edge `1->2`. Pop. Stack: `[0, 1, 2]`.
4.  Top 2. Has edge `2->0`. Pop. Stack: `[0, 1, 2, 0]`.
5.  Top 0. No edges. Pop 0. Trail: `[0]`.
6.  Top 2. No edges. Pop 2. Trail: `[0, 2]`.
7.  Top 1. No edges. Pop 1. Trail: `[0, 2, 1]`.
8.  Top 0. No edges. Pop 0. Trail: `[0, 2, 1, 0]`.

**Result:** Reverse trail -> `0 1 2 0`. Correct.

## ✅ Proof of Correctness

-   **Degrees:** Euler proved that a connected graph has an Eulerian trail iff the degree conditions are met.
-   **Hierholzer:** By greedily following edges and backtracking only when stuck, we essentially find a main cycle and splice in sub-cycles. Since the graph is connected, we eventually visit all edges.

## 💡 Interview Extensions (High-Value Add-ons)

-   **Undirected Graph:** Conditions change (all degrees even, or exactly two odd). Algorithm is similar but must handle back-edges (remove `u->v` and `v->u`).
-   **Chinese Postman Problem:** Find shortest path visiting all edges (allows repeating). If Eulerian, it's just total weight. If not, add edges to make it Eulerian.

### Common Mistakes to Avoid

1.  **Connectivity:** Degree check passes, but graph has two disjoint components with edges. Check `trail.length == m + 1`.
2.  **Recursion Depth:** Python/Java recursion limit is low. Use `sys.setrecursionlimit` or iterative stack.
3.  **Edge Removal:** Removing from middle of list is O(N). Use `pop()` from end or an index pointer.
