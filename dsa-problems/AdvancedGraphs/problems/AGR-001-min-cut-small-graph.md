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

![Problem Illustration](../images/AGR-001/problem-illustration.png)

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

The minimum cut separates `{0, 3}` from `{1, 2}`.
Edges crossing: `(0, 1)` (weight 1) and `(2, 3)` (weight 1).
Total cost: `1 + 1 = 2`.

![Example Visualization](../images/AGR-001/example-1.png)

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
        // Your implementation here
        return 0L;
    }
}

public class Main {
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
def min_cut(n: int, edges: list[tuple[int, int, int]]) -> int:
    # Your implementation here
    return 0

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it))
    edges = []
    for _ in range(m):
        u = int(next(it)); v = int(next(it)); w = int(next(it))
        edges.append((u, v, w))
    print(min_cut(n, edges))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <array>
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    long long minCut(int n, const vector<array<int, 3>>& edges) {
        // Your implementation here
        return 0LL;
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
    // Your implementation here
    return 0;
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
