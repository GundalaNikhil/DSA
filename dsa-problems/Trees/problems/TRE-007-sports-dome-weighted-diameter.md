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
        // Your implementation here
        return 0L;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] left = new int[n];
        int[] right = new int[n];
        long[] lw = new long[n];
        long[] rw = new long[n];
        for (int i = 0; i < n; i++) {
            int val = sc.nextInt();
            left[i] = sc.nextInt();
            right[i] = sc.nextInt();
            lw[i] = sc.nextLong();
            rw[i] = sc.nextLong();
        }

        Solution solution = new Solution();
        System.out.println(solution.weightedDiameter(n, left, right, lw, rw));
        sc.close();
    }
}
```

### Python

```python
def weighted_diameter(n: int, left: list[int], right: list[int], lw: list[int], rw: list[int]) -> int:
    # Your implementation here
    return 0

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]); idx += 1
    left = [0] * n
    right = [0] * n
    lw = [0] * n
    rw = [0] * n
    for i in range(n):
        _ = data[idx]; idx += 1
        left[i] = int(data[idx]); idx += 1
        right[i] = int(data[idx]); idx += 1
        lw[i] = int(data[idx]); idx += 1
        rw[i] = int(data[idx]); idx += 1
    print(weighted_diameter(n, left, right, lw, rw))

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
    long long weightedDiameter(int n, const vector<int>& left, const vector<int>& right,
                               const vector<long long>& lw, const vector<long long>& rw) {
        // Your implementation here
        return 0LL;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<int> left(n), right(n);
    vector<long long> lw(n), rw(n);
    for (int i = 0; i < n; i++) {
        int val;
        cin >> val >> left[i] >> right[i] >> lw[i] >> rw[i];
    }

    Solution solution;
    cout << solution.weightedDiameter(n, left, right, lw, rw) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  weightedDiameter(n, left, right, lw, rw) {
    // Your implementation here
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
  const left = new Array(n);
  const right = new Array(n);
  const lw = new Array(n);
  const rw = new Array(n);
  for (let i = 0; i < n; i++) {
    idx++; // value
    left[i] = parseInt(data[idx++], 10);
    right[i] = parseInt(data[idx++], 10);
    lw[i] = parseInt(data[idx++], 10);
    rw[i] = parseInt(data[idx++], 10);
  }

  const solution = new Solution();
  console.log(solution.weightedDiameter(n, left, right, lw, rw).toString());
});
```
