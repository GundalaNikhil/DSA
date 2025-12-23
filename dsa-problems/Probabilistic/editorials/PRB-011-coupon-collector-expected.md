---
problem_id: PRB_COUPON_COLLECTOR_EXPECTED__1148
display_id: PRB-011
slug: coupon-collector-expected
title: "Coupon Collector Expected Trials"
difficulty: Medium
difficulty_score: 40
topics:
  - Probability
  - Expected Value
  - Harmonic Numbers
tags:
  - probability
  - expectation
  - harmonic
  - medium
premium: true
subscription_tier: basic
---

# PRB-011: Coupon Collector Expected Trials

## 📋 Problem Summary

Calculate the expected number of trials to collect all N distinct coupons, assuming each trial yields a coupon uniformly at random with replacement.

| | |
|---|---|
| **Formula** | E = N × Σ(1/i) for i=1 to N |
| **Input** | N |
| **Output** | Expected trials (float) |

## 🌍 Real-World Scenario

**Scenario Title:** The Complete Sticker Album

You are collecting a set of N stickers for a World Cup album.

- You buy packets of stickers one by one.
- Each packet contains one random sticker.
- At first, it's easy to find new stickers.
- As you near completion, it becomes increasingly difficult to find the specific missing ones (you keep getting duplicates).
- You want to estimate the total number of packets you need to buy to complete the entire album.

**Why This Problem Matters:**

- **Cybersecurity:** Time to brute-force a set of keys or IDs.
- **Ecology:** Estimating species richness based on observed samples.
- **Software Testing:** How many random tests needed to cover all code paths.

![Real-World Application](../images/PRB-011/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Collection Process

N = 3$ stickers: A, B, C. Let's trace the collection journey:

```
┌──────────────────────────────────────────────────────────┐
│ Stage 1: Finding First Sticker                          │
│ Missing: {A, B, C}                                       │
│ Probability of new: 3/3 = 1.0 (100%)                   │
│ Expected draws: 1/(3/3) = 1.0                           │
│                                                          │
│ Progress: [█████████████████████] 100% chance           │
│           Got 'A' ✓                                      │
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│ Stage 2: Finding Second Sticker                         │
│ Have: {A}    Missing: {B, C}                           │
│ Probability of new: 2/3 ≈ 0.667 (67%)                  │
│ Expected draws: 1/(2/3) = 3/2 = 1.5                     │
│                                                          │
│ Progress: [█████████████      ] 67% chance              │
│           Got 'B' ✓   (took ~1.5 tries on average)      │
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│ Stage 3: Finding Third Sticker                          │
│ Have: {A, B}    Missing: {C}                           │
│ Probability of new: 1/3 ≈ 0.333 (33%)                  │
│ Expected draws: 1/(1/3) = 3.0                           │
│                                                          │
│ Progress: [██████        ] 33% chance                   │
│           Got 'C' ✓   (took ~3 tries on average)        │
└──────────────────────────────────────────────────────────┘

Total Expected Draws = 1.0 + 1.5 + 3.0 = 5.5 ✓
```

### Difficulty Progression Visualization

As you get closer to completion, finding new items becomes exponentially harder:

```
Difficulty Chart (N=5):
                                               ╱╲
Stage 5 (Last Item)   ████████████████████    ╱  ╲  5.0 draws
      20% new        (Very Hard!)            ╱    ╲
                                            │      │
Stage 4              ████████████████      ╱        ╲  2.5 draws
      40% new        (Hard)               │          │
                                         ╱            ╲
Stage 3              ████████████       │              │ 1.67 draws
      60% new        (Medium)          ╱                ╲
                                      │                  │
Stage 2              ████████        │                    │ 1.25 draws
      80% new        (Easy)         ╱                      ╲
                                   │                        │
Stage 1              ████         │                          │ 1.0 draw
      100% new       (Trivial)   └────────────────────────────┘

Time →               [════════════════════════════════════════>]
                     Fast          ←→        Slooooow
```

### Real Collection Simulation

Example run collecting 5 items:

```
Draw #  │ Got  │ Collection Status        │ New? │ Stage
────────┼──────┼──────────────────────────┼──────┼────────
   1    │  C   │ {C}                      │  ✓   │ 1/5
   2    │  A   │ {A, C}                   │  ✓   │ 2/5
   3    │  C   │ {A, C}                   │  ✗   │ Still 2/5
   4    │  E   │ {A, C, E}                │  ✓   │ 3/5
   5    │  A   │ {A, C, E}                │  ✗   │ Still 3/5
   6    │  D   │ {A, C, D, E}             │  ✓   │ 4/5
   7    │  C   │ {A, C, D, E}             │  ✗   │ Still 4/5
   8    │  A   │ {A, C, D, E}             │  ✗   │ Still 4/5
   9    │  E   │ {A, C, D, E}             │  ✗   │ Still 4/5
   10   │  D   │ {A, C, D, E}             │  ✗   │ Still 4/5
   11   │  B   │ {A, B, C, D, E}          │  ✓   │ DONE!

Actual draws: 11   Expected: N×H₅ = 5×(1+½+⅓+¼+⅕) ≈ 11.42
```

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Formula:** E = N H_N = N (1 + 1/2 + \dots + 1/N)$.
- **Constraints:** N \le 10^6$. O(N) loop is acceptable.
- **Precision:** Use `double`.

### Core Concept: Geometric Distribution

Let X_i be the number of draws to find the i-th distinct coupon after finding i-1.
The probability of success for X_i is `p_i = fracN - (i-1)N`.
X_i follows a Geometric distribution with mean `1/p_i = fracNN-i+1`.
Total Expectation E = \sum E[X_i] = \sum \frac{N}{N-i+1} = N \sum \frac{1}{k}$.

## Naive Approach

### Intuition

Simulate the process.

### Algorithm

Monte Carlo.

### Time Complexity

- **O(Trials \cdot N \log N)**. Too slow.

## Optimal Approach

### Key Insight

Compute the harmonic sum directly.

### Algorithm

1. Initialize `sum = 0.0`.
2. Loop `i` from 1 to `N`: `sum += 1.0 / i`.
3. Return `N * sum`.

### Time Complexity

- **O(N)**.

### Space Complexity

- **O(1)**.

![Algorithm Visualization](../images/PRB-011/algorithm-visualization.png)
![Algorithm Steps](../images/PRB-011/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public double expectedDraws(int N) {
        double harmonicSum = 0.0;
        for (int i = 1; i <= N; i++) {
            harmonicSum += 1.0 / i;
        }
        return N * harmonicSum;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int N = sc.nextInt();
            Solution solution = new Solution();
            System.out.printf("%.6f\n", solution.expectedDraws(N));
        }
        sc.close();
    }
}
```

### Python

```python
import sys

