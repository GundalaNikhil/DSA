---
problem_id: BIT_PAIRWISE_XOR_BAND_PARITY__8404
display_id: BIT-004
slug: pairwise-xor-band-index-parity
title: Pairwise XOR in Band With Index Parity
difficulty: Medium
difficulty_score: 55
topics:
- Bitwise Operations
- Array Processing
- XOR
tags:
- bitwise
- array
- medium
premium: true
subscription_tier: basic
---
# Pairwise XOR in Band With Index Parity

## Real-World Scenario: Network Packet Error Detection

Imagine you're designing a distributed network monitoring system where packets are analyzed for error patterns. The system needs to compute XOR checksums between packets at different positions, but with special rules:

1. **Band Constraint**: Only packets within distance `k` can be XOR'd together (to represent temporal locality)
2. **Parity Constraint**: Only packets at even indices XOR with even, odd with odd (to separate control/data channels)
3. **Accumulation**: All valid XOR checksums are combined to detect overall network health

This problem models exactly this scenario: finding all valid pairwise XOR values within constraints and computing their total XOR.

**ASCII Visualization: Network Packet Analysis**

```
Array: [5, 3, 8, 4, 7]  k=2

Indices:    0   1   2   3   4
Values:     5   3   8   4   7
Parity:    [E] [O] [E] [O] [E]

Valid Pairs (|i-j| <= k, same parity):
┌─────────────────────────────────────┐
│ Even Indices: 0, 2, 4               │
│   (0,2): |0-2|=2 ≤ 2 ✓  5⊕8 = 13   │
│   (2,4): |2-4|=2 ≤ 2 ✓  8⊕7 = 15   │
│                                     │
│ Odd Indices: 1, 3                   │
│   (1,3): |1-3|=2 ≤ 2 ✓  3⊕4 = 7    │
└─────────────────────────────────────┘

Final XOR: 13 ⊕ 15 ⊕ 7 = 9
```

---

## Understanding the Problem

### Key Observations

1. **Two Independent Groups**: Even and odd indices form separate groups
2. **Band Constraint**: For indices `i` and `j`, we need `|i - j| ≤ k`
3. **No Self-Pairs**: We only consider `i < j` to avoid counting pairs twice
4. **XOR Properties**:
   - `a ⊕ a = 0` (self-cancellation)
   - `a ⊕ b = b ⊕ a` (commutative)
   - `(a ⊕ b) ⊕ c = a ⊕ (b ⊕ c)` (associative)

### Constraint Analysis

- **Array Size**: Up to 10⁵ elements
- **Band Size**: `k` can be up to `n-1` (full array)
- **Values**: Up to 10⁶ (20 bits maximum)

---

## Approach 1: Brute Force (Naive)

### Algorithm

Check every possible pair and validate both conditions.

```
result = 0
for i from 0 to n-2:
    for j from i+1 to n-1:
        if |i - j| <= k AND (i % 2 == j % 2):
            result ^= (arr[i] ^ arr[j])
return result
```

**ASCII: Brute Force Scanning**

```
Array: [5, 3, 8, 4, 7]  k=2

Scan all pairs:
(0,1): dist=1≤2 ✓, parity: 0≠1 ✗  SKIP
(0,2): dist=2≤2 ✓, parity: 0=0 ✓  XOR: 5⊕8=13  ✓
(0,3): dist=3>2 ✗  SKIP
(0,4): dist=4>2 ✗  SKIP
(1,2): dist=1≤2 ✓, parity: 1≠0 ✗  SKIP
(1,3): dist=2≤2 ✓, parity: 1=1 ✓  XOR: 3⊕4=7   ✓
(1,4): dist=3>2 ✗  SKIP
(2,3): dist=1≤2 ✓, parity: 0≠1 ✗  SKIP
(2,4): dist=2≤2 ✓, parity: 0=0 ✓  XOR: 8⊕7=15  ✓
(3,4): dist=1≤2 ✓, parity: 1≠0 ✗  SKIP

Result: 13 ⊕ 7 ⊕ 15 = 9
```

