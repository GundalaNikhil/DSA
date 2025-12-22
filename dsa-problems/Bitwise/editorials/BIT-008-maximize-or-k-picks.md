---
problem_id: BIT_MAXIMIZE_OR_K_PICKS__8408
display_id: BIT-008
slug: maximize-or-k-picks
title: "Maximize OR With K Picks"
difficulty: Medium
difficulty_score: 48
topics:
  - Bitwise Operations
  - Greedy
  - Optimization
tags:
  - bitwise
  - greedy
  - medium
premium: true
subscription_tier: basic
---

# Maximize OR With K Picks

## Real-World Scenario: Feature Flags in Software Deployment

Imagine you're deploying software with feature flags represented as bit patterns. Each module has certain features enabled (set bits):

1. **Modules**: Each with a feature bitmask
2. **Resource Limit**: Can deploy only `k` modules
3. **Goal**: Maximize total enabled features (OR of selected modules)
4. **OR Property**: Deploying module adds its features without removing existing ones

**Application**: This models resource allocation where combining items creates cumulative benefits without conflicts.

**ASCII Visualization: Feature Flag Selection**

```
Modules: [1, 2, 4, 8], k=2

Module A: 0001 (Feature 0)
Module B: 0010 (Feature 1)
Module C: 0100 (Feature 2)
Module D: 1000 (Feature 3)

Best selection: C + D = 0100 OR 1000 = 1100
Features enabled: 2, 3 (maximum coverage)

Why not A + B? 0001 OR 0010 = 0011 (only features 0,1)
Lower-value features!
```

---

## Understanding the Problem

### Key Observations

1. **OR Property**: `a OR b` sets all bits that are 1 in either a or b
2. **Monotonicity**: Adding more elements can only increase (or maintain) the OR value
3. **Higher Bits Matter More**: Bit position 30 contributes 2^30, much more than bit 0 (2^0)
4. **Greedy Opportunity**: Prioritize elements that contribute high-value bits

### Critical Insight

**Greedy Strategy**: Prioritize elements that set the highest-order bits not yet set.

```
Example: [7, 8, 15, 1], k=2

7  = 0111
8  = 1000  ← Has bit 3 (highest)
15 = 1111  ← Has bit 3 AND lower bits
1  = 0001

Best choice: {8, 15} OR {7, 15}
- 8 OR 15 = 1000 OR 1111 = 1111 = 15
- 7 OR 15 = 0111 OR 1111 = 1111 = 15

Both give 15 (maximum possible)
```

---

## Approach 1: Brute Force (Combinations)

### Algorithm

Try all C(n, k) combinations and find maximum OR.

```python
from itertools import combinations

max_or = 0
for combo in combinations(arr, k):
    current_or = 0
    for num in combo:
        current_or |= num
    max_or = max(max_or, current_or)
return max_or
```

**ASCII: Combination Tree**

```
Array: [1, 2, 4], k=2

        root
       /  |  \
      1   2   4
     / \  |
    2  4  4

Combinations:
(1,2): 1|2 = 3
(1,4): 1|4 = 5
(2,4): 2|4 = 6  ← Maximum
```

### Complexity

- **Time**: O(C(n,k) × k) = O(n^k) in worst case
- **Space**: O(k) for storing combination
- **Issue**: Exponential time, infeasible for large n

---

## Approach 2: Greedy Bit-by-Bit (Optimal)

### Key Insight

Process bits from MSB (most significant) to LSB. For each bit position:

- Count elements that have this bit set
- Greedily select elements with higher bits

**Refined Strategy**:

1. Sort elements by their "contribution" to OR
2. Contribution = which new bits they add
3. Select k elements that together maximize OR

**Better Strategy (Actual Optimal)**:
Since we want maximum OR, we should:

1. Consider which bits can possibly be set in final answer
2. Greedily pick elements that contribute highest-value bits first

### Algorithm

