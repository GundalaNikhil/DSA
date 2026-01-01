---
problem_id: NUM_MODULAR_EXPONENT_DIGIT_STREAM__9056
display_id: NUM-009
slug: modular-exponent-digit-stream
title: "Modular Exponent With Digit Stream"
difficulty: Medium
difficulty_score: 50
topics:
  - Number Theory
  - Modular Exponentiation
  - Big Integers
tags:
  - number-theory
  - modular
  - exponentiation
  - medium
premium: true
subscription_tier: basic
---

# NUM-009: Modular Exponent With Digit Stream

## 📋 Problem Summary

Compute `a^e +/-od m`, where the exponent `e` is a very large number given as a string of decimal digits.
- Input: Integers `a, m`, string `e`.
- Output: `a^e +/-od m`.

## 🌍 Real-World Scenario

**Scenario Title:** The Secure Token Generator

You are designing a secure authentication system where user tokens are generated using a specialized hashing algorithm involving modular exponentiation.
- The exponent `e` is derived from a user's biometric data stream, resulting in a number with thousands of digits.
- You need to compute `a^e +/-od m` to verify the token.
- Standard integer types cannot store `e`, so you must process the digits of `e` sequentially as they arrive from the biometric scanner.

**Why This Problem Matters:**

- **Cryptography:** RSA decryption involves `c^d +/-od n` where `d` is huge.
- **Big Data:** Processing streams of data to form a single hash.
- **Algorithm Design:** Handling inputs larger than memory limits.

![Real-World Application](../images/NUM-009/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Stream Processing

Exponent `e = "123"`.
Base `a`, Mod `m`.

```
Step 1: Process '1'
Current Exponent Val: 1
Result: a^1 mod m

Step 2: Process '2'
Current Exponent Val: 12 = 1 * 10 + 2
Result: (a^1)^10 * a^2 = a^10 * a^2 = a^12 mod m

Step 3: Process '3'
Current Exponent Val: 123 = 12 * 10 + 3
Result: (a^12)^10 * a^3 = a^120 * a^3 = a^123 mod m
```

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Constraints:** `|e| <= 100,000`. This means `e ~= 10^100000`.
- **Euler's Theorem:** We could compute `e +/-odphi(m)` to reduce the exponent, but calculating `phi(m)` requires factorization, which is hard for large `m`.
- **Direct Approach:** It's better to process digits left-to-right using the property `a^10x + d = (a^x)^10 * a^d`.

### Core Concept: Modular Exponentiation Property

`a^10x + d = (a^x)^10 * a^d +/-od m`.
We maintain the current value `res` corresponding to the prefix of digits processed so far.
For each new digit `d`:
`res = power(res, 10, m) * power(a, d, m) % m`.

## Naive Approach

### Intuition

Convert string `e` to BigInteger and use built-in `modPow`.

### Algorithm

- Python: `pow(a, int(e), m)`.
- Java: `BigInteger`.
- C++: No built-in BigInt.

### Limitations

- While Python/Java handle this easily, understanding the underlying algorithm is crucial for C++ or constrained environments.
- Also, converting a `10^5` digit string to BigInt might be slower than processing it on the fly.

## Optimal Approach

### Key Insight

Process the string character by character.
Initialize `res = 1` (representing `a^0`).
Let's trace:
`e = d_0 d_1 dots d_k`.
Value `V_0 = d_0`.
`V_i = V_i-1 * 10 + d_i`.
We want `a^V_k +/-od m`.
Let `R_i = a^V_i +/-od m`.
`R_i = a^10 V_i-1 + d_i = (a^V_i-1)^10 * a^d_i = (R_i-1)^10 * a^d_i +/-od m`.
Base case: `R_-1 = a^0 = 1`. Then `R_0 = (1)^10 * a^d_0 = a^d_0`.

### Algorithm

1. Initialize `ans = 1`.
2. For each digit `c` in `e`:
   - Convert `c` to integer `d`.
   - `ans = power(ans, 10, m)`.
   - `ans = (ans * power(a, d, m)) % m`.
3. Return `ans`.

### Time Complexity

- **O(|e| \cdot \log m)**.
- Each step involves a constant number of modular multiplications (computing power 10 and power `d <= 9`).
- Total operations `~= 10^5 x 30`, very fast.

### Space Complexity

- **O(1)**.

![Algorithm Visualization](../images/NUM-009/algorithm-visualization.png)
![Algorithm Steps](../images/NUM-009/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

Input: `a=3, m=7, e="5"`.
1. `ans = 1`.
2. Digit '5':
   - `ans = 1^10 = 1`.
   - `term = 3^5 mod 7`.
   - `3^1=3, 3^2=2, 3^3=6, 3^4=4, 3^5=5`.
   - `ans = 1 * 5 = 5`.
3. Result 5.

Input: `a=2, m=100, e="12"`.
1. `ans = 1`.
2. Digit '1':
   - `ans = 1^10 = 1`.
   - `term = 2^1 = 2`.
   - `ans = 2`.
3. Digit '2':
   - `ans = 2^10 = 1024 = 24 mod 100`.
   - `term = 2^2 = 4`.
   - `ans = 24 * 4 = 96`.
4. Check: `2^12 = 4096 equiv 96 +/-od100`. Correct.

## ✅ Proof of Correctness

### Invariant
At step `i`, `ans` holds `a^prefix_i +/-od m`.
Transition: `a^10P + d = (a^P)^10 * a^d`.

### Why the approach is correct
Follows directly from exponentiation laws.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Reduce exponent using Euler's Theorem.
  - *Hint:* If we can compute `phi(m)`, we can reduce `e` modulo `phi(m)`. This is useful if `a` is huge too or if we want canonical form.
- **Extension 2:** `a` is also a large string.
  - *Hint:* Compute `a +/-od m` first.
- **Extension 3:** Tower of powers `a^b^c`.
  - *Hint:* Compute exponent modulo `phi(m)`, then that exponent modulo `phi(phi(m))`, etc.

### Common Mistakes to Avoid

1. **String Parsing**
   - ❌ Wrong: Parsing entire string to int (overflows in C++/Java).
   - ✅ Correct: Process char by char.
2. **Modulo Arithmetic**
   - ❌ Wrong: Forgetting modulo at any step (intermediate values explode).
   - ✅ Correct: Modulo after every multiplication.

## Related Concepts

- **Horner's Method:** Evaluating polynomials (this is essentially evaluating the exponent value polynomial `d_0 10^k + dots`).
- **Modular Exponentiation:** Binary exponentiation (used for the small powers).
