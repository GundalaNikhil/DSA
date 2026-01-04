---
problem_id: GMT_BLOCKING_TOKENS__5821
display_id: GMT-011
slug: blocking-tokens-dag
title: "Blocking Tokens on DAG"
difficulty: Medium
difficulty_score: 55
topics:
  - Game Theory
  - Graph Theory
  - Dynamic Programming
tags:
  - impartial-game
  - memoization
  - dag
premium: true
subscription_tier: basic
time_limit: 1000
memory_limit: 256
---

# GMT-011: Blocking Tokens on DAG

## Problem Statement

You are given a Directed Acyclic Graph (DAG) with `n` nodes and `m` edges.
There are two tokens placed on distinct nodes `u` and `v`.
Two players take turns making a move.
In each turn, a player must choose **one** of the two tokens and move it along a directed edge to an adjacent node.
**Constraint:** A token cannot be moved to a node that is currently occupied by the other token.

The player who cannot make a valid move loses.
(This happens when both tokens are stuck, or the only available moves are blocked).

Determine if the first player has a winning strategy.

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767539108/dsa/gametheory_simple/bzehnyamdwqw0vr6sajg.jpg)

## Input Format

- The first line contains two integers `n` and `m`.
- The next `m` lines each contain two integers `a` and `b`, representing a directed edge from `a` to `b`.
- The last line contains two integers `u` and `v`, the starting positions of the two tokens.

## Output Format

- Return "First" if the first player wins, and "Second" if the second player wins.

## Constraints

- `2 <= n <= 100`
- `0 <= m <= 2000`
- `1 <= u, v <= n`
- `u != v`
- The graph is a DAG (no cycles).

## Example

**Input:**

```
4 3
1 2
2 3
1 3
1 2
```

**Output:**

```
First
```

**Explanation:**

- Nodes: 1, 2, 3, 4.
- Edges: 1->2, 2->3, 1->3.
- Tokens at 1 and 2.
- Player 1 moves:
  - Move Token 1 (at 1):
    - To 2? Blocked (Token 2 is at 2).
    - To 3? Valid. State becomes {3, 2}.
  - Move Token 2 (at 2):
    - To 3? Valid. State becomes {1, 3}.
- If P1 moves 1->3 (State {2, 3}):
  - P2 moves:
    - Token at 2 can go to 3? Blocked.
    - Token at 3 has no moves.
  - P2 has no moves. P2 loses.
- So P1 wins by moving 1->3.

![Example Visualization](../images/GMT-011/example-1.png)

## Notes

- The game state is defined by the pair of positions `{pos1, pos2}`.
- Since it's a DAG, the game is guaranteed to end.
- `N` is small enough for `O(N^2)` solutions.

## Related Topics

Game Theory, Graph Traversal, Memoization

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public String determineWinner(int n, int m, List<List<Integer>> adj, int u, int v) {
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
        for (int i = 0; i <= n; i++) adj.add(new ArrayList<>());
        for (int i = 0; i < m; i++) {
            String line = br.readLine();
            if (line == null) break;
            String[] uvParts = line.trim().split("\\s+");
            int a = Integer.parseInt(uvParts[0]);
            int b = Integer.parseInt(uvParts[1]);
            adj.get(a).add(b);
        }

        String startLine = br.readLine();
        if (startLine == null) return;
        String[] startParts = startLine.trim().split("\\s+");
        int u = Integer.parseInt(startParts[0]);
        int v = Integer.parseInt(startParts[1]);

        Solution sol = new Solution();
        System.out.println(sol.determineWinner(n, m, adj, u, v));
    }
}
```

### Python

```python
import sys

# Increase recursion depth if needed
sys.setrecursionlimit(20000)

class Solution:
    def determine_winner(self, n, m, adj, u, v):
        # Implement here
        return ""

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])

    adj = [[] for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        a = int(input_data[idx])
        b = int(input_data[idx+1])
        adj[a].append(b)
        idx += 2

    u = int(input_data[idx])
    v = int(input_data[idx+1])

    sol = Solution()
    print(sol.determine_winner(n, m, adj, u, v))

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
    string determineWinner(int n, int m, const vector<vector<int>>& adj, int u, int v) {
        // Implement here
        return "";
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        adj[a].push_back(b);
    }

    int u, v;
    cin >> u >> v;

    Solution sol;
    cout << sol.determineWinner(n, m, adj, u, v) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  determineWinner(n, m, adj, u, v) {
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

  const adj = Array.from({ length: n + 1 }, () => []);
  for (let i = 0; i < m; i++) {
    const a = parseInt(input[idx++]);
    const b = parseInt(input[idx++]);
    adj[a].push(b);
  }

  const u = parseInt(input[idx++]);
  const v = parseInt(input[idx++]);

  const sol = new Solution();
  console.log(sol.determineWinner(n, m, adj, u, v));
}

solve();
```
