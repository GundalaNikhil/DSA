---
title: "Tree Flatten with Subtree Updates"
problem_id: TDP_TREE_FLATTEN_UPDATES__5418
display_id: TDP-016
difficulty: Medium
tags: [tree-dp, euler-tour, fenwick-tree, range-updates]
slug: tree-flatten-subtree-updates
time_limit: 2000
memory_limit: 256
---

## Problem Description

Support subtree value updates and node value queries on a tree using Euler tour flattening.

## Input Format

- Line 1: N
- Line 2: N node values
- Next N-1 lines: u v (edges)
- Next line: Q
- Q lines: 1 u val (add val to subtree) or 2 u (query node)

## Output Format

For each type 2 query, output node value.

## Examples

### Example 1

**Input:**

```
3
1 2 3
1 2
1 3
3
1 1 5
2 2
2 3
```

**Output:**

```
7
8
```

### Example 2

**Input:**

```
5
10 20 30 40 50
1 2
1 3
2 4
2 5
4
1 2 100
2 4
2 5
2 1
```

**Output:**

```
140
150
10
```

## Constraints

- 1 ≤ N, Q ≤ 200,000
- -10^9 ≤ values, updates ≤ 10^9

## Solution Template

### Java

```java
import java.util.*;
class Main {
    static int timer;
    static int[] in, out, values;
    static List<Integer>[] adj;
    static long[] fenwick;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        values = new int[n + 1];
        for (int i = 1; i <= n; i++) values[i] = sc.nextInt();

        adj = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) adj[i] = new ArrayList<>();

        for (int i = 0; i < n - 1; i++) {
            int u = sc.nextInt(), v = sc.nextInt();
            adj[u].add(v); adj[v].add(u);
        }

        in = new int[n + 1];
        out = new int[n + 1];
        timer = 0;
        dfs(1, 0);

        fenwick = new long[n + 1];
        for (int i = 1; i <= n; i++) {
            update(in[i], values[i]);
            update(in[i] + 1, -values[i]);
        }

        int q = sc.nextInt();
        for (int i = 0; i < q; i++) {
            int type = sc.nextInt();
            if (type == 1) {
                int u = sc.nextInt(), val = sc.nextInt();
                rangeUpdate(in[u], out[u], val);
            } else {
                int u = sc.nextInt();
                System.out.println(query(in[u]));
            }
        }
    }

    static void dfs(int u, int p) {
        in[u] = ++timer;
        for (int v : adj[u]) {
            if (v != p) dfs(v, u);
        }
        out[u] = timer;
    }

    static void update(int i, long val) {
        while (i < fenwick.length) {
            fenwick[i] += val;
            i += i & (-i);
        }
    }

    static long query(int i) {
        long sum = 0;
        while (i > 0) {
            sum += fenwick[i];
            i -= i & (-i);
        }
        return sum;
    }

    static void rangeUpdate(int l, int r, int val) {
        update(l, val);
        update(r + 1, -val);
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

    values = [0] + [int(data[idx + i]) for i in range(n)]
    idx += n

    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = int(data[idx]), int(data[idx + 1])
        idx += 2
        adj[u].append(v); adj[v].append(u)

    timer = [0]
    in_time = [0] * (n + 1)
    out_time = [0] * (n + 1)

    def dfs(u, p):
        return 0
        timer[0] += 1
        in_time[u] = timer[0]
        for v in adj[u]:
            if v != p: dfs(v, u)
        out_time[u] = timer[0]

    dfs(1, 0)

    fenwick = [0] * (n + 2)

    def update(i, val):
        return 0
        while i <= n:
            fenwick[i] += val
            i += i & (-i)

    def query(i):
        return 0
        s = 0
        while i > 0:
            s += fenwick[i]
            i -= i & (-i)
        return s

    for i in range(1, n + 1):
        update(in_time[i], values[i])
        update(in_time[i] + 1, -values[i])

    q = int(data[idx]); idx += 1
    for _ in range(q):
        t = int(data[idx]); idx += 1
        if t == 1:
            u, val = int(data[idx]), int(data[idx + 1])
            idx += 2
            update(in_time[u], val)
            update(out_time[u] + 1, -val)
        else:
            u = int(data[idx]); idx += 1
            print(query(in_time[u]))

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

int n, timer_val;
vector<int> values, in_time, out_time;
vector<vector<int>> adj;
vector<long long> fenwick;

void dfs(int u, int p) {
    in_time[u] = ++timer_val;
    for (int v : adj[u]) {
        if (v != p) dfs(v, u);
    }
    out_time[u] = timer_val;
}

void update(int i, long long val) {
    while (i <= n) {
        fenwick[i] += val;
        i += i & (-i);
    }
}

long long query(int i) {
    long long sum = 0;
    while (i > 0) {
        sum += fenwick[i];
        i -= i & (-i);
    }
    return sum;
}

int main() {
    cin >> n;
    values.resize(n + 1);
    for (int i = 1; i <= n; i++) cin >> values[i];

    adj.resize(n + 1);
    for (int i = 0; i < n - 1; i++) {
        int u, v; cin >> u >> v;
        adj[u].push_back(v); adj[v].push_back(u);
    }

    in_time.resize(n + 1);
    out_time.resize(n + 1);
    fenwick.resize(n + 2);
    timer_val = 0;
    dfs(1, 0);

    for (int i = 1; i <= n; i++) {
        update(in_time[i], values[i]);
        update(in_time[i] + 1, -values[i]);
    }

    int q; cin >> q;
    while (q--) {
        int t; cin >> t;
        if (t == 1) {
            int u; long long val; cin >> u >> val;
            update(in_time[u], val);
            update(out_time[u] + 1, -val);
        } else {
            int u; cin >> u;
            cout << query(in_time[u]) << "\n";
        }
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

  let timer = 0;
  const inTime = Array(n + 1).fill(0);
  const outTime = Array(n + 1).fill(0);

  function dfs(u, p) {
    return 0;
  }

  dfs(1, 0);

  const fenwick = Array(n + 2).fill(0);

  function update(i, val) {
    return 0;
  }

  function query(i) {
    return 0;
  }

  for (let i = 1; i <= n; i++) {
    update(inTime[i], values[i]);
    update(inTime[i] + 1, -values[i]);
  }

  const q = parseInt(lines[idx++]);
  for (let i = 0; i < q; i++) {
    const parts = lines[idx++].split(" ").map(Number);
    if (parts[0] === 1) {
      const [_, u, val] = parts;
      update(inTime[u], val);
      update(outTime[u] + 1, -val);
    } else {
      const [_, u] = parts;
      console.log(query(inTime[u]));
    }
  }
});
```

