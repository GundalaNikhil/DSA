---
title: Locate Peak with Limited Queries
slug: locate-peak-limited-queries
difficulty: Medium
difficulty_score: 55
tags:
- Binary Search
- Peak Finding
- Searching
problem_id: SRT_LOCATE_PEAK_LIMITED_QUERIES__1358
display_id: SRT-016
topics:
- Searching
- Binary Search
- Peaks
---
# Locate Peak with Limited Queries - Editorial

## Problem Summary

You are given an array `a` of size `n`. A peak element is an element that is strictly greater than its neighbors. You need to find the index of any peak element. The catch is that you should conceptually limit your access to the array to at most `q` queries (where `q` is small, e.g., 20 for `n=100,000`).

## Real-World Scenario

Imagine you are a **Hiker** in a mountain range covered in thick fog.
-   You want to reach a peak (a point higher than its immediate neighbors).
-   You have a GPS that can tell you the altitude at your current location.
-   However, the GPS battery is very low, and you can only check the altitude a few times.
-   You need a strategy to find a peak by checking altitudes at specific points and deciding which direction to move.

## Problem Exploration

### 1. Peak Finding Logic
-   If we pick a random index `mid` and check its neighbors:
    -   If `a[mid] > a[mid+1]` and `a[mid] > a[mid-1]`, `mid` is a peak.
    -   If `a[mid] < a[mid+1]`, then the slope is rising to the right. There must be a peak to the right (eventually it either goes down or hits the boundary, which counts as a peak).
    -   If `a[mid] < a[mid-1]`, then the slope is rising to the left. There must be a peak to the left.
-   This property allows us to discard half of the search space in each step, similar to Binary Search.

### 2. Binary Search Approach
-   Range `[low, high]`.
-   `mid = (low + high) / 2`.
-   Compare `a[mid]` with `a[mid+1]`.
-   If `a[mid] < a[mid+1]`, then a peak exists in `[mid+1, high]`. Set `low = mid + 1`.
-   Else (`a[mid] >= a[mid+1]`), a peak exists in `[low, mid]`. Set `high = mid`.
    -   If `a[mid] > a[mid+1]`, we know the slope is going down to the right.
    -   Does that guarantee a peak to the left?
    -   Yes, because `a[low]` (conceptually `a[-1] = -inf`) starts low. If we go up to `a[mid]` and then down to `a[mid+1]`, there must be a peak in `[low, mid]`.
-   This logic requires only 1 comparison per step (checking `mid` vs `mid+1`).
-   Total queries: `log2(N)`. For `N=100,000`, `log2(N) approx 17`.
-   The constraint `q=20` fits perfectly.

### 3. Edge Cases
-   `n=1`: Peak is index 0.
-   `n=2`: Compare `a[0]` and `a[1]`.
-   Peak at ends: Handled correctly by the logic.
-   Plateaus (`a[mid] == a[mid+1]`): The problem says "strictly greater" for peak. If neighbors are equal, it's not a peak?
    -   Problem statement says "at least one peak... a[i] > a[i-1] and a[i] > a[i+1]".
    -   If array is `[2, 2, 2]`, no peak?
    -   Constraints usually imply no adjacent equal elements for standard peak finding, OR the definition allows `>=`.
    -   The problem says "strictly greater". If `[2, 2, 2]`, no peak exists. But "An array has at least one peak". This implies inputs won't be flat like that, or at least one strict peak exists.
    -   If `a[mid] == a[mid+1]`, we can't strictly say which side has a peak.
    -   However, many peak finding problems guarantee adjacent elements are distinct.
    -   If not distinct, we might need linear search in worst case.
    -   Given `q=20`, we can assume inputs allow `O(log N)`. We'll assume we can go either way or `a[mid] != a[mid+1]`.
    -   If `a[mid] == a[mid+1]`, we technically don't know. But standard binary search peak finding on LeetCode (162) allows `a[i] != a[i+1]`.
    -   If duplicates exist, worst case is `O(N)`. But with `q` limit, we must assume "nice" inputs or `a[mid] != a[mid+1]`.

