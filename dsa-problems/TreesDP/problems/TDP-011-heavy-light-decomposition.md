---
title: "Heavy-Light Decomposition Basics"
problem_id: TDP_HEAVY_LIGHT_DECOMP__8154
display_id: TDP-011
difficulty: Medium
tags: [tree-dp, heavy-light-decomposition, path-queries, segment-tree]
slug: heavy-light-decomposition
time_limit: 2000
memory_limit: 256
---

## Problem Description

Given a weighted tree, preprocess it to answer path sum queries efficiently. Use Heavy-Light Decomposition to partition the tree into chains.

---

## Input Format

- Line 1: N (number of nodes)
- Line 2: N integers (node values)
- Next N-1 lines: u, v (edges)
- Next line: Q (number of queries)
- Next Q lines: u, v (query sum on path from u to v)

---

## Output Format

For each query, print the sum of values on the path from u to v.

---

## Examples

### Example 1

**Input:**

```
5
1 2 3 4 5
1 2
1 3
2 4
2 5
3
1 4
3 5
4 5
```

**Output:**

```
7
11
11
```

### Example 2

**Input:**

```
3
10 20 30
1 2
2 3
2
1 3
1 2
```

**Output:**

```
60
30
```

---

## Constraints

- 1 ≤ N ≤ 200,000
- 1 ≤ Q ≤ 200,000
- 1 ≤ values[i] ≤ 10^9

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public void build(int n, int[] values, int[][] edges) {
        // Implement here
    }

    public long queryPath(int u, int v) {
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
        for (int i = 0; i < q; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            System.out.println(solution.queryPath(u, v));
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

    def query_path(self, u: int, v: int) -> int:
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
            u = int(next(iterator))
            v = int(next(iterator))
            print(solution.query_path(u, v))
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

    long long queryPath(int u, int v) {
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
        int u, v;
        cin >> u >> v;
        cout << solution.queryPath(u, v) << "\n";
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

  queryPath(u, v) {
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
    const u = parseInt(tokens[idx++]);
    const v = parseInt(tokens[idx++]);
    console.log(solution.queryPath(u, v));
  }
});
```

---

## Hints

<details>
<summary>Hint 1</summary>
Partition tree into heavy chains where heavy child has largest subtree.
</details>

<details>
<summary>Hint 2</summary>
Build segment tree over chain positions for range sum queries.
</details>
