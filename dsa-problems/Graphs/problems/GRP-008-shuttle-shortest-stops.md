---
problem_id: GRP_SHUTTLE_SHORTEST_STOPS__9247
display_id: GRP-008
slug: shuttle-shortest-stops
title: "Shuttle Shortest Stops"
difficulty: Easy-Medium
difficulty_score: 35
topics:
  - Graph Traversal
  - BFS
  - Shortest Path
tags:
  - graph
  - bfs
  - shortest-path
  - unweighted
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRP-008: Shuttle Shortest Stops

## Problem Statement

Given an unweighted undirected graph with `n` nodes (numbered 0 to n-1) and a source node `s`, find the shortest distance (in number of edges) from the source to all other nodes.

For each node, output its shortest distance from the source. If a node is unreachable from the source, output `-1` for that node.

![Problem Illustration](../images/GRP-008/problem-illustration.png)

## Input Format

- First line: integer `n` (number of nodes)
- Second line: integer `m` (number of edges)
- Next `m` lines: two integers `u v` representing an undirected edge between nodes `u` and `v`
- Last line: integer `s` (source node)

## Output Format

- Single line with `n` space-separated integers representing the shortest distance from source `s` to nodes 0, 1, 2, ..., n-1

## Constraints

- `1 <= n <= 10^5`
- `0 <= m <= 2*10^5`
- `0 <= u, v < n`
- `0 <= s < n`
- There are no self-loops or multiple edges

## Example

**Input:**

```
5
4
0 1
1 2
0 3
3 4
0
```

**Output:**

```
0 1 2 1 2
```

**Explanation:**

Starting from node 0 (source):

- Distance to node 0: 0 (source itself)
- Distance to node 1: 1 (direct edge 0→1)
- Distance to node 2: 2 (path 0→1→2)
- Distance to node 3: 1 (direct edge 0→3)
- Distance to node 4: 2 (path 0→3→4)

![Example Visualization](../images/GRP-008/example-1.png)

## Notes

- Use BFS (Breadth-First Search) to find shortest paths in unweighted graphs
- Initialize all distances to -1, then set source distance to 0
- BFS guarantees that nodes are visited in increasing order of distance from source
- Time complexity: O(n + m)
- Space complexity: O(n) for queue and distance array

## Related Topics

BFS, Shortest Path, Unweighted Graph, Level Order Traversal

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int[] shortestDistances(int n, List<List<Integer>> adj, int source) {
        //Implement here
        return new int[0];
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();

        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adj.add(new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            adj.get(u).add(v);
            adj.get(v).add(u);
        }

        // Handle optional source input
        int source = 0;
        if (sc.hasNextInt()) {
            source = sc.nextInt();
        }

        Solution solution = new Solution();
        int[] result = solution.shortestDistances(n, adj, source);

        for (int i = 0; i < result.length; i++) {
            System.out.print(result[i]);
            if (i < result.length - 1) System.out.print(" ");
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
from typing import List

# Increase recursion depth for deep DFS/Graph traversals
sys.setrecursionlimit(200000)

class Solution:
    def shortest_distances(self, n: int, adj: List[List[int]], source: int) -> List[int]:
        # //Implement here
        return []

if __name__ == "__main__":
    try:
        input_data = sys.stdin.read().split()
    except Exception:
        sys.exit(0)

    if not input_data:
        sys.exit(0)

    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))

        adj = [[] for _ in range(n)]
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            adj[u].append(v)
            adj[v].append(u)

        try:
            source = int(next(iterator))
        except StopIteration:
            source = 0

        solution = Solution()
        result = solution.shortest_distances(n, adj, source)
        print(' '.join(map(str, result)))
    except StopIteration:
        pass
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
    vector<int> shortestDistances(int n, vector<vector<int>>& adj, int source) {
        //Implement here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    vector<vector<int>> adj(n);
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    int source = 0;
    if (cin.peek() != EOF) {
        cin >> source;
    }

    Solution solution;
    vector<int> result = solution.shortestDistances(n, adj, source);

    for (int i = 0; i < result.size(); i++) {
        cout << result[i];
        if (i < result.size() - 1) cout << " ";
    }
    cout << endl;

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  shortestDistances(n, adj, source) {
    //Implement here
    return [];
  }
}

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

  const adj = Array.from({ length: n }, () => []);

  for (let i = 0; i < m; i++) {
    const u = Number(tokens[ptr++]);
    const v = Number(tokens[ptr++]);
    adj[u].push(v);
    adj[v].push(u);
  }

  // Sort neighbors for deterministic traversal
  for (let i = 0; i < n; i++) {
    adj[i].sort((a, b) => a - b);
  }

  let source = 0;
  if (ptr < tokens.length) {
    source = Number(tokens[ptr++]);
  }

  const solution = new Solution();
  const result = solution.shortestDistances(n, adj, source);
  console.log(result.join(" "));
});
```
