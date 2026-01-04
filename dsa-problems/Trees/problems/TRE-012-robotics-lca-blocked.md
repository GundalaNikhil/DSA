---
problem_id: TRE_ROBOTICS_LCA_BLOCKED__7104
display_id: TRE-012
slug: robotics-lca-blocked
title: "Robotics LCA with Blocked Nodes"
difficulty: Medium
difficulty_score: 54
topics:
  - Trees
  - LCA
  - DFS
tags:
  - trees
  - lca
  - dfs
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# TRE-012: Robotics LCA with Blocked Nodes

## Problem Statement

Some nodes in the tree are blocked and cannot be used as part of any path. Given two target nodes that are not blocked, find their lowest common ancestor (LCA) that is also not blocked.

If all common ancestors are blocked, output `-1`.

![Problem Illustration](../images/TRE-012/problem-illustration.png)

## Input Format

- First line: integer `n`, number of nodes
- Next `n` lines: `value blocked left right` for nodes `0..n-1`
- Last line: two integers `u` and `v`, the node indices of the targets

`left` and `right` are child indices, or `-1` if absent. The root is node `0` when `n > 0`.

## Output Format

- Single integer: value of the lowest unblocked common ancestor, or `-1` if none

## Constraints

- `1 <= n <= 100000`
- `blocked` is `0` or `1`
- Node values are distinct and fit in 32-bit signed integers
- Target nodes are unblocked

## Example

**Input:**

```
5
6 1 1 2
2 0 3 4
8 0 -1 -1
1 0 -1 -1
4 0 -1 -1
3 4
```

**Output:**

```
2
```

**Explanation:**

The LCA of nodes 3 and 4 is node 1 (value 2). The root is blocked, but the LCA node itself is unblocked.

![Example Visualization](../images/TRE-012/example-1.png)

## Notes

- If the LCA is blocked, climb to the nearest unblocked ancestor.
- Use DFS to detect presence of targets in subtrees.
- Output `-1` if no unblocked common ancestor exists.

## Related Topics

LCA, DFS, Binary Trees

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int lcaBlocked(int n, int[] values, int[] blocked, int[] left, int[] right, int u, int v) {
        // Implement here
        return -1;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] values = new int[n];
        int[] blocked = new int[n];
        int[] left = new int[n];
        int[] right = new int[n];
        for (int i = 0; i < n; i++) {
            values[i] = sc.nextInt();
            blocked[i] = sc.nextInt();
            left[i] = sc.nextInt();
            right[i] = sc.nextInt();
        }
        int u = sc.hasNextInt() ? sc.nextInt() : 0;
        int v = sc.hasNextInt() ? sc.nextInt() : 0;

        Solution solution = new Solution();
        System.out.println(solution.lcaBlocked(n, values, blocked, left, right, u, v));
        sc.close();
    }
}
```

### Python

```python
import sys
from typing import List

sys.setrecursionlimit(200000)

class Solution:
    def lca_blocked(self, n: int, values: List[int], blocked: List[int],
                    left: List[int], right: List[int], u: int, v: int) -> int:
        # Implement here
        return -1

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        values = [0] * n
        blocked = [0] * n
        left = [-1] * n
        right = [-1] * n
        for i in range(n):
            values[i] = int(next(iterator))
            blocked[i] = int(next(iterator))
            left[i] = int(next(iterator))
            right[i] = int(next(iterator))

        u = int(next(iterator))
        v = int(next(iterator))

        solution = Solution()
        print(solution.lca_blocked(n, values, blocked, left, right, u, v))
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
    int lcaBlocked(int n, const vector<int>& values, const vector<int>& blocked,
                   const vector<int>& left, const vector<int>& right, int u, int v) {
        // Implement here
        return -1;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;
    vector<int> values(n), blocked(n), left(n), right(n);
    for (int i = 0; i < n; i++) {
        cin >> values[i] >> blocked[i] >> left[i] >> right[i];
    }
    int u, v;
    cin >> u >> v;

    Solution solution;
    cout << solution.lcaBlocked(n, values, blocked, left, right, u, v) << endl;

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  lcaBlocked(n, values, blocked, left, right, u, v) {
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
  const values = [],
    blocked = [],
    left = [],
    right = [];
  for (let i = 0; i < n; i++) {
    values.push(parseInt(tokens[idx++]));
    blocked.push(parseInt(tokens[idx++]));
    left.push(parseInt(tokens[idx++]));
    right.push(parseInt(tokens[idx++]));
  }
  let u = 0,
    v = 0;
  if (idx < tokens.length) u = parseInt(tokens[idx++]);
  if (idx < tokens.length) v = parseInt(tokens[idx++]);

  const solution = new Solution();
  console.log(solution.lcaBlocked(n, values, blocked, left, right, u, v));
});
```
