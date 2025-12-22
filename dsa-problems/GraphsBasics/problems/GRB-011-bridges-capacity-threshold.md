---
problem_id: GRB_BRIDGES_CAPACITY_THRESHOLD__4509
display_id: GRB-011
slug: bridges-capacity-threshold
title: "Bridges With Capacity Threshold"
difficulty: Medium
difficulty_score: 55
topics:
  - Graphs
  - Bridges
  - DFS
tags:
  - graphs-basics
  - bridges
  - dfs
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# GRB-011: Bridges With Capacity Threshold

## Problem Statement

You are given an undirected graph where each edge has a capacity `c`. An edge is **critical** if:

1. It is a bridge (removing it increases the number of connected components), and
2. Its capacity is strictly less than a threshold `T`.

Find all such edges.

![Problem Illustration](../images/GRB-011/problem-illustration.png)

## Input Format

- First line: integers `n`, `m`, and `T`
- Next `m` lines: `u v c` describing an undirected edge with capacity `c`

## Output Format

- Line 1: integer `k`, number of critical edges
- Next `k` lines: `u v` for each critical edge in the order they appear in input

## Constraints

- `1 <= n <= 100000`
- `0 <= m <= 200000`
- `0 <= c <= 10^9`
- `0 <= T <= 10^9`
- `0 <= u, v < n`

## Example

**Input:**

```
4 4 3
0 1 1
1 2 5
2 0 1
1 3 2
```

**Output:**

```
1
1 3
```

**Explanation:**

Edge (1,3) is a bridge and has capacity 2 < 3.

![Example Visualization](../images/GRB-011/example-1.png)

## Notes

- Use DFS low-link to detect bridges.
- The order of output edges must match their input order.
- If no edges qualify, print `0` and nothing else.

## Related Topics

Bridges, DFS, Graph Connectivity

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public List<int[]> criticalEdges(int n, int[][] edges, int T) {
        // Your implementation here
        return new ArrayList<>();
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        int T = sc.nextInt();
        int[][] edges = new int[m][3];
        for (int i = 0; i < m; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
            edges[i][2] = sc.nextInt();
        }

        Solution solution = new Solution();
        List<int[]> ans = solution.criticalEdges(n, edges, T);
        StringBuilder sb = new StringBuilder();
        sb.append(ans.size()).append('\n');
        for (int[] e : ans) {
            sb.append(e[0]).append(' ').append(e[1]).append('\n');
        }
        System.out.print(sb.toString().trim());
        sc.close();
    }
}
```

### Python

```python
def critical_edges(n: int, edges: list[tuple[int, int, int]], T: int) -> list[tuple[int, int]]:
    # Your implementation here
    return []

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); T = int(next(it))
    edges = []
    for _ in range(m):
        u = int(next(it)); v = int(next(it)); c = int(next(it))
        edges.append((u, v, c))
    ans = critical_edges(n, edges, T)
    out = [str(len(ans))]
    out += [f"{u} {v}" for (u, v) in ans]
    sys.stdout.write("\n".join(out))

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
    vector<pair<int, int>> criticalEdges(int n, const vector<array<int, 3>>& edges, int T) {
        // Your implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, T;
    if (!(cin >> n >> m >> T)) return 0;
    vector<array<int, 3>> edges(m);
    for (int i = 0; i < m; i++) {
        cin >> edges[i][0] >> edges[i][1] >> edges[i][2];
    }

    Solution solution;
    vector<pair<int, int>> ans = solution.criticalEdges(n, edges, T);
    cout << ans.size() << "\n";
    for (auto& e : ans) {
        cout << e.first << ' ' << e.second << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  criticalEdges(n, edges, T) {
    // Your implementation here
    return [];
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
  const T = parseInt(data[idx++], 10);
  const edges = [];
  for (let i = 0; i < m; i++) {
    const u = parseInt(data[idx++], 10);
    const v = parseInt(data[idx++], 10);
    const c = parseInt(data[idx++], 10);
    edges.push([u, v, c]);
  }

  const solution = new Solution();
  const ans = solution.criticalEdges(n, edges, T);
  const out = [ans.length.toString(), ...ans.map((e) => `${e[0]} ${e[1]}`)];
  console.log(out.join("\n"));
});
```
