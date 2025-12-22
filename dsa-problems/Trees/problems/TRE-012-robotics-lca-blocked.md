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
        // Your implementation here
        return -1;
    }
}

public class Main {
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
        int u = sc.nextInt();
        int v = sc.nextInt();

        Solution solution = new Solution();
        System.out.println(solution.lcaBlocked(n, values, blocked, left, right, u, v));
        sc.close();
    }
}
```

### Python

```python
def lca_blocked(n: int, values: list[int], blocked: list[int], left: list[int], right: list[int], u: int, v: int) -> int:
    # Your implementation here
    return -1

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]); idx += 1
    values = [0] * n
    blocked = [0] * n
    left = [0] * n
    right = [0] * n
    for i in range(n):
        values[i] = int(data[idx]); idx += 1
        blocked[i] = int(data[idx]); idx += 1
        left[i] = int(data[idx]); idx += 1
        right[i] = int(data[idx]); idx += 1
    u = int(data[idx]); idx += 1
    v = int(data[idx]); idx += 1
    print(lca_blocked(n, values, blocked, left, right, u, v))

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
    int lcaBlocked(int n, const vector<int>& values, const vector<int>& blocked,
                   const vector<int>& left, const vector<int>& right, int u, int v) {
        // Your implementation here
        return -1;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<int> values(n), blocked(n), left(n), right(n);
    for (int i = 0; i < n; i++) {
        cin >> values[i] >> blocked[i] >> left[i] >> right[i];
    }
    int u, v;
    cin >> u >> v;

    Solution solution;
    cout << solution.lcaBlocked(n, values, blocked, left, right, u, v) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  lcaBlocked(n, values, blocked, left, right, u, v) {
    // Your implementation here
    return -1;
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
  const values = new Array(n);
  const blocked = new Array(n);
  const left = new Array(n);
  const right = new Array(n);
  for (let i = 0; i < n; i++) {
    values[i] = parseInt(data[idx++], 10);
    blocked[i] = parseInt(data[idx++], 10);
    left[i] = parseInt(data[idx++], 10);
    right[i] = parseInt(data[idx++], 10);
  }
  const u = parseInt(data[idx++], 10);
  const v = parseInt(data[idx++], 10);

  const solution = new Solution();
  console.log(solution.lcaBlocked(n, values, blocked, left, right, u, v).toString());
});
```
