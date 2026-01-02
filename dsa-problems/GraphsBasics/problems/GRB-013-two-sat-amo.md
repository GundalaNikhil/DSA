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
![Problem Illustration](../images/GRB-013/problem-illustration.png)
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
2-SAT, Implication Graph, SCC
---
## Solution Template

### Java

```java
import java.util.*;

class Solution {
    private List<List<Integer>> adj;
    private List<List<Integer>> revAdj;
    private List<Integer> order;
    private boolean[] visited;
    private int[] component;
    private int numVars;

    public int[] solveTwoSat(int n, int[][] clauses, List<int[]> groups) {
        return null;
    }

    private void addClause(int a, int b, int N) {
    }
    
    private void addImplication(int a, int b, int N) {
    }

    private void addEdge(int u, int v) {
    }

    private int map(int literal, int N) {
        return 0;
    }

    private int neg(int literal, int N) {
        return 0;
    }

    private void dfs1(int u) {
    }

    private void dfs2(int u, int c) {
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[][] clauses = new int[m][2];
        for (int i = 0; i < m; i++) {
            clauses[i][0] = sc.nextInt();
            clauses[i][1] = sc.nextInt();
        }
        int g = sc.nextInt();
        List<int[]> groups = new ArrayList<>();
        for (int i = 0; i < g; i++) {
            int k = sc.nextInt();
            int[] vars = new int[k];
            for (int j = 0; j < k; j++) vars[j] = sc.nextInt();
            groups.add(vars);
        }

        Solution solution = new Solution();
        int[] assign = solution.solveTwoSat(n, clauses, groups);
        if (assign == null) {
            System.out.print("UNSAT");
        } else {
            StringBuilder sb = new StringBuilder();
            sb.append("SAT\n");
            for (int i = 0; i < n; i++) {
                if (i > 0) sb.append(' ');
                sb.append(assign[i]);
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

# Increase recursion depth
sys.setrecursionlimit(400000)

def solve_two_sat(n: int, clauses: list[tuple[int, int]], groups: list[list[int]]):
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
        clauses = []
        for _ in range(m):
            a = int(next(iterator))
            b = int(next(iterator))
            clauses.append((a, b))
            
        g = int(next(iterator))
        groups = []
        for _ in range(g):
            k = int(next(iterator))
            vars_list = [int(next(iterator)) for _ in range(k)]
            groups.append(vars_list)
            
        assign = solve_two_sat(n, clauses, groups)
        if assign is None:
            print("UNSAT")
        else:
            print("SAT")
            print(" ".join(map(str, assign)))
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

using namespace std;

class Solution {
    vector<vector<int>> adj, revAdj;
    vector<int> order, component;
    vector<bool> visited;
    int N;

    int map(int literal) {
        return 0;
    }

    int neg(int literal) {
        return 0;
    }

    void addEdge(int u, int v) {
    }

    void addImplication(int a, int b) {
    }

    void dfs1(int u) {
    }

    void dfs2(int u, int c) {
    }

public:
    vector<int> solveTwoSat(int n, const vector<pair<int, int>>& clauses,
                            const vector<vector<int>>& groups) {
        int totalGroupSize = 0;
        for (const auto& g : groups) totalGroupSize += g.size();

        N = n + totalGroupSize;
        int totalNodes = 2 * N + 2;

        adj.assign(totalNodes, vector<int>());
        revAdj.assign(totalNodes, vector<int>());

        // Clauses
        for (const auto& p : clauses) {
            // a OR b <=> ¬a -> b
            addImplication(-p.first, p.second);
        }

        // AMO
        int currentAux = n + 1;
        for (const auto& group : groups) {
            int k = group.size();
            if (k <= 1) continue;

            for (int i = 0; i < k; i++) {
                int x = group[i];
                int p = currentAux + i;

                // x -> P_i
                addImplication(x, p);

                // P_i -> P_{i+1}
                if (i < k - 1) {
                    addImplication(p, p + 1);
                }

                // P_{i-1} -> ¬x
                if (i > 0) {
                    addImplication(p - 1, -x);
                }
            }
            currentAux += k;
        }

        // SCC
        visited.assign(totalNodes, false);
        order.clear();
        for (int i = 1; i <= 2 * N; i++) {
            if (!visited[i]) dfs1(i);
        }

        reverse(order.begin(), order.end());
        component.assign(totalNodes, -1);
        int compCount = 0;

        for (int u : order) {
            if (component[u] == -1) {
                dfs2(u, compCount++);
            }
        }

        vector<int> result;
        for (int i = 1; i <= n; i++) {
            if (component[i] == component[i + N]) return {};
            result.push_back(component[i] > component[i + N] ? 1 : 0);
        }
        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<pair<int, int>> clauses(m);
    for (int i = 0; i < m; i++) {
        cin >> clauses[i].first >> clauses[i].second;
    }
    int g;
    cin >> g;
    vector<vector<int>> groups(g);
    for (int i = 0; i < g; i++) {
        int k;
        cin >> k;
        groups[i].resize(k);
        for (int j = 0; j < k; j++) cin >> groups[i][j];
    }

    Solution solution;
    vector<int> assign = solution.solveTwoSat(n, clauses, groups);
    if (assign.empty()) {
        cout << "UNSAT";
    } else {
        cout << "SAT\n";
        for (int i = 0; i < n; i++) {
            if (i) cout << ' ';
            cout << assign[i];
        }
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  solveTwoSat(n, clauses, groups) {
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
  const clauses = [];
  for (let i = 0; i < m; i++) {
    const a = parseInt(data[idx++], 10);
    const b = parseInt(data[idx++], 10);
    clauses.push([a, b]);
  }
  const g = parseInt(data[idx++], 10);
  const groups = [];
  for (let i = 0; i < g; i++) {
    const k = parseInt(data[idx++], 10);
    const varsList = [];
    for (let j = 0; j < k; j++) varsList.push(parseInt(data[idx++], 10));
    groups.push(varsList);
  }

  const solution = new Solution();
  const assign = solution.solveTwoSat(n, clauses, groups);
  if (assign === null) {
    console.log("UNSAT");
  } else {
    console.log("SAT");
    console.log(assign.join(" "));
  }
});
```

