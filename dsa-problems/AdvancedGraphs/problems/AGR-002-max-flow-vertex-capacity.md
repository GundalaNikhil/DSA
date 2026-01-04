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
import java.io.*;

class Solution {
    public long maxFlowVertexCap(int n, int m, int s, int t, int[] caps, int[][] edges) {
        // Implement here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        if (line == null) return;
        String[] parts = line.trim().split("\\s+");
        int n = Integer.parseInt(parts[0]);
        int m = Integer.parseInt(parts[1]);
        int s = Integer.parseInt(parts[2]);
        int t = Integer.parseInt(parts[3]);

        int[] caps = new int[n];
        line = br.readLine();
        if (line != null) {
            parts = line.trim().split("\\s+");
            for (int i = 0; i < n; i++) {
                caps[i] = Integer.parseInt(parts[i]);
            }
        }

        int[][] edges = new int[m][3];
        for (int i = 0; i < m; i++) {
            parts = br.readLine().trim().split("\\s+");
            edges[i][0] = Integer.parseInt(parts[0]);
            edges[i][1] = Integer.parseInt(parts[1]);
            edges[i][2] = Integer.parseInt(parts[2]);
        }

        Solution sol = new Solution();
        System.out.println(sol.maxFlowVertexCap(n, m, s, t, caps, edges));
    }
}
```

### Python

```python
import sys

class Solution:
    def max_flow_vertex_cap(self, n, m, s, t, caps, edges):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        s = int(next(iterator))
        t = int(next(iterator))

        caps = []
        for _ in range(n):
            caps.append(int(next(iterator)))

        edges = []
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            cap = int(next(iterator))
            edges.append([u, v, cap])

    except StopIteration:
        pass

    sol = Solution()
    print(sol.max_flow_vertex_cap(n, m, s, t, caps, edges))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    long long maxFlowVertexCap(int n, int m, int s, int t, vector<int>& caps, vector<vector<int>>& edges) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m, s, t;
    if (!(cin >> n >> m >> s >> t)) return 0;

    vector<int> caps(n);
    for (int i = 0; i < n; i++) {
        cin >> caps[i];
    }

    vector<vector<int>> edges(m, vector<int>(3));
    for (int i = 0; i < m; i++) {
        cin >> edges[i][0] >> edges[i][1] >> edges[i][2];
    }

    Solution sol;
    cout << sol.maxFlowVertexCap(n, m, s, t, caps, edges) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  maxFlowVertexCap(n, m, s, t, caps, edges) {
    // Implement here
    return 0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 4) return;

  let idx = 0;
  function readInt() {
    return parseInt(input[idx++]);
  }

  const n = readInt();
  const m = readInt();
  const s = readInt();
  const t = readInt();

  const caps = [];
  for (let i = 0; i < n; i++) caps.push(readInt());

  const edges = [];
  for (let i = 0; i < m; i++) {
    const u = readInt();
    const v = readInt();
    const c = readInt();
    edges.push([u, v, c]);
  }

  const sol = new Solution();
  console.log(sol.maxFlowVertexCap(n, m, s, t, caps, edges));
}

solve();
```
