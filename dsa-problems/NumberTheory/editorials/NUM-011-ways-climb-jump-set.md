---
problem_id: NUM_WAYS_CLIMB_JUMP_SET__7681
display_id: NUM-011
slug: ways-climb-jump-set
title: "Ways to Climb With Jumps Set"
difficulty: Medium
difficulty_score: 48
topics:
  - Number Theory
  - Dynamic Programming
  - Combinatorics
tags:
  - number-theory
  - dp
  - combinatorics
  - medium
premium: true
subscription_tier: basic
---

# NUM-011: Ways to Climb With Jumps Set

## 📋 Problem Summary

Count the number of ways to reach the `n`-th stair starting from 0, given a set of allowed jump sizes `J`.
- Input: Target `n`, jump sizes `J`.
- Output: Number of ways modulo `10^9+7`.

## 🌍 Real-World Scenario

**Scenario Title:** The Robot Climber

You are programming a robot to climb a staircase. The robot's hydraulics allow it to perform specific jumps (e.g., 1 step, 3 steps, or 5 steps at a time), but not others.
- You need to calculate the total number of distinct sequences of moves the robot can take to reach exactly the top of the stairs.
- This calculation helps in analyzing the complexity of the robot's motion planning algorithm or estimating the entropy of its path choices.

**Why This Problem Matters:**

- **Combinatorics:** Generalization of Fibonacci numbers.
- **Dynamic Programming:** Classic linear recurrence problem.
- **Compiler Design:** Parsing sequences with specific grammar rules.

