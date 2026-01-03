---
problem_id: AGR_EULERIAN_TRAIL_DIRECTED__4836
display_id: AGR-007
slug: eulerian-trail-directed
title: "Eulerian Trail With Directed Edges"
difficulty: Medium
difficulty_score: 48
topics:
  - Graphs
  - Eulerian Path
  - DFS
tags:
  - advanced-graphs
  - eulerian
  - hierholzer
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# AGR-007: Eulerian Trail With Directed Edges

## Problem Statement

Determine whether a directed graph has an Eulerian trail (a path that uses every edge exactly once). If it exists, output one such trail.

![Problem Illustration](../images/AGR-007/problem-illustration.png)

## Input Format

- First line: integers `n` and `m`
- Next `m` lines: `u v` describing a directed edge `u -> v`

## Output Format

- If no Eulerian trail exists: print `NO`
- Otherwise: print `YES` and then one line with the trail as a sequence of `m+1` nodes

## Constraints

- `1 <= n <= 100000`
- `0 <= m <= 200000`
- `0 <= u, v < n`

## Example

**Input:**

```
3 3
0 1
1 2
2 0
```

**Output:**

```
YES
0 1 2 0
```

**Explanation:**

The cycle uses each directed edge exactly once.

![Example Visualization](../images/AGR-007/example-1.png)

## Notes

- A directed Euler trail exists if at most one node has out-in = 1 and at most one node has in-out = 1, and all edges are in one weakly connected component.
- Use Hierholzer's algorithm to construct the trail.
- If `m=0`, output `YES` and any single node (e.g., 0).

## Related Topics

Eulerian Path, Hierholzer, Graph Traversal

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int[] eulerTrail(int n, int[][] edges) {
        //Implement here
        return new int[0];
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[][] edges = new int[m][2];
        for (int i = 0; i < m; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
        }

        Solution solution = new Solution();
        int[] trail = solution.eulerTrail(n, edges);
        if (trail == null) {
            System.out.print("NO");
        } else {
            StringBuilder sb = new StringBuilder();
            sb.append("YES\n");
            for (int i = 0; i < trail.length; i++) {
                if (i > 0) sb.append(' ');
                sb.append(trail[i]);
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

sys.setrecursionlimit(300000)

def euler_trail(n: int, edges: list[tuple[int, int]]):
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
        edges = []
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            edges.append((u, v))
            
        trail = euler_trail(n, edges)
        if trail is None:
            sys.stdout.write("NO")
        else:
            sys.stdout.write("YES\n" + " ".join(map(str, trail)))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <deque>

using namespace std;

class Solution {
public:
    vector<int> eulerTrail(int n, const vector<pair<int, int>>& edges) {
        //Implement here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<pair<int, int>> edges(m);
    for (int i = 0; i < m; i++) {
        cin >> edges[i].first >> edges[i].second;
    }

    Solution solution;
    vector<int> trail = solution.eulerTrail(n, edges);
    if (trail.empty()) {
        cout << "NO";
    } else {
        cout << "YES\n";
        for (int i = 0; i < (int)trail.size(); i++) {
            if (i) cout << ' ';
            cout << trail[i];
        }
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  eulerTrail(n, edges) {
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
  const edges = [];
  for (let i = 0; i < m; i++) {
    const u = parseInt(data[idx++], 10);
    const v = parseInt(data[idx++], 10);
    edges.push([u, v]);
  }

  const solution = new Solution();
  const trail = solution.eulerTrail(n, edges);
  if (trail === null) {
    console.log("NO");
  } else {
    console.log("YES");
    console.log(trail.join(" "));
  }
});
```