### Complexity Analysis

- **Time**: O(n²) - nested loops over all pairs
- **Space**: O(1) - constant extra space

### Issues

- Too slow for `n = 10⁵` (10¹⁰ operations)
- Doesn't leverage the parity separation

---

## Approach 2: Optimized with Parity Grouping

### Key Insight

Since even and odd indices are independent, we can:

1. Process even indices separately (indices 0, 2, 4, ...)
2. Process odd indices separately (indices 1, 3, 5, ...)
3. Within each group, only check pairs within band distance

### Algorithm

```
result = 0

# Process even indices
for i in range(0, n, 2):  # 0, 2, 4, ...
    j = i + 2  # next even index
    while j < n and (j - i) <= k:
        result ^= (arr[i] ^ arr[j])
        j += 2

# Process odd indices
for i in range(1, n, 2):  # 1, 3, 5, ...
    j = i + 2  # next odd index
    while j < n and (j - i) <= k:
        result ^= (arr[i] ^ arr[j])
        j += 2

return result
```

**ASCII: Parity Group Processing**

```
Array: [5, 3, 8, 4, 7]  k=2

EVEN GROUP (indices: 0, 2, 4):
┌──────────────────────────┐
│ Start i=0: [5, _, 8, _, 7]│
│   j=2: dist=2≤2 ✓         │
│   XOR 5⊕8=13              │
│   j=4: dist=4>2 ✗ STOP    │
│                          │
│ Start i=2: [_, _, 8, _, 7]│
│   j=4: dist=2≤2 ✓         │
│   XOR 8⊕7=15              │
│                          │
│ Start i=4: no more pairs  │
└──────────────────────────┘

ODD GROUP (indices: 1, 3):
┌──────────────────────────┐
│ Start i=1: [_, 3, _, 4, _]│
│   j=3: dist=2≤2 ✓         │
│   XOR 3⊕4=7               │
│                          │
│ Start i=3: no more pairs  │
└──────────────────────────┘

Final: 13 ⊕ 15 ⊕ 7 = 9
```

### Complexity Analysis

- **Time**: O(n·k/2) ≈ O(n·k)
  - Each index `i` checks at most `k/2` indices ahead in its parity group
  - With k small, this is much better than O(n²)
- **Space**: O(1) - constant extra space

### When is this optimal?

- When `k` is small relative to `n`
- Best case: `k = O(1)`, giving O(n) time
- Worst case: `k = n-1`, still O(n²) but with better constants

---

## Approach 3: Window Sliding for Fixed K

### Key Insight (for small k)

If `k` is constant or small, we can process each parity group with a sliding window approach:

- Maintain a window of at most `k/2` elements in each parity group
- For each new element, XOR with all elements in the current window

### Algorithm

```
def solve_with_window(arr, k):
    n = len(arr)
    result = 0

    # Process even indices
    even_window = []
    for i in range(0, n, 2):
        # XOR with all elements in window
        for val in even_window:
            result ^= (arr[i] ^ val)

        # Add to window
        even_window.append(arr[i])

        # Remove elements outside band
        if len(even_window) * 2 > k:
            even_window.pop(0)

    # Process odd indices similarly
    odd_window = []
    for i in range(1, n, 2):
        for val in odd_window:
            result ^= (arr[i] ^ val)
        odd_window.append(arr[i])
        if len(odd_window) * 2 > k:
            odd_window.pop(0)

    return result
```

### Complexity Analysis

- **Time**: O(n·k)
- **Space**: O(k) - for maintaining windows

---

### C++omplete Implementation

### Java Solution

