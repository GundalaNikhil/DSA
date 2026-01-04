---
problem_id: AGR_APSP_WITH_NEGATIVES__6027
display_id: AGR-004
slug: apsp-with-negatives
title: "All-Pairs Shortest Path With Negative Edges"
difficulty: Medium
difficulty_score: 58
topics:
  - Graphs
  - APSP
  - Johnson
tags:
  - advanced-graphs
  - apsp
  - johnson
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# AGR-004: All-Pairs Shortest Path With Negative Edges

## Problem Statement

Given a directed weighted graph with no negative cycles, compute the shortest path distance between every pair of nodes.

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767187669/dsa-problems/AGR-004/problem/nii8p5fuu2xwkypthout.jpg)

## Input Format

- First line: integers `n` and `m`
- Next `m` lines: `u v w` describing a directed edge `u -> v` with weight `w`

## Output Format

- Print `n` lines, each with `n` entries
- Use `INF` for unreachable pairs

## Constraints

- `1 <= n <= 2000`
- `0 <= m <= 5000`
- `-10^9 <= w <= 10^9`
- The graph has no negative cycles

## Example

**Input:**

```
3 3
0 1 2
1 2 -1
0 2 4
```

**Output:**

```
0 2 1
INF 0 -1
INF INF 0
```

**Explanation:**

The shortest path from 0 to 2 goes through 1 with total cost 1.

![Example Visualization](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767187671/dsa-problems/AGR-004/problem/mpmwtfgxrk0cjmjldfs0.jpg)

## Notes

- Johnson's algorithm runs Bellman-Ford once, then Dijkstra from each node.
- Use 64-bit integers to avoid overflow.
- `INF` is only for unreachable; negative distances can occur.

## Related Topics

APSP, Johnson, Dijkstra

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public long[][] apsp(int n, int m, int[][] edges) {
        // Implement here
        return new long[0][0];
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

        int[][] edges = new int[m][3];
        for (int i = 0; i < m; i++) {
            parts = br.readLine().trim().split("\\s+");
            edges[i][0] = Integer.parseInt(parts[0]);
            edges[i][1] = Integer.parseInt(parts[1]);
            edges[i][2] = Integer.parseInt(parts[2]);
        }

        Solution sol = new Solution();
        long[][] result = sol.apsp(n, m, edges);

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (result[i][j] == Long.MAX_VALUE) sb.append("INF");
                else sb.append(result[i][j]);
                sb.append(j == n - 1 ? "" : " ");
            }
            sb.append("\n");
        }
        System.out.print(sb);
    }
}
```

### Python

```python
import sys

class Solution:
    def apsp(self, n, m, edges):
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
            w = int(next(iterator))
            edges.append([u, v, w])
    except StopIteration:
        pass

    sol = Solution()
    result = sol.apsp(n, m, edges)

    for row in result:
        print(*(row))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

class Solution {
public:
    vector<vector<long long>> apsp(int n, int m, vector<vector<int>>& edges) {
        // Implement here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<int>> edges(m, vector<int>(3));
    for (int i = 0; i < m; i++) {
        cin >> edges[i][0] >> edges[i][1] >> edges[i][2];
    }

    Solution sol;
    vector<vector<long long>> result = sol.apsp(n, m, edges);

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (result[i][j] == LLONG_MAX) cout << "INF";
            else cout << result[i][j];
            cout << (j == n - 1 ? "" : " ");
        }
        cout << "\n";
    }

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  apsp(n, m, edges) {
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
    const w = readInt();
    edges.push([u, v, w]);
  }

  const sol = new Solution();
  const result = sol.apsp(n, m, edges);

  result.forEach((row) => {
    console.log(row.join(" "));
  });
}

solve();
```
