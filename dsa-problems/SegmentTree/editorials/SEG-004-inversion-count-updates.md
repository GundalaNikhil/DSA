---
title: Inversion Count Updates
slug: inversion-count-updates
difficulty: Medium
difficulty_score: 58
tags:
- Inversion Count
- Fenwick Tree
- Segment Tree
problem_id: SEG_INVERSION_COUNT_UPDATES__5048
display_id: SEG-004
topics:
- Segment Tree
- Fenwick Tree
- Inversions
---
# Inversion Count Updates - Editorial

## Problem Summary

You are given an array `a`. You need to process `q` updates. Each update changes the value at a specific index `i` to `x`. After each update, you must output the total number of inversions in the array. An inversion is a pair `(i, j)` such that `i < j` and `a[i] > a[j]`.


## Constraints

- `1 <= n, q <= 200000`
- `-10^9 <= a[i], x <= 10^9`
- Indices are 0-based
## Real-World Scenario

Imagine a **Ranking System**. You have a list of players ranked by their current score. An "inversion" represents a pair of players where the one listed earlier actually has a higher score (if the list is supposed to be ascending) or vice-versa. When a player's score changes, you want to know how "unsorted" the list has become without re-scanning everyone.

## Problem Exploration

### 1. Naive Approach
After each update, recalculate inversions in `O(N^2)` or `O(N log N)`. With `Q` updates, this is `O(Q * N log N)`, which is too slow given `N, Q <= 200,000`.

### 2. Incremental Updates
When we change `a[i]` from `old_val` to `new_val`, how does the inversion count change?
Only pairs involving index `i` are affected.
-   **Pairs (j, i) where j < i**:
    -   If `a[j] > old_val`, we lose an inversion.
    -   If `a[j] > new_val`, we gain an inversion.
-   **Pairs (i, k) where i < k**:
    -   If `old_val > a[k]`, we lose an inversion.
    -   If `new_val > a[k]`, we gain an inversion.

So, `new_inversions = old_inversions - (inversions involving old a[i]) + (inversions involving new a[i])`.

### 3. Calculating Affected Inversions
To efficiently count `j < i` with `a[j] > val` or `k > i` with `val > a[k]`, we can use a data structure.
However, standard Fenwick/Segment trees count values in a range.
This problem is tricky because we need to count values *by index* and *by value*.
This looks like a 2D range query problem, or we can use **Square Root Decomposition** (Block Decomposition).
Can we do better? `O(Q log^2 N)`?
1.  Count `j < i` such that `a[j] > val`.
2.  Count `k > i` such that `a[k] < val`.
This requires a data structure that supports:
-   `update(index, val)`
-   `query_greater(index_range, value)`
-   `query_smaller(index_range, value)`

This is exactly what a **Merge Sort Tree** or **Segment Tree over Fenwick Tree** supports, but updates are hard.
Divide array into blocks of size `sqrtN`.
For each block, maintain a sorted version of its elements.
Update:
-   Remove `old_val` from block's sorted list.
-   Insert `new_val`.
-   This takes `O(sqrtN)`.
Query:
-   For blocks fully to left/right: binary search in sorted list (`O(log sqrtN)`).
-   For partial blocks: iterate (`O(sqrtN)`).
Total per update: `O(sqrtN log N)`. With `N=200,000`, `sqrtN ~= 450`. `450 x 18 ~= 8000`. `200,000 x 8000 ~= 1.6 x 10^9`. Might be tight for 2 seconds.

**Alternative approaches:**
- Coordinate Compression + Fenwick Tree would maintain frequencies of values but loses index information.
- Fenwick Tree over indices would maintain values but cannot efficiently count by value ranges.

For "Medium" difficulty with values up to `10^9` and 0-based indices, **Square Root Decomposition** (Block Decomposition) achieves `O(Q sqrtN log N)` complexity.

The key insight: count `j < i` with `a[j] > x` is essentially a 2D range sum query - counting points in rectangle `[0, i-1] x [x+1, infinity]`. While dynamic 2D range sums are complex, Square Root Decomposition provides an efficient solution for this difficulty level.

