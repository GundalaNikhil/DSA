---
problem_id: ARR_SLIDE_MAX__14AE
display_id: ARR-016
slug: power-window-drop
title: "Power Window With Drop"
difficulty: Hard
difficulty_score: 75
topics:
  - Array
  - Sliding Window
  - Optimization
  - Maximum Subarray
  - Greedy
  - Dynamic Programming
tags:
  - arrays
  - sliding-window
  - greedy
  - hard
premium: true
subscription_tier: pro
---

# Power Window With Drop

![Problem Header](../images/ARR-016/header.png)

---

## Real-World Scenario 🎯

**Sprint Planning with Buffer Days**

Imagine you're a project manager planning a software sprint. You have **n consecutive work days** with varying **productivity scores** (some days might be negative due to technical debt, meetings, or blockers). You need to select a **sprint of exactly k days** to maximize team output.

However, you have a **"skip day" policy**: within the selected k-day sprint, you can designate **one day as a planning/buffer day** (dropping it from productivity calculation) if it helps the overall output.

**Example**: Days = [3, -2, 5, 1, -1, 4], k = 4

- Window [3, -2, 5, 1]: Sum = 7, but dropping -2 gives 11 ✅
- Window [-2, 5, 1, -1]: Sum = 3, but dropping -2 gives 8
- Window [5, 1, -1, 4]: Sum = 9, but dropping -1 gives 10

**Answer**: Maximum productivity = 11 (first window, dropping the -2 day)

---

## Problem Statement

Given an array `arr` of `n` integers and an integer `k`, find the **maximum sum** of a contiguous subarray of length `k`, with the option to **drop one element** from that window.

**Constraints**:

- You must select exactly k consecutive elements
- You can drop at most 1 element (not required if sum is already maximum)
- If k = 1, you cannot drop (return the element itself)
- Array can contain negative numbers

---

## Why This Problem is Challenging 🤔

1. **Dual Decision**: For each window, you need to decide:

   - Should I drop an element?
   - If yes, which element should I drop? (Always the minimum!)

2. **Sliding Window Variation**: Standard sliding window maintains sum, but here you also need to track the minimum in each window

3. **Edge Cases**:

   - What if all elements are negative? (Drop the least negative/minimum)
   - What if k = 1? (Cannot drop)
   - What if dropping makes it worse? (All elements positive and large)

4. **Optimization Challenge**: Naive solution recalculates everything for each window (O(n×k)). Optimal solution should slide efficiently in O(n).

---

## Approach 1: Naive Solution (Brute Force)

### Idea

For every possible window of size k:

1. Calculate the sum of all k elements
2. Try dropping each of the k elements one by one
3. Track the maximum sum achieved (with or without dropping)

### Why It's Inefficient

- For each window, we recalculate sum from scratch: **O(k) per window**
- We try dropping each element: **O(k) comparisons per window**
- Total: **O(n × k)** for n-k+1 windows

### Complexity Analysis

**Time Complexity**: **O(n × k)**

- **Why?** We have (n - k + 1) windows, and for each window:
  - Calculate sum: O(k)
  - Find minimum to drop: O(k)
  - Total per window: O(k)
  - Overall: O((n-k+1) × k) ≈ O(n × k)

**Space Complexity**: **O(1)**

- Only using variables for sum, min, and max tracking

---

## Approach 2: Optimal Sliding Window ⭐

### Key Insight 💡

**Always drop the minimum element in the window** (if it improves the sum).

Why? Because dropping the minimum element removes the least value, maximizing the remaining sum.

**Optimization**: Instead of recalculating everything for each window:

1. Use **sliding window** to maintain sum in O(1) per slide
2. Track the **minimum element** in the current window
3. For each window, compare:
   - Sum with all elements: `windowSum`
   - Sum after dropping min: `windowSum - minElement`

### Algorithm Steps

```
1. Initialize first window (indices 0 to k-1):
   - Calculate windowSum
   - Find minElement in window

2. For the first window:
   - maxResult = max(windowSum, windowSum - minElement)

3. Slide window from index k to n-1:
   - Remove arr[i-k] from windowSum
   - Add arr[i] to windowSum
   - Recalculate minElement in new window (check all k elements)
   - Update maxResult = max(maxResult, windowSum, windowSum - minElement)

4. Return maxResult
```

### Why This is Optimal

- **Window sum update**: O(1) per slide (add new, remove old)
- **Min tracking**: O(k) per window (scan k elements)
  - _Note_: Can be optimized to O(1) using a deque/heap, but for simplicity, O(k) is acceptable
