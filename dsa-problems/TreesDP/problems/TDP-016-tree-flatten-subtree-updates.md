---
title: "Tree Flatten with Subtree Updates"
problem_id: TDP_TREE_FLATTEN_UPDATES__5418
display_id: TDP-016
difficulty: Medium
tags: [tree-dp, euler-tour, fenwick-tree, range-updates]
slug: tree-flatten-subtree-updates
time_limit: 2000
memory_limit: 256
---

## Problem Description

Support subtree value updates and node value queries on a tree using Euler tour flattening.

## Input Format

- Line 1: N
- Line 2: N node values
- Next N-1 lines: u v (edges)
- Next line: Q
- Q lines: 1 u val (add val to subtree) or 2 u (query node)

## Output Format

For each type 2 query, output node value.

## Examples

### Example 1

**Input:**

```
3
1 2 3
1 2
1 3
3
1 1 5
2 2
2 3
```

**Output:**

```
7
8
```

### Example 2

**Input:**

```
5
10 20 30 40 50
1 2
1 3
2 4
2 5
4
1 2 100
2 4
2 5
2 1
```

**Output:**

```
140
150
10
```

## Constraints

- 1 ≤ N, Q ≤ 200,000
- -10^9 ≤ values, updates ≤ 10^9

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public void build(int n, int[] values, int[][] edges) {
        // Implement here
    }

    public void update(int u, int val) {
        // Implement here
    }

    public long query(int u) {
        // Implement here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();

        int[] values = new int[n];
        for (int i = 0; i < n; i++) {
            values[i] = sc.nextInt();
        }

        int[][] edges = new int[n - 1][2];
        for (int i = 0; i < n - 1; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
        }

        Solution solution = new Solution();
        solution.build(n, values, edges);

        int q = sc.nextInt();
        while (q-- > 0) {
            int type = sc.nextInt();
            if (type == 1) {
                int u = sc.nextInt();
                int val = sc.nextInt();
                solution.update(u, val);
            } else {
                int u = sc.nextInt();
                System.out.println(solution.query(u));
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
    def build(self, n: int, values: List[int], edges: List[List[int]]) -> None:
        # Implement here
        pass

    def update(self, u: int, val: int) -> None:
        # Implement here
        pass

    def query(self, u: int) -> int:
        # Implement here
        return 0

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))

        values = []
        for _ in range(n):
            values.append(int(next(iterator)))

        edges = []
        for _ in range(n - 1):
            u = int(next(iterator))
            v = int(next(iterator))
            edges.append([u, v])

        solution = Solution()
        solution.build(n, values, edges)

        q = int(next(iterator))
        for _ in range(q):
            type = int(next(iterator))
            if type == 1:
                u = int(next(iterator))
                val = int(next(iterator))
                solution.update(u, val)
            else:
                u = int(next(iterator))
                print(solution.query(u))
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
    void build(int n, const vector<int>& values, const vector<vector<int>>& edges) {
        // Implement here
    }

    void update(int u, int val) {
        // Implement here
    }

    long long query(int u) {
        // Implement here
        return 0;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    if (!(cin >> n)) return 0;

    vector<int> values(n);
    for (int i = 0; i < n; i++) {
        cin >> values[i];
    }

    vector<vector<int>> edges(n - 1, vector<int>(2));
    for (int i = 0; i < n - 1; i++) {
        cin >> edges[i][0] >> edges[i][1];
    }

    Solution solution;
    solution.build(n, values, edges);

    int q;
    cin >> q;
    while (q--) {
        int type;
        cin >> type;
        if (type == 1) {
            int u, val;
            cin >> u >> val;
            solution.update(u, val);
        } else {
            int u;
            cin >> u;
            cout << solution.query(u) << "\n";
        }
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  build(n, values, edges) {
    // Implement here
  }

  update(u, val) {
    // Implement here
  }

  query(u) {
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

  const values = [];
  for (let i = 0; i < n; i++) {
    values.push(parseInt(tokens[idx++]));
  }

  const edges = [];
  for (let i = 0; i < n - 1; i++) {
    const u = parseInt(tokens[idx++]);
    const v = parseInt(tokens[idx++]);
    edges.push([u, v]);
  }

  const solution = new Solution();
  solution.build(n, values, edges);

  const q = parseInt(tokens[idx++]);
  for (let i = 0; i < q; i++) {
    const type = parseInt(tokens[idx++]);
    if (type === 1) {
      const u = parseInt(tokens[idx++]);
      const val = parseInt(tokens[idx++]);
      solution.update(u, val);
    } else {
      const u = parseInt(tokens[idx++]);
      console.log(solution.query(u));
    }
  }
});
```

## Hints

<details>
<summary>Hint 1</summary>
Use Euler tour to convert subtree to contiguous range.
</details>
