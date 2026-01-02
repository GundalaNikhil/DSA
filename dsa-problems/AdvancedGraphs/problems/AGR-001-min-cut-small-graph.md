---
problem_id: AGR_MIN_CUT_SMALL_GRAPH__4182
display_id: AGR-001
slug: min-cut-small-graph
title: "Minimum Cut on Small Graph"
difficulty: Medium
difficulty_score: 50
topics:
  - Graphs
  - Min Cut
  - Stoer-Wagner
tags:
  - advanced-graphs
  - min-cut
  - stoer-wagner
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# AGR-001: Minimum Cut on Small Graph

## Problem Statement

Given an undirected weighted graph with `n` nodes, compute the value of the **global minimum cut**. The cut value is the total weight of edges crossing between the two partitions.

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767185652/dsa-problems/AGR-001/problem/ngj17ehpuwgruaqgacaw.jpg)

## Input Format

- First line: integers `n` and `m`
- Next `m` lines: `u v w` describing an undirected edge with weight `w`

## Output Format

- Single integer: the minimum cut value

## Constraints

- `1 <= n <= 200`
- `0 <= m <= 2000`
- `0 <= w <= 10^9`
- `0 <= u, v < n`

## Example

**Input:**

```
4 4
0 1 1
1 2 2
2 3 1
0 3 2
```

**Output:**

```
2
```

**Explanation:**

One minimum cut separates `{0, 3}` from `{1, 2}`.
Edges crossing: `(0, 1)` (weight 1) and `(3, 2)` (weight 1).
Total cost: `1 + 1 = 2`.

![Example Visualization](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767185654/dsa-problems/AGR-001/problem/lhavu7kthroej0xvm6av.jpg)

## Notes

- The graph may be disconnected; then the minimum cut is 0.
- Use Stoer-Wagner for the global min-cut in `O(n^3)`.
- Use 64-bit integers for the cut value.

## Related Topics

Global Min-Cut, Stoer-Wagner, Graph Algorithms

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long minCut(int n, List<int[]> edges) {
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        List<int[]> edges = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            int w = sc.nextInt();
            edges.add(new int[]{u, v, w});
        }

        Solution solution = new Solution();
        System.out.println(solution.minCut(n, edges));
        sc.close();
    }
}
```

### Python

```python
import sys

def min_cut(n: int, edges: list[tuple[int, int, int]]) -> int:
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
        edges = []
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            w = int(next(iterator))
            edges.append((u, v, w))
        print(min_cut(n, edges))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <array>
#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

class Solution {
public:
    long long minCut(int n, const vector<array<int, 3>>& edges) {
        vector<vector<long long>> adj(n, vector<long long>(n, 0));
        for (const auto& e : edges) {
            adj[e[0]][e[1]] += e[2];
            adj[e[1]][e[0]] += e[2];
        }

        long long globalMinCut = LLONG_MAX;
        vector<bool> merged(n, false);
        int nodesRemaining = n;

        while (nodesRemaining > 1) {
            vector<long long> weights(n, 0);
            vector<bool> inSet(n, false);
            int prev = -1, curr = -1;

            for (int step = 0; step < nodesRemaining; step++) {
                prev = curr;
                curr = -1;
                long long maxW = -1;

                for (int i = 0; i < n; i++) {
                    if (!merged[i] && !inSet[i]) {
                        if (weights[i] > maxW) {
                            maxW = weights[i];
                            curr = i;
                        }
                    }
                }

                if (curr == -1) break;
                inSet[curr] = true;

                for (int i = 0; i < n; i++) {
                    if (!merged[i] && !inSet[i]) {
                        weights[i] += adj[curr][i];
                    }
                }
            }

            globalMinCut = min(globalMinCut, weights[curr]);

            // Merge curr into prev
            for (int i = 0; i < n; i++) {
                if (i != curr && i != prev && !merged[i]) {
                    adj[prev][i] += adj[curr][i];
                    adj[i][prev] += adj[curr][i];
                }
            }
            merged[curr] = true;
            nodesRemaining--;
        }

        return globalMinCut == LLONG_MAX ? 0 : globalMinCut;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<array<int, 3>> edges(m);
    for (int i = 0; i < m; i++) {
        cin >> edges[i][0] >> edges[i][1] >> edges[i][2];
    }

    Solution solution;
    cout << solution.minCut(n, edges) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  minCut(n, edges) {
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
  const edges = [];
  for (let i = 0; i < m; i++) {
    const u = parseInt(data[idx++], 10);
    const v = parseInt(data[idx++], 10);
    const w = parseInt(data[idx++], 10);
    edges.push([u, v, w]);
  }

  const solution = new Solution();
  console.log(solution.minCut(n, edges).toString());
});
```

