---
problem_id: GRB_BIPARTITE_CHECK_BFS__5073
display_id: GRB-009
slug: bipartite-check-bfs
title: "Bipartite Check BFS"
difficulty: Easy
difficulty_score: 36
topics:
  - Graphs
  - BFS
  - Bipartite
tags:
  - graphs-basics
  - bipartite
  - bfs
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRB-009: Bipartite Check BFS

## Problem Statement

Given an undirected graph, determine whether it is bipartite. If it is bipartite, output a valid 2-coloring. Otherwise, output `false`.

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/dsa/graph_basics/GRB-009.jpg)

## Input Format

- First line: integers `n` and `m`
- Next `m` lines: `u v` describing an undirected edge

## Output Format

- If bipartite: print `true` on line 1 and a line of `n` integers (`0` or `1`) for node colors
- If not bipartite: print `false`

## Constraints

- `1 <= n <= 100000`
- `0 <= m <= 200000`
- `0 <= u, v < n`

## Example

**Input:**

```
3 3
0 1
1 2
2 0
```

**Output:**

```
false
```

**Explanation:**

A triangle has an odd cycle, so it is not bipartite.

![Example Visualization](../images/GRB-009/example-1.png)

## Notes

- The graph may be disconnected; check each component.
- Use BFS coloring with two colors.
- Any valid coloring is accepted.

## Related Topics

Bipartite Graph, BFS, Coloring

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public boolean isBipartite(int n, int m, List<List<Integer>> adj, int[] colors) {
        // Implement here
        return false;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String nmLine = br.readLine();
        if (nmLine == null) return;
        String[] nm = nmLine.trim().split("\\s+");
        int n = Integer.parseInt(nm[0]);
        int m = Integer.parseInt(nm[1]);

        List<List<Integer>> adj = new ArrayList<>(n);
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());

        for (int i = 0; i < m; i++) {
            String[] edgeLine = br.readLine().trim().split("\\s+");
            int u = Integer.parseInt(edgeLine[0]);
            int v = Integer.parseInt(edgeLine[1]);
            adj.get(u).add(v);
            adj.get(v).add(u);
        }

        int[] colors = new int[n];
        Solution sol = new Solution();
        if (sol.isBipartite(n, m, adj, colors)) {
            PrintWriter out = new PrintWriter(System.out);
            out.println("true");
            for (int i = 0; i < n; i++) {
                out.print(colors[i] + (i == n - 1 ? "" : " "));
            }
            out.println();
            out.flush();
        } else {
            System.out.println("false");
        }
    }
}
```

### Python

```python
import sys
from collections import deque

class Solution:
    def is_bipartite(self, n, m, adj, colors):
        # Implement here
        return False

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])

    adj = [[] for _ in range(n)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2

    colors = [0] * n
    sol = Solution()
    if sol.is_bipartite(n, m, adj, colors):
        print("true")
        print(*(colors))
    else:
        print("false")

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    bool isBipartite(int n, int m, vector<vector<int>>& adj, vector<int>& colors) {
        // Implement here
        return false;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<int>> adj(n);
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<int> colors(n);
    Solution sol;
    if (sol.isBipartite(n, m, adj, colors)) {
        cout << "true" << endl;
        for (int i = 0; i < n; i++) {
            cout << colors[i] << (i == n - 1 ? "" : " ");
        }
        cout << endl;
    } else {
        cout << "false" << endl;
    }

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  isBipartite(n, m, adj, colors) {
    // Implement here
    return false;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const m = parseInt(input[idx++]);

  const adj = Array.from({ length: n }, () => []);
  for (let i = 0; i < m; i++) {
    const u = parseInt(input[idx++]);
    const v = parseInt(input[idx++]);
    adj[u].push(v);
    adj[v].push(u);
  }

  const colors = new Array(n).fill(0);
  const sol = new Solution();
  if (sol.isBipartite(n, m, adj, colors)) {
    console.log("true");
    console.log(colors.join(" "));
  } else {
    console.log("false");
  }
}

solve();
```