```python
def maximize_or_greedy(arr, k):
    # Strategy: Sort by value (descending), but smarter
    # For OR, higher values tend to have higher bits set

    selected = []
    current_or = 0
    remaining = list(arr)

    for _ in range(k):
        best_num = None
        best_or = current_or
        best_idx = -1

        # Find element that maximizes OR when added
        for i, num in enumerate(remaining):
            new_or = current_or | num
            if new_or > best_or:
                best_or = new_or
                best_num = num
                best_idx = i

        if best_idx != -1:
            selected.append(best_num)
            current_or = best_or
            remaining.pop(best_idx)

    return current_or
```

**ASCII: Greedy Selection**

```
Array: [7, 8, 15, 1], k=2

Round 1: current_or = 0
  Try 7:  0 | 7  = 7  (0111)
  Try 8:  0 | 8  = 8  (1000) ← Best so far
  Try 15: 0 | 15 = 15 (1111) ← Best!
  Try 1:  0 | 1  = 1  (0001)

  Select: 15, current_or = 15

Round 2: current_or = 15 (1111)
  Try 7:  15 | 7  = 15
  Try 8:  15 | 8  = 15
  Try 1:  15 | 1  = 15

  All same! Pick any: 7

Result: 15
```

### Complexity

- **Time**: O(n × k)
  - For each of k selections, scan n elements
- **Space**: O(n) for remaining array
- **Optimality**: Greedy is optimal for OR maximization!

---

## Approach 3: Optimized with Sorting

### Key Insight

Sort by descending order. Elements with higher values tend to have higher bits set.

```python
def maximize_or_sorted(arr, k):
    # Sort descending
    arr_sorted = sorted(arr, reverse=True)

    # This doesn't always work! Counterexample:
    # [7, 8], k=1: Sorted = [8, 7]
    # Pick 8: OR = 8

    # Better: Still need greedy approach, but sorting helps
    # as a heuristic to reduce search space

    current_or = 0
    for i in range(min(k, len(arr_sorted))):
        current_or |= arr_sorted[i]

    return current_or
```

**Problem**: Simple sorting doesn't guarantee optimality!

**Counterexample**:

```
Array: [4, 2, 1], k=2
Sorted: [4, 2, 1]

Simple approach: Pick 4, 2
4 | 2 = 0100 | 0010 = 0110 = 6

But: 4 | 1 = 0100 | 0001 = 0101 = 5
And: 2 | 1 = 0010 | 0001 = 0011 = 3

So [4,2] is indeed optimal here.

Better counterexample:
Array: [3, 5, 6], k=2
3 = 011
5 = 101
6 = 110

Sorted: [6, 5, 3]
Pick [6,5]: 110 | 101 = 111 = 7

Pick [6,3]: 110 | 011 = 111 = 7
Pick [5,3]: 101 | 011 = 111 = 7

All give 7! (All 3 bits can be set)
```

**Conclusion**: For OR, greedy approach works, but need proper strategy!

---

### Correct Optimal Approach

### Key Insight

**Observation**: To maximize OR, we want to maximize the highest bit position set.

**Algorithm**:

1. For each round, pick the element that, when OR'd with current result, gives maximum value
2. This is the greedy approach from Approach 2

**Why it works**: OR is monotonic - adding elements can only increase (or maintain) the OR value. At each step, picking the element that maximizes current OR also maximizes final OR.

### Complete Implementation

### Java Solution