def expected_draws(N: int) -> float:
    harmonic_sum = 0.0
    for i in range(1, N + 1):
        harmonic_sum += 1.0 / i
    return N * harmonic_sum

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    N = int(data[0])
    print(f"{expected_draws(N):.6f}")

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
    double expectedDraws(int N) {
        double harmonicSum = 0.0;
        for (int i = 1; i <= N; i++) {
            harmonicSum += 1.0 / i;
        }
        return N * harmonicSum;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    if (cin >> N) {
        Solution solution;
        cout << fixed << setprecision(6) << solution.expectedDraws(N) << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function expectedDraws(N) {
  let harmonicSum = 0.0;
  for (let i = 1; i <= N; i++) {
    harmonicSum += 1.0 / i;
  }
  return N * harmonicSum;
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  if (data.length === 0) return;
  const N = parseInt(data[0], 10);
  console.log(expectedDraws(N).toFixed(6));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

Input: `3`.

1. `sum = 1 + 0.5 + 0.3333 = 1.8333`.
2. `3 * 1.8333 = 5.5`.
   Matches example.

## ✅ Proof of Correctness

### Invariant

The sum of expectations of geometric random variables.

### Why the approach is correct

Linearity of expectation allows summing the expected time for each phase.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Variance.
  - _Hint:_ Sum of variances of geometric distributions (`N^2 sum 1/i^2`).
- **Extension 2:** Collecting k sets of coupons.
  - _Hint:_ N \ln N + (k-1) N \ln \ln N$.
- **Extension 3:** Unequal probabilities.
  - _Hint:_ Much harder, uses inclusion-exclusion or integrals.

### Common Mistakes to Avoid

1. **Integer Division**
   - ❌ Wrong: `1/i`.
   - ✅ Correct: `1.0/i`.
2. **Approximation**
   - ❌ Wrong: Using N \ln N$ for small N.
   - ✅ Correct: Exact sum is better for N \le 10^6$.

## Related Concepts

- **Birthday Paradox:** Collision probability vs Coverage time.
- **Cover Time:** Random walk covering a graph.
