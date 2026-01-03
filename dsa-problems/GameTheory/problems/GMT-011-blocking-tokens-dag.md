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

![Problem Illustration](../images/GMT-011/problem-illustration.png)

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

class Solution {
    public String blockingTokens(int n, int[][] edges, int u, int v) {
        //Implement here
        return "";
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
            int u = sc.nextInt();
            int v = sc.nextInt();

            Solution solution = new Solution();
            System.out.println(solution.blockingTokens(n, edges, u, v));
        }
        sc.close();
    }
}
```

### Python

```python
from typing import List
import sys

sys.setrecursionlimit(20000)

def blocking_tokens(n: int, edges: List[List[int]], u: int, v: int) -> str:
    # //Implement here
    return 0

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
            u_edge = int(next(iterator))
            v_edge = int(next(iterator))
            edges.append([u_edge, v_edge])
        u = int(next(iterator))
        v = int(next(iterator))
            
        print(blocking_tokens(n, edges, u, v))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    string blockingTokens(int n, vector<vector<int>>& edges, int u, int v) {
        //Implement here
        return "";
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
        int u, v;
        cin >> u >> v;
        
        Solution solution;
        cout << solution.blockingTokens(n, edges, u, v) << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  blockingTokens(n, edges, u, v) {
    //Implement here
    return 0;
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
      edges.push([parseInt(flatData[idx++]), parseInt(flatData[idx++])]);
  }
  const u = parseInt(flatData[idx++]);
  const v = parseInt(flatData[idx++]);

  const solution = new Solution();
  console.log(solution.blockingTokens(n, edges, u, v));
});
```

