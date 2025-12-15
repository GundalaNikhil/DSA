---
problem_id: ARR_WEIGHTED_BAL__7746
display_id: ARR-005
slug: weighted-balance-point
title: "Weighted Balance Point"
difficulty: Medium
difficulty_score: 55
topics:
  - Array
  - Prefix Sum
  - Balance Point
  - Mathematical
tags:
  - arrays
  - prefix-sum
  - equilibrium
  - medium
premium: true
subscription_tier: pro
---

# Weighted Balance Point

![Problem Header](../images/ARR-005/header.png)

### 📋 Problem Summary

Find an index `i` where `sum(elements left of i) × L == sum(elements right of i) × R`, for given weight multipliers L and R.

### 🌍 Real-World Scenario

**Weighted Voting System**

Imagine a committee voting system where:

- **Left wing votes** (progressive policies) have weight L
- **Right wing votes** (conservative policies) have weight R
- Need to find a "pivot member" where both sides have equal weighted influence

Example:

```
Votes: [2, 3, -1, 3, 2], L=2, R=1

At index 1:
Left votes: [2] → sum=2 → weighted = 2×2 = 4
Right votes: [-1, 3, 2] → sum=4 → weighted = 4×1 = 4
Balance! ✓ (Both sides have equal weighted influence)
```

**Applications**:

- **Political Science**: Finding equilibrium in weighted voting
- **Economics**: Balancing weighted market forces
- **Game Theory**: Fair resource distribution with different priorities
- **Engineering**: Load balancing with priority weights

### 📚 Detailed Explanation

**What is Weighted Balance?**

For index `i`, we check if:

```
sum(arr[0..i-1]) × L == sum(arr[i+1..n-1]) × R
```

Where:

- **L** = weight/multiplier for left side (given as input)
- **R** = weight/multiplier for right side (given as input)
- **Left sum** = sum of all elements before index i
- **Right sum** = sum of all elements after index i
- **Element at index i is excluded from both sums**

**Key Insight**:
Use prefix sum to compute left sum, derive right sum from total, then compare `leftSum × L` with `rightSum × R`!

### ❌ Naive Approach

**Algorithm**:

```
For each index i:
  Calculate sum of elements before i (left sum)
  Calculate sum of elements after i (right sum)
  If leftSum × L == rightSum × R, return i
Return -1
```

**⏱️ Time Complexity: O(n²)**

```
For n positions:
  Each position: O(n) to calculate sums
Total: n × n = O(n²)
```

**Impact**:

- n = 100: 10,000 operations
- n = 10,000: 100,000,000 operations (slow!)
- n = 100,000: 10,000,000,000 operations (timeout!)

**📦 Space Complexity: O(1)**

- Only storing sums and counters

### ✅ Optimal Approach

**Algorithm**:

1. Precompute total sum of all elements
2. Iterate through each index i:
   - Maintain left sum (elements before i)
   - Calculate right sum = total - left sum - arr[i]
   - Check if leftSum × L == rightSum × R
3. Return first index that satisfies condition, or -1

**Mathematical Simplification**:

```
At index i:
  leftSum = arr[0] + arr[1] + ... + arr[i-1]
  rightSum = arr[i+1] + arr[i+2] + ... + arr[n-1]
           = totalSum - leftSum - arr[i]

Check: leftSum × L == rightSum × R
```

**⏱️ Time Complexity: O(n)**

```
Single pass to calculate total: O(n)
Single pass to check each index: O(n)
Total: O(n) + O(n) = O(n)
```

**Speedup Factor**:

- From O(n²) to O(n) = **n times faster**
- n = 10,000: 100M → 10K operations (10,000× speedup!)

**📦 Space Complexity: O(1)**

- Only storing running sums and totals

### 🎨 Visual Representation

**Example**: `arr = [2, 3, -1, 3, 2]`, `L = 2`, `R = 1`

