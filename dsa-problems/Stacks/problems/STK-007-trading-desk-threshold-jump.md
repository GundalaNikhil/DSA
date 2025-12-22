---
problem_id: STK_TRADING_DESK_THRESHOLD_JUMP__2549
display_id: STK-007
slug: trading-desk-threshold-jump
title: "Trading Desk Threshold Jump"
difficulty: Medium
difficulty_score: 48
topics:
  - Stack
  - Monotonic Stack
  - Arrays
tags:
  - stack
  - monotonic
  - next-greater
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# STK-007: Trading Desk Threshold Jump

## Problem Statement

Given prices `p[i]` and a threshold `t`, for each index find how many steps forward until you see a price at least `t` higher than `p[i]`. If no such future price exists, output `0`.

![Problem Illustration](../images/STK-007/problem-illustration.png)

## Input Format

- First line: integers `n` and `t`
- Second line: `n` space-separated integers

## Output Format

- Single line: `n` integers of wait steps (0 if none)

## Constraints

- `1 <= n <= 200000`
- `0 <= p[i], t <= 10^9`

## Example

**Input:**

```
5 2
3 1 4 6 5
```

**Output:**

```
2 1 1 0 0
```

**Explanation:**

For 3, the first price at least 2 higher is 4 at distance 2. For 6, no future price is >= 8.

![Example Visualization](../images/STK-007/example-1.png)

## Notes

- Use a monotonic stack of indices
- Compare `p[j] - p[i] >= t`
- Pop indices that are satisfied by the current price
- Time complexity: O(n)

## Related Topics

Next Greater Element, Monotonic Stack, Arrays

---

## Solution Template
### Java

```java
import java.util.*;

class Solution {
    public int[] thresholdJump(int[] prices, int t) {
        // Your implementation here
        return new int[0];
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int t = sc.nextInt();
        int[] prices = new int[n];
        for (int i = 0; i < n; i++) prices[i] = sc.nextInt();

        Solution solution = new Solution();
        int[] result = solution.thresholdJump(prices, t);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < result.length; i++) {
            if (i > 0) sb.append(' ');
            sb.append(result[i]);
        }
        System.out.println(sb.toString());
        sc.close();
    }
}
```

### Python

```python
def threshold_jump(prices: list[int], t: int) -> list[int]:
    # Your implementation here
    return []

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    t = int(next(it))
    prices = [int(next(it)) for _ in range(n)]

    result = threshold_jump(prices, t)
    sys.stdout.write(" ".join(str(x) for x in result))

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
    vector<int> thresholdJump(const vector<int>& prices, int t) {
        // Your implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, t;
    if (!(cin >> n >> t)) return 0;
    vector<int> prices(n);
    for (int i = 0; i < n; i++) cin >> prices[i];

    Solution solution;
    vector<int> result = solution.thresholdJump(prices, t);
    for (int i = 0; i < (int)result.size(); i++) {
        if (i) cout << ' ';
        cout << result[i];
    }
    cout << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  thresholdJump(prices, t) {
    // Your implementation here
    return [];
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
  const t = parseInt(data[idx++], 10);
  const prices = [];
  for (let i = 0; i < n; i++) prices.push(parseInt(data[idx++], 10));

  const solution = new Solution();
  const result = solution.thresholdJump(prices, t);
  console.log(result.join(" "));
});
```
