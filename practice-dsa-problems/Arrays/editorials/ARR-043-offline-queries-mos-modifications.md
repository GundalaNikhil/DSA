---
problem_id: ARR_MOS_UPDATES__6120
display_id: ARR-043
slug: offline-queries-mos-modifications
title: "Offline Queries with Mo's and Modifications"
difficulty: Hard
difficulty_score: 70
topics:
  - Arrays
tags:
  - algorithms
  - array-manipulation
  - arrays
  - coding-interviews
  - data-structures
  - offline-processing
  - range-queries
  - searching
  - square-root-decomposition
  - technical-interview-prep
  - two-pointers
premium: false
subscription_tier: basic
---

# ARR-043: Offline Queries with Mo's and Modifications

## 📋 Problem Summary

You are given an array and asked to maintain its state while performing two types of operations:

1. **Update ($U \ i \ x$):** Modify element $a[i]$ to value $x$.
2. **Query ($Q \ l \ r$):** Calculate a specific "score" for the range $[l, r]$.

**Score Formula:**
$$\text{Score} = \sum_{\text{distinct } v} (\text{value } v) \times (\text{frequency of } v)^2$$

**The Constraint:** This must be done efficiently despite updates and queries mixed together. Since the problem allows an **offline** solution (all operations are given up front), we can use a modified version of **Mo's Algorithm**.

## 🌍 Real-World Scenarios

**Scenario 1: 📊 Dynamic E-commerce Analytics Dashboard**
A store manager views a "Popularity Power" score for products. The score heavily weights products that appear multiple times in a customer's journey (using $\text{freq}^2$). Prices (values) change, and the manager often looks at different time windows. They upload a batch of changes and queries at once.

**Scenario 2: 🧬 Genomic Sequence Variation Analysis**
Researchers analyze segments of a DNA sequence. They assign a "Dominance Score" to specific base pairs based on their local density. As the sequence model is refined (updates), they need to recount the dominance score in various regions (queries).

**Scenario 3: 🔋 Smart Grid Load Balancing**
An electrical grid records usage pulses. The "Stress Score" is the sum of (Voltage $\times$ $\text{PulseCount}^2$). Technicians update historical readings when calibration errors are found and query specific segments of the day to identify overload risks.

**Scenario 4: 🔊 Real-Time Audio Pattern Recognition**
An audio processor calculates the energy of different frequency bins using a sliding window. It "updates" the background noise profile and "queries" frequency ranges to detect specific patterns (like a voice or a alarm).

**Scenario 5: 📑 Distributed Ledger Corrective Auditing**
A blockchain auditor processes a batch of transaction corrections and balance queries. The score identifies "Centralized Risk" where one account holds a significant, repeated portion of the transaction volume.

### Real-World Relevance

Standard range queries are usually handled by Segment Trees. However, the $\text{Freq}^2$ metric is non-linear and doesn't "merge" easily in a tree structure. Mo's Algorithm is the "Swiss Army Knife" for problems where the metric can be updated easily when adding/removing a single element.

## 🚀 Detailed Explanation

### 1. The 3D Coordinate Space

In standard Mo's, we move in 2D space $(L, R)$. With updates, we add a third dimension: **Time ($T$)**.

- $L$: Left boundary of the query.
- $R$: Right boundary of the query.
- $T$: How many updates have occurred before this query.

Every query is now a point $(L, R, T)$ in 3D space. Our Goal: Find a path through all query points that minimizes the total distance traveled.

### 2. Sorting Logic (3D Block Sorting)

We divide the array into blocks of size $B = n^{2/3}$.
We sort the queries by:

1.  **Block of $L$:** `L / B`
2.  **Block of $R$:** `R / B`
3.  **Time $T$:** Increasing (or alternating for a small speed boost).

### 3. The Update Mechanism

When moving the $T$ pointer:

- **Move Forward ($T \to T+1$):** Apply the $(T+1)$-th update.
- **Move Backward ($T \to T-1$):** Revert the $T$-th update.

**Crucial Logic:** An update at index $i$ only changes the current score if index $i$ is currently inside the window $[L, R]$.

1. If $i \in [L, R]$: Remove the old value's contribution, update the array, and add the new value's contribution.
2. If $i \notin [L, R]$: Just update the value in the underlying array so the next time the $L$ or $R$ pointers pass over $i$, they see the correct value.

### 4. Coordinate Compression

Since $a_i$ can be $10^9$ and only $400,000$ distinct values exist (Initial array + up to $Q$ updates), we must map all values into the range $[1, 2N+Q]$ using a hash map or sorting, so we can use a simple array for frequencies.

### 🔄 Algorithm Flow Diagram

