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

![Problem Illustration](../images/GMT-002/problem-illustration.png)

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

class Solution {
    public List<String> determineWinningNodes(int n, int[][] edges) {
        // Implementation here
        return new ArrayList<>();
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int m = sc.nextInt();
            int[][] edges = new int[m][2];
            for (int i = 0; i < m; i++) {
                edges[i][0] = sc.nextInt();
                edges[i][1] = sc.nextInt();
            }

            Solution solution = new Solution();
            List<String> result = solution.determineWinningNodes(n, edges);
            
            for (int i = 0; i < result.size(); i++) {
                System.out.print(result.get(i) + (i == result.size() - 1 ? "" : " "));
            }
            System.out.println();
        }
        sc.close();
    }
}
```

### Python

```python
from typing import List
import sys

def determine_winning_nodes(n: int, edges: List[List[int]]) -> List[str]:
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
        edges = []
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            edges.append([u, v])
            
        result = determine_winning_nodes(n, edges)
        print(" ".join(result))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<string> determineWinningNodes(int n, vector<vector<int>>& edges) {
        // Implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, m;
    if (cin >> n >> m) {
        vector<vector<int>> edges(m, vector<int>(2));
        for (int i = 0; i < m; i++) {
            cin >> edges[i][0] >> edges[i][1];
        }
        
        Solution solution;
        vector<string> result = solution.determineWinningNodes(n, edges);
        
        for (int i = 0; i < result.size(); i++) {
            cout << result[i] << (i == result.size() - 1 ? "" : " ");
        }
        cout << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  determineWinningNodes(n, edges) {
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
  
  // Flatten data
  const flatData = [];
  data.forEach(line => {
      line.trim().split(/\s+/).forEach(part => {
          if (part) flatData.push(part);
      });
  });
  
  if (flatData.length === 0) return;
  
  let idx = 0;
  const n = parseInt(flatData[idx++]);
  const m = parseInt(flatData[idx++]);
  
  const edges = [];
  for (let i = 0; i < m; i++) {
      const u = parseInt(flatData[idx++]);
      const v = parseInt(flatData[idx++]);
      edges.push([u, v]);
  }

  const solution = new Solution();
  const result = solution.determineWinningNodes(n, edges);
  console.log(result.join(" "));
});
```
