---
problem_id: SEG_DYNAMIC_CONNECTIVITY_OFFLINE__6384
display_id: SEG-016
slug: dynamic-connectivity-offline
title: "Dynamic Connectivity Over Time (Offline)"
difficulty: Hard
difficulty_score: 78
topics:
  - Segment Tree
  - DSU Rollback
  - Offline Queries
tags:
  - segment-tree
  - dsu
  - offline
  - hard
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# SEG-016: Dynamic Connectivity Over Time (Offline)

## Problem Statement

You are given a sequence of events on an undirected graph with `n` nodes. The events are:

- `ADD u v`: add edge `(u, v)`
- `REMOVE u v`: remove edge `(u, v)`
- `QUERY u v`: ask whether `u` and `v` are connected at this time

Answer all queries in order. You must process the events offline.

![Problem Illustration](../images/SEG-016/problem-illustration.png)

## Input Format

- First line: integers `n` and `m` (number of nodes and events)
- Next `m` lines: events `ADD`, `REMOVE`, or `QUERY`

## Output Format

- For each `QUERY`, print `true` if connected, otherwise `false`

## Constraints

- `1 <= n <= 100000`
- `1 <= m <= 200000`
- `1 <= u, v <= n`

## Example

**Input:**

```
3 4
ADD 1 2
QUERY 1 2
REMOVE 1 2
QUERY 1 2
```

**Output:**

```
true
false
```

**Explanation:**

The first query is connected by edge (1,2). After removal, the nodes are disconnected.

![Example Visualization](../images/SEG-016/example-1.png)

## Notes

- Use a segment tree over time intervals
- Maintain a DSU with rollback to undo unions
- Map each edge to the active time intervals
- Process queries with depth-first traversal

## Related Topics

DSU Rollback, Offline Queries, Segment Tree

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    static class Edge {
        int u, v;
        Edge(int u, int v) {
            this.u = u;
            this.v = v;
        }
        
        @Override
        public boolean equals(Object o) {
        return false;
    }
        
        @Override
        public int hashCode() {
        return 0;
    }
    }

    static class DSU {
        int[] parent;
        int[] rank;
        Stack<int[]> history;

        DSU(int n) {
            parent = new int[n + 1];
            rank = new int[n + 1];
            history = new Stack<>();
            for (int i = 1; i <= n; i++) {
                parent[i] = i;
                rank[i] = 1;
            }
        }

        int find(int i) {
        return 0;
    }

        void union(int i, int j) {
    }

        void rollback() {
    }
        
        boolean connected(int i, int j) {
        return false;
    }
    }

    private List<Edge>[] tree;
    private List<String> results;
    private List<String[]> queries; // Store queries by time index

    public List<String> process(int n, List<String[]> events) {
        return null;
    }

    private void addEdge(int node, int start, int end, int l, int r, Edge e) {
    }

    private void dfs(int node, int start, int end, DSU dsu) {
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int m = sc.nextInt();
            List<String[]> events = new ArrayList<>();
            for (int i = 0; i < m; i++) {
                String type = sc.next();
                events.add(new String[]{type, sc.next(), sc.next()});
            }
            Solution sol = new Solution();
            List<String> results = sol.process(n, events);
            for (String res : results) {
                System.out.println(res);
            }
        }
        sc.close();
    }
}
```

### Python

```python
import sys

# Increase recursion depth just in case
sys.setrecursionlimit(300000)

class DSU:
    def __init__(self, n):
        return 0
    def find(self, i):
        return 0
    def union(self, i, j):
        return 0
    def rollback(self):
        return 0
    def connected(self, i, j):
        return 0
class Solution:
    def process(self, n: int, events: list[list[str]]) -> list[str]:
        return []
    def add_edge(self, tree, node, start, end, l, r, edge):
        return 0
    def dfs(self, tree, node, start, end, dsu, queries, results):
        return 0
def main():
    import sys
    sys.setrecursionlimit(500000)
    def input_gen():
        return 0

        for line in sys.stdin:

            for token in line.split():

                yield token

    it = input_gen()
    n = int(next(it))
    m = int(next(it))
    events = []
    for _ in range(m):
        type = next(it)
        events.append([type, next(it), next(it)])
    
    sol = Solution()
    results = sol.process(n, events)
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <vector>
#include <string>
#include <map>
#include <stack>
#include <algorithm>
#include <iostream>

using namespace std;

struct Edge {
    int u, v;
};

struct DSU {
    vector<int> parent;
    vector<int> rank;
    struct RollbackInfo {
        int child, parent;
    };
    stack<RollbackInfo> history;

    DSU(int n) {
        parent.resize(n + 1);
        rank.resize(n + 1, 1);
        for (int i = 1; i <= n; i++) parent[i] = i;
    }

    int find(int i) {
        if (parent[i] == i) return i;
        return find(parent[i]);
    }

    void unite(int i, int j) {
        int rootI = find(i);
        int rootJ = find(j);
        if (rootI != rootJ) {
            if (rank[rootI] < rank[rootJ]) swap(rootI, rootJ);
            parent[rootJ] = rootI;
            rank[rootI] += rank[rootJ];
            history.push({rootJ, rootI});
        } else {
            history.push({-1, -1});
        }
    }

    void rollback() {
        RollbackInfo op = history.top();
        history.pop();
        if (op.child != -1) {
            parent[op.child] = op.child;
            rank[op.parent] -= rank[op.child];
        }
    }

    bool connected(int i, int j) {
        return find(i) == find(j);
    }
};

class Solution {
    vector<vector<Edge>> tree;
    vector<pair<int, int>> queries;
    vector<string> results;

    void addEdge(int node, int start, int end, int l, int r, Edge e) {
    }

    void dfs(int node, int start, int end, DSU& dsu) {
    }

public:
    vector<string> process(int n, const vector<vector<string>>& events) {
        return "";
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<vector<string>> events(m);
    for (int i = 0; i < m; i++) {
        string type, u, v;
        cin >> type >> u >> v;
        events[i] = {type, u, v};
    }
    Solution sol;
    vector<string> results = sol.process(n, events);
    for (const string& res : results) {
        cout << res << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
class Solution {
  process(n, events) {
    return 0;
  }
}

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => {
  const parts = line.trim().split(/\s+/).filter(x => x !== "");
  for (const p of parts) data.push(p);
});
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const m = parseInt(data[idx++], 10);
  const events = [];
  for (let i = 0; i < m; i++) {
    const type = data[idx++];
    const u = data[idx++];
    const v = data[idx++];
    events.push([type, u, v]);
  }
  const solution = new Solution();
  const out = solution.process(n, events);
  console.log(out.join("\n"));
});
```

