---
problem_id: NUM_COUNT_SURJECTIVE_FUNCTIONS__7773
display_id: NUM-016
slug: count-surjective-functions
title: "Count Surjective Functions"
difficulty: Medium
difficulty_score: 55
topics:
  - Number Theory
  - Combinatorics
  - Inclusion-Exclusion
tags:
  - number-theory
  - combinatorics
  - inclusion-exclusion
  - medium
premium: true
subscription_tier: basic
---

# NUM-016: Count Surjective Functions

## 📋 Problem Summary

Count the number of surjective (onto) functions from a set of size `n` to a set of size `k`.
- A function is surjective if every element in the codomain is mapped to by at least one element in the domain.
- Input: `n, k`.
- Output: Count modulo `10^9+7`.

## 🌍 Real-World Scenario

**Scenario Title:** The Team Assignment

You are a project manager with `n` distinct tasks and `k` distinct team members.
- You need to assign every task to a team member.
- However, to ensure fairness and engagement, **every team member must be assigned at least one task**.
- You want to calculate the number of valid assignment configurations to understand the flexibility of your resource allocation.

**Why This Problem Matters:**

- **Combinatorics:** Stirling numbers of the second kind (`S(n, k) x k!`).
- **Network Design:** Routing packets such that all channels are utilized.
- **Testing:** Generating test cases that cover all features.

