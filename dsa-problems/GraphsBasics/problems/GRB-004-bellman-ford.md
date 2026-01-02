---
problem_id: GRB_BELLMAN_FORD__3812
display_id: GRB-004
slug: bellman-ford
title: "Bellman-Ford with Negative Edges"
difficulty: Medium
difficulty_score: 50
topics:
  - Graphs
  - Shortest Path
  - Bellman-Ford
tags:
  - graphs-basics
  - bellman-ford
  - shortest-path
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# GRB-004: Bellman-Ford with Negative Edges

## Problem Statement

You are given a directed graph that may contain negative edge weights. Compute shortest distances from a source node `s`.

If a negative cycle is reachable from `s`, output `NEGATIVE CYCLE`.

![Problem Illustration](../images/GRB-004/problem-illustration.png)

## Input Format

- First line: integers `n`, `m`, and `s`
- Next `m` lines: `u v w` describing a directed edge `u -> v` with weight `w`

## Output Format

- If a reachable negative cycle exists: print `NEGATIVE CYCLE`
- Otherwise: print `n` integers, the distances from `s` to nodes `0..n-1` (`-1` if unreachable)

## Constraints

- `1 <= n <= 10000`
- `0 <= m <= 50000`
- `-10^9 <= w <= 10^9`
- `0 <= s < n`

## Example

**Input:**

```
2 2 0
0 1 -1
1 0 -1
```

**Output:**

```
NEGATIVE CYCLE
```

**Explanation:**

The cycle `0 -> 1 -> 0` has total weight `-2` and is reachable from the source.

![Example Visualization](../images/GRB-004/example-1.png)

## Notes

- Run `n-1` relaxations, then one extra pass to detect negative cycles.
- Distances should use 64-bit integers.
- Unreachable nodes keep distance `-1`.

## Related Topics

Bellman-Ford, Shortest Path, Negative Cycles

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long[] bellmanFord(int n, int s, int[][] edges) {
        return null;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        int s = sc.nextInt();
        int[][] edges = new int[m][3];
        for (int i = 0; i < m; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
            edges[i][2] = sc.nextInt();
        }

        Solution solution = new Solution();
        long[] dist = solution.bellmanFord(n, s, edges);
        if (dist == null) {
            System.out.print("NEGATIVE CYCLE");
        } else {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < n; i++) {
                if (i > 0) sb.append(' ');
                sb.append(dist[i]);
            }
            System.out.print(sb.toString());
        }
        sc.close();
    }
}
```

### Python

```python
import sys

def bellman_ford(n: int, s: int, edges: list[tuple[int, int, int]]):
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
        
        edges = []
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            w = int(next(iterator))
            edges.append((u, v, w))
            
        dist = bellman_ford(n, s, edges)
        if dist is None:
            print("NEGATIVE CYCLE")
        else:
            print(" ".join(map(str, dist)))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <array>

using namespace std;

class Solution {
public:
    vector<long long> bellmanFord(int n, int s, const vector<array<int, 3>>& edges) {
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, s;
    if (!(cin >> n >> m >> s)) return 0;
    vector<array<int, 3>> edges(m);
    for (int i = 0; i < m; ++i) {
        cin >> edges[i][0] >> edges[i][1] >> edges[i][2];
    }

    Solution solution;
    vector<long long> dist = solution.bellmanFord(n, s, edges);

    if (dist.empty()) {
        cout << "NEGATIVE CYCLE";
    } else {
        for (int i = 0; i < n; ++i) {
            if (i) cout << ' ';
            cout << dist[i];
        }
    }
    cout << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  bellmanFord(n, s, edges) {
    return 0;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  if (data.length === 0) return;
  
  const tokens = data.join(" ").trim().split(/\s+/);
  if (tokens.length === 0 || tokens[0] === "") return;
  
  let ptr = 0;
  const n = parseInt(tokens[ptr++], 10);
  const m = parseInt(tokens[ptr++], 10);
  const s = parseInt(tokens[ptr++], 10);
  
  const edges = [];
  for (let i = 0; i < m; i++) {
    const u = parseInt(tokens[ptr++], 10);
    const v = parseInt(tokens[ptr++], 10);
    const w = parseInt(tokens[ptr++], 10);
    edges.push([u, v, w]);
  }

  const solution = new Solution();
  const dist = solution.bellmanFord(n, s, edges);
  
  if (dist === null) {
    console.log("NEGATIVE CYCLE");
  } else {
    console.log(dist.join(" "));
  }
});
```

