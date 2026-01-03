---
problem_id: TRE_LAB_BOTTOM_VIEW_SHADOW_LIMIT__3395
display_id: TRE-011
slug: lab-bottom-view-shadow-limit
title: "Lab Bottom View with Shadow Limit"
difficulty: Medium
difficulty_score: 50
topics:
  - Trees
  - BFS
  - Views
tags:
  - trees
  - bottom-view
  - bfs
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# TRE-011: Lab Bottom View with Shadow Limit

## Problem Statement

Return the bottom view of a binary tree, but ignore any node deeper than depth `D` (root at depth 0). Only nodes with depth `<= D` can be chosen for each vertical column.

![Problem Illustration](../images/TRE-011/problem-illustration.png)

## Input Format

- First line: integer `n`, number of nodes
- Next `n` lines: `value left right` for nodes `0..n-1`
- Last line: integer `D`, maximum depth to consider

`left` and `right` are child indices, or `-1` if absent. The root is node `0` when `n > 0`.

## Output Format

- Single line: bottom view values from left to right
- If the tree is empty, print an empty line

## Constraints

- `0 <= n <= 100000`
- `0 <= D <= 100000`
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
1
```

**Output:**

```
2 1 3
```

**Explanation:**

Depth limit `D=1` excludes nodes at depth 2. The bottom view within this limit is `[2, 1, 3]`.

![Example Visualization](../images/TRE-011/example-1.png)

## Notes

- Use BFS with column and depth tracking.
- For each column, keep the deepest node seen so far within depth `D`.
- If multiple nodes tie on depth, the later BFS order can be used.

## Related Topics

Bottom View, BFS, Binary Trees

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public List<Integer> bottomViewWithLimit(int n, int[] values, int[] left, int[] right, int D) {
        //Implement here
        return new ArrayList<>();
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
        int D = 0;
        if (sc.hasNextInt()) D = sc.nextInt();

        Solution solution = new Solution();
        List<Integer> ans = solution.bottomViewWithLimit(n, values, left, right, D);
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

def bottom_view_with_limit(n: int, values: list[int], left: list[int], right: list[int], D: int) -> list[int]:
    # //Implement here
    return 0
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
    D = int(data[idx]) if idx < len(data) else 0
    ans = bottom_view_with_limit(n, values, left, right, D)
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

class Solution {
public:
    vector<int> bottomViewWithLimit(int n, const vector<int>& values,
                                    const vector<int>& left, const vector<int>& right, int D) {
        //Implement here
        return {};
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
    int D;
    cin >> D;

    Solution solution;
    vector<int> ans = solution.bottomViewWithLimit(n, values, left, right, D);
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
  bottomViewWithLimit(n, values, left, right, D) {
    //Implement here
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
  const D = idx < data.length ? parseInt(data[idx], 10) : 0;

  const solution = new Solution();
  const ans = solution.bottomViewWithLimit(n, values, left, right, D);
  console.log(ans.join(" "));
});
```
