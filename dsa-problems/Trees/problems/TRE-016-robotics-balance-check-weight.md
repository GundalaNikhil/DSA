---
problem_id: TRE_ROBOTICS_BALANCE_CHECK_WEIGHT__6280
display_id: TRE-016
slug: robotics-balance-check-weight
title: "Robotics Balance Check with Weight Limit"
difficulty: Medium
difficulty_score: 54
topics:
  - Trees
  - DFS
  - Balance
tags:
  - trees
  - balance
  - dfs
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# TRE-016: Robotics Balance Check with Weight Limit

## Problem Statement

Each node has a weight. A tree is balanced if, at every node:

1. The height difference between left and right subtrees is at most 1.
2. The absolute difference between total weights of left and right subtrees is at most `W`.

Return `true` if the tree is balanced, otherwise `false`.

![Problem Illustration](../images/TRE-016/problem-illustration.png)

## Input Format

- First line: integer `n`, number of nodes
- Next `n` lines: `weight left right` for nodes `0..n-1`
- Last line: integer `W`

`left` and `right` are child indices, or `-1` if absent. The root is node `0` when `n > 0`.

## Output Format

- Print `true` if the tree is balanced, otherwise `false`

## Constraints

- `0 <= n <= 100000`
- `1 <= weight <= 10^9`
- `0 <= W <= 10^12`

## Example

**Input:**

```
3
1 1 2
2 -1 -1
1 -1 -1
1
```

**Output:**

```
true
```

**Explanation:**

The tree has equal heights and the subtree weight difference at the root is 1.

![Example Visualization](../images/TRE-016/example-1.png)

## Notes

- Use postorder DFS to compute height and subtree weight.
- Stop early when an imbalance is detected.
- An empty tree is considered balanced.

## Related Topics

Balanced Trees, DFS, Tree Properties

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public boolean isBalancedWeighted(int n, long[] weight, int[] left, int[] right, long W) {
        // Your implementation here
        return false;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        long[] weight = new long[n];
        int[] left = new int[n];
        int[] right = new int[n];
        for (int i = 0; i < n; i++) {
            weight[i] = sc.nextLong();
            left[i] = sc.nextInt();
            right[i] = sc.nextInt();
        }
        long W = sc.nextLong();

        Solution solution = new Solution();
        System.out.println(solution.isBalancedWeighted(n, weight, left, right, W) ? "true" : "false");
        sc.close();
    }
}
```

### Python

```python
def is_balanced_weighted(n: int, weight: list[int], left: list[int], right: list[int], W: int) -> bool:
    # Your implementation here
    return False

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]); idx += 1
    weight = [0] * n
    left = [0] * n
    right = [0] * n
    for i in range(n):
        weight[i] = int(data[idx]); idx += 1
        left[i] = int(data[idx]); idx += 1
        right[i] = int(data[idx]); idx += 1
    W = int(data[idx]) if idx < len(data) else 0
    print("true" if is_balanced_weighted(n, weight, left, right, W) else "false")

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
    bool isBalancedWeighted(int n, const vector<long long>& weight,
                            const vector<int>& left, const vector<int>& right, long long W) {
        // Your implementation here
        return false;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<long long> weight(n);
    vector<int> left(n), right(n);
    for (int i = 0; i < n; i++) {
        cin >> weight[i] >> left[i] >> right[i];
    }
    long long W;
    cin >> W;

    Solution solution;
    cout << (solution.isBalancedWeighted(n, weight, left, right, W) ? "true" : "false") << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  isBalancedWeighted(n, weight, left, right, W) {
    // Your implementation here
    return false;
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
  const weight = new Array(n);
  const left = new Array(n);
  const right = new Array(n);
  for (let i = 0; i < n; i++) {
    weight[i] = parseInt(data[idx++], 10);
    left[i] = parseInt(data[idx++], 10);
    right[i] = parseInt(data[idx++], 10);
  }
  const W = idx < data.length ? parseInt(data[idx], 10) : 0;

  const solution = new Solution();
  console.log(solution.isBalancedWeighted(n, weight, left, right, W) ? "true" : "false");
});
```
