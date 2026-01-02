---
title: Max Path Sum with Length Limit
problem_id: TDP_MAX_PATH_SUM_LENGTH_LIMIT__6382
display_id: TDP-005
difficulty: Medium
time_limit: 2000
memory_limit: 256
tags:
  - Tree DP
  - Path Algorithms
  - Constrained Optimization
categories:
  - Algorithms
  - Data Structures
slug: max-path-sum-length-limit
---

# Max Path Sum with Length Limit

## Problem Description

You are given a tree with `n` nodes where each node has a value (possibly negative). Find the maximum path sum where the path uses **at most `L` edges**.

A path is a sequence of distinct nodes where consecutive nodes are connected by an edge. The path sum is the sum of all node values in the path.

## Input Format

- First line: two integers `n` and `L` (number of nodes and maximum path length in edges)
- Second line: `n` space-separated integers representing node values `value[1], value[2], ..., value[n]`
- Next `n-1` lines: each contains two integers `u v` representing an edge between nodes `u` and `v`

## Output Format

- Single integer: the maximum path sum using at most `L` edges

## Constraints

- `1 <= n <= 2 x 10^5`
- `1 <= L <= n-1`
- `-10^9 <= value[i] <= 10^9`
- The graph forms a valid tree

## Example 1

**Input:**

```
3 2
1 -2 3
1 2
1 3
```

**Output:**

```
4
```

**Explanation:**
Tree structure:

```
    1 (val=1)
   / \
  2   3
(val=-2) (val=3)
```

Possible paths with at most 2 edges:

- Single nodes: 1, -2, 3 → max = 3
- Path 1-2: 1 + (-2) = -1
- Path 1-3: 1 + 3 = 4 ✓ (maximum)
- Path 2-1-3: -2 + 1 + 3 = 2 (uses 2 edges)

Maximum sum is 4 (path from node 1 to node 3).

## Example 2

**Input:**

```
5 3
10 -5 20 -10 30
1 2
1 3
2 4
2 5
```

**Output:**

```
45
```

**Explanation:**
Tree structure:

```
      1(10)
     / \
  2(-5) 3(20)
   / \
4(-10) 5(30)
```

Best path with at most 3 edges:

Possible paths:

- Just node 5: 30
- Path 1-3: 10 + 20 = 30
- Path 5-2-1: 30 + (-5) + 10 = 35
- Path 5-2-1-3: 30 + (-5) + 10 + 20 = 55 (uses 3 edges) ✓

Maximum is 55 (path from node 5 through nodes 2, 1, to node 3).

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
    static long[] value;
    static long[][] dp;
    static long maxSum;
    static int n, L;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        L = sc.nextInt();

        value = new long[n + 1];
        for (int i = 1; i <= n; i++) {
            value[i] = sc.nextLong();
        }

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

        dp = new long[n + 1][L + 1];
        for (int i = 0; i <= n; i++) {
            Arrays.fill(dp[i], Long.MIN_VALUE / 2);
        }

        maxSum = Long.MIN_VALUE;

        dfs(1, -1);

        // Also consider single node paths
        for (int i = 1; i <= n; i++) {
            maxSum = Math.max(maxSum, value[i]);
        }

        System.out.println(maxSum);
        sc.close();
    }

    static void dfs(int u, int parent) {
        dp[u][0] = value[u];
        maxSum = Math.max(maxSum, value[u]);

        List<long[]> childPaths = new ArrayList<>();

        for (Edge e : graph[u]) {
            int v = e.to;
            if (v == parent) continue;

            dfs(v, u);

            // Extend paths from child
            long[] childBest = new long[L + 1];
            Arrays.fill(childBest, Long.MIN_VALUE / 2);

            for (int len = 0; len < L; len++) {
                if (dp[v][len] > Long.MIN_VALUE / 2) {
                    long extended = dp[v][len] + value[u];
                    dp[u][len + 1] = Math.max(dp[u][len + 1], extended);
                    childBest[len] = dp[v][len];
                }
            }

            childPaths.add(childBest);
        }

        // Update max with single downward path
        for (int len = 0; len <= L; len++) {
            maxSum = Math.max(maxSum, dp[u][len]);
        }

        // Combine two paths through this node
        for (int i = 0; i < childPaths.size(); i++) {
            for (int j = i + 1; j < childPaths.size(); j++) {
                long[] path1 = childPaths.get(i);
                long[] path2 = childPaths.get(j);

                for (int len1 = 0; len1 <= L; len1++) {
                    for (int len2 = 0; len2 <= L; len2++) {
                        // Total edges: len1 + 1 (to u) + 1 (from u) + len2
                        if (len1 + len2 + 2 > L) continue;
                        if (path1[len1] > Long.MIN_VALUE / 2 &&
                            path2[len2] > Long.MIN_VALUE / 2) {
                            long combined = path1[len1] + path2[len2] + value[u];
                            maxSum = Math.max(maxSum, combined);
                        }
                    }
                }
            }
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
const long long NEG_INF = LLONG_MIN / 2;

vector<int> graph[MAXN];
long long value[MAXN];
long long dp[MAXN][505];
long long maxSum;
int n, L;

void dfs(int u, int parent) {
    dp[u][0] = value[u];
    maxSum = max(maxSum, value[u]);

    vector<vector<long long>> childPaths;

    for (int v : graph[u]) {
        if (v == parent) continue;

        dfs(v, u);

        vector<long long> childBest(L + 1, NEG_INF);

        for (int len = 0; len < L; len++) {
            if (dp[v][len] > NEG_INF) {
                long long extended = dp[v][len] + value[u];
                dp[u][len + 1] = max(dp[u][len + 1], extended);
                childBest[len] = dp[v][len];
            }
        }

        childPaths.push_back(childBest);
    }

    for (int len = 0; len <= L; len++) {
        maxSum = max(maxSum, dp[u][len]);
    }

    for (int i = 0; i < (int)childPaths.size(); i++) {
        for (int j = i + 1; j < (int)childPaths.size(); j++) {
            auto& path1 = childPaths[i];
            auto& path2 = childPaths[j];

            for (int len1 = 0; len1 <= L; len1++) {
                for (int len2 = 0; len2 <= L; len2++) {
                    // Total edges: len1 + 1 (to u) + 1 (from u) + len2
                    if (len1 + len2 + 2 > L) continue;
                    if (path1[len1] > NEG_INF && path2[len2] > NEG_INF) {
                        long long combined = path1[len1] + path2[len2] + value[u];
                        maxSum = max(maxSum, combined);
                    }
                }
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> L;

    for (int i = 1; i <= n; i++) {
        cin >> value[i];
    }

    for (int i = 0; i < n - 1; i++) {
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    for (int i = 0; i <= n; i++) {
        for (int j = 0; j <= L; j++) {
            dp[i][j] = NEG_INF;
        }
    }

    maxSum = NEG_INF;

    dfs(1, -1);

    cout << maxSum << endl;

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

  console.log(maxSum);
}
```

