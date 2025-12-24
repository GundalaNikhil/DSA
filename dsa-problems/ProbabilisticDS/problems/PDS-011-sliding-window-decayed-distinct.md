---
problem_id: PDS_SLIDING_WINDOW_DECAYED_DISTINCT__5072
display_id: PDS-011
slug: sliding-window-decayed-distinct
title: "Sliding Window Distinct with Exponential Decay"
difficulty: Medium
difficulty_score: 56
topics:
  - Probabilistic Data Structures
  - Sliding Window
  - Decay
tags:
  - probabilistic-ds
  - sliding-window
  - decay
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PDS-011: Sliding Window Distinct with Exponential Decay

## Problem Statement

Estimate a decayed distinct count using the last-seen time of each distinct item. Given current time `T`, decay factor `lambda`, and last-seen timestamps `t_i`, compute:

```
Estimate = sum exp(-lambda * (T - t_i))
```

![Problem Illustration](../images/PDS-011/problem-illustration.png)

## Input Format

- First line: integer `T`, real `lambda`, and integer `m`
- Second line: `m` integers (last-seen times)

## Output Format

- Single floating-point number: decayed distinct estimate

## Constraints

- `0 <= T <= 10^9`
- `0 < lambda <= 1`
- `1 <= m <= 100000`
- `0 <= t_i <= T`

## Example

**Input:**

```
10 0.1 3
10 8 5
```

**Output:**

```
2.425261
```

**Explanation:**

exp(0) + exp(-0.2) + exp(-0.5) = 2.425261.

![Example Visualization](../images/PDS-011/example-1.png)

## Notes

- Use double precision
- Accept answers with absolute error <= 1e-6
- Time complexity: O(m)

## Related Topics

Exponential Decay, Sliding Window, Distinct Counting

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public double decayedDistinct(int T, double lambda, int[] times) {
        // Your implementation here
        return 0.0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        double lambda = sc.nextDouble();
        int m = sc.nextInt();
        int[] times = new int[m];
        for (int i = 0; i < m; i++) times[i] = sc.nextInt();

        Solution solution = new Solution();
        System.out.println(solution.decayedDistinct(T, lambda, times));
        sc.close();
    }
}
```

### Python

```python
import math

def decayed_distinct(T: int, lam: float, times):
    # Your implementation here
    return 0.0

def main():
    T, lam, m = input().split()
    T = int(T)
    lam = float(lam)
    m = int(m)
    times = list(map(int, input().split()))
    print(f"{decayed_distinct(T, lam, times):.6f}")

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
using namespace std;

class Solution {
public:
    double decayedDistinct(int T, double lambda, const vector<int>& times) {
        // Your implementation here
        return 0.0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T, m;
    double lambda;
    cin >> T >> lambda >> m;
    vector<int> times(m);
    for (int i = 0; i < m; i++) cin >> times[i];

    Solution solution;
    cout << solution.decayedDistinct(T, lambda, times) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function decayedDistinct(T, lambda, times) {
  // Your implementation here
  return 0.0;
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
  const T = parseInt(data[idx++], 10);
  const lambda = parseFloat(data[idx++]);
  const m = parseInt(data[idx++], 10);
  const times = [];
  for (let i = 0; i < m; i++) times.push(parseInt(data[idx++], 10));
  console.log(decayedDistinct(T, lambda, times).toFixed(6));
});
```
