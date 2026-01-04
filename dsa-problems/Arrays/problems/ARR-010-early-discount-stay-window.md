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
import java.io.*;

class Solution {
    public int maxProfitDiscount(int n, int[] prices, int dMin, int dMax, int C) {
        // Implement here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String nLine = br.readLine();
        if (nLine == null) return;
        int n = Integer.parseInt(nLine.trim());

        int[] prices = new int[n];
        String pLine = br.readLine();
        if (pLine != null) {
            String[] parts = pLine.trim().split("\\s+");
            for (int i = 0; i < n; i++) {
                prices[i] = Integer.parseInt(parts[i]);
            }
        }

        String constraintsLine = br.readLine();
        if (constraintsLine == null) return;
        String[] cParts = constraintsLine.trim().split("\\s+");
        int dMin = Integer.parseInt(cParts[0]);
        int dMax = Integer.parseInt(cParts[1]);
        int C = Integer.parseInt(cParts[2]);

        Solution sol = new Solution();
        System.out.println(sol.maxProfitDiscount(n, prices, dMin, dMax, C));
    }
}
```

### Python

```python
import sys

class Solution:
    def max_profit_discount(self, n, prices, d_min, d_max, C):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    prices = list(map(int, input_data[1:n+1]))
    d_min = int(input_data[n+1])
    d_max = int(input_data[n+2])
    C = int(input_data[n+3])

    sol = Solution()
    print(sol.max_profit_discount(n, prices, d_min, d_max, C))

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
    int maxProfitDiscount(int n, vector<int>& prices, int dMin, int dMax, int C) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> prices(n);
    for (int i = 0; i < n; i++) {
        cin >> prices[i];
    }

    int dMin, dMax, C;
    cin >> dMin >> dMax >> C;

    Solution sol;
    cout << sol.maxProfitDiscount(n, prices, dMin, dMax, C) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  maxProfitDiscount(n, prices, dMin, dMax, C) {
    // Implement here
    return 0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 1) return;

  let idx = 0;
  function readInt() {
    return parseInt(input[idx++]);
  }

  const n = readInt();
  const prices = [];
  for (let i = 0; i < n; i++) prices.push(readInt());
  const dMin = readInt();
  const dMax = readInt();
  const C = readInt();

  const sol = new Solution();
  console.log(sol.maxProfitDiscount(n, prices, dMin, dMax, C));
}

solve();
```
