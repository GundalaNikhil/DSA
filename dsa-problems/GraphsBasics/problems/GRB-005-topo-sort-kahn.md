---
problem_id: GRB_TOPO_SORT_KAHN__7394
display_id: GRB-005
slug: topo-sort-kahn
title: "Topological Sort (Kahn)"
difficulty: Easy
difficulty_score: 34
topics:
  - Graphs
  - Topological Sort
  - BFS
tags:
  - graphs-basics
  - topo-sort
  - bfs
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# GRB-005: Topological Sort (Kahn)

## Problem Statement

Given a directed acyclic graph (DAG), output any valid topological ordering of its nodes.

![Problem Illustration](../images/GRB-005/problem-illustration.png)

## Input Format

- First line: integers `n` and `m`
- Next `m` lines: `u v` representing a directed edge `u -> v`

## Output Format

- Single line: `n` integers representing a topological ordering

## Constraints

- `1 <= n <= 100000`
- `0 <= m <= 200000`
- `0 <= u, v < n`
- The input graph is guaranteed to be a DAG

## Example

**Input:**

```
3 2
0 1
1 2
```

**Output:**

```
0 1 2
```

**Explanation:**

The ordering `0 -> 1 -> 2` respects all edges.

![Example Visualization](../images/GRB-005/example-1.png)

## Notes

- Use Kahn's algorithm with an indegree queue.
- Multiple valid orders may exist; any is accepted.
- Since the graph is a DAG, a full ordering always exists.

## Related Topics

Topological Sort, DAGs, BFS

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int[] topoSort(int n, List<List<Integer>> adj) {
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
        }

        Solution solution = new Solution();
        int[] order = solution.topoSort(n, adj);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < order.length; i++) {
            if (i > 0) sb.append(' ');
            sb.append(order[i]);
        }
        System.out.print(sb.toString());
        sc.close();
    }
}
```

### Python

```python
import sys
from collections import deque

def topo_sort(n: int, adj: list[list[int]]) -> list[int]:
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
            
        order = topo_sort(n, adj)
        print(" ".join(map(str, order)))
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
    public: vector<int> topoSort(int n, const vector<vector<int>>& adj) {
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
    }

    Solution solution;
    vector<int> order = solution.topoSort(n, adj);
    for (int i = 0; i < (int)order.size(); i++) {
        if (i) cout << ' ';
        cout << order[i];
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  topoSort(n, adj) {
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
  }

  const solution = new Solution();
  const order = solution.topoSort(n, adj);
  console.log(order.join(" "));
});
```

