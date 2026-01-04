---
title: "Centroid Decomposition with Time-Decay Queries"
problem_id: TDP_CENTROID_TIME_DECAY__9247
display_id: TDP-014
difficulty: Hard
tags: [tree-dp, centroid-decomposition, time-decay, advanced]
slug: centroid-decomp-time-decay
time_limit: 2000
memory_limit: 256
---

## Problem Description

Weighted tree with node values and timestamps. Query: find minimum (distance × decay + value) to any marked node.

## Input Format

- Line 1: N D (nodes, decay constant)
- Next N-1 lines: u v w (edges)
- Next line: Q (queries)
- Q lines: type params

## Output Format

Per query output.

## Examples

### Example 1

**Input:**

```
3 1000
1 2 10
2 3 20
2
1 1 100 0
2 2 0
```

**Output:**

```
110
```

### Example 2

**Input:**

```
5 500
1 2 5
1 3 10
2 4 7
2 5 3
3
1 1 50 0
1 4 80 0
2 5 0
```

**Output:**

```
62
```

## Constraints

- 1 ≤ N ≤ 100,000
- 1 ≤ Q ≤ 100,000

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public void build(int n, int D, int[][] edges) {
        // Implement here
    }

    public void update(int v, long val, int t) {
        // Implement here
    }

    public long query(int v, int t) {
        // Implement here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int D = sc.nextInt();

        int[][] edges = new int[n - 1][3];
        for (int i = 0; i < n - 1; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
            edges[i][2] = sc.nextInt();
        }

        Solution solution = new Solution();
        solution.build(n, D, edges);

        int q = sc.nextInt();
        while (q-- > 0) {
            int type = sc.nextInt();
            if (type == 1) {
                int v = sc.nextInt();
                long val = sc.nextLong();
                int t = sc.nextInt();
                solution.update(v, val, t);
            } else {
                int v = sc.nextInt();
                int t = sc.nextInt();
                System.out.println(solution.query(v, t));
            }
        }
    }
}
```

### Python

```python
from typing import List
import sys

sys.setrecursionlimit(200000)

class Solution:
    def build(self, n: int, D: int, edges: List[List[int]]) -> None:
        # Implement here
        pass

    def update(self, v: int, val: int, t: int) -> None:
        # Implement here
        pass

    def query(self, v: int, t: int) -> int:
        # Implement here
        return 0

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        D = int(next(iterator))

        edges = []
        for _ in range(n - 1):
            u = int(next(iterator))
            v = int(next(iterator))
            w = int(next(iterator))
            edges.append([u, v, w])

        solution = Solution()
        solution.build(n, D, edges)

        q = int(next(iterator))
        for _ in range(q):
            type = int(next(iterator))
            if type == 1:
                v = int(next(iterator))
                val = int(next(iterator))
                t = int(next(iterator))
                solution.update(v, val, t)
            else:
                v = int(next(iterator))
                t = int(next(iterator))
                print(solution.query(v, t))
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
    void build(int n, int D, const vector<vector<int>>& edges) {
        // Implement here
    }

    void update(int v, long long val, int t) {
        // Implement here
    }

    long long query(int v, int t) {
        // Implement here
        return 0;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n, D;
    if (!(cin >> n >> D)) return 0;

    vector<vector<int>> edges(n - 1, vector<int>(3));
    for (int i = 0; i < n - 1; i++) {
        cin >> edges[i][0] >> edges[i][1] >> edges[i][2];
    }

    Solution solution;
    solution.build(n, D, edges);

    int q;
    cin >> q;
    while (q--) {
        int type;
        cin >> type;
        if (type == 1) {
            int v, t;
            long long val;
            cin >> v >> val >> t;
            solution.update(v, val, t);
        } else {
            int v, t;
            cin >> v >> t;
            cout << solution.query(v, t) << "\n";
        }
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  build(n, D, edges) {
    // Implement here
  }

  update(v, val, t) {
    // Implement here
  }

  query(v, t) {
    // Implement here
    return 0;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const lines = [];
rl.on("line", (line) => {
  lines.push(line);
}).on("close", () => {
  const tokens = lines
    .join(" ")
    .split(/\s+/)
    .filter((t) => t !== "");
  if (tokens.length === 0) return;

  let idx = 0;
  const n = parseInt(tokens[idx++]);
  const D = parseInt(tokens[idx++]);

  const edges = [];
  for (let i = 0; i < n - 1; i++) {
    const u = parseInt(tokens[idx++]);
    const v = parseInt(tokens[idx++]);
    const w = parseInt(tokens[idx++]);
    edges.push([u, v, w]);
  }

  const solution = new Solution();
  solution.build(n, D, edges);

  const q = parseInt(tokens[idx++]);
  for (let i = 0; i < q; i++) {
    const type = parseInt(tokens[idx++]);
    if (type === 1) {
      const v = parseInt(tokens[idx++]);
      const val = parseInt(tokens[idx++]);
      const t = parseInt(tokens[idx++]);
      solution.update(v, val, t);
    } else {
      const v = parseInt(tokens[idx++]);
      const t = parseInt(tokens[idx++]);
      console.log(solution.query(v, t));
    }
  }
});
```

## Hints

<details>
<summary>Hint 1</summary>
Use centroid decomposition for tree queries.
</details>
