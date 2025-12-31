---
problem_id: AGR_MAX_FLOW_VERTEX_CAPACITY__5913
display_id: AGR-002
slug: max-flow-vertex-capacity
title: "Max Flow With Vertex Capacities"
difficulty: Medium
difficulty_score: 58
topics:
  - Graphs
  - Max Flow
  - Vertex Capacities
tags:
  - advanced-graphs
  - max-flow
  - vertex-capacity
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# AGR-002: Max Flow With Vertex Capacities

## Problem Statement

You are given a directed graph with edge capacities and **vertex capacities**. Compute the maximum flow from source `s` to sink `t` while respecting both edge and vertex limits.

A vertex with capacity `C` can carry at most `C` units of flow through it. The source and sink have unlimited capacity.

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767186940/dsa-problems/AGR-002/problem/cunfjp4k77gbrhhghgms.jpg)

## Input Format

- First line: integers `n`, `m`, `s`, `t`
- Second line: `n` integers `cap[i]` (`-1` means infinite capacity)
- Next `m` lines: `u v c` describing a directed edge `u -> v` with capacity `c`

## Output Format

- Single integer: maximum flow from `s` to `t`

## Constraints

- `2 <= n <= 2000`
- `0 <= m <= 5000`
- `0 <= c <= 10^9`
- `cap[i] = -1` or `0 <= cap[i] <= 10^9`
- `0 <= s, t < n`, `s != t`

## Example

**Input:**

```
4 3 0 3
-1 3 2 -1
0 1 3
1 2 2
2 3 3
```

**Output:**

```
2
```

**Explanation:**

Vertex 2 limits the flow to 2, so the max flow is 2.

![Example Visualization](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767186943/dsa-problems/AGR-002/problem/zssufeqz99vcroa175c6.jpg)

## Notes

- Split each vertex into `in` and `out` with an edge of its capacity.
- Use a max flow algorithm like Dinic on the transformed graph.
- Treat `cap[s]` and `cap[t]` as infinite.

## Related Topics

Max Flow, Vertex Capacities, Dinic

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long maxFlowVertexCap(int n, int s, int t, long[] cap, int[][] edges) {
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
        int s = sc.nextInt();
        int t = sc.nextInt();
        long[] cap = new long[n];
        for (int i = 0; i < n; i++) cap[i] = sc.nextLong();
        int[][] edges = new int[m][3];
        for (int i = 0; i < m; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
            edges[i][2] = sc.nextInt();
        }

        Solution solution = new Solution();
        System.out.println(solution.maxFlowVertexCap(n, s, t, cap, edges));
        sc.close();
    }
}
```

### Python

```python
def max_flow_vertex_cap(n: int, s: int, t: int, cap: list[int], edges: list[tuple[int, int, int]]) -> int:
    # Your implementation here
    return 0

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); s = int(next(it)); t = int(next(it))
    cap = [int(next(it)) for _ in range(n)]
    edges = []
    for _ in range(m):
        u = int(next(it)); v = int(next(it)); c = int(next(it))
        edges.append((u, v, c))
    print(max_flow_vertex_cap(n, s, t, cap, edges))

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
    long long maxFlowVertexCap(int n, int s, int t, const vector<long long>& cap,
                               const vector<array<int, 3>>& edges) {
        // Your implementation here
        return 0LL;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, s, t;
    if (!(cin >> n >> m >> s >> t)) return 0;
    vector<long long> cap(n);
    for (int i = 0; i < n; i++) cin >> cap[i];
    vector<array<int, 3>> edges(m);
    for (int i = 0; i < m; i++) {
        cin >> edges[i][0] >> edges[i][1] >> edges[i][2];
    }

    Solution solution;
    cout << solution.maxFlowVertexCap(n, s, t, cap, edges) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  maxFlowVertexCap(n, s, t, cap, edges) {
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
  const s = parseInt(data[idx++], 10);
  const t = parseInt(data[idx++], 10);
  const cap = new Array(n);
  for (let i = 0; i < n; i++) cap[i] = parseInt(data[idx++], 10);
  const edges = [];
  for (let i = 0; i < m; i++) {
    const u = parseInt(data[idx++], 10);
    const v = parseInt(data[idx++], 10);
    const c = parseInt(data[idx++], 10);
    edges.push([u, v, c]);
  }

  const solution = new Solution();
  console.log(solution.maxFlowVertexCap(n, s, t, cap, edges).toString());
});
```
