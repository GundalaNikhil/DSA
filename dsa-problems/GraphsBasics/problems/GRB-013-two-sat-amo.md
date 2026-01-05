---
problem_id: GRB_TWO_SAT_AMO__6607
display_id: GRB-013
slug: two-sat-amo
title: "2-SAT with At-Most-One Constraints"
difficulty: Medium
difficulty_score: 60
topics:
  - Graphs
  - 2-SAT
  - Implication Graph
tags:
  - graphs-basics
  - 2-sat
  - implications
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRB-013: 2-SAT with At-Most-One Constraints

## Problem Statement

You are given a 2-SAT formula with `n` boolean variables `x1..xn`. Each clause is of the form `(a OR b)` where `a` and `b` are literals. Additionally, you are given several **at-most-one** constraints: within each subset, at most one variable can be true.
Determine whether the formula is satisfiable and, if it is, output one valid assignment.
![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/dsa/graph_basics/GRB-013.jpg)

## Input Format

- First line: integers `n` and `m`
- Next `m` lines: two integers `a` and `b` (literals, negative means negation)
- Next line: integer `g`, number of at-most-one groups
- Next `g` lines: integer `k` followed by `k` variable indices (1-based)
  Literals use integers from `1..n` for `xi` and `-i` for `¬xi`.

## Output Format

- If unsatisfiable: print `UNSAT`
- If satisfiable: print `SAT` and then a line of `n` integers (0/1) for `x1..xn`

## Constraints

- `1 <= n <= 100000`
- `0 <= m <= 200000`
- Total size of all groups `<= 200000`

## Example

**Input:**

```
2 1
1 2
1
2 1 2
```

**Output:**

```
SAT
1 0
```

**Explanation:**
Clause `(x1 OR x2)` and at-most-one `{x1,x2}` allow either variable to be true.
![Example Visualization](../images/GRB-013/example-1.png)

## Notes

- Encode each clause into an implication graph.
- Encode at-most-one constraints with pairwise implications.
- Use SCC to solve 2-SAT and produce an assignment.

## Related Topics

## 2-SAT, Implication Graph, SCC

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public void solveTwoSat(int n, int m, int[][] clauses, int g, int[][] amoGroups) {
        // Implement here
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String nmLine = br.readLine();
        if (nmLine == null) return;
        String[] nm = nmLine.trim().split("\\s+");
        int n = Integer.parseInt(nm[0]);
        int m = Integer.parseInt(nm[1]);

        int[][] clauses = new int[m][2];
        for (int i = 0; i < m; i++) {
            String[] line = br.readLine().trim().split("\\s+");
            clauses[i][0] = Integer.parseInt(line[0]);
            clauses[i][1] = Integer.parseInt(line[1]);
        }

        String gLine = br.readLine();
        if (gLine == null) return;
        int g = Integer.parseInt(gLine.trim());
        int[][] amoGroups = new int[g][];
        for (int i = 0; i < g; i++) {
            String[] line = br.readLine().trim().split("\\s+");
            int k = Integer.parseInt(line[0]);
            amoGroups[i] = new int[k];
            for (int j = 0; j < k; j++) {
                amoGroups[i][j] = Integer.parseInt(line[j + 1]);
            }
        }

        Solution sol = new Solution();
        sol.solveTwoSat(n, m, clauses, g, amoGroups);
    }
}
```

### Python

```python
import sys

# Increase recursion depth for deep DFS (SCC) trees
sys.setrecursionlimit(500000)

class Solution:
    def solve_two_sat(self, n, m, clauses, g, amo_groups):
        # Implement here
        pass

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])

    idx = 2
    clauses = []
    for _ in range(m):
        a = int(input_data[idx])
        b = int(input_data[idx+1])
        clauses.append((a, b))
        idx += 2

    g = int(input_data[idx])
    idx += 1
    amo_groups = []
    for _ in range(g):
        k = int(input_data[idx])
        idx += 1
        group = []
        for _ in range(k):
            group.append(int(input_data[idx]))
            idx += 1
        amo_groups.append(group)

    sol = Solution()
    sol.solve_two_sat(n, m, clauses, g, amo_groups)

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    void solveTwoSat(int n, int m, vector<pair<int, int>>& clauses, int g, vector<vector<int>>& amoGroups) {
        // Implement here
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<pair<int, int>> clauses(m);
    for (int i = 0; i < m; i++) {
        cin >> clauses[i].first >> clauses[i].second;
    }

    int g;
    if (!(cin >> g)) return 0;
    vector<vector<int>> amoGroups(g);
    for (int i = 0; i < g; i++) {
        int k;
        cin >> k;
        amoGroups[i].resize(k);
        for (int j = 0; j < k; j++) {
            cin >> amoGroups[i][j];
        }
    }

    Solution sol;
    sol.solveTwoSat(n, m, clauses, g, amoGroups);

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  solveTwoSat(n, m, clauses, g, amoGroups) {
    // Implement here
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const m = parseInt(input[idx++]);

  const clauses = [];
  for (let i = 0; i < m; i++) {
    const a = parseInt(input[idx++]);
    const b = parseInt(input[idx++]);
    clauses.push([a, b]);
  }

  const g = parseInt(input[idx++]);
  const amoGroups = [];
  for (let i = 0; i < g; i++) {
    const k = parseInt(input[idx++]);
    const group = [];
    for (let j = 0; j < k; j++) {
      group.push(parseInt(input[idx++]));
    }
    amoGroups.push(group);
  }

  const sol = new Solution();
  sol.solveTwoSat(n, m, clauses, g, amoGroups);
}

solve();
```
