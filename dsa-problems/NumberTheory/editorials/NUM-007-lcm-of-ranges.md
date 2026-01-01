---
problem_id: NUM_LCM_OF_RANGES__8402
display_id: NUM-007
slug: lcm-of-ranges
title: "LCM of Ranges"
difficulty: Medium
difficulty_score: 52
topics:
  - Number Theory
  - LCM
  - Prime Factorization
tags:
  - number-theory
  - lcm
  - queries
  - medium
premium: true
subscription_tier: basic
---

# NUM-007: LCM of Ranges

## 📋 Problem Summary

Given an array `A`, answer queries for the Least Common Multiple (LCM) of the subarray `A[l dots r]` modulo `M`.
- Constraint: The range length `r - l + 1` is small (`<= 21`).
- Input: Array `A`, queries `(l, r)`, modulus `M`.
- Output: `lcm(A[l], dots, A[r]) +/-od M`.

## 🌍 Real-World Scenario

**Scenario Title:** The Event Synchronizer

You are managing a factory with multiple machines. Each machine `i` has a cycle time `A[i]` seconds.
- You want to synchronize a specific group of machines (from index `l` to `r`) so that they all start a new cycle simultaneously.
- The time until they all align again is the Least Common Multiple (LCM) of their cycle times.
- Since the LCM can be huge (exceeding standard integer limits), you only need the value modulo a large number `M` for scheduling purposes (e.g., checking if alignment happens within a specific time window).

**Why This Problem Matters:**

- **Scheduling:** Finding common periods for tasks.
- **Cryptography:** Order of elements in groups.
- **Arithmetic:** Handling large numbers via modular arithmetic.

