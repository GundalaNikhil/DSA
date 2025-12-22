---
problem_id: GRB_MST_PRIM__9142
display_id: GRB-008
slug: mst-prim
title: "MST Prim"
difficulty: Medium
difficulty_score: 42
topics:
  - Graphs
  - MST
  - Priority Queue
tags:
  - graphs-basics
  - mst
  - prim
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# GRB-008: MST Prim

## Problem Statement

Given a connected, undirected weighted graph, compute the total weight of its minimum spanning tree (MST) using Prim's algorithm.

![Problem Illustration](../images/GRB-008/problem-illustration.png)

## Input Format

- First line: integers `n` and `m`
- Next `m` lines: `u v w` describing an undirected edge with weight `w`

## Output Format

- Single integer: the total weight of the MST

## Constraints

- `1 <= n <= 100000`
- `n-1 <= m <= 200000`
- `0 <= w <= 10^9`
- The graph is connected

## Example

**Input:**

```
3 3
0 1 1
1 2 2
0 2 3
```

**Output:**

```
3
```

**Explanation:**

Prim's algorithm selects edges with weights 1 and 2 for total 3.

![Example Visualization](../images/GRB-008/example-1.png)

## Notes

- Use a min-heap keyed by edge weight.
- Track visited nodes to avoid cycles.
- Total MST weight fits in 64-bit integers.

## Related Topics

Minimum Spanning Tree, Prim, Priority Queue

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long mstPrim(int n, List<List<int[]>> adj) {
        // Your implementation here
        return 0L;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        List<List<int[]>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            int w = sc.nextInt();
            adj.get(u).add(new int[]{v, w});
            adj.get(v).add(new int[]{u, w});
        }

        Solution solution = new Solution();
        System.out.println(solution.mstPrim(n, adj));
        sc.close();
    }
}
```

### Python

```python
def mst_prim(n: int, adj: list[list[tuple[int, int]]]) -> int:
    # Your implementation here
    return 0

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it))
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)); v = int(next(it)); w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))
    print(mst_prim(n, adj))

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
    long long mstPrim(int n, const vector<vector<pair<int, int>>>& adj) {
        // Your implementation here
        return 0LL;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<vector<pair<int, int>>> adj(n);
    for (int i = 0; i < m; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
        adj[v].push_back({u, w});
    }

    Solution solution;
    cout << solution.mstPrim(n, adj) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  mstPrim(n, adj) {
    // Your implementation here
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
    const w = parseInt(data[idx++], 10);
    adj[u].push([v, w]);
    adj[v].push([u, w]);
  }

  const solution = new Solution();
  console.log(solution.mstPrim(n, adj).toString());
});
```
