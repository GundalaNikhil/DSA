---
problem_id: TRE_LAB_TREE_RIGHT_VIEW_SKIPS__3748
display_id: TRE-017
slug: lab-tree-right-view-skips
title: "Lab Tree Right View with Skips"
difficulty: Medium
difficulty_score: 46
topics:
  - Trees
  - BFS
  - Views
tags:
  - trees
  - right-view
  - bfs
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# TRE-017: Lab Tree Right View with Skips

## Problem Statement

Return the right view of a binary tree, but skip any node whose value is negative. If a level contains only skipped nodes, omit that level entirely.

![Problem Illustration](../images/TRE-017/problem-illustration.png)

## Input Format

- First line: integer `n`, number of nodes
- Next `n` lines: `value left right` for nodes `0..n-1`

`left` and `right` are child indices, or `-1` if absent. The root is node `0` when `n > 0`.

## Output Format

- Single line: right view values separated by spaces
- If no visible nodes exist, print an empty line

## Constraints

- `0 <= n <= 100000`
- Node values fit in 32-bit signed integers

## Example

**Input:**

```
4
10 1 2
-6 3 -1
14 -1 -1
7 -1 -1
```

**Output:**

```
10 14 7
```

**Explanation:**

At depth 1, the rightmost node is `14`. At depth 2, the only node is `7`. The negative node `-6` is skipped.

![Example Visualization](../images/TRE-017/example-1.png)

## Notes

- Level order traversal makes it easy to identify rightmost nodes.
- Skip nodes with negative values but still traverse their children.
- If the tree is empty, output an empty line.

## Related Topics

Right View, BFS, Binary Trees

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public List<Integer> rightViewWithSkips(int n, int[] values, int[] left, int[] right) {
        return null;
    }

    private int dfs(int u, int depth, int[] values, int[] left, int[] right, Map<Integer, Integer> view) {
        if (u == -1) return -1;

        // If valid and first time seeing this depth (since we go Right -> Left)
        if (values[u] >= 0 && !view.containsKey(depth)) {
            view.put(depth, values[u]);
        }

        int d1 = dfs(right[u], depth + 1, values, left, right, view);
        int d2 = dfs(left[u], depth + 1, values, left, right, view);
        
        return Math.max(depth, Math.max(d1, d2));
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] values = new int[n];
        int[] left = new int[n];
        int[] right = new int[n];
        for (int i = 0; i < n; i++) {
            values[i] = sc.nextInt();
            left[i] = sc.nextInt();
            right[i] = sc.nextInt();
        }

        Solution solution = new Solution();
        List<Integer> ans = solution.rightViewWithSkips(n, values, left, right);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < ans.size(); i++) {
            if (i > 0) sb.append(' ');
            sb.append(ans.get(i));
        }
        System.out.println(sb.toString());
        sc.close();
    }
}
```

### Python

```python
import sys

# Increase recursion depth
sys.setrecursionlimit(200000)

def right_view_with_skips(n: int, values: list[int], left: list[int], right: list[int]) -> list[int]:
    return []
def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]); idx += 1
    values = [0] * n
    left = [0] * n
    right = [0] * n
    for i in range(n):
        values[i] = int(data[idx]); idx += 1
        left[i] = int(data[idx]); idx += 1
        right[i] = int(data[idx]); idx += 1
    ans = right_view_with_skips(n, values, left, right)
    sys.stdout.write(" ".join(str(x) for x in ans))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

class Solution {
    int maxDepth = -1;
    void dfs(int u, int depth, const vector<int>& values, const vector<int>& left, const vector<int>& right, map<int, int>& view) {
    }

public:
    vector<int> rightViewWithSkips(int n, const vector<int>& values,
                                   const vector<int>& left, const vector<int>& right) {
        if (n == 0) return {};

        map<int, int> view;
        maxDepth = -1;
        dfs(0, 0, values, left, right, view);

        vector<int> result;
        for (int d = 0; d <= maxDepth; d++) {
            if (view.count(d)) {
                result.push_back(view[d]);
            }
        }
        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<int> values(n), left(n), right(n);
    for (int i = 0; i < n; i++) {
        cin >> values[i] >> left[i] >> right[i];
    }

    Solution solution;
    vector<int> ans = solution.rightViewWithSkips(n, values, left, right);
    for (int i = 0; i < (int)ans.size(); i++) {
        if (i) cout << ' ';
        cout << ans[i];
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  rightViewWithSkips(n, values, left, right) {
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
  const values = new Array(n);
  const left = new Array(n);
  const right = new Array(n);
  for (let i = 0; i < n; i++) {
    values[i] = parseInt(data[idx++], 10);
    left[i] = parseInt(data[idx++], 10);
    right[i] = parseInt(data[idx++], 10);
  }

  const solution = new Solution();
  const ans = solution.rightViewWithSkips(n, values, left, right);
  console.log(ans.join(" "));
});
```

