---
title: "Weighted Median of Two Sorted Arrays - Editorial"
slug: weighted-median-two-sorted-editorial
difficulty: Medium
tags: [Median, Binary Search, Sorted Arrays]
---

# Weighted Median of Two Sorted Arrays - Editorial

## Problem Summary

You are given two sorted arrays `A` and `B`. Each element in `A` has a weight `wA` (meaning it appears `wA` times) and each element in `B` has a weight `wB`. You need to find the median of the combined multiset of numbers. If the total number of elements is even, return the average of the two middle elements.

## Real-World Scenario

Imagine you are analyzing **Salary Data** from two different departments.
-   Dept A has `N` distinct salary bands, but each band applies to `wA` employees.
-   Dept B has `M` distinct salary bands, but each band applies to `wB` employees.
-   You want to find the **Median Salary** of the entire company.
-   Since the data is already sorted by salary bands, you don't want to list out every single employee (which could be millions). You want to compute the median directly from the summarized data.

## Problem Exploration

### 1. Total Count and Median Position
-   Let `Total = n * wA + m * wB`.
-   If `Total` is odd, the median is the element at index `Total / 2` (0-indexed).
-   If `Total` is even, the median is the average of elements at `Total / 2 - 1` and `Total / 2`.
-   We need a function `findKth(k)` that returns the `k`-th smallest element in the combined multiset.

### 2. Finding K-th Element in Two Weighted Sorted Arrays
-   This is a variation of the classic "Median of Two Sorted Arrays".
-   However, since elements have weights, we can't just use indices directly.
-   But wait, the weights are *uniform* for each array.
    -   Array A: `A[0]` appears `wA` times, `A[1]` appears `wA` times...
    -   Array B: `B[0]` appears `wB` times...
-   This means the cumulative count of elements from `A` less than or equal to `A[i]` is `(i + 1) * wA`.
-   We can use **Binary Search on the Answer** (Value Range) or **Binary Search on Index**.
-   **Binary Search on Value**:
    -   Range `[min(A[0], B[0]), max(A[n-1], B[m-1])]`.
    -   For a value `V`, count how many elements are `<= V`.
    -   Count = `(upper_bound(A, V) * wA) + (upper_bound(B, V) * wB)`.
    -   If `Count > k`, then the answer is `<= V`.
    -   This works if values are integers and range is small. Constraints say values fit in integer, but range can be large (`10^9`). `log(10^9) = 30` iterations. This is feasible.
-   **Alternative: K-th Element Logic**:
    -   We can binary search on the index of `A`. Suppose we pick `A[i]`.
    -   This `A[i]` is greater than `i` elements in `A` (contributing `i * wA` count).
    -   We can find how many elements in `B` are less than `A[i]` using binary search (`j` elements, contributing `j * wB`).
    -   Total rank of the first copy of `A[i]` is `i * wA + j * wB`.
    -   The last copy of `A[i]` is at rank `(i + 1) * wA + j * wB - 1`.
    -   If `k` falls in this range, `A[i]` is the answer.
    -   We can do this for `A` and `B`.
    -   Since we need the exact value, checking `A` and `B` covers all candidates.
    -   Complexity: `O(log N * log M)` or `O(log N + log M)`.

### 3. Handling Even Total Count
-   If `Total` is even, we need `findKth(Total/2 - 1)` and `findKth(Total/2)`.
-   Usually these are the same or adjacent values.
-   We can call the `findKth` function twice.

### 4. Algorithm Details (Binary Search on Value)
-   Range `[L, R] = [-2e9, 2e9]` (safe bounds).
-   While `L <= R`:
    -   `mid = L + (R - L) / 2`.
    -   `count = countLessEqual(mid)`.
    -   If `count > k`: `ans = mid`, `R = mid - 1`.
    -   Else: `L = mid + 1`.
-   `countLessEqual(val)`:
    -   Find `idxA` such that `A[idxA] <= val` (using `upper_bound` logic). Count `idxA * wA`.
    -   Find `idxB` such that `B[idxB] <= val`. Count `idxB * wB`.
    -   Total count.
-   Complexity: `O(log(Range) * (log N + log M))`.
-   With `Range ~ 2*10^9`, `log Range ~ 31`. `log N ~ 17`. Total ops ~ `31 * 34 ~ 1000`. Very fast.

