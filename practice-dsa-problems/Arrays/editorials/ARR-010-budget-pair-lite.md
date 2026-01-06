---
problem_id: ARR_BUDGET_PAIR__4482
display_id: ARR-010
slug: budget-pair-lite
title: "Budget Pair Lite"
difficulty: Easy
difficulty_score: 28
topics:
  - Arrays
tags:
  - algorithms
  - array-manipulation
  - arrays
  - coding-interviews
  - constraint-optimization
  - data-structures
  - lexicographical-order
  - searching
  - technical-interview-prep
  - two-pointers
  - two-sum
premium: false
subscription_tier: basic
---

# ARR-010: Budget Pair Lite

## 📋 Problem Summary

Given an array of $n$ integers, a target sum $T$, and a maximum allowed difference $D$, you need to find a pair of indices $(i, j)$ that meet three specific criteria:

1. **The Order Criterion:** $i < j$.
2. **The Sum Criterion:** $a_i + a_j = T$.
3. **The Difference Criterion:** $|a_i - a_j| \le D$.

**Priority Rules:**

- If multiple such pairs exist, you must return the one with the smallest $i$.
- If there is still a tie, choose the one with the smallest $j$.
- If no valid pair exists, return $-1$.

**Constraint Note:** Indices are 1-based in the output. $n=200,000$ requires an optimized $O(n \log n)$ or $O(n)$ solution.

## 🌍 Real-World Scenarios

**Scenario 1: 🎁 The Balanced Gift Exchange**
You are buying two gifts for a company secret santa. The total budget approved by the finance department is exactly $T$. To ensure fairness and avoid resentment among employees, the difference in value between the two gifts cannot exceed $D$. You look through the store catalog in order. To save time, you want to propose the first valid pair of items you see, prioritizing the item that appears earliest in the catalog for your own convenience.

**Scenario 2: 🎮 Skill-Based Matchmaking**
In a 2v2 competitive game, you need to pair two players to reach a team "Power Level" of exactly $T$. However, to ensure good team chemistry, the skill gap between the two players should not be larger than $D$. The database lists players in the order they joined the queue. The system prioritizes the "Oldest" player (smallest $i$) to get them into a game as soon as possible, matching them with the earliest possible companion who satisfies the constraints.

**Scenario 3: 🧪 Chemical Reagent Synthesis**
A laboratory needs to mix two chemical compounds to produce a stable solution with a target volume $T$. For the reaction to proceed safely without overheating, the volatility values of the two chemicals must be within $D$ of each other. The chemist picks the first suitable chemical from the shelf and looks for the next earliest compatible chemical to minimize movement in the lab.

**Scenario 4: 🪑 IKEA Furniture Assembly (Component Matching)**
You are building a complex shelf. You need two specific screws whose combined length is precisely $T$. If one screw is significantly longer than the other, the structure will be lopsided; thus, the length difference must be $\le D$. You pull screws from the bin in the order they are packed. You want to use the first screw in the bin that can be paired up to finish the step.

**Scenario 5: 📅 Event Coordination (Shift Pairing)**
A manager needs to assign two employees to a task that requires exactly $T$ man-hours. To avoid workload jealousy, the difference in hours assigned to each employee must be $\le D$. The manager processes employee requests in order of seniority ($i < j$) and picks the most senior possible pairing.

### Real-World Relevance

This problem is a constrained version of the classic **Two Sum** problem. In real systems, we rarely just want "any" pair; we often have secondary constraints (like the difference $D$) and a priority system (like the smallest index $i$) to ensure fairness, efficiency, or stability.

## 🚀 Detailed Explanation

### 1. The Core Logic: Two Sum with a Twist

In a standard Two Sum problem, for every $a_i$, we look for $a_j = T - a_i$.
In this problem, once we find $a_j$, we must also verify:
$$|a_i - a_j| \le D$$
Substituting $a_j = T - a_i$:
$$|a_i - (T - a_i)| \le D$$
$$|2a_i - T| \le D$$
$$-D \le 2a_i - T \le D$$
$$T - D \le 2a_i \le T + D$$

This means a value $a_i$ is only even **capable** of being part of a valid pair if its value falls within a specific range related to $T$ and $D$.

### 2. Solving for Lexicographical Priority (Smallest $i$, then $j$)

To satisfy the "Smallest $i$ first" rule:

1. We should iterate $i$ from $1 \dots n$.
2. For each $i$, we calculate the required $a_j = T - a_i$.
3. We check if the difference constraint $|a_i - a_j| \le D$ is met.
4. If yes, we need to find the **first index $j$** such that $j > i$ and $a_j$ is the required value.
5. Since we are moving through $i$ in increasing order, the first valid pair we find is guaranteed to have the smallest $i$. Furthermore, if we find the smallest $j > i$ for that $i$, we satisfy the second priority rule.

### 3. Efficient Searching

With $n=200,000$, we cannot scan through $j$ for every $i$ ($O(n^2)$). We need a data structure:

- **Map of Lists:** Use a Hash Map where the key is the number value and the value is a **Sorted List** of indices where that number appears.
  - `Map<Value, List<Index>>`
- **Example:** `[1, 4, 7, 3, 2], T=5`.
  - Map: `{1: [1], 4: [2], 7: [3], 3: [4], 2: [5]}`.
- When $i=1$ ($a_i=1$), we need $a_j = 5-1=4$. We check the list for value `4`: `[2]`. The first index `> 1` is `2`. This is a candidate.

### 🔄 Algorithm Flow Diagram