- **Total**: O(n × k) in worst case, but with efficient sliding and early comparisons

**Better Optimization**: Use a **deque** or **multiset** to maintain minimum in O(log k) per update, achieving **O(n log k)** overall.

### Detailed Complexity Analysis

**Time Complexity**: **O(n × k)** (basic sliding window) or **O(n log k)** (with deque/heap)

- **Basic approach** (as implemented below):

  - First window: O(k) to calculate sum and min
  - Sliding: O(n) iterations, each requiring O(k) to find new min
  - Total: O(n × k)

- **Advanced approach** (using deque for min tracking):
  - Maintain a deque of indices in increasing order of values
  - Each element added/removed once: O(n)
  - Total: O(n)

**Space Complexity**: **O(1)** for basic approach, **O(k)** if using deque

---

## Visual Representation 📊

### Example: arr = [3, -2, 5, 1, -1, 4], k = 4

```
Sliding Window Analysis:
========================

Initial Array:
Index:   0   1   2   3   4   5
Value: [ 3, -2,  5,  1, -1,  4 ]

Window 1: Indices [0, 1, 2, 3]
┌─────────────────────────┐
│  3  │ -2  │  5  │  1  │ -1  │  4
└─────────────────────────┘
Sum = 3 + (-2) + 5 + 1 = 7
Min = -2
Drop min? 7 - (-2) = 9 ✅ (better!)
Best for this window: 9

Window 2: Indices [1, 2, 3, 4]
       ┌─────────────────────────┐
  3  │ -2  │  5  │  1  │ -1  │  4
       └─────────────────────────┘
Sum = -2 + 5 + 1 + (-1) = 3
Min = -2
Drop min? 3 - (-2) = 5 ✅ (better!)
Best for this window: 5

Window 3: Indices [2, 3, 4, 5]
              ┌─────────────────────────┐
  3   -2   5  │  1  │ -1  │  4
              └─────────────────────────┘
Sum = 5 + 1 + (-1) + 4 = 9
Min = -1
Drop min? 9 - (-1) = 10 ✅ (better!)
Best for this window: 10

MAXIMUM ACROSS ALL WINDOWS: 10
```

### Decision Tree for Window 1:

```
Window [3, -2, 5, 1]
         │
    ┌────┴────┐
    │         │
Keep All    Drop One
 Sum=7      Which?
            │
    ┌───┬───┼───┬───┐
    │   │   │   │   │
  Drop3 Drop-2 Drop5 Drop1
  Sum=4 Sum=9  Sum=2 Sum=6
         ↑
      BEST!
```

---

## Test Case Walkthrough 🔍

### Test Case: arr = [3, -2, 5, 1, -1, 4], k = 4

**Step-by-Step Execution:**

**Initialization:**

```
n = 6, k = 4
maxResult = -∞
```

**Window 1: [3, -2, 5, 1] (indices 0-3)**

```
windowSum = 3 + (-2) + 5 + 1 = 7
minElement = min(3, -2, 5, 1) = -2

Option A: Keep all elements → sum = 7
Option B: Drop minimum (-2) → sum = 7 - (-2) = 9 ✅

maxResult = max(-∞, 7, 9) = 9
```

**Slide to Window 2: [-2, 5, 1, -1] (indices 1-4)**

```
Remove arr[0] = 3: windowSum = 7 - 3 = 4
Add arr[4] = -1: windowSum = 4 + (-1) = 3
minElement = min(-2, 5, 1, -1) = -2

Option A: Keep all → sum = 3
Option B: Drop -2 → sum = 3 - (-2) = 5

maxResult = max(9, 3, 5) = 9 (unchanged)
```

**Slide to Window 3: [5, 1, -1, 4] (indices 2-5)**

```
Remove arr[1] = -2: windowSum = 3 - (-2) = 5
Add arr[5] = 4: windowSum = 5 + 4 = 9
minElement = min(5, 1, -1, 4) = -1

Option A: Keep all → sum = 9
Option B: Drop -1 → sum = 9 - (-1) = 10 ✅

maxResult = max(9, 9, 10) = 10
```

**Final Answer: 10**

---

### C++ommon Mistakes & Pitfalls ⚠️

### 1. **Not Considering the "Keep All" Option**

❌ **Wrong**: Always drop the minimum

```java
// BUG: What if all elements are positive and large?
return windowSum - minElement;
```

