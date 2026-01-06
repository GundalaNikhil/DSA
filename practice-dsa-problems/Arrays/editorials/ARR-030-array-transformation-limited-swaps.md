---
problem_id: ARR_LIMITED_SWAPS__6732
display_id: ARR-030
slug: array-transformation-limited-swaps
title: "Array Transformation with Limited Swaps"
difficulty: Medium
difficulty_score: 45
topics:
  - Arrays
tags:
  - algorithms
  - array-manipulation
  - arrays
  - coding-interviews
  - data-structures
  - greedy
  - inversion-count
  - searching
  - sequence-alignment
  - technical-interview-prep
  - two-pointers
premium: false
subscription_tier: basic
---

# ARR-030: Array Transformation with Limited Swaps

## 📋 Problem Summary

Given two arrays $A$ and $B$ (both of length $n$) and a budget of $K$ operations, your task is to determine if $A$ can be transformed into $B$. The only allowed operation is **swapping two adjacent elements** in $A$.

**Core Objectives:**

1. Determine if $A$ and $B$ contain the same numbers (multiset equality).
2. If they do, calculate the minimum number of adjacent swaps needed to rearrange $A$ to match $B$.
3. Check if this minimum number is $\le K$.

**Constraints Note:** $K$ can be as large as $10^{12}$, while $n$ is up to $200,000$. This implies we need an efficient way to count swaps without actually performing them.

## 🌍 Real-World Scenarios

**Scenario 1: 🧩 Automated Warehouse Bot**
A warehouse has a row of storage bins. A robot can move one bin past its neighbor at a time (adjacent swap). If the bins are in state $A$ and need to be in state $B$ for optimal shipping, can the robot complete the reorganization within its battery life (represented by $K$ moves)?

**Scenario 2: 🧱 DNA Sequence Alignment**
Scientists are comparing two DNA strands where sections have been transposed. They want to know the minimum "evolutionary distance" in terms of single-displacement mutations required to make the strands identical.

**Scenario 3: 🚦 Traffic Management**
A line of autonomous vehicles needs to change order for a specific highway exit. Swapping lanes between non-adjacent cars is risky. If each adjacent lane-swap has a time cost, can the convoy reach the desired configuration before the exit window closes?

**Scenario 4: 🚆 Train Shunting Yard**
Rail cars on a single track need to be reordered. Because of track physics, cars can only be moved past one another if they are adjacent. If the engine has limited fuel ($K$), can it achieve the target formation?

### Real-World Relevance

The "Swap Distance" or "Kendall Tau Distance" is a fundamental metric in statistics and computer science for measuring the dissimilarity between two rankings or sequences. It represents the number of pairwise disagreements between two permutations.

## 🚀 Detailed Explanation

### 1. The Adjacent Swap / Inversion Relationship

A key theorem in combinatorics states: **The minimum number of adjacent swaps needed to transform one permutation into another is equal to the number of inversions.**

An inversion is a pair of indices $(i, j)$ such that $i < j$ but the element that should come later appears earlier in the current sequence.

### 2. Handling Duplicate Values (The Greedy Map)

When $A$ and $B$ have duplicate values, the problem becomes: "Which specific `1` in $A$ should go to which specific `1` in $B$?"

**The Matching Rule:** The $p$-th occurrence of a value $x$ in $A$ should always map to the $p$-th occurrence of $x$ in $B$.
_Proof Sketch:_ Crossing two identical values (sending the first `1` to the second position and the second `1` to the first) requires more swaps without changing the final result. To minimize swaps, we preserve the relative order of identical elements.

### 3. Transformation to a Permutation Problem

To apply inversion counting, we need to map $A$ into a permutation of $0$ to $n-1$:

1. Check if $A$ and $B$ are multisets. If counts of any number differ, return `NO`.
2. For each distinct value in $B$, record the list of indices where it appears.
3. For each value in $A$, assign it the next available target index from $B$'s records.
4. This results in an array $P$ where $P[i]$ is the index in $B$ where $A[i]$ should eventually land.
5. If $A$ can be transformed into $B$, $P$ will be a permutation of $\{0, 1, \dots, n-1\}$.

**Example:**
$A = [1, 2, 1, 3], B = [1, 1, 2, 3]$

- $B$ occurrences: `1: [0, 1]`, `2: [2]`, `3: [3]`
- $A[0]=1 \rightarrow 0$ (first 1)
- $A[1]=2 \rightarrow 2$
- $A[2]=1 \rightarrow 1$ (second 1)
- $A[3]=3 \rightarrow 3$
- **Permutation $P$:** $[0, 2, 1, 3]$

### 4. Efficient Inversion Counting

A naive inversion count takes $O(n^2)$. With $n=200,000$, we must use $O(n \log n)$:

- **Fenwick Tree (BIT) Approach:**
  1. Iterate through $P$ from right to left.
  2. For each $P[i]$, count how many elements smaller than $P[i]$ have already been seen (this is a prefix sum in the BIT).
  3. Add $P[i]$ to the BIT.
  4. The count of smaller elements seen so far is the number of inversions for that element.

### 🔄 Algorithm Flow Diagram

