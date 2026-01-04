---
problem_id: AGR_EULERIAN_TRAIL_DIRECTED__4836
display_id: AGR-007
slug: eulerian-trail-directed
title: "Eulerian Trail With Directed Edges"
difficulty: Medium
difficulty_score: 48
topics:
  - Graphs
  - Eulerian Path
  - DFS
tags:
  - advanced-graphs
  - eulerian
  - hierholzer
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# AGR-007: Eulerian Trail With Directed Edges

## Problem Statement

Determine whether a directed graph has an Eulerian trail (a path that uses every edge exactly once). If it exists, output one such trail.

![Problem Illustration](../images/AGR-007/problem-illustration.png)

## Input Format

- First line: integers `n` and `m`
- Next `m` lines: `u v` describing a directed edge `u -> v`

## Output Format

- If no Eulerian trail exists: print `NO`
- Otherwise: print `YES` and then one line with the trail as a sequence of `m+1` nodes

## Constraints

- `1 <= n <= 100000`
- `0 <= m <= 200000`
- `0 <= u, v < n`

## Example

**Input:**

```
3 3
0 1
1 2
2 0
```

**Output:**

```
YES
0 1 2 0
```

**Explanation:**

The cycle uses each directed edge exactly once.

![Example Visualization](../images/AGR-007/example-1.png)

## Notes

- A directed Euler trail exists if at most one node has out-in = 1 and at most one node has in-out = 1, and all edges are in one weakly connected component.
- Use Hierholzer's algorithm to construct the trail.
- If `m=0`, output `YES` and any single node (e.g., 0).

## Related Topics

Eulerian Path, Hierholzer, Graph Traversal

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public List<Integer> findEulerianTrail(int n, int m, int[][] edges) {
        // Implement here
        return null;
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
        List<Integer> result = sol.findEulerianTrail(n, m, edges);

        if (result == null) {
            System.out.println("NO");
        } else {
            System.out.println("YES");
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < result.size(); i++) {
                sb.append(result.get(i)).append(i == result.size() - 1 ? "" : " ");
            }
            System.out.println(sb);
        }
    }
}
```

### Python

```python
import sys

# Increase recursion depth for deep recursion in Hierholzer
sys.setrecursionlimit(200005)

class Solution:
    def find_eulerian_trail(self, n, m, edges):
        # Implement here
        return None

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
    result = sol.find_eulerian_trail(n, m, edges)

    if result is None:
        print("NO")
    else:
        print("YES")
        print(*(result))

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

    vector<int> findEulerianTrail(int n, int m, vector<vector<int>>& edges) {
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
    vector<int> result = sol.findEulerianTrail(n, m, edges);

    if (result.empty()) {
        cout << "NO" << endl;
    } else {
        cout << "YES" << endl;
        for (int i = 0; i < result.size(); i++) {
            cout << result[i] << (i == result.size() - 1 ? "" : " ");
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
  findEulerianTrail(n, m, edges) {
    // Implement here
    return null;
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
  const result = sol.findEulerianTrail(n, m, edges);

  if (result === null) {
    console.log("NO");
  } else {
    console.log("YES");
    console.log(result.join(" "));
  }
}

solve();
```