✅ **Correct**: Compare both options

```java
maxResult = Math.max(maxResult, windowSum);        // Keep all
maxResult = Math.max(maxResult, windowSum - minElement);  // Drop min
```

**Why?** If window = [10, 12, 15, 11], dropping min (10) gives 38, but keeping all gives 48!

---

### 2. **Forgetting the k=1 Edge Case**

❌ **Wrong**: Try to drop even when k=1

```java
// BUG: If k=1, we can't drop anything!
maxResult = Math.max(windowSum, windowSum - minElement);
```

✅ **Correct**: Handle k=1 separately

```java
if (k == 1) {
    return Arrays.stream(arr).max().getAsInt();
}
```

**Why?** With k=1, the "window" is a single element—you can't drop it!

---

### 3. **Incorrect Minimum Tracking After Sliding**

❌ **Wrong**: Update min incrementally

```java
// BUG: Removed element might have been the min!
windowSum = windowSum - arr[i-k] + arr[i];
if (arr[i] < minElement) minElement = arr[i];  // INCOMPLETE!
```

✅ **Correct**: Recalculate min for the entire new window

```java
windowSum = windowSum - arr[i-k] + arr[i];
minElement = Integer.MAX_VALUE;
for (int j = i-k+1; j <= i; j++) {
    minElement = Math.min(minElement, arr[j]);
}
```

**Why?** If you remove the old minimum, you must rescan the window to find the new minimum.

---

### 4. **Off-by-One Errors in Window Bounds**

❌ **Wrong**: Incorrect loop bounds

```java
for (int i = k; i < n; i++) {  // Missing last window!
```

✅ **Correct**: Include all windows

```java
for (int i = k; i <= n - 1; i++) {
    // Or: for (int i = 0; i <= n - k; i++)
}
```

---

### 5. **Integer Overflow with Large Sums**

❌ **Wrong**: Using int for large arrays

```java
int windowSum = 0;  // May overflow if k is large
```

✅ **Correct**: Use long for sum calculations

```java
long windowSum = 0;
long maxResult = Long.MIN_VALUE;
```

**Why?** If k=1000 and all elements are 10^6, sum could exceed Integer.MAX_VALUE.

---

### 6. **Not Handling All-Negative Arrays**

❌ **Wrong**: Initializing maxResult to 0

```java
int maxResult = 0;  // BUG: What if all sums are negative?
```

✅ **Correct**: Use MIN_VALUE

```java
int maxResult = Integer.MIN_VALUE;
```

**Why?** If array is [-5, -3, -8], answer is -3 (not 0).

---

---

## Implementations

### Java (Basic Sliding Window - O(n × k))

```java
class Solution {
    public int maxWindowSumWithDrop(int[] arr, int k) {
        int n = arr.length;

        // Edge case: k=1, can't drop anything
        if (k == 1) {
            int max = arr[0];
            for (int val : arr) {
                max = Math.max(max, val);
            }
            return max;
        }

        if (n < k) return 0;  // Invalid case

        // Initialize first window (indices 0 to k-1)
        int windowSum = 0;
        int minElement = Integer.MAX_VALUE;

        for (int i = 0; i < k; i++) {
            windowSum += arr[i];
            minElement = Math.min(minElement, arr[i]);
        }

        // Check first window: keep all vs drop min
        int maxResult = Math.max(windowSum, windowSum - minElement);

        // Slide the window from index k to n-1
        for (int i = k; i < n; i++) {
            // Remove leftmost element of previous window
            windowSum -= arr[i - k];

            // Add new element to window
            windowSum += arr[i];

            // Recalculate minimum in the new window
            // We need to scan all k elements in current window [i-k+1, i]
            minElement = Integer.MAX_VALUE;
            for (int j = i - k + 1; j <= i; j++) {
                minElement = Math.min(minElement, arr[j]);
            }

            // Update maxResult: compare keep-all vs drop-min
            maxResult = Math.max(maxResult, windowSum);
            maxResult = Math.max(maxResult, windowSum - minElement);
        }

        return maxResult;
    }
}
```

### Java (Optimized with Deque - O(n))