![Real-World Application](../images/NUM-016/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Mapping

`n=3` Tasks (T1, T2, T3), `k=2` Members (M1, M2).

Valid Assignments (Surjective):
1. T1->M1, T2->M1, T3->M2 (M1 has 2, M2 has 1)
2. T1->M1, T2->M2, T3->M1
3. T1->M2, T2->M1, T3->M1
4. T1->M2, T2->M2, T3->M1 (M1 has 1, M2 has 2)
5. T1->M2, T2->M1, T3->M2
6. T1->M1, T2->M2, T3->M2

Invalid (Not Surjective):
- All to M1 (M2 has 0)
- All to M2 (M1 has 0)

Total Functions: `2^3 = 8`.
Invalid: 2.
Valid: `8 - 2 = 6`.

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Constraints:** `n, k <= 30`. Small enough for simple iteration, but logic works for larger.
- **Modulo:** `10^9+7`.
- **Formula:** `k! * S(n, k)`, where `S(n, k)` is Stirling number of second kind.
- **Inclusion-Exclusion:** `sum_i=0^k (-1)^i binomki (k-i)^n`.

### Core Concept: Inclusion-Exclusion Principle

Total functions without restriction: `k^n`.
Subtract functions that miss at least 1 element: `binomk1 (k-1)^n`.
Add back functions that miss at least 2 elements: `binomk2 (k-2)^n`.
...
General term: `(-1)^i binomki (k-i)^n`.

## Naive Approach

### Intuition

Iterate all `k^n` functions and check surjectivity.

### Algorithm

Recursion depth `n`.

### Time Complexity

- **O(k^n)**. Too slow for `n=30`.

## Optimal Approach

### Key Insight

Use the Inclusion-Exclusion formula directly.
Since `k <= 30`, we can compute binomial coefficients easily.

### Algorithm

1. Initialize `ans = 0`.
2. Precompute combinations `binomki`.
3. Loop `i` from 0 to `k`:
   - Term: `binomki x (k-i)^n`.
   - If `i` is odd, subtract term.
   - If `i` is even, add term.
   - Handle modulo carefully (add MOD before modulo for subtraction).
4. Return `ans`.

### Time Complexity

- **O(k \log n)** or **O(k^2)** depending on implementation of power/nCr.
- With `k=30`, extremely fast.

### Space Complexity

- **O(k)**.

![Algorithm Visualization](../images/NUM-016/algorithm-visualization.png)
![Algorithm Steps](../images/NUM-016/algorithm-steps.png)

## Implementations

### Java
```java
import java.util.*;

class Solution {
    static final int MOD = 1000000007;

    private long power(long base, long exp) {
        long res = 1;
        base %= MOD;
        while (exp > 0) {
            if ((exp & 1) == 1) res = (res * base) % MOD;
            base = (base * base) % MOD;
            exp >>= 1;
        }
        return res;
    }

    public long countSurjections(int n, int k) {
        if (k > n) return 0;
        
        long ans = 0;
        long[][] C = new long[k + 1][k + 1];
        
        // Compute Binomial Coefficients
        for (int i = 0; i <= k; i++) {
            C[i][0] = 1;
            for (int j = 1; j <= i; j++) {
                C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD;
            }
        }
        
        for (int i = 0; i <= k; i++) {
            long term = (C[k][i] * power(k - i, n)) % MOD;
            if (i % 2 == 1) {
                ans = (ans - term + MOD) % MOD;
            } else {
                ans = (ans + term) % MOD;
            }
        }
        
        return ans;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int k = sc.nextInt();
            Solution solution = new Solution();
            System.out.println(solution.countSurjections(n, k));
        }
        sc.close();
    }
}
```

### Python
```python
import sys

def power(base, exp, mod):
    res = 1
    base %= mod
    while exp > 0:
        if exp % 2 == 1:
            res = (res * base) % mod
        base = (base * base) % mod
        exp //= 2
    return res

def count_surjections(n: int, k: int) -> int:
    MOD = 1000000007
    
    if k > n:
        return 0
        
    # Precompute Combinations
    C = [[0] * (k + 1) for _ in range(k + 1)]
    for i in range(k + 1):
        C[i][0] = 1
        for j in range(1, i + 1):
            C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD
            
    ans = 0
    for i in range(k + 1):
        term = (C[k][i] * power(k - i, n, MOD)) % MOD
        if i % 2 == 1:
            ans = (ans - term + MOD) % MOD
        else:
            ans = (ans + term) % MOD
            
    return ans

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    k = int(data[1])
    print(count_surjections(n, k))

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

    long long power(long long base, long long exp) {
        long long res = 1;
        base %= MOD;
        while (exp > 0) {
            if (exp % 2 == 1) res = (res * base) % MOD;
            base = (base * base) % MOD;
            exp /= 2;
        }
        return res;
    }

public:
    long long countSurjections(int n, int k) {
        if (k > n) return 0;

        vector<vector<long long>> C(k + 1, vector<long long>(k + 1));
        for (int i = 0; i <= k; i++) {
            C[i][0] = 1;
            for (int j = 1; j <= i; j++) {
                C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD;
            }
        }

        long long ans = 0;
        for (int i = 0; i <= k; i++) {
            long long term = (C[k][i] * power(k - i, n)) % MOD;
            if (i % 2 == 1) {
                ans = (ans - term + MOD) % MOD;
            } else {
                ans = (ans + term) % MOD;
            }
        }

        return ans;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (cin >> n >> k) {
        Solution solution;
        cout << solution.countSurjections(n, k) << "\n";
    }
    return 0;
}
```

### JavaScript
```javascript
const readline = require("readline");

const MOD = 1000000007n;

function power(base, exp) {
  let res = 1n;
  base %= MOD;
  while (exp > 0n) {
    if (exp % 2n === 1n) res = (res * base) % MOD;
    base = (base * base) % MOD;
    exp /= 2n;
  }
  return res;
}

function countSurjections(n, k) {
  if (k > n) return 0;
  
  const N = BigInt(n);
  const K = BigInt(k);
  
  const C = Array(k + 1).fill(0).map(() => Array(k + 1).fill(0n));
  
  for (let i = 0; i <= k; i++) {
    C[i][0] = 1n;
    for (let j = 1; j <= i; j++) {
      C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD;
    }
  }
  
  let ans = 0n;
  for (let i = 0; i <= k; i++) {
    const term = (C[k][i] * power(BigInt(k - i), N)) % MOD;
    if (i % 2 === 1) {
      ans = (ans - term + MOD) % MOD;
    } else {
      ans = (ans + term) % MOD;
    }
  }
  
  return ans.toString();
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
  console.log(countSurjections(n, k));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

Input: `3 2`.
1. `i=0`: `binom20 (2)^3 = 1 * 8 = 8`. `ans = 8`.
2. `i=1`: `binom21 (1)^3 = 2 * 1 = 2`. `ans = 8 - 2 = 6`.
3. `i=2`: `binom22 (0)^3 = 1 * 0 = 0`. `ans = 6 + 0 = 6`.
Result 6.

## ✅ Proof of Correctness

### Invariant
The term for index `i` counts functions that miss at least `i` elements.
Inclusion-Exclusion ensures we count functions that miss exactly 0 elements.

### Why the approach is correct
Standard application of Inclusion-Exclusion Principle.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Stirling Numbers.
  - *Hint:* `S(n, k) = frac1k! sum (-1)^i binomki (k-i)^n`.
- **Extension 2:** Distinguishable vs Indistinguishable.
  - *Hint:* If balls (domain) are indistinguishable, it's partitions of integer `n` into `k` parts.
- **Extension 3:** Fixed points.
  - *Hint:* Derangements.

### Common Mistakes to Avoid

1. **Sign Errors**
   - ❌ Wrong: `ans -= term`.
   - ✅ Correct: `ans = (ans - term + MOD) % MOD`.
2. **Base Case**
   - ❌ Wrong: `k > n` returns negative or garbage.
   - ✅ Correct: Return 0 immediately.

## Related Concepts

- **Stirling Numbers (2nd Kind):** Partitions of a set.
- **Bell Numbers:** Sum of Stirling numbers.
