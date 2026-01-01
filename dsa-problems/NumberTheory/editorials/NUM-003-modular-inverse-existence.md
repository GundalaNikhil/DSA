---
problem_id: NUM_MODULAR_INVERSE_EXISTENCE__3507
display_id: NUM-003
slug: modular-inverse-existence
title: "Modular Inverse Existence"
difficulty: Easy
difficulty_score: 22
topics:
  - Number Theory
  - GCD
  - Modular Arithmetic
tags:
  - number-theory
  - gcd
  - modular
  - easy
premium: true
subscription_tier: basic
---

# NUM-003: Modular Inverse Existence

## 📋 Problem Summary

Given pairs `(a, m)`, determine if `a` has a modular multiplicative inverse modulo `m`.
- Input: Multiple queries `(a, m)`.
- Output: `true` if inverse exists, `false` otherwise.
- Condition: Inverse exists `iff gcd(a, m) = 1`.

## 🌍 Real-World Scenario

**Scenario Title:** The Scrambled Message Decrypter

In many encryption schemes (like Affine Cipher), a message is encrypted by multiplying the numeric value of each character by a key `a` modulo `m` (where `m` is the alphabet size).
- To decrypt the message, you need to multiply by the **inverse** of `a`.
- If `a` does not have an inverse modulo `m`, the encryption is irreversible (information is lost), and the message cannot be uniquely decoded.
- Before accepting an encryption key `a`, the system must verify that it is valid (i.e., has an inverse).

**Why This Problem Matters:**

- **Cryptography:** RSA and Elliptic Curve Cryptography rely heavily on modular inverses.
- **Hashing:** Ensuring hash functions are reversible or have specific properties.
- **Algebra:** Fundamental concept in group theory (units in ring `mathbbZ_m`).

