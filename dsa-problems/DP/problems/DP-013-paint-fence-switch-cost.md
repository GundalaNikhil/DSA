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

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767513333/dsa/dp/llqliea6mb6jplerjlgp.jpg)

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
import java.io.*;

class Solution {
    public long minPaintingCost(int n, int k, int[] s) {
        // Implement here
        return -1;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String nkLine = br.readLine();
        if (nkLine == null) return;
        String[] nkParts = nkLine.trim().split("\\s+");
        int n = Integer.parseInt(nkParts[0]);
        int k = Integer.parseInt(nkParts[1]);

        int[] s = new int[n];
        String sLine = br.readLine();
        if (sLine != null) {
            String[] sParts = sLine.trim().split("\\s+");
            for (int i = 0; i < n; i++) {
                s[i] = Integer.parseInt(sParts[i]);
            }
        }

        Solution sol = new Solution();
        System.out.println(sol.minPaintingCost(n, k, s));
    }
}
```

### Python

```python
import sys

class Solution:
    def min_painting_cost(self, n, k, s):
        # Implement here
        return -1

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    k = int(input_data[1])
    s = list(map(int, input_data[2:2+n]))

    sol = Solution()
    print(sol.min_painting_cost(n, k, s))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    long long minPaintingCost(int n, int k, const vector<int>& s) {
        // Implement here
        return -1;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<int> s(n);
    for (int i = 0; i < n; i++) {
        cin >> s[i];
    }

    Solution sol;
    cout << sol.minPaintingCost(n, k, s) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  minPaintingCost(n, k, s) {
    // Implement here
    return -1;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const k = parseInt(input[idx++]);
  const s = [];
  for (let i = 0; i < n; i++) {
    s.push(parseInt(input[idx++]));
  }

  const sol = new Solution();
  const res = sol.minPaintingCost(n, k, s);
  console.log(res === null || res === undefined ? -1 : res.toString());
}

solve();
```
