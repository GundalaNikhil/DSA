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
import java.io.*;

class Solution {
    public String bellmanFord(int n, int m, int s, List<Edge> edges) {
        // Implement here
        return "";
    }

    static class Edge {
        int u, v;
        long w;
        Edge(int u, int v, long w) {
            this.u = u;
            this.v = v;
            this.w = w;
        }
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String nmsLine = br.readLine();
        if (nmsLine == null) return;
        String[] nms = nmsLine.trim().split("\\s+");
        int n = Integer.parseInt(nms[0]);
        int m = Integer.parseInt(nms[1]);
        int s = Integer.parseInt(nms[2]);

        List<Solution.Edge> edges = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            String[] edgeLine = br.readLine().trim().split("\\s+");
            int u = Integer.parseInt(edgeLine[0]);
            int v = Integer.parseInt(edgeLine[1]);
            long w = Long.parseLong(edgeLine[2]);
            edges.add(new Solution.Edge(u, v, w));
        }

        Solution sol = new Solution();
        System.out.println(sol.bellmanFord(n, m, s, edges));
    }
}
```

### Python

```python
import sys

class Solution:
    def bellman_ford(self, n, m, s, edges):
        # Implement here
        return ""

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])
    s = int(input_data[2])

    edges = []
    idx = 3
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        w = int(input_data[idx+2])
        edges.append((u, v, w))
        idx += 3

    sol = Solution()
    print(sol.bellman_ford(n, m, s, edges))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

struct Edge {
    int u, v;
    long long w;
};

class Solution {
public:
    string bellmanFord(int n, int m, int s, vector<Edge>& edges) {
        // Implement here
        return "";
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m, s;
    if (!(cin >> n >> m >> s)) return 0;

    vector<Edge> edges(m);
    for (int i = 0; i < m; i++) {
        cin >> edges[i].u >> edges[i].v >> edges[i].w;
    }

    Solution sol;
    cout << sol.bellmanFord(n, m, s, edges) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  bellmanFord(n, m, s, edges) {
    // Implement here
    return "";
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 3) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const m = parseInt(input[idx++]);
  const s = parseInt(input[idx++]);

  const edges = [];
  for (let i = 0; i < m; i++) {
    const u = parseInt(input[idx++]);
    const v = parseInt(input[idx++]);
    const w = BigInt(input[idx++]);
    edges.push({ u, v, w });
  }

  const sol = new Solution();
  console.log(sol.bellmanFord(n, m, s, edges));
}

solve();
```
