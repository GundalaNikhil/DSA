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

class Solution {
    public long minColoringCost(int n, int k, int[][] costs, int[][] edges) {
        // Implement here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int k = sc.nextInt();

        int[][] costs = new int[n][k];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < k; j++) {
                costs[i][j] = sc.nextInt();
            }
        }

        int[][] edges = new int[n - 1][2];
        for (int i = 0; i < n - 1; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
        }

        Solution solution = new Solution();
        System.out.println(solution.minColoringCost(n, k, costs, edges));
    }
}
```

### Python

```python
from typing import List
import sys

sys.setrecursionlimit(200000)

class Solution:
    def min_coloring_cost(self, n: int, k: int, costs: List[List[int]], edges: List[List[int]]) -> int:
        # Implement here
        return 0

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        k = int(next(iterator))

        costs = []
        for _ in range(n):
            row = []
            for _ in range(k):
                row.append(int(next(iterator)))
            costs.append(row)

        edges = []
        for _ in range(n - 1):
            u = int(next(iterator))
            v = int(next(iterator))
            edges.append([u, v])

        solution = Solution()
        print(solution.min_coloring_cost(n, k, costs, edges))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    long long minColoringCost(int n, int k, const vector<vector<int>>& costs, const vector<vector<int>>& edges) {
        // Implement here
        return 0;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<vector<int>> costs(n, vector<int>(k));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < k; j++) {
            cin >> costs[i][j];
        }
    }

    vector<vector<int>> edges(n - 1, vector<int>(2));
    for (int i = 0; i < n - 1; i++) {
        cin >> edges[i][0] >> edges[i][1];
    }

    Solution solution;
    cout << solution.minColoringCost(n, k, costs, edges) << endl;

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  minColoringCost(n, k, costs, edges) {
    // Implement here
    return 0;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const lines = [];
rl.on("line", (line) => {
  lines.push(line);
}).on("close", () => {
  const tokens = lines
    .join(" ")
    .split(/\s+/)
    .filter((t) => t !== "");
  if (tokens.length === 0) return;

  let idx = 0;
  const n = parseInt(tokens[idx++]);
  const k = parseInt(tokens[idx++]);

  const costs = [];
  for (let i = 0; i < n; i++) {
    const row = [];
    for (let j = 0; j < k; j++) {
      row.push(parseInt(tokens[idx++]));
    }
    costs.push(row);
  }

  const edges = [];
  for (let i = 0; i < n - 1; i++) {
    const u = parseInt(tokens[idx++]);
    const v = parseInt(tokens[idx++]);
    edges.push([u, v]);
  }

  const solution = new Solution();
  console.log(solution.minColoringCost(n, k, costs, edges));
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