Let's refine the Square Root Decomposition approach.
Block size `B ~= sqrtN log N` or just `sqrtN`.
Maintain `blocks[b]` as a sorted list of values in that block.
To update `a[i]` from `u` to `v`:
1.  Calculate contribution of `u` to inversions (remove it).
    -   Iterate blocks to left: count elements `> u`.
    -   Iterate blocks to right: count elements `< u`.
    -   Iterate within `i`'s block: brute force.
2.  Update `a[i] = v`. Update block's sorted list.
3.  Calculate contribution of `v` to inversions (add it).
    -   Iterate blocks to left: count elements `> v`.
    -   Iterate blocks to right: count elements `< v`.
    -   Iterate within `i`'s block: brute force.

Complexity: `O(fracNB log B + B)`.
If `B = sqrtN log N`, this is efficient.
For `N=200,000`, `B ~= 1000`.
Operations: `200 x 10 + 1000 ~= 3000`.
`200,000 x 3000 = 6 x 10^8`.
This should pass in C++/Java. Python might struggle.

## Approaches

### Approach 1: Square Root Decomposition
1.  Divide array into blocks of size `K`.
2.  For each block, keep a sorted version `sorted_blocks[b]`.
3.  **Initial Inversions**: Compute using Fenwick Tree (`O(N log N)`).
4.  **Update(i, x)**:
    -   Let `old = a[i]`.
    -   **Subtract** inversions caused by `old` at `i`.
        -   Left blocks: `count > old`. (Binary search in sorted blocks).
        -   Right blocks: `count < old`.
        -   Same block: iterate elements.
    -   **Update** `a[i] = x`. Update `sorted_blocks[i/K]`.
    -   **Add** inversions caused by `x` at `i`.
        -   Left blocks: `count > x`.
        -   Right blocks: `count < x`.
        -   Same block: iterate elements.
    -   Update total count.

