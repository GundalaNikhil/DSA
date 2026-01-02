---
problem_id: ARR_EARLY_DISCOUNT_WINDOW__9051
display_id: ARR-010
slug: early-discount-stay-window
title: "Early Discount With Stay Window and Ceiling"
difficulty: Medium
difficulty_score: 50
topics:
  - Arrays
  - Sliding Window
  - Greedy
tags:
  - arrays
  - sliding-window
  - greedy
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# ARR-010: Early Discount With Stay Window and Ceiling

## Problem Statement

You may buy once and sell once. You must hold the item for at least dMin days and at most dMax days. The selling price is capped at C. Return the maximum profit, or 0 if no profitable trade exists.

![Problem Illustration](../images/ARR-010/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers prices[i]
- Third line: integers dMin, dMax, and C

## Output Format

Print the maximum achievable profit (0 if none).

## Constraints

- `1 <= n <= 200000`
- `0 <= prices[i] <= 1000000000`
- `1 <= dMin <= dMax <= n`
- `0 <= C <= 1000000000`

## Example

**Input:**
```
5
7 2 5 1 9
1 3 6
```

**Output:**
```
5
```

**Explanation:**

Buy at price 1 and sell at min(9, 6) = 6 for a profit of 5.

![Example Visualization](../images/ARR-010/example-1.png)

## Notes

- You must buy before you sell.
- The holding period is in days between buy and sell indices.

## Related Topics

Sliding Window, Greedy, Arrays

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int maxProfitWithConstraints(int[] prices, int dMin, int dMax, int C) {
        // Implementation here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] prices = new int[n];
        for (int i = 0; i < n; i++) prices[i] = sc.nextInt();

        int dMin = sc.nextInt();
        int dMax = sc.nextInt();
        int C = sc.nextInt();

        Solution solution = new Solution();
        System.out.println(solution.maxProfitWithConstraints(prices, dMin, dMax, C));
        sc.close();
    }
}
```

### Python

```python
import sys
from collections import deque

def max_profit_with_constraints(prices: list[int], dMin: int, dMax: int, C: int) -> int:
    # Implementation here
    return 0

def main():

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maxProfitWithConstraints(vector<int>& prices, int dMin, int dMax, int C) {
        // Implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> prices(n);
    for (int i = 0; i < n; i++) cin >> prices[i];

    int dMin, dMax, C;
    cin >> dMin >> dMax >> C;

    Solution solution;
    cout << solution.maxProfitWithConstraints(prices, dMin, dMax, C) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  maxProfitWithConstraints(prices, dMin, dMax, C) {
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
  const tokens = data.join(" ").split(/\s+/);
  if (tokens.length === 0 || tokens[0] === "") return;

  let ptr = 0;
  const n = Number(tokens[ptr++]);
  const prices = [];
  for (let i = 0; i < n; i++) prices.push(Number(tokens[ptr++]));

  const dMin = Number(tokens[ptr++]);
  const dMax = Number(tokens[ptr++]);
  const C = Number(tokens[ptr++]);

  const solution = new Solution();
  console.log(solution.maxProfitWithConstraints(prices, dMin, dMax, C));
});
```
