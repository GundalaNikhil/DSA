---
title: Tree DP for Vertex Cover
problem_id: TDP_TREE_VERTEX_COVER__7514
display_id: TDP-006
difficulty: Medium
time_limit: 2000
memory_limit: 256
tags:
  - Tree DP
  - Graph Theory
  - Optimization
categories:
  - Algorithms
  - Data Structures
slug: tree-vertex-cover
---

# Tree DP for Vertex Cover

## Problem Description

Given a tree with `n` nodes, find the size of the **minimum vertex cover**.

A vertex cover is a set of vertices such that every edge in the tree has at least one of its endpoints in the set.

## Input Format

- First line: integer `n` (number of nodes)
- Next `n-1` lines: each contains two integers `u v` representing an edge

## Output Format

- Single integer: the size of the minimum vertex cover

## Constraints

- `1 <= n <= 2 x 10^5`
- `1 <= u, v <= n`
- The graph forms a valid tree

## Example 1

**Input:**

```
3
1 2
1 3
```

**Output:**

```
1
```

**Explanation:**
Tree structure:

```
  1
 / \
2   3
```

Vertex cover = {1} covers both edges (1-2) and (1-3).
Size = 1 (minimum possible).

## Example 2

**Input:**

```
4
1 2
2 3
3 4
```

**Output:**

```
2
```

**Explanation:**
Tree structure: 1 -- 2 -- 3 -- 4

Possible minimum vertex covers:

- {2, 3} covers edges (1-2), (2-3), and (3-4)
- Size = 2

Alternatively: {1, 3} or {2, 4} also work.

## Solution Template

### Java

```java
import java.util.*;

class Main {
    static class Edge {
        int to;
        Edge(int to) {
            this.to = to;
        }
    }

    static List<Edge>[] graph;
    static int[][] dp;
    static int n;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();

        graph = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < n - 1; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            graph[u].add(new Edge(v));
            graph[v].add(new Edge(u));
        }

        dp = new int[n + 1][2];

        dfs(1, -1);

        int result = Math.min(dp[1][0], dp[1][1]);
        System.out.println(result);

        sc.close();
    }

    static void dfs(int u, int parent) {
        dp[u][0] = 0;  // Not including u
        dp[u][1] = 1;  // Including u

        for (Edge e : graph[u]) {
            int v = e.to;
            if (v == parent) continue;

            dfs(v, u);

            // If u is not included, all children must be included
            dp[u][0] += dp[v][1];

            // If u is included, children can be included or not
            dp[u][1] += Math.min(dp[v][0], dp[v][1]);
        }
    }
}
```

### Python

```python
import sys
sys.setrecursionlimit(300000)

def solve():
    return 0
solve()

def main():
    import sys
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    # TODO: Parse input and call solution
    pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <cmath>
#include <cstring>
#include <climits>
using namespace std;

const int MAXN = 200005;
vector<int> graph[MAXN];
int dp[MAXN][2];
int n;

void dfs(int u, int parent) {
    dp[u][0] = 0;  // Not including u
    dp[u][1] = 1;  // Including u

    for (int v : graph[u]) {
        if (v == parent) continue;

        dfs(v, u);

        // If u not included, all children must be included
        dp[u][0] += dp[v][1];

        // If u included, take minimum for each child
        dp[u][1] += min(dp[v][0], dp[v][1]);
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n;

    for (int i = 0; i < n - 1; i++) {
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    dfs(1, -1);

    int result = min(dp[1][0], dp[1][1]);
    cout << result << endl;

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let lines = [];
rl.on("line", (line) => {
  lines.push(line);
}).on("close", () => {
  solve();
});

function solve() {
    return 0;
  }
  function dfs(u, parent) {
    return 0;
  }

  dfs(1, -1);

  const result = Math.min(dp[1][0], dp[1][1]);
  console.log(result);
}
```