```java
public class Solution {
    /**
     * Compute XOR of all valid pairwise XORs
     * Valid pairs: |i-j| <= k and same parity
     */
    public static int pairwiseXorWithBandAndParity(int[] arr, int k) {
        int n = arr.length;
        int result = 0;

        // Process even indices: 0, 2, 4, ...
        for (int i = 0; i < n; i += 2) {
            // Check pairs with subsequent even indices within band
            for (int j = i + 2; j < n && (j - i) <= k; j += 2) {
                result ^= (arr[i] ^ arr[j]);
            }
        }

        // Process odd indices: 1, 3, 5, ...
        for (int i = 1; i < n; i += 2) {
            // Check pairs with subsequent odd indices within band
            for (int j = i + 2; j < n && (j - i) <= k; j += 2) {
                result ^= (arr[i] ^ arr[j]);
            }
        }

        return result;
    }

    // Test helper
    public static void main(String[] args) {
        // Test case 1
        int[] arr1 = {5, 3, 8, 4, 7};
        int k1 = 2;
        System.out.println(pairwiseXorWithBandAndParity(arr1, k1)); // Expected: 9

        // Test case 2
        int[] arr2 = {1, 2, 3, 4, 5};
        int k2 = 1;
        System.out.println(pairwiseXorWithBandAndParity(arr2, k2)); // Expected: 0
    }
}
```

### Python Solution

```python
def pairwise_xor_with_band_and_parity(arr: list[int], k: int) -> int:
    """
    Compute XOR of all valid pairwise XORs.

    Valid pairs satisfy:
    1. |i - j| <= k (band constraint)
    2. i and j have same parity (both even or both odd)

    Args:
        arr: List of integers
        k: Maximum distance between pair indices

    Returns:
        XOR of all valid pairwise XORs
    """
    n = len(arr)
    result = 0

    # Process even indices: 0, 2, 4, ...
    for i in range(0, n, 2):
        # Check pairs with subsequent even indices within band
        j = i + 2
        while j < n and (j - i) <= k:
            result ^= (arr[i] ^ arr[j])
            j += 2

    # Process odd indices: 1, 3, 5, ...
    for i in range(1, n, 2):
        # Check pairs with subsequent odd indices within band
        j = i + 2
        while j < n and (j - i) <= k:
            result ^= (arr[i] ^ arr[j])
            j += 2

    return result


# Test cases
if __name__ == "__main__":
    # Test case 1
    arr1 = [5, 3, 8, 4, 7]
    k1 = 2
    print(pairwise_xor_with_band_and_parity(arr1, k1))  # Expected: 9

    # Test case 2
    arr2 = [1, 2, 3, 4, 5]
    k2 = 1
    print(pairwise_xor_with_band_and_parity(arr2, k2))  # Expected: 0
```

### C++ Solution

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    /**
     * Compute XOR of all valid pairwise XORs
     * Valid pairs: |i-j| <= k and same parity
     */
    static int pairwiseXorWithBandAndParity(const vector<int>& arr, int k) {
        int n = arr.size();
        int result = 0;

        // Process even indices: 0, 2, 4, ...
        for (int i = 0; i < n; i += 2) {
            // Check pairs with subsequent even indices within band
            for (int j = i + 2; j < n && (j - i) <= k; j += 2) {
                result ^= (arr[i] ^ arr[j]);
            }
        }

        // Process odd indices: 1, 3, 5, ...
        for (int i = 1; i < n; i += 2) {
            // Check pairs with subsequent odd indices within band
            for (int j = i + 2; j < n && (j - i) <= k; j += 2) {
                result ^= (arr[i] ^ arr[j]);
            }
        }

        return result;
    }
};

