---
title: "Tree Coloring with Color Costs"
problem_id: TDP_TREE_COLORING_COST__5821
display_id: TDP-008
difficulty: Medium
tags: [tree-dp, coloring, optimization, dynamic-programming]
slug: tree-coloring-cost
time_limit: 2000
memory_limit: 256
---

## Problem Description

You are given a tree with N nodes and K available colors. Each node must be colored with exactly one color. For each node i and color j, there is an associated cost c[i][j] to paint node i with color j.

Two adjacent nodes (connected by an edge) cannot have the same color. Find the minimum total cost to color all nodes while satisfying this constraint.

---

## Input Format

- First line: Two integers N and K (1 ≤ N ≤ 200,000, 2 ≤ K ≤ 200)
- Next N lines: K integers each, where the j-th integer on line i represents the cost c[i][j] to color node i with color j (1 ≤ c[i][j] ≤ 10^9)
- Next N-1 lines: Two integers u and v representing an edge between nodes u and v

---

## Output Format

Print a single integer — the minimum total cost to color all nodes.

---

## Examples

### Example 1

**Input:**

```
3 2
10 20
15 5
8 12
1 2
1 3
```

**Output:**

```
27
```

**Explanation:**

- Color node 1 with color 1 (cost 10)
- Color node 2 with color 2 (cost 5) — different from node 1
- Color node 3 with color 2 (cost 12) — different from node 1
- Total cost: 10 + 5 + 12 = 27

### Example 2

**Input:**

```
5 3
1 5 3
4 2 6
3 1 2
5 4 1
2 3 4
1 2
1 3
2 4
2 5
```

**Output:**

```
7
```

**Explanation:**

- Optimal coloring: Node 1→color 1, Node 2→color 2, Node 3→color 2, Node 4→color 3, Node 5→color 1
- Costs: 1 + 2 + 1 + 1 + 2 = 7

---

## Constraints

- 1 ≤ N ≤ 200,000
- 2 ≤ K ≤ 200
- 1 ≤ c[i][j] ≤ 10^9
- The graph is guaranteed to be a tree
- Answer fits in 64-bit signed integer

---

## Solution Template

### Java

```java
import java.util.*;

class Main {
    static List<List<Integer>> adj;
    static int[][] cost;
    static long[][] dp;
    static int n, k;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        k = sc.nextInt();

        cost = new int[n + 1][k + 1];
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= k; j++) {
                cost[i][j] = sc.nextInt();
            }
        }

        adj = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            adj.add(new ArrayList<>());
        }

        for (int i = 0; i < n - 1; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            adj.get(u).add(v);
            adj.get(v).add(u);
        }

        dp = new long[n + 1][k + 1];
        boolean[] visited = new boolean[n + 1];

        dfs(1, visited);

        long result = Long.MAX_VALUE;
        for (int c = 1; c <= k; c++) {
            result = Math.min(result, dp[1][c]);
        }

        System.out.println(result);
    }

    static void dfs(int u, boolean[] visited) {
        visited[u] = true;

        // Initialize dp[u][c] with cost of coloring node u with color c
        for (int c = 1; c <= k; c++) {
            dp[u][c] = cost[u][c];
        }

        for (int v : adj.get(u)) {
            if (!visited[v]) {
                dfs(v, visited);

                // Find min and second min for child v
                long min1 = Long.MAX_VALUE, min2 = Long.MAX_VALUE;
                int minColor = -1;
                for (int c = 1; c <= k; c++) {
                    if (dp[v][c] < min1) {
                        min2 = min1;
                        min1 = dp[v][c];
                        minColor = c;
                    } else if (dp[v][c] < min2) {
                        min2 = dp[v][c];
                    }
                }

                // Update dp[u][c] for each color
                for (int c = 1; c <= k; c++) {
                    if (c == minColor) {
                        dp[u][c] += min2;
                    } else {
                        dp[u][c] += min1;
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
from collections import defaultdict
sys.setrecursionlimit(200005)

def main():
    input_data = sys.stdin.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    k = int(input_data[idx]); idx += 1

    cost = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            cost[i][j] = int(input_data[idx]); idx += 1

    adj = defaultdict(list)
    for _ in range(n - 1):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        adj[u].append(v)
        adj[v].append(u)

    dp = [[0] * (k + 1) for _ in range(n + 1)]
    visited = [False] * (n + 1)

    def dfs(u):
        return 0
    dfs(1)
    print(min(dp[1][c] for c in range(1, k + 1)))

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

int n, k;
vector<vector<int>> adj;
vector<vector<int>> cost;
vector<vector<long long>> dp;
vector<bool> visited;

void dfs(int u) {
    visited[u] = true;
    for (int c = 1; c <= k; c++) {
        dp[u][c] = cost[u][c];
    }

    for (int v : adj[u]) {
        if (!visited[v]) {
            dfs(v);

            long long min1 = LLONG_MAX, min2 = LLONG_MAX;
            int minColor = -1;
            for (int c = 1; c <= k; c++) {
                if (dp[v][c] < min1) {
                    min2 = min1;
                    min1 = dp[v][c];
                    minColor = c;
                } else if (dp[v][c] < min2) {
                    min2 = dp[v][c];
                }
            }

            for (int c = 1; c <= k; c++) {
                if (c == minColor) {
                    dp[u][c] += min2;
                } else {
                    dp[u][c] += min1;
                }
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> k;

    cost.assign(n + 1, vector<int>(k + 1));
    dp.assign(n + 1, vector<long long>(k + 1));
    adj.resize(n + 1);
    visited.assign(n + 1, false);

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= k; j++) {
            cin >> cost[i][j];
        }
    }

    for (int i = 0; i < n - 1; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    dfs(1);

    long long result = LLONG_MAX;
    for (int c = 1; c <= k; c++) {
        result = min(result, dp[1][c]);
    }

    cout << result << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false,
});

const lines = [];
rl.on("line", (line) => lines.push(line.trim()));
rl.on("close", () => {
  // Token-based parsing like Python
  const data = [];
  lines.forEach(line => data.push(...line.split(" ")));
  
  let idx = 0;
  const n = parseInt(data[idx++]);
  const k = parseInt(data[idx++]);

  const cost = Array.from({ length: n + 1 }, () => Array(k + 1).fill(0));
  for (let i = 1; i <= n; i++) {
    for (let j = 1; j <= k; j++) {
      cost[i][j] = parseInt(data[idx++]);
    }
  }

  const adj = Array.from({ length: n + 1 }, () => []);
  for (let i = 0; i < n - 1; i++) {
    const u = parseInt(data[idx++]);
    const v = parseInt(data[idx++]);
    adj[u].push(v);
    adj[v].push(u);
  }

  const dp = Array.from({ length: n + 1 }, () => Array(k + 1).fill(0));
  const visited = Array(n + 1).fill(false);

  function dfs(u) {
    return 0;
  }

  dfs(1);
  
  let result = Infinity;
  for (let c = 1; c <= k; c++) {
    result = Math.min(result, dp[1][c]);
  }

  console.log(result);
});
```