![Real-World Application](../images/NUM-011/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Path Tree

Target `n=4`, Jumps `1, 3`.

```
Start (0)
|
+--- Jump 1 ---> (1)
|                |
|                +--- Jump 1 ---> (2)
|                |                |
|                |                +--- Jump 1 ---> (3)
|                |                |                |
|                |                |                +--- Jump 1 ---> (4) ✅ (1,1,1,1)
|                |                |
|                |                +--- Jump 3 ---> (X) > 4
|                |
|                +--- Jump 3 ---> (4) ✅ (1,3)
|
+--- Jump 3 ---> (3)
                 |
                 +--- Jump 1 ---> (4) ✅ (3,1)

Total Ways: 3
```

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Constraints:** `n <= 10^5`, `|J| <= 20`.
- **Modulo:** `10^9+7`.
- **Order Matters:** `1+3` is different from `3+1`.

### Core Concept: Linear Recurrence

Let `dp[i]` be the number of ways to reach step `i`.
To reach step `i`, the robot must have come from `i-j` for some `j in J`.
`dp[i] = sum_j in J dp[i-j]`.
Base case: `dp[0] = 1`.

## Naive Approach

### Intuition

Recursion with memoization.

### Algorithm


### Time Complexity

- **O(n \cdot |J|)**.
- With `n=10^5, |J|=20`, ops `~= 2 * 10^6`. Fast enough.

### Space Complexity

- **O(n)** for recursion stack/memo.

## Optimal Approach

### Key Insight

Iterative DP is cleaner and avoids recursion depth limits.
Since `n` is up to `10^5`, `O(n * |J|)` is perfectly acceptable.
If `n` were huge (`10^18`), we would use Matrix Exponentiation, but here simple DP suffices.

### Algorithm

1. Init `dp` array of size `n+1` with 0.
2. `dp[0] = 1`.
3. Iterate `i` from 1 to `n`:
   - For each jump `j` in `J`:
     - If `i >= j`: `dp[i] = (dp[i] + dp[i-j]) % MOD`.
4. Return `dp[n]`.

### Time Complexity

- **O(n \cdot m)**.

### Space Complexity

- **O(n)**.

![Algorithm Visualization](../images/NUM-011/algorithm-visualization.png)
![Algorithm Steps](../images/NUM-011/algorithm-steps.png)

## Implementations

### Java
```java
import java.util.*;

class Solution {
    static final int MOD = 1000000007;

    public int countWays(int n, int[] jumps) {
        int[] dp = new int[n + 1];
        dp[0] = 1;
        
        for (int i = 1; i <= n; i++) {
            for (int jump : jumps) {
                if (i >= jump) {
                    dp[i] = (dp[i] + dp[i - jump]) % MOD;
                }
            }
        }
        
        return dp[n];
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int m = sc.nextInt();
            int[] jumps = new int[m];
            for (int i = 0; i < m; i++) jumps[i] = sc.nextInt();

            Solution solution = new Solution();
            System.out.println(solution.countWays(n, jumps));
        }
        sc.close();
    }
}
```

### Python
```python
import sys

def count_ways(n: int, jumps):
    MOD = 1000000007
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for i in range(1, n + 1):
        for jump in jumps:
            if i >= jump:
                dp[i] = (dp[i] + dp[i - jump]) % MOD
                
    return dp[n]

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    jumps = [int(x) for x in data[2:]]
    print(count_ways(n, jumps))

if __name__ == "__main__":
    main()
```

### C++
```cpp
#include <iostream>
#include <vector>

using namespace std;

class Solution {
    const int MOD = 1000000007;
public:
    int countWays(int n, const vector<int>& jumps) {
        vector<int> dp(n + 1, 0);
        dp[0] = 1;
        
        for (int i = 1; i <= n; i++) {
            for (int jump : jumps) {
                if (i >= jump) {
                    dp[i] = (dp[i] + dp[i - jump]) % MOD;
                }
            }
        }
        
        return dp[n];
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (cin >> n >> m) {
        vector<int> jumps(m);
        for (int i = 0; i < m; i++) cin >> jumps[i];

        Solution solution;
        cout << solution.countWays(n, jumps) << "\n";
    }
    return 0;
}
```

### JavaScript
```javascript
const readline = require("readline");

function countWays(n, jumps) {
  const MOD = 1000000007;
  const dp = new Int32Array(n + 1);
  dp[0] = 1;
  
  for (let i = 1; i <= n; i++) {
    for (const jump of jumps) {
      if (i >= jump) {
        dp[i] = (dp[i] + dp[i - jump]) % MOD;
      }
    }
  }
  
  return dp[n];
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
  const m = parseInt(data[idx++], 10);
  const jumps = [];
  for (let i = 0; i < m; i++) jumps.push(parseInt(data[idx++], 10));
  console.log(countWays(n, jumps));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

Input: `n=4, jumps=[1, 3]`.
1. `dp` size 5. `dp[0]=1`.
2. `i=1`: `dp[1] += dp[0]` (jump 1) -> `1`.
3. `i=2`: `dp[2] += dp[1]` (jump 1) -> `1`.
4. `i=3`:
   - `dp[3] += dp[2]` (jump 1) -> `1`.
   - `dp[3] += dp[0]` (jump 3) -> `1+1=2`.
5. `i=4`:
   - `dp[4] += dp[3]` (jump 1) -> `2`.
   - `dp[4] += dp[1]` (jump 3) -> `2+1=3`.
Result: 3.

## ✅ Proof of Correctness

### Invariant
`dp[i]` correctly sums the ways to reach `i` from all possible previous steps `i-j`.
This covers all valid last moves.

### Why the approach is correct
Standard DP for counting paths in DAGs.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** `N <= 10^18`.
  - *Hint:* Matrix Exponentiation. Construct a transition matrix of size `max(J) x max(J)`.
- **Extension 2:** Minimize number of jumps.
  - *Hint:* BFS or DP with `min` instead of sum.
- **Extension 3:** Forbidden steps.
  - *Hint:* Set `dp[forbidden] = 0` and never update from it.

### Common Mistakes to Avoid

1. **Modulo Arithmetic**
   - ❌ Wrong: Forgetting modulo on addition.
   - ✅ Correct: `(a + b) % MOD`.
2. **Index Out of Bounds**
   - ❌ Wrong: Accessing `dp[i-jump]` when `i < jump`.
   - ✅ Correct: Check `i >= jump`.

## Related Concepts

- **Fibonacci Sequence:** Case where `J=1, 2`.
- **Coin Change Problem:** Similar structure (but usually order doesn't matter there; here it does).
