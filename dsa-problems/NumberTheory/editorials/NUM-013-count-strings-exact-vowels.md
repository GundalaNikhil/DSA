---
problem_id: NUM_COUNT_STRINGS_EXACT_VOWELS__6419
display_id: NUM-013
slug: count-strings-exact-vowels
title: "Count Strings With Exact Vowels"
difficulty: Medium
difficulty_score: 50
topics:
  - Number Theory
  - Combinatorics
  - Modular Arithmetic
tags:
  - number-theory
  - combinatorics
  - modular
  - medium
premium: true
subscription_tier: basic
---

# NUM-013: Count Strings With Exact Vowels

## 📋 Problem Summary

Count the number of strings of length `n` that contain exactly `k` vowels.
- Alphabet: 26 lowercase English letters.
- Vowels: `a, e, i, o, u` (5).
- Consonants: 21.
- Output: Count modulo `10^9+7`.

## 🌍 Real-World Scenario

**Scenario Title:** The Password Validator

You are designing a password policy for a secure system. The policy requires passwords to be exactly `n` characters long and contain exactly `k` special characters (in this analogy, vowels).
- To estimate the strength of this policy against brute-force attacks, you need to calculate the total size of the valid password space.
- A larger space implies higher security (entropy).
- Since the numbers are massive, you compute them modulo a large prime for verification purposes.

**Why This Problem Matters:**

- **Combinatorics:** Fundamental counting principles (multiplication rule, combinations).
- **Probability:** Calculating the probability of specific events in a sequence (Bernoulli trials).
- **Coding Theory:** Error correcting codes often involve counting strings with specific weights.

