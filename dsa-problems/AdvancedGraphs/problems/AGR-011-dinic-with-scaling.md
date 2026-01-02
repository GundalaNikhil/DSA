---
problem_id: AGR_DINIC_WITH_SCALING__5083
display_id: AGR-011
slug: dinic-with-scaling
title: "Dinic With Scaling"
difficulty: Medium
difficulty_score: 56
topics:
  - Graphs
  - Max Flow
  - Scaling
tags:
  - advanced-graphs
  - max-flow
  - dinic
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# AGR-011: Dinic With Scaling

## Problem Statement

Compute the maximum flow in a directed graph using Dinic's algorithm with capacity scaling.

![Problem Illustration](../images/AGR-011/problem-illustration.png)

## Input Format

- First line: integers `n`, `m`, `s`, `t`
- Next `m` lines: `u v c` describing a directed edge `u -> v` with capacity `c`

## Output Format

- Single integer: maximum flow from `s` to `t`

## Constraints

- `2 <= n <= 5000`
- `0 <= m <= 20000`
- `0 <= c <= 10^9`
- `0 <= s, t < n`, `s != t`

## Example

**Input:**

```
4 4 0 3
0 1 10
0 2 5
1 3 7
2 3 8
```

**Output:**

```
12
```

**Explanation:**

The maximum flow sends 7 through node 1 and 5 through node 2.

![Example Visualization](../images/AGR-011/example-1.png)

## Notes

- Capacity scaling improves performance on large capacities.
- Use 64-bit integers for flow values.
- Dinic still works without scaling; scaling is an optimization.

## Related Topics

Max Flow, Dinic, Capacity Scaling

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long maxFlow(int n, int s, int t, int[][] edges) {
        // Implementation here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt(), m = sc.nextInt(), s = sc.nextInt(), t = sc.nextInt();
        int[][] edges = new int[m][3];
        for (int i = 0; i < m; i++) { edges[i][0] = sc.nextInt(); edges[i][1] = sc.nextInt(); edges[i][2] = sc.nextInt(); }
        System.out.println(new Solution().maxFlow(n, s, t, edges));
        sc.close();
    }
}
```

### Python

```python
import sys

def max_flow(n: int, s: int, t: int, edges: list[tuple[int, int, int]]) -> int:
    # Implementation here
    return 0

def main():
    data = sys.stdin.read().split()
    if not data: return
    it = iter(data)
    n, m, s, t = int(next(it)), int(next(it)), int(next(it)), int(next(it))
    edges = [(int(next(it)), int(next(it)), int(next(it))) for _ in range(m)]
    print(max_flow(n, s, t, edges))

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
    long long maxFlow(int n, int s, int t, const vector<array<int, 3>>& edges) {
        // Implementation here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n, m, s, t;
    if (!(cin >> n >> m >> s >> t)) return 0;
    vector<array<int, 3>> edges(m);
    for (int i = 0; i < m; i++) cin >> edges[i][0] >> edges[i][1] >> edges[i][2];
    cout << Solution().maxFlow(n, s, t, edges) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  maxFlow(n, s, t, edges) {
    /* Implementation */ return 0;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
let data = [];
rl.on("line", (line) => {
  for (const p of line.trim().split(/\s+/)) if (p) data.push(p);
});
rl.on("close", () => {
  let idx = 0;
  const n = parseInt(data[idx++], 10),
    m = parseInt(data[idx++], 10),
    s = parseInt(data[idx++], 10),
    t = parseInt(data[idx++], 10);
  const edges = [];
  for (let i = 0; i < m; i++)
    edges.push([
      parseInt(data[idx++], 10),
      parseInt(data[idx++], 10),
      parseInt(data[idx++], 10),
    ]);
  console.log(new Solution().maxFlow(n, s, t, edges).toString());
});
```