```
Checking each index for weighted balance:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Index 0: [2] (3, -1, 3, 2)
┌───┐┌────────────────┐
│ 2 ││ 3 -1  3  2     │
└───┘└────────────────┘
  ↑ pivot

Left:  [] = 0
Right: [3, -1, 3, 2] = 7
Check: 0 × 2 == 7 × 1?
       0 == 7? NO ✗

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Index 1: (2) [3] (-1, 3, 2)
┌───┐┌───┐┌────────────┐
│ 2 ││ 3 ││ -1  3  2   │
└───┘└───┘└────────────┘
       ↑ pivot

Left:  [2] = 2
Right: [-1, 3, 2] = 4
Check: 2 × 2 == 4 × 1?
       4 == 4? YES! ✓

Answer: Index 1

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Index 2: (2, 3) [-1] (3, 2)
┌───────┐┌────┐┌───────┐
│ 2  3  ││ -1 ││ 3  2  │
└───────┘└────┘└───────┘
            ↑ pivot

Left:  [2, 3] = 5
Right: [3, 2] = 5
Check: 5 × 2 == 5 × 1?
       10 == 5? NO ✗

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 🧪 Test Case Walkthrough

**Input**: `arr = [2, 3, -1, 3, 2]`, `L = 2`, `R = 1`

**Step-by-Step Calculation**:

```
Total sum = 2 + 3 + (-1) + 3 + 2 = 9

┌───────┬────────────────┬─────────────────┬──────────────┬──────────┐
│ Index │ Left Elements  │ Right Elements  │ Weighted Eq  │ Balance? │
├───────┼────────────────┼─────────────────┼──────────────┼──────────┤
│   0   │ []             │ [3,-1,3,2]      │ 0×2 vs 7×1   │    ✗     │
│       │ sum=0          │ sum=7           │ 0 vs 7       │          │
├───────┼────────────────┼─────────────────┼──────────────┼──────────┤
│   1   │ [2]            │ [-1,3,2]        │ 2×2 vs 4×1   │    ✓     │
│       │ sum=2          │ sum=4           │ 4 vs 4       │ FOUND!   │
├───────┼────────────────┼─────────────────┼──────────────┼──────────┤
│   2   │ [2,3]          │ [3,2]           │ 5×2 vs 5×1   │    ✗     │
│       │ sum=5          │ sum=5           │ 10 vs 5      │          │
├───────┼────────────────┼─────────────────┼──────────────┼──────────┤
│   3   │ [2,3,-1]       │ [2]             │ 4×2 vs 2×1   │    ✗     │
│       │ sum=4          │ sum=2           │ 8 vs 2       │          │
├───────┼────────────────┼─────────────────┼──────────────┼──────────┤
│   4   │ [2,3,-1,3]     │ []              │ 7×2 vs 0×1   │    ✗     │
│       │ sum=7          │ sum=0           │ 14 vs 0      │          │
└───────┴────────────────┴─────────────────┴──────────────┴──────────┘

Output: 1 (first index where leftSum×L == rightSum×R)
```

### ⚠️ Common Mistakes

#### 1. **Forgetting to Exclude Current Element**

```java
// ❌ WRONG - includes arr[i] in right sum
rightSum = totalSum - leftSum;

// ✅ CORRECT - excludes arr[i]
rightSum = totalSum - leftSum - arr[i];
```

#### 2. **Wrong Multiplication Order**

```java
// ❌ WRONG - potential overflow
if (leftSum * L == rightSum * R)  // Both sides multiply first

// ✅ CORRECT - cross multiply to avoid overflow
if ((long)leftSum * L == (long)rightSum * R)
```

#### 3. **Integer Overflow**

```java
// ❌ WRONG (int might overflow)
int leftWeighted = leftSum * L;

// ✅ CORRECT (use long for multiplication)
long leftWeighted = (long)leftSum * L;
```

#### 4. **Off-by-One in Sum Calculation**

```java
// ❌ WRONG
for (int j = 0; j <= i; j++)  // Includes arr[i]!
    leftSum += arr[j];

// ✅ CORRECT
for (int j = 0; j < i; j++)  // Excludes arr[i]
    leftSum += arr[j];
