---
problem_id: GRB_DSU_BASICS__1728
display_id: GRB-012
slug: dsu-basics
title: "Disjoint Set Union Basics"
difficulty: Easy
difficulty_score: 30
topics:
  - Graphs
  - DSU
  - Connectivity
tags:
  - graphs-basics
  - dsu
  - connectivity
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# GRB-012: Disjoint Set Union Basics

## Problem Statement

Maintain a set of `n` nodes under two operations:

- `union u v`: connect the sets containing `u` and `v`
- `find u v`: report whether `u` and `v` are in the same set

Answer all queries in order.

![Problem Illustration](../images/GRB-012/problem-illustration.png)

## Input Format

- First line: integers `n` and `q`
- Next `q` lines: queries in one of two forms:
  - `union u v`
  - `find u v`

## Output Format

- For each `find` query, print `true` or `false` on its own line

## Constraints

- `1 <= n <= 200000`
- `1 <= q <= 200000`
- `0 <= u, v < n`

## Example

**Input:**

```
4 3
union 0 1
union 2 3
find 0 3
```

**Output:**

```
false
```

**Explanation:**

Nodes 0 and 3 are in different sets after the two unions.

![Example Visualization](../images/GRB-012/example-1.png)

## Notes

- Use DSU with path compression and union by rank/size.
- The graph is implicit; queries are dynamic.
- Output only for `find` queries.

## Related Topics

Disjoint Set Union, Connectivity Queries

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    class DSU {
        int[] parent;
        int[] rank;

        DSU(int n) {
            parent = new int[n];
            rank = new int[n];
            for (int i = 0; i < n; i++) {
                parent[i] = i;
                rank[i] = 0;
            }
        }

        int find(int i) {
        return 0;
    }

        void union(int i, int j) {
    }
    }

    public List<Boolean> processQueries(int n, String[] type, int[] u, int[] v) {
        return null;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int q = sc.nextInt();
        String[] type = new String[q];
        int[] u = new int[q];
        int[] v = new int[q];
        for (int i = 0; i < q; i++) {
            type[i] = sc.next();
            u[i] = sc.nextInt();
            v[i] = sc.nextInt();
        }

        Solution solution = new Solution();
        List<Boolean> ans = solution.processQueries(n, type, u, v);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < ans.size(); i++) {
            sb.append(ans.get(i) ? "true" : "false");
            if (i + 1 < ans.size()) sb.append('\n');
        }
        System.out.print(sb.toString());
        sc.close();
    }
}
```

### Python

```python
import sys

# Increase recursion depth for deep trees (though path compression prevents this mostly)
sys.setrecursionlimit(200000)

class DSU:
    def __init__(self, n):
        return 0
    def find(self, i):
        return 0
    def union(self, i, j):
        return 0
def process_queries(n: int, queries: list[tuple[str, int, int]]) -> list[bool]:
    return []
def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        q = int(next(iterator))
        queries = []
        for _ in range(q):
            t = next(iterator)
            u = int(next(iterator))
            v = int(next(iterator))
            queries.append((t, u, v))
            
        ans = process_queries(n, queries)
        print("\n".join("true" if x else "false" for x in ans))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <numeric>

using namespace std;

class DSU {
    vector<int> parent;
    vector<int> rank;
public:
    DSU(int n) {
        parent.resize(n);
        iota(parent.begin(), parent.end(), 0);
        rank.assign(n, 0);
    }
    int find(int i) {
        if (parent[i] != i)
            parent[i] = find(parent[i]);
        return parent[i];
    }
    void unite(int i, int j) {
        int rootI = find(i);
        int rootJ = find(j);
        if (rootI != rootJ) {
            if (rank[rootI] < rank[rootJ])
                parent[rootI] = rootJ;
            else if (rank[rootI] > rank[rootJ])
                parent[rootJ] = rootI;
            else {
                parent[rootI] = rootJ;
                rank[rootJ]++;
            }
        }
    }
};

class Solution {
public:
    vector<bool> processQueries(int n, const vector<string>& type,
                                const vector<int>& u, const vector<int>& v) {
        DSU dsu(n);
        vector<bool> results;
        for (size_t i = 0; i < type.size(); ++i) {
            if (type[i] == "union") {
                dsu.unite(u[i], v[i]);
            } else {
                results.push_back(dsu.find(u[i]) == dsu.find(v[i]));
            }
        }
        return results;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;
    vector<string> type(q);
    vector<int> u(q), v(q);
    for (int i = 0; i < q; i++) {
        cin >> type[i] >> u[i] >> v[i];
    }

    Solution solution;
    vector<bool> ans = solution.processQueries(n, type, u, v);
    for (int i = 0; i < (int)ans.size(); i++) {
        cout << (ans[i] ? "true" : "false");
        if (i + 1 < (int)ans.size()) cout << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class DSU {
  constructor(n) {
    this.parent = new Int32Array(n);
    this.rank = new Int32Array(n);
    for (let i = 0; i < n; i++) this.parent[i] = i;
  }
  find(i) {
    if (this.parent[i] !== i) {
      this.parent[i] = this.find(this.parent[i]);
    }
    return this.parent[i];
  }
  union(i, j) {
    const rootI = this.find(i);
    const rootJ = this.find(j);
    if (rootI !== rootJ) {
      if (this.rank[rootI] < this.rank[rootJ]) {
        this.parent[rootI] = rootJ;
      } else if (this.rank[rootI] > this.rank[rootJ]) {
        this.parent[rootJ] = rootI;
      } else {
        this.parent[rootI] = rootJ;
        this.rank[rootJ]++;
      }
    }
  }
}

class Solution {
  processQueries(n, queries) {
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
  const q = parseInt(data[idx++], 10);
  const queries = [];
  for (let i = 0; i < q; i++) {
    const t = data[idx++];
    const u = parseInt(data[idx++], 10);
    const v = parseInt(data[idx++], 10);
    queries.push([t, u, v]);
  }

  const solution = new Solution();
  const ans = solution.processQueries(n, queries);
  console.log(ans.map((x) => (x ? "true" : "false")).join("\n"));
});
```

