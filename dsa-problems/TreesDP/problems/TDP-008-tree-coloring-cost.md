---
title: "Tree Coloring with Color Costs"
problem_id: TDP_TREE_COLORING_COST__5821
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

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();

        int[][] cost = new int[n + 1][k + 1];
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= k; j++) {
                cost[i][j] = sc.nextInt();
            }
        }

        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            adj.add(new ArrayList<>());
        }

        for (int i = 0; i < n - 1; i++) {
            int u = sc.nextInt(), v = sc.nextInt();
            adj.get(u).add(v);
            adj.get(v).add(u);
        }

        // TODO: Implement tree coloring DP

        System.out.println(0);
    }
}
```

### Python

```python
import sys
from collections import defaultdict
sys.setrecursionlimit(200005)

def main():
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    k = int(data[idx]); idx += 1

    cost = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            cost[i][j] = int(data[idx]); idx += 1

    adj = defaultdict(list)
    for _ in range(n - 1):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        adj[u].append(v)
        adj[v].append(u)

    # TODO: Implement tree coloring DP

    print(0)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    cin >> n >> k;

    vector<vector<int>> cost(n + 1, vector<int>(k + 1));
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= k; j++) {
            cin >> cost[i][j];
        }
    }

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < n - 1; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    // TODO: Implement tree coloring DP

    cout << 0 << "\n";
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
  let idx = 0;
  const [n, k] = lines[idx++].split(" ").map(Number);

  const cost = Array.from({ length: n + 1 }, () => Array(k + 1).fill(0));
  for (let i = 1; i <= n; i++) {
    const vals = lines[idx++].split(" ").map(Number);
    for (let j = 1; j <= k; j++) {
      cost[i][j] = vals[j - 1];
    }
  }

  const adj = Array.from({ length: n + 1 }, () => []);
  for (let i = 0; i < n - 1; i++) {
    const [u, v] = lines[idx++].split(" ").map(Number);
    adj[u].push(v);
    adj[v].push(u);
  }

  // TODO: Implement tree coloring DP

  console.log(0);
});
```

---

## Hints

<details>
<summary>Hint 1</summary>
Think about what information you need to track for each node. Since adjacent nodes can't share colors, you need to know the color of each node.
</details>

<details>
<summary>Hint 2</summary>
Use dp[u][c] to represent the minimum cost to color the subtree rooted at u, where u has color c.
</details>

<details>
<summary>Hint 3</summary>
For the recurrence, when node u has color c, each child can have any color except c. You need the minimum among valid colors for each child.
</details>

<details>
<summary>Hint 4</summary>
To optimize from O(N × K²) to O(N × K), track the minimum and second minimum costs across all colors for each child.
</details>