```

#### 5. **Not Handling Edge Cases**

```java
// ❌ WRONG - doesn't check empty array
return findBalance(arr);

// ✅ CORRECT
if (arr.length == 0) return -1;
if (arr.length == 1) return 0;  // Single element is always balanced
```

### 🔑 Key Algorithm Points

1. **Prefix sum approach**: Build cumulative sums
2. **Incremental updates**: Don't recalculate from scratch
3. **Mathematical optimization**: Use algebra to simplify
4. **Balance equation**: leftWeighted = rightWeighted

### 💻 Implementations

#### Java

```java
class Solution {
    public int weightedBalancePoint(int[] arr, int L, int R) {
        int n = arr.length;
        if (n == 0) return -1;

        // Calculate total sum
        long totalSum = 0;
        for (int val : arr) {
            totalSum += val;
        }

        long leftSum = 0;

        for (int i = 0; i < n; i++) {
            // Right sum = total - left - current element
            long rightSum = totalSum - leftSum - arr[i];

            // Check if leftSum × L == rightSum × R
            if (leftSum * L == rightSum * R) {
                return i;
            }

            // Add current element to left sum for next iteration
            leftSum += arr[i];
        }

        return -1;
    }
}

// Time: O(n), Space: O(1)
```

#### Python

```python
def weighted_balance_point(arr, L, R):
    """
    Find index where sum(left) × L == sum(right) × R.

    Args:
        arr: List of integers
        L: Weight multiplier for left side
        R: Weight multiplier for right side

    Returns:
        Index of balance point, or -1 if none exists
    """
    n = len(arr)
    if n == 0:
        return -1

    # Calculate total sum
    total_sum = sum(arr)

    left_sum = 0

    for i in range(n):
        # Right sum = total - left - current element
        right_sum = total_sum - left_sum - arr[i]

        # Check if leftSum × L == rightSum × R
        if left_sum * L == right_sum * R:
            return i

        # Add current element to left sum for next iteration
        left_sum += arr[i]

    return -1

# Time: O(n), Space: O(1)
```

#### C++

```cpp
class Solution {
public:
    int weightedBalancePoint(vector<int>& arr, int L, int R) {
        int n = arr.size();
        if (n == 0) return -1;

        // Calculate total sum
        long long totalSum = 0;
        for (int val : arr) {
            totalSum += val;
        }

        long long leftSum = 0;

        for (int i = 0; i < n; i++) {
            // Right sum = total - left - current element
            long long rightSum = totalSum - leftSum - arr[i];

            // Check if leftSum × L == rightSum × R
            if (leftSum * L == rightSum * R) {
                return i;
            }

            // Add current element to left sum for next iteration
            leftSum += arr[i];
        }

        return -1;
    }
};

// Time: O(n), Space: O(1)
```

### 📊 Comparison Table

| **Aspect**           | **Naive (Recalculate)**         | **Optimal (Prefix Sum)** |
| -------------------- | ------------------------------- | ------------------------ |
| **Algorithm**        | Recalculate sums for each index | Use prefix sum technique |
| **Time Complexity**  | O(n²)                           | O(n) ⭐                  |
| **Space Complexity** | O(1)                            | O(1)                     |
| **For n=1000**       | ~1,000,000 ops                  | ~2,000 ops               |
| **For n=100,000**    | ~10,000,000,000 ops             | ~200,000 ops             |
| **Speedup**          | Baseline                        | **n times faster** ⭐    |
| **Key Optimization** | None                            | Reuse total sum          |
| **Best for**         | Learning concept                | Production use ⭐        |

### 🔑 Key Algorithm Points

1. **Total sum optimization**: Calculate once, reuse for all indices
2. **Simple arithmetic**: `rightSum = totalSum - leftSum - arr[i]`
3. **Cross multiplication**: Compare `leftSum × L` with `rightSum × R`
4. **No nested loops**: Single pass through array
5. **O(1) space**: Only need a few variables
