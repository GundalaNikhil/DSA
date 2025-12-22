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
---

# PRB-001: Coin Flip Streak Probability

## 📋 Problem Summary

Calculate the probability that in a sequence of n fair coin flips, there is at least one streak of k consecutive heads.

|            |                     |
| ---------- | ------------------- |
| **Input**  | Integers n and k    |
| **Output** | Probability (float) |

## 🌍 Real-World Scenario

**Scenario Title:** The Server Uptime Guarantee

You are a reliability engineer for a cloud service. Your servers have a small chance of failing every minute.

- A "failure streak" of k consecutive minutes causes a system-wide outage.
- You want to calculate the probability that the system will crash within a given time window of n minutes.
- This helps in defining Service Level Agreements (SLAs) and deciding whether to invest in better hardware redundancy.

**Why This Problem Matters:**

- **Reliability Engineering:** Estimating failure rates in systems.
- **Finance:** Analyzing streaks of market gains or losses.
- **Genomics:** Finding specific DNA motifs (sequences of nucleotides).

![Real-World Application](../images/PRB-001/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Streak Analysis

For n=3, k=2, we enumerate all 2³ = 8 possible sequences:

```
HHH -> Contains substring "HH" (YES) ✓
HHT -> Contains substring "HH" (YES) ✓
HTH -> Max streak 1 (NO)
HTT -> Max streak 1 (NO)
THH -> Contains substring "HH" (YES) ✓
THT -> Max streak 1 (NO)
TTH -> Max streak 1 (NO)
TTT -> Max streak 0 (NO)
```

**Successes:** HHH, HHT, THH → 3 out of 8 sequences
**Probability:** 3/8 = 0.375

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Constraints:** N ≤ 60, K ≤ N. O(N) solution required.
- **Precision:** Float output with error tolerance ≤ 10⁻⁶.
- **Interpretation:** "At least one streak of k consecutive heads" means the pattern H^k (k heads in a row) appears as a substring anywhere in the sequence.

### Core Concept: Complement DP

It is easier to calculate the probability of **NOT** having any streak of k heads, and subtract from 1.

Let dp[i] = number of sequences of length i with **NO** streak of k consecutive heads.

**Recurrence Logic:**

- A valid sequence of length i can be formed by appending H or T to any valid sequence of length i-1
- This gives us 2 · dp[i-1] total sequences
- However, some of these create a forbidden streak of exactly k heads
- Specifically, sequences that end with TH^k (one tail followed by k heads) must be subtracted
- The number of such sequences equals dp[i-k-1] (valid sequences we extend with TH^k)

**Formula:**
dp[i] = 2 \cdot dp[i-1] - dp[i-k-1]

**Base Cases:**

- dp[i] = 2^i for 0 ≤ i < k (all sequences are valid if length < k)
- dp[k] = 2^k - 1 (all sequences except H^k)

**Final Answer:**
P(at least one streak) = 1 - dp[n] / 2^n

### Visual Example: Building dp Array for n=3, k=2

```
Position:  0    1    2    3
         ┌────┬────┬────┬────┐
   dp[] │ 1  │ 2  │ 3  │ 5  │
         └────┴────┴────┴────┘
          ↑    ↑    ↑    ↑
          │    │    │    └─── 2×3 - 1 = 5 sequences (no HH)
          │    │    └──────── 2^2 - 1 = 3 sequences (no HH)
          │    └───────────── 2^1 = 2 sequences (H, T)
          └────────────────── 2^0 = 1 sequence (empty)

Valid sequences of length 3 (no HH):
  HTH, HTT, THT, TTH, TTT = 5 sequences ✓

Invalid sequences (contain HH):
  HHH, HHT, THH = 3 sequences

Probability = 1 - 5/8 = 3/8 = 0.375 ✓
```

## Naive Approach

### Intuition

Generate all 2^n sequences, check each for a streak of k consecutive heads.

### Algorithm

1. Generate all 2^n bit sequences
2. For each sequence, scan for k consecutive 1s (heads)
3. Count valid sequences

### Time Complexity

- **O(2^n · n)**. Too slow for N=60.

### Space Complexity

- **O(n)**.

### Limitations

Exponential time complexity makes this infeasible for large n.

## Optimal Approach

### Key Insight

Use **Complement DP**: Calculate the probability of NOT having any streak of k heads, then subtract from 1.

Let dp[i] be the number of sequences of length i with **NO** streak of k consecutive heads.

**Recurrence Logic:**

- When we extend a valid sequence of length i-1 by adding one more flip, we get 2 · dp[i-1] possibilities
- However, some of these create a forbidden streak of k heads
- Specifically, if we had a valid sequence ending in T H^(k-1) (tail followed by k-1 heads), and we append H, we create T H^k
- The number of such problematic sequences is dp[i-k-1] (valid sequences of length i-k-1, to which we append T H^k)

**Formula:**
dp[i] = 2 \cdot dp[i-1] - dp[i-k-1]


**Base cases:**

- dp[i] = 2^i for 0 ≤ i < k (all sequences valid if length < k)
- dp[k] = 2^k - 1 (all sequences except H^k)
- dp[i] = 2 · dp[i-1] - dp[i-k-1] for i > k

**Final Answer:**
P(at least one streak) = 1 - dp[n] / 2^n

### Algorithm

1. Initialize `dp` array of size n+1
2. Set base cases: `dp[i] = 2^i` for i < k
3. Set `dp[k] = 2^k - 1`
4. For i from k+1 to n: `dp[i] = 2*dp[i-1] - dp[i-k-1]`
5. Return 1 - dp[n] / 2^n

### Time Complexity

- **O(n)**.

### Space Complexity

- **O(n)**.

### Why This Is Optimal

Linear time is optimal since we must output a result that depends on all n positions.

![Algorithm Visualization](../images/PRB-001/algorithm-visualization.png)
![Algorithm Steps](../images/PRB-001/algorithm-steps.png)

## Implementations

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public double streakProbability(int n, int k) {
        if (k > n) return 0.0;

        // dp[i] = number of sequences of length i with NO streak of k heads
        long[] dp = new long[n + 1];

        // Base cases
        for (int i = 0; i < k; i++) {
            dp[i] = 1L << i; // 2^i
        }
        dp[k] = (1L << k) - 1; // 2^k - 1 (exclude H...H)

        for (int i = k + 1; i <= n; i++) {
            // dp[i] = 2 * dp[i-1] - dp[i-k-1]
            // We subtract cases ending in T H...H (k times)
            // The prefix must be valid of length i - (k+1)
            dp[i] = 2 * dp[i - 1] - dp[i - k - 1];
        }

        long total = 1L << n;
        long valid = dp[n];
        return 1.0 - (double)valid / total;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int k = sc.nextInt();
            Solution solution = new Solution();
            System.out.println(solution.streakProbability(n, k));
        }
        sc.close();
    }
}
```

### Python

```python
import sys

