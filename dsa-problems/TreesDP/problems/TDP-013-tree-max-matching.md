---
title: "DP on Tree for Maximum Matching"
problem_id: TDP_TREE_MAX_MATCHING__6183
display_id: TDP-013
difficulty: Medium
tags: [tree-dp, matching, graph-theory]
slug: tree-max-matching
time_limit: 2000
memory_limit: 256
---

## Problem Description

Find maximum matching in a tree. A matching is a set of edges with no shared vertices.

## Input Format

- Line 1: N
- Next N-1 lines: u v (edges)

## Output Format

Maximum matching size.

## Examples

### Example 1

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

### Example 2

**Input:**

```
7
1 2
1 3
2 4
2 5
3 6
3 7
```

**Output:**

```
3
```

## Constraints

- 1 ≤ N ≤ 200,000

## Solution Template

### Java

```java
import java.util.*;
class Main {
    static List<Integer>[] adj;
    static int[][] dp;
    static int n;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        adj = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) adj[i] = new ArrayList<>();

        for (int i = 0; i < n - 1; i++) {
            int u = sc.nextInt(), v = sc.nextInt();
            adj[u].add(v); adj[v].add(u);
        }

        dp = new int[n + 1][2];
        dfs(1, 0);
        System.out.println(Math.max(dp[1][0], dp[1][1]));
    }


    static void dfs(int u, int p) {

        //Implement here

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

    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = int(data[idx]), int(data[idx + 1])
        idx += 2
        adj[u].append(v); adj[v].append(u)

    dp = [[0, 0] for _ in range(n + 1)]

    def dfs(u, p):
        # //Implement here
        return 0
    dfs(1, 0)
    print(max(dp[1][0], dp[1][1]))

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

int n;
vector<vector<int>> adj;
vector<array<int, 2>> dp;


void dfs(int u, int p) {

    //Implement here

}

int main() {
    cin >> n;
    adj.resize(n + 1);
    dp.resize(n + 1);

    for (int i = 0; i < n - 1; i++) {
        int u, v; cin >> u >> v;
        adj[u].push_back(v); adj[v].push_back(u);
    }

    dfs(1, 0);
    cout << max(dp[1][0], dp[1][1]) << "\n";
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

  const adj = Array.from({ length: n + 1 }, () => []);
  for (let i = 0; i < n - 1; i++) {
    const [u, v] = lines[idx++].split(" ").map(Number);
    adj[u].push(v);
    adj[v].push(u);
  }

  const dp = Array.from({ length: n + 1 }, () => [0, 0]);

  function dfs(u, p) {
    //Implement here
    return 0;
  }

  dfs(1, 0);
  console.log(Math.max(dp[1][0], dp[1][1]));
});
```
