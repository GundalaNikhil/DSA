---
problem_id: AGR_MIN_CUT_SMALL_GRAPH__4182
display_id: AGR-001
slug: min-cut-small-graph
title: "Minimum Cut on Small Graph"
difficulty: Medium
difficulty_score: 50
topics:
  - Graphs
  - Min Cut
  - Stoer-Wagner
tags:
  - advanced-graphs
  - min-cut
  - stoer-wagner
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# AGR-001: Minimum Cut on Small Graph

## Problem Statement

Given an undirected weighted graph with `n` nodes, compute the value of the **global minimum cut**. The cut value is the total weight of edges crossing between the two partitions.

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767185652/dsa-problems/AGR-001/problem/ngj17ehpuwgruaqgacaw.jpg)

## Input Format

- First line: integers `n` and `m`
- Next `m` lines: `u v w` describing an undirected edge with weight `w`

## Output Format

- Single integer: the minimum cut value

## Constraints

- `1 <= n <= 200`
- `0 <= m <= 2000`
- `0 <= w <= 10^9`
- `0 <= u, v < n`

## Example

**Input:**

```
4 4
0 1 1
1 2 2
2 3 1
0 3 2
```

**Output:**

```
2
```

**Explanation:**

One minimum cut separates `{0, 3}` from `{1, 2}`.
Edges crossing: `(0, 1)` (weight 1) and `(3, 2)` (weight 1).
Total cost: `1 + 1 = 2`.

![Example Visualization](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767185654/dsa-problems/AGR-001/problem/lhavu7kthroej0xvm6av.jpg)

## Notes

- The graph may be disconnected; then the minimum cut is 0.
- Use Stoer-Wagner for the global min-cut in `O(n^3)`.
- Use 64-bit integers for the cut value.

## Related Topics

Global Min-Cut, Stoer-Wagner, Graph Algorithms

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public long minCut(int n, int m, int[][] edges) {
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

        int[][] edges = new int[m][3];
        for (int i = 0; i < m; i++) {
            parts = br.readLine().trim().split("\\s+");
            edges[i][0] = Integer.parseInt(parts[0]);
            edges[i][1] = Integer.parseInt(parts[1]);
            edges[i][2] = Integer.parseInt(parts[2]);
        }

        Solution sol = new Solution();
        System.out.println(sol.minCut(n, m, edges));
    }
}
```

### Python

```python
import sys

class Solution:
    def min_cut(self, n, m, edges):
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
        edges = []
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            w = int(next(iterator))
            edges.append([u, v, w])
    except StopIteration:
        pass

    sol = Solution()
    print(sol.min_cut(n, m, edges))

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
    long long minCut(int n, int m, vector<vector<int>>& edges) {
        // Implement here
        return 0;
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
    cout << sol.minCut(n, m, edges) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  minCut(n, m, edges) {
    // Implement here
    return 0;
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
  console.log(sol.minCut(n, m, edges));
}

solve();
```
