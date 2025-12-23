---
problem_id: NUM_CRT_EXISTENCE_VALUE__5186
display_id: NUM-015
slug: crt-existence-value
title: "CRT Existence and Value"
difficulty: Medium
difficulty_score: 58
topics:
  - Number Theory
  - Chinese Remainder Theorem
  - GCD
tags:
  - number-theory
  - crt
  - gcd
  - medium
premium: true
subscription_tier: basic
---

# NUM-015: CRT Existence and Value

## 📋 Problem Summary

Solve a system of `k` linear congruences:
`x equiv a_1 +/-odm_1`
`x equiv a_2 +/-odm_2`
`dots`
`x equiv a_k +/-odm_k`
- Moduli `m_i` are **not necessarily coprime**.
- Determine if a solution exists. If yes, find the smallest non-negative `x`.

## 🌍 Real-World Scenario

**Scenario Title:** The Planetary Alignment

You are an astronomer tracking `k` different planets orbiting a star.
- Planet `i` completes an orbit every `m_i` days.
- Currently, Planet `i` is at position `a_i` (measured in days since passing a reference point).
- You want to know when all planets will simultaneously be at their respective reference points (or a specific alignment configuration).
- This requires finding a time `x` that satisfies the orbital periodicity constraints for all planets simultaneously.
- Since orbital periods might share common factors (resonances), a perfect alignment might never happen. You need to verify existence first.

**Why This Problem Matters:**

- **Cryptography:** Secret sharing schemes (Shamir's Secret Sharing uses polynomial interpolation, but CRT is used in others like Mignotte's).
- **Scheduling:** Synchronizing periodic tasks with offsets.
- **Parallel Computing:** Reconstructing large integers from modular residues.

