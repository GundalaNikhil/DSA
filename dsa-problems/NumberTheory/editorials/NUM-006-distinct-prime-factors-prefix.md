---
problem_id: NUM_DISTINCT_PRIME_FACTORS_PREFIX__5173
display_id: NUM-006
slug: distinct-prime-factors-prefix
title: "Distinct Prime Factors Count Prefix"
difficulty: Medium
difficulty_score: 50
topics:
  - Number Theory
  - Sieve
  - Prefix Sums
tags:
  - number-theory
  - sieve
  - prefix
  - medium
premium: true
subscription_tier: basic
---

# NUM-006: Distinct Prime Factors Count Prefix

## 📋 Problem Summary

Let $f(x)$ be the number of distinct prime factors of $x$.
- Precompute $f(x)$ for all $x$ up to $N$.
- Answer queries for the sum of $f(x)$ in range $[l, r]$.
- Input: $N$, $Q$, and queries.
- Output: Range sums.

## 🌍 Real-World Scenario

**Scenario Title:** The Chemical Compound Screener

Imagine you are screening a database of chemical compounds, where each compound is identified by an integer ID.
- The "complexity" of a compound is determined by the number of distinct basic elements (primes) that make up its structure (prime factorization).
- For example, a compound with ID 12 ($2^2 \cdot 3$) has 2 distinct elements (2 and 3). A compound with ID 30 ($2 \cdot 3 \cdot 5$) has 3.
- You want to analyze the total complexity of all compounds in a specific range of IDs to estimate the processing power required for a batch simulation.
- Since you have millions of compounds and thousands of batch queries, you need an efficient way to sum these complexity scores.

**Why This Problem Matters:**

- **Number Theory:** Understanding the distribution of $\omega(n)$ (number of distinct prime factors).
- **Performance:** Combining sieving with prefix sums is a standard technique for range query problems.
- **Data Analysis:** Aggregating properties over ranges.

![Real-World Application](../images/NUM-006/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Sieve Process

Let $N=10$. We want to compute $f(x)$.
Initialize `count` array to 0.

```
i=2 (prime): Add 1 to multiples 2, 4, 6, 8, 10.
i=3 (prime): Add 1 to multiples 3, 6, 9.
i=4 (not prime): Skip.
i=5 (prime): Add 1 to multiples 5, 10.
...

Result f(x):
x: 1 2 3 4 5 6 7 8 9 10
f: 0 1 1 1 1 2 1 1 1 2

Prefix Sum P(x):
x: 0 1 2 3 4 5 6 7 8 9 10
P: 0 0 1 2 3 4 6 7 8 9 11
```

Query $[2, 5]$: $P[5] - P[1] = 4 - 0 = 4$.
($f(2)+f(3)+f(4)+f(5) = 1+1+1+1 = 4$).

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Constraints:** $N \le 10^6$, $Q \le 10^5$.
- **Function:** $f(x)$ counts **distinct** primes. $f(12) = f(2^2 \cdot 3) = 2$.
- **Prefix Sum:** Use 1-based indexing for convenience. $P[i] = P[i-1] + f(i)$.

### Core Concept: Modified Sieve

Instead of marking numbers as composite, we iterate through primes and increment a counter for every multiple.
This is similar to the Sieve of Eratosthenes but additive.
The complexity is $\sum_{p \le N} \frac{N}{p} \approx N \ln \ln N$.

## Naive Approach

### Intuition

For each query, iterate $l$ to $r$, factorize each number, and sum up.

### Algorithm

Factorization takes $O(\sqrt{x})$.
Total time: $O(Q \cdot (r-l) \cdot \sqrt{N})$.
With $N=10^6$, this is way too slow.

### Time Complexity

- **O(Q \cdot N \cdot \sqrt{N})** worst case.

### Space Complexity

- **O(1)**.

## Optimal Approach

### Key Insight

1. **Precompute $f(x)$:** Use a sieve. Iterate $i$ from 2 to $N$. If $f(i) == 0$, it's prime. Iterate multiples $j = i, 2i, \dots$ and increment $f(j)$.
2. **Prefix Sums:** Build $P[i] = P[i-1] + f(i)$.
3. **Query:** Answer in $O(1)$.

### Algorithm

1. Init `f` array of size $N+1$ with 0.
2. For `i` from 2 to $N$:
   - If `f[i] == 0`: (i is prime)
     - For `j` from `i` to `N` step `i`:
       - `f[j]++`
3. Init `pref` array.
4. `pref[0] = 0`.
5. For `i` from 1 to $N$: `pref[i] = pref[i-1] + f[i]`.
6. Answer queries: `pref[r] - pref[l-1]`.

### Time Complexity

- **Precomputation:** $O(N \log \log N)$.
- **Query:** $O(1)$.
- **Total:** $O(N \log \log N + Q)$.

### Space Complexity

- **O(N)**.

![Algorithm Visualization](../images/NUM-006/algorithm-visualization.png)
![Algorithm Steps](../images/NUM-006/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public long[] buildPrefixDistinct(int N) {
        int[] f = new int[N + 1];
        
        // Modified Sieve
        for (int i = 2; i <= N; i++) {
            if (f[i] == 0) { // i is prime
                for (int j = i; j <= N; j += i) {
                    f[j]++;
                }
            }
        }
        
        long[] pref = new long[N + 1];
        for (int i = 1; i <= N; i++) {
            pref[i] = pref[i - 1] + f[i];
        }
        
        return pref;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int N = sc.nextInt();
            int q = sc.nextInt();
            
            Solution solution = new Solution();
            long[] pref = solution.buildPrefixDistinct(N);
            
            for (int i = 0; i < q; i++) {
                int l = sc.nextInt();
                int r = sc.nextInt();
                System.out.println(pref[r] - pref[l - 1]);
            }
        }
        sc.close();
    }
}
```

### Python

```python
import sys

