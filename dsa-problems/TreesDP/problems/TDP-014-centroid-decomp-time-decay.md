---
title: "Centroid Decomposition with Time-Decay Queries"
problem_id: TDP_CENTROID_TIME_DECAY__9247
display_id: TDP-014
difficulty: Hard
tags: [tree-dp, centroid-decomposition, time-decay, advanced]
slug: centroid-decomp-time-decay
time_limit: 2000
memory_limit: 256
---

## Problem Description

Weighted tree with node values and timestamps. Query: find minimum (distance × decay + value) to any marked node.

## Input Format

- Line 1: N D (nodes, decay constant)
- Next N-1 lines: u v w (edges)
- Next line: Q (queries)
- Q lines: type params

## Output Format

Per query output.

## Examples

### Example 1

**Input:**

```
3 1000
1 2 10
2 3 20
2
1 1 100 0
2 2 0
```

**Output:**

```
110
```

### Example 2

**Input:**

```
5 500
1 2 5
1 3 10
2 4 7
2 5 3
3
1 1 50 0
1 4 80 0
2 5 0
```

**Output:**

```
62
```

## Constraints

- 1 ≤ N ≤ 100,000
- 1 ≤ Q ≤ 100,000

## Solution Template

### Java

```java
import java.util.*;

class Main {
    static List<int[]>[] adj;
    static int n;


    static long bfs(int start, Map<Integer, Long> marked) {

        //Implement here

        return 0;

    }

public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        int D = sc.nextInt();

        adj = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) adj[i] = new ArrayList<>();

        for (int i = 0; i < n - 1; i++) {
            int u = sc.nextInt(), v = sc.nextInt(), w = sc.nextInt();
            adj[u].add(new int[]{v, w});
            adj[v].add(new int[]{u, w});
        }

        int q = sc.nextInt();
        Map<Integer, Long> marked = new HashMap<>();
        StringBuilder sb = new StringBuilder();

        while (q-- > 0) {
            int type = sc.nextInt();
            if (type == 1) {
                int v = sc.nextInt();
                long val = sc.nextLong();
                int t = sc.nextInt();
                marked.put(v, val);
            } else {
                int v = sc.nextInt();
                int t = sc.nextInt();
                sb.append(bfs(v, marked)).append("\n");
            }
        }
        System.out.print(sb);
    }
}
```

### Python

```python
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    D = int(data[idx]); idx += 1

    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v, w = int(data[idx]), int(data[idx + 1]), int(data[idx + 2])
        idx += 3
        adj[u].append((v, w))
        adj[v].append((u, w))

    q = int(data[idx]); idx += 1
    marked = {}
    results = []

    def bfs(start):
        # //Implement here
        return 0
    for _ in range(q):
        qtype = int(data[idx]); idx += 1
        if qtype == 1:
            v = int(data[idx]); idx += 1
            val = int(data[idx]); idx += 1
            t = int(data[idx]); idx += 1
            marked[v] = val
        else:
            v = int(data[idx]); idx += 1
            t = int(data[idx]); idx += 1
            results.append(str(bfs(v)))

    print('\n'.join(results))

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
vector<pair<int, long long>> adj[100005];
map<int, long long> marked;


long long bfs(int start) {

    //Implement here

    return 0;

}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int D;
    cin >> n >> D;

    for (int i = 0; i < n - 1; i++) {
        int u, v;
        long long w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
        adj[v].push_back({u, w});
    }

    int q;
    cin >> q;

    while (q--) {
        int type;
        cin >> type;
        if (type == 1) {
            int v, t;
            long long val;
            cin >> v >> val >> t;
            marked[v] = val;
        } else {
            int v, t;
            cin >> v >> t;
            cout << bfs(v) << "\n";
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
  const [n, D] = lines[idx++].split(" ").map(Number);

  const adj = Array.from({ length: n + 1 }, () => []);
  for (let i = 0; i < n - 1; i++) {
    const [u, v, w] = lines[idx++].split(" ").map(Number);
    adj[u].push([v, w]);
    adj[v].push([u, w]);
  }

  const q = parseInt(lines[idx++]);
  const marked = new Map();
  const results = [];

  function bfs(start) {
    //Implement here
    return 0;
  }

  for (let i = 0; i < q; i++) {
    const parts = lines[idx++].split(" ").map(Number);
    if (parts[0] === 1) {
      const [_, v, val, t] = parts;
      marked.set(v, val);
    } else {
      const [_, v, t] = parts;
      results.push(bfs(v));
    }
  }

  console.log(results.join("\n"));
});
```
