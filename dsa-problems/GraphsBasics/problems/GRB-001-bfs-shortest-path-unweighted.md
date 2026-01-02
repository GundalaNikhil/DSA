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
time_limit: 2000
memory_limit: 256
---

# GRB-001: BFS Shortest Path in Unweighted Graph

## Problem Statement

You are given an undirected, unweighted graph with `n` nodes (numbered from `0` to `n-1`) and `m` edges. You need to find the shortest path distance from a source node `s` to all other nodes in the graph.

In an unweighted graph, each edge has the same weight (you can think of it as weight 1). The shortest path between two nodes is the path with the minimum number of edges.

If a node is not reachable from the source, its distance should be `-1`.

![Problem Illustration](../images/GRB-001/problem-illustration.png)

## Input Format

- First line: Three integers `n`, `m`, and `s` — the number of nodes, number of edges, and source node.
- Next `m` lines: Two integers `u` and `v` representing an undirected edge between nodes `u` and `v`.

## Output Format

Print `n` space-separated integers representing the shortest distance from node `s` to nodes `0, 1, 2, ..., n-1`.

## Constraints

- `1 <= n <= 100000`
- `0 <= m <= 200000`
- `0 <= s < n`
- `0 <= u, v < n`
- No self-loops or multiple edges between the same pair of nodes

## Example

**Input:**

```
4 3 0
0 1
1 2
0 3
```

**Output:**

```
0 1 2 1
```

**Explanation:**

Starting from node 0:

- Distance to node 0 = 0 (itself)
- Distance to node 1 = 1 (direct edge: 0 → 1)
- Distance to node 2 = 2 (path: 0 → 1 → 2)
- Distance to node 3 = 1 (direct edge: 0 → 3)

![Example Visualization](../images/GRB-001/example-1.png)

## Notes

- The graph is undirected, so edge (u, v) means you can travel from u to v and from v to u.
- BFS (Breadth-First Search) naturally finds shortest paths in unweighted graphs.
- Make sure to handle disconnected components (nodes unreachable from source should have distance -1).

## Related Topics

Graphs, BFS, Queue, Shortest Path

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int[] shortestPath(int n, int[][] edges, int s) {
        // Implementation here
        return new int[0];
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
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
import sys
from collections import deque

def shortest_path(n: int, edges: list, s: int) -> list:
    # Implementation here
    return []

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return

    iterator = iter(data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        s = int(next(iterator))

        edges = []
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            edges.append([u, v])

        result = shortest_path(n, edges, s)
        print(' '.join(map(str, result)))
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
    vector<int> shortestPath(int n, vector<vector<int>>& edges, int s) {
        // Implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, s;
    if (!(cin >> n >> m >> s)) return 0;

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
    // Implementation here
    return null;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  if (data.length === 0) return;

  // Flatten data array to handle multiple numbers on one line
  const tokens = data.join(" ").trim().split(/\s+/);
  if (tokens.length === 0 || tokens[0] === "") return;

  let ptr = 0;
  const n = Number(tokens[ptr++]);
  const m = Number(tokens[ptr++]);
  const s = Number(tokens[ptr++]);

  const edges = [];
  for (let i = 0; i < m; i++) {
    const u = Number(tokens[ptr++]);
    const v = Number(tokens[ptr++]);
    edges.push([u, v]);
  }

  const solution = new Solution();
  const result = solution.shortestPath(n, edges, s);
  console.log(result.join(" "));
});
```
