---
problem_id: PRB_COIN_FLIP_STREAK_PROBABILITY__1842
display_id: PRB-001
slug: coin-flip-streak-probability
title: "Coin Flip Streak Probability"
difficulty: Medium
difficulty_score: 40
topics:
  - Probability
  - Dynamic Programming
  - Markov Chains
tags:
  - probability
  - dp
  - streaks
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PRB-001: Coin Flip Streak Probability

## Problem Statement

A fair coin is flipped `n` times. Compute the probability of getting at least one streak of `k` consecutive heads.

![Problem Illustration](../images/PRB-001/problem-illustration.png)

## Input Format

- Single line: two integers `n` and `k`

## Output Format

- Single floating-point number: the probability

## Constraints

- `1 <= n <= 60`
- `1 <= k <= n`

## Example

**Input:**

```
3 2
```

**Output:**

```
0.375
```

**Explanation:**

The sequences with at least one streak of two consecutive heads are HHT, HHH, and THH. Each has probability 1/8, total 3/8 = 0.375.

![Example Visualization](../images/PRB-001/example-1.png)

## Notes

- Use DP with state (position, current run of heads)
- Probability = 1 - probability of no length-k streak
- Accept answers with absolute error <= 1e-6
- Time complexity: O(n \* k)

## Related Topics

Probability, DP, Streaks

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public double streakProbability(int n, int k) {
        //Implement here
        return 0.0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int k = sc.nextInt();
            Solution solution = new Solution();
            System.out.printf("%.6f\n", solution.streakProbability(n, k));
        }
        sc.close();
    }
}
```

### Python

```python
import sys

def streak_probability(n: int, k: int) -> float:
    # //Implement here
    return 0

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    k = int(data[1])
    print(f"{streak_probability(n, k):.6f}")

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>

using namespace std;

class Solution {
public:
    double streakProbability(int n, int k) {
        //Implement here
        return 0.0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (cin >> n >> k) {
        Solution solution;
        cout << fixed << setprecision(6) << solution.streakProbability(n, k) << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function streakProbability(n, k) {
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
  const n = parseInt(data[0], 10);
  const k = parseInt(data[1], 10);
  console.log(streakProbability(n, k).toFixed(6));
});
```

