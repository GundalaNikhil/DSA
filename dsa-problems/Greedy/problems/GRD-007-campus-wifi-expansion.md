---
problem_id: GRD_CAMPUS_WIFI_EXPANSION__4892
display_id: GRD-007
slug: campus-wifi-expansion
title: "Campus Wi-Fi Expansion"
difficulty: Medium
difficulty_score: 55
topics:
  - Greedy Algorithms
  - Minimum Spanning Tree
  - Kruskal's Algorithm
tags:
  - greedy
  - mst
  - kruskal
  - graph
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRD-007: Campus Wi-Fi Expansion

## Problem Statement

You need to connect `n` buildings on campus with network cables. Some buildings may already have cable connections between them (at no additional cost).

For buildings that aren't connected, laying a new cable between buildings `i` and `j` costs `|h[i] - h[j]|`, where `h[i]` is the height of building `i`.

Your goal is to find the minimum total cost to ensure all buildings are connected (directly or indirectly) to the same network.

![Problem Illustration](../images/GRD-007/problem-illustration.png)

## Input Format

- First line: integer `n` (number of buildings)
- Second line: `n` space-separated integers representing building heights `h[0], h[1], ..., h[n-1]`
- Third line: integer `m` (number of existing free cables)
- Next `m` lines: two integers `u v` representing an existing cable between buildings `u` and `v`

## Output Format

- Single integer: minimum total cost to connect all buildings

## Constraints

- `1 <= n <= 10^5`
- `1 <= h[i] <= 10^9`
- `0 <= m < n`
- `0 <= u, v < n`

## Example

**Input:**

```
3
5 1 9
0
```

**Output:**

```
8
```

**Explanation:**

Buildings with heights: [5, 1, 9]
No existing cables (m = 0)

Need to connect all 3 buildings. Possible edges:

- Building 0 to Building 1: cost = |5 - 1| = 4
- Building 0 to Building 2: cost = |5 - 9| = 4
- Building 1 to Building 2: cost = |1 - 9| = 8

Using Minimum Spanning Tree (MST):

- Connect buildings 0 and 1: cost = 4
- Connect buildings 0 and 2: cost = 4
- Total cost = 8

![Example Visualization](../images/GRD-007/example-1.png)

## Notes

- This is a Minimum Spanning Tree (MST) problem
- Existing cables are free (cost = 0) and should be used first
- For new cables, generate all possible edges with costs |h[i] - h[j]|
- Use Kruskal's algorithm with Union-Find
- Optimization: Sort buildings by height and only consider edges between adjacent buildings in sorted order
- Time complexity: O(n² log n) for generating all edges, or O(n log n) with optimization

## Related Topics

Minimum Spanning Tree, Kruskal's Algorithm, Greedy Algorithms, Union-Find, Graph Theory

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public long minCostToConnect(int n, long[] h, int m, int[][] freeCables) {
        // Implement here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String nLine = br.readLine();
        if (nLine == null) return;
        int n = Integer.parseInt(nLine.trim());

        long[] h = new long[n];
        String[] hLine = br.readLine().trim().split("\\s+");
        for (int i = 0; i < n; i++) h[i] = Long.parseLong(hLine[i]);

        String mLine = br.readLine();
        if (mLine == null) return;
        int m = Integer.parseInt(mLine.trim());

        int[][] freeCables = new int[m][2];
        for (int i = 0; i < m; i++) {
            String[] cableLine = br.readLine().trim().split("\\s+");
            freeCables[i][0] = Integer.parseInt(cableLine[0]);
            freeCables[i][1] = Integer.parseInt(cableLine[1]);
        }

        Solution sol = new Solution();
        System.out.println(sol.minCostToConnect(n, h, m, freeCables));
    }
}
```

### Python

```python
import sys

class Solution:
    def min_cost_to_connect(self, n, h, m, free_cables):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    h = list(map(int, input_data[1:1+n]))
    idx = 1 + n
    m = int(input_data[idx])
    idx += 1
    free_cables = []
    for _ in range(m):
        free_cables.append([int(input_data[idx]), int(input_data[idx+1])])
        idx += 2

    sol = Solution()
    print(sol.min_cost_to_connect(n, h, m, free_cables))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    long long minCostToConnect(int n, vector<long long>& h, int m, vector<vector<int>>& freeCables) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> h(n);
    for (int i = 0; i < n; i++) cin >> h[i];

    int m;
    if (!(cin >> m)) return 0;

    vector<vector<int>> freeCables(m, vector<int>(2));
    for (int i = 0; i < m; i++) {
        cin >> freeCables[i][0] >> freeCables[i][1];
    }

    Solution sol;
    cout << sol.minCostToConnect(n, h, m, freeCables) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  minCostToConnect(n, h, m, freeCables) {
    // Implement here
    return 0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 1) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const h = [];
  for (let i = 0; i < n; i++) h.push(BigInt(input[idx++]));

  const m = parseInt(input[idx++]);
  const freeCables = [];
  for (let i = 0; i < m; i++) {
    freeCables.push([parseInt(input[idx++]), parseInt(input[idx++])]);
  }

  const sol = new Solution();
  console.log(sol.minCostToConnect(n, h, m, freeCables).toString());
}

solve();
```