```mermaid
flowchart TD
    Start([Start]) --> Comp[Extract all initial and update values<br>Coordinate Compress to 1..K]
    Comp --> Block[Set Block Size B = N^2/3]
    Block --> Sort[Sort Queries by L-Block, R-Block, then Time T]

    Sort --> Init[CurL=1, CurR=0, CurT=0, curScore=0]
    Init --> QueryLoop{For each Query Q_i}

    QueryLoop -- Next --> AdjT[Move CurT to Q_i.T:<br>If index in [CurL, CurR], update score]
    AdjT --> AdjL[Move CurL to Q_i.L:<br>Add/Remove from score]
    AdjL --> AdjR[Move CurR to Q_i.R:<br>Add/Remove from score]

    AdjR --> Save[Store Answer for Q_i]
    Save --> QueryLoop

    QueryLoop -- Done --> End([Print results in original order])
```

## 🔍 Complexity Analysis

### Time Complexity: $O(N^{5/3})$

This looks scary, but let's derive it. Let $B$ be the block size.

- **T Move:** For each $(L_{block}, R_{block})$ pair (there are $(N/B)^2$ pairs), $T$ moves at most $Q$ times. Total: $O((N/B)^2 \cdot Q)$.
- **R Move:** Within one $L_{block}$, $R$ moves at most $N$ for each $L$-block. Total: $O((N/B) \cdot N \cdot (??))$. More accurately, $R$ moves $B$ times per query and $N$ times per $L_{block}$ reset.
- **L Move:** Moves $B$ times per query. Total: $O(Q \cdot B)$.

Setting $B = N^{2/3}$ minimizes this to **$O(N^{5/3})$**.
For $N=200,000$: $N^{5/3} \approx 6.8 \times 10^8$.
_Note:_ This is a tight fit for 2 seconds. In competitive programming, you must use a very efficient `add` and `remove` function.

### Space Complexity: $O(N + Q)$

- We store the array, the updates, the queries, and the frequency array.
- All are linear with respect to $N$ and $Q$.

## 🧪 Edge Cases & Testing

### 1. Update at the Boundary

- If an update happens at index $L$ or $R$, make sure the `add`/`remove` logic precisely accounts for the presence/absence of that element.

### 2. No Queries or No Updates

- If there are no updates, the Time pointer stays at 0. The complexity reduces toward standard Mo's (though the $N^{5/3}$ sort is still used).

### 3. All Queries in the Same Range

- The $T$ pointer will move monotonically, visiting each update once.

### 4. Large Values

- Handled by Coordinate Compression.

### 5. Window size 1

- `sum(val * 1^2) = val`.

## ⚠️ Common Pitfalls & Debugging

**1. Poor Block Size Selection**

- **Pitfall:** Using $\sqrt{N}$.
- **Consequence:** 3D Mo's with $B=\sqrt{N}$ is much slower than $B=N^{2/3}$.
- **Fix:** Use $N^{2/3}$, or better yet, manually tune $B$ (around 2000-3000 for $N=200,000$).

**2. Update Logic Error**

- **Pitfall:** Forgetting to check `if (idx >= curL && idx <= curR)` when moving the Time pointer.
- **Result:** You'll update the global array but fail to update the current window's score.

**3. Integer Overflow**

- **Pitfall:** `curScore` as an `int`.
- **Reason:** $\text{Value} \times \text{Freq}^2 = 10^9 \times (2 \cdot 10^5)^2$ is massive! Even after coordinate compression, the "Value" part is the original $10^9$.
- **Fix:** Use **64-bit integers** (long long) for the score.

**4. Coordinate Compression Scope**

- **Pitfall:** Only compressing the initial array values.
- **Problem:** Updating an element to a value $x$ that wasn't in the initial array.
- **Fix:** Collect ALL initial values and ALL update values into one giant list before compressing.

## 🎯 Variations & Extensions

### Variation 1: Different Score Functions

Any function that can be updated in $O(1)$ when adding/removing can use Mo's. (e.g., number of distinct elements, sum of counts).

### Variation 2: Tree Mo's with Updates

Mo's on a tree (using Euler tours) with modifications.

### Variation 3: Hilbert Curve Ordering

Using a fractal space-filling curve to sort $(L, R)$ points is faster in standard Mo's, but harder to generalize to 3D.

### Variation 4: Rollback Mo's

If the "remove" operation is hard or impossible (e.g., finding the maximum in a range), special versions of Mo's that only "add" and "rollback" are used.

## 🎓 Key Takeaways

1. **Offline Flexibility:** If you know all operations, you can reorder them to your advantage.
2. **The Time Dimension:** Updates are just a third axis in your search space.
3. **Block Scaling:** $N^{2/3}$ is the magical scaling for 3D square-root decomposition.
4. **Coordinate Compression:** Essential for turning large value ranges into usable array indices.

## 📚 Related Problems

- **D-query:** Count distinct elements in a range.
- **Powerful Array:** The quintessential Mo's problem (similar score formula).
- **Static Range K-th Smallest:** Can be solved with Mo's (though slower than persistence).
- **ARR-041:** Persistent Prefix Max (The "online" alternative for some versioned problems).