## Approaches

### Approach 1: Binary Search on Value
-   Since we need to find the `k`-th value, and the function `count(x)` (number of elements <= x) is monotonic, we can binary search for the smallest `x` such that `count(x) > k`.
-   Note: We want the element at 0-based index `k`. This is the `(k+1)`-th smallest. So we look for smallest `x` with `count(x) >= k + 1`.

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public String weightedMedian(int[] A, int[] B, long wA, long wB) {
        long n = A.length;
        long m = B.length;
        long total = n * wA + m * wB;
        
        if (total % 2 == 1) {
            long val = findKth(A, B, wA, wB, total / 2);
            return String.valueOf(val);
        } else {
            long val1 = findKth(A, B, wA, wB, total / 2 - 1);
            long val2 = findKth(A, B, wA, wB, total / 2);
            if ((val1 + val2) % 2 == 0) {
                return String.valueOf((val1 + val2) / 2);
            } else {
                return (val1 + val2) / 2 + ".5";
            }
        }
    }
    
    private long findKth(int[] A, int[] B, long wA, long wB, long k) {
        long low = -2000000000L; // Sufficiently small
        long high = 2000000000L; // Sufficiently large
        long ans = high;
        
        while (low <= high) {
            long mid = low + (high - low) / 2;
            if (countLessEqual(A, B, wA, wB, mid) > k) {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return ans;
    }
    
    private long countLessEqual(int[] A, int[] B, long wA, long wB, long val) {
        long count = 0;
        count += upperBound(A, val) * wA;
        count += upperBound(B, val) * wB;
        return count;
    }
    
    private int upperBound(int[] arr, long val) {
        int l = 0, r = arr.length - 1;
        int res = 0;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (arr[mid] <= val) {
                res = mid + 1;
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        return res;
    }
}
```

### Python

```python
def weighted_median(A: list[int], B: list[int], wA: int, wB: int) -> str:
    n = len(A)
    m = len(B)
    total = n * wA + m * wB
    
    def upper_bound(arr, val):
        l, r = 0, len(arr) - 1
        res = 0
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] <= val:
                res = mid + 1
                l = mid + 1
            else:
                r = mid - 1
        return res

    def count_less_equal(val):
        c = 0
        c += upper_bound(A, val) * wA
        c += upper_bound(B, val) * wB
        return c

    def find_kth(k):
        low, high = -2 * 10**9, 2 * 10**9
        ans = high
        while low <= high:
            mid = (low + high) // 2
            if count_less_equal(mid) > k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

    if total % 2 == 1:
        val = find_kth(total // 2)
        return str(val)
    else:
        val1 = find_kth(total // 2 - 1)
        val2 = find_kth(total // 2)
        s = val1 + val2
        if s % 2 == 0:
            return str(s // 2)
        else:
            return f"{s // 2}.5"
```

### C++

```cpp
#include <vector>
#include <string>
#include <algorithm>
#include <iostream>

using namespace std;

class Solution {
    int upperBound(const vector<int>& arr, long long val) {
        int l = 0, r = arr.size() - 1;
        int res = 0;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (arr[mid] <= val) {
                res = mid + 1;
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        return res;
    }

    long long countLessEqual(const vector<int>& A, const vector<int>& B, long long wA, long long wB, long long val) {
        long long count = 0;
        count += (long long)upperBound(A, val) * wA;
        count += (long long)upperBound(B, val) * wB;
        return count;
    }

    long long findKth(const vector<int>& A, const vector<int>& B, long long wA, long long wB, long long k) {
        long long low = -2000000000LL;
        long long high = 2000000000LL;
        long long ans = high;
        
        while (low <= high) {
            long long mid = low + (high - low) / 2;
            if (countLessEqual(A, B, wA, wB, mid) > k) {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return ans;
    }

public:
    string weightedMedian(const vector<int>& A, const vector<int>& B, long long wA, long long wB) {
        long long n = A.size();
        long long m = B.size();
        long long total = n * wA + m * wB;
        
        if (total % 2 == 1) {
            return to_string(findKth(A, B, wA, wB, total / 2));
        } else {
            long long val1 = findKth(A, B, wA, wB, total / 2 - 1);
            long long val2 = findKth(A, B, wA, wB, total / 2);
            long long sum = val1 + val2;
            if (sum % 2 == 0) {
                return to_string(sum / 2);
            } else {
                return to_string(sum / 2) + ".5";
            }
        }
    }
};
```

### JavaScript

```javascript
class Solution {
  weightedMedian(A, B, wA, wB) {
    // Use BigInt for counts as they can exceed 2^53
    const n = BigInt(A.length);
    const m = BigInt(B.length);
    const bigWA = BigInt(wA);
    const bigWB = BigInt(wB);
    const total = n * bigWA + m * bigWB;
    
    const upperBound = (arr, val) => {
      let l = 0, r = arr.length - 1;
      let res = 0;
      while (l <= r) {
        const mid = Math.floor((l + r) / 2);
        if (arr[mid] <= val) {
          res = mid + 1;
          l = mid + 1;
        } else {
          r = mid - 1;
        }
      }
      return BigInt(res);
    };
    
    const countLessEqual = (val) => {
      let count = 0n;
      count += upperBound(A, val) * bigWA;
      count += upperBound(B, val) * bigWB;
      return count;
    };
    
    const findKth = (k) => {
      let low = -2000000000;
      let high = 2000000000;
      let ans = high;
      
      while (low <= high) {
        const mid = Math.floor((low + high) / 2); // JS bitwise ops are 32-bit, use Math.floor
        if (countLessEqual(mid) > k) {
          ans = mid;
          high = mid - 1;
        } else {
          low = mid + 1;
        }
      }
      return BigInt(ans);
    };
    
    if (total % 2n === 1n) {
      return findKth(total / 2n).toString();
    } else {
      const val1 = findKth(total / 2n - 1n);
      const val2 = findKth(total / 2n);
      const sum = val1 + val2;
      if (sum % 2n === 0n) {
        return (sum / 2n).toString();
      } else {
        return (sum / 2n).toString() + ".5";
      }
    }
  }
}
```

## Test Case Walkthrough

**Input:**
`2 2`
`1 3`
`2 7`
`1 2`

1.  **Setup**: `A=[1, 3]`, `B=[2, 7]`. `wA=1`, `wB=2`.
2.  **Total**: `2*1 + 2*2 = 6`. Even.
3.  **Targets**: `k1 = 6/2 - 1 = 2`. `k2 = 6/2 = 3`.
4.  **Find K=2**:
    -   Try `mid=2`.
    -   `A`: `<=2` is `[1]` (count 1 * 1 = 1).
    -   `B`: `<=2` is `[2]` (count 1 * 2 = 2).
    -   Total `<=2` is 3. `3 > 2`. `ans=2`. `high=1`.
    -   Try `mid=1`. Total `<=1` is 1. `1 <= 2`. `low=2`.
    -   Result `2`.
5.  **Find K=3**:
    -   Try `mid=2`. Total `<=2` is 3. `3 <= 3`. `low=3`.
    -   Try `mid=3`.
    -   `A`: `<=3` is `[1, 3]` (count 2).
    -   `B`: `<=3` is `[2]` (count 2).
    -   Total 4. `4 > 3`. `ans=3`.
    -   Result `3`.
6.  **Average**: `(2 + 3) / 2 = 2.5`.

## Proof of Correctness

-   **Monotonicity**: The count of elements `<= x` is non-decreasing with `x`.
-   **Binary Search**: Correctly finds the smallest `x` such that `count(<= x) > k`. This `x` is the `(k+1)`-th element (0-indexed `k`).
-   **Coverage**: Since we check the combined count from both arrays, we correctly account for all elements and their weights.

## Interview Extensions

1.  **Median of K Sorted Arrays?**
    -   Same logic: Binary search on value, sum counts from all K arrays. `O(K log N * log Range)`.
2.  **Fractional Weights?**
    -   Multiply all weights by a common denominator to make them integers.

## Common Mistakes

-   **Integer Overflow**: Total weight can be large. Use `long long` / `BigInt`.
-   **Binary Search Range**: Ensure range covers all possible input values.
-   **Off-by-one**: `k` is 0-indexed. `count > k` finds the element at index `k`.
