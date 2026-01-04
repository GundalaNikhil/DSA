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

class Solution {
    public long countValidPaths(int n, int k, int forbiddenColor, int[] colors, int[][] edges) {
        // Implement here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int k = sc.nextInt();
        int forbiddenColor = sc.nextInt();

        int[] colors = new int[n];
        for (int i = 0; i < n; i++) {
            colors[i] = sc.nextInt();
        }

        int[][] edges = new int[n - 1][2];
        for (int i = 0; i < n - 1; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
        }

        Solution solution = new Solution();
        System.out.println(solution.countValidPaths(n, k, forbiddenColor, colors, edges));
    }
}
```

### Python

```python
from typing import List
import sys

sys.setrecursionlimit(200000)

class Solution:
    def count_valid_paths(self, n: int, k: int, forbidden_color: int, colors: List[int], edges: List[List[int]]) -> int:
        # Implement here
        return 0

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        k = int(next(iterator))
        forbidden_color = int(next(iterator))

        colors = []
        for _ in range(n):
            colors.append(int(next(iterator)))

        edges = []
        for _ in range(n - 1):
            u = int(next(iterator))
            v = int(next(iterator))
            edges.append([u, v])

        solution = Solution()
        print(solution.count_valid_paths(n, k, forbidden_color, colors, edges))
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
    long long countValidPaths(int n, int k, int forbiddenColor, const vector<int>& colors, const vector<vector<int>>& edges) {
        // Implement here
        return 0;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n, k, forbiddenColor;
    if (!(cin >> n >> k >> forbiddenColor)) return 0;

    vector<int> colors(n);
    for (int i = 0; i < n; i++) {
        cin >> colors[i];
    }

    vector<vector<int>> edges(n - 1, vector<int>(2));
    for (int i = 0; i < n - 1; i++) {
        cin >> edges[i][0] >> edges[i][1];
    }

    Solution solution;
    cout << solution.countValidPaths(n, k, forbiddenColor, colors, edges) << endl;

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  countValidPaths(n, k, forbiddenColor, colors, edges) {
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
  const k = parseInt(tokens[idx++]);
  const forbiddenColor = parseInt(tokens[idx++]);

  const colors = [];
  for (let i = 0; i < n; i++) {
    colors.push(parseInt(tokens[idx++]));
  }

  const edges = [];
  for (let i = 0; i < n - 1; i++) {
    const u = parseInt(tokens[idx++]);
    const v = parseInt(tokens[idx++]);
    edges.push([u, v]);
  }

  const solution = new Solution();
  console.log(solution.countValidPaths(n, k, forbiddenColor, colors, edges));
});
```

---

## Hints

<details>
<summary>Hint 1</summary>
Use DP with state tracking: dp[node][distance][hasForbidden]
</details>

<details>
<summary>Hint 2</summary>
During DFS, merge child contributions to count valid pairs at distance K
</details>
