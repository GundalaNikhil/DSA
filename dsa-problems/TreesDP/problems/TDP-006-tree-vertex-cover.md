---
title: Tree DP for Vertex Cover
problem_id: TDP_TREE_VERTEX_COVER__7514
display_id: TDP-006
difficulty: Medium
time_limit: 2000
memory_limit: 256
tags:
  - Tree DP
  - Graph Theory
  - Optimization
categories:
  - Algorithms
  - Data Structures
slug: tree-vertex-cover
---

# Tree DP for Vertex Cover

## Problem Description

Given a tree with `n` nodes, find the size of the **minimum vertex cover**.

A vertex cover is a set of vertices such that every edge in the tree has at least one of its endpoints in the set.

## Input Format

- First line: integer `n` (number of nodes)
- Next `n-1` lines: each contains two integers `u v` representing an edge

## Output Format

- Single integer: the size of the minimum vertex cover

## Constraints

- `1 <= n <= 2 x 10^5`
- `1 <= u, v <= n`
- The graph forms a valid tree

## Example 1

**Input:**

```
3
1 2
1 3
```

**Output:**

```
1
```

**Explanation:**
Tree structure:

```
  1
 / \
2   3
```

Vertex cover = {1} covers both edges (1-2) and (1-3).
Size = 1 (minimum possible).

## Example 2

**Input:**

```
4
1 2
2 3
3 4
```

**Output:**

```
2
```

**Explanation:**
Tree structure: 1 -- 2 -- 3 -- 4

Possible minimum vertex covers:

- {2, 3} covers edges (1-2), (2-3), and (3-4)
- Size = 2

Alternatively: {1, 3} or {2, 4} also work.

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int minVertexCover(int n, int[][] edges) {
        // Implement here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();

        int[][] edges = new int[n - 1][2];
        for (int i = 0; i < n - 1; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
        }

        Solution solution = new Solution();
        System.out.println(solution.minVertexCover(n, edges));
    }
}
```

### Python

```python
from typing import List
import sys

sys.setrecursionlimit(200000)

class Solution:
    def min_vertex_cover(self, n: int, edges: List[List[int]]) -> int:
        # Implement here
        return 0

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))

        edges = []
        for _ in range(n - 1):
            u = int(next(iterator))
            v = int(next(iterator))
            edges.append([u, v])

        solution = Solution()
        print(solution.min_vertex_cover(n, edges))
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
    int minVertexCover(int n, const vector<vector<int>>& edges) {
        // Implement here
        return 0;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    if (!(cin >> n)) return 0;

    vector<vector<int>> edges(n - 1, vector<int>(2));
    for (int i = 0; i < n - 1; i++) {
        cin >> edges[i][0] >> edges[i][1];
    }

    Solution solution;
    cout << solution.minVertexCover(n, edges) << endl;

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  minVertexCover(n, edges) {
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

  const edges = [];
  for (let i = 0; i < n - 1; i++) {
    const u = parseInt(tokens[idx++]);
    const v = parseInt(tokens[idx++]);
    edges.push([u, v]);
  }

  const solution = new Solution();
  console.log(solution.minVertexCover(n, edges));
});
```

## Notes

- dp[u][0] = minimum cover size for subtree of u when u is NOT included
- dp[u][1] = minimum cover size for subtree of u when u IS included
- When u is not included, all children must be included
- When u is included, children can be included or not (take minimum)
