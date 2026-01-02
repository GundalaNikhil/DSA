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

![Problem Illustration](../images/DP-002/problem-illustration.png)

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

class Solution {
    private static final long INF = Long.MAX_VALUE / 4;

    private static long key(long dpVal, int y) {
        return dpVal - (long) y;
    }

    public long minCost(int k, int target, int[] d, long[] c, long[] p) {
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int k = sc.nextInt();
        int target = sc.nextInt();
        int[] d = new int[k];
        long[] c = new long[k];
        long[] p = new long[k];
        for (int i = 0; i < k; i++) {
            d[i] = sc.nextInt();
            c[i] = sc.nextLong();
            p[i] = sc.nextLong();
        }
        System.out.println(new Solution().minCost(k, target, d, c, p));
        sc.close();
    }
}
```

### Python

```python
from collections import deque

INF = 10**30

def min_cost(k: int, target: int, d: list[int], c: list[int], p: list[int]) -> int:
    return 0
def main():
    k, target = map(int, input().split())
    d, c, p = [], [], []
    for _ in range(k):
        di, ci, pi = map(int, input().split())
        d.append(di); c.append(ci); p.append(pi)
    print(min_cost(k, target, d, c, p))

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
#include <stack>
#include <string>
#include <sstream>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <numeric>
#include <limits>
#include <cmath>
#include <cstring>
#include <utility>
using namespace std;

class Solution {
    static constexpr long long INF = (1LL<<62);
public:
    long long minCost(int k, int target, const vector<int>& d,
                      const vector<long long>& c, const vector<long long>& p) {
        vector<long long> dp(target + 1, INF);
        dp[0] = 0;

        for (int i = 0; i < k; i++) {
            int denom = d[i];
            int cap = (int)min<long long>(c[i], target / (long long)denom);
            int t = (int)min<long long>(c[i] / 2LL, cap);
            long long penalty = p[i];

            vector<long long> nxt(target + 1, INF);

            for (int r = 0; r < denom; r++) {
                int qMax = (target - r) / denom;
                if (qMax < 0) continue;

                int L1 = min(cap, t);
                deque<int> dqNo, dqPen;

                auto key = [&](int q) -> long long {
                    long long val = dp[r + q * denom];
                    return val - (long long)q;
                };

                for (int q = 0; q <= qMax; q++) {
                    int sQ = r + q * denom;

                    if (dp[sQ] < INF) {
                        long long kv = key(q);
                        while (!dqNo.empty() && kv <= key(dqNo.back())) dqNo.pop_back();
                        dqNo.push_back(q);
                    }

                    int minY = q - L1;
                    while (!dqNo.empty() && dqNo.front() < minY) dqNo.pop_front();

                    long long best = INF;
                    if (!dqNo.empty()) best = min(best, (long long)q + key(dqNo.front()));

                    if (cap > t) {
                        int yAdd = q - (t + 1);
                        if (yAdd >= 0) {
                            int sAdd = r + yAdd * denom;
                            if (dp[sAdd] < INF) {
                                long long kv = key(yAdd);
                                while (!dqPen.empty() && kv <= key(dqPen.back())) dqPen.pop_back();
                                dqPen.push_back(yAdd);
                            }
                        }

                        int minYPen = q - cap;
                        while (!dqPen.empty() && dqPen.front() < minYPen) dqPen.pop_front();

                        if (!dqPen.empty()) best = min(best, (long long)q + penalty + key(dqPen.front()));
                    }

                    int s = r + q * denom;
                    nxt[s] = min(nxt[s], best);
                }
            }

            dp.swap(nxt);
        }

        return dp[target] >= INF ? -1 : dp[target];
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k, target;
    cin >> k >> target;
    vector<int> d(k);
    vector<long long> c(k), p(k);
    for (int i = 0; i < k; i++) cin >> d[i] >> c[i] >> p[i];

    Solution sol;
    cout << sol.minCost(k, target, d, c, p) << '\n';
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

const INF = 10n ** 30n;

class Deque {
  constructor() {
    this.a = [];
    this.h = 0;
  }
  pushBack(x) { this.a.push(x); }
  popBack() { this.a.pop(); }
  popFront() { this.h++; }
  front() { return this.a[this.h]; }
  back() { return this.a[this.a.length - 1]; }
  empty() { return this.h >= this.a.length; }
  cleanup() {
    if (this.h > 1024 && this.h * 2 > this.a.length) {
      this.a = this.a.slice(this.h);
      this.h = 0;
    }
  }
}

class Solution {
  minCost(k, target, d, c, p) {
    return 0;
  }
}

const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
const lines = [];
rl.on("line", (line) => lines.push(line.trim()));
rl.on("close", () => {
  let idx = 0;
  const [kStr, targetStr] = lines[idx++].split(" ");
  const k = Number(kStr);
  const target = Number(targetStr);
  const d = new Array(k), c = new Array(k), p = new Array(k);
  for (let i = 0; i < k; i++) {
    const [di, ci, pi] = lines[idx++].split(" ").map(Number);
    d[i] = di; c[i] = ci; p[i] = pi;
  }
  const sol = new Solution();
  console.log(sol.minCost(k, target, d, c, p));
});
```