![Real-World Application](../images/NUM-007/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: LCM Calculation

Range: `[2, 6, 3]`

```
2 = 2^1
6 = 2^1 * 3^1
3 = 3^1

Max exponents:
Prime 2: max(1, 1, 0) = 1 -> 2^1
Prime 3: max(0, 1, 1) = 1 -> 3^1

LCM = 2^1 * 3^1 = 6
```

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Range Length:** Small (`<= 21`). This is the key constraint. We don't need a Segment Tree.
- **Modulo:** The result must be modulo `M`.
- **LCM Definition:** `lcm(a, b) = (a * b) / gcd(a, b)`. For multiple numbers, `lcm(S) = prod p_i^max(e_i)`.
- **Caution:** We cannot simply do `(a * b / gcd(a, b)) % M` because division modulo `M` requires modular inverse, which might not exist if `gcd(a, b)` is not coprime to `M`. Instead, we must use prime factorization.

### Core Concept: Prime Factorization

Since the range is small, we can collect all numbers in the range, find their prime factorizations, and for each prime `p`, find the maximum exponent `e` that appears in the range.
The answer is `prod p^max(e) +/-od M`.

## Naive Approach

### Intuition

Iteratively compute LCM: `res = lcm(res, A[i])`.

### Algorithm


### Issues

- Intermediate `res` can grow very large (hundreds of digits), causing overflow before modulo.
- Python handles large integers automatically, but C++/Java do not.
- Even in Python, operations on huge numbers are slow.

## Optimal Approach

### Key Insight

Use the property: `lcm(S) = prod_p p^max_x in S v_p(x)`.
Since range is small and numbers are up to `10^9`, we can just use a map to store max exponents.

### Algorithm

1. For each query `(l, r)`:
   - Create a map `max_exponents`.
   - For each number `x` in `A[l dots r]`:
     - Factorize `x`: `x = p_1^e_1 p_2^e_2 dots`
     - For each factor `p^e`, update `max_exponents[p] = max(max_exponents[p], e)`.
   - Compute result: `ans = 1`.
   - For each `p, e` in `max_exponents`:
     - `ans = (ans * power(p, e, M)) % M`.
   - Return `ans`.

### Time Complexity

- **Factorization:** `O(sqrtA[i])`.
- **Total per query:** `O(len * sqrtA[i])`.
- With len `<= 21` and `A[i] <= 10^9`, this is roughly `20 x 31622 ~= 6 * 10^5` ops per query.
- For `Q=10^5`, this is too slow (`6 * 10^10`).
- **Optimization:** Since the range length is small (`<= 21`), trial division up to `sqrtx` is efficient enough. Average case is very fast when we stop early once `x=1`.

### Space Complexity

- **O(1)** auxiliary (map size is small).

![Algorithm Visualization](../images/NUM-007/algorithm-visualization.png)
![Algorithm Steps](../images/NUM-007/algorithm-steps.png)

## Implementations

### Java
```java
import java.util.*;

class Solution {
    public long lcmRange(int[] a, int l, int r, long MOD) {
        Map<Integer, Integer> maxExponents = new HashMap<>();
        
        for (int i = l; i <= r; i++) {
            int num = a[i];
            for (int p = 2; p * p <= num; p++) {
                if (num % p == 0) {
                    int count = 0;
                    while (num % p == 0) {
                        num /= p;
                        count++;
                    }
                    maxExponents.put(p, Math.max(maxExponents.getOrDefault(p, 0), count));
                }
            }
            if (num > 1) {
                maxExponents.put(num, Math.max(maxExponents.getOrDefault(num, 0), 1));
            }
        }
        
        long ans = 1;
        for (Map.Entry<Integer, Integer> entry : maxExponents.entrySet()) {
            int p = entry.getKey();
            int e = entry.getValue();
            long term = power(p, e, MOD);
            ans = (ans * term) % MOD;
        }
        return ans;
    }
    
    private long power(long base, long exp, long mod) {
        long res = 1;
        base %= mod;
        while (exp > 0) {
            if ((exp & 1) == 1) res = (res * base) % mod;
            base = (base * base) % mod;
            exp >>= 1;
        }
        return res;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int q = sc.nextInt();
            long MOD = sc.nextLong();
            int[] a = new int[n];
            for (int i = 0; i < n; i++) a[i] = sc.nextInt();

            Solution solution = new Solution();
            for (int i = 0; i < q; i++) {
                int l = sc.nextInt();
                int r = sc.nextInt();
                System.out.println(solution.lcmRange(a, l, r, MOD));
            }
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

def lcm_range(a, l, r, MOD):
    max_exponents = {}
    
    for i in range(l, r + 1):
        num = a[i]
        d = 2
        while d * d <= num:
            if num % d == 0:
                count = 0
                while num % d == 0:
                    num //= d
                    count += 1
                max_exponents[d] = max(max_exponents.get(d, 0), count)
            d += 1
        if num > 1:
            max_exponents[num] = max(max_exponents.get(num, 0), 1)
            
    ans = 1
    for p, e in max_exponents.items():
        ans = (ans * power(p, e, MOD)) % MOD
        
    return ans

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
        
    iterator = iter(data)
    try:
        n = int(next(iterator))
        q = int(next(iterator))
        MOD = int(next(iterator))
        a = [int(next(iterator)) for _ in range(n)]
        
        results = []
        for _ in range(q):
            l = int(next(iterator))
            r = int(next(iterator))
            results.append(str(lcm_range(a, l, r, MOD)))
            
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
#include <map>
#include <algorithm>

using namespace std;

class Solution {
    long long power(long long base, long long exp, long long mod) {
        long long res = 1;
        base %= mod;
        while (exp > 0) {
            if (exp % 2 == 1) res = (res * base) % mod;
            base = (base * base) % mod;
            exp /= 2;
        }
        return res;
    }

public:
    long long lcmRange(const vector<int>& a, int l, int r, long long MOD) {
        map<int, int> maxExponents;
        
        for (int i = l; i <= r; i++) {
            int num = a[i];
            for (long long p = 2; p * p <= num; p++) {
                if (num % p == 0) {
                    int count = 0;
                    while (num % p == 0) {
                        num /= p;
                        count++;
                    }
                    if (maxExponents.find(p) == maxExponents.end() || count > maxExponents[p]) {
                        maxExponents[p] = count;
                    }
                }
            }
            if (num > 1) {
                if (maxExponents.find(num) == maxExponents.end() || 1 > maxExponents[num]) {
                    maxExponents[num] = 1;
                }
            }
        }
        
        long long ans = 1;
        for (auto const& [p, e] : maxExponents) {
            ans = (ans * power(p, e, MOD)) % MOD;
        }
        return ans;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    long long MOD;
    if (cin >> n >> q >> MOD) {
        vector<int> a(n);
        for (int i = 0; i < n; i++) cin >> a[i];

        Solution solution;
        for (int i = 0; i < q; i++) {
            int l, r;
            cin >> l >> r;
            cout << solution.lcmRange(a, l, r, MOD) << "\n";
        }
    }
    return 0;
}
```

### JavaScript
```javascript
const readline = require("readline");

function power(base, exp, mod) {
  let res = 1n;
  base %= mod;
  while (exp > 0n) {
    if (exp % 2n === 1n) res = (res * base) % mod;
    base = (base * base) % mod;
    exp /= 2n;
  }
  return res;
}

function lcmRange(a, l, r, MOD) {
  const maxExponents = new Map();
  const modBig = BigInt(MOD);
  
  for (let i = l; i <= r; i++) {
    let num = a[i];
    for (let p = 2; p * p <= num; p++) {
      if (num % p === 0) {
        let count = 0;
        while (num % p === 0) {
          num /= p;
          count++;
        }
        const current = maxExponents.get(p) || 0;
        if (count > current) maxExponents.set(p, count);
      }
    }
    if (num > 1) {
      const current = maxExponents.get(num) || 0;
      if (1 > current) maxExponents.set(num, 1);
    }
  }
  
  let ans = 1n;
  for (const [p, e] of maxExponents.entries()) {
    ans = (ans * power(BigInt(p), BigInt(e), modBig)) % modBig;
  }
  
  return ans.toString();
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => {
  const parts = line.trim().split(/\s+/);
  for (let i = 0; i < parts.length; i++) {
    if (parts[i].length > 0) data.push(parts[i]);
  }
});
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const q = parseInt(data[idx++], 10);
  const MOD = parseInt(data[idx++], 10);
  const a = [];
  for (let i = 0; i < n; i++) a.push(parseInt(data[idx++], 10));
  
  const out = [];
  for (let i = 0; i < q; i++) {
    const l = parseInt(data[idx++], 10);
    const r = parseInt(data[idx++], 10);
    out.push(lcmRange(a, l, r, MOD));
  }
  console.log(out.join("\n"));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

Input: `A = [2, 6, 3]`, Query `[0, 1]`.
1. `l=0, r=1`. Range `[2, 6]`.
2. `num=2`: `2^1`. Map: `{2: 1}`.
3. `num=6`: `2^1 * 3^1`. Map: `{2: 1, 3: 1}`.
4. Result: `2^1 x 3^1 = 6`.
5. `6 +/-od10^9+7 = 6`.

## ✅ Proof of Correctness

### Invariant
`lcm(S) = prod p^max(e_p)`.
We iterate all numbers, factorize them, and maintain the max exponent for each prime.

### Why the approach is correct
Fundamental theorem of arithmetic.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Large Ranges.
  - *Hint:* Use Segment Tree where each node stores LCM. Requires merging LCMs (expensive). Or Mo's Algorithm.
- **Extension 2:** GCD of range.
  - *Hint:* Sparse Table / Segment Tree.
- **Extension 3:** LCM of all pairs.
  - *Hint:* `lcm(a, b) = ab/gcd(a, b)`. Summing this is harder.

### Common Mistakes to Avoid

1. **Overflow**
   - ❌ Wrong: `res = res * x` without modulo.
   - ✅ Correct: Use modular arithmetic, but be careful with division (GCD). Map approach avoids division.
2. **Modulo Division**
   - ❌ Wrong: `(a / b) % M`.
   - ✅ Correct: `(a * modInverse(b)) % M`. Only works if `gcd(b, M) = 1`.

## Related Concepts

- **Prime Factorization:** Trial division.
- **Modular Arithmetic:** Power function.
