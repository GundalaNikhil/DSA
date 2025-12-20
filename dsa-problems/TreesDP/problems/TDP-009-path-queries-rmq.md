---
title: "Path Queries with Euler Tour and RMQ"
problem_id: TDP_PATH_QUERIES_RMQ__6729
difficulty: Medium
tags: [tree-dp, euler-tour, rmq, lca, sparse-table]
slug: path-queries-rmq
time_limit: 2000
memory_limit: 256
---

## Problem Description

You are given a weighted tree with N nodes. The tree has N-1 edges, where each edge has a weight w. You need to preprocess the tree to efficiently answer Q distance queries. Each query asks for the shortest distance between two nodes u and v along the tree path.

---

## Input Format

- First line: Integer N (1 ≤ N ≤ 200,000) — number of nodes
- Next N-1 lines: Three integers u, v, w (1 ≤ u, v ≤ N, 1 ≤ w ≤ 10^6) — edge between u and v with weight w
- Next line: Integer Q (1 ≤ Q ≤ 200,000) — number of queries
- Next Q lines: Two integers u, v — query for distance between u and v

---

## Output Format

For each query, print the distance between nodes u and v.

---

## Examples

### Example 1

**Input:**

```
3
1 2 5
1 3 10
2
2 3
1 2
```

**Output:**

```
15
5
```

**Explanation:**

- Query 1: Distance from node 2 to node 3 = 5 (edge 2-1) + 10 (edge 1-3) = 15
- Query 2: Distance from node 1 to node 2 = 5

### Example 2

**Input:**

```
5
1 2 3
1 3 7
2 4 2
2 5 4
3
4 5
3 5
1 4
```

**Output:**

```
6
14
5
```

**Explanation:**

- Query 1: Distance from node 4 to node 5
  - Path: 4→2→5
  - Distance: 2 (edge 4-2) + 4 (edge 2-5) = 6
- Query 2: Distance from node 3 to node 5
  - Path: 3→1→2→5
  - Distance: 7 (edge 3-1) + 3 (edge 1-2) + 4 (edge 2-5) = 14
- Query 3: Distance from node 1 to node 4
  - Path: 1→2→4
  - Distance: 3 (edge 1-2) + 2 (edge 2-4) = 5

---

## Constraints

- 1 ≤ N ≤ 200,000
- 1 ≤ Q ≤ 200,000
- 1 ≤ w ≤ 10^6
- The graph is guaranteed to be a tree
- 1 ≤ u, v ≤ N

---

## Solution Template

### Java

```java
import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        List<int[]>[] adj = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) {
            adj[i] = new ArrayList<>();
        }

        for (int i = 0; i < n - 1; i++) {
            int u = sc.nextInt(), v = sc.nextInt(), w = sc.nextInt();
            adj[u].add(new int[]{v, w});
            adj[v].add(new int[]{u, w});
        }

        // TODO: Build Euler tour and sparse table

        int q = sc.nextInt();
        for (int i = 0; i < q; i++) {
            int u = sc.nextInt(), v = sc.nextInt();
            System.out.println(0); // Placeholder
        }
    }
}
```

### Python

```python
import sys
from collections import defaultdict

def main():
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1

    adj = defaultdict(list)
    for _ in range(n - 1):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        w = int(data[idx]); idx += 1
        adj[u].append((v, w))
        adj[v].append((u, w))

    # TODO: Build Euler tour and sparse table

    q = int(data[idx]); idx += 1
    for _ in range(q):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        print(0)  # Placeholder

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    vector<vector<pair<int, int>>> adj(n + 1);
    for (int i = 0; i < n - 1; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
        adj[v].push_back({u, w});
    }

    // TODO: Build Euler tour and sparse table

    int q;
    cin >> q;
    for (int i = 0; i < q; i++) {
        int u, v;
        cin >> u >> v;
        cout << 0 << "\n";
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false,
});

const lines = [];
rl.on("line", (line) => lines.push(line.trim()));
rl.on("close", () => {
  let idx = 0;
  const n = parseInt(lines[idx++]);

  const adj = Array.from({ length: n + 1 }, () => []);
  for (let i = 0; i < n - 1; i++) {
    const [u, v, w] = lines[idx++].split(" ").map(Number);
    adj[u].push([v, w]);
    adj[v].push([u, w]);
  }

  // TODO: Build Euler tour and sparse table

  const q = parseInt(lines[idx++]);
  for (let i = 0; i < q; i++) {
    const [u, v] = lines[idx++].split(" ").map(Number);
    console.log(0);
  }
});
```

---

## Hints

<details>
<summary>Hint 1</summary>
Use Euler tour to convert the tree into an array. Record the depth of each node during the tour.
</details>

<details>
<summary>Hint 2</summary>
LCA(u, v) is the node with minimum depth between the first occurrences of u and v in the Euler tour.
</details>

<details>
<summary>Hint 3</summary>
Build a Sparse Table for Range Minimum Query (RMQ) on the depth array to find LCA in O(1).
</details>

<details>
<summary>Hint 4</summary>
Distance between u and v equals: dist(root, u) + dist(root, v) - 2 × dist(root, LCA(u, v)).
</details>
