---
problem_id: BIT_SMALLEST_ABSENT_XOR__8409
display_id: BIT-009
slug: smallest-absent-xor
title: "Smallest Absent XOR"
difficulty: Medium
difficulty_score: 60
topics:
  - Bitwise Operations
  - XOR
  - XOR Basis
  - Linear Algebra
tags:
  - bitwise
  - xor
  - xor-basis
  - hard
  - medium
premium: true
subscription_tier: basic
---

# BIT-009: Smallest Absent XOR

## 📋 Problem Summary

Given an array of integers, consider the set `S` of all possible values that can be formed by XORing a subset of the array. Find the smallest non-negative integer `k` that is **not** in `S`.

## 🌍 Real-World Scenario

**Scenario Title:** The Frequency Gap

You are analyzing a synthesizer that produces frequencies by combining (XORing) base oscillators.
- **Base Oscillators**: You have a set of primary tuning forks with digital signatures `a[0], a[1], ...`.
- **Harmonics**: By activating combinations of these forks, you can generate new signatures. The physics of this digital synth follows XOR addition rules (GF(2) vector space).
- **Gap**: You want to find the lowest "frequency" (numerical value) that this synthesizer *cannot* produce. This gap represents the first limitation of your instrument.

**Why This Problem Matters:**

- **Linear Basis**: Understanding that the span of XOR values forms a vector space.
- **Vector Space Properties**: The "Smallest Missing Value" (MEX) of a subspace measure its completeness.
- **Efficiency**: Reducing $2^N$ subsets to a basis of size $\approx 60$.

![Real-World Application](../images/BIT-009/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Basis Span
```
Array: [10, 5] -> {1010, 0101}
Basis Construction:
- Insert 1010. Basis element for bit 3.
- Insert 0101. Basis element for bit 2.

Span:
0000 (Empty)
1010 (10)
0101 (5)
1111 (15)

Values: {0, 5, 10, 15}.
Smallest Absent:
0? Present.
1? Absent.
Answer: 1.
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input**: Integer array `a`.
- **Subset**: Includes empty subset (value 0). So 0 is always present.
- **Constraints**: Values up to $10^9$. Basis size max 30.

Common interpretation mistake:

- ❌ Checking all $2^N$ subsets.
- ✅ Constructing a **Linear Basis** and analyzing its pivots.

### Core Concept: Smallest Absent is a Power of 2

**Theorem**: The smallest non-negative integer NOT representable by an XOR subset is always a power of 2 ($2^k$).

**Proof**:
The set of reachable values `V` is a vector space over GF(2). It is closed under XOR.
Suppose the smallest missing number `M` is NOT a power of 2.
Then `M` has at least two bits set or is 0. (But 0 is always in `V`, so `M > 0`).
If `M` is not a power of 2, write $M = 2^k + R$ where $2^k$ is the MSB and $0 < R < 2^k$.
Since `M` is the *smallest* missing, both $2^k$ and $R$ must be present in `V` (because they are smaller than `M`).
Since `V` is closed under XOR, $2^k \oplus R$ must be in `V`.
But $2^k \oplus R = M$.
Contradiction. `M` is in `V`.
Therefore, the smallest missing number MUST be a power of 2. Specifically, it is $2^k$ where $k$ is the smallest index such that we *cannot* form a basis vector with MSB $k$.

### Why Naive Approach is too slow

Generating all subsets is O(2^N). N=200,000. Impossible.

## Naive Approach (Set Generation)

### Intuition

Generate all subsets, store in a Set, find MEX.

### Algorithm

1. `reachable = {0}`.
2. For `x` in `a`:
   - `new_vals = {}`
   - For `r` in `reachable`: `new_vals.add(r ^ x)`
   - `reachable.addAll(new_vals)`
3. check `0, 1, 2...`

### Time Complexity

- **O(2^N)**.

### Space Complexity

- **O(2^N)**.

## Optimal Approach (Linear Basis)

### Key Insight

Construct the Linear Basis. A basis is a minimal set of numbers that can generate the same XOR span as the original array.
We maintain an array `basis[30]` where `basis[i]` stores a basis mask whose Highest Set Bit (MSB) is `i`.
If `basis[i]` exists, we can "control" bit `i`.
The smallest missing number is $2^k$ where $k$ is the first index with `basis[k] == 0`.

### Algorithm

1. `basis = array[32]` initialized to 0.
2. For each `x` in `a`:
   - Loop `i` from 30 down to 0:
     - If `(x >> i) & 1`:
       - If `basis[i] == 0`:
         - `basis[i] = x`
         - Break
       - Else:
         - `x ^= basis[i]`
3. Loop `i` from 0 to 31:
   - If `basis[i] == 0`: return `1 << i`
4. Return `1 << 30` (or appropriate limit).

### Time Complexity

- **O(N * 30)**.

### Space Complexity

- **O(30)** (Basis storage).

![Algorithm Visualization](../images/BIT-009/algorithm-visualization.png)
![Algorithm Steps](../images/BIT-009/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input**: `1, 2, 3`.
1. Insert 1 (`01`). Bit 0 set. `basis[0] = 1`.
2. Insert 2 (`10`). Bit 1 set. `basis[1] = 2`.
3. Insert 3 (`11`).
   - Bit 1 set -> `3 ^ basis[1]` = `3 ^ 2 = 1`.
   - Bit 0 set -> `1 ^ basis[0]` = `1 ^ 1 = 0`.
   - 0 -> Redundant.
Basis state: `basis[0]=1`, `basis[1]=2`.
Check:
- `basis[0]` exists? Yes.
- `basis[1]` exists? Yes.
- `basis[2]` exists? No.
Return `1<<2` = 4. Correct.

## ✅ Proof of Correctness

### Invariant

The basis we obtain (`basis[i]`) ensures that we can form any number $X$ in the span if and only if for every bit $i$ where $X$ has a 1, we can reduce that bit using `basis[i]` (possibly modifying lower bits). If `basis[k]` is missing, it implies no combination of basis vectors produces a number with MSB $k$. Thus $2^k$ is not formable. Since all smaller powers of 2 have basis vectors, they are formable.

## 💡 Interview Extensions (High-Value Add-ons)

- **Max XOR**: Finding max XOR using the same basis.
- **K-th Smallest XOR**: Reconstruct basis to Reduced Row Echelon Form.

## Common Mistakes to Avoid

1. **Order of Insertion**:
   - ❌ Sorting array first? Not needed.
   - ✅ Order irrelevant for span properties.
2. **Result Size**:
   - ❌ Returning `int` when answer could be $2^{31}$. Use `long/BigInt`.

## Related Concepts

- **Gaussian Elimination**: The algorithm is effectively Gaussian elimination over GF(2).
- **Matroid Theory**: Independent sets.