def streak_probability(n: int, k: int) -> float:
    if k > n:
        return 0.0

    # dp[i] = number of sequences of length i with NO streak of k heads
    dp = [0] * (n + 1)

    for i in range(k):
        dp[i] = 1 << i

    dp[k] = (1 << k) - 1

    for i in range(k + 1, n + 1):
        dp[i] = 2 * dp[i - 1] - dp[i - k - 1]

    total = 1 << n
    valid = dp[n]
    return 1.0 - valid / total

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    k = int(data[1])
    print(streak_probability(n, k))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

class Solution {
public:
    double streakProbability(int n, int k) {
        if (k > n) return 0.0;

        // Use long long for counts. 2^60 fits in long long (signed is up to 2^63-1).
        vector<long long> dp(n + 1);

        for (int i = 0; i < k; i++) {
            dp[i] = 1LL << i;
        }
        dp[k] = (1LL << k) - 1;

        for (int i = k + 1; i <= n; i++) {
            dp[i] = 2 * dp[i - 1] - dp[i - k - 1];
        }

        long long total = 1LL << n;
        return 1.0 - (double)dp[n] / total;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (cin >> n >> k) {
        Solution solution;
        cout << solution.streakProbability(n, k) << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function streakProbability(n, k) {
  if (k > n) return 0.0;

  // Use BigInt because 2^60 exceeds Number.MAX_SAFE_INTEGER
  const dp = new Array(n + 1).fill(0n);

  for (let i = 0; i < k; i++) {
    dp[i] = 1n << BigInt(i);
  }
  dp[k] = (1n << BigInt(k)) - 1n;

  for (let i = k + 1; i <= n; i++) {
    dp[i] = 2n * dp[i - 1] - dp[i - k - 1];
  }

  const total = 1n << BigInt(n);
  const valid = dp[n];

  // Convert to double for division
  // Since we need probability, we can do Number(total - valid) / Number(total)
  // But total might be huge.
  // Better: 1.0 - Number(valid) / Number(total)
  // But valid and total are huge.
  // We can compute 1 - (valid/total).
  // BigInt division truncates.
  // Convert to string and parse? Or scale?
  // Number() works up to 2^1024, but loses precision after 2^53.
  // For probability, standard double precision is fine.

  const v = Number(valid);
  const t = Number(total);
  return 1.0 - v / t;
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
  console.log(streakProbability(n, k));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

Input: `3 2`.

1. `dp` size 4.
2. `dp[0] = 1`.
3. `dp[1] = 2` (H, T).
4. `dp[2] = 3` (HT, TH, TT). (Exclude HH).
5. `dp[3] = 2*dp[2] - dp[0] = 2*3 - 1 = 5`.
   - Valid sequences without HH: HTH, HTT, THT, TTH, TTT (5 total)
   - Sequences with HH: HHT, HHH, THH (3 total)
   - Verification: 5 + 3 = 8 ✓
6. Total 2³ = 8.
7. Prob = 1 - 5/8 = 3/8 = 0.375.

## ✅ Proof of Correctness

### Invariant

`dp[i]` counts sequences of length `i` without H^k.
The recurrence subtracts exactly those sequences that form H^k at the very end.

### Why the approach is correct

Complement counting is standard for "at least one" probabilities.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Biased coin (P(H) = p).
  - _Hint:_ Use probabilities instead of counts. dp[i] = dp[i-1] - dp[i-k-1] · (1-p) · p^k.
- **Extension 2:** Expected number of flips to get streak k.
  - _Hint:_ E = 2^(k+1) - 2 (for p=0.5).
- **Extension 3:** Streak of Heads OR Tails.
  - _Hint:_ Similar DP, just more states.

## Common Mistakes to Avoid

1. **Precision**
   - ❌ Wrong: Using `int` for counts (overflows at N=31).
   - ✅ Correct: Use `long long` or `BigInt`.
2. **Base Cases**
   - ❌ Wrong: `dp[k] = 2^k`.
   - ✅ Correct: `dp[k] = 2^k - 1`.

## Related Concepts

- **Markov Chains:** Can model this as states 0, 1, ..., k heads.
- **Fibonacci:** k=2 gives Fibonacci-like recurrence.
