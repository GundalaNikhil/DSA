---
problem_id: AGR_TREE_DIAMETER_AFTER_REMOVAL__5964
display_id: AGR-014
slug: tree-diameter-after-removal
title: "Tree Diameter With Edge Removal"
difficulty: Medium
difficulty_score: 56
topics:
  - Graphs
  - Trees
  - Diameter
tags:
  - advanced-graphs
  - tree-diameter
  - rerooting
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# AGR-014: Tree Diameter With Edge Removal

## Problem Statement

Given a tree with `n` nodes, consider removing each edge one at a time. This splits the tree into two components. Compute the diameter (longest path length in edges) of each component and take the maximum of the two.

Return the maximum diameter value over all edge removals.

![Problem Illustration](../images/AGR-014/problem-illustration.png)

## Input Format

- First line: integer `n`
- Next `n-1` lines: `u v` describing an undirected edge

## Output Format

- Single integer: the maximum diameter after removing one edge

## Constraints

- `2 <= n <= 200000`
- `0 <= u, v < n`

## Example

**Input:**

```
4
0 1
1 2
1 3
```

**Output:**

```
2
```

**Explanation:**

Removing any edge leaves a component with diameter 2, so the maximum is 2.

![Example Visualization](../images/AGR-014/example-1.png)

## Notes

- The tree is unweighted; edge lengths are 1.
- Use rerooting DP to compute subtree diameters and heights.
- The answer fits in 32-bit integers.

## Related Topics

Tree Diameter, Rerooting DP, Trees

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public int solve(int n, int[][] edges) {
        // Implement here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        if (line == null) return;
        int n = Integer.parseInt(line.trim());

        int[][] edges = new int[n - 1][2];
        for (int i = 0; i < n - 1; i++) {
            line = br.readLine();
            if (line == null) break;
            String[] parts = line.trim().split("\\s+");
            edges[i][0] = Integer.parseInt(parts[0]);
            edges[i][1] = Integer.parseInt(parts[1]);
        }

        Solution sol = new Solution();
        System.out.println(sol.solve(n, edges));
    }
}
```

### Python

```python
import sys

# Increase recursion depth for tree traversal
sys.setrecursionlimit(300005)

class Solution:
    def solve(self, n, edges):
        # Implement here
        return 0

def run_program():
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

    except StopIteration:
        pass

    sol = Solution()
    print(sol.solve(n, edges))

if __name__ == "__main__":
    run_program()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int solve(int n, vector<vector<int>>& edges) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<int>> edges(n - 1, vector<int>(2));
    for (int i = 0; i < n - 1; i++) {
        cin >> edges[i][0] >> edges[i][1];
    }

    Solution sol;
    cout << sol.solve(n, edges) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  solve(n, edges) {
    // Implement here
    return 0;
  }
}

function runProgram() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 1) return;

  let idx = 0;
  function readInt() {
    return parseInt(input[idx++]);
  }

  const n = readInt();
  const edges = [];
  for (let i = 0; i < n - 1; i++) {
    const u = readInt();
    const v = readInt();
    edges.push([u, v]);
  }

  const sol = new Solution();
  console.log(sol.solve(n, edges));
}

runProgram();
```
