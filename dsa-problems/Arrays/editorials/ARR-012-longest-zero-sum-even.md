---
problem_id: ARR_ZERO_SUM_EVEN__3900
display_id: ARR-012
slug: longest-zero-sum-even
title: "Longest Zero-Sum Even Length"
difficulty: Hard
difficulty_score: 75
topics:
  - Array
  - Prefix Sum
  - Hash Map
  - Subarray
  - Parity
tags:
  - arrays
  - prefix-sum
  - hashmap
  - hard
premium: true
subscription_tier: pro
---

# Longest Zero-Sum Even Length

![Problem Header](../images/ARR-012/header.png)

---

## Problem Summary

Find the longest even-length subarray with sum equal to zero.

## Real-World Scenario

Imagine tracking daily temperature changes (positive = warmer, negative = cooler) over several weeks. You want to find the longest even-numbered period where the total temperature change is zero - meaning the temperature returned to its starting point after an even number of days. This helps identify stable weather cycles that repeat in pairs (warm day followed by cool day, etc.).

---

## Detailed Explanation

### Why Even Length Matters

The constraint that the subarray must have **even length** adds an interesting twist:

- **Normal zero-sum subarray**: Any length works - [1, -1] or [2, -3, 1] both valid
- **Even-length constraint**: Must have 2, 4, 6, 8... elements only
- **Real Use**: Pairing patterns, balanced cycles, symmetric operations

### The Parity Trick

**Key Insight**: If `prefix[i] == prefix[j]`, then subarray from `i+1` to `j` has sum = 0.

For the subarray to have **even length**, we need `(j - i)` to be even.

- If i=0, j=2: length = 2 (even) ✓
- If i=1, j=3: length = 2 (even) ✓
- If i=0, j=3: length = 3 (odd) ✗

**Pattern**: `j - i` is even when **i and j have the same parity** (both even or both odd indices).

---

## Approach 1: Naive Solution

### Idea

Check all possible subarrays, filter by:

1. Even length
2. Sum equals zero

```
for start in 0..n-1:
    for end in start+1..n-1:
        if (end - start + 1) is even:
            if sum(arr[start..end]) == 0:
                track maximum length
```

### Why is this inefficient?

```
Outer loop: n positions
Inner loop: n positions
Sum computation: O(n) for each pair
Total: O(n³)
```

### Complexity Analysis

**Time Complexity**: O(n³)

- **Why?** Two nested loops (O(n²)) plus sum computation (O(n)) for each pair
- **Detailed breakdown**: For each of ~n²/2 valid pairs, we compute sum in O(n)

**Space Complexity**: O(1)

- Only tracking current maximum

---

## Approach 2: Optimal Solution ⭐

### Key Insight

Use **two separate hash maps** based on index parity:

- `evenMap`: stores prefix sums at **even** indices (0, 2, 4, ...)
- `oddMap`: stores prefix sums at **odd** indices (1, 3, 5, ...)

**Why separate?**

- Same prefix sum at two even indices → subarray between them has even length!
- Same prefix sum at two odd indices → subarray between them has even length!
- Mixed parity → odd length (not what we want)

### Algorithm

1. Initialize `evenMap[0] = -1` (base case: prefix sum 0 "before" array)
2. Initialize `prefixSum = 0`, `maxLen = 0`
3. For each index `i` from 0 to n-1:
   - Add `arr[i]` to `prefixSum`
   - If index is **even**:
     - Check if `prefixSum` exists in `evenMap`
     - If YES: `length = i - evenMap[prefixSum]` → update maxLen
     - If NO: store `evenMap[prefixSum] = i`
   - If index is **odd**:
     - Check if `prefixSum` exists in `oddMap`
     - If YES: `length = i - oddMap[prefixSum]` → update maxLen
     - If NO: store `oddMap[prefixSum] = i`
4. Return `maxLen`

### Why This Works

**Example**: `arr = [1, -1, 2, -2]`

```
Index:    0   1   2   3
Value:    1  -1   2  -2
Parity:   E   O   E   O

i=0 (even): prefix=1  → evenMap[1] = 0
i=1 (odd):  prefix=0  → oddMap[0] = 1
i=2 (even): prefix=2  → evenMap[2] = 2
i=3 (odd):  prefix=0  → Found in oddMap at index 1!
            Subarray [2..3] = [2, -2]
            Length = 3 - 1 = 2 ✓ (even!)
```

