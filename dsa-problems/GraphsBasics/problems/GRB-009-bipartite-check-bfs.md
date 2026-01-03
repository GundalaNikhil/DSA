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

![Problem Illustration](../images/GRB-009/problem-illustration.png)

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

class Solution {
    public int[] bipartiteColors(int n, List<List<Integer>> adj) {
        //Implement here
        return new int[0];
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            adj.get(u).add(v);
            adj.get(v).add(u);
        }

        Solution solution = new Solution();
        int[] colors = solution.bipartiteColors(n, adj);
        System.out.println(colors == null ? "0" : "1");
        sc.close();
    }
}
```

### Python

```python
import sys
from collections import deque

def bipartite_colors(n: int, adj: list[list[int]]):
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
        adj = [[] for _ in range(n)]
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            adj[u].append(v)
            adj[v].append(u)
            
        colors = bipartite_colors(n, adj)
        if colors is None:
            print("0")
        else:
            print("1")
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

using namespace std;

class Solution {
public:
    public: vector<int> bipartiteColors(int n, const vector<vector<int>>& adj) {
        //Implement here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<vector<int>> adj(n);
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    Solution solution;
    vector<int> colors = solution.bipartiteColors(n, adj);
    
    cout << (colors.empty() ? "0" : "1");
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  bipartiteColors(n, adj) {
    //Implement here
    return 0;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const m = parseInt(data[idx++], 10);
  
  const adj = Array.from({ length: n }, () => []);
  for (let i = 0; i < m; i++) {
    const u = parseInt(data[idx++], 10);
    const v = parseInt(data[idx++], 10);
    adj[u].push(v);
    adj[v].push(u);
  }

  const solution = new Solution();
  const colors = solution.bipartiteColors(n, adj);
  
  console.log(colors === null ? "0" : "1");
});
```

