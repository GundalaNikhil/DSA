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

class Solution {
    public long[][] floydWarshall(long[][] dist) {
        // Implementation here
        return new long[0][0];
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        long[][] dist = new long[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                dist[i][j] = sc.nextLong();
            }
        }

        Solution solution = new Solution();
        long[][] ans = solution.floydWarshall(dist);
        if (ans == null) {
            System.out.print("NEGATIVE CYCLE");
        } else {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (j > 0) sb.append(' ');
                    sb.append(ans[i][j]);
                }
                if (i + 1 < n) sb.append('\n');
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

def floyd_warshall(dist: list[list[int]]):
    # Implementation here
    return None

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        dist = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                dist[i][j] = int(next(iterator))
                
        ans = floyd_warshall(dist)
        if ans is None:
            print("NEGATIVE CYCLE")
        else:
            out = []
            for i in range(n):
                out.append(" ".join(str(x) for x in ans[i]))
            print("\n".join(out))
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
public:
    public:
    vector<vector<long long>> floydWarshall(vector<vector<long long>> dist) {
        // Implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<vector<long long>> dist(n, vector<long long>(n));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> dist[i][j];
        }
    }

    Solution solution;
    vector<vector<long long>> ans = solution.floydWarshall(dist);
    if (ans.empty()) {
        cout << "NEGATIVE CYCLE";
    } else {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (j) cout << ' ';
                cout << ans[i][j];
            }
            if (i + 1 < n) cout << "\n";
        }
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  floydWarshall(dist) {
    // Implementation here
    return null;
  }
}

class Solution {
  floydWarshall(dist) {
    const n = dist.length;
    const INF = 1e15; // Safe large number

    // Preprocess
    for (let i = 0; i < n; i++) {
      for (let j = 0; j < n; j++) {
        if (i !== j && dist[i][j] === -1) {
          dist[i][j] = INF;
        }
      }
    }

    for (let k = 0; k < n; k++) {
      for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
          if (dist[i][k] !== INF && dist[k][j] !== INF) {
            if (dist[i][k] + dist[k][j] < dist[i][j]) {
              dist[i][j] = dist[i][k] + dist[k][j];
            }
          }
        }
      }
    }

    // Negative Cycle Check
    for (let i = 0; i < n; i++) {
      if (dist[i][i] < 0) return null;
    }

    // Postprocess
    for (let i = 0; i < n; i++) {
      for (let j = 0; j < n; j++) {
        if (dist[i][j] >= INF / 2) {
          dist[i][j] = -1;
        }
      }
    }

    return dist;
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
  const dist = Array.from({ length: n }, () => new Array(n).fill(0));
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      dist[i][j] = parseInt(data[idx++], 10);
    }
  }

  const solution = new Solution();
  const ans = solution.floydWarshall(dist);
  if (ans === null) {
    console.log("NEGATIVE CYCLE");
  } else {
    const out = [];
    for (let i = 0; i < n; i++) {
      out.push(ans[i].join(" "));
    }
    console.log(out.join("\n"));
  }
});
```
