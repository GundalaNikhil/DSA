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
import java.io.*;

class Solution {
    public List<Long> kShortestPaths(int n, int m, int s, int t, int k, int[][] edges) {
        // Implement here
        return new ArrayList<>();
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        if (line == null) return;
        String[] parts = line.trim().split("\\s+");
        int n = Integer.parseInt(parts[0]);
        int m = Integer.parseInt(parts[1]);
        int s = Integer.parseInt(parts[2]);
        int t = Integer.parseInt(parts[3]);
        int k = Integer.parseInt(parts[4]);

        int[][] edges = new int[m][3];
        for (int i = 0; i < m; i++) {
            parts = br.readLine().trim().split("\\s+");
            edges[i][0] = Integer.parseInt(parts[0]);
            edges[i][1] = Integer.parseInt(parts[1]);
            edges[i][2] = Integer.parseInt(parts[2]);
        }

        Solution sol = new Solution();
        List<Long> result = sol.kShortestPaths(n, m, s, t, k, edges);

        System.out.println(result.size());
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < result.size(); i++) {
            sb.append(result.get(i)).append(i == result.size() - 1 ? "" : " ");
        }
        System.out.println(sb);
    }
}
```

### Python

```python
import sys
import heapq

class Solution:
    def k_shortest_paths(self, n, m, s, t, k, edges):
        # Implement here
        return []

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        s = int(next(iterator))
        t = int(next(iterator))
        k = int(next(iterator))

        edges = []
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            w = int(next(iterator))
            edges.append([u, v, w])

    except StopIteration:
        pass

    sol = Solution()
    result = sol.k_shortest_paths(n, m, s, t, k, edges)

    print(len(result))
    print(*(result))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

class Solution {
public:
    vector<long long> kShortestPaths(int n, int m, int s, int t, int k, vector<vector<int>>& edges) {
        // Implement here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m, s, t, k;
    if (!(cin >> n >> m >> s >> t >> k)) return 0;

    vector<vector<int>> edges(m, vector<int>(3));
    for (int i = 0; i < m; i++) {
        cin >> edges[i][0] >> edges[i][1] >> edges[i][2];
    }

    Solution sol;
    vector<long long> result = sol.kShortestPaths(n, m, s, t, k, edges);

    cout << result.size() << endl;
    for (int i = 0; i < result.size(); i++) {
        cout << result[i] << (i == result.size() - 1 ? "" : " ");
    }
    cout << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  kShortestPaths(n, m, s, t, k, edges) {
    // Implement here
    return [];
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 5) return;

  let idx = 0;
  function readInt() {
    return parseInt(input[idx++]);
  }

  const n = readInt();
  const m = readInt();
  const s = readInt();
  const t = readInt();
  const k = readInt();

  const edges = [];
  for (let i = 0; i < m; i++) {
    const u = readInt();
    const v = readInt();
    const w = readInt();
    edges.push([u, v, w]);
  }

  const sol = new Solution();
  const result = sol.kShortestPaths(n, m, s, t, k, edges);

  console.log(result.length);
  console.log(result.join(" "));
}

solve();
```
