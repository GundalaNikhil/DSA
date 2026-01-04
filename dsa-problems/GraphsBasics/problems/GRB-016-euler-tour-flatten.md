---
problem_id: GRB_EULER_TOUR_FLATTEN__5068
display_id: GRB-016
slug: euler-tour-flatten
title: "Euler Tour of Tree (Array Flatten)"
difficulty: Medium
difficulty_score: 44
topics:
  - Graphs
  - Trees
  - DFS
  - Euler Tour
tags:
  - graphs-basics
  - euler-tour
  - dfs
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRB-016: Euler Tour of Tree (Array Flatten)

## Problem Statement

You are given a rooted tree with `n` nodes. Produce the entry time `tin[u]` and exit time `tout[u]` for each node using a DFS Euler tour. The subtree of `u` corresponds to the contiguous range `[tin[u], tout[u]]` in the Euler order.

![Problem Illustration](../images/GRB-016/problem-illustration.png)

## Input Format

- First line: integer `n`
- Next `n-1` lines: `u v` describing an undirected edge
- Last line: integer `r`, the root node

## Output Format

- Line 1: `n` integers `tin[0..n-1]`
- Line 2: `n` integers `tout[0..n-1]`

## Constraints

- `1 <= n <= 200000`
- `0 <= u, v, r < n`

## Example

**Input:**

```
3
0 1
0 2
0
```

**Output:**

```
0 1 2
2 1 2
```

**Explanation:**

A DFS from root 0 visits nodes in order 0,1,2. The subtree of 0 covers indices 0..2.

![Example Visualization](../images/GRB-016/example-1.png)

## Notes

- Use a global timer that increments on entry.
- `tout[u]` is the last time index inside `u`'s subtree.
- The exact times depend on DFS order; any valid Euler tour is accepted.

## Related Topics

Euler Tour, Tree Flattening, DFS

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public void eulerTour(int n, List<List<Integer>> adj, int root, int[] tin, int[] tout) {
        // Implement here
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String nLine = br.readLine();
        if (nLine == null) return;
        int n = Integer.parseInt(nLine.trim());

        List<List<Integer>> adj = new ArrayList<>(n);
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());

        for (int i = 0; i < n - 1; i++) {
            String[] edge = br.readLine().trim().split("\\s+");
            int u = Integer.parseInt(edge[0]);
            int v = Integer.parseInt(edge[1]);
            adj.get(u).add(v);
            adj.get(v).add(u);
        }

        String rLine = br.readLine();
        if (rLine == null) return;
        int r = Integer.parseInt(rLine.trim());

        int[] tin = new int[n];
        int[] tout = new int[n];
        Solution sol = new Solution();
        sol.eulerTour(n, adj, r, tin, tout);

        PrintWriter out = new PrintWriter(System.out);
        for (int i = 0; i < n; i++) {
            out.print(tin[i] + (i == n - 1 ? "" : " "));
        }
        out.println();
        for (int i = 0; i < n; i++) {
            out.print(tout[i] + (i == n - 1 ? "" : " "));
        }
        out.println();
        out.flush();
    }
}
```

### Python

```python
import sys

# Increase recursion depth for deep DFS (tree) trees
sys.setrecursionlimit(300000)

class Solution:
    def euler_tour(self, n, adj, root, tin, tout):
        # Implement here
        pass

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    adj = [[] for _ in range(n)]
    idx = 1
    for _ in range(n - 1):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2

    r = int(input_data[idx])

    tin = [0] * n
    tout = [0] * n
    sol = Solution()
    sol.euler_tour(n, adj, r, tin, tout)

    print(*(tin))
    print(*(tout))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    void eulerTour(int n, vector<vector<int>>& adj, int root, vector<int>& tin, vector<int>& tout) {
        // Implement here
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<int>> adj(n);
    for (int i = 0; i < n - 1; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    int r;
    cin >> r;

    vector<int> tin(n), tout(n);
    Solution sol;
    sol.eulerTour(n, adj, r, tin, tout);

    for (int i = 0; i < n; i++) {
        cout << tin[i] << (i == n - 1 ? "" : " ");
    }
    cout << endl;
    for (int i = 0; i < n; i++) {
        cout << tout[i] << (i == n - 1 ? "" : " ");
    }
    cout << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  eulerTour(n, adj, root, tin, tout) {
    // Implement here
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 1) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const adj = Array.from({ length: n }, () => []);
  for (let i = 0; i < n - 1; i++) {
    const u = parseInt(input[idx++]);
    const v = parseInt(input[idx++]);
    adj[u].push(v);
    adj[v].push(u);
  }

  const r = parseInt(input[idx++]);
  const tin = new Array(n).fill(0);
  const tout = new Array(n).fill(0);

  const sol = new Solution();
  sol.eulerTour(n, adj, r, tin, tout);

  console.log(tin.join(" "));
  console.log(tout.join(" "));
}

solve();
```
