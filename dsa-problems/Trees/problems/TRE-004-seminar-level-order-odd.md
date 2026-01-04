---
problem_id: TRE_SEMINAR_LEVEL_ORDER_ODD__5168
display_id: TRE-004
slug: seminar-level-order-odd
title: "Seminar Level Order Odd-Depth Only"
difficulty: Easy
difficulty_score: 26
topics:
  - Trees
  - BFS
  - Level Order
tags:
  - trees
  - bfs
  - traversal
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# TRE-004: Seminar Level Order Odd-Depth Only

## Problem Statement

Return the level-order traversal of a binary tree, but include only nodes at odd depths. The root is at depth 0.

For each odd depth that exists, output the node values in left-to-right order.

![Problem Illustration](../images/TRE-004/problem-illustration.png)

## Input Format

- First line: integer `n`, number of nodes
- Next `n` lines: `value left right` for nodes `0..n-1`

`left` and `right` are child indices, or `-1` if absent. The root is node `0` when `n > 0`.

## Output Format

- For each odd depth that has nodes, print one line with the values in left-to-right order
- If there are no odd-depth nodes, print an empty line

## Constraints

- `0 <= n <= 100000`
- Node values fit in 32-bit signed integers

## Example

**Input:**

```
4
10 1 2
5 3 -1
12 -1 -1
7 -1 -1
```

**Output:**

```
5 12
```

**Explanation:**

Depth 1 nodes are `5` and `12`. Depth 3 does not exist, so only one line is printed.

![Example Visualization](../images/TRE-004/example-1.png)

## Notes

- Traverse all levels, but only output odd depths.
- Preserve left-to-right order within each level.
- An empty tree produces a single empty line.

## Related Topics

Level Order Traversal, BFS, Binary Trees

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public List<List<Integer>> oddDepthLevels(int n, int[] values, int[] left, int[] right) {
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
        List<List<Integer>> result = solution.oddDepthLevels(n, values, left, right);

        for (int i = 0; i < result.size(); i++) {
            List<Integer> level = result.get(i);
            for (int j = 0; j < level.size(); j++) {
                System.out.print(level.get(j) + (j == level.size() - 1 ? "" : " "));
            }
            System.out.println();
        }
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
    def odd_depth_levels(self, n: int, values: List[int], left: List[int], right: List[int]) -> List[List[int]]:
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

        solution = Solution()
        levels = solution.odd_depth_levels(n, values, left, right)
        for level in levels:
            print(*(level))
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
    vector<vector<int>> oddDepthLevels(int n, const vector<int>& values, const vector<int>& left, const vector<int>& right) {
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
    vector<vector<int>> result = solution.oddDepthLevels(n, values, left, right);
    for (const auto& level : result) {
        for (int i = 0; i < level.size(); i++) {
            cout << level[i] << (i == level.size() - 1 ? "" : " ");
        }
        cout << "\n";
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  oddDepthLevels(n, values, left, right) {
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
  const values = Array(n).fill(0);
  const left = Array(n).fill(-1);
  const right = Array(n).fill(-1);
  for (let i = 0; i < n; i++) {
    values[i] = parseInt(tokens[idx++]);
    left[i] = parseInt(tokens[idx++]);
    right[i] = parseInt(tokens[idx++]);
  }

  const solution = new Solution();
  const levels = solution.oddDepthLevels(n, values, left, right);
  levels.forEach((level) => console.log(level.join(" ")));
});
```
