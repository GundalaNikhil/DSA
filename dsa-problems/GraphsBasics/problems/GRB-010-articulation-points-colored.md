---
problem_id: GRB_ARTICULATION_POINTS_COLORED__1685
display_id: GRB-010
slug: articulation-points-colored
title: "Articulation Points Under Edge Colors"
difficulty: Medium
difficulty_score: 60
topics:
  - Graphs
  - DFS
  - Articulation Points
tags:
  - graphs-basics
  - articulation-points
  - dfs
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# GRB-010: Articulation Points Under Edge Colors

## Problem Statement

You are given an undirected graph where each edge is colored `R` (red) or `B` (blue). A node is **critical** if removing it disconnects the graph into components such that at least one component contains a red edge and at least one (different) component contains a blue edge.

Return all critical nodes in increasing order.

![Problem Illustration](../images/GRB-010/problem-illustration.png)

## Input Format

- First line: integers `n` and `m`
- Next `m` lines: `u v c` describing an undirected edge with color `c` (`R` or `B`)

## Output Format

- Line 1: integer `k`, number of critical nodes
- Line 2: `k` integers, the critical node indices in increasing order (or empty line if `k=0`)

## Constraints

- `1 <= n <= 100000`
- `0 <= m <= 200000`
- `0 <= u, v < n`
- `c` is `R` or `B`

## Example

**Input:**

```
5 4
0 2 R
3 4 B
1 0 R
1 3 B
```

**Output:**

```
1
1
```

**Explanation:**

Removing node `1` splits the graph into a red-edge component `{0,2}` and a blue-edge component `{3,4}`.

![Example Visualization](../images/GRB-010/example-1.png)

## Notes

- Use DFS low-link to identify articulation points.
- Track whether each subtree contains red/blue edges to detect color separation.
- A node can be an articulation point without being critical under color rules.

## Related Topics

Articulation Points, DFS, Graph Coloring

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int[] criticalNodes(int n, List<int[]> edges) {
        // Your implementation here
        return new int[0];
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
            String c = sc.next();
            edges.add(new int[]{u, v, c.equals("R") ? 0 : 1});
        }

        Solution solution = new Solution();
        int[] ans = solution.criticalNodes(n, edges);
        StringBuilder sb = new StringBuilder();
        sb.append(ans.length).append('\n');
        for (int i = 0; i < ans.length; i++) {
            if (i > 0) sb.append(' ');
            sb.append(ans[i]);
        }
        System.out.print(sb.toString());
        sc.close();
    }
}
```

### Python

```python
def critical_nodes(n: int, edges: list[tuple[int, int, int]]) -> list[int]:
    # Your implementation here
    return []

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it))
    edges = []
    for _ in range(m):
        u = int(next(it)); v = int(next(it)); c = next(it)
        edges.append((u, v, 0 if c == "R" else 1))
    ans = critical_nodes(n, edges)
    out = [str(len(ans)), " ".join(str(x) for x in ans)]
    sys.stdout.write("\n".join(out))

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
    vector<int> criticalNodes(int n, const vector<array<int, 3>>& edges) {
        // Your implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<array<int, 3>> edges;
    edges.reserve(m);
    for (int i = 0; i < m; i++) {
        int u, v; char c;
        cin >> u >> v >> c;
        edges.push_back({u, v, c == 'R' ? 0 : 1});
    }

    Solution solution;
    vector<int> ans = solution.criticalNodes(n, edges);
    cout << ans.size() << "\n";
    for (int i = 0; i < (int)ans.size(); i++) {
        if (i) cout << ' ';
        cout << ans[i];
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  criticalNodes(n, edges) {
    // Your implementation here
    return [];
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
    const c = data[idx++];
    edges.push([u, v, c === "R" ? 0 : 1]);
  }

  const solution = new Solution();
  const ans = solution.criticalNodes(n, edges);
  console.log(ans.length.toString());
  console.log(ans.join(" "));
});
```
