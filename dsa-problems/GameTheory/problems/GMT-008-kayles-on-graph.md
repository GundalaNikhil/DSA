---
problem_id: GMT_KAYLES_GRAPH__8203
display_id: GMT-008
slug: kayles-on-graph
title: "Kayles on Graph"
difficulty: Hard
difficulty_score: 65
topics:
  - Game Theory
  - Graph Theory
  - Dynamic Programming
  - Bitmask
tags:
  - impartial-game
  - sprague-grundy
  - state-compression
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GMT-008: Kayles on Graph

## Problem Statement

You are given an undirected graph with `n` nodes and `m` edges.
Two players take turns making a move.
In each turn, a player must choose a node `u` that is currently available (not removed).
The player removes `u` and **all its neighbors** from the graph.
The player who cannot make a valid move loses.
(This happens when the graph is empty).

Determine if the first player has a winning strategy.

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767539106/dsa/gametheory_simple/btxxdaq0hyu44ta7giax.jpg)

## Input Format

- The first line contains two integers `n` and `m`.
- The next `m` lines each contain two integers `u` and `v`, representing an edge between `u` and `v`.
- Nodes are 0-indexed.

## Output Format

- Return "First" if the first player wins, and "Second" if the second player wins.

## Constraints

- `1 <= n <= 15`
- `0 <= m <= n * (n - 1) / 2`

## Example

**Input:**

```
3 2
0 1
1 2
```

**Output:**

```
First
```

**Explanation:**

- Graph: 0-1-2 (Path).
- Available moves:
  - Pick 0: Removes 0 and neighbor 1. Remaining: {2}.
    - From {2}, P2 picks 2 (removes 2). Graph empty. P2 wins.
    - So picking 0 leads to P2 winning. Bad for P1.
  - Pick 1: Removes 1 and neighbors 0, 2. Remaining: {}.
    - Graph empty. P2 has no moves. P2 loses.
    - So picking 1 leads to P1 winning.
  - Pick 2: Removes 2 and neighbor 1. Remaining: {0}.
    - From {0}, P2 picks 0. P2 wins. Bad for P1.
- Since P1 can pick 1 and win, P1 has a winning strategy.

![Example Visualization](../images/GMT-008/example-1.png)

## Notes

- This is a variation of the game Kayles played on a general graph.
- Since `n` is small, use bitmask DP with Sprague-Grundy theorem (or just Win/Loss since it's a single graph).

## Related Topics

Game Theory, Bitmask DP, Graph Theory

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public String determineWinner(int n, int m, List<List<Integer>> adj) {
        // Implement here
        return "";
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
            int u = Integer.parseInt(uvParts[0]);
            int v = Integer.parseInt(uvParts[1]);
            adj.get(u).add(v);
            adj.get(v).add(u);
        }

        Solution sol = new Solution();
        System.out.println(sol.determineWinner(n, m, adj));
    }
}
```

### Python

```python
import sys

class Solution:
    def determine_winner(self, n, m, adj):
        # Implement here
        return ""

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

    sol = Solution()
    print(sol.determine_winner(n, m, adj))

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
    string determineWinner(int n, int m, const vector<vector<int>>& adj) {
        // Implement here
        return "";
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

    Solution sol;
    cout << sol.determineWinner(n, m, adj) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  determineWinner(n, m, adj) {
    // Implement here
    return "";
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

  const sol = new Solution();
  console.log(sol.determineWinner(n, m, adj));
}

solve();
```
