---
problem_id: HSH_TWO_STRING_CONCAT_EQUAL__4156
display_id: HSH-010
slug: two-string-concat-equal
title: "Two-String Concatenation Equal Check"
difficulty: Medium
difficulty_score: 45
topics:
  - Hashing
  - String Algorithms
tags:
  - hashing
  - concatenation
  - medium
premium: true
subscription_tier: basic
---

# HSH-010: Two-String Concatenation Equal Check

## 📋 Problem Summary

You are given four strings: `a`, `b`, `c`, and `d`. Determine if the concatenation `a + b` is equal to `c + d`.
The catch is to do this efficiently without explicitly creating the large concatenated strings (though for `N=10^5`, explicit creation is feasible, the goal is to learn the hashing technique).

## 🌍 Real-World Scenario

**Scenario Title:** Database Sharding Verification

Imagine you have a distributed database where data is split (sharded) across different servers.

- Server 1 has part `a` and part `b`.
- Server 2 has part `c` and part `d`.
- You want to verify if the combined data on Server 1 (`a+b`) is identical to the combined data on Server 2 (`c+d`) without transferring the full strings over the network.
- You can compute the hash of `a` and `b` locally, combine them mathematically, and send only the small hash value to compare with Server 2's combined hash.

![Real-World Application](../images/HSH-010/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concatenation Hash

String A: "ab" (Hash `H_A`, Len 2)
String B: "cd" (Hash `H_B`, Len 2)

Combined "abcd":
`H_AB = H_A x B^Len_B + H_B`

```text
Hash("ab") = 'a'*B + 'b'
Hash("cd") = 'c'*B + 'd'

Hash("abcd") = 'a'*B^3 + 'b'*B^2 + 'c'*B^1 + 'd'*B^0
             = ('a'*B + 'b') * B^2 + ('c'*B + 'd')
             = H_A * B^2 + H_B
```

### Key Concept: Mathematical Concatenation

We don't need to physically join strings to know their combined hash.
If we know `Hash(S_1)` and `Hash(S_2)`, then:

`Hash(S_1 + S_2) = (Hash(S_1) x Base^|S_2| + Hash(S_2)) +/-od M`

This allows `O(1)` combination if we have precomputed powers.

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** Four strings `a`, `b`, `c`, `d`.
- **Output:** Boolean `true` or `false`.
- **Constraints:** Lengths up to `10^5`.
- **Note:** Standard string concatenation in Java/Python/C++ takes linear time `O(|a|+|b|)`. This is acceptable here, but the hashing approach is `O(|a|+|b|)` to compute hashes initially and then `O(1)` to check any combination.

## Naive Approach

### Intuition

Create `s1 = a + b`, `s2 = c + d`. Compare `s1.equals(s2)`.

### Time Complexity

- **O(N)**: String creation and comparison.
- **Space:** `O(N)` to store new strings.

## Optimal Approach (Hashing)

### Key Insight

Compute hashes of `a`, `b`, `c`, `d` individually.
Combine them using the formula:
`H_AB = (H_A x B^|b| + H_B) +/-od M`
`H_CD = (H_C x B^|d| + H_D) +/-od M`
Compare `H_AB` and `H_CD`.
Also check if total lengths match: `|a|+|b| == |c|+|d|`.

### Algorithm

1. Compute `H_A, H_B, H_C, H_D`.
2. Compute `P_|b| = B^|b| +/-od M`.
3. Compute `P_|d| = B^|d| +/-od M`.
4. Calculate combined hashes.
5. Compare.

### Time Complexity

- **O(N)**: To compute initial hashes.
- **Space:** `O(1)`.

![Algorithm Visualization](../images/HSH-010/algorithm-visualization.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:**

```
ab
cd
a
bcd
```

**Hashes:**

- `H("ab")`. `H("cd")`.
- `H("a")`. `H("bcd")`.

**Combine:**

- `H_AB = H("ab") x B^2 + H("cd")`.
- `H_CD = H("a") x B^3 + H("bcd")`.

**Result:**

- Both represent "abcd".
- Hashes match. Return `true`.

## ✅ Proof of Correctness

### Invariant

`Hash(S_1 + S_2) = Hash(S_1) x B^|S_2| + Hash(S_2)`.
This is derived directly from the polynomial definition of rolling hash.
If `H_AB == H_CD` and lengths match, strings are equal (with high probability).

## 💡 Interview Extensions

- **Extension 1:** Check if `A+B+C == D+E`.
  - _Answer:_ Generalize the formula. `((H_A B^|B| + H_B) B^|C| + H_C)`.
- **Extension 2:** Given a list of strings, find two that concatenate to form a palindrome.
  - _Answer:_ Use hashing to check palindrome property efficiently.

### Common Mistakes to Avoid

1. **Length Mismatch**
   - ❌ Wrong: Ignoring length check. Hash collision possible if lengths differ (though rare with polynomial hash if implemented correctly, but good practice).
   - ✅ Correct: Check `len(a)+len(b) == len(c)+len(d)` first.
2. **Power Calculation**
   - ❌ Wrong: Linear loop for power.
   - ✅ Correct: Modular exponentiation (`O(log N)`) or precomputed array.

## Related Concepts

- **Rabin-Karp:** Uses this rolling property.
- **Merkle Trees:** Combine hashes of blocks to verify data integrity.
