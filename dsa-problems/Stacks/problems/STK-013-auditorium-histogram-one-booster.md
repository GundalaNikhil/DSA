---
problem_id: STK_AUDITORIUM_HISTOGRAM_ONE_BOOSTER__9153
display_id: STK-013
slug: auditorium-histogram-one-booster
title: "Auditorium Histogram With One Booster"
difficulty: Medium
difficulty_score: 60
topics:
  - Stack
  - Histogram
  - Optimization
tags:
  - stack
  - histogram
  - optimization
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# STK-013: Auditorium Histogram With One Booster

## Problem Statement

You are given histogram heights. You may increase exactly one bar by at most `b` units (you may choose to add less than `b`). Compute the maximum possible rectangle area after the boost.

![Problem Illustration](../images/STK-013/problem-illustration.png)

## Input Format

- First line: integers `n` and `b`
- Second line: `n` space-separated integers (heights)

## Output Format

- Single integer: maximum possible rectangle area

## Constraints

- `1 <= n <= 200000`
- `0 <= h[i], b <= 10^9`

## Example

**Input:**

```
3 3
2 4 2
```

**Output:**

```
7
```

**Explanation:**

Boost the middle bar to 7; the best rectangle has area 7.

![Example Visualization](../images/STK-013/example-1.png)

## Notes

- The classic largest-rectangle-in-histogram uses a monotonic stack
- You must account for a single boosted bar
- Consider how far each bar can extend as the minimum height
- Time complexity should be near O(n)

## Related Topics

Histogram, Monotonic Stack, Optimization

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long maxAreaWithBooster(int n, long b, long[] h) {
        // Implement here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            long b = sc.nextLong();
            long[] h = new long[n];
            for (int i = 0; i < n; i++) {
                if (sc.hasNextLong()) h[i] = sc.nextLong();
            }
            Solution sol = new Solution();
            System.out.println(sol.maxAreaWithBooster(n, b, h));
        }
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def max_area_with_booster(self, n: int, b: int, h: list) -> int:
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    b = int(input_data[1])
    h = [int(x) for x in input_data[2:]]
    sol = Solution()
    print(sol.max_area_with_booster(n, b, h))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>

using namespace std;

class Solution {
public:
    long long maxAreaWithBooster(int n, long long b, const vector<long long>& h) {
        // Implement here
        return 0;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    long long b;
    if (cin >> n >> b) {
        vector<long long> h(n);
        for (int i = 0; i < n; i++) {
            cin >> h[i];
        }
        Solution sol;
        cout << sol.maxAreaWithBooster(n, b, h) << endl;
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  maxAreaWithBooster(n, b, h) {
    // Implement here
    return 0n;
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
  const [n, b] = input[0].split(/\s+/).map(Number);
  const h = input[1].split(/\s+/).map(BigInt);
  const sol = new Solution();
  console.log(sol.maxAreaWithBooster(n, BigInt(b), h).toString());
});
```
