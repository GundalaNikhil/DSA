---
problem_id: GRB_BELLMAN_FORD__3812
display_id: GRB-004
slug: bellman-ford
title: "Bellman-Ford with Negative Edges"
difficulty: Medium
difficulty_score: 50
topics:
  - Graphs
  - Shortest Path
  - Bellman-Ford
tags:
  - graphs-basics
  - bellman-ford
  - shortest-path
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# GRB-004: Bellman-Ford with Negative Edges

## Problem Statement

You are given a directed graph that may contain negative edge weights. Compute shortest distances from a source node `s`.

If a negative cycle is reachable from `s`, output `NEGATIVE CYCLE`.

![Problem Illustration](../images/GRB-004/problem-illustration.png)

## Input Format

- First line: integers `n`, `m`, and `s`
- Next `m` lines: `u v w` describing a directed edge `u -> v` with weight `w`

## Output Format

- If a reachable negative cycle exists: print `NEGATIVE CYCLE`
- Otherwise: print `n` integers, the distances from `s` to nodes `0..n-1` (`-1` if unreachable)

## Constraints

- `1 <= n <= 10000`
- `0 <= m <= 50000`
- `-10^9 <= w <= 10^9`
- `0 <= s < n`

## Example

**Input:**

```
2 2 0
0 1 -1
1 0 -1
```

**Output:**

```
NEGATIVE CYCLE
```

**Explanation:**

The cycle `0 -> 1 -> 0` has total weight `-2` and is reachable from the source.

![Example Visualization](../images/GRB-004/example-1.png)

## Notes

- Run `n-1` relaxations, then one extra pass to detect negative cycles.
- Distances should use 64-bit integers.
- Unreachable nodes keep distance `-1`.

## Related Topics

Bellman-Ford, Shortest Path, Negative Cycles

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long[] bellmanFord(int n, int s, int[][] edges) {
        // Your implementation here
        return new long[n];
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        int s = sc.nextInt();
        int[][] edges = new int[m][3];
        for (int i = 0; i < m; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
            edges[i][2] = sc.nextInt();
        }

        Solution solution = new Solution();
        long[] dist = solution.bellmanFord(n, s, edges);
        if (dist == null) {
            System.out.print("NEGATIVE CYCLE");
        } else {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < n; i++) {
                if (i > 0) sb.append(' ');
                sb.append(dist[i]);
            }
            System.out.print(sb.toString());
        }
        sc.close();
    }
}
```

### Python

```python
def bellman_ford(n: int, s: int, edges: list[tuple[int, int, int]]):
    # Your implementation here
    return [0] * n

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); s = int(next(it))
    edges = []
    for _ in range(m):
        u = int(next(it)); v = int(next(it)); w = int(next(it))
        edges.append((u, v, w))
    dist = bellman_ford(n, s, edges)
    if dist is None:
        sys.stdout.write("NEGATIVE CYCLE")
    else:
        sys.stdout.write(" ".join(str(x) for x in dist))

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
    vector<long long> bellmanFord(int n, int s, const vector<array<int, 3>>& edges) {
        // Your implementation here
        return vector<long long>(n, 0LL);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, s;
    if (!(cin >> n >> m >> s)) return 0;
    vector<array<int, 3>> edges(m);
    for (int i = 0; i < m; i++) {
        cin >> edges[i][0] >> edges[i][1] >> edges[i][2];
    }

    Solution solution;
    vector<long long> dist = solution.bellmanFord(n, s, edges);
    if (dist.empty()) {
        cout << "NEGATIVE CYCLE";
    } else {
        for (int i = 0; i < n; i++) {
            if (i) cout << ' ';
            cout << dist[i];
        }
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  bellmanFord(n, s, edges) {
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
  const s = parseInt(data[idx++], 10);
  const edges = [];
  for (let i = 0; i < m; i++) {
    const u = parseInt(data[idx++], 10);
    const v = parseInt(data[idx++], 10);
    const w = parseInt(data[idx++], 10);
    edges.push([u, v, w]);
  }

  const solution = new Solution();
  const dist = solution.bellmanFord(n, s, edges);
  if (dist === null || dist.length === 0) {
    console.log("NEGATIVE CYCLE");
  } else {
    console.log(dist.join(" "));
  }
});
```
