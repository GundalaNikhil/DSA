---
problem_id: TRE_SPORTS_DOME_WEIGHTED_DIAMETER__9532
display_id: TRE-007
slug: sports-dome-weighted-diameter
title: "Sports Dome Weighted Diameter"
difficulty: Medium
difficulty_score: 48
topics:
  - Trees
  - DFS
  - Tree Diameter
tags:
  - trees
  - diameter
  - dfs
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# TRE-007: Sports Dome Weighted Diameter

## Problem Statement

Edges of the binary tree have non-negative weights. Find the maximum total edge weight along any path between two nodes.

This value is the weighted diameter of the tree.

![Problem Illustration](../images/TRE-007/problem-illustration.png)

## Input Format

- First line: integer `n`, number of nodes
- Next `n` lines: `value left right leftWeight rightWeight` for nodes `0..n-1`

`left` and `right` are child indices, or `-1` if absent. The corresponding weight is ignored when the child is `-1`. The root is node `0` when `n > 0`.

## Output Format

- Single integer: weighted diameter of the tree

## Constraints

- `0 <= n <= 100000`
- Edge weights are integers in `[0, 10^9]`
- Node values fit in 32-bit signed integers

## Example

**Input:**

```
4
1 1 2 3 1
2 3 -1 2 0
3 -1 -1 0 0
4 -1 -1 0 0
```

**Output:**

```
6
```

**Explanation:**

The path `4 -> 2 -> 1 -> 3` has total weight `2 + 3 + 1 = 6`, which is the maximum.

![Example Visualization](../images/TRE-007/example-1.png)

## Notes

- The diameter can pass through or avoid the root.
- Use DFS to compute the best downward path at each node.
- The answer fits in 64-bit signed integers.

## Related Topics

Tree Diameter, DFS, Weighted Trees

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long weightedDiameter(int n, int[] left, int[] right, long[] lw, long[] rw) {
        // Implement here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] left = new int[n];
        int[] right = new int[n];
        long[] lw = new long[n];
        long[] rw = new long[n];

        for (int i = 0; i < n; i++) {
            int val = sc.nextInt(); // unused
            left[i] = sc.nextInt();
            right[i] = sc.nextInt();
            lw[i] = sc.hasNextLong() ? sc.nextLong() : 1;
            rw[i] = sc.hasNextLong() ? sc.nextLong() : 1;
        }

        Solution solution = new Solution();
        System.out.println(solution.weightedDiameter(n, left, right, lw, rw));
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
    def weighted_diameter(self, n: int, left: List[int], right: List[int], lw: List[int], rw: List[int]) -> int:
        # Implement here
        return 0

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        left = [-1] * n
        right = [-1] * n
        lw = [0] * n
        rw = [0] * n

        for i in range(n):
            _ = next(iterator) # value unused
            left[i] = int(next(iterator))
            right[i] = int(next(iterator))
            lw[i] = int(next(iterator))
            rw[i] = int(next(iterator))

        solution = Solution()
        print(solution.weighted_diameter(n, left, right, lw, rw))
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
    long long weightedDiameter(int n, const vector<int>& left, const vector<int>& right, const vector<long long>& lw, const vector<long long>& rw) {
        // Implement here
        return 0;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;
    vector<int> left(n), right(n);
    vector<long long> lw(n), rw(n);
    for (int i = 0; i < n; i++) {
        int val;
        cin >> val >> left[i] >> right[i] >> lw[i] >> rw[i];
    }

    Solution solution;
    cout << solution.weightedDiameter(n, left, right, lw, rw) << endl;

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  weightedDiameter(n, left, right, lw, rw) {
    // Implement here
    return 0;
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
  const left = [],
    right = [],
    lw = [],
    rw = [];
  for (let i = 0; i < n; i++) {
    const val = tokens[idx++]; // unused
    left.push(parseInt(tokens[idx++]));
    right.push(parseInt(tokens[idx++]));
    lw.push(BigInt(tokens[idx++]));
    rw.push(BigInt(tokens[idx++]));
  }

  const solution = new Solution();
  console.log(solution.weightedDiameter(n, left, right, lw, rw).toString());
});
```
