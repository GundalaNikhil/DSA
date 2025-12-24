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
    public long maxAreaWithBoost(int[] h, long b) {
        // Your implementation here
        return 0L;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        long b = sc.nextLong();
        int[] h = new int[n];
        for (int i = 0; i < n; i++) h[i] = sc.nextInt();

        Solution solution = new Solution();
        System.out.println(solution.maxAreaWithBoost(h, b));
        sc.close();
    }
}
```

### Python

```python
def max_area_with_boost(h: list[int], b: int) -> int:
    # Your implementation here
    return 0

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    b = int(next(it))
    h = [int(next(it)) for _ in range(n)]

    print(max_area_with_boost(h, b))

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
    long long maxAreaWithBoost(const vector<int>& h, long long b) {
        // Your implementation here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long b;
    if (!(cin >> n >> b)) return 0;
    vector<int> h(n);
    for (int i = 0; i < n; i++) cin >> h[i];

    Solution solution;
    cout << solution.maxAreaWithBoost(h, b) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  maxAreaWithBoost(h, b) {
    // Your implementation here
    return 0;
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
  const b = parseInt(data[idx++], 10);
  const h = [];
  for (let i = 0; i < n; i++) h.push(parseInt(data[idx++], 10));

  const solution = new Solution();
  const result = solution.maxAreaWithBoost(h, b);
  console.log(result.toString());
});
```
