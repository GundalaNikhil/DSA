---
problem_id: DP_COIN_CAP_PENALTY__1842
display_id: DP-002
slug: capped-coin-change-penalty
title: "Capped Coin Change With Penalty"
difficulty: Medium
difficulty_score: 58
topics:
  - Dynamic Programming
  - Knapsack
  - Optimization
tags:
  - dp
  - knapsack
  - bounded-knapsack
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP-002: Capped Coin Change With Penalty

## Problem Statement

You are given `k` coin types. Coin type `i` has:

- denomination `d[i]`
- maximum usable count `c[i]`
- penalty `p[i]`

You want to form an exact sum `target`.

Cost rules:

- Each coin you use contributes `+1` to total cost.
- For each coin type `i`, if you use **more than** `floor(c[i]/2)` coins of that type, you pay an additional one-time penalty `+p[i]` (for that type).

Compute the minimum total cost to form `target`. If it is impossible, print `-1`.

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767513325/dsa/dp/wroooy43bhikdkvrjhoa.jpg)

## Input Format

- First line: two integers `k` and `target`
- Next `k` lines: three integers `d[i] c[i] p[i]`

## Output Format

Print a single integer: the minimum cost, or `-1` if unreachable.

## Constraints

- `1 <= k <= 50`
- `1 <= target <= 5000`
- `1 <= d[i] <= 5000`
- `0 <= c[i] <= 10^9` (effective usage is capped by `target / d[i]`)
- `0 <= p[i] <= 10^9`

## Example

**Input:**

```
2 7
1 4 2
5 2 1
```

**Output:**

```
3
```

**Explanation:**

- One optimal way is `5 + 1 + 1 = 7`. It uses:
  - coin `5`: 1 time (≤ floor(2/2)=1, no penalty)
  - coin `1`: 2 times (≤ floor(4/2)=2, no penalty)
- Total coins used = 3, and no penalties are triggered ⇒ minimum cost is `3`.

![Example Visualization](../images/DP-002/example-1.png)

## Notes

- The penalty for type `i` is charged **at most once**, and only if `used_i > floor(c[i]/2)`.
- You must respect the maximum count `c[i]` for each type.
- This is a bounded knapsack variant with a “threshold + activation cost”.

## Related Topics

Dynamic Programming, Knapsack, Optimization

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public long minCost(int k, int target, long[][] coins) {
        // Implement here
        return -1;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String firstLine = br.readLine();
        if (firstLine == null) return;
        String[] parts = firstLine.trim().split("\\s+");
        int k = Integer.parseInt(parts[0]);
        int target = Integer.parseInt(parts[1]);

        long[][] coins = new long[k][3];
        for (int i = 0; i < k; i++) {
            String[] cParts = br.readLine().trim().split("\\s+");
            coins[i][0] = Long.parseLong(cParts[0]); // denomination
            coins[i][1] = Long.parseLong(cParts[1]); // capacity
            coins[i][2] = Long.parseLong(cParts[2]); // penalty
        }

        Solution sol = new Solution();
        System.out.println(sol.minCost(k, target, coins));
    }
}
```

### Python

```python
import sys

class Solution:
    def min_cost(self, k, target, coins):
        # Implement here
        return -1

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    k = int(input_data[0])
    target = int(input_data[1])
    idx = 2
    coins = []
    for _ in range(k):
        coins.append([int(input_data[idx]), int(input_data[idx+1]), int(input_data[idx+2])])
        idx += 3

    sol = Solution()
    print(sol.min_cost(k, target, coins))

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
    long long minCost(int k, int target, const vector<vector<long long>>& coins) {
        // Implement here
        return -1;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int k, target;
    if (!(cin >> k >> target)) return 0;

    vector<vector<long long>> coins(k, vector<long long>(3));
    for (int i = 0; i < k; i++) {
        cin >> coins[i][0] >> coins[i][1] >> coins[i][2];
    }

    Solution sol;
    cout << sol.minCost(k, target, coins) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  minCost(k, target, coins) {
    // Implement here
    return -1;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;

  let idx = 0;
  const k = parseInt(input[idx++]);
  const target = parseInt(input[idx++]);
  const coins = [];
  for (let i = 0; i < k; i++) {
    coins.push([
      BigInt(input[idx++]),
      BigInt(input[idx++]),
      BigInt(input[idx++]),
    ]);
  }

  const sol = new Solution();
  const res = sol.minCost(k, target, coins);
  console.log(res === null || res === undefined ? -1 : res.toString());
}

solve();
```
