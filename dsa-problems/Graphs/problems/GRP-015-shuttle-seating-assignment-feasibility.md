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
import java.io.*;

class Solution {
    public int[] checkFeasibility(int n, int m, List<List<Integer>> adj) {
        // Implement here
        return new int[0];
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String nLine = br.readLine();
        if (nLine == null) return;
        int n = Integer.parseInt(nLine.trim());

        String mLine = br.readLine();
        if (mLine == null) return;
        int m = Integer.parseInt(mLine.trim());

        List<List<Integer>> adj = new ArrayList<>(n);
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());

        for (int i = 0; i < m; i++) {
            String[] edge = br.readLine().trim().split("\\s+");
            int u = Integer.parseInt(edge[0]);
            int v = Integer.parseInt(edge[1]);
            adj.get(u).add(v);
        }

        Solution sol = new Solution();
        int[] result = sol.checkFeasibility(n, m, adj);

        if (result == null || result.length == 0) {
            System.out.println("-1");
        } else {
            System.out.println(result[0] + " " + result[1]);
        }
    }
}
```

### Python

```python
import sys

class Solution:
    def check_feasibility(self, n, m, adj):
        # Implement here
        return []

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])

    adj = [[] for _ in range(n)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        adj[u].append(v)
        idx += 2

    sol = Solution()
    result = sol.check_feasibility(n, m, adj)
    if not result:
        print("-1")
    else:
        print(*(result))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    vector<int> checkFeasibility(int n, int m, vector<vector<int>>& adj) {
        // Implement here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<int>> adj(n);
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
    }

    Solution sol;
    vector<int> result = sol.checkFeasibility(n, m, adj);

    if (result.empty()) {
        cout << "-1" << endl;
    } else {
        cout << result[0] << " " << result[1] << endl;
    }

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  checkFeasibility(n, m, adj) {
    // Implement here
    return [];
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const m = parseInt(input[idx++]);

  const adj = Array.from({ length: n }, () => []);
  for (let i = 0; i < m; i++) {
    const u = parseInt(input[idx++]);
    const v = parseInt(input[idx++]);
    adj[u].push(v);
  }

  const sol = new Solution();
  const result = sol.checkFeasibility(n, m, adj);
  if (result.length === 0) {
    console.log("-1");
  } else {
    console.log(result.join(" "));
  }
}

solve();
```