```mermaid
flowchart TD
    Start([Start]) --> Pre[1. Pre-process: Build Map<br>Value -> Sorted List of 1-based Indices]
    Pre --> Loop{2. Loop i from 1 to n}

    Loop -- Next --> Target[Calculate Target a_j = T - a_i]
    Target --> DiffCheck{Is |a_i - a_j| <= D?}

    DiffCheck -- No --> Loop
    DiffCheck -- Yes --> MapCheck{Does a_j exist in Map?}

    MapCheck -- No --> Loop
    MapCheck -- Yes --> Search[Use Binary Search to find the<br>smallest index j in list[a_j] such that j > i]

    Search --> Found{j exists?}
    Found -- Yes --> Done([Return i, j])
    Found -- No --> Loop

    Loop -- Done --> Fail([-1])
```

## 🔍 Complexity Analysis

### Time Complexity: $O(N \log N)$

- **Building the Map:** $O(N)$ to iterate and $O(1)$ amortized for hash map insertion.
- **Main Loop:** $N$ iterations.
- **Binary Search:** For each $i$, we perform a binary search (like `upper_bound` in C++ or `bisect_right` in Python) on the list of indices for $a_j$. Total $\log N$.
- Total: $O(N \log N)$. Perfectly suited for $N=200,000$ within a 1-2 second time limit.

### Space Complexity: $O(N)$

- The Map stores every index of the array exactly once.
- Total space: $O(N)$ for the index lists.

## 🧪 Edge Cases & Testing

### 1. $T = 2a_i$ (Pairing with the Same Value)

- **Input:** `[3, 4, 3], T=6, D=10`
- **Logic:** $i=1$ ($a_1=3$). Target $a_j = 3$. Indices for 3 are `[1, 3]`. Smallest index $> 1$ is `3`.
- **Result:** `1 3`.
- **Pitfall:** If you only store one index per value, you won't be able to pair two identical numbers.

### 2. Difference Constraint Exactly $D$

- **Input:** `[1, 5], T=6, D=4`
- **Logic:** $|1 - 5| = 4$. Since $4 \le 4$, this is valid.

### 3. $D = 0$ (Perfect Equality)

- **Input:** `[5, 4, 5], T=10, D=0`
- **Logic:** Pairs must have $|a_i - a_j| = 0$, meaning $a_i = a_j$. Since $a_i + a_j = 10$, both must be $5$.
- **Result:** `1 3`.

### 4. Negative Numbers

- **Input:** `[-1, 1], T=0, D=5`
- **Logic:** $|-1 - 1| = 2 \le 5$. Valid.

### 5. No Solution

- **Input:** `[1, 2, 3], T=10, D=100`
- **Result:** `-1`.

### 6. Smallest $i$ Priority

- **Input:** `[1, 4, 2, 3], T=5, D=5`
- **Pairs:** `(1, 4)` and `(2, 3)` both sum to 5.
- **Indices:** `(1, 2)` and `(3, 4)`.
- **Result:** `1 2` (because $1 < 3$).

## ⚠️ Common Pitfalls & Debugging

**1. 1-Based Indexing**

- **Pitfall:** Array indexing is typically 0-based in coding, but the output requires 1-based.
- **Fix:** Add $+1$ to your loop index and stored map indices when outputting.

**2. Duplicate Value Lists**

- **Pitfall:** Using a `Map<Integer, Integer>` to store only the _last_ seen index.
- **Result:** You might skip the smallest $j$ or fail to find a $j$ that exists but was overwritten in the map.
- **Fix:** Use a `List` of indices for each key.

**3. Binary Search Boundary**

- **Pitfall:** Looking for $j \ge i$.
- **Correction:** The problem says $i < j$, so you must look for $j > i$.

**4. Integer Overflow**

- **Pitfall:** $a_i + a_j$ might exceed $2^{31}-1$.
- **Correction:** $T$ is given as $10^9$ and $n$ elements are $10^9$. The sum can be $2 \times 10^9$, which fits in a standard 32-bit signed integer. However, $2a_i$ in the $|2a_i - T| \le D$ check can reach $2 \times 10^9$. Be cautious if $T$ or $a_i$ could be larger, or use 64-bit integers (`long`) to avoid worries.

## 🎯 Variations & Extensions

### Variation 1: Budget Pair Pro (Sum $\le T$)

Find a pair where $a_i + a_j \le T$.
_Solution: Requires a Fenwick Tree or Segment Tree to find the range of valid partners._

### Variation 2: Closest Pair to $T$

Find the pair whose sum is closest to $T$ while maintaining $|diff| \le D$.

### Variation 3: 3-Way Budget Matching

Find $i < j < k$ such that $a_i+a_j+a_k = T$.

### Variation 4: Multi-Target Search

Find a pair whose sum is $T_1$ or $T_2$.

### Variation 5: Penalty-Based Pairing

Each pair has a penalty proportional to $|a_i - a_j|$. Find the pair with weight $\le D$ and min penalty.

## 🎓 Key Takeaways

1. **Lexicographical Preference:** To minimize the first index, the outer loop should iterate forward through that index.
2. **Inverse Lookup:** Hash Maps turn an $O(n)$ search into $O(1)$ for specific target values.
3. **Sorted Index Management:** Storing multiple indices in sorted order allows for efficient "next available" queries via Binary Search.
4. **Range Deduction:** Using algebra to simplify constraints ($|2a_i - T| \le D$) can help in understanding the problem's bounds.

## 📚 Related Problems

- **Two Sum (LeetCode 1):** The classic foundation.
- **Two Sum II (Sorted):** Uses two pointers (unsuitable here as sorting ruins index order).
- **Pairs with Specific Difference:** Finding $|a_i - a_j| = K$.
- **3Sum:** Finding triples.
- **ARR-013:** Two Sum Cost Optimization (Adding a cost factor to the pair selection).
