---
problem_id: PRB_RANDOM_WALK_HITTING_PROB_2D__5274
display_id: PRB-013
slug: random-walk-hitting-prob-2d
title: "Random Walk Hitting Probability 2D"
difficulty: Hard
difficulty_score: 70
topics:
  - Probability
  - Random Walk
  - Dynamic Programming
tags:
  - probability
  - random-walk
  - dp
  - hard
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PRB-013: Random Walk Hitting Probability 2D

## Problem Statement

A simple symmetric random walk starts at `(0,0)` on the 2D integer grid. At each step, it moves one unit north, south, east, or west with equal probability.

Given a target `(a, b)` and a time horizon `T`, compute the probability that the walk hits `(a, b)` at least once within `T` steps.

![Problem Illustration](../images/PRB-013/problem-illustration.png)

## Input Format

- Single line: integers `a`, `b`, and `T`

## Output Format

- Single floating-point number: probability of hitting within `T` steps

## Constraints

- `|a|, |b| <= 10`
- `1 <= T <= 500`

## Example

**Input:**

```
1 0 1
```

**Output:**

```
0.250000
```

**Explanation:**

The walk reaches (1,0) in one step only if it moves east, which has probability 1/4.

![Example Visualization](../images/PRB-013/example-1.png)

## Notes

- Use DP over steps and bounded positions
- Track probability of first hit or use complement of never hitting
- Accept answers with absolute error <= 1e-6
- Time complexity: O(T * bound^2)

## Related Topics

Random Walks, DP, Probability

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public double hitProbability(int a, int b, int T) {
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
            int T = sc.nextInt();

            Solution solution = new Solution();
            System.out.printf("%.6f\n", solution.hitProbability(a, b, T));
        }
        sc.close();
    }
}
```

### Python

```python
import sys

def hit_probability(a: int, b: int, T: int) -> float:
    # //Implement here
    return 0

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    a = int(data[0])
    b = int(data[1])
    T = int(data[2])
    print(f"{hit_probability(a, b, T):.6f}")

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;

class Solution {
public:
    double hitProbability(int a, int b, int T) {
        //Implement here
        return 0.0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int a, b, T;
    if (cin >> a >> b >> T) {
        Solution solution;
        cout << fixed << setprecision(6) << solution.hitProbability(a, b, T) << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function hitProbability(a, b, T) {
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
  const T = parseInt(data[2], 10);
  console.log(hitProbability(a, b, T).toFixed(6));
});
```

