---
title: "Binary Lifting for K-th Ancestor with Color Filter"
problem_id: TDP_KTH_ANCESTOR_COLOR__3741
display_id: TDP-012
difficulty: Medium
tags: [tree-dp, binary-lifting, ancestor-queries, color-filter]
slug: kth-ancestor-color-filter
time_limit: 2000
memory_limit: 256
---

## Problem Description

Given tree where each node has a color, answer queries: find k-th ancestor of node v with color c.

## Input Format

- Line 1: N
- Line 2: N colors
- Next N-1 lines: edges u v
- Next line: Q queries
- Next Q lines: v c k

## Output Format

For each query, print k-th ancestor with color c, or -1 if doesn't exist.

## Examples

### Example 1

**Input:**

```
5
1 2 1 2 1
1 2
1 3
2 4
2 5
3
4 2 1
5 1 2
3 1 1
```

**Output:**

```
2
1
1
```

### Example 2

**Input:**

```
3
1 1 2
1 2
2 3
2
3 1 1
3 1 2
```

**Output:**

```
2
1
```

## Constraints

- 1 ≤ N ≤ 200,000
- 1 ≤ Q ≤ 200,000
- 1 ≤ color[i] ≤ 10

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public void build(int n, int[] colors, int[][] edges) {
        // Implement here
    }

    public int findKthColoredAncestor(int v, int c, int k) {
        // Implement here
        return -1;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();

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
        solution.build(n, colors, edges);

        int q = sc.nextInt();
        for (int i = 0; i < q; i++) {
            int v = sc.nextInt();
            int c = sc.nextInt();
            int k = sc.nextInt();
            System.out.println(solution.findKthColoredAncestor(v, c, k));
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
    def build(self, n: int, colors: List[int], edges: List[List[int]]) -> None:
        # Implement here
        pass

    def find_kth_colored_ancestor(self, v: int, c: int, k: int) -> int:
        # Implement here
        return -1

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))

        colors = []
        for _ in range(n):
            colors.append(int(next(iterator)))

        edges = []
        for _ in range(n - 1):
            u = int(next(iterator))
            v = int(next(iterator))
            edges.append([u, v])

        solution = Solution()
        solution.build(n, colors, edges)

        q = int(next(iterator))
        for _ in range(q):
            v = int(next(iterator))
            c = int(next(iterator))
            k = int(next(iterator))
            print(solution.find_kth_colored_ancestor(v, c, k))
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
    void build(int n, const vector<int>& colors, const vector<vector<int>>& edges) {
        // Implement here
    }

    int findKthColoredAncestor(int v, int c, int k) {
        // Implement here
        return -1;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    if (!(cin >> n)) return 0;

    vector<int> colors(n);
    for (int i = 0; i < n; i++) {
        cin >> colors[i];
    }

    vector<vector<int>> edges(n - 1, vector<int>(2));
    for (int i = 0; i < n - 1; i++) {
        cin >> edges[i][0] >> edges[i][1];
    }

    Solution solution;
    solution.build(n, colors, edges);

    int q;
    cin >> q;
    while (q--) {
        int v, c, k;
        cin >> v >> c >> k;
        cout << solution.findKthColoredAncestor(v, c, k) << "\n";
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  build(n, colors, edges) {
    // Implement here
  }

  findKthColoredAncestor(v, c, k) {
    // Implement here
    return -1;
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
  solution.build(n, colors, edges);

  const q = parseInt(tokens[idx++]);
  for (let i = 0; i < q; i++) {
    const v = parseInt(tokens[idx++]);
    const c = parseInt(tokens[idx++]);
    const k = parseInt(tokens[idx++]);
    console.log(solution.findKthColoredAncestor(v, c, k));
  }
});
```

## Hints

<details>
<summary>Hint 1</summary>
Use binary lifting to jump ancestors quickly.
</details>

<details>
<summary>Hint 2</summary>
Track color count along ancestor path.
</details>
