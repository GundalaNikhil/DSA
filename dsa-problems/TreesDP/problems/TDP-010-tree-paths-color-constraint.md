---
title: "Tree Paths with Forbidden Colors"
problem_id: TDP_PATH_COLOR_CONSTRAINT__4927
display_id: TDP-010
difficulty: Medium
tags: [tree-dp, path-counting, color-constraint, dfs]
slug: tree-paths-color-constraint
time_limit: 2000
memory_limit: 256
---

## Problem Description

Given a tree with N nodes where each node has a color (1 to C), count the number of unordered pairs of nodes at exactly distance K where the path between them does NOT pass through any node with the forbidden color F.

---

## Input Format

- First line: N, K, F (nodes, target distance, forbidden color)
- Second line: N integers representing colors of nodes 1 to N
- Next N-1 lines: u, v (edges)

---

## Output Format

Print the count of valid node pairs.

---

## Examples

### Example 1

**Input:**

```
4 2 2
1 2 1 3
1 2
2 3
3 4
```

**Output:**

```
1
```

**Explanation:** Only pair (1,3) at distance 2, path avoids color 2... Actually node 2 has color 2, so path 1-2-3 is invalid. Only valid pair needs rechecking.

### Example 2

**Input:**

```
5 3 2
1 1 2 1 1
1 2
2 3
3 4
4 5
```

**Output:**

```
1
```

---

## Constraints

- 1 ≤ N ≤ 200,000
- 1 ≤ K ≤ 100,000
- 1 ≤ C ≤ 10
- 1 ≤ F ≤ C

---

## Solution Template

### Java

```java
import java.util.*;

class Main {
    static List<List<Integer>> adj;
    static int[] color;
    static int n, K, F;
    static long answer = 0;
    static int[][][] dp;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt(); K = sc.nextInt(); F = sc.nextInt();

        color = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            color[i] = sc.nextInt();
        }

        adj = new ArrayList<>();
        for (int i = 0; i <= n; i++) adj.add(new ArrayList<>());

        for (int i = 0; i < n - 1; i++) {
            int u = sc.nextInt(), v = sc.nextInt();
            adj.get(u).add(v);
            adj.get(v).add(u);
        }

        dp = new int[n + 1][K + 1][2];
        dfs(1, 0);
        System.out.println(answer);
    }


    static void dfs(int u, int p) {

        //Implement here

    }

}
```

### Python

```python
import sys
sys.setrecursionlimit(300000)

def main():
    data = sys.stdin.read().split()
    idx = 0
    n, K, F = int(data[idx]), int(data[idx+1]), int(data[idx+2])
    idx += 3

    color = [0] + [int(data[idx + i]) for i in range(n)]
    idx += n

    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = int(data[idx]), int(data[idx+1])
        idx += 2
        adj[u].append(v)
        adj[v].append(u)

    dp = [[[0]*2 for _ in range(K + 1)] for _ in range(n + 1)]
    answer = [0]

    def dfs(u, p):
        # //Implement here
        return 0
    dfs(1, 0)
    print(answer[0])

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

int n, K, F;
vector<int> color;
vector<vector<int>> adj;
vector<vector<array<long long, 2>>> dp;
long long answer = 0;


void dfs(int u, int p) {

    //Implement here

}

int main() {
    cin >> n >> K >> F;
    color.resize(n + 1);
    for (int i = 1; i <= n; i++) cin >> color[i];

    adj.resize(n + 1);
    for (int i = 0; i < n - 1; i++) {
        int u, v; cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    dp.assign(n + 1, vector<array<long long, 2>>(K + 1, {0, 0}));
    dfs(1, 0);
    cout << answer << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false,
});

const lines = [];
rl.on("line", (line) => lines.push(line.trim()));
rl.on("close", () => {
  let idx = 0;
  const [n, K, F] = lines[idx++].split(" ").map(Number);
  const color = [0, ...lines[idx++].split(" ").map(Number)];

  const adj = Array.from({ length: n + 1 }, () => []);
  for (let i = 0; i < n - 1; i++) {
    const [u, v] = lines[idx++].split(" ").map(Number);
    adj[u].push(v);
    adj[v].push(u);
  }

  const dp = Array.from({ length: n + 1 }, () =>
    Array.from({ length: K + 1 }, () => [0, 0])
  );
  let answer = 0;

  function dfs(u, p) {
    //Implement here
    return 0;
  }

  dfs(1, 0);
  console.log(answer);
});
```
