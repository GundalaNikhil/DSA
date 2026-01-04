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
    public List<Integer> topView(int n, int[] values, int[] left, int[] right) {
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

        Solution solution = new Solution();
        List<Integer> ans = solution.topView(n, values, left, right);
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
    def top_view(self, n: int, values: List[int], left: List[int], right: List[int]) -> List[int]:
        # Implement here
        return []
```

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

        solution = Solution()
        ans = solution.top_view(n, values, left, right)
        print(*(ans))
    except StopIteration:
        pass

if **name** == "**main**":
main()

````

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> topView(int n, const vector<int>& values, const vector<int>& left, const vector<int>& right) {
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

    Solution solution;
    vector<int> ans = solution.topView(n, values, left, right);
    for (int i = 0; i < ans.size(); i++) {
        cout << ans[i] << (i == ans.size() - 1 ? "" : " ");
    }
    cout << endl;

    return 0;
}
````

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  topView(n, values, left, right) {
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

  const solution = new Solution();
  console.log(solution.topView(n, values, left, right).join(" "));
});
```