![Real-World Application](../images/NUM-003/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: GCD and Inverse

We want to solve `ax equiv 1 +/-od m`.
This is equivalent to finding integers `x, y` such that `ax + my = 1`.
By Bezout's Identity, such `x, y` exist if and only if `gcd(a, m)` divides 1.
Since GCD is always positive, this means `gcd(a, m) = 1`.

```
Example: a=4, m=7
gcd(4, 7) = 1
Inverse exists. (4 * 2 = 8 = 1 mod 7)

Example: a=4, m=6
gcd(4, 6) = 2
2 does not divide 1.
Inverse does not exist.
(4*1=4, 4*2=8=2, 4*3=12=0, ...) -> Never 1.
```

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Constraints:** `Q <= 100,000`, `a, m <= 10^9`.
- **Efficiency:** We need an algorithm faster than `O(m)`. The Euclidean algorithm is `O(log(min(a, m)))`, which is extremely fast.
- **Output:** Boolean string "true" or "false".

### Core Concept: Euclidean Algorithm

The Euclidean algorithm efficiently computes the greatest common divisor (GCD) of two numbers.
`gcd(a, b) = gcd(b, a +/-od b)`.
Base case: `gcd(a, 0) = a`.

## Naive Approach

### Intuition

Try every number `x` from `1` to `m-1` and check if `(a * x) +/-od m = 1`.

### Algorithm


### Time Complexity

- **O(m)** per query. With `m=10^9`, this is impossible.

### Space Complexity

- **O(1)**.

## Optimal Approach

### Key Insight

Use the property: Inverse exists `iff gcd(a, m) = 1`.

### Algorithm

1. Implement `gcd(a, b)` using Euclidean algorithm.
2. For each query `(a, m)`, check if `gcd(a, m) == 1`.
3. Return result.

### Time Complexity

- **O(\log(\min(a, m)))** per query.
- Total: `O(Q log m)`.
- For `10^9`, `log m ~= 30`. Total ops `~= 3 * 10^6`, well within time limit.

### Space Complexity

- **O(1)**.

![Algorithm Visualization](../images/NUM-003/algorithm-visualization.png)
![Algorithm Steps](../images/NUM-003/algorithm-steps.png)

## Implementations

### Java
```java
import java.util.*;

class Solution {
    private long gcd(long a, long b) {
        while (b != 0) {
            long temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

    public boolean hasInverse(long a, long m) {
        return gcd(a, m) == 1;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int q = sc.nextInt();
            Solution solution = new Solution();
            for (int i = 0; i < q; i++) {
                long a = sc.nextLong();
                long m = sc.nextLong();
                System.out.println(solution.hasInverse(a, m) ? "true" : "false");
            }
        }
        sc.close();
    }
}
```

### Python
```python
import math

def has_inverse(a: int, m: int) -> bool:
    if m <= 0: return False
    return math.gcd(a, m) == 1

def main():
    import sys
    input_data = sys.stdin.read().strip().split()
    if not input_data: return
    q = int(input_data[0])
    idx = 1
    results = []
    for _ in range(q):
        a = int(input_data[idx])
        m = int(input_data[idx+1])
        idx += 2
        results.append("true" if has_inverse(a, m) else "false")
    print("\n".join(results))

if __name__ == "__main__":
    main()
```

### C++
```cpp
#include <iostream>
#include <numeric>

using namespace std;

class Solution {
    long long gcd(long long a, long long b) {
        while (b) {
            a %= b;
            swap(a, b);
        }
        return a;
    }

public:
    bool hasInverse(long long a, long long m) {
        return gcd(a, m) == 1;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    if (cin >> q) {
        Solution solution;
        for (int i = 0; i < q; i++) {
            long long a, m;
            cin >> a >> m;
            cout << (solution.hasInverse(a, m) ? "true" : "false") << "\n";
        }
    }
    return 0;
}
```

### JavaScript
```javascript
const readline = require("readline");

function gcd(a, b) {
  while (b !== 0) {
    let temp = b;
    b = a % b;
    a = temp;
  }
  return a;
}

function hasInverse(a, m) {
  return gcd(a, m) === 1;
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
  const q = parseInt(data[idx++], 10);
  const out = [];
  for (let i = 0; i < q; i++) {
    const a = parseInt(data[idx++], 10);
    const m = parseInt(data[idx++], 10);
    out.push(hasInverse(a, m) ? "true" : "false");
  }
  console.log(out.join("\n"));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

Input: `a=4, m=7`.
1. `gcd(4, 7)`:
   - `4 % 7 = 4` -> `gcd(7, 4)`
   - `7 % 4 = 3` -> `gcd(4, 3)`
   - `4 % 3 = 1` -> `gcd(3, 1)`
   - `3 % 1 = 0` -> `gcd(1, 0)`
   - Returns 1.
2. `1 == 1` -> `true`.

Input: `a=4, m=6`.
1. `gcd(4, 6)`:
   - `4 % 6 = 4` -> `gcd(6, 4)`
   - `6 % 4 = 2` -> `gcd(4, 2)`
   - `4 % 2 = 0` -> `gcd(2, 0)`
   - Returns 2.
2. `2 == 1` -> `false`.

## ✅ Proof of Correctness

### Invariant
The Euclidean algorithm correctly computes the GCD.
The theorem states `a^-1 +/-od m` exists `iff gcd(a, m) = 1`.

### Why the approach is correct
Direct application of number theory basics.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Find the inverse if it exists.
  - *Hint:* Use Extended Euclidean Algorithm to find `x, y` such that `ax + my = 1`. Then `x` is the inverse.
- **Extension 2:** Solve `ax equiv b +/-od m`.
  - *Hint:* Solvable iff `gcd(a, m)` divides `b`.
- **Extension 3:** Inverse modulo prime `p`.
  - *Hint:* Use Fermat's Little Theorem: `a^p-2 +/-od p`.

### Common Mistakes to Avoid

1. **Recursion Depth**
   - ❌ Wrong: In languages without tail-call optimization, deep recursion for GCD might stack overflow (rare for GCD since depth is log, but possible in other recursions).
   - ✅ Correct: Iterative GCD is safer and standard.
2. **Large Inputs**
   - ❌ Wrong: Using 32-bit int for `10^9` inputs might overflow during intermediate steps in some languages (though GCD doesn't grow).
   - ✅ Correct: Use `long` / `long long` to be safe.

## Related Concepts

- **Extended Euclidean Algorithm:** Finds the coefficients `x, y`.
- **Fermat's Little Theorem:** Alternative way to find inverse modulo prime.
- **Euler's Theorem:** Generalization for non-primes.
