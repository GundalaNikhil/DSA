---
problem_id: AGR_K_SHORTEST_LOOPLESS_PATHS__2749
display_id: AGR-003
slug: k-shortest-loopless-paths
title: "K Shortest Paths (Loopless)"
difficulty: Medium
difficulty_score: 62
topics:
  - Graphs
  - Shortest Path
  - Yen Algorithm
tags:
  - advanced-graphs
  - k-shortest
  - yen
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# AGR-003: K Shortest Paths (Loopless)

## Problem Statement

Given a directed weighted graph, find the `k` shortest **simple** paths from source `s` to target `t` (no repeated vertices). Output the path lengths in ascending order.

If fewer than `k` simple paths exist, output all of them.

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767187126/dsa-problems/AGR-003/problem/ycidx4enufuhzccowmgb.jpg)

## Input Format

- First line: integers `n`, `m`, `s`, `t`, and `k`
- Next `m` lines: `u v w` describing a directed edge `u -> v` with weight `w`

## Output Format

- Line 1: integer `r`, the number of paths found
- Line 2: `r` integers, the path lengths in ascending order

## Constraints

- `1 <= n <= 500`
- `0 <= m <= 5000`
- `1 <= k <= 50`
- `0 <= w <= 10^9`
- `0 <= s, t < n`

## Example

**Input:**

```
3 3 0 2 2
0 1 1
1 2 1
0 2 3
```

**Output:**

```
2
2 3
```

**Explanation:**

The two shortest simple paths are `0-1-2` (length 2) and `0-2` (length 3).

![Example Visualization](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767187128/dsa-problems/AGR-003/problem/wvacrhnvixycwwqlk1md.jpg)

## Notes

- Use Yen's algorithm with Dijkstra for spur paths.
- Distances can exceed 32-bit; use 64-bit integers.
- If no path exists, output `0` and an empty second line.

## Related Topics

K Shortest Paths, Dijkstra, Yen's Algorithm

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long[] kShortestPaths(int n, List<List<int[]>> adjList, int s, int t, int k) {
        //Implement here
        return new long[0];
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        int s = sc.nextInt();
        int t = sc.nextInt();
        int k = sc.nextInt();
        List<List<int[]>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            int w = sc.nextInt();
            adj.get(u).add(new int[]{v, w});
        }

        Solution solution = new Solution();
        long[] paths = solution.kShortestPaths(n, adj, s, t, k);
        StringBuilder sb = new StringBuilder();
        sb.append(paths.length).append('\n');
        for (int i = 0; i < paths.length; i++) {
            if (i > 0) sb.append(' ');
            sb.append(paths[i]);
        }
        System.out.print(sb.toString());
        sc.close();
    }
}
```

### Python

```python
import sys
import heapq

def k_shortest_paths(n: int, adj: list[list[tuple[int, int]]], s: int, t: int, k: int) -> list[int]:
    # //Implement here
    return 0

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        s = int(next(iterator))
        t = int(next(iterator))
        k = int(next(iterator))
        adj = [[] for _ in range(n)]
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            w = int(next(iterator))
            adj[u].append((v, w))
            
        paths = k_shortest_paths(n, adj, s, t, k)
        print(len(paths))
        print(" ".join(map(str, paths)))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <algorithm>
#include <map>

using namespace std;

class Solution {
public:
    vector<long long> kShortestPaths(int n, const vector<vector<pair<int, int>>>& adjList, int s, int t, int k) {
        //Implement here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, s, t, k;
    if (!(cin >> n >> m >> s >> t >> k)) return 0;
    vector<vector<pair<int, int>>> adj(n);
    for (int i = 0; i < m; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
    }

    Solution solution;
    vector<long long> paths = solution.kShortestPaths(n, adj, s, t, k);
    cout << paths.size() << "\n";
    for (int i = 0; i < (int)paths.size(); i++) {
        if (i) cout << ' ';
        cout << paths[i];
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  kShortestPaths(n, adj, s, t, k) {
    //Implement here
    return 0;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => { const parts = line.trim().split(/\s+/); for (const p of parts) if (p) data.push(p); });
rl.on("close", () => {
  if (data.length === 0) return;
  
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const m = parseInt(data[idx++], 10);
  const s = parseInt(data[idx++], 10);
  const t = parseInt(data[idx++], 10);
  const k = parseInt(data[idx++], 10);
  const adj = Array.from({ length: n }, () => []);
  for (let i = 0; i < m; i++) {
    const u = parseInt(data[idx++], 10);
    const v = parseInt(data[idx++], 10);
    const w = parseInt(data[idx++], 10);
    if (u >= n || u < 0) { console.error(`Error: u=${u} n=${n} idx=${idx-3} len=${data.length}`); }
    if (!adj[u]) { console.error(`Error: adj[${u}] undefined. n=${n}`); }
    adj[u].push([v, w]);
  }

  const solution = new Solution();
  const paths = solution.kShortestPaths(n, adj, s, t, k);
  console.log(paths.length.toString());
  console.log(paths.join(" "));
});
```

