---
problem_id: GMT_COIN_SPLIT__4721
display_id: GMT-014
slug: greedy-coin-split-game
title: "Greedy Coin Split Game"
difficulty: Medium
difficulty_score: 65
topics:
  - Game Theory
  - Dynamic Programming
tags:
  - minimax
  - memoization
  - interval-dp
premium: true
subscription_tier: basic
---

# GMT-014: Greedy Coin Split Game

## 📋 Problem Summary

Split array into two. Opponent keeps one part. Repeat on remainder. Maximize Diff.

## 🌍 Real-World Scenario

**Scenario Title:** The Estate Division.

Two heirs are dividing a linear estate (coastline properties).
- One heir draws a line to split the estate.
- The other heir chooses which side to take immediately.
- The remaining side is then split by the second heir, and the first chooses.
- This continues until the land is too small to split.

![Real-World Application](../images/GMT-014/real-world-scenario.png)

## Detailed Explanation

### State Representation

`dp[i][j]` represents the maximum score difference `(Splitter - Chooser)` obtainable from the subarray `A[i...j]`.

### Transitions

For a subarray `A[i...j]`, the Splitter can split at any index `k` (`i <= k < j`).
This creates `Left = A[i...k]` and `Right = A[k+1...j]`.

The Chooser has two options:
1.  **Take Left:**
    - Chooser gets `Sum(Left)`.
    - Game continues on `Right` with Chooser becoming Splitter.
    - Future outcome from `Right` is `dp[k+1][j]` (which is `NewSplitter - NewChooser`).
    - Since current Chooser becomes New Splitter, `dp[k+1][j]` represents `Chooser - Splitter` relative to current roles.
    - So Chooser's total advantage = `Sum(Left) + dp[k+1][j]`.
    - Splitter's advantage = `- (Sum(Left) + dp[k+1][j])`.

2.  **Take Right:**
    - Chooser gets `Sum(Right)`.
    - Game continues on `Left`.
    - Chooser's total advantage = `Sum(Right) + dp[i][k]`.
    - Splitter's advantage = `- (Sum(Right) + dp[i][k])`.

The Chooser will choose the option that maximizes their advantage (minimizes Splitter's advantage).
So for a fixed split `k`, the outcome is:
`Outcome(k) = min( -Sum(Left) - dp[k+1][j], -Sum(Right) - dp[i][k] )`.

The Splitter will choose `k` to maximize this outcome:
`dp[i][j] = max_{k} ( Outcome(k) )`.

### Base Case

- If `i == j` (single element), no split is possible.
- The coin is discarded.
- `dp[i][i] = 0`.

### Complexity

- **States:** `N^2`.
- **Transitions:** `O(N)`.
- **Total:** `O(N^3)`.
- With `N=100`, `10^6` operations. Fast.

![Algorithm Visualization](../images/GMT-014/algorithm-visualization.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    private int[][] dp;
    private int[] prefixSum;
    private boolean[][] visited;

    private int getSum(int i, int j) {
        return prefixSum[j + 1] - prefixSum[i];
    }

    private int solve(int i, int j) {
        if (i == j) return 0;
        if (visited[i][j]) return dp[i][j];

        int maxDiff = Integer.MIN_VALUE;

        for (int k = i; k < j; k++) {
            // Split into [i...k] and [k+1...j]
            int sumLeft = getSum(i, k);
            int sumRight = getSum(k + 1, j);

            // If Chooser takes Left: Splitter gets -(sumLeft + solve(k+1, j))
            int valTakeLeft = -sumLeft - solve(k + 1, j);
            
            // If Chooser takes Right: Splitter gets -(sumRight + solve(i, k))
            int valTakeRight = -sumRight - solve(i, k);

            // Chooser minimizes Splitter's gain
            int outcome = Math.min(valTakeLeft, valTakeRight);
            maxDiff = Math.max(maxDiff, outcome);
        }

        visited[i][j] = true;
        dp[i][j] = maxDiff;
        return maxDiff;
    }

    public int coinSplit(int n, int[] A) {
        dp = new int[n][n];
        visited = new boolean[n][n];
        prefixSum = new int[n + 1];
        for (int i = 0; i < n; i++) prefixSum[i + 1] = prefixSum[i] + A[i];

        return solve(0, n - 1);
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int[] A = new int[n];
            for (int i = 0; i < n; i++) {
                A[i] = sc.nextInt();
            }

            Solution solution = new Solution();
            System.out.println(solution.coinSplit(n, A));
        }
        sc.close();
    }
}
```

### Python

```python
from typing import List
import sys

# Increase recursion depth
sys.setrecursionlimit(20000)

def coin_split(n: int, A: List[int]) -> int:
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i+1] = prefix_sum[i] + A[i]
    
    def get_sum(i, j):
        return prefix_sum[j+1] - prefix_sum[i]
    
    memo = {}

    def solve(i, j):
        if i == j:
            return 0
        state = (i, j)
        if state in memo:
            return memo[state]
        
        max_diff = -float('inf')
        
        for k in range(i, j):
            # Split [i...k] and [k+1...j]
            sum_left = get_sum(i, k)
            sum_right = get_sum(k+1, j)
            
            val_take_left = -sum_left - solve(k+1, j)
            val_take_right = -sum_right - solve(i, k)
            
            outcome = min(val_take_left, val_take_right)
            max_diff = max(max_diff, outcome)
            
        memo[state] = max_diff
        return max_diff

    return solve(0, n - 1)

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        A = []
        for _ in range(n):
            A.append(int(next(iterator)))
            
        print(coin_split(n, A))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>