### Approach 2: Fenwick Tree (Offline)
If we process queries offline, we can use CDQ Divide and Conquer, but that's for static 2D range sums or batch updates. Here updates are dependent.
So Square Root Decomposition is the most viable online approach.

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public List<Long> process(int[] arr, List<int[]> updates) {
        int n = arr.length;
        int blockSize = (int) Math.sqrt(n * Math.log(n + 1) / Math.log(2)) + 1;
        if (blockSize < 50) blockSize = 50; // Heuristic lower bound
        
        int numBlocks = (n + blockSize - 1) / blockSize;
        List<List<Integer>> blocks = new ArrayList<>();
        for (int i = 0; i < numBlocks; i++) blocks.add(new ArrayList<>());
        
        for (int i = 0; i < n; i++) {
            blocks.get(i / blockSize).add(arr[i]);
        }
        
        for (List<Integer> b : blocks) Collections.sort(b);
        
        // Initial inversion count using Merge Sort or BIT
        long currentInversions = countInversions(arr);
        List<Long> results = new ArrayList<>();
        
        for (int[] up : updates) {
            int idx = up[0];
            int val = up[1];
            int oldVal = arr[idx];
            
            if (val == oldVal) {
                results.add(currentInversions);
                continue;
            }
            
            int bIdx = idx / blockSize;
            
            // Remove contribution of oldVal
            currentInversions -= countGreaterLeft(blocks, arr, idx, oldVal, blockSize);
            currentInversions -= countSmallerRight(blocks, arr, idx, oldVal, blockSize);
            
            // Update structures
            arr[idx] = val;
            List<Integer> block = blocks.get(bIdx);
            // Remove oldVal using binary search to find index
            int pos = Collections.binarySearch(block, oldVal);
            // binarySearch might return any index if duplicates, but we just need to remove one instance.
            // However, we must ensure we remove the correct instance? Values are identical, so any instance works.
            // But Collections.binarySearch returns arbitrary index.
            if (pos < 0) pos = -pos - 1; // Should be found though
            // If duplicates exist, binarySearch returns one of them.
            // We need to iterate to find one if binarySearch isn't guaranteed (it is for found elements).
            // We can just remove at pos.
            block.remove(pos);
            
            // Insert val
            int insertPos = Collections.binarySearch(block, val);
            if (insertPos < 0) insertPos = -insertPos - 1;
            block.add(insertPos, val);
            
            // Add contribution of val
            currentInversions += countGreaterLeft(blocks, arr, idx, val, blockSize);
            currentInversions += countSmallerRight(blocks, arr, idx, val, blockSize);
            
            results.add(currentInversions);
        }
        return results;
    }
    
    private long countGreaterLeft(List<List<Integer>> blocks, int[] arr, int idx, int val, int blockSize) {
        long count = 0;
        int bIdx = idx / blockSize;
        
        // Full blocks to the left
        for (int i = 0; i < bIdx; i++) {
            List<Integer> b = blocks.get(i);
            // Count elements > val
            int pos = upperBound(b, val);
            count += (b.size() - pos);
        }
        
        // Elements in same block to the left
        int start = bIdx * blockSize;
        for (int i = start; i < idx; i++) {
            if (arr[i] > val) count++;
        }
        return count;
    }
    
    private long countSmallerRight(List<List<Integer>> blocks, int[] arr, int idx, int val, int blockSize) {
        long count = 0;
        int bIdx = idx / blockSize;
        int numBlocks = blocks.size();
        
        // Elements in same block to the right
        int end = Math.min((bIdx + 1) * blockSize, arr.length);
        for (int i = idx + 1; i < end; i++) {
            if (arr[i] < val) count++;
        }
        
        // Full blocks to the right
        for (int i = bIdx + 1; i < numBlocks; i++) {
            List<Integer> b = blocks.get(i);
            // Count elements < val
            int pos = lowerBound(b, val);
            count += pos;
        }
        return count;
    }
    
    private int lowerBound(List<Integer> list, int val) {
        int l = 0, r = list.size();
        while (l < r) {
            int mid = (l + r) / 2;
            if (list.get(mid) >= val) r = mid;
            else l = mid + 1;
        }
        return l;
    }
    
    private int upperBound(List<Integer> list, int val) {
        int l = 0, r = list.size();
        while (l < r) {
            int mid = (l + r) / 2;
            if (list.get(mid) > val) r = mid;
            else l = mid + 1;
        }
        return l;
    }
    
    // Standard Merge Sort Inversion Count
    private long countInversions(int[] arr) {
        return mergeSort(arr.clone(), 0, arr.length - 1);
    }
    
    private long mergeSort(int[] arr, int l, int r) {
        if (l >= r) return 0;
        int mid = (l + r) / 2;
        long count = mergeSort(arr, l, mid) + mergeSort(arr, mid + 1, r);
        
        int[] temp = new int[r - l + 1];
        int i = l, j = mid + 1, k = 0;
        while (i <= mid && j <= r) {
            if (arr[i] <= arr[j]) {
                temp[k++] = arr[i++];
            } else {
                temp[k++] = arr[j++];
                count += (mid - i + 1);
            }
        }
        while (i <= mid) temp[k++] = arr[i++];
        while (j <= r) temp[k++] = arr[j++];
        System.arraycopy(temp, 0, arr, l, temp.length);
        return count;
    }
}
```

### Python

```python
import bisect