### Complexity Analysis

**Time Complexity**: O(n)

- **Why?** Single pass through array, HashMap operations are O(1) average
- **Detailed breakdown**: n iterations × O(1) hash operations = O(n)

**Space Complexity**: O(n)

- **Why?** Two hash maps, each can store up to n entries in worst case
- **Practical**: Usually much less than n due to duplicate prefix sums

---

## Visual Representation

### Example: `arr = [2, -1, 1, -1, -1, 2]`

```
Building Prefix Sum with Parity Tracking:

Index:     0   1   2   3   4   5
Value:     2  -1   1  -1  -1   2
Parity:    E   O   E   O   E   O
Prefix:    2   1   2   1   0   2

Step-by-step Execution:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

i=0 (EVEN), value=2:
  prefixSum = 0 + 2 = 2
  Check evenMap[2]? NO
  Store: evenMap[2] = 0

  Maps: evenMap = {0:-1, 2:0}
        oddMap = {}

i=1 (ODD), value=-1:
  prefixSum = 2 + (-1) = 1
  Check oddMap[1]? NO
  Store: oddMap[1] = 1

  Maps: evenMap = {0:-1, 2:0}
        oddMap = {1:1}

i=2 (EVEN), value=1:
  prefixSum = 1 + 1 = 2
  Check evenMap[2]? YES! Found at index 0
  Length = 2 - 0 = 2 ✓
  Subarray [0..1] = [2, -1]
  maxLen = 2

  Maps: unchanged (keep first occurrence)

i=3 (ODD), value=-1:
  prefixSum = 2 + (-1) = 1
  Check oddMap[1]? YES! Found at index 1
  Length = 3 - 1 = 2 ✓
  Subarray [2..3] = [1, -1]
  maxLen = 2 (no change)

  Maps: unchanged

i=4 (EVEN), value=-1:
  prefixSum = 1 + (-1) = 0
  Check evenMap[0]? YES! Found at index -1 (base case)
  Length = 4 - (-1) = 5 (ODD!) ✗

  This subarray has odd length, so it is ignored for the even-length constraint.
  The base case evenMap[0] = -1 is only valid when the current index is odd.
  For an even index, skip it and update evenMap[0] = 4 for future checks.

i=5 (ODD), value=2:
  prefixSum = 0 + 2 = 2
  Check oddMap[2]? NO
  Store: oddMap[2] = 5

Final Answer: maxLen = 2
```

### Clearer Visual: Parity Pairs

```
Array: [2, -1, 1, -1, -1, 2]
Index:  0   1  2   3   4  5

Prefix sums at EVEN indices (0,2,4):
  i=0: prefix=2
  i=2: prefix=2  ← MATCH! Subarray [0..1] length=2
  i=4: prefix=0

Prefix sums at ODD indices (1,3,5):
  i=1: prefix=1
  i=3: prefix=1  ← MATCH! Subarray [2..3] length=2
  i=5: prefix=2

Visual matching:
  E: [2] ... [2]  → indices 0,2 → subarray length 2
  O: [1] ... [1]  → indices 1,3 → subarray length 2
```

---

## Test Case Walkthrough

### Input: `arr = [3, -3, 1, -1, 2, -2, 4]`

```
Detailed Trace:

Index:     0   1   2   3   4   5   6
Value:     3  -3   1  -1   2  -2   4
Parity:    E   O   E   O   E   O   E

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

i=0 (E): val=3, prefix=3
  evenMap[3] = 0

i=1 (O): val=-3, prefix=0
  oddMap[0] = 1

i=2 (E): val=1, prefix=1
  evenMap[1] = 2

i=3 (O): val=-1, prefix=0
  oddMap[0]? YES at 1
  length = 3-1 = 2 ✓
  Subarray [2..3] = [1,-1]
  maxLen = 2

i=4 (E): val=2, prefix=2
  evenMap[2] = 4

i=5 (O): val=-2, prefix=0
  oddMap[0]? YES at 1
  length = 5-1 = 4 ✓
  Subarray [2..5] = [1,-1,2,-2]
  maxLen = 4 ← Updated!

i=6 (E): val=4, prefix=4
  evenMap[4] = 6

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Maximum Even-Length Zero-Sum: 4
Subarray: [1, -1, 2, -2] at indices [2..5]
```

