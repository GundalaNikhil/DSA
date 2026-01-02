---
problem_id: DP_STOCK_WEEK_REST_FEE__6420
display_id: DP-015
slug: stock-trading-weekly-rest-fee
title: "Stock Trading With Weekly Rest and Fee"
difficulty: Medium
difficulty_score: 55
topics:
  - Dynamic Programming
  - Greedy
  - Finance
tags:
  - dp
  - stocks
  - cooldown
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP-015: Stock Trading With Weekly Rest and Fee

## Problem Statement

You are given stock prices for `n` days and a transaction fee `f`. Day 0 is Monday, day 1 is Tuesday, day 6 is Sunday, day 7 is the next Monday, and so on.

Rules:

- You may buy and sell multiple times.
- After **every sale on day `i`**, you must **rest until the next Monday** (day index `i - (i % 7) + 7`). During rest you cannot buy, but you may finish the sale that triggered the rest.
- Each sale pays `price[i] - fee` (the fee is subtracted once per sale).

Find the maximum achievable profit.

![Problem Illustration](../images/DP-015/problem-illustration.png)

## Input Format

- First line: two integers `n` and `f`
- Second line: `n` integers `price[0..n-1]`

## Output Format

- Single integer: maximum profit.

## Constraints

- `1 <= n <= 100000`
- `0 <= price[i], f <= 10^9`
- Use 64-bit integers to store profits.

## Example

**Input:**
```
7 1
1 5 3 6 4 2 7
```

**Output:**
```
5
```

**Explanation:**

- Buy day 0 (Mon) at 1, sell day 1 (Tue) at 5 → profit 4, rest until next Monday (day 7, beyond the list).
- Profit = 4; no further trades possible.
- Best profit is 5 by instead holding longer: buy day 0 at 1, sell day 3 at 6 → profit 5, rest to day 7.

![Example Visualization](../images/DP-015/example-1.png)

## Notes

- You cannot buy during a rest window triggered by your last sale.
- Buying and selling on the same day is not allowed by this model (sell uses stock you already held).
- If you never sell, profit is 0.

## Related Topics

Dynamic Programming, Cooldown Scheduling, Greedy

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long maxProfit(int[] prices, long fee) {
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        long fee = sc.nextLong();
        int[] prices = new int[n];
        for (int i = 0; i < n; i++) prices[i] = sc.nextInt();
        Solution sol = new Solution();
        System.out.println(sol.maxProfit(prices, fee));
        sc.close();
    }
}
```

### Python

```python
from typing import List

def max_profit(prices: List[int], fee: int) -> int:
    return 0
def main():
    n, fee = map(int, input().split())
    prices = list(map(int, input().split()))
    print(max_profit(prices, fee))

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

long long maxProfit(const vector<int>& prices, long long fee) {
    int n = (int)prices.size();
    const long long NEG = (long long)-4e18;
    long long buyable = 0, hold = NEG, ans = 0;
    vector<long long> unlock(n + 8, NEG);
    for (int i = 0; i < n; ++i) {
        if (unlock[i] != NEG) buyable = max(buyable, unlock[i]);
        long long prevHold = hold;
        hold = max(hold, buyable - prices[i]);
        if (prevHold != NEG) {
            long long sellProfit = prevHold + prices[i] - fee;
            ans = max(ans, sellProfit);
            int nextMonday = i - (i % 7) + 7;
            if (nextMonday < (int)unlock.size()) {
                unlock[nextMonday] = max(unlock[nextMonday], sellProfit);
            }
        }
    }
    if (hold != NEG) ans = max(ans, hold + prices.back() - fee);
    ans = max(ans, buyable);
    for (int i = n; i < (int)unlock.size(); ++i) ans = max(ans, unlock[i]);
    return ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; long long fee;
    if (!(cin >> n >> fee)) return 0;
    vector<int> prices(n);
    for (int i = 0; i < n; ++i) cin >> prices[i];
    cout << maxProfit(prices, fee) << '\n';
    return 0;
}
```

### JavaScript

```javascript
const NEG = BigInt(-4e18);

function maxProfit(prices, fee) {
    return 0;
  }

const readline = require("readline");

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
  const fee = parts[1];
  const prices = data[ptr++].split(/\s+/).map(Number);

  console.log(maxProfit(prices, fee));
});
```

