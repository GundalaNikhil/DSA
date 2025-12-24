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
    public List<List<Integer>> verticalOrderWithWeights(int n, int[] values, int[] weights,
                                                       int[] left, int[] right, long W) {
        // Your implementation here
        return new ArrayList<>();
    }
}

public class Main {
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
        long W = sc.nextLong();
        Solution solution = new Solution();
        List<List<Integer>> cols = solution.verticalOrderWithWeights(n, values, weights, left, right, W);
        if (cols.isEmpty()) {
            System.out.println();
        } else {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < cols.size(); i++) {
                List<Integer> col = cols.get(i);
                for (int j = 0; j < col.size(); j++) {
                    if (j > 0) sb.append(' ');
                    sb.append(col.get(j));
                }
                if (i + 1 < cols.size()) sb.append('\n');
            }
            System.out.print(sb.toString());
        }
        sc.close();
    }
}
```

### Python

```python
def vertical_order_with_weights(n: int, values: list[int], weights: list[int],
                                left: list[int], right: list[int], W: int) -> list[list[int]]:
    # Your implementation here
    return []

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]); idx += 1
    values = [0] * n
    weights = [0] * n
    left = [0] * n
    right = [0] * n
    for i in range(n):
        values[i] = int(data[idx]); idx += 1
        weights[i] = int(data[idx]); idx += 1
        left[i] = int(data[idx]); idx += 1
        right[i] = int(data[idx]); idx += 1
    W = int(data[idx]) if idx < len(data) else 0
    cols = vertical_order_with_weights(n, values, weights, left, right, W)
    if not cols:
        sys.stdout.write("\n")
    else:
        sys.stdout.write("\n".join(" ".join(str(x) for x in col) for col in cols))

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
    vector<vector<int>> verticalOrderWithWeights(int n, const vector<int>& values,
                                                 const vector<int>& weights, const vector<int>& left,
                                                 const vector<int>& right, long long W) {
        // Your implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<int> values(n), weights(n), left(n), right(n);
    for (int i = 0; i < n; i++) {
        cin >> values[i] >> weights[i] >> left[i] >> right[i];
    }
    long long W;
    cin >> W;
    Solution solution;
    vector<vector<int>> cols = solution.verticalOrderWithWeights(n, values, weights, left, right, W);
    if (cols.empty()) {
        cout << "\n";
    } else {
        for (int i = 0; i < (int)cols.size(); i++) {
            for (int j = 0; j < (int)cols[i].size(); j++) {
                if (j) cout << ' ';
                cout << cols[i][j];
            }
            if (i + 1 < (int)cols.size()) cout << "\n";
        }
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  verticalOrderWithWeights(n, values, weights, left, right, W) {
    // Your implementation here
    return [];
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
  const weights = new Array(n);
  const left = new Array(n);
  const right = new Array(n);
  for (let i = 0; i < n; i++) {
    values[i] = parseInt(data[idx++], 10);
    weights[i] = parseInt(data[idx++], 10);
    left[i] = parseInt(data[idx++], 10);
    right[i] = parseInt(data[idx++], 10);
  }
  const W = idx < data.length ? parseInt(data[idx], 10) : 0;
  const solution = new Solution();
  const cols = solution.verticalOrderWithWeights(n, values, weights, left, right, W);
  if (cols.length === 0) {
    console.log("");
  } else {
    console.log(cols.map((col) => col.join(" ")).join("\n"));
  }
});
```