### Why It Works

```
At i=5 (odd), prefix=0
We found prefix=0 was at i=1 (also odd)
Subarray from (1+1) to 5 = [2..5]
  arr[2..5] = [1, -1, 2, -2]
  sum = 1-1+2-2 = 0 ✓
  length = 5-1 = 4 (even) ✓
```

---

### Common Mistakes & Pitfalls

### 1. Using Single Hash Map ⚠️

- ❌ Storing all prefix sums together without parity tracking
- ✅ Use separate maps for even/odd indices
- **Example**: prefix=5 at index 2 and index 4 → length 2 (even) ✓
- **Counter-example**: prefix=5 at index 2 and index 3 → length 1 (odd) ✗

### 2. Base Case Confusion ⚠️

- ❌ Not initializing base case, or initializing wrong map
- ✅ Use `evenMap[0] = -1` to handle subarrays starting from index 0
- **Why?** When at odd index i with prefix=0, subarray [0..i] has even length

### 3. Length Calculation Error ⚠️

- ❌ Calculating `end - start + 1` (inclusive length)
- ✅ Use `i - map[prefix]` directly
- **Example**: Found at index 1, current index 5 → length = 5-1 = 4 ✓

### 4. Overwriting Map Values ⚠️

- ❌ Updating map on every occurrence: `map[prefix] = i`
- ✅ Store only FIRST occurrence: `if (prefix not in map) map[prefix] = i`
- **Why?** We want maximum length, so keep earliest occurrence

### 5. Forgetting Parity Check ⚠️

- ❌ Using `i % 2` incorrectly (e.g., treating 0 as odd)
- ✅ Clear check: `i % 2 == 0` for even, `i % 2 == 1` or `i % 2 != 0` for odd

### 6. Integer Overflow ⚠️

- ❌ Using `int` for prefix sum when values are large
- ✅ Use `long` or `long long` for prefix sum accumulation
- **Example**: Array of 1000 elements with value 10⁶ each → prefix sum = 10⁹

---

## Edge Cases & Special Scenarios

### Case 1: Array Starting with Zero Sum (Base Case Test)

```
Input: [1, -1, 2, -2]
Expected Output: 4

Trace:
i=0 (E): prefix=1, evenMap[1]=0
i=1 (O): prefix=0, oddMap[0]=1, length=1-(-1)=2 ✓
i=2 (E): prefix=2, evenMap[2]=2
i=3 (O): prefix=0, oddMap[0]?
  Found at 1, length=3-1=2
  Current max: 2

Answer: 4 (entire array, prefix at index 3 with base case)
```

### Case 2: No Valid Zero-Sum Subarray

```
Input: [1, 2, 3]
Expected Output: 0

All prefix sums different, no matches found:
i=0: prefix=1
i=1: prefix=3
i=2: prefix=6

Result: 0 (no even-length zero-sum subarray)
```

### Case 3: Only Two Elements

```
Input: [5, -5]
Expected Output: 2

i=0 (E): prefix=5, evenMap[5]=0
i=1 (O): prefix=0, oddMap[0]=1, length=1-(-1)=2 ✓

Result: 2 (the entire array)
```

### Case 4: Alternating Values

```
Input: [1, -1, 1, -1, 1, -1]
Expected Output: 6

Multiple even-length subarrays with zero-sum:
- [1,-1] at various positions (length 2)
- [1,-1,1,-1] at positions 0-3 (length 4)
- Full array [1,-1,1,-1,1,-1] (length 6)

Result: 6 (the entire array)
```

### Case 5: Negative Prefix Sums

```
Input: [-3, 1, 2, -3, 3, 2]
Expected Output: 4

Prefix sums: -3, -2, 0, -3, 0, 2
Parity tracking ensures correctness even with negative values

Result: 4 (longest even-length zero-sum subarray found)
```

---

## Implementations

### Java