def process(arr: list[int], updates: list[tuple[int, int]]) -> list[int]:
    n = len(arr)
    # Heuristic block size
    block_size = int((n * 0.5) ** 0.5) + 1
    if block_size < 50: block_size = 50
    
    blocks = []
    for i in range(0, n, block_size):
        chunk = arr[i : i + block_size]
        blocks.append(sorted(chunk))
        
    # Initial inversions
    def count_inversions(a):
        res = 0
        temp = [0] * len(a)
        def merge_sort(left, right):
            nonlocal res
            if left >= right: return
            mid = (left + right) // 2
            merge_sort(left, mid)
            merge_sort(mid + 1, right)
            
            i, j, k = left, mid + 1, left
            while i <= mid and j <= right:
                if a[i] <= a[j]:
                    temp[k] = a[i]
                    i += 1
                else:
                    temp[k] = a[j]
                    j += 1
                    res += (mid - i + 1)
                k += 1
            while i <= mid:
                temp[k] = a[i]
                i += 1
                k += 1
            while j <= right:
                temp[k] = a[j]
                j += 1
                k += 1
            for x in range(left, right + 1):
                a[x] = temp[x]
                
        merge_sort(0, len(a) - 1)
        return res

    current_inversions = count_inversions(list(arr))
    results = []
    
    for idx, val in updates:
        old_val = arr[idx]
        if val == old_val:
            results.append(current_inversions)
            continue
            
        b_idx = idx // block_size
        
        # Remove old_val contribution
        # Left blocks
        for i in range(b_idx):
            b = blocks[i]
            # Count > old_val
            pos = bisect.bisect_right(b, old_val)
            current_inversions -= (len(b) - pos)
            
        # Left in same block
        start = b_idx * block_size
        for i in range(start, idx):
            if arr[i] > old_val:
                current_inversions -= 1
                
        # Right in same block
        end = min((b_idx + 1) * block_size, n)
        for i in range(idx + 1, end):
            if arr[i] < old_val:
                current_inversions -= 1
                
        # Right blocks
        for i in range(b_idx + 1, len(blocks)):
            b = blocks[i]
            # Count < old_val
            pos = bisect.bisect_left(b, old_val)
            current_inversions -= pos
            
        # Update
        arr[idx] = val
        block = blocks[b_idx]
        # Remove one instance of old_val
        # bisect doesn't remove, list.remove is O(B)
        block.remove(old_val)
        bisect.insort(block, val)
        
        # Add val contribution
        # Left blocks
        for i in range(b_idx):
            b = blocks[i]
            pos = bisect.bisect_right(b, val)
            current_inversions += (len(b) - pos)
            
        # Left in same block
        for i in range(start, idx):
            if arr[i] > val:
                current_inversions += 1
                
        # Right in same block
        for i in range(idx + 1, end):
            if arr[i] < val:
                current_inversions += 1
                
        # Right blocks
        for i in range(b_idx + 1, len(blocks)):
            b = blocks[i]
            pos = bisect.bisect_left(b, val)
            current_inversions += pos
            
        results.append(current_inversions)
        
    return results
```

### C++

```cpp
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

