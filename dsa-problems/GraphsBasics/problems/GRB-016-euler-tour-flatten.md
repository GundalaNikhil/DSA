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

class Solution {
    public int[][] eulerTour(int n, List<List<Integer>> adj, int root) {
        // Your implementation here
        return new int[2][n];
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int i = 0; i < n - 1; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            adj.get(u).add(v);
            adj.get(v).add(u);
        }
        int root = sc.nextInt();

        Solution solution = new Solution();
        int[][] res = solution.eulerTour(n, adj, root);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            if (i > 0) sb.append(' ');
            sb.append(res[0][i]);
        }
        sb.append('\n');
        for (int i = 0; i < n; i++) {
            if (i > 0) sb.append(' ');
            sb.append(res[1][i]);
        }
        System.out.print(sb.toString());
        sc.close();
    }
}
```

### Python

```python
def euler_tour(n: int, adj: list[list[int]], root: int):
    # Your implementation here
    return [0] * n, [0] * n

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    adj = [[] for _ in range(n)]
    for _ in range(n - 1):
        u = int(next(it)); v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
    root = int(next(it))
    tin, tout = euler_tour(n, adj, root)
    sys.stdout.write(" ".join(str(x) for x in tin) + "\n")
    sys.stdout.write(" ".join(str(x) for x in tout))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    pair<vector<int>, vector<int>> eulerTour(int n, const vector<vector<int>>& adj, int root) {
        // Your implementation here
        return {vector<int>(n, 0), vector<int>(n, 0)};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<vector<int>> adj(n);
    for (int i = 0; i < n - 1; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    int root;
    cin >> root;

    Solution solution;
    auto res = solution.eulerTour(n, adj, root);
    for (int i = 0; i < n; i++) {
        if (i) cout << ' ';
        cout << res.first[i];
    }
    cout << "\n";
    for (int i = 0; i < n; i++) {
        if (i) cout << ' ';
        cout << res.second[i];
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  eulerTour(n, adj, root) {
    // Your implementation here
    return [new Array(n).fill(0), new Array(n).fill(0)];
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const adj = Array.from({ length: n }, () => []);
  for (let i = 0; i < n - 1; i++) {
    const u = parseInt(data[idx++], 10);
    const v = parseInt(data[idx++], 10);
    adj[u].push(v);
    adj[v].push(u);
  }
  const root = parseInt(data[idx++], 10);

  const solution = new Solution();
  const res = solution.eulerTour(n, adj, root);
  console.log(res[0].join(" "));
  console.log(res[1].join(" "));
});
```