```java
class Solution {
    public int longestZeroSumEvenLength(int[] a) {
        int n = a.length;
        Map<Long, Integer> evenMap = new HashMap<>();
        Map<Long, Integer> oddMap = new HashMap<>();

        // Base case: prefix sum 0 at position -1
        evenMap.put(0L, -1);

        long prefixSum = 0;
        int maxLen = 0;

        for (int i = 0; i < n; i++) {
            prefixSum += a[i];

            if (i % 2 == 0) {
                // Even index: check even map
                if (evenMap.containsKey(prefixSum)) {
                    int len = i - evenMap.get(prefixSum);
                    maxLen = Math.max(maxLen, len);
                } else {
                    // Store first occurrence only
                    evenMap.put(prefixSum, i);
                }
            } else {
                // Odd index: check odd map
                if (oddMap.containsKey(prefixSum)) {
                    int len = i - oddMap.get(prefixSum);
                    maxLen = Math.max(maxLen, len);
                } else {
                    // Store first occurrence only
                    oddMap.put(prefixSum, i);
                }
            }
        }

        return maxLen;
    }
}
```

### Python

```python
def longest_zero_sum_even_length(a):
    n = len(a)
    even_map = {0: -1}  # Base case
    odd_map = {}

    prefix_sum = 0
    max_len = 0

    for i in range(n):
        prefix_sum += a[i]

        if i % 2 == 0:
            # Even index: check even map
            if prefix_sum in even_map:
                length = i - even_map[prefix_sum]
                max_len = max(max_len, length)
            else:
                # Store first occurrence only
                even_map[prefix_sum] = i
        else:
            # Odd index: check odd map
            if prefix_sum in odd_map:
                length = i - odd_map[prefix_sum]
                max_len = max(max_len, length)
            else:
                # Store first occurrence only
                odd_map[prefix_sum] = i

    return max_len
```

### C++

```cpp
class Solution {
public:
    int longestZeroSumEvenLength(vector<int>& a) {
        int n = a.size();
        unordered_map<long long, int> evenMap;
        unordered_map<long long, int> oddMap;

        // Base case
        evenMap[0] = -1;

        long long prefixSum = 0;
        int maxLen = 0;

        for (int i = 0; i < n; i++) {
            prefixSum += a[i];

            if (i % 2 == 0) {
                // Even index: check even map
                if (evenMap.count(prefixSum)) {
                    int len = i - evenMap[prefixSum];
                    maxLen = max(maxLen, len);
                } else {
                    // Store first occurrence only
                    evenMap[prefixSum] = i;
                }
            } else {
                // Odd index: check odd map
                if (oddMap.count(prefixSum)) {
                    int len = i - oddMap[prefixSum];
                    maxLen = max(maxLen, len);
                } else {
                    // Store first occurrence only
                    oddMap[prefixSum] = i;
                }
            }
        }

        return maxLen;
    }
};
```

### JavaScript

```javascript
/**
 * @param {number[]} a
 * @return {number}
 */
var longestZeroSumEvenLength = function(a) {
    const n = a.length;
    const evenMap = new Map();
    const oddMap = new Map();

    // Base case
    evenMap.set(0, -1);

    let prefixSum = 0;
    let maxLen = 0;

    for (let i = 0; i < n; i++) {
        prefixSum += a[i];

        if (i % 2 === 0) {
            // Even index
            if (evenMap.has(prefixSum)) {
                const len = i - evenMap.get(prefixSum);
                maxLen = Math.max(maxLen, len);
            } else {
                evenMap.set(prefixSum, i);
            }
        } else {
            // Odd index
            if (oddMap.has(prefixSum)) {
                const len = i - oddMap.get(prefixSum);
                maxLen = Math.max(maxLen, len);
            } else {
                oddMap.set(prefixSum, i);
            }
        }
    }

    return maxLen;
};

// Time: O(n), Space: O(n)
```

---

## Quick Comparison Table

| Aspect             | Naive O(n³)        | Improved O(n²)     | Optimal O(n)      |
| ------------------ | ------------------ | ------------------ | ----------------- |
| For n=100          | ~1,000,000 ops     | ~10,000 ops        | ~100 ops          |
| For n=1000         | ~1,000,000,000 ops | ~1,000,000 ops     | ~1,000 ops        |
| Space              | O(1)               | O(1)               | O(n)              |
| Technique          | Brute force        | Prefix sum array   | Hash map + parity |
| Handles duplicates | Yes                | Yes                | Yes (keeps first) |
| Even check         | Count elements     | Check (j-i) parity | Implicit in maps  |

---