![Real-World Application](../images/NUM-015/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Merging Congruences

Eq 1: `x equiv 2 +/-od 6 implies x in 2, 8, 14, 20, dots`
Eq 2: `x equiv 5 +/-od 9 implies x in 5, 14, 23, 32, dots`

Intersection:
- 14 is in both.
- Next is `14 + lcm(6, 9) = 14 + 18 = 32`.
- Solution: `x equiv 14 +/-od18`.

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Coprimality:** Standard CRT requires `gcd(m_i, m_j) = 1`. Here, we must handle `gcd > 1`.
- **Condition:** `x equiv a_1 +/-odm_1` and `x equiv a_2 +/-odm_2` has a solution iff `a_1 equiv a_2 +/-odgcd(m_1, m_2)`.
- **Overflow:** Intermediate moduli can grow up to `lcm(m_1 dots m_k)`. With `m_i <= 10^9` and `k=10`, this can exceed 64-bit integers. However, usually test cases for "Medium" keep the LCM within `long long` range, or we need `__int128` (C++) / `BigInt` (Java/JS/Python). Given constraints `m_i <= 10^9`, LCM can be huge. But typical CP problems with this constraint imply the answer fits in 64-bit or we use BigInt. Python/Java/JS handle this. C++ needs `__int128`.

### Core Concept: Generalized CRT

Iteratively merge two congruences:
1. `x = k_1 m_1 + a_1`
2. `k_1 m_1 + a_1 equiv a_2 +/-odm_2`
3. `k_1 m_1 equiv a_2 - a_1 +/-odm_2`
   - Let `g = gcd(m_1, m_2)`.
   - If `(a_2 - a_1) % g !=q 0`, no solution.
   - Divide by `g`: `k_1 fracm_1g equiv fraca_2 - a_1g +/-odfracm_2g`.
   - Solve for `k_1` using Modular Inverse.
   - Substitute `k_1` back to find `x`.
   - New modulus is `lcm(m_1, m_2)`.

## Naive Approach

### Intuition

Check numbers `0, 1, 2, dots` until one satisfies all.

### Algorithm

Loop `x` from 0 to `lcm(m_i)`.

### Time Complexity

- **O(LCM)**. Exponential.

## Optimal Approach

### Key Insight

Use the iterative merging strategy described above.
Use Extended Euclidean Algorithm for modular inverse.
Handle potential overflows with `__int128` in C++.

### Algorithm

1. Start with `current_a = 0`, `current_m = 1`.
2. For each `(a_i, m_i)`:
   - Solve system:
     - `X equiv current_a +/-odcurrent_m`
     - `X equiv a_i +/-odm_i`
   - Let `g = gcd(current_m, m_i)`.
   - Check if `(a_i - current_a) % g == 0`. If not, return NO.
   - Solve `p * current_m equiv (a_i - current_a) +/-odm_i` for `p`.
     - This reduces to `p * fraccurrent_mg equiv fraca_i - current_ag +/-odfracm_ig`.
     - Let `inv = modInverse(fraccurrent_mg, fracm_ig)`.
     - `p = (inv * fraca_i - current_ag) % fracm_ig`.
   - New `X = current_a + p * current_m`.
   - New modulus `M = lcm(current_m, m_i)`.
   - Update `current_a = X`, `current_m = M`.
   - Ensure `current_a` is normalized to `[0, M-1]`.
3. Return `current_a`.

### Time Complexity

- **O(k \log(\text{max\_m}))**.

### Space Complexity

- **O(1)**.

![Algorithm Visualization](../images/NUM-015/algorithm-visualization.png)
![Algorithm Steps](../images/NUM-015/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;
import java.math.BigInteger;

class Solution {
    // Extended Euclidean Algorithm
    // Returns [g, x, y] such that ax + by = g
    private long[] extendedGCD(long a, long b) {
        if (b == 0) return new long[]{a, 1, 0};
        long[] vals = extendedGCD(b, a % b);
        long g = vals[0];
        long x1 = vals[1];
        long y1 = vals[2];
        long x = y1;
        long y = x1 - (a / b) * y1;
        return new long[]{g, x, y};
    }

    private long mulMod(long a, long b, long m) {
        // Java long is 64-bit signed. a*b can overflow.
        // Use BigInteger for safety or __int128 logic equivalent
        return BigInteger.valueOf(a).multiply(BigInteger.valueOf(b))
                .mod(BigInteger.valueOf(m)).longValue();
    }

    public Long crtSolve(long[] a, long[] m) {
        long curA = 0;
        long curM = 1;
        
        for (int i = 0; i < a.length; i++) {
            long A = a[i];
            long M = m[i];
            
            // Solve: x = curA (mod curM), x = A (mod M)
            // curA + k * curM = A (mod M)
            // k * curM = A - curA (mod M)
            
            long rhs = (A - curA) % M;
            if (rhs < 0) rhs += M;
            
            long[] gcdRes = extendedGCD(curM, M);
            long g = gcdRes[0];
            long x = gcdRes[1]; // curM * x + M * y = g
            
            if (rhs % g != 0) return null;
            
            // k * (curM/g) = (rhs/g) (mod M/g)
            // We know x * curM = g (mod M) -> x * (curM/g) * g = g (mod M) -> x * (curM/g) = 1 (mod M/g)
            // So inverse of (curM/g) mod (M/g) is x.
            
            long mod = M / g;
            long k = mulMod(rhs / g, (x % mod + mod) % mod, mod);
            
            // Update curA = curA + k * curM
            // But we need to be careful about overflow for curA + k * curM
            // The new modulus will be lcm(curM, M) = curM * (M/g)
            
            BigInteger bigCurA = BigInteger.valueOf(curA);
            BigInteger bigK = BigInteger.valueOf(k);
            BigInteger bigCurM = BigInteger.valueOf(curM);
            
            BigInteger term = bigK.multiply(bigCurM);
            BigInteger newCurA = bigCurA.add(term);
            
            BigInteger newCurM = bigCurM.multiply(BigInteger.valueOf(M / g));
            
            curA = newCurA.mod(newCurM).longValue(); // Assuming result fits in long, else return String/BigInt
            curM = newCurM.longValue();
        }
        
        return curA;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int k = sc.nextInt();
            long[] a = new long[k];
            long[] m = new long[k];
            for (int i = 0; i < k; i++) {
                a[i] = sc.nextLong();
                m[i] = sc.nextLong();
            }

            Solution solution = new Solution();
            Long res = solution.crtSolve(a, m);
            if (res == null) {
                System.out.println("NO");
            } else {
                System.out.println(res);
            }
        }
        sc.close();
    }
}
```

### Python

```python
import sys

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y

def crt_solve(a, m):
    cur_a = 0
    cur_m = 1
    
    for i in range(len(a)):
        A = a[i]
        M = m[i]
        
        # k * cur_m = A - cur_a (mod M)
        rhs = (A - cur_a) % M
        
        g, x, y = extended_gcd(cur_m, M)
        
        if rhs % g != 0:
            return None
            
        inv = x % (M // g)
        k = (rhs // g) * inv % (M // g)
        
        # New state
        # cur_a = cur_a + k * cur_m
        # cur_m = lcm(cur_m, M)
        
        new_m = cur_m * (M // g)
        cur_a = (cur_a + k * cur_m) % new_m
        cur_m = new_m
        
    return cur_a

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    iterator = iter(data)
    try:
        k = int(next(iterator))
        a = []
        m = []
        for _ in range(k):
            a.append(int(next(iterator)))
            m.append(int(next(iterator)))
            
        res = crt_solve(a, m)
        print("NO" if res is None else res)
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

using namespace std;

class Solution {
    // Use __int128 for intermediate calculations to prevent overflow
    typedef __int128_t int128;

    int128 extendedGCD(int128 a, int128 b, int128 &x, int128 &y) {
        if (b == 0) {
            x = 1;
            y = 0;
            return a;
        }
        int128 x1, y1;
        int128 g = extendedGCD(b, a % b, x1, y1);
        x = y1;
        y = x1 - (a / b) * y1;
        return g;
    }

public:
    bool crtSolve(const vector<long long>& a, const vector<long long>& m, long long& result) {
        int128 curA = 0;
        int128 curM = 1;
        
        for (size_t i = 0; i < a.size(); ++i) {
            int128 A = a[i];
            int128 M = m[i];
            
            // k * curM = A - curA (mod M)
            int128 rhs = (A - curA) % M;
            if (rhs < 0) rhs += M;
            
            int128 x, y;
            int128 g = extendedGCD(curM, M, x, y);
            
            if (rhs % g != 0) return false;
            
            int128 mod = M / g;
            // x is inverse of curM/g mod M/g
            // k = (rhs/g) * x (mod M/g)
            
            int128 k = (rhs / g) % mod * (x % mod + mod) % mod;
            k %= mod;
            
            int128 newM = curM * (M / g);
            curA = (curA + k * curM) % newM;
            curM = newM;
        }
        
        result = (long long)curA;
        return true;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k;
    if (cin >> k) {
        vector<long long> a(k), m(k);
        for (int i = 0; i < k; i++) {
            cin >> a[i] >> m[i];
        }

        Solution solution;
        long long result;
        if (!solution.crtSolve(a, m, result)) {
            cout << "NO\n";
        } else {
            cout << result << "\n";
        }
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function extendedGCD(a, b) {
  if (b === 0n) return [a, 1n, 0n];
  const [g, x1, y1] = extendedGCD(b, a % b);
  const x = y1;
  const y = x1 - (a / b) * y1;
  return [g, x, y];
}

function crtSolve(a, m) {
  let curA = 0n;
  let curM = 1n;
  
  for (let i = 0; i < a.length; i++) {
    const A = BigInt(a[i]);
    const M = BigInt(m[i]);
    
    let rhs = (A - curA) % M;
    if (rhs < 0n) rhs += M;
    
    const [g, x, y] = extendedGCD(curM, M);
    
    if (rhs % g !== 0n) return null;
    
    const mod = M / g;
    let k = (rhs / g) * (x % mod + mod) % mod; // x is inverse of curM/g
    
    const newM = curM * (M / g);
    curA = (curA + k * curM) % newM;
    curM = newM;
  }
  
  return curA;
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
  const k = parseInt(data[idx++], 10);
  const a = [];
  const m = [];
  for (let i = 0; i < k; i++) {
    a.push(parseInt(data[idx++], 10));
    m.push(parseInt(data[idx++], 10));
  }
  const res = crtSolve(a, m);
  console.log(res === null ? "NO" : res.toString());
});
```

## 🧪 Test Case Walkthrough (Dry Run)

Input: `2 6`, `5 9`.
1. `curA=0, curM=1`.
2. Eq 1: `2 6`.
   - `rhs = 2`. `g=1`. `inv=1`. `k=2`.
   - `curA = 0 + 2*1 = 2`. `curM = 6`.
3. Eq 2: `5 9`.
   - `curA=2, curM=6`.
   - `rhs = (5-2)%9 = 3`.
   - `gcd(6, 9) = 3`.
   - `3 % 3 == 0`. Valid.
   - `mod = 9/3 = 3`.
   - `inv`: `6x + 9y = 3`. `2x + 3y = 1`. `x=-1` (or 2 mod 3).
   - `k = (3/3) * 2 % 3 = 2`.
   - `newM = 6 * (9/3) = 18`.
   - `curA = 2 + 2*6 = 14`.
   - `curA = 14 % 18 = 14`.
4. Result 14.

## ✅ Proof of Correctness

### Invariant
`curA` is the unique solution modulo `curM` for the first `i` equations.
We inductively extend this to `i+1`.

### Why the approach is correct
Generalized CRT logic handles non-coprime moduli by checking consistency with GCD.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Output all solutions in range `[0, N]`.
  - *Hint:* Solutions are `x, x+M, x+2M dots`. Just iterate.
- **Extension 2:** Moduli are large primes.
  - *Hint:* Standard CRT with precomputed inverses.
- **Extension 3:** Parallel CRT.
  - *Hint:* Divide and conquer merging.

### Common Mistakes to Avoid

1. **Overflow**
   - ❌ Wrong: `curA + k * curM` overflows `long long`.
   - ✅ Correct: Use `__int128` or `BigInt`.
2. **Negative Modulo**
   - ❌ Wrong: `(a - b) % m` can be negative in C++/Java.
   - ✅ Correct: `((a - b) % m + m) % m`.

## Related Concepts

- **Extended Euclidean Algorithm:** The core engine here.
- **Modular Inverse:** Special case of linear congruence.