#include <climits>

using namespace std;

class Solution {
    int dp[105][105];
    bool visited[105][105];
    vector<int> prefixSum;

    int getSum(int i, int j) {
        return prefixSum[j + 1] - prefixSum[i];
    }

    int solve(int i, int j) {
        if (i == j) return 0;
        if (visited[i][j]) return dp[i][j];

        int maxDiff = INT_MIN;

        for (int k = i; k < j; k++) {
            int sumLeft = getSum(i, k);
            int sumRight = getSum(k + 1, j);

            int valTakeLeft = -sumLeft - solve(k + 1, j);
            int valTakeRight = -sumRight - solve(i, k);

            int outcome = min(valTakeLeft, valTakeRight);
            maxDiff = max(maxDiff, outcome);
        }

        visited[i][j] = true;
        return dp[i][j] = maxDiff;
    }

public:
    int coinSplit(int n, vector<int>& A) {
        prefixSum.assign(n + 1, 0);
        for (int i = 0; i < n; i++) prefixSum[i + 1] = prefixSum[i] + A[i];
        
        for(int i=0; i<n; ++i)
            for(int j=0; j<n; ++j)
                visited[i][j] = false;

        return solve(0, n - 1);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    if (cin >> n) {
        vector<int> A(n);
        for (int i = 0; i < n; i++) {
            cin >> A[i];
        }
        
        Solution solution;
        cout << solution.coinSplit(n, A) << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  coinSplit(n, A) {
    const prefixSum = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) prefixSum[i + 1] = prefixSum[i] + A[i];

    const getSum = (i, j) => prefixSum[j + 1] - prefixSum[i];
    const memo = new Map();

    const solve = (i, j) => {
      if (i === j) return 0;
      const key = `${i},${j}`;
      if (memo.has(key)) return memo.get(key);

      let maxDiff = -Infinity;

      for (let k = i; k < j; k++) {
        const sumLeft = getSum(i, k);
        const sumRight = getSum(k + 1, j);

        const valTakeLeft = -sumLeft - solve(k + 1, j);
        const valTakeRight = -sumRight - solve(i, k);

        const outcome = Math.min(valTakeLeft, valTakeRight);
        maxDiff = Math.max(maxDiff, outcome);
      }

      memo.set(key, maxDiff);
      return maxDiff;
    };

    return solve(0, n - 1);
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  if (data.length === 0) return;
  
  const flatData = [];
  data.forEach(line => {
      line.trim().split(/\s+/).forEach(part => {
          if (part) flatData.push(part);
      });
  });
  
  if (flatData.length === 0) return;
  
  let idx = 0;
  const n = parseInt(flatData[idx++]);
  
  const A = [];
  for (let i = 0; i < n; i++) {
      A.push(parseInt(flatData[idx++]));
  }

  const solution = new Solution();
  console.log(solution.coinSplit(n, A));
});
```

## 🧪 Test Case Walkthrough

**Input:** `[10, 20, 30]`
- `f(20, 30) = 30`. (Split 20|30. P2 takes 20 -> P1 gets 30).
- `f(10, 20) = 20`.
- `f(10, 20, 30)`:
  - Split `10 | 20, 30`: `min(-10 - 30, -50 - 0) = min(-40, -50) = -50`.
  - Split `10, 20 | 30`: `min(-30 - 20, -30 - 0) = min(-50, -30) = -50`.
- Wait, my manual trace in editorial text has errors.
- Let's re-verify `f(20, 30)`.
  - Split `20 | 30`.
  - Take `20`: Splitter gets `-20 - f(30,30) = -20`.
  - Take `30`: Splitter gets `-30 - f(20,20) = -30`.
  - Chooser minimizes -> `-30`.
  - So `f(20, 30) = -30`.
- Ah! `f` is `Splitter - Chooser`.
- If `f(20, 30) = -30`, it means Chooser wins by 30.
- `f(10, 20) = -20`.
- `f(10, 20, 30)`:
  - Split `10 | 20, 30`:
    - Take `10`: `-10 - (-30) = 20`.
    - Take `20, 30`: `-50 - 0 = -50`.
    - Min: `-50`.
  - Split `10, 20 | 30`:
    - Take `30`: `-30 - (-20) = -10`.
    - Take `10, 20`: `-30 - 0 = -30`.
    - Min: `-30`.
- Max of `-50` and `-30` is `-30`.
- Correct result is `-30`.

## ✅ Proof of Correctness

- **DP State:** Captures full game state (subarray).
- **Minimax:** Correctly models adversarial play.
- **Base Case:** Correctly handles termination.

## 💡 Interview Extensions

- **Extension 1:** What if we can split into K parts?
  - *Answer:* Loop over K-1 split points.
- **Extension 2:** What if we want to maximize Sum?
  - *Answer:* Change recurrence to return `(MyScore, OppScore)`.

## Common Mistakes

1.  **Sign Error:**
    - ❌ Wrong: `sumLeft + solve(...)`.
    - ✅ Correct: `-sumLeft - solve(...)` because roles swap.
2.  **Base Case:**
    - ❌ Wrong: `return A[i]`.
    - ✅ Correct: `return 0` (discarded).

## Related Concepts

- **Interval DP**
- **Game Theory**