```mermaid
flowchart TD
    Start([Start]) --> Multiset{Multiset Equality?}
    Multiset -- No --> NO([Return NO])
    Multiset -- Yes -- > Map[B indices: Map Val to Queue of Indices]

    Map --> BuildP[Build Permutation P:<br>P_i = Map A_i .pop()]
    BuildP --> Inv[Count Inversions in P<br>using Fenwick Tree or Merge Sort]

    Inv --> Compare{Inversions <= K?}
    Compare -- Yes --> YES([Return YES])
    Compare -- No --> NO2([Return NO])
```

## 🔍 Complexity Analysis

### Time Complexity: $O(N \log N)$

- **Multiset Check:** $O(N \log N)$ using sorting or $O(N)$ using hashing.
- **Mapping:** $O(N)$ using hash maps and queues.
- **Inversion Counting:** $O(N \log N)$ using a Fenwick Tree or Merge Sort.
- Since $N = 200,000$, $N \log N \approx 3.6 \times 10^6$, which is well within performance limits.

### Space Complexity: $O(N)$

- We store the mapping queues ($N$ total entries).
- We store the generated permutation $P$ ($N$ integers).
- The Fenwick Tree requires $O(N)$ space.

## 🧪 Edge Cases & Testing

### 1. Already Balanced ($A = B$)

- **Input:** $A=[1, 2, 3], B=[1, 2, 3], K=0$
- **Expectation:** `YES`. Inversion count should be exactly 0.

### 2. Multisets Differ

- **Input:** $A=[1, 2, 1], B=[1, 2, 2]$
- **Expectation:** `NO`. No amount of swaps can change the "identity" of the elements.

### 3. $K=0$

- **Input:** $A=[2, 1], B=[1, 2], K=0$
- **Expectation:** `NO`. Even though transformation is possible, we have no "budget" for swaps.

### 4. Reversed Array

- **Input:** $A=[3, 2, 1], B=[1, 2, 3], K=2$
- **Expectation:** `NO`. Minimum swaps to reverse $[1, 2, 3]$ is $3$ ($n(n-1)/2$). $3 > 2$.

### 5. Large $K$

- **Input:** $n=200,000, K=10^{12}$
- **Logic:** $K$ can be much larger than the maximum possible inversions ($n^2/2 \approx 2 \times 10^{10}$). The logic must use `long long` integers for the counter to avoid overflow.

### 6. Many Identical Elements

- **Input:** $A=[1, 1, 1, 1], B=[1, 1, 1, 1]$
- **Expectation:** `YES`. Greedy matching ensures 0 swaps are used.

## ⚠️ Common Pitfalls & Debugging

**1. Integer Overflow**

- **Pitfall:** Using a 32-bit `int` to store the inversion count.
- **Consequence:** Inversions can exceed $2 \times 10^{10}$. A 32-bit signed integer maxes at $\sim 2 \times 10^9$.
- **Fix:** Use a 64-bit integer type (`long` in Java/CS, `long long` in C++, `int` in Python 3).

**2. Direct Value Comparison in BIT**

- **Pitfall:** Trying to use the raw values of $A_i$ as indices in a Fenwick Tree.
- **Consequence:** $A_i$ can be $10^9$. You cannot create an array of size $10^9$.
- **Fix:** Map the values to a permutation $0 \dots n-1$ as described in the explanation first. The Fenwick Tree will then only need a size of $N$.

**3. Ignoring Multiset Equality**

- **Pitfall:** Jumping straight to inversion counting.
- **Consequence:** If $A$ and $B$ don't have the same elements, your mapping logic will crash or return a garbage permutation.
- **Fix:** Validate counts/sorting first.

**4. 0-based vs 1-based indexing in BIT**

- Fenwick Trees are traditionally 1-based. If your permutation $P$ contains a $0$, you must add $1$ before calling `update` or `query` on the Fenwick Tree.

## 🎯 Variations & Extensions

### Variation 1: Minimum Cost Swaps

Instead of "total swaps $\le K$", each pair $(A_i, A_j)$ has a specific cost to swap.
_Solution: Usually involves Weighted Inversions or Min-Cost Flow._

### Variation 2: Non-Adjacent Swaps

If you can swap _any_ two elements, the distance is $n - (\text{number of cycles in the permutation})$.
_Application: Cycle Decomposition._

### Variation 3: Circular Adjacent Swaps

If the array is a circle, you can swap $A[n-1]$ and $A[0]$.
_Solution: Requires testing different "rotation" offsets._

### Variation 4: Multiple Target Arrays

Given $A$, which of $B_1, B_2, \dots, B_m$ is the "closest" in terms of adjacent swaps?

### Variation 5: Limited Swap Budget Sorting

Sort an array $A$ greedily using at most $K$ adjacent swaps to get the **lexicographically smallest** result.
_Application: String manipulation with budget._

## 🎓 Key Takeaways

1. **Distance Metric:** Adjacent swap count = Inversion count.
2. **Greedy Matching:** Preserve relative order of duplicates to minimize effort.
3. **Efficiency:** $O(N \log N)$ is required for $N > 10^4$. Use Fenwick Tree or Merge Sort.
4. **Permutation Mapping:** Convert value-based problems into index-based problems to simplify logic.

## 📚 Related Problems

- **Count Inversions:** The basic building block.
- **Bubble Sort Swaps:** Identical logic.
- **Kendall Tau Distance:** Statistical term for this problem.
- **Minimum Swaps to Sort:** Non-adjacent version.
- **ARR-031:** Online Array with Rollbacks.