## Approaches

### Approach 1: Binary Search
-   Iterative binary search.
-   Compare `mid` and `mid+1`.
-   Complexity: `O(log N)`.

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public int findPeak(int[] arr, int qLimit) {
        int n = arr.length;
        int low = 0;
        int high = n - 1;
        
        while (low < high) {
            int mid = low + (high - low) / 2;
            // We access mid and mid+1.
            // Since low < high, mid is at least 0 and at most n-2.
            // So mid+1 is valid.
            if (arr[mid] < arr[mid+1]) {
                // Rising slope, peak must be to the right
                low = mid + 1;
            } else {
                // Falling slope or peak, peak is at mid or left
                high = mid;
            }
        }
        return low;
    }
}
```

### Python

```python
def find_peak(arr: list[int], q_limit: int) -> int:
    n = len(arr)
    low = 0
    high = n - 1
    
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < arr[mid+1]:
            low = mid + 1
        else:
            high = mid
            
    return low
```

### C++

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int findPeak(const vector<int>& arr, int qLimit) {
        int n = arr.size();
        int low = 0;
        int high = n - 1;
        
        while (low < high) {
            int mid = low + (high - low) / 2;
            if (arr[mid] < arr[mid+1]) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }
        return low;
    }
};
```

### JavaScript

```javascript
class Solution {
  findPeak(arr, qLimit) {
    let low = 0;
    let high = arr.length - 1;
    
    while (low < high) {
      const mid = Math.floor((low + high) / 2);
      if (arr[mid] < arr[mid + 1]) {
        low = mid + 1;
      } else {
        high = mid;
      }
    }
    return low;
  }
}
```

## Test Case Walkthrough

**Input:**
`5 5`
`1 3 2 4 1`

1.  `low=0, high=4`. `mid=2` (val 2).
2.  `arr[2] (2) < arr[3] (4)`.
3.  `low = 3`.
4.  `low=3, high=4`. `mid=3` (val 4).
5.  `arr[3] (4) > arr[4] (1)`. (Else branch).
6.  `high = 3`.
7.  `low=3, high=3`. Loop ends.
8.  **Result**: 3. (Value 4 is a peak).
    -   Both 1 and 3 are valid peaks. My algorithm found 3.
    -   The problem says "any peak index". So 3 is correct.
    -   If I want to find 1? The binary search path depends on `mid`.
    -   Initial `mid=2` (val 2). `2 < 4`. We went right.
    -   If we checked `mid=1` (val 3)? `3 > 2`. We go left. `high=1`. `low=0`. `mid=0`. `1 < 3`. `low=1`. Result 1.
    -   Both are correct.

## Proof of Correctness

-   **Invariant**: At start of each loop, a peak exists in `[low, high]`.
-   **Base Case**: `[0, n-1]` contains a peak (given).
-   **Step**:
    -   If `a[mid] < a[mid+1]`, the subarray `[mid+1, high]` starts with a value larger than its left neighbor `a[mid]`. Since `a[high]` (or boundary) eventually drops, a peak must exist in `[mid+1, high]`.
    -   If `a[mid] >= a[mid+1]`, the subarray `[low, mid]` ends with a value larger than its right neighbor `a[mid+1]`. Since `a[low]` starts low, a peak must exist in `[low, mid]`.
-   **Termination**: Range shrinks by half each time. Converges to length 1.

## Interview Extensions

1.  **2D Peak Finding?**
    -   `O(N log M)` or `O(N)` algorithms exist.
2.  **Multiple Peaks?**
    -   Find all? `O(N)`. Find specific one? Harder.

### Common Mistakes

-   **Index Out of Bounds**: Accessing `mid+1` when `mid=n-1`. Loop condition `low < high` prevents this (mid is always `< high`).
-   **Infinite Loop**: `high = mid - 1` vs `high = mid`. Since we check `mid < mid+1`, if condition false, `mid` could be the peak, so we must keep `mid`. `high = mid`.
