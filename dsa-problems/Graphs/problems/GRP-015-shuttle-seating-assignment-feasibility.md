---
problem_id: GRP_SHUTTLE_SEATING_FEASIBILITY__8362
display_id: GRP-015
slug: shuttle-seating-assignment-feasibility
title: "Shuttle Seating Assignment Feasibility"
difficulty: Medium
difficulty_score: 50
topics:
  - Topological Sort
  - Directed Acyclic Graph
  - Kahn's Algorithm
tags:
  - graph
  - topological-sort
  - dag
  - kahns-algorithm
  - scheduling
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRP-015: Shuttle Seating Assignment Feasibility

## Problem Statement

Given `n` tasks (numbered 0 to n-1) with directed dependencies (represented as edges where `u → v` means task `u` must be completed before task `v`), determine:
1. Whether a valid ordering of tasks exists (i.e., the graph is a DAG with no cycles)
2. How many nodes had zero in-degree initially (i.e., could be started first)

Return these two pieces of information.

![Problem Illustration](../images/GRP-015/problem-illustration.png)

## Input Format

- First line: integer `n` (number of tasks)
- Second line: integer `m` (number of directed edges/dependencies)
- Next `m` lines: two integers `u v` representing "task u must be completed before task v"

## Output Format

- If a valid ordering exists: Two space-separated integers: `1 count`
  - `1` indicates ordering is possible
  - `count` is the number of tasks with initial in-degree 0
- If no valid ordering exists (cycle detected): `-1`

## Constraints

- `1 <= n <= 10^5`
- `0 <= m <= 2*10^5`
- `0 <= u, v < n`

## Example

**Input:**
```
4
3
0 2
1 2
2 3
```

**Output:**
```
1 2
```

**Explanation:**

Task dependencies:
- Task 0 must be done before task 2
- Task 1 must be done before task 2
- Task 2 must be done before task 3

In-degrees:
- Task 0: in-degree 0 (can start immediately)
- Task 1: in-degree 0 (can start immediately)
- Task 2: in-degree 2 (depends on tasks 0 and 1)
- Task 3: in-degree 1 (depends on task 2)

Valid orderings exist (e.g., [0, 1, 2, 3] or [1, 0, 2, 3]).
Initially, 2 tasks (0 and 1) had in-degree 0.

Output: `1 2`

![Example Visualization](../images/GRP-015/example-1.png)

## Notes

- Use Kahn's algorithm for topological sort
- Initialize in-degrees for all nodes
- Start with all nodes having in-degree 0
- Process nodes by reducing in-degrees of neighbors
- If all nodes are processed → valid ordering exists
- If some nodes remain unprocessed → cycle exists
- Count initial zero in-degree nodes before starting the algorithm
- Time complexity: O(n + m)

## Related Topics

Topological Sort, Kahn's Algorithm, DAG, In-Degree, Cycle Detection, Task Scheduling

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int[] checkFeasibility(int n, int[][] edges) {
        return null;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();

        int[][] edges = new int[m][2];
        for (int i = 0; i < m; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
        }

        Solution solution = new Solution();
        int[] result = solution.checkFeasibility(n, edges);

        if (result.length == 1) {
            System.out.println(result[0]);
        } else {
            System.out.println(result[0] + " " + result[1]);
        }
        sc.close();
    }
}
```

### Python

```python
import sys
sys.setrecursionlimit(200000)
from collections import deque
from typing import List, Tuple

def check_feasibility(n: int, edges: List[Tuple[int, int]]) -> Tuple[int, ...]:
    return 0
def main():
    try:
        input_data = sys.stdin.read().split()
    except Exception:
        return
        
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        
        edges = []
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            edges.append((u, v))
            
        result = check_feasibility(n, edges)
        
        if len(result) == 1:
            print(result[0])
        else:
            print(f"{result[0]} {result[1]}")
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
#include <algorithm>
using namespace std;

class Solution {
public:
    pair<int, int> checkFeasibility(int n, vector<pair<int,int>>& edges) {
        vector<int> indegree(n, 0);
        vector<vector<int>> adj(n);

        // Build graph
        for (auto& [u, v] : edges) {
            adj[u].push_back(v);
            indegree[v]++;
        }

        // Sort adjacency lists for deterministic behavior
        for (int i = 0; i < n; i++) {
            sort(adj[i].begin(), adj[i].end());
        }

        // Count nodes with indegree 0
        int initialZeros = 0;
        queue<int> q;
        for (int i = 0; i < n; i++) {
            if (indegree[i] == 0) {
                q.push(i);
                initialZeros++;
            }
        }

        int processed = 0;

        while (!q.empty()) {
            int u = q.front();
            q.pop();
            processed++;

            for (int v : adj[u]) {
                indegree[v]--;
                if (indegree[v] == 0) {
                    q.push(v);
                }
            }
        }

        if (processed == n) {
            return {1, initialZeros};
        } else {
            return {-1, -1};
        }
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    vector<pair<int,int>> edges;
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        edges.push_back({u, v});
    }

    Solution solution;
    auto [result, zeros] = solution.checkFeasibility(n, edges);

    if (result == -1) {
        cout << -1 << endl;
    } else {
        cout << result << " " << zeros << endl;
    }

    return 0;
}
```

### JavaScript

```javascript
class Solution {
  checkFeasibility(n, edges) {
    return 0;
  }
}

const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  const tokens = data.join(" ").split(/\s+/);
  let ptr = 0;
  const n = Number(tokens[ptr++]);
  const m = Number(tokens[ptr++]);

  const edges = [];
  for (let i = 0; i < m; i++) {
    const u = Number(tokens[ptr++]);
    const v = Number(tokens[ptr++]);
    edges.push([u, v]);
  }

  const solution = new Solution();
  const result = solution.checkFeasibility(n, edges);

  if (result.length === 1) {
    console.log(result[0]);
  } else {
    console.log(`${result[0]} ${result[1]}`);
  }
});
```

