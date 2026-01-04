---
problem_id: GMT_TOKEN_WALK_DAG__2847
display_id: GMT-002
slug: token-walk-directed-graph
title: "Token Walk on Directed Graph"
difficulty: Medium
difficulty_score: 50
topics:
  - Game Theory
  - Graph Theory
  - Dynamic Programming
tags:
  - dag
  - topological-sort
  - memoization
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GMT-002: Token Walk on Directed Graph

## Problem Statement

You are given a directed acyclic graph (DAG) with `n` nodes labeled from `0` to `n-1`, and `m` directed edges.

A game is played with a single token placed on one of the nodes. Two players take turns moving the token.
In each turn, a player must move the token from its current node `u` to an adjacent node `v` such that there is a directed edge `u -> v`.
The player who cannot make a valid move loses the game.

For each node `i` from `0` to `n-1`, determine if the first player has a winning strategy if the token initially starts at node `i`.

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767513717/dsa/gametheory/uazsin9hdpesoymmncdp.jpg)

## Input Format

- The first line contains two integers `n` and `m`, the number of nodes and edges.
- The next `m` lines each contain two integers `u` and `v`, representing a directed edge from `u` to `v`.

## Output Format

- Return a list of strings (or print them space-separated) where the `i-th` string is "Winning" if the starting node `i` is a winning position, and "Losing" otherwise.

## Constraints

- `1 <= n <= 2 * 10^5`
- `0 <= m <= 2 * 10^5`
- The graph is guaranteed to be a DAG (no cycles).

## Example

**Input:**

```
3 2
0 1
1 2
```

**Output:**

```
Losing Winning Losing
```

**Explanation:**

- Node 2 has no outgoing edges, so it is Losing.
- Node 1 can move to node 2 (Losing), so it is Winning.
- Node 0 can only move to node 1 (Winning), so it is Losing.

![Example Visualization](../images/GMT-002/example-1.png)

## Notes

- A node is a **Losing** position if all reachable nodes are Winning positions (or if there are no moves).
- A node is a **Winning** position if there is at least one move to a Losing position.

## Related Topics

Graph Theory, DFS, Memoization

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public List<String> getWinningPositions(int n, List<List<Integer>> adj) {
        // Implement here
        return new ArrayList<>();
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String nmLine = br.readLine();
        if (nmLine == null) return;
        String[] nmParts = nmLine.trim().split("\\s+");
        int n = Integer.parseInt(nmParts[0]);
        int m = Integer.parseInt(nmParts[1]);

        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int i = 0; i < m; i++) {
            String line = br.readLine();
            if (line == null) break;
            String[] uvParts = line.trim().split("\\s+");
            if (uvParts.length < 2) continue;
            int u = Integer.parseInt(uvParts[0]);
            int v = Integer.parseInt(uvParts[1]);
            adj.get(u).add(v);
        }

        Solution sol = new Solution();
        List<String> results = sol.getWinningPositions(n, adj);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < results.size(); i++) {
            sb.append(results.get(i)).append(i == results.size() - 1 ? "" : " ");
        }
        System.out.println(sb.toString());
    }
}
```

### Python

```python
import sys

# Increase recursion depth for deep DAGs
sys.setrecursionlimit(300000)

class Solution:
    def get_winning_positions(self, n, adj):
        # Implement here
        return []

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
    results = sol.get_winning_positions(n, adj)
    print(" ".join(results))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<string> getWinningPositions(int n, const vector<vector<int>>& adj) {
        // Implement here
        return {};
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
    vector<string> results = sol.getWinningPositions(n, adj);
    for (int i = 0; i < n; i++) {
        cout << results[i] << (i == n - 1 ? "" : " ");
    }
    cout << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  getWinningPositions(n, adj) {
    // Implement here
    return [];
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
  }

  const sol = new Solution();
  const results = sol.getWinningPositions(n, adj);
  console.log(results.join(" "));
}

solve();
```
