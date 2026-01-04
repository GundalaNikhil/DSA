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
    public int[] waitSteps(int n, int t, int[] p) {
        // Implement here
        return new int[n];
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int t = sc.nextInt();
            int[] p = new int[n];
            for (int i = 0; i < n; i++) {
                if (sc.hasNextInt()) p[i] = sc.nextInt();
            }
            Solution sol = new Solution();
            int[] res = sol.waitSteps(n, t, p);
            for (int i = 0; i < n; i++) {
                System.out.print(res[i] + (i == n - 1 ? "" : " "));
            }
            System.out.println();
        }
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def wait_steps(self, n: int, t: int, p: list) -> list:
        # Implement here
        return [0] * n

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    t = int(input_data[1])
    p = [int(x) for x in input_data[2:]]
    sol = Solution()
    res = sol.wait_steps(n, t, p)
    print(*(res))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <stack>

using namespace std;

class Solution {
public:
    vector<int> waitSteps(int n, int t, const vector<int>& p) {
        // Implement here
        return vector<int>(n, 0);
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, t;
    if (cin >> n >> t) {
        vector<int> p(n);
        for (int i = 0; i < n; i++) {
            cin >> p[i];
        }
        Solution sol;
        vector<int> res = sol.waitSteps(n, t, p);
        for (int i = 0; i < n; i++) {
            cout << res[i] << (i == n - 1 ? "" : " ");
        }
        cout << endl;
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  waitSteps(n, t, p) {
    // Implement here
    return new Array(n).fill(0);
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false,
});

let input = [];
rl.on("line", (line) => {
  if (line.trim()) input.push(line.trim());
}).on("close", () => {
  if (input.length < 2) return;
  const [n, t] = input[0].split(/\s+/).map(Number);
  const p = input[1].split(/\s+/).map(Number);
  const sol = new Solution();
  const res = sol.waitSteps(n, t, p);
  console.log(res.join(" "));
});
```
