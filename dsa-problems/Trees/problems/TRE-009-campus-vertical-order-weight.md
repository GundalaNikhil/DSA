---
problem_id: TRE_CAMPUS_VERTICAL_ORDER_WEIGHT__4502
display_id: TRE-009
slug: campus-vertical-order-weight
title: "Campus Vertical Order With Weight Priority"
difficulty: Medium
difficulty_score: 58
topics:
  - Trees
  - BFS
  - Sorting
tags:
  - trees
  - vertical-order
  - sorting
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# TRE-009: Campus Vertical Order With Weight Priority

## Problem Statement

Each node has a value and a weight. Return the vertical order traversal of the tree with custom ordering rules inside each column:

1. Depth ascending
2. Weight descending
3. Value ascending

Only include columns whose total weight is at least `W`.

![Problem Illustration](../images/TRE-009/problem-illustration.png)

## Input Format

- First line: integer `n`, number of nodes
- Next `n` lines: `value weight left right` for nodes `0..n-1`
- Last line: integer `W`, the minimum column weight

`left` and `right` are child indices, or `-1` if absent. The root is node `0` when `n > 0`.

## Output Format

- Print columns from left to right
- Each column is one line with its values in the required order
- If no column meets the threshold, print an empty line

## Constraints

- `0 <= n <= 100000`
- `1 <= weight <= 1000000`
- `0 <= W <= 10^12`

## Example

**Input:**

```
5
3 5 1 2
9 2 -1 -1
8 3 3 4
4 1 -1 -1
7 4 -1 -1
3
```

**Output:**

```
3 4
8
7
```

**Explanation:**

Column weights are: col -1 = 2, col 0 = 6, col 1 = 3, col 2 = 4. Columns with weight >= 3 are col 0, 1, and 2.

![Example Visualization](../images/TRE-009/example-1.png)

## Notes

- Columns are indexed by horizontal distance from the root.
- Stable ordering is not required; use the specified sort keys.
- Use 64-bit integers for column weight sums.

## Related Topics

Vertical Traversal, BFS, Sorting

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public List<List<Integer>> verticalOrderWithWeights(int n, int[] values, int[] weights, int[] left, int[] right, int W) {
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
        int[] weights = new int[n];
        int[] left = new int[n];
        int[] right = new int[n];

        for (int i = 0; i < n; i++) {
            values[i] = sc.nextInt();
            weights[i] = sc.nextInt();
            left[i] = sc.nextInt();
            right[i] = sc.nextInt();
        }

        int W = sc.hasNextInt() ? sc.nextInt() : 0;

        Solution solution = new Solution();
        List<List<Integer>> result = solution.verticalOrderWithWeights(n, values, weights, left, right, W);
        for (List<Integer> col : result) {
            for (int i = 0; i < col.size(); i++) {
                System.out.print(col.get(i) + (i == col.size() - 1 ? "" : " "));
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
    def vertical_order_with_weights(self, n: int, values: List[int], weights: List[int],
                                    left: List[int], right: List[int], W: int) -> List[List[int]]:
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
        weights = [0] * n
        left = [-1] * n
        right = [-1] * n
        for i in range(n):
            values[i] = int(next(iterator))
            weights[i] = int(next(iterator))
            left[i] = int(next(iterator))
            right[i] = int(next(iterator))

        W = 0
        try:
            W = int(next(iterator))
        except StopIteration:
            pass

        solution = Solution()
        cols = solution.vertical_order_with_weights(n, values, weights, left, right, W)
        for col in cols:
            print(*(col))
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
    vector<vector<int>> verticalOrderWithWeights(int n, const vector<int>& values, const vector<int>& weights,
                                                 const vector<int>& left, const vector<int>& right, int W) {
        // Implement here
        return {};
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;
    vector<int> values(n), weights(n), left(n), right(n);
    for (int i = 0; i < n; i++) {
        cin >> values[i] >> weights[i] >> left[i] >> right[i];
    }
    int W;
    cin >> W;

    Solution solution;
    vector<vector<int>> result = solution.verticalOrderWithWeights(n, values, weights, left, right, W);
    for (const auto& col : result) {
        for (int i = 0; i < col.size(); i++) {
            cout << col[i] << (i == col.size() - 1 ? "" : " ");
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
  verticalOrderWithWeights(n, values, weights, left, right, W) {
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
    weights = [],
    left = [],
    right = [];
  for (let i = 0; i < n; i++) {
    values.push(parseInt(tokens[idx++]));
    weights.push(parseInt(tokens[idx++]));
    left.push(parseInt(tokens[idx++]));
    right.push(parseInt(tokens[idx++]));
  }
  let W = 0;
  if (idx < tokens.length) W = parseInt(tokens[idx++]);

  const solution = new Solution();
  const cols = solution.verticalOrderWithWeights(
    n,
    values,
    weights,
    left,
    right,
    W
  );
  cols.forEach((col) => console.log(col.join(" ")));
});
```
