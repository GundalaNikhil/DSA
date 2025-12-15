---
problem_id: ARR_SLIDE_WINDOW__96A0
display_id: ARR-010
slug: early-discount-window
title: "Early Discount With Stay Window"
difficulty: Easy
difficulty_score: 30
topics:
  - Array
  - Sliding Window
  - Stock Trading
  - Optimization
tags:
  - arrays
  - sliding-window
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Early Discount With Stay Window

## Problem Statement

You may buy once and sell once. You must hold the item for at least `dMin` days and at most `dMax` days, and the sell price must not exceed a ceiling `C` (if price > C, you are forced to sell at C). Return maximum achievable profit (or 0 if not profitable).

![Problem Illustration](../images/ARR-010/problem-illustration.png)


## Input Format

- First line: Integer `n` (1 ≤ n ≤ 2 × 10^5) - number of days
- Second line: `n` space-separated integers representing prices
- Third line: Three integers `dMin`, `dMax`, `C` - constraints

## Output Format

Print the maximum achievable profit, or 0 if no profitable trade exists.

## Constraints

- 1 ≤ n ≤ 2 × 10^5
- 0 ≤ price[i] ≤ 10^9
- 1 ≤ dMin ≤ dMax ≤ n
- 0 ≤ C ≤ 10^9

## Examples

### Example 1

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

- Buy at price 1 on day 3 (0-indexed)
- Sell at min(9, 6) = 6 on day 4
- Profit = 6 - 1 = 5

![Example 1 Visualization](../images/ARR-010/example-1.png)

### Example 2

**Input:**

```
5
5 4 3 2 1
1 2 10
```

**Output:**

```
0
```

**Explanation:**

- Prices are declining throughout
- No profitable trade possible within holding constraints

## Notes

- Track best effective buy value up to day i-dMin
- When selling on day i: profit = min(price[i], C) - best buy in window [i-dMax, i-dMin]

## Related Topics

Array, Sliding Window, Stock Trading, Optimization

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int maxProfit(int[] prices, int dMin, int dMax, int C) {
        // Your implementation here
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] prices = new int[n];
        for (int i = 0; i < n; i++) {
            prices[i] = sc.nextInt();
        }
        int dMin = sc.nextInt();
        int dMax = sc.nextInt();
        int C = sc.nextInt();

        Solution solution = new Solution();
        int result = solution.maxProfit(prices, dMin, dMax, C);

        System.out.println(result);
        sc.close();
    }
}
```

### Python

```python
from typing import List

def max_profit(prices: List[int], dMin: int, dMax: int, C: int) -> int:
    # Your implementation here
    pass

def main():
    n = int(input())
    prices = list(map(int, input().split()))
    dMin, dMax, C = map(int, input().split())
    result = max_profit(prices, dMin, dMax, C)
    print(result)

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
    int maxProfit(vector<int>& prices, int dMin, int dMax, int C) {
        // Your implementation here
    }
};

int main() {
    int n;
    cin >> n;
    vector<int> prices(n);
    for (int i = 0; i < n; i++) {
        cin >> prices[i];
    }
    int dMin, dMax, C;
    cin >> dMin >> dMax >> C;

    Solution solution;
    int result = solution.maxProfit(prices, dMin, dMax, C);

    cout << result << endl;

    return 0;
}
```

### JavaScript

```javascript
const readline = require('readline');

class Solution {
    maxProfit(prices, dMin, dMax, C) {
        // Your implementation here
    }
}

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let lines = [];
rl.on('line', (line) => {
    lines.push(line);
    if (lines.length === 3) {
        const n = parseInt(lines[0]);
        const prices = lines[1].split(' ').map(Number);
        const [dMin, dMax, C] = lines[2].split(' ').map(Number);

        const solution = new Solution();
        const result = solution.maxProfit(prices, dMin, dMax, C);

        console.log(result);
        rl.close();
    }
});
```
