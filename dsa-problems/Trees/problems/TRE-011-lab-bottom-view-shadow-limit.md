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
        // Implement here
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
        int D = sc.hasNextInt() ? sc.nextInt() : 0;

        Solution solution = new Solution();
        List<Integer> ans = solution.bottomViewWithLimit(n, values, left, right, D);
        for (int i = 0; i < ans.size(); i++) {
            System.out.print(ans.get(i) + (i == ans.size() - 1 ? "" : " "));
        }
        System.out.println();
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
    def bottom_view_with_limit(self, n: int, values: List[int], left: List[int], right: List[int], D: int) -> List[int]:
        # Implement here
        return []

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        values = [0] * n
        left = [-1] * n
        right = [-1] * n
        for i in range(n):
            values[i] = int(next(iterator))
            left[i] = int(next(iterator))
            right[i] = int(next(iterator))

        D = 0
        try:
            D = int(next(iterator))
        except StopIteration:
            pass

        solution = Solution()
        ans = solution.bottom_view_with_limit(n, values, left, right, D)
        print(*(ans))
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
    vector<int> bottomViewWithLimit(int n, const vector<int>& values, const vector<int>& left, const vector<int>& right, int D) {
        // Implement here
        return {};
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

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
    for (int i = 0; i < ans.size(); i++) {
        cout << ans[i] << (i == ans.size() - 1 ? "" : " ");
    }
    cout << endl;

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  bottomViewWithLimit(n, values, left, right, D) {
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
  const values = [],
    left = [],
    right = [];
  for (let i = 0; i < n; i++) {
    values.push(parseInt(tokens[idx++]));
    left.push(parseInt(tokens[idx++]));
    right.push(parseInt(tokens[idx++]));
  }
  let D = 0;
  if (idx < tokens.length) D = parseInt(tokens[idx++]);

  const solution = new Solution();
  console.log(
    solution.bottomViewWithLimit(n, values, left, right, D).join(" ")
  );
});
```