// Test driver
int main() {
    // Test case 1
    vector<int> arr1 = {5, 3, 8, 4, 7};
    int k1 = 2;
    cout << Solution::pairwiseXorWithBandAndParity(arr1, k1) << endl; // Expected: 9

    // Test case 2
    vector<int> arr2 = {1, 2, 3, 4, 5};
    int k2 = 1;
    cout << Solution::pairwiseXorWithBandAndParity(arr2, k2) << endl; // Expected: 0

    return 0;
}
```

### JavaScript Solution

```javascript
/**
 * Compute XOR of all valid pairwise XORs
 * Valid pairs: |i-j| <= k and same parity
 *
 * @param {number[]} arr - Array of integers
 * @param {number} k - Maximum distance between pair indices
 * @return {number} XOR of all valid pairwise XORs
 */
function pairwiseXorWithBandAndParity(arr, k) {
  const n = arr.length;
  let result = 0;

  // Process even indices: 0, 2, 4, ...
  for (let i = 0; i < n; i += 2) {
    // Check pairs with subsequent even indices within band
    for (let j = i + 2; j < n && j - i <= k; j += 2) {
      result ^= arr[i] ^ arr[j];
    }
  }

  // Process odd indices: 1, 3, 5, ...
  for (let i = 1; i < n; i += 2) {
    // Check pairs with subsequent odd indices within band
    for (let j = i + 2; j < n && j - i <= k; j += 2) {
      result ^= arr[i] ^ arr[j];
    }
  }

  return result;
}

// Test cases
console.log(pairwiseXorWithBandAndParity([5, 3, 8, 4, 7], 2)); // Expected: 9
console.log(pairwiseXorWithBandAndParity([1, 2, 3, 4, 5], 1)); // Expected: 0
```

---

## Edge Cases and Special Scenarios

### Edge Case 1: k = 0 (No valid pairs)

```
Input: arr = [5, 3, 8], k = 0
Output: 0

Explanation: No pairs with |i-j| <= 0 and i < j
```

### Edge Case 2: Single element

```
Input: arr = [42], k = 5
Output: 0

Explanation: No pairs possible with single element
```

### Edge Case 3: k = 1 (Adjacent same parity only)

```
Input: arr = [1, 2, 3, 4, 5], k = 1
Output: 0

Explanation:
- Even: (0,2)? No, |0-2|=2 > 1
- Odd: (1,3)? No, |1-3|=2 > 1
No valid pairs!
```

### Edge Case 4: All same values

```
Input: arr = [7, 7, 7, 7], k = 3
Output: 0

Explanation:
- (0,2): 7⊕7 = 0
- (1,3): 7⊕7 = 0
- Result: 0⊕0 = 0
```

### Edge Case 5: Large k (all pairs valid)

```
Input: arr = [1, 2, 3, 4], k = 10
Output: 0

Explanation:
- Even: (0,2): 1⊕3 = 2
- Odd: (1,3): 2⊕4 = 6
- Result: 2⊕6 = 4
Actually Result = 2⊕6 = 4 (not 0)
```

---

### C++ommon Mistakes and How to Avoid Them

### Mistake 1: Forgetting Parity Constraint

```java
// WRONG: Checking all pairs within band
for (int i = 0; i < n; i++) {
    for (int j = i + 1; j < n && (j - i) <= k; j++) {
        result ^= (arr[i] ^ arr[j]);  // Missing parity check!
    }
}

// CORRECT: Check parity
for (int i = 0; i < n; i++) {
    for (int j = i + 1; j < n && (j - i) <= k; j++) {
        if (i % 2 == j % 2) {  // Same parity
            result ^= (arr[i] ^ arr[j]);
        }
    }
}
```

### Mistake 2: Double Counting Pairs

```python
# WRONG: Counting each pair twice
for i in range(n):
    for j in range(n):
        if abs(i - j) <= k and i % 2 == j % 2:
            result ^= (arr[i] ^ arr[j])  # Counts (i,j) and (j,i)

# CORRECT: Use i < j
for i in range(n):
    for j in range(i + 1, n):  # j > i
        if (j - i) <= k and i % 2 == j % 2:
            result ^= (arr[i] ^ arr[j])