class Solution {
    long long mergeSort(vector<int>& arr, int l, int r) {
        if (l >= r) return 0;
        int mid = (l + r) / 2;
        long long count = mergeSort(arr, l, mid) + mergeSort(arr, mid + 1, r);
        
        vector<int> temp;
        temp.reserve(r - l + 1);
        int i = l, j = mid + 1;
        while (i <= mid && j <= r) {
            if (arr[i] <= arr[j]) {
                temp.push_back(arr[i++]);
            } else {
                temp.push_back(arr[j++]);
                count += (mid - i + 1);
            }
        }
        while (i <= mid) temp.push_back(arr[i++]);
        while (j <= r) temp.push_back(arr[j++]);
        for (int k = 0; k < temp.size(); k++) arr[l + k] = temp[k];
        return count;
    }

public:
    vector<long long> process(const vector<int>& inputArr, const vector<pair<int,int>>& updates) {
        vector<int> arr = inputArr;
        int n = arr.size();
        int blockSize = sqrt(n * log2(n + 1)) + 1;
        if (blockSize < 50) blockSize = 50;
        
        int numBlocks = (n + blockSize - 1) / blockSize;
        vector<vector<int>> blocks(numBlocks);
        
        for (int i = 0; i < n; i++) {
            blocks[i / blockSize].push_back(arr[i]);
        }
        for (auto& b : blocks) sort(b.begin(), b.end());
        
        vector<int> tempArr = arr;
        long long currentInversions = mergeSort(tempArr, 0, n - 1);
        
        vector<long long> results;
        results.reserve(updates.size());
        
        for (const auto& up : updates) {
            int idx = up.first;
            int val = up.second;
            int oldVal = arr[idx];
            
            if (val == oldVal) {
                results.push_back(currentInversions);
                continue;
            }
            
            int bIdx = idx / blockSize;
            
            // Remove oldVal
            // Left blocks
            for (int i = 0; i < bIdx; i++) {
                auto& b = blocks[i];
                auto it = upper_bound(b.begin(), b.end(), oldVal);
                currentInversions -= distance(it, b.end());
            }
            // Same block left
            int start = bIdx * blockSize;
            for (int i = start; i < idx; i++) {
                if (arr[i] > oldVal) currentInversions--;
            }
            // Same block right
            int end = min((bIdx + 1) * blockSize, n);
            for (int i = idx + 1; i < end; i++) {
                if (arr[i] < oldVal) currentInversions--;
            }
            // Right blocks
            for (int i = bIdx + 1; i < numBlocks; i++) {
                auto& b = blocks[i];
                auto it = lower_bound(b.begin(), b.end(), oldVal);
                currentInversions -= distance(b.begin(), it);
            }
            
            // Update
            arr[idx] = val;
            auto& block = blocks[bIdx];
            auto it = lower_bound(block.begin(), block.end(), oldVal);
            block.erase(it);
            auto it2 = upper_bound(block.begin(), block.end(), val);
            block.insert(it2, val);
            
            // Add val
            // Left blocks
            for (int i = 0; i < bIdx; i++) {
                auto& b = blocks[i];
                auto it = upper_bound(b.begin(), b.end(), val);
                currentInversions += distance(it, b.end());
            }
            // Same block left
            for (int i = start; i < idx; i++) {
                if (arr[i] > val) currentInversions++;
            }
            // Same block right
            for (int i = idx + 1; i < end; i++) {
                if (arr[i] < val) currentInversions++;
            }
            // Right blocks
            for (int i = bIdx + 1; i < numBlocks; i++) {
                auto& b = blocks[i];
                auto it = lower_bound(b.begin(), b.end(), val);
                currentInversions += distance(b.begin(), it);
            }
            
            results.push_back(currentInversions);
        }
        return results;
    }
};
```

### JavaScript

```javascript
class Solution {
  process(arr, updates) {
    const n = arr.length;
    const blockSize = Math.floor(Math.sqrt(n * Math.log2(n + 1))) + 1;
    const safeBlockSize = blockSize < 50 ? 50 : blockSize;
    
    const blocks = [];
    for (let i = 0; i < n; i += safeBlockSize) {
      const chunk = arr.slice(i, i + safeBlockSize);
      chunk.sort((a, b) => a - b);
      blocks.push(chunk);
    }
    
    // Initial inversions
    const countInversions = (a) => {
      let count = 0n;
      const mergeSort = (arr) => {
        if (arr.length <= 1) return arr;
        const mid = Math.floor(arr.length / 2);
        const left = mergeSort(arr.slice(0, mid));
        const right = mergeSort(arr.slice(mid));
        
        let i = 0, j = 0;
        const res = [];
        while (i < left.length && j < right.length) {
          if (left[i] <= right[j]) {
            res.push(left[i++]);
          } else {
            res.push(right[j++]);
            count += BigInt(left.length - i);
          }
        }
        return res.concat(left.slice(i)).concat(right.slice(j));
      };
      mergeSort(a);
      return count;
    };
    
    let currentInversions = countInversions([...arr]);
    const results = [];
    
    // Helper for binary search
    const upperBound = (list, val) => {
      let l = 0, r = list.length;
      while (l < r) {
        const mid = (l + r) >>> 1;
        if (list[mid] > val) r = mid;
        else l = mid + 1;
      }
      return l;
    };
    
    const lowerBound = (list, val) => {
      let l = 0, r = list.length;
      while (l < r) {
        const mid = (l + r) >>> 1;
        if (list[mid] >= val) r = mid;
        else l = mid + 1;
      }
      return l;
    };

    for (const [idx, val] of updates) {
      const oldVal = arr[idx];
      if (val === oldVal) {
        results.push(currentInversions.toString());
        continue;
      }
      
      const bIdx = Math.floor(idx / safeBlockSize);
      
      // Remove oldVal
      for (let i = 0; i < bIdx; i++) {
        const b = blocks[i];
        const pos = upperBound(b, oldVal);
        currentInversions -= BigInt(b.length - pos);
      }
      
      const start = bIdx * safeBlockSize;
      for (let i = start; i < idx; i++) {
        if (arr[i] > oldVal) currentInversions--;
      }
      
      const end = Math.min((bIdx + 1) * safeBlockSize, n);
      for (let i = idx + 1; i < end; i++) {
        if (arr[i] < oldVal) currentInversions--;
      }
      
      for (let i = bIdx + 1; i < blocks.length; i++) {
        const b = blocks[i];
        const pos = lowerBound(b, oldVal);
        currentInversions -= BigInt(pos);
      }
      
      // Update
      arr[idx] = val;
      const block = blocks[bIdx];
      const removePos = lowerBound(block, oldVal);
      block.splice(removePos, 1);
      const insertPos = upperBound(block, val); // Insert to maintain stability/order
      // Actually lowerBound or upperBound works for insert position to keep sorted
      // Let's use lowerBound to keep identicals together
      const insertPos2 = lowerBound(block, val);
      block.splice(insertPos2, 0, val);
      
      // Add val
      for (let i = 0; i < bIdx; i++) {
        const b = blocks[i];
        const pos = upperBound(b, val);
        currentInversions += BigInt(b.length - pos);
      }
      
      for (let i = start; i < idx; i++) {
        if (arr[i] > val) currentInversions++;
      }
      
      for (let i = idx + 1; i < end; i++) {
        if (arr[i] < val) currentInversions++;
      }
      
      for (let i = bIdx + 1; i < blocks.length; i++) {
        const b = blocks[i];
        const pos = lowerBound(b, val);
        currentInversions += BigInt(pos);
      }
      
      results.push(currentInversions.toString());
    }
    return results;
  }
}
```

## Test Case Walkthrough

**Input:**
`3 1`
`3 1 2`
`SET 1 4`

1.  **Initial**: `[3, 1, 2]`. Inversions: `(3,1), (3,2)`. Count = 2.
2.  **Update**: `a[1]` changes `1 -> 4`.
    -   Remove `1` at index 1.
        -   Left `[3]`: `3 > 1`. Inversions -1.
        -   Right `[2]`: `2 < 1` (False).
        -   Count becomes 1.
    -   Insert `4` at index 1.
        -   Left `[3]`: `3 > 4` (False).
        -   Right `[2]`: `2 < 4` (True). Inversions +1.
        -   Count becomes 2.
3.  **Result**: 2.
    -   Array `[3, 4, 2]`. Inversions `(3,2), (4,2)`. Correct.

## Proof of Correctness

-   **Decomposition**: By splitting into blocks, we balance the cost of updating (small block size) and querying (few blocks).
-   **Counting**: We correctly identify all pairs `(j, i)` and `(i, k)` that form inversions with the updated index `i`.
-   **Sorted Blocks**: Allows `O(log B)` counting for full blocks.

## Interview Extensions

1.  **Range Updates?**
    -   Much harder. Requires Segment Tree Beats or advanced techniques.
2.  **Small Values (`A[i] <= N`)?**

### Common Mistakes

-   **Block Size**: Too small = slow query. Too large = slow update. `sqrtN log N` is a good balance.
-   **Binary Search**: `upper_bound` vs `lower_bound`.
    -   Count `> x`: `size - upper_bound`.
    -   Count `< x`: `lower_bound`.