![Real-World Application](../images/NUM-013/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: String Construction

`n=3, k=1`.
We need strings like `VCC`, `CVC`, `CCV` (V=Vowel, C=Consonant).

```
Structure 1: V C C
Choices:     5 * 21 * 21 = 2205

Structure 2: C V C
Choices:     21 * 5 * 21 = 2205

Structure 3: C C V
Choices:     21 * 21 * 5 = 2205

Total = 3 * 2205 = 6615.
Formula: C(3, 1) * 5^1 * 21^2 = 3 * 5 * 441 = 6615.
```

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Constraints:** `n <= 10^6`. We need `O(n)` or `O(1)` if precomputed.
- **Modulo:** `10^9+7`.
- **Formula:** `binomnk x 5^k x 21^n-k`.

### Core Concept: Binomial Coefficients

We choose `k` positions for the vowels out of `n` available positions: `binomnk`.
For each of the `k` vowel positions, we have 5 choices. Total `5^k`.
For each of the `n-k` consonant positions, we have 21 choices. Total `21^n-k`.
Result: `binomnk * 5^k * 21^n-k`.

## Naive Approach

### Intuition

Generate all strings (recursion) and count.

### Algorithm

Recursive backtracking.

### Time Complexity

- **O(26^n)**. Impossible for `n > 10`.

## Optimal Approach

### Key Insight

Use the closed-form formula.
Precompute factorials to compute `binomnk` in `O(1)` or `O(log MOD)` time.
Use modular exponentiation for powers.

### Algorithm

1. Precompute factorials up to `n`.
2. Compute `binomnk = fracn!k!(n-k)! +/-od M`.
3. Compute `P_1 = 5^k +/-od M`.
4. Compute `P_2 = 21^n-k +/-od M`.
5. Result = `(binomnk * P_1 * P_2) +/-od M`.

### Time Complexity

- **O(n)** for precomputation (or `O(1)` if just one query and we compute factorials on fly, but usually `O(n)` is standard).
- **O(\log M)** for modular inverse and exponentiation.

### Space Complexity

- **O(n)** for factorials.

![Algorithm Visualization](../images/NUM-013/algorithm-visualization.png)
![Algorithm Steps](../images/NUM-013/algorithm-steps.png)

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

    private long modInverse(long n) {
        return power(n, MOD - 2);
    }

    private long nCr(int n, int r, long[] fact, long[] invFact) {
        if (r < 0 || r > n) return 0;
        return fact[n] * invFact[r] % MOD * invFact[n - r] % MOD;
    }

    public long countStrings(int n, int k) {
        long[] fact = new long[n + 1];
        long[] invFact = new long[n + 1];
        fact[0] = 1;
        invFact[0] = 1;
        
        for (int i = 1; i <= n; i++) {
            fact[i] = (fact[i - 1] * i) % MOD;
        }
        invFact[n] = modInverse(fact[n]);
        for (int i = n - 1; i >= 1; i--) {
            invFact[i] = (invFact[i + 1] * (i + 1)) % MOD;
        }

        long combinations = nCr(n, k, fact, invFact);
        long vowels = power(5, k);
        long consonants = power(21, n - k);
        
        return combinations * vowels % MOD * consonants % MOD;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int k = sc.nextInt();
            Solution solution = new Solution();
            System.out.println(solution.countStrings(n, k));
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

def modInverse(n, mod):
    return power(n, mod - 2, mod)

def count_strings(n: int, k: int) -> int:
    MOD = 1000000007
    
    if k < 0 or k > n:
        return 0
        
    # Compute nCr
    # Since we only need one nCr, we can compute directly without full array if we wanted O(k) or O(n)
    # But O(n) precompute is fine.
    
    fact = [1] * (n + 1)
    for i in range(2, n + 1):
        fact[i] = (fact[i - 1] * i) % MOD
        
    invFact = [1] * (n + 1)
    invFact[n] = modInverse(fact[n], MOD)
    for i in range(n - 1, 1, -1):
        invFact[i] = (invFact[i + 1] * (i + 1)) % MOD
        
    nCr = fact[n] * invFact[k] % MOD * invFact[n - k] % MOD
    
    vowels = power(5, k, MOD)
    consonants = power(21, n - k, MOD)
    
    return nCr * vowels % MOD * consonants % MOD

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    k = int(data[1])
    print(count_strings(n, k))

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

    long long modInverse(long long n) {
        return power(n, MOD - 2);
    }

public:
    long long countStrings(int n, int k) {
        if (k < 0 || k > n) return 0;

        vector<long long> fact(n + 1);
        vector<long long> invFact(n + 1);
        fact[0] = 1;
        invFact[0] = 1;

        for (int i = 1; i <= n; i++) {
            fact[i] = (fact[i - 1] * i) % MOD;
        }
        invFact[n] = modInverse(fact[n]);
        for (int i = n - 1; i >= 1; i--) {
            invFact[i] = (invFact[i + 1] * (i + 1)) % MOD;
        }

        long long nCr = fact[n] * invFact[k] % MOD * invFact[n - k] % MOD;
        long long vowels = power(5, k);
        long long consonants = power(21, n - k);

        return nCr * vowels % MOD * consonants % MOD;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (cin >> n >> k) {
        Solution solution;
        cout << solution.countStrings(n, k) << "\n";
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

function modInverse(n) {
  return power(n, MOD - 2n);
}

function countStrings(n, k) {
  if (k < 0 || k > n) return 0;
  
  const N = BigInt(n);
  const K = BigInt(k);
  
  // Compute factorial directly if n is small, or use array
  // Given n <= 10^6, array is needed.
  // But JS memory limit might be tight for 10^6 BigInts?
  // Let's optimize: we only need fact[n], invFact[k], invFact[n-k].
  // We can compute fact[n] in O(n), then invFact.
  
  // We can just compute these three values.
  
  let factN = 1n;
  let factK = 1n;
  let factNK = 1n;
  
  for (let i = 1n; i <= N; i++) {
    factN = (factN * i) % MOD;
    if (i === K) factK = factN;
    if (i === (N - K)) factNK = factN;
  }
  
  // Handle 0! = 1
  if (K === 0n) factK = 1n;
  if (N - K === 0n) factNK = 1n;
  
  const invFactK = modInverse(factK);
  const invFactNK = modInverse(factNK);
  
  const nCr = factN * invFactK % MOD * invFactNK % MOD;
  const vowels = power(5n, K);
  const consonants = power(21n, N - K);
  
  return (nCr * vowels % MOD * consonants % MOD).toString();
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
  console.log(countStrings(n, k));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

Input: `2 1`.
1. `nCr(2, 1) = 2`.
2. `5^1 = 5`.
3. `21^1 = 21`.
4. `2 * 5 * 21 = 10 * 21 = 210`.
Matches example.

## ✅ Proof of Correctness

### Invariant
The formula counts disjoint sets of strings based on vowel positions.
Since we sum over all possible positions (`binomnk`), we cover all cases exactly once.

### Why the approach is correct
Standard combinatorics.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** At least `k` vowels.
  - *Hint:* Sum the results for `i = k dots n`.
- **Extension 2:** No two vowels adjacent.
  - *Hint:* Stars and Bars or DP.
- **Extension 3:** Palindromes with `k` vowels.
  - *Hint:* Construct half the string.

### Common Mistakes to Avoid

1. **Integer Overflow**
   - ❌ Wrong: `fact[i] * i` without modulo.
   - ✅ Correct: Always modulo.
2. **Inverse Calculation**
   - ❌ Wrong: Division `a / b % MOD`.
   - ✅ Correct: `a * modInverse(b) % MOD`.

## Related Concepts

- **Binomial Distribution:** Probability version of this problem.
- **Fermat's Little Theorem:** Used for modular inverse.
