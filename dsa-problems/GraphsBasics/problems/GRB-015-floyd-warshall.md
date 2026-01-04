---
problem_id: GRB_FLOYD_WARSHALL__9386
display_id: GRB-015
slug: floyd-warshall
title: "Floyd-Warshall All-Pairs"
difficulty: Medium
difficulty_score: 48
topics:
  - Graphs
  - Floyd-Warshall
  - Shortest Path
tags:
  - graphs-basics
  - floyd-warshall
  - shortest-path
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRB-015: Floyd-Warshall All-Pairs

## Problem Statement

Given a directed weighted graph with up to 500 nodes, compute the shortest path distance between every pair of nodes using the Floyd-Warshall algorithm.

If a negative cycle exists, output `NEGATIVE CYCLE`.

![Problem Illustration](../images/GRB-015/problem-illustration.png)

## Input Format

- First line: integer `n`
- Next `n` lines: `n` integers each, the adjacency matrix

For `i != j`, a value of `-1` means no direct edge. The diagonal entries are `0`.

## Output Format

- If a negative cycle exists: print `NEGATIVE CYCLE`
- Otherwise: print the `n x n` distance matrix, with `-1` for unreachable pairs

## Constraints

- `1 <= n <= 500`
- Edge weights are in `[-10^9, 10^9]`

## Example

**Input:**

```
3
0 1 4
-1 0 2
-1 -1 0
```

**Output:**

```
0 1 3
-1 0 2
-1 -1 0
```

**Explanation:**

The shortest path from 0 to 2 goes through 1 with total cost 3.

![Example Visualization](../images/GRB-015/example-1.png)

## Notes

- Use 64-bit integers to avoid overflow.
- After running, if any `dist[i][i] < 0`, a negative cycle exists.
- Keep `-1` for unreachable pairs.

## Related Topics

Floyd-Warshall, APSP, Dynamic Programming

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public long[][] floydWarshall(int n, long[][] dist) {
        // Implement here
        return new long[0][0];
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String nLine = br.readLine();
        if (nLine == null) return;
        int n = Integer.parseInt(nLine.trim());

        long[][] dist = new long[n][n];
        for (int i = 0; i < n; i++) {
            String[] line = br.readLine().trim().split("\\s+");
            for (int j = 0; j < n; j++) {
                dist[i][j] = Long.parseLong(line[j]);
            }
        }

        Solution sol = new Solution();
        long[][] result = sol.floydWarshall(n, dist);

        if (result == null || result.length == 0) {
            System.out.println("NEGATIVE CYCLE");
        } else {
            PrintWriter out = new PrintWriter(System.out);
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    out.print(result[i][j] + (j == n - 1 ? "" : " "));
                }
                out.println();
            }
            out.flush();
        }
    }
}
```

### Python

```python
import sys

class Solution:
    def floyd_warshall(self, n, dist):
        # Implement here
        return None

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    idx = 1
    dist = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(int(input_data[idx]))
            idx += 1
        dist.append(row)

    sol = Solution()
    result = sol.floyd_warshall(n, dist)

    if result is None:
        print("NEGATIVE CYCLE")
    else:
        for row in result:
            print(*(row))

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
    vector<vector<long long>> floydWarshall(int n, vector<vector<long long>>& dist) {
        // Implement here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<long long>> dist(n, vector<long long>(n));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> dist[i][j];
        }
    }

    Solution sol;
    vector<vector<long long>> result = sol.floydWarshall(n, dist);

    if (result.empty()) {
        cout << "NEGATIVE CYCLE" << endl;
    } else {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cout << result[i][j] << (j == n - 1 ? "" : " ");
            }
            cout << endl;
        }
    }

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  floydWarshall(n, dist) {
    // Implement here
    return null;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 1) return;

  let idx = 0;
  const n = parseInt(input[idx++]);

  const dist = [];
  for (let i = 0; i < n; i++) {
    const row = [];
    for (let j = 0; j < n; j++) {
      row.push(BigInt(input[idx++]));
    }
    dist.push(row);
  }

  const sol = new Solution();
  const result = sol.floydWarshall(n, dist);

  if (result === null) {
    process.stdout.write("NEGATIVE CYCLE\n");
  } else {
    for (let i = 0; i < n; i++) {
      process.stdout.write(result[i].join(" ") + "\n");
    }
  }
}

solve();
```
