---
problem_id: GRB_MST_KRUSKAL__2657
display_id: GRB-007
slug: mst-kruskal
title: "MST Kruskal"
difficulty: Medium
difficulty_score: 42
topics:
  - Graphs
  - MST
  - DSU
tags:
  - graphs-basics
  - mst
  - dsu
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# GRB-007: MST Kruskal

## Problem Statement

Given a connected, undirected weighted graph, compute the total weight of its minimum spanning tree (MST) using Kruskal's algorithm.

![Problem Illustration](../images/GRB-007/problem-illustration.png)

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

The MST uses edges (0-1) and (1-2) with total weight 3.

![Example Visualization](../images/GRB-007/example-1.png)

## Notes

- Sort edges by weight and add if they connect different components.
- Use DSU (disjoint set union) with path compression and union by rank.
- The total fits in 64-bit integers.

## Related Topics

Minimum Spanning Tree, Kruskal, DSU

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long mstKruskal(int n, int[][] edges) {
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
        int[][] edges = new int[m][3];
        for (int i = 0; i < m; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
            edges[i][2] = sc.nextInt();
        }

        Solution solution = new Solution();
        System.out.println(solution.mstKruskal(n, edges));
        sc.close();
    }
}
```

### Python

```python
def mst_kruskal(n: int, edges: list[tuple[int, int, int]]) -> int:
    # Your implementation here
    return 0

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it))
    edges = []
    for _ in range(m):
        u = int(next(it)); v = int(next(it)); w = int(next(it))
        edges.append((u, v, w))
    print(mst_kruskal(n, edges))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <array>
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    long long mstKruskal(int n, const vector<array<int, 3>>& edges) {
        // Your implementation here
        return 0LL;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<array<int, 3>> edges(m);
    for (int i = 0; i < m; i++) {
        cin >> edges[i][0] >> edges[i][1] >> edges[i][2];
    }

    Solution solution;
    cout << solution.mstKruskal(n, edges) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  mstKruskal(n, edges) {
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
  const edges = [];
  for (let i = 0; i < m; i++) {
    const u = parseInt(data[idx++], 10);
    const v = parseInt(data[idx++], 10);
    const w = parseInt(data[idx++], 10);
    edges.push([u, v, w]);
  }

  const solution = new Solution();
  console.log(solution.mstKruskal(n, edges).toString());
});
```
