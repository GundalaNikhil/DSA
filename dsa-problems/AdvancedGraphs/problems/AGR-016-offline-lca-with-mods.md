---
problem_id: AGR_OFFLINE_LCA_WITH_MODS__9025
display_id: AGR-016
slug: offline-lca-with-mods
title: "Offline Lowest Common Ancestor with Modifications"
difficulty: Hard
difficulty_score: 72
topics:
  - Graphs
  - Trees
  - LCA
tags:
  - advanced-graphs
  - lca
  - offline
  - hard
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# AGR-016: Offline Lowest Common Ancestor with Modifications

## Problem Statement

You are given an initial tree on `n` nodes rooted at node `0`. Then you must process a sequence of operations:

- `cut u v`: remove the edge between `u` and `v`
- `link u v`: add an edge between `u` and `v`
- `query u v`: output the LCA of `u` and `v` in the current tree
  If `u` and `v` are not connected, output `-1`.
  All operations are valid, and the active edge set always forms a forest.
  ![Problem Illustration](../images/AGR-016/problem-illustration.png)

## Input Format

- First line: integer `n`
- Next `n-1` lines: `u v` edges of the initial tree
- Next line: integer `q`
- Next `q` lines: one of the operations above

## Output Format

- For each `query`, print the LCA value on its own line

## Constraints

- `1 <= n <= 200000`
- `1 <= q <= 200000`
- `0 <= u, v < n`
- Operations are valid and keep the active edges acyclic

## Example

**Input:**

```
4
0 1
1 2
1 3
4
query 2 3
cut 1 3
query 2 3
link 1 3
```

**Output:**

```
1
-1
```

**Explanation:**
Initially, LCA(2,3)=1. After removing edge (1,3), nodes 2 and 3 are disconnected.
![Example Visualization](../images/AGR-016/example-1.png)

## Notes

- Solve offline using a segment tree over time for edge activation intervals.
- Use DSU rollback for dynamic connectivity, and binary lifting for LCA in the base tree.
- Treat LCA as undefined if nodes are disconnected.

## Related Topics

## LCA, DSU Rollback, Offline Queries

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public List<Integer> solveOffline(int n, int[][] initialEdges, int q, String[][] queries) {
        // Implement here
        return new ArrayList<>();
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        if (line == null) return;
        int n = Integer.parseInt(line.trim());

        int[][] initialEdges = new int[n - 1][2];
        for (int i = 0; i < n - 1; i++) {
            line = br.readLine();
            String[] parts = line.trim().split("\\s+");
            initialEdges[i][0] = Integer.parseInt(parts[0]);
            initialEdges[i][1] = Integer.parseInt(parts[1]);
        }

        line = br.readLine();
        int q = Integer.parseInt(line.trim());

        String[][] queries = new String[q][3];
        for (int i = 0; i < q; i++) {
            line = br.readLine();
            queries[i] = line.trim().split("\\s+");
        }

        Solution sol = new Solution();
        List<Integer> result = sol.solveOffline(n, initialEdges, q, queries);

        for (int val : result) {
            System.out.println(val);
        }
    }
}
```

### Python

```python
import sys

# Increase recursion depth for deep trees
sys.setrecursionlimit(200005)

class Solution:
    def solve_offline(self, n, initial_edges, q, queries):
        # Implement here
        return []

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        initial_edges = []
        for _ in range(n - 1):
            u = int(next(iterator))
            v = int(next(iterator))
            initial_edges.append([u, v])

        q = int(next(iterator))
        queries = []
        for _ in range(q):
            type = next(iterator)
            u = next(iterator)
            v = next(iterator)
            queries.append([type, u, v])

    except StopIteration:
        pass

    sol = Solution()
    result = sol.solve_offline(n, initial_edges, q, queries)

    for val in result:
        print(val)

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> solveOffline(int n, vector<vector<int>>& initialEdges, int q, vector<vector<string>>& queries) {
        // Implement here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<int>> initialEdges(n - 1, vector<int>(2));
    for (int i = 0; i < n - 1; i++) {
        cin >> initialEdges[i][0] >> initialEdges[i][1];
    }

    int q;
    cin >> q;

    vector<vector<string>> queries(q, vector<string>(3));
    for (int i = 0; i < q; i++) {
        cin >> queries[i][0] >> queries[i][1] >> queries[i][2];
    }

    Solution sol;
    vector<int> result = sol.solveOffline(n, initialEdges, q, queries);

    for (int val : result) {
        cout << val << endl;
    }

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  solveOffline(n, initialEdges, q, queries) {
    // Implement here
    return [];
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 1) return;

  let idx = 0;
  function readInt() {
    return parseInt(input[idx++]);
  }
  function readString() {
    return input[idx++];
  }

  const n = readInt();
  const initialEdges = [];
  for (let i = 0; i < n - 1; i++) {
    const u = readInt();
    const v = readInt();
    initialEdges.push([u, v]);
  }

  const q = readInt();
  const queries = [];
  for (let i = 0; i < q; i++) {
    const type = readString();
    const u = readString();
    const v = readString();
    queries.push([type, u, v]);
  }

  const sol = new Solution();
  const result = sol.solveOffline(n, initialEdges, q, queries);

  result.forEach((val) => console.log(val));
}

solve();
```
