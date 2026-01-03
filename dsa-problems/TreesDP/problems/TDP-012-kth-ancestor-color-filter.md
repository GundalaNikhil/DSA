---
title: "Binary Lifting for K-th Ancestor with Color Filter"
problem_id: TDP_KTH_ANCESTOR_COLOR__3741
display_id: TDP-012
difficulty: Medium
tags: [tree-dp, binary-lifting, ancestor-queries, color-filter]
slug: kth-ancestor-color-filter
time_limit: 2000
memory_limit: 256
---

## Problem Description

Given tree where each node has a color, answer queries: find k-th ancestor of node v with color c.

## Input Format

- Line 1: N
- Line 2: N colors
- Next N-1 lines: edges u v
- Next line: Q queries
- Next Q lines: v c k

## Output Format

For each query, print k-th ancestor with color c, or -1 if doesn't exist.

## Examples

### Example 1

**Input:**

```
5
1 2 1 2 1
1 2
1 3
2 4
2 5
3
4 2 1
5 1 2
3 1 1
```

**Output:**

```
2
1
1
```

### Example 2

**Input:**

```
3
1 1 2
1 2
2 3
2
3 1 1
3 1 2
```

**Output:**

```
2
1
```

## Constraints

- 1 ≤ N ≤ 200,000
- 1 ≤ Q ≤ 200,000
- 1 ≤ color[i] ≤ 10

## Solution Template

### Java

```java
import java.util.*;
class Main {
    static int n, LOG;
    static int[] color, depth;
    static int[][] up;
    static List<Integer>[] adj;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        LOG = 20;

        color = new int[n + 1];
        for (int i = 1; i <= n; i++) color[i] = sc.nextInt();

        adj = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) adj[i] = new ArrayList<>();

        for (int i = 0; i < n - 1; i++) {
            int u = sc.nextInt(), v = sc.nextInt();
            adj[u].add(v); adj[v].add(u);
        }

        up = new int[n + 1][LOG];
        depth = new int[n + 1];
        dfs(1, 0);

        int q = sc.nextInt();
        for (int i = 0; i < q; i++) {
            int v = sc.nextInt(), c = sc.nextInt(), k = sc.nextInt();
            System.out.println(findKthColoredAncestor(v, c, k));
        }
    }


    static void dfs(int u, int p) {

        //Implement here

    }

static int findKthColoredAncestor(int v, int c, int k) {

        //Implement here

        return 0;

    }

}
```

### Python

```python
import sys
sys.setrecursionlimit(300000)

def main():
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    LOG = 20

    color = [0] + [int(data[idx + i]) for i in range(n)]
    idx += n

    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = int(data[idx]), int(data[idx + 1])
        idx += 2
        adj[u].append(v); adj[v].append(u)

    up = [[0] * LOG for _ in range(n + 1)]

    def dfs(u, p):
        # //Implement here
        return 0
    dfs(1, 0)

    def find_kth(v, c, k):
        # //Implement here
        return 0
    q = int(data[idx]); idx += 1
    for _ in range(q):
        v, c, k = int(data[idx]), int(data[idx + 1]), int(data[idx + 2])
        idx += 3
        print(find_kth(v, c, k))

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

int n, LOG = 20;
vector<int> color;
vector<vector<int>> up, adj;


void dfs(int u, int p) {

    //Implement here

}

int findKth(int v, int c, int k) {

    //Implement here

    return 0;

}

int main() {
    cin >> n;
    color.resize(n + 1);
    for (int i = 1; i <= n; i++) cin >> color[i];

    adj.resize(n + 1);
    for (int i = 0; i < n - 1; i++) {
        int u, v; cin >> u >> v;
        adj[u].push_back(v); adj[v].push_back(u);
    }

    up.assign(n + 1, vector<int>(LOG));
    dfs(1, 0);

    int q; cin >> q;
    while (q--) {
        int v, c, k; cin >> v >> c >> k;
        cout << findKth(v, c, k) << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");
const rl = readline.createInterface({ input: process.stdin, terminal: false });

const lines = [];
rl.on("line", (line) => lines.push(line.trim()));
rl.on("close", () => {
  let idx = 0;
  const n = parseInt(lines[idx++]);
  const LOG = 20;
  const color = [0, ...lines[idx++].split(" ").map(Number)];

  const adj = Array.from({ length: n + 1 }, () => []);
  for (let i = 0; i < n - 1; i++) {
    const [u, v] = lines[idx++].split(" ").map(Number);
    adj[u].push(v);
    adj[v].push(u);
  }

  const up = Array.from({ length: n + 1 }, () => Array(LOG).fill(0));

  function dfs(u, p) {
    //Implement here
    return 0;
  }

  dfs(1, 0);

  function findKth(v, c, k) {
    //Implement here
    return 0;
  }

  const q = parseInt(lines[idx++]);
  for (let i = 0; i < q; i++) {
    const [v, c, k] = lines[idx++].split(" ").map(Number);
    console.log(findKth(v, c, k));
  }
});
```
