---
problem_id: PRB_EXPECTED_STEPS_RANDOM_WALK_1D__3079
display_id: PRB-002
slug: expected-steps-random-walk-1d
title: "Expected Steps Random Walk 1D"
difficulty: Medium
difficulty_score: 50
topics:
  - Probability
  - Random Walk
  - Linear Equations
tags:
  - probability
  - random-walk
  - dp
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PRB-002: Expected Steps Random Walk 1D

## Problem Statement

A random walk starts at position 0 on the integer line. Each step moves +1 with probability `p`, and -1 with probability `1-p`. The walk stops when it reaches `+a` or `-b` (absorbing boundaries). Compute the expected number of steps until absorption.

![Problem Illustration](../images/PRB-002/problem-illustration.png)

## Input Format

- Single line: integers `a`, `b`, and real `p`

## Output Format

- Single floating-point number: expected steps

## Constraints

- `1 <= a, b <= 200`
- `0 < p < 1`

## Example

**Input:**

```
2 1 0.5
```

**Output:**

```
2
```

**Explanation:**

For a symmetric walk with boundaries at +2 and -1, the expected time to absorption from 0 is 2.

![Example Visualization](../images/PRB-002/example-1.png)

## Notes

- Use DP or solve linear equations for states in [-b+1, a-1]
- Accept answers with absolute error <= 1e-6
- Time complexity: O((a+b)^2) for equation solving

## Related Topics

Random Walk, Expected Value, Linear Systems

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public double expectedSteps(int a, int b, double p) {
        //Implement here
        return 0.0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            double p = sc.nextDouble();
            Solution solution = new Solution();
            System.out.printf("%.6f\n", solution.expectedSteps(a, b, p));
        }
        sc.close();
    }
}
```

### Python

```python
import sys

def expected_steps(a: int, b: int, p: float) -> float:
    # //Implement here
    return 0

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    a = int(data[0])
    b = int(data[1])
    p = float(data[2])
    print(f"{expected_steps(a, b, p):.6f}")

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

class Solution {
public:
    double expectedSteps(int a, int b, double p) {
        //Implement here
        return 0.0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int a, b;
    double p;
    if (cin >> a >> b >> p) {
        Solution solution;
        cout << fixed << setprecision(6) << solution.expectedSteps(a, b, p) << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function expectedSteps(a, b, p) {
  //Implement here
  return 0;
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  const a = parseInt(data[0], 10);
  const b = parseInt(data[1], 10);
  const p = parseFloat(data[2]);
  console.log(expectedSteps(a, b, p).toFixed(6));
});
```