```java
import java.util.*;

class SolutionOptimized {
    public int maxWindowSumWithDrop(int[] arr, int k) {
        int n = arr.length;
        if (k == 1) {
            return Arrays.stream(arr).max().getAsInt();
        }
        if (n < k) return 0;

        // Deque to maintain indices of minimum elements
        // Front of deque always has index of current window's minimum
        Deque<Integer> deque = new LinkedList<>();

        int windowSum = 0;
        int maxResult = Integer.MIN_VALUE;

        // Process first k elements
        for (int i = 0; i < k; i++) {
            windowSum += arr[i];

            // Remove elements from back while current element is smaller
            while (!deque.isEmpty() && arr[deque.peekLast()] >= arr[i]) {
                deque.pollLast();
            }
            deque.offerLast(i);
        }

        // Check first window
        int minElement = arr[deque.peekFirst()];
        maxResult = Math.max(windowSum, windowSum - minElement);

        // Slide the window
        for (int i = k; i < n; i++) {
            // Remove element going out of window
            windowSum -= arr[i - k];

            // Remove indices outside current window from deque
            while (!deque.isEmpty() && deque.peekFirst() <= i - k) {
                deque.pollFirst();
            }

            // Add new element
            windowSum += arr[i];

            // Maintain deque property for new element
            while (!deque.isEmpty() && arr[deque.peekLast()] >= arr[i]) {
                deque.pollLast();
            }
            deque.offerLast(i);

            // Get minimum from deque front
            minElement = arr[deque.peekFirst()];

            // Update result
            maxResult = Math.max(maxResult, windowSum);
            maxResult = Math.max(maxResult, windowSum - minElement);
        }

        return maxResult;
    }
}
```

### Python (Basic Approach)

```python
def max_window_sum_with_drop(arr, k):
    """
    Find maximum sum of k-length window with option to drop one element.

    Time: O(n * k)
    Space: O(1)
    """
    n = len(arr)

    # Edge case: k=1, cannot drop
    if k == 1:
        return max(arr)

    if n < k:
        return 0

    # Initialize first window
    window_sum = sum(arr[:k])
    min_element = min(arr[:k])

    # Check first window
    max_result = max(window_sum, window_sum - min_element)

    # Slide window
    for i in range(k, n):
        # Update sum: remove left, add right
        window_sum = window_sum - arr[i - k] + arr[i]

        # Recalculate minimum in new window
        min_element = min(arr[i - k + 1:i + 1])

        # Update result
        max_result = max(max_result, window_sum, window_sum - min_element)

    return max_result
```

### Python (Optimized with Deque)

```python
from collections import deque

def max_window_sum_with_drop_optimized(arr, k):
    """
    Optimized using deque for O(n) minimum tracking.

    Time: O(n)
    Space: O(k)
    """
    n = len(arr)

    if k == 1:
        return max(arr)

    if n < k:
        return 0

    # Deque stores indices in increasing order of values
    dq = deque()
    window_sum = 0
    max_result = float('-inf')

    # Initialize first window
    for i in range(k):
        window_sum += arr[i]

        # Maintain increasing order of values
        while dq and arr[dq[-1]] >= arr[i]:
            dq.pop()
        dq.append(i)

    # Check first window
    min_element = arr[dq[0]]
    max_result = max(window_sum, window_sum - min_element)

    # Slide window
    for i in range(k, n):
        # Remove leftmost element
        window_sum -= arr[i - k]

        # Remove indices outside window
        while dq and dq[0] <= i - k:
            dq.popleft()

        # Add new element
        window_sum += arr[i]

        # Maintain deque invariant
        while dq and arr[dq[-1]] >= arr[i]:
            dq.pop()
        dq.append(i)

        # Get minimum
        min_element = arr[dq[0]]

        # Update result
        max_result = max(max_result, window_sum, window_sum - min_element)

    return max_result
```

### C++ (Basic Approach)

```cpp
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

class Solution {
public:
    int maxWindowSumWithDrop(vector<int>& arr, int k) {
        int n = arr.size();

        // Edge case: k=1
        if (k == 1) {
            return *max_element(arr.begin(), arr.end());
        }

        if (n < k) return 0;

        // Initialize first window
        int windowSum = 0;
        int minElement = INT_MAX;

        for (int i = 0; i < k; i++) {
            windowSum += arr[i];
            minElement = min(minElement, arr[i]);
        }

        // Check first window
        int maxResult = max(windowSum, windowSum - minElement);

        // Slide window
        for (int i = k; i < n; i++) {
            // Update sum
            windowSum = windowSum - arr[i - k] + arr[i];

            // Recalculate minimum in current window [i-k+1, i]
            minElement = INT_MAX;
            for (int j = i - k + 1; j <= i; j++) {
                minElement = min(minElement, arr[j]);
            }

            // Update result
            maxResult = max({maxResult, windowSum, windowSum - minElement});
        }

        return maxResult;
    }
};
```