def build_prefix_distinct(N: int):
    f = [0] * (N + 1)
    
    # Modified Sieve
    for i in range(2, N + 1):
        if f[i] == 0:  # i is prime
            for j in range(i, N + 1, i):
                f[j] += 1
                
    pref = [0] * (N + 1)
    for i in range(1, N + 1):
        pref[i] = pref[i-1] + f[i]
        
    return pref

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
        
    iterator = iter(data)
    try:
        N = int(next(iterator))
        q = int(next(iterator))
        
        pref = build_prefix_distinct(N)
        
        results = []
        for _ in range(q):
            l = int(next(iterator))
            r = int(next(iterator))
            results.append(str(pref[r] - pref[l-1]))
            
        print('\n'.join(results))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<long long> buildPrefixDistinct(int N) {
        vector<int> f(N + 1, 0);
        
        for (int i = 2; i <= N; i++) {
            if (f[i] == 0) { // i is prime
                for (int j = i; j <= N; j += i) {
                    f[j]++;
                }
            }
        }
        
        vector<long long> pref(N + 1, 0);
        for (int i = 1; i <= N; i++) {
            pref[i] = pref[i - 1] + f[i];
        }
        
        return pref;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, q;
    if (cin >> N >> q) {
        Solution solution;
        vector<long long> pref = solution.buildPrefixDistinct(N);
        
        for (int i = 0; i < q; i++) {
            int l, r;
            cin >> l >> r;
            cout << pref[r] - pref[l - 1] << "\n";
        }
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function buildPrefixDistinct(N) {
  const f = new Int32Array(N + 1);
  
  for (let i = 2; i <= N; i++) {
    if (f[i] === 0) { // i is prime
      for (let j = i; j <= N; j += i) {
        f[j]++;
      }
    }
  }
  
  // Use BigInt for prefix sums to be safe, though N*logN fits in 53 bits
  // Max sum approx 10^6 * 7 approx 7*10^6. Fits in standard number.
  const pref = new Float64Array(N + 1);
  for (let i = 1; i <= N; i++) {
    pref[i] = pref[i - 1] + f[i];
  }
  
  return pref;
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
  const N = parseInt(data[idx++], 10);
  const q = parseInt(data[idx++], 10);
  
  const pref = buildPrefixDistinct(N);
  const out = [];
  
  for (let i = 0; i < q; i++) {
    const l = parseInt(data[idx++], 10);
    const r = parseInt(data[idx++], 10);
    out.push((pref[r] - pref[l - 1]).toString());
  }
  console.log(out.join("\n"));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

Input: `N=6, Query=[2, 5]`.
1. `f` init 0.
2. `i=2`: `f[2]++, f[4]++, f[6]++`. `f=[0,0,1,0,1,0,1]`.
3. `i=3`: `f[3]++, f[6]++`. `f=[0,0,1,1,1,0,2]`.
4. `i=4`: Skip.
5. `i=5`: `f[5]++`. `f=[0,0,1,1,1,1,2]`.
6. `i=6`: Skip.
7. `pref`:
   - `P[0]=0`
   - `P[1]=0`
   - `P[2]=1`
   - `P[3]=2`
   - `P[4]=3`
   - `P[5]=4`
   - `P[6]=6`
8. Query `[2, 5]`: `P[5] - P[1] = 4 - 0 = 4`.
   - Correct.

## ✅ Proof of Correctness

### Invariant
The sieve iterates every prime $p$ and adds 1 to all its multiples.
Thus, `f[x]` counts exactly how many distinct primes divide $x$.

### Why the approach is correct
Standard application of additive sieve and prefix sums.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Sum of total prime factors (with multiplicity).
  - *Hint:* Instead of `f[j]++`, do `temp = j; while(temp%i==0) { count++; temp/=i; }`. Or better: `f[j] = f[j/p] + 1` where `p` is smallest prime factor.
- **Extension 2:** Count numbers with exactly $k$ prime factors.
  - *Hint:* Use the same sieve, then build prefix sums for each $k$ (or just store counts).
- **Extension 3:** Square-free numbers.
  - *Hint:* Check if any prime factor has exponent > 1.

## Common Mistakes to Avoid

1. **Memory Limit**
   - ❌ Wrong: Using `long` array for `f` if `int` suffices (saves memory).
   - ✅ Correct: `f[x]` is small ($\le 8$ for $N=10^6$), so `int` or even `byte` is fine. `pref` needs `long` for very large $N$, but here `int` fits.
2. **Loop Bounds**
   - ❌ Wrong: `j` starts at `i*i`.
   - ✅ Correct: `j` starts at `i` because we count the prime itself too.

## Related Concepts

- **Omega Function $\omega(n)$:** Number of distinct prime factors.
- **Big Omega Function $\Omega(n)$:** Total number of prime factors.
- **Harmonic Series:** Complexity analysis.
