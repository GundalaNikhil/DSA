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
        int[][] edges = new int[m][3];
        for (int i = 0; i < m; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
            edges[i][2] = sc.nextInt();
        }

        Solution solution = new Solution();
        System.out.println(solution.maxFlow(n, s, t, edges));
        sc.close();
    }
}
```

### Python

```python
def max_flow(n: int, s: int, t: int, edges: list[tuple[int, int, int]]) -> int:
    # Your implementation here
    return 0

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); s = int(next(it)); t = int(next(it))
    edges = []
    for _ in range(m):
        u = int(next(it)); v = int(next(it)); c = int(next(it))
        edges.append((u, v, c))
    print(max_flow(n, s, t, edges))

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
    long long maxFlow(int n, int s, int t, const vector<array<int, 3>>& edges) {
        // Your implementation here
        return 0LL;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, s, t;
    if (!(cin >> n >> m >> s >> t)) return 0;
    vector<array<int, 3>> edges(m);
    for (int i = 0; i < m; i++) {
        cin >> edges[i][0] >> edges[i][1] >> edges[i][2];
    }

    Solution solution;
    cout << solution.maxFlow(n, s, t, edges) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  maxFlow(n, s, t, edges) {
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
  const edges = [];
  for (let i = 0; i < m; i++) {
    const u = parseInt(data[idx++], 10);
    const v = parseInt(data[idx++], 10);
    const c = parseInt(data[idx++], 10);
    edges.push([u, v, c]);
  }

  const solution = new Solution();
  console.log(solution.maxFlow(n, s, t, edges).toString());
});
```