```java
import java.util.*;

public class Solution {
    /**
     * Maximize bitwise OR by selecting k elements
     *
     * @param arr Array of non-negative integers
     * @param k Number of elements to select
     * @return Maximum bitwise OR of k elements
     */
    public static int maximizeOrWithKPicks(int[] arr, int k) {
        int n = arr.length;
        boolean[] used = new boolean[n];
        int currentOr = 0;

        for (int pick = 0; pick < k; pick++) {
            int bestValue = 0;
            int bestIdx = -1;

            // Find element that maximizes OR when added
            for (int i = 0; i < n; i++) {
                if (!used[i]) {
                    int newOr = currentOr | arr[i];
                    if (newOr > bestValue) {
                        bestValue = newOr;
                        bestIdx = i;
                    }
                }
            }

            if (bestIdx != -1) {
                used[bestIdx] = true;
                currentOr = bestValue;
            }
        }

        return currentOr;
    }

    public static void main(String[] args) {
        int[] arr1 = {1, 2, 4};
        System.out.println(maximizeOrWithKPicks(arr1, 2));  // Expected: 6

        int[] arr2 = {7, 8, 15, 1};
        System.out.println(maximizeOrWithKPicks(arr2, 2));  // Expected: 15

        int[] arr3 = {5, 10, 15, 20};
        System.out.println(maximizeOrWithKPicks(arr3, 3));  // Expected: 31
    }
}
```

### Python Solution

```python
def maximize_or_with_k_picks(arr: list[int], k: int) -> int:
    """
    Maximize bitwise OR by selecting k elements greedily.

    Greedy strategy: At each step, pick the element that
    maximizes the current OR value.

    Args:
        arr: List of non-negative integers
        k: Number of elements to select

    Returns:
        Maximum bitwise OR of k elements
    """
    n = len(arr)
    used = [False] * n
    current_or = 0

    for _ in range(k):
        best_value = 0
        best_idx = -1

        # Find element that maximizes OR when added
        for i in range(n):
            if not used[i]:
                new_or = current_or | arr[i]
                if new_or > best_value:
                    best_value = new_or
                    best_idx = i

        if best_idx != -1:
            used[best_idx] = True
            current_or = best_value

    return current_or


# Test cases
if __name__ == "__main__":
    print(maximize_or_with_k_picks([1, 2, 4], 2))       # Expected: 6
    print(maximize_or_with_k_picks([7, 8, 15, 1], 2))   # Expected: 15
    print(maximize_or_with_k_picks([5, 10, 15, 20], 3)) # Expected: 31
```

### C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    /**
     * Maximize bitwise OR by selecting k elements
     */
    static int maximizeOrWithKPicks(const vector<int>& arr, int k) {
        int n = arr.size();
        vector<bool> used(n, false);
        int currentOr = 0;

        for (int pick = 0; pick < k; pick++) {
            int bestValue = 0;
            int bestIdx = -1;

            for (int i = 0; i < n; i++) {
                if (!used[i]) {
                    int newOr = currentOr | arr[i];
                    if (newOr > bestValue) {
                        bestValue = newOr;
                        bestIdx = i;
                    }
                }
            }

            if (bestIdx != -1) {
                used[bestIdx] = true;
                currentOr = bestValue;
            }
        }

        return currentOr;
    }
};

int main() {
    vector<int> arr1 = {1, 2, 4};
    cout << Solution::maximizeOrWithKPicks(arr1, 2) << endl;  // Expected: 6

    vector<int> arr2 = {7, 8, 15, 1};
    cout << Solution::maximizeOrWithKPicks(arr2, 2) << endl;  // Expected: 15

    vector<int> arr3 = {5, 10, 15, 20};
    cout << Solution::maximizeOrWithKPicks(arr3, 3) << endl;  // Expected: 31

    return 0;
}
```

### JavaScript Solution

```javascript
/**
 * Maximize bitwise OR by selecting k elements
 *
 * @param {number[]} arr - Array of non-negative integers
 * @param {number} k - Number of elements to select
 * @return {number} Maximum bitwise OR
 */
