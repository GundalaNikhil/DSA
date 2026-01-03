---
title: "DP for Subtree LIS on Tree"
problem_id: TDP_SUBTREE_LIS__7392
display_id: TDP-015
difficulty: Hard
tags: [tree-dp, lis, coordinate-compression, fenwick]
slug: subtree-lis-tree
time_limit: 2000
memory_limit: 256
---

## Problem Description

For each node, compute LIS length of values along root-to-node path.

## Input Format

- Line 1: N
- Line 2: N node values
- Next N-1 lines: u v (edges)

## Output Format

N integers: LIS length for each node's root path.

## Examples

### Example 1

**Input:**

```
3
2 1 3
1 2
1 3
```

**Output:**

```
1 1 2
```

### Example 2

**Input:**

```
5
1 5 2 4 3
1 2
1 3
2 4
2 5
```

**Output:**

```
1 2 2 3 3
```

## Constraints

- 1 ≤ N ≤ 200,000
- 1 ≤ values[i] ≤ 10^9

## Solution Template

### Java

```java
import java.util.*;

class Main {
    static List<Integer>[] adj;
    static int[] values, lis;
    static ArrayList<Integer> active;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        values = new int[n + 1];
        lis = new int[n + 1];

        for (int i = 1; i <= n; i++) values[i] = sc.nextInt();

        adj = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) adj[i] = new ArrayList<>();

        for (int i = 0; i < n - 1; i++) {
            int u = sc.nextInt(), v = sc.nextInt();
            adj[u].add(v);
            adj[v].add(u);
        }

        active = new ArrayList<>();
        dfs(1, 0);

        for (int i = 1; i <= n; i++) {
            System.out.print(lis[i] + (i < n ? " " : "\n"));
        }
    }


    static void dfs(int u, int p) {

        //Implement here

    }

}
```

### Python

```python
import sys
from bisect import bisect_left
sys.setrecursionlimit(300000)

def main():
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1

    values = [0] + [int(data[idx + i]) for i in range(n)]
    idx += n

    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = int(data[idx]), int(data[idx + 1])
        idx += 2
        adj[u].append(v); adj[v].append(u)

    lis = [0] * (n + 1)
    active = []

    def dfs(u, p):
        # //Implement here
        return 0
    dfs(1, 0)
    print(' '.join(map(str, lis[1:])))

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
vector<int> values, lis_len;
vector<vector<int>> adj;
vector<int> active;


void dfs(int u, int p) {

    //Implement here

}

int main() {
    cin >> n;
    values.resize(n + 1);
    lis_len.resize(n + 1);
    adj.resize(n + 1);

    for (int i = 1; i <= n; i++) cin >> values[i];

    for (int i = 0; i < n - 1; i++) {
        int u, v; cin >> u >> v;
        adj[u].push_back(v); adj[v].push_back(u);
    }

    dfs(1, 0);

    for (int i = 1; i <= n; i++) {
        cout << lis_len[i] << (i < n ? " " : "\n");
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
  const values = [0, ...lines[idx++].split(" ").map(Number)];

  const adj = Array.from({ length: n + 1 }, () => []);
  for (let i = 0; i < n - 1; i++) {
    const [u, v] = lines[idx++].split(" ").map(Number);
    adj[u].push(v);
    adj[v].push(u);
  }

  const lis = Array(n + 1).fill(0);
  const active = [];

  function binarySearch(arr, val) {
    //Implement here
    return 0;
  }

  function dfs(u, p) {
    //Implement here
    return 0;
  }

  dfs(1, 0);
  console.log(lis.slice(1).join(" "));
});
```
