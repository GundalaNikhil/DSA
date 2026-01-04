---
problem_id: AGR_DIRECTED_CYCLE_BASIS__8240
display_id: AGR-015
slug: directed-cycle-basis
title: "Directed Cycle Basis"
difficulty: Hard
difficulty_score: 72
topics:
  - Graphs
  - Cycle Basis
  - Spanning Forest
tags:
  - advanced-graphs
  - cycle-basis
  - directed
  - hard
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# AGR-015: Directed Cycle Basis

## Problem Statement

Given a directed graph, output a cycle basis of size `m - n + c`, where `c` is the number of connected components in the underlying undirected graph.

Each cycle should be a simple directed cycle. Any valid basis is accepted.

![Problem Illustration](../images/AGR-015/problem-illustration.png)

## Input Format

- First line: integers `n` and `m`
- Next `m` lines: `u v` describing a directed edge `u -> v`

## Output Format

- Line 1: integer `b`, number of cycles output
- Next `b` lines: each cycle as `k v1 v2 ... vk` where `v1 == vk` (cycle closed)

## Constraints

- `1 <= n <= 500`
- `0 <= m <= 2000`
- `0 <= u, v < n`

## Example

**Input:**

```
4 5
0 1
1 2
2 0
1 3
3 1
```

**Output:**

```
2
4 0 1 2 0
3 1 3 1
```

**Explanation:**

Two independent directed cycles are shown. This is a valid basis.

![Example Visualization](../images/AGR-015/example-1.png)

## Notes

- Build a spanning forest on the underlying undirected graph.
- Each non-tree edge creates a fundamental cycle via parent pointers.
- Any valid basis size is accepted.

## Related Topics

Cycle Basis, Spanning Forest, Graph Theory

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public List<List<Integer>> findCycleBasis(int n, int m, int[][] edges) {
        // Implement here
        return new ArrayList<>();
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

        int[][] edges = new int[m][2];
        for (int i = 0; i < m; i++) {
            line = br.readLine();
            if (line == null) break;
            parts = line.trim().split("\\s+");
            edges[i][0] = Integer.parseInt(parts[0]);
            edges[i][1] = Integer.parseInt(parts[1]);
        }

        Solution sol = new Solution();
        List<List<Integer>> result = sol.findCycleBasis(n, m, edges);

        System.out.println(result.size());
        for (List<Integer> cycle : result) {
            StringBuilder sb = new StringBuilder();
            sb.append(cycle.size());
            for (int u : cycle) {
                sb.append(" ").append(u);
            }
            System.out.println(sb);
        }
    }
}
```

### Python

```python
import sys

# Increase recursion depth for DFS
sys.setrecursionlimit(200005)

class Solution:
    def find_cycle_basis(self, n, m, edges):
        # Implement here
        return []

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        edges = []
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            edges.append([u, v])

    except StopIteration:
        pass

    sol = Solution()
    result = sol.find_cycle_basis(n, m, edges)

    print(len(result))
    for cycle in result:
        print(len(cycle), end=" ")
        print(*(cycle))

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
    vector<vector<int>> findCycleBasis(int n, int m, vector<vector<int>>& edges) {
        // Implement here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<int>> edges(m, vector<int>(2));
    for (int i = 0; i < m; i++) {
        cin >> edges[i][0] >> edges[i][1];
    }

    Solution sol;
    vector<vector<int>> result = sol.findCycleBasis(n, m, edges);

    cout << result.size() << endl;
    for (const auto& cycle : result) {
        cout << cycle.size();
        for (int u : cycle) {
            cout << " " << u;
        }
        cout << endl;
    }

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  findCycleBasis(n, m, edges) {
    // Implement here
    return [];
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;

  let idx = 0;
  function readInt() {
    return parseInt(input[idx++]);
  }

  const n = readInt();
  const m = readInt();
  const edges = [];
  for (let i = 0; i < m; i++) {
    const u = readInt();
    const v = readInt();
    edges.push([u, v]);
  }

  const sol = new Solution();
  const result = sol.findCycleBasis(n, m, edges);

  console.log(result.length);
  result.forEach((cycle) => {
    console.log(cycle.length + " " + cycle.join(" "));
  });
}

solve();
```
