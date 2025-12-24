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
    public long minCost(int k, int target, int[] d, long[] c, long[] p) {
        // Your implementation here
        return -1;
    }
}

public class Main {
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
def min_cost(k: int, target: int, d: list[int], c: list[int], p: list[int]) -> int:
    # Your implementation here
    return -1

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
using namespace std;

class Solution {
public:
    long long minCost(int k, int target, const vector<int>& d,
                      const vector<long long>& c, const vector<long long>& p) {
        // Your implementation here
        return -1;
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
    cout << sol.minCost(k, target, d, c, p) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  minCost(k, target, d, c, p) {
    // Your implementation here
    return -1;
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
  const d = new Array(k);
  const c = new Array(k);
  const p = new Array(k);
  for (let i = 0; i < k; i++) {
    const [di, ci, pi] = lines[idx++].split(" ").map(Number);
    d[i] = di; c[i] = ci; p[i] = pi;
  }
  const sol = new Solution();
  console.log(sol.minCost(k, target, d, c, p));
});
```
