---
problem_id: GRB_DETECT_CYCLE_DIRECTED__8425
display_id: GRB-006
slug: detect-cycle-directed
title: "Detect Cycle in Directed Graph"
difficulty: Easy
difficulty_score: 34
topics:
  - Graphs
  - DFS
  - Cycle Detection
tags:
  - graphs-basics
  - cycle-detection
  - dfs
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# GRB-006: Detect Cycle in Directed Graph

## Problem Statement

Given a directed graph, determine whether it contains a cycle.

![Problem Illustration](../images/GRB-006/problem-illustration.png)

## Input Format

- First line: integers `n` and `m`
- Next `m` lines: `u v` representing a directed edge `u -> v`

## Output Format

- Print `true` if a directed cycle exists, otherwise `false`

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
true
```

**Explanation:**

The edges form a cycle `0 -> 1 -> 2 -> 0`.

![Example Visualization](../images/GRB-006/example-1.png)

## Notes

- Use DFS with colors (0=unvisited, 1=visiting, 2=done) or Kahn's algorithm.
- Self-loops also count as cycles.
- The graph may be disconnected.

## Related Topics

Cycle Detection, DFS, Directed Graphs

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public boolean hasCycle(int n, List<List<Integer>> adj) {
        return false;
    }

    private boolean dfs(int u, List<List<Integer>> adj, int[] state) {
        state[u] = 1; // Mark as visiting
        for (int v : adj.get(u)) {
            if (state[v] == 1) return true; // Found a back edge to a node in current stack
            if (state[v] == 0) {
                if (dfs(v, adj, state)) return true;
            }
        }
        state[u] = 2; // Mark as visited
        return false;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            adj.get(u).add(v);
        }

        Solution solution = new Solution();
        System.out.println(solution.hasCycle(n, adj) ? "1" : "0");
        sc.close();
    }
}
```

### Python

```python
import sys

# Increase recursion depth
sys.setrecursionlimit(200000)

def has_cycle(n: int, adj: list[list[int]]) -> bool:
    return False
def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        adj = [[] for _ in range(n)]
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            adj[u].append(v)
            
        print("1" if has_cycle(n, adj) else "0")
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>

using namespace std;

class Solution {
    bool dfs(int u, const vector<vector<int>>& adj, vector<int>& state) {
        return false;
    }

public:
    bool hasCycle(int n, const vector<vector<int>>& adj) {
        return false;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<vector<int>> adj(n);
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
    }

    Solution solution;
    cout << (solution.hasCycle(n, adj) ? "1" : "0");
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  hasCycle(n, adj) {
    return 0;
  }

  dfs(u, adj, state) {
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
  
  const adj = Array.from({ length: n }, () => []);
  for (let i = 0; i < m; i++) {
    const u = parseInt(data[idx++], 10);
    const v = parseInt(data[idx++], 10);
    adj[u].push(v);
  }

  const solution = new Solution();
  console.log(solution.hasCycle(n, adj) ? "1" : "0");
});
```

