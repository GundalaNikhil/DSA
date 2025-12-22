---
problem_id: NUM_SUM_DIVISORS_RANGE__4175
display_id: NUM-010
slug: sum-divisors-range
title: "Sum of Divisors in Range"
difficulty: Medium
difficulty_score: 50
topics:
  - Number Theory
  - Divisors
  - Prefix Sums
tags:
  - number-theory
  - divisors
  - prefix
  - medium
premium: true
subscription_tier: basic
---

# NUM-010: Sum of Divisors in Range

## 📋 Problem Summary

Compute the sum of $\sigma(n)$ for all $n$ in the range $[L, R]$, modulo $10^9+7$.
- $\sigma(n)$ is the sum of all positive divisors of $n$.
- Input: $L, R$.
- Output: $\sum_{n=L}^R \sigma(n) \pmod{10^9+7}$.

## 🌍 Real-World Scenario

**Scenario Title:** The Resource Allocator

You are managing a distributed cloud system where each server node $n$ has a capacity determined by the sum of its factors (representing modular components it can support).
- You are given a cluster of servers with IDs ranging from $L$ to $R$.
- To balance the load or estimate the total computational power of this cluster, you need to sum up the capacities of all servers in this range.
- Since the IDs can be up to $1,000,000$, iterating through each number and finding its divisors individually is too slow. You need a bulk estimation method.

**Why This Problem Matters:**

- **Number Theory:** Understanding the average order of arithmetic functions.
- **Algorithm Design:** Using sieves for bulk precomputation.
- **Performance:** Optimizing $O(N \sqrt{N})$ to $O(N \log N)$.

![Real-World Application](../images/NUM-010/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Divisor Contribution

Let $R=6$. We want $\sum_{n=1}^6 \sigma(n)$.
Instead of summing by number, sum by divisor.
How many times does divisor $d$ appear in numbers $1 \dots 6$?
It appears in multiples: $d, 2d, 3d, \dots$.
Count is $\lfloor 6/d \rfloor$.
Total Sum = $\sum_{d=1}^6 d \cdot \lfloor 6/d \rfloor$.

```
d=1: 1 appears in 1,2,3,4,5,6 (6 times) -> 1*6 = 6
d=2: 2 appears in 2,4,6 (3 times)       -> 2*3 = 6
d=3: 3 appears in 3,6 (2 times)         -> 3*2 = 6
d=4: 4 appears in 4 (1 time)            -> 4*1 = 4
d=5: 5 appears in 5 (1 time)            -> 5*1 = 5
d=6: 6 appears in 6 (1 time)            -> 6*1 = 6
Total = 33.

Check sigma:
s(1)=1
s(2)=3
s(3)=4
s(4)=7
s(5)=6
s(6)=12
Sum = 1+3+4+7+6+12 = 33. Matches.
```

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Constraints:** $R \le 10^6$.
- **Range:** $[L, R]$. We can compute $S(R) - S(L-1)$, where $S(x) = \sum_{i=1}^x \sigma(i)$.
- **Modulo:** Result modulo $10^9+7$.

### Core Concept: Divisor Sum Sieve

We can compute $\sigma(n)$ for all $n$ using a sieve-like process.
Initialize array `sigma` to 0.
Iterate $i$ from 1 to $R$.
For each multiple $j = i, 2i, 3i \dots$, add $i$ to `sigma[j]`.
This takes $O(R \log R)$.

## Naive Approach

### Intuition

For each $n$ from $L$ to $R$, find divisors by trial division up to $\sqrt{n}$.

### Algorithm

```python
total = 0
for n in range(L, R + 1):
    s = 0
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            s += i
            if i*i != n: s += n//i
    total += s
return total
```

### Time Complexity

- **O((R-L) \sqrt{R})**.
- Worst case $L=1, R=10^6$: $10^6 \times 1000 = 10^9$ ops. Too slow.

## Optimal Approach

### Key Insight

Since we need the sum over a range, we can use the "contribution technique" (Dirichlet Hyperbola Method logic) or simply precompute $\sigma$ array using a sieve.
Given $R=10^6$, $O(R \log R)$ precomputation is perfectly fine ($\approx 2 \cdot 10^7$ ops).

### Algorithm

1. Create array `sigma` of size $R+1$.
2. Iterate `i` from 1 to $R$:
   - Iterate `j` from `i` to `R` step `i`:
     - `sigma[j] += i`.
3. Compute prefix sums of `sigma` array.
4. Answer is `prefix[R] - prefix[L-1]`.

### Time Complexity

- **O(R \log R)**.
- **Space:** $O(R)$.

### Alternative (Dirichlet Hyperbola Method)

We can compute $\sum_{i=1}^N \sigma(i) = \sum_{d=1}^N d \cdot \lfloor N/d \rfloor$ in $O(\sqrt{N})$ time.
This is even faster!
Since we only have one query (or few), we can just compute `solve(R) - solve(L-1)` where `solve(N)` uses the $O(\sqrt{N})$ approach.
However, the problem statement mentions "Precompute sigma values using a sieve-like method", suggesting the sieve approach is expected. But the $O(\sqrt{N})$ approach is superior. I will implement the Sieve approach as it aligns with the "Notes" and is simpler to explain for beginners, but mention the $\sqrt{N}$ optimization.
The Sieve approach is $O(R \log R)$.
The $\sqrt{N}$ approach is $O(\sqrt{R})$.
Given the constraints and "Notes", I will stick to the Sieve approach as it's more general if we had multiple queries (though here we don't).

