---
problem_id: GRB_DETECT_CYCLE_DIRECTED__8425
display_id: GRB-006
slug: detect-cycle-directed
title: "Detect Cycle in Directed Graph"
difficulty: Easy
difficulty_score: 34
topics:
  - Graphs
  - DFS
  - Cycle Detection
tags:
  - graphs-basics
  - cycle-detection
  - dfs
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRB-006: Detect Cycle in Directed Graph

## Problem Statement

Given a directed graph, determine whether it contains a cycle.

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/dsa/graph_basics/GRB-006.jpg)

## Input Format

- First line: integers `n` and `m`
- Next `m` lines: `u v` representing a directed edge `u -> v`

## Output Format

- Print `true` if a directed cycle exists, otherwise `false`

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
true
```

**Explanation:**

The edges form a cycle `0 -> 1 -> 2 -> 0`.

![Example Visualization](../images/GRB-006/example-1.png)

## Notes

- Use DFS with colors (0=unvisited, 1=visiting, 2=done) or Kahn's algorithm.
- Self-loops also count as cycles.
- The graph may be disconnected.

## Related Topics

Cycle Detection, DFS, Directed Graphs

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public boolean hasCycle(int n, int m, List<List<Integer>> adj) {
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
            String[] edge = br.readLine().trim().split("\\s+");
            int u = Integer.parseInt(edge[0]);
            int v = Integer.parseInt(edge[1]);
            adj.get(u).add(v);
        }

        Solution sol = new Solution();
        System.out.println(sol.hasCycle(n, m, adj));
    }
}
```

### Python

```python
import sys

# Increase recursion depth for deep DFS trees
sys.setrecursionlimit(200000)

class Solution:
    def has_cycle(self, n, m, adj):
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
        idx += 2

    sol = Solution()
    print(str(sol.has_cycle(n, m, adj)).lower())

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    bool hasCycle(int n, int m, vector<vector<int>>& adj) {
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
    }

    Solution sol;
    if (sol.hasCycle(n, m, adj)) {
        cout << "true" << endl;
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
  hasCycle(n, m, adj) {
    // Implement here
    return false;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 1) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const m = parseInt(input[idx++]);

  const adj = Array.from({ length: n }, () => []);
  for (let i = 0; i < m; i++) {
    const u = parseInt(input[idx++]);
    const v = parseInt(input[idx++]);
    adj[u].push(v);
  }

  const sol = new Solution();
  console.log(sol.hasCycle(n, m, adj).toString());
}

solve();
```
