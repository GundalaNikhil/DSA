---
problem_id: DP_PAINT_FENCE_SWITCH_COST__4281
display_id: DP-013
slug: paint-fence-switch-cost
title: "Paint Fence With Switch Cost"
difficulty: Medium
difficulty_score: 55
topics:
  - Dynamic Programming
  - Optimization
  - Combinatorics
tags:
  - dp
  - optimization
  - painting
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP-013: Paint Fence With Switch Cost

## Problem Statement

You must paint a straight fence of `n` posts using exactly one color per post. There are `k` available colors.

Rules:

- Painting any post costs **1** unit regardless of color.
- You may not have more than **two consecutive posts** with the same color.
- If post `i` (1-indexed) uses a different color than post `i-1`, you pay an additional **switch cost** `s[i]`. For `i = 1`, there is no previous post, so only the base cost applies.
- If it is impossible to satisfy the “no three in a row” rule with the given `k` and `n`, output `-1`.

Return the minimum possible total cost to paint all posts while respecting the constraint.

![Problem Illustration](../images/DP-013/problem-illustration.png)

## Input Format

- First line: two integers `n` and `k`
- Second line: `n` integers `s[1..n]`, where `s[1]` may be `0` and `s[i]` is the cost paid **only when** the color at post `i` differs from the color at post `i-1}`.

## Output Format

- Single integer: the minimum achievable total cost, or `-1` if no valid coloring exists.

## Constraints

- `1 <= n <= 100000`
- `1 <= k <= 50`
- `0 <= s[i] <= 10000`
- All costs fit in 64-bit signed integers.

## Example

**Input:**
```
3 2
0 2 1
```

**Output:**
```
4
```

**Explanation:**

- Paint post 1 with color A (cost 1).
- Paint post 2 with color A (cost 1, no switch).
- Paint post 3 with color B (cost 1 + switch 1).
- Total = 4; the sequence A, A, B respects the “no three identical in a row” rule.

![Example Visualization](../images/DP-013/example-1.png)

## Notes

- If `k = 1`, you can paint at most two posts; for `n > 2`, the answer is `-1`.
- Switch cost applies only when the color changes between consecutive posts.
- Use 64-bit arithmetic when summing costs.

## Related Topics

Dynamic Programming, Optimization, Greedy

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long minCost(int n, int k, int[] s) {
        // Implementation here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), k = sc.nextInt();
        int[] s = new int[n];
        for (int i = 0; i < n; i++) s[i] = sc.nextInt();
        Solution sol = new Solution();
        System.out.println(sol.minCost(n, k, s));
        sc.close();
    }
}
```

### Python

```python
from typing import List

def min_cost(n: int, k: int, s: List[int]) -> int:
    # Implementation here
    return 0

def main():
    n, k = map(int, input().split())
    s = list(map(int, input().split()))
    print(min_cost(n, k, s))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <deque>
#include <queue>

using namespace std;

class Solution {
public:
    long long minCost(int n, int k, const vector<int>& s) {
        // Implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, k;
    if (!(cin >> n >> k)) return 0;
    vector<int> s(n);
    for (int i = 0; i < n; ++i) cin >> s[i];
    cout << minCost(n, k, s) << '\n';
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  minCost(n, k, s) {
    // Implementation here
    return null;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  if (data.length === 0) return;

  let ptr = 0;
  const parts = data[ptr++].split(/\s+/).map(Number);
  const n = parts[0];
  const k = parts[1];
  const s = data[ptr++].split(/\s+/).map(x => parseInt(x));

  console.log(new Solution().minCost(n, k, s));
});
```
