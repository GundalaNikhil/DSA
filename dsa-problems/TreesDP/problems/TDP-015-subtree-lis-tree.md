---
title: "DP for Subtree LIS on Tree"
problem_id: TDP_SUBTREE_LIS__7392
display_id: TDP-015
difficulty: Hard
tags: [tree-dp, lis, coordinate-compression, fenwick]
slug: subtree-lis-tree
time_limit: 2000
memory_limit: 256
---

## Problem Description

For each node, compute LIS length of values along root-to-node path.

## Input Format

- Line 1: N
- Line 2: N node values
- Next N-1 lines: u v (edges)

## Output Format

N integers: LIS length for each node's root path.

## Examples

### Example 1

**Input:**

```
3
2 1 3
1 2
1 3
```

**Output:**

```
1 1 2
```

### Example 2

**Input:**

```
5
1 5 2 4 3
1 2
1 3
2 4
2 5
```

**Output:**

```
1 2 2 3 3
```

## Constraints

- 1 ≤ N ≤ 200,000
- 1 ≤ values[i] ≤ 10^9

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int[] computeSubtreeLIS(int n, int[] values, int[][] edges) {
        // Implement here
        return new int[0];
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
        int[] result = solution.computeSubtreeLIS(n, values, edges);

        // Print array space separated or newline separated based on problem
        // Usually space separated for arrays
        for (int i = 0; i < result.length; i++) {
            System.out.print(result[i] + (i == result.length - 1 ? "" : " "));
        }
        System.out.println();
    }
}
```

### Python

```python
from typing import List
import sys

sys.setrecursionlimit(200000)

class Solution:
    def compute_subtree_lis(self, n: int, values: List[int], edges: List[List[int]]) -> List[int]:
        # Implement here
        return []

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
        result = solution.compute_subtree_lis(n, values, edges)
        print(" ".join(map(str, result)))
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
    vector<int> computeSubtreeLIS(int n, const vector<int>& values, const vector<vector<int>>& edges) {
        // Implement here
        return {};
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
    vector<int> result = solution.computeSubtreeLIS(n, values, edges);

    for (int i = 0; i < n; i++) {
        cout << result[i] << (i == n - 1 ? "" : " ");
    }
    cout << endl;

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  computeSubtreeLIS(n, values, edges) {
    // Implement here
    return [];
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
  const result = solution.computeSubtreeLIS(n, values, edges);
  console.log(result.join(" "));
});
```

## Hints

<details>
<summary>Hint 1</summary>
Use DFS with LIS data structure that supports add/remove.
</details>
