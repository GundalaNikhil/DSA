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
import java.io.*;

class Solution {
    public void processQueries(int n, int q, List<Query> queries) {
        // Implement here
    }

    static class Query {
        String type;
        int u, v;
        Query(String type, int u, int v) {
            this.type = type;
            this.u = u;
            this.v = v;
        }
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String nqLine = br.readLine();
        if (nqLine == null) return;
        String[] nq = nqLine.trim().split("\\s+");
        int n = Integer.parseInt(nq[0]);
        int q = Integer.parseInt(nq[1]);

        List<Solution.Query> queries = new ArrayList<>();
        for (int i = 0; i < q; i++) {
            String[] line = br.readLine().trim().split("\\s+");
            queries.add(new Solution.Query(line[0], Integer.parseInt(line[1]), Integer.parseInt(line[2])));
        }

        Solution sol = new Solution();
        sol.processQueries(n, q, queries);
    }
}
```

### Python

```python
import sys

class Solution:
    def process_queries(self, n, q, queries):
        # Implement here
        pass

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    q = int(input_data[1])

    queries = []
    idx = 2
    for _ in range(q):
        q_type = input_data[idx]
        u = int(input_data[idx+1])
        v = int(input_data[idx+2])
        queries.append((q_type, u, v))
        idx += 3

    sol = Solution()
    sol.process_queries(n, q, queries)

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

struct Query {
    string type;
    int u, v;
};

class Solution {
public:
    void processQueries(int n, int q, vector<Query>& queries) {
        // Implement here
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<Query> queries(q);
    for (int i = 0; i < q; i++) {
        cin >> queries[i].type >> queries[i].u >> queries[i].v;
    }

    Solution sol;
    sol.processQueries(n, q, queries);

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  processQueries(n, q, queries) {
    // Implement here
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const q = parseInt(input[idx++]);

  const queries = [];
  for (let i = 0; i < q; i++) {
    const type = input[idx++];
    const u = parseInt(input[idx++]);
    const v = parseInt(input[idx++]);
    queries.push({ type, u, v });
  }

  const sol = new Solution();
  sol.processQueries(n, q, queries);
}

solve();
```
