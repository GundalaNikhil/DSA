---
title: Distance-2 Independent Set on Tree
problem_id: TDP_DISTANCE2_INDEPENDENT_SET__8395
display_id: TDP-007
difficulty: Medium
time_limit: 2000
memory_limit: 256
tags:
  - Tree DP
  - Independent Set
  - Optimization
categories:
  - Algorithms
  - Data Structures
slug: tree-independent-set-distance2
---

# Distance-2 Independent Set on Tree

## Problem Description

Given a tree with `n` nodes where each node `i` has a weight `w[i]`, find the maximum total weight of a subset of nodes such that any two chosen nodes are at distance **at least 3**.

Two nodes are at distance at least 3 if they are not adjacent AND do not share a common neighbor.

## Input Format

- First line: integer `n`
- Second line: `n` space-separated integers `w[1], w[2], ..., w[n]`
- Next `n-1` lines: edges `u v`

## Output Format

- Single integer: maximum total weight

## Constraints

- `1 <= n <= 2 x 10^5`
- `1 <= w[i] <= 10^9`

## Example 1

**Input:**

```
3
1 2 3
1 2
1 3
```

**Output:**

```
3
```

**Explanation:** Can only pick node 3 (or any single node). Nodes 2 and 3 share neighbor 1, so can't pick both.

## Example 2

**Input:**

```
5
10 20 30 40 50
1 2
2 3
3 4
4 5
```

**Output:**

```
60
```

**Explanation:** Pick nodes 1 and 4 (or 2 and 5): 10+50=60 or 20+40=60.

## Solution Template

### Java

```java
import java.util.*;

class Main {
    static List<Integer>[] graph;
    static long[] weight;
    static long[][] dp;
    static int n;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();

        weight = new long[n + 1];
        for (int i = 1; i <= n; i++) {
            weight[i] = sc.nextLong();
        }

        graph = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < n - 1; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            graph[u].add(v);
            graph[v].add(u);
        }

        dp = new long[n + 1][3];

        dfs(1, -1);

        long result = Math.max(dp[1][0], Math.max(dp[1][1], dp[1][2]));
        System.out.println(result);

        sc.close();
    }


    static void dfs(int u, int parent) {

        //Implement here

    }

}
```

### Python

```python
import sys
sys.setrecursionlimit(300000)

def solve():
    # //Implement here
    return 0
solve()


def main():
    import sys
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    # TODO: Parse input and call solution
    pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <cmath>
#include <cstring>
#include <climits>
using namespace std;

const int MAXN = 200005;
vector<int> graph[MAXN];
long long weight[MAXN];
long long dp[MAXN][3];
int n;


void dfs(int u, int parent) {

    //Implement here

}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n;

    for (int i = 1; i <= n; i++) {
        cin >> weight[i];
    }

    for (int i = 0; i < n - 1; i++) {
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    dfs(1, -1);

    long long result = max({dp[1][0], dp[1][1], dp[1][2]});
    cout << result << endl;

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let lines = [];
rl.on("line", (line) => {
  lines.push(line);
}).on("close", () => {
  solve();
});

function solve() {
  //Implement here
  return 0;
}
```
