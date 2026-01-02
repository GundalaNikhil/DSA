---
problem_id: TRE_AUDITORIUM_TOP_VIEW_HEIGHT__5601
display_id: TRE-010
slug: auditorium-top-view-height
title: "Auditorium Top View With Height Bonus"
difficulty: Medium
difficulty_score: 46
topics:
  - Trees
  - BFS
  - Views
tags:
  - trees
  - top-view
  - bfs
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# TRE-010: Auditorium Top View With Height Bonus

## Problem Statement

For each vertical column, choose the node with the smallest depth (top view). If multiple nodes share the same column and depth, choose the one with the largest value.

Return the chosen values from leftmost column to rightmost column.

![Problem Illustration](../images/TRE-010/problem-illustration.png)

## Input Format

- First line: integer `n`, number of nodes
- Next `n` lines: `value left right` for nodes `0..n-1`

`left` and `right` are child indices, or `-1` if absent. The root is node `0` when `n > 0`.

## Output Format

- Single line: top view values from left to right, separated by spaces
- If the tree is empty, print an empty line

## Constraints

- `0 <= n <= 100000`
- Node values fit in 32-bit signed integers

## Example

**Input:**

```
5
1 1 2
2 3 -1
3 -1 4
4 -1 -1
5 -1 -1
```

**Output:**

```
4 2 1 3 5
```

**Explanation:**

Columns from left to right are `-2, -1, 0, 1, 2`, giving values `4, 2, 1, 3, 5`.

![Example Visualization](../images/TRE-010/example-1.png)

## Notes

- Track column and depth for each node using BFS.
- Tie-breaking on the same depth uses the larger value.
- The root is always part of the top view if it exists.

## Related Topics

Top View, BFS, Binary Trees

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    static class NodeEntry {
        int val;
        int depth;
        NodeEntry(int v, int d) {
            this.val = v;
            this.depth = d;
        }
    }

    public List<Integer> topView(int n, int[] values, int[] left, int[] right) {
        return null;
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
        List<Integer> ans = solution.topView(n, values, left, right);
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
sys.setrecursionlimit(200000)
from collections import deque

def top_view(n: int, values: list[int], left: list[int], right: list[int]) -> list[int]:
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
    ans = top_view(n, values, left, right)
    sys.stdout.write(" ".join(str(x) for x in ans))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <map>
#include <queue>

using namespace std;

struct NodeInfo {
    int val;
    int depth;
};

class Solution {
public:
    vector<int> topView(int n, const vector<int>& values,
                        const vector<int>& left, const vector<int>& right) {
        if (n == 0) return {};

        map<int, NodeInfo> viewMap;
        queue<pair<int, pair<int, int>>> q; // u, {col, depth}
        q.push({0, {0, 0}});

        while (!q.empty()) {
            auto curr = q.front();
            q.pop();
            int u = curr.first;
            int c = curr.second.first;
            int d = curr.second.second;

            if (viewMap.find(c) == viewMap.end()) {
                viewMap[c] = {values[u], d};
            } else {
                if (d < viewMap[c].depth) {
                    viewMap[c] = {values[u], d};
                } else if (d == viewMap[c].depth) {
                    if (values[u] > viewMap[c].val) {
                        viewMap[c].val = values[u];
                    }
                }
            }

            if (left[u] != -1) q.push({left[u], {c - 1, d + 1}});
            if (right[u] != -1) q.push({right[u], {c + 1, d + 1}});
        }

        vector<int> result;
        for (auto const& [col, info] : viewMap) {
            result.push_back(info.val);
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
    vector<int> ans = solution.topView(n, values, left, right);
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
  topView(n, values, left, right) {
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
  const ans = solution.topView(n, values, left, right);
  console.log(ans.join(" "));
});
```

