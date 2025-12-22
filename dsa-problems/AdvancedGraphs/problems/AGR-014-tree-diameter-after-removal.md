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

class Solution {
    public int maxDiameterAfterRemoval(int n, int[][] edges) {
        // Your implementation here
        return 0;
    }
}

public class Main {
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
        System.out.println(solution.maxDiameterAfterRemoval(n, edges));
        sc.close();
    }
}
```

### Python

```python
def max_diameter_after_removal(n: int, edges: list[tuple[int, int]]) -> int:
    # Your implementation here
    return 0

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    edges = []
    for _ in range(n - 1):
        u = int(next(it)); v = int(next(it))
        edges.append((u, v))
    print(max_diameter_after_removal(n, edges))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int maxDiameterAfterRemoval(int n, const vector<pair<int, int>>& edges) {
        // Your implementation here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<pair<int, int>> edges(n - 1);
    for (int i = 0; i < n - 1; i++) {
        cin >> edges[i].first >> edges[i].second;
    }

    Solution solution;
    cout << solution.maxDiameterAfterRemoval(n, edges) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  maxDiameterAfterRemoval(n, edges) {
    // Your implementation here
    return 0;
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
  const edges = [];
  for (let i = 0; i < n - 1; i++) {
    const u = parseInt(data[idx++], 10);
    const v = parseInt(data[idx++], 10);
    edges.push([u, v]);
  }

  const solution = new Solution();
  console.log(solution.maxDiameterAfterRemoval(n, edges).toString());
});
```