function maximizeOrWithKPicks(arr, k) {
  const n = arr.length;
  const used = new Array(n).fill(false);
  let currentOr = 0;

  for (let pick = 0; pick < k; pick++) {
    let bestValue = 0;
    let bestIdx = -1;

    // Find element that maximizes OR when added
    for (let i = 0; i < n; i++) {
      if (!used[i]) {
        const newOr = currentOr | arr[i];
        if (newOr > bestValue) {
          bestValue = newOr;
          bestIdx = i;
        }
      }
    }

    if (bestIdx !== -1) {
      used[bestIdx] = true;
      currentOr = bestValue;
    }
  }

  return currentOr;
}

// Test cases
console.log(maximizeOrWithKPicks([1, 2, 4], 2)); // Expected: 6
console.log(maximizeOrWithKPicks([7, 8, 15, 1], 2)); // Expected: 15
console.log(maximizeOrWithKPicks([5, 10, 15, 20], 3)); // Expected: 31
```

---

## Edge Cases and Special Scenarios

### Edge Case 1: k = 1

```
Input: arr = [5, 10, 15], k = 1
Output: 15

Explanation: Pick the maximum value
```

### Edge Case 2: k = n (all elements)

```
Input: arr = [1, 2, 4, 8], k = 4
Output: 15

Explanation: OR of all: 1|2|4|8 = 15
```

### Edge Case 3: All zeros

```
Input: arr = [0, 0, 0], k = 2
Output: 0

Explanation: OR of zeros is zero
```

### Edge Case 4: One large element

```
Input: arr = [1000, 1, 2, 3], k = 2
Output: 1003

Explanation: Pick 1000 first (1111101000)
Then pick 3 (11) → 1000|3 = 1003
```

### Edge Case 5: Powers of 2

```
Input: arr = [1, 2, 4, 8, 16], k = 3
Output: 28

Explanation: Pick 16, 8, 4 → 16|8|4 = 11100 = 28
```

---

### Common Mistakes

### Mistake 1: Simple Sorting

```python
# WRONG: Just taking k largest
arr.sort(reverse=True)
result = 0
for i in range(k):
    result |= arr[i]
# This often works but not always optimal!
```

### Mistake 2: Not Using Greedy

```python
# WRONG: Random selection
import random
selected = random.sample(arr, k)
result = 0
for num in selected:
    result |= num
```

### Mistake 3: Forgetting OR Property

```python
# WRONG: Trying to maximize sum instead of OR
arr.sort(reverse=True)
return sum(arr[:k])  # This is NOT the same!
```

---

## Interview Extensions

### Extension 1: Minimum OR

**Question**: Find minimum OR with k picks.

**Answer**: Pick k smallest elements (OR can't decrease, so pick smallest).

### Extension 2: XOR Instead of OR

**Question**: Maximize XOR with k picks.

**Answer**: More complex - need different strategy (XOR can decrease).

### Extension 3: Return Selected Elements

**Question**: Return which elements to pick.

**Answer**: Track indices in the greedy algorithm.

---

## Practice Problems

1. **LeetCode 1318**: Minimum Flips to Make a OR b Equal to c
2. **LeetCode 2275**: Largest Combination With Bitwise AND Greater Than Zero
3. **Codeforces 1556C**: Compressed Bracket Sequence

---

## Summary Table

| Approach         | Time        | Space | Optimal?           |
| ---------------- | ----------- | ----- | ------------------ |
| Brute Force      | O(C(n,k)×k) | O(k)  | Yes (too slow)     |
| Greedy           | O(n×k)      | O(n)  | Yes (fast!)        |
| Sorted Heuristic | O(n log n)  | O(1)  | No (usually works) |

**Recommended**: Greedy approach (Approach 2).

---

## Key Takeaways

1. **OR Monotonicity**: Adding elements can only increase OR
2. **Greedy Works**: At each step, pick element that maximizes current OR
3. **Higher Bits Win**: Prioritize elements contributing to higher bit positions
4. **O(n×k) Time**: Efficient enough for n, k ≤ 2×10^5
5. **Simple Implementation**: No complex data structures needed
6. **Optimal Solution**: Greedy is provably optimal for OR maximization