![Algorithm Visualization](../images/NUM-010/algorithm-visualization.png)
![Algorithm Steps](../images/NUM-010/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    static final int MOD = 1000000007;

    public long rangeSigma(int L, int R) {
        long[] sigma = new long[R + 1];
        
        // Sieve-like process to compute sigma for all numbers up to R
        for (int i = 1; i <= R; i++) {
            for (int j = i; j <= R; j += i) {
                sigma[j] += i;
            }
        }
        
        long total = 0;
        for (int i = L; i <= R; i++) {
            total = (total + sigma[i]) % MOD;
        }
        
        return total;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int L = sc.nextInt();
            int R = sc.nextInt();
            Solution solution = new Solution();
            System.out.println(solution.rangeSigma(L, R));
        }
        sc.close();
    }
}
```

### Python

```python
import sys

def range_sigma(L: int, R: int) -> int:
    MOD = 1000000007
    sigma = [0] * (R + 1)
    
    for i in range(1, R + 1):
        for j in range(i, R + 1, i):
            sigma[j] += i
            
    total = 0
    for i in range(L, R + 1):
        total = (total + sigma[i]) % MOD
        
    return total

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    L = int(data[0])
    R = int(data[1])
    print(range_sigma(L, R))

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
    long long rangeSigma(int L, int R) {
        vector<long long> sigma(R + 1, 0);
        
        for (int i = 1; i <= R; i++) {
            for (int j = i; j <= R; j += i) {
                sigma[j] += i;
            }
        }
        
        long long total = 0;
        for (int i = L; i <= R; i++) {
            total = (total + sigma[i]) % MOD;
        }
        
        return total;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int L, R;
    if (cin >> L >> R) {
        Solution solution;
        cout << solution.rangeSigma(L, R) << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function rangeSigma(L, R) {
  const MOD = 1000000007n;
  const sigma = new BigInt64Array(R + 1);
  
  for (let i = 1; i <= R; i++) {
    const val = BigInt(i);
    for (let j = i; j <= R; j += i) {
      sigma[j] += val;
    }
  }
  
  let total = 0n;
  for (let i = L; i <= R; i++) {
    total = (total + sigma[i]) % MOD;
  }
  
  return total.toString();
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  const L = parseInt(data[0], 10);
  const R = parseInt(data[1], 10);
  console.log(rangeSigma(L, R));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

Input: `L=2, R=4`.
1. `sigma` array size 5.
2. `i=1`: `sigma` becomes `[0, 1, 1, 1, 1]`.
3. `i=2`: `sigma` becomes `[0, 1, 3, 1, 3]`. (Add 2 to idx 2, 4)
4. `i=3`: `sigma` becomes `[0, 1, 3, 4, 3]`. (Add 3 to idx 3)
5. `i=4`: `sigma` becomes `[0, 1, 3, 4, 7]`. (Add 4 to idx 4)
6. Sum range `[2, 4]`: `sigma[2] + sigma[3] + sigma[4]`.
7. `3 + 4 + 7 = 14`.
Matches example.

## ✅ Proof of Correctness

### Invariant
After the outer loop finishes for value `i`, every multiple of `i` in the array has had `i` added to it.
Thus, `sigma[n]` contains the sum of all its divisors.

### Why the approach is correct
Standard sieve technique for arithmetic functions.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** $N \le 10^{12}$.
  - *Hint:* Use Dirichlet Hyperbola Method. $\sum_{i=1}^N \sigma(i) = \sum_{i=1}^N i \lfloor N/i \rfloor$. Can be computed in $O(\sqrt{N})$.
- **Extension 2:** Sum of $\sigma(n)^k$.
  - *Hint:* Multiplicative functions and Min_25 sieve.
- **Extension 3:** Average value of $\sigma(n)$.
  - *Hint:* It's $\frac{\pi^2}{6} n$.

### Common Mistakes to Avoid

1. **Modulo Placement**
   - ❌ Wrong: `sigma[j] = (sigma[j] + i) % MOD`.
   - ✅ Correct: While technically correct, it's better to keep `sigma[j]` exact if it fits in `long` (it does, max $\sigma(10^6) \approx 2.5 \cdot 10^6$) and modulo only at the end sum. This avoids modulo overhead in the inner loop.
2. **Loop Bounds**
   - ❌ Wrong: `j` starts at 0.
   - ✅ Correct: `j` starts at `i`.

## Related Concepts

- **Harmonic Series:** The complexity is $\sum N/i \approx N \ln N$.
- **Dirichlet Convolution:** $\sigma = 1 * Id$.