### C++ (Optimized with Deque)

```cpp
#include <vector>
#include <deque>
#include <algorithm>
using namespace std;

class SolutionOptimized {
public:
    int maxWindowSumWithDrop(vector<int>& arr, int k) {
        int n = arr.size();

        if (k == 1) {
            return *max_element(arr.begin(), arr.end());
        }

        if (n < k) return 0;

        deque<int> dq;  // Stores indices
        int windowSum = 0;
        int maxResult = INT_MIN;

        // Initialize first window
        for (int i = 0; i < k; i++) {
            windowSum += arr[i];

            // Maintain increasing order
            while (!dq.empty() && arr[dq.back()] >= arr[i]) {
                dq.pop_back();
            }
            dq.push_back(i);
        }

        // Check first window
        int minElement = arr[dq.front()];
        maxResult = max({windowSum, windowSum - minElement});

        // Slide window
        for (int i = k; i < n; i++) {
            // Remove leftmost
            windowSum -= arr[i - k];

            // Remove out-of-window indices
            while (!dq.empty() && dq.front() <= i - k) {
                dq.pop_front();
            }

            // Add new element
            windowSum += arr[i];

            // Maintain deque
            while (!dq.empty() && arr[dq.back()] >= arr[i]) {
                dq.pop_back();
            }
            dq.push_back(i);

            // Get minimum
            minElement = arr[dq.front()];

            // Update result
            maxResult = max({maxResult, windowSum, windowSum - minElement});
        }

        return maxResult;
    }
};
```

### JavaScript (Optimized with Deque)

```javascript
/**
 * @param {number[]} arr
 * @param {number} k
 * @return {number}
 */
var maxWindowSumWithDrop = function(arr, k) {
    const n = arr.length;

    if (k === 1) {
        return Math.max(...arr);
    }

    if (n < k) return 0;

    // Deque stores indices in increasing order of values
    const dq = [];
    let windowSum = 0;
    let maxResult = -Infinity;

    // Initialize first window
    for (let i = 0; i < k; i++) {
        windowSum += arr[i];

        // Maintain increasing order
        while (dq.length > 0 && arr[dq[dq.length - 1]] >= arr[i]) {
            dq.pop();
        }
        dq.push(i);
    }

    // Check first window
    let minElement = arr[dq[0]];
    maxResult = Math.max(windowSum, windowSum - minElement);

    // Slide window
    for (let i = k; i < n; i++) {
        // Remove leftmost
        windowSum -= arr[i - k];

        // Remove out-of-window indices
        while (dq.length > 0 && dq[0] <= i - k) {
            dq.shift();
        }

        // Add new element
        windowSum += arr[i];

        // Maintain deque
        while (dq.length > 0 && arr[dq[dq.length - 1]] >= arr[i]) {
            dq.pop();
        }
        dq.push(i);

        // Get minimum
        minElement = arr[dq[0]];

        // Update result
        maxResult = Math.max(maxResult, windowSum, windowSum - minElement);
    }

    return maxResult;
};

// Time: O(n), Space: O(k)
```

---

## Quick Comparison Table 📊

| Approach                 | Time Complexity | Space Complexity | When to Use                   | Pros                               | Cons                       |
| ------------------------ | --------------- | ---------------- | ----------------------------- | ---------------------------------- | -------------------------- |
| **Brute Force**          | O(n × k²)       | O(1)             | k ≤ 5, n ≤ 100                | Simple to implement                | Too slow for large inputs  |
| **Basic Sliding Window** | O(n × k)        | O(1)             | k ≤ 1000, n ≤ 10⁵             | Easy to understand, no extra space | Recalculates min each time |
| **Deque Optimization**   | O(n)            | O(k)             | All cases, especially large k | Fastest, handles n=10⁶             | More complex code          |

### Performance Example:

- **Input**: n = 100,000, k = 1,000
- **Brute Force**: ~100 billion operations ❌ (timeout)
- **Basic Sliding**: ~100 million operations ⚠️ (slow but works)
- **Deque Optimized**: ~100,000 operations ✅ (instant)

---

## Tags

`#arrays` `#sliding-window` `#optimization` `#greedy` `#deque` `#monotonic-queue` `#dynamic-window` `#maximum-subarray` `#drop-element` `#medium` `#interview-favorite` `#google` `#facebook`

