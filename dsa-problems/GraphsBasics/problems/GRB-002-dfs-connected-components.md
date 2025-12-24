---
problem_id: GRB_DFS_CONNECTED_COMPONENTS__5190
display_id: GRB-002
slug: dfs-connected-components
title: "DFS Connected Components"
difficulty: Easy
difficulty_score: 28
topics:
  - Graphs
  - DFS
  - Components
tags:
  - graphs-basics
  - dfs
  - components
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# GRB-002: DFS Connected Components

## Problem Statement

You are given an undirected graph with `n` nodes (0 to `n-1`) and `m` edges. Count the number of connected components and label each node with its component id.

Use depth-first search (DFS) to explore the graph.

![Problem Illustration](../images/GRB-002/problem-illustration.png)

## Input Format

- First line: two integers `n` and `m`
- Next `m` lines: two integers `u` and `v` describing an undirected edge

## Output Format

- Line 1: integer `c`, the number of connected components
- Line 2: `n` integers, `comp[i]` is the component id (1-based) for node `i`

## Constraints

- `1 <= n <= 100000`
- `0 <= m <= 200000`
- `0 <= u, v < n`

## Example

**Input:**

```
4 2
0 1
2 3
```

**Output:**

```
2
1 1 2 2
```

**Explanation:**

Nodes `{0,1}` form component 1 and nodes `{2,3}` form component 2.

![Example Visualization](../images/GRB-002/example-1.png)

## Notes

- Components are numbered in the order they are discovered by DFS.
- If `m=0`, each node is its own component.
- An isolated node forms a component of size 1.

## Related Topics

Graph Traversal, DFS, Connected Components

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int[] components(int n, List<List<Integer>> adj) {
        // Your implementation here
        return new int[n];
    }
}

public class Main {
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
        int[] comp = solution.components(n, adj);
        int maxComp = 0;
        for (int id : comp) maxComp = Math.max(maxComp, id);
        StringBuilder sb = new StringBuilder();
        sb.append(maxComp).append('\n');
        for (int i = 0; i < n; i++) {
            if (i > 0) sb.append(' ');
            sb.append(comp[i]);
        }
        System.out.print(sb.toString());
        sc.close();
    }
}
```

### Python

```python
def components(n: int, adj: list[list[int]]) -> list[int]:
    # Your implementation here
    return [0] * n

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
    comp = components(n, adj)
    max_comp = max(comp) if comp else 0
    out = [str(max_comp), " ".join(str(x) for x in comp)]
    sys.stdout.write("\n".join(out))

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
    vector<int> components(int n, const vector<vector<int>>& adj) {
        // Your implementation here
        return vector<int>(n, 0);
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
    vector<int> comp = solution.components(n, adj);
    int maxComp = 0;
    for (int id : comp) maxComp = max(maxComp, id);
    cout << maxComp << "\n";
    for (int i = 0; i < n; i++) {
        if (i) cout << ' ';
        cout << comp[i];
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  components(n, adj) {
    // Your implementation here
    return new Array(n).fill(0);
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
  const comp = solution.components(n, adj);
  let maxComp = 0;
  for (const id of comp) maxComp = Math.max(maxComp, id);
  console.log(maxComp.toString());
  console.log(comp.join(" "));
});
```
