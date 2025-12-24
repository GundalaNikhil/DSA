---
problem_id: PRB_MEDIAN_UNIFORMS_CLT__3524
display_id: PRB-015
slug: median-uniforms-clt
title: "Median of Uniforms CLT"
difficulty: Medium
difficulty_score: 50
topics:
  - Probability
  - Statistics
  - CLT
tags:
  - probability
  - clt
  - median
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PRB-015: Median of Uniforms CLT

## Problem Statement

Let `n` i.i.d. random variables be uniformly distributed on [0,1]. Using the CLT approximation for the sample median, output the approximate mean and variance of the median.

For uniform distribution, the asymptotic variance is:

```
Var(median) ≈ 1 / (4n)
```

and the mean is 0.5.

![Problem Illustration](../images/PRB-015/problem-illustration.png)

## Input Format

- Single line: integer `n`

## Output Format

- Two floating-point numbers: mean and variance

## Constraints

- `1 <= n <= 1000`

## Example

**Input:**

```
5
```

**Output:**

```
0.500000 0.050000
```

**Explanation:**

Var ≈ 1/(4*5) = 0.05.

![Example Visualization](../images/PRB-015/example-1.png)

## Notes

- This is an approximation for large n
- Accept answers with absolute error <= 1e-6
- Time complexity: O(1)

## Related Topics

CLT, Order Statistics, Probability

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public double[] medianClt(int n) {
        // Your implementation here
        return new double[]{0.0, 0.0};
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        Solution solution = new Solution();
        double[] res = solution.medianClt(n);
        System.out.printf("%.6f %.6f\n", res[0], res[1]);
        sc.close();
    }
}
```

### Python

```python
def median_clt(n: int):
    # Your implementation here
    return 0.0, 0.0

def main():
    n = int(input())
    mean, var = median_clt(n)
    print(f"{mean:.6f} {var:.6f}")

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

class Solution {
public:
    pair<double, double> medianClt(int n) {
        // Your implementation here
        return {0.0, 0.0};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    Solution solution;
    auto res = solution.medianClt(n);
    cout << fixed << setprecision(6) << res.first << " " << res.second << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function medianClt(n) {
  // Your implementation here
  return [0.0, 0.0];
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  if (data.length === 0) return;
  const n = parseInt(data[0], 10);
  const res = medianClt(n);
  console.log(res[0].toFixed(6) + " " + res[1].toFixed(6));
});
```