```

### Mistake 3: Incorrect Band Check with Step

```python
# WRONG: Forgetting actual distance
for i in range(0, n, 2):  # Even indices
    j = i + 2
    while j < n and j - i <= k:  # Correct distance check
        result ^= (arr[i] ^ arr[j])
        j += 2

# Not checking if there are enough elements in between
```

### Mistake 4: Integer Overflow (in languages without arbitrary precision)

```cpp
// WRONG in C++ with int (though problem fits in 32-bit)
int result = 0;  // Fine for this problem

// For larger values, might need:
long long result = 0;
```

### Mistake 5: Off-by-One in Loop

```java
// WRONG: Missing last valid pair
for (int i = 0; i < n - 1; i += 2) {  // Should be i < n
    for (int j = i + 2; j < n && (j - i) <= k; j += 2) {
        result ^= (arr[i] ^ arr[j]);
    }
}
```

---

## Interview Extensions

### Extension 1: Count Valid Pairs

**Question**: Instead of computing XOR, return the count of valid pairs.

**Answer**: Same loop structure, just count instead of XOR:

```python
count = 0
for i in range(0, n, 2):
    j = i + 2
    while j < n and (j - i) <= k:
        count += 1
        j += 2
for i in range(1, n, 2):
    j = i + 2
    while j < n and (j - i) <= k:
        count += 1
        j += 2
return count
```

### Extension 2: Maximum XOR Pair

**Question**: Find the pair (i, j) with maximum XOR value among valid pairs.

**Answer**: Track maximum while iterating:

```python
max_xor = 0
for i in range(0, n, 2):
    j = i + 2
    while j < n and (j - i) <= k:
        max_xor = max(max_xor, arr[i] ^ arr[j])
        j += 2
# Repeat for odd indices
```

### Extension 3: Different Parity Rule

**Question**: What if we want to XOR pairs with _different_ parity instead?

**Answer**: Similar approach but alternate between even and odd:

```python
for i in range(0, n, 2):  # Even indices
    j = i + 1  # Start from next odd
    while j < n and (j - i) <= k:
        result ^= (arr[i] ^ arr[j])
        j += 2  # Skip to next odd
```

### Extension 4: Multiple Bands

**Question**: What if we have multiple k values and need result for each?

**Answer**:

- Preprocess: Sort indices by parity
- For each k, use the same algorithm
- Optimization: Process in increasing k order and reuse computations

### Extension 5: 2D Array Extension

**Question**: Extend to 2D array with Manhattan distance constraint.

**Answer**:

```python
for i1 in range(rows):
    for j1 in range(cols):
        for i2 in range(rows):
            for j2 in range(cols):
                manhattan = abs(i1 - i2) + abs(j1 - j2)
                if manhattan <= k and same_parity(i1, j1, i2, j2):
                    result ^= (arr[i1][j1] ^ arr[i2][j2])
```

---

## Practice Problems

1. **LeetCode 1738**: Kth Largest XOR (uses XOR with pairs)
2. **LeetCode 1829**: Maximum XOR for Each Query
3. **Codeforces 578C**: XOR and Distance
4. **HackerRank**: XOR Subsequence (similar constraints)

---

## Summary Table

| Approach        | Time   | Space | Best For           |
| --------------- | ------ | ----- | ------------------ |
| Brute Force     | O(n²)  | O(1)  | Small n            |
| Parity Grouping | O(n·k) | O(1)  | Medium k           |
| Window Sliding  | O(n·k) | O(k)  | Small k, streaming |

**Recommended Solution**: Parity grouping with separate even/odd processing (Approach 2).

---

## Key Takeaways

1. **Separate Independent Groups**: Even and odd indices don't interact
2. **Band Constraint**: Limits the search space significantly when k is small
3. **XOR Properties**: Result independent of pair order (associative, commutative)
4. **Optimization**: Process each parity group separately to avoid unnecessary checks
5. **Edge Cases**: Handle k=0, single element, all same values carefully
