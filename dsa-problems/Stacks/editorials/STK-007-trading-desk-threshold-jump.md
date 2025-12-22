---
title: Trading Desk Threshold Jump
slug: trading-desk-threshold-jump
difficulty: Medium
difficulty_score: 48
tags:
- Stack
- Monotonic Stack
- Next Greater Element
problem_id: STK_TRADING_DESK_THRESHOLD_JUMP__2549
display_id: STK-007
topics:
- Stack
- Monotonic Stack
- Arrays
---
# Trading Desk Threshold Jump - Editorial

## Problem Summary

For each price `p[i]` in an array, find the number of steps forward (distance) to the nearest future price `p[j]` (where `j > i`) such that `p[j] >= p[i] + t`. If no such price exists, output `0`.

## Real-World Scenario

Imagine you are an **Algorithmic Trader**.
-   You buy a stock at price `P`.
-   You have a strict rule: you only sell if the price rises by at least `T` dollars (i.e., reaches `P + T`).
-   You want to know, for every possible buying moment in history, how long you would have had to wait to trigger a sell.
-   If the price never rose by `T` after that point, you would have been stuck holding the bag forever (wait time 0 or infinity).

## Problem Exploration

### 1. Next Greater Element Variation
-   This is very similar to the "Next Greater Element" problem.
-   Standard NGE: Find nearest `j > i` such that `p[j] > p[i]`.
-   Our Problem: Find nearest `j > i` such that `p[j] >= p[i] + t`.
-   The condition `p[j] >= p[i] + t` depends on both `p[i]` and `p[j]`.

### 2. Monotonic Stack?
-   In standard NGE, we maintain a decreasing stack. When a large element comes, it resolves smaller elements on the stack.
-   Here, if we have a decreasing stack `[10, 8, 5]` and `t=2`.
-   New element `12`.
    -   `12 >= 5 + 2` (7). Yes. `5` is resolved by `12`.
    -   `12 >= 8 + 2` (10). Yes. `8` is resolved by `12`.
    -   `12 >= 10 + 2` (12). Yes. `10` is resolved by `12`.
-   This looks promising.
-   What if the stack is NOT decreasing?
    -   Suppose `[5, 8]` (indices `0, 1`) and `t=2`.
    -   New element `9` (index 2).
    -   `9 >= 8 + 2` (10)? No. `8` waits.
    -   `9 >= 5 + 2` (7)? Yes. `5` is resolved by `9`.
    -   We need to access `5` below `8`.
    -   This breaks the standard stack property where we only interact with the top.

### 3. Sorting + Monotonic Stack?
-   The condition is `p[j] >= p[i] + t`.
-   This looks like a 2D range query or a specific ordering problem.
-   However, we want the *nearest* `j`.
-   Let's reconsider the stack.
-   If we process elements from **Right to Left**:
    -   For `p[i]`, we want the nearest `j > i` with `p[j] >= p[i] + t`.
    -   We have seen all `p[j]` for `j > i`.
    -   We want to query this set of future values.
    -   Specifically, we want the smallest index `j` among those with value `>= Target`.
    -   This is a Range Minimum Query on indices, or a search on values.
    -   If we maintain a data structure of "seen future values and their indices", we can query it.
    -   Since we want the *nearest* (smallest index), and we process R-to-L (indices decreasing), the most recently seen elements are the best candidates.
    -   But we process R-to-L, so the one we see *last* (closest to `i`) is the best.
    -   So for each value `V`, we only care about its most recent index.
    -   We need to find `min(index)` for all `V >= p[i] + t`.
    -   This is a range query: "Min index in value range `[p[i]+t, infinity]`".
    -   We can use a **Segment Tree** or **Fenwick Tree** over the *values*.
    -   Coordinate compression might be needed if values are large (up to `10^9`).
    -   With coordinate compression, values map to `1..N`.
    -   We build a Segment Tree over `[1, N]`. Each node stores the minimum index seen so far for that value range.
    -   Iterate `i` from `n-1` to `0`:
        -   Query SegTree for range `[rank(p[i]+t), max_rank]`. Result is `nearest_j`.
        -   Update SegTree at `rank(p[i])` with `i`.
    -   Complexity: `O(N log N)`.

### 4. Can we do O(N)?
-   The problem constraints `N=200,000` usually allow `O(N log N)`.
-   Is there a monotonic stack approach?
-   Let's go back to Left-to-Right processing.
-   Stack contains indices `i` waiting for a jump.
-   When `p[j]` comes, it can satisfy any `i` where `p[i] <= p[j] - t`.
-   This doesn't imply monotonicity on `p[i]`.
-   However, if we have `i1` and `i2` in stack with `p[i1] >= p[i2]`.
    -   If `p[j]` satisfies `i1` (`p[j] >= p[i1] + t`), does it satisfy `i2`?
    -   `p[j] >= p[i1] + t >= p[i2] + t`. Yes.
    -   So if a larger waiting element is satisfied, smaller ones are too.
    -   But `i1` might be satisfied later than `i2`.
    -   We can maintain the waiting list sorted by value?
    -   If we sort waiting indices by `p[i]`, we can binary search or iterate.
    -   But we need to remove them efficiently.
    -   Since we want to resolve them as soon as possible, we check every time? Too slow `O(N^2)`.
    -   The Segment Tree approach is the most robust standard solution here.

### 5. Segment Tree Details
-   **Coordinate Compression**: Collect all `p[i]` and `p[i] + t`. Sort and remove duplicates. Map values to ranks `1..M`.
-   **SegTree**: Size `M`. Supports `update(pos, val)` and `query(l, r)`.
-   **Operation**: `min` query. Initialize with infinity.
-   **Loop**: `i` from `n-1` down to `0`.
    -   Target value `V = p[i] + t`.
    -   Find rank `r` of `V` (using `lower_bound`).
    -   Query min index in range `[r, M]`.
    -   If result is infinity, ans is 0. Else `result - i`.
    -   Update position `rank(p[i])` with `i`.
-   This works perfectly.

## Approaches

### Approach 1: Coordinate Compression + Segment Tree
-   Map values to ranks.
-   Use a Segment Tree to store the minimum index for each value range.
-   Process Right-to-Left.
-   Complexity: `O(N log N)`.

## Implementations

### Java

```java
import java.util.*;

class Solution {
    int[] tree;
    int size;

    void update(int node, int start, int end, int idx, int val) {
        if (start == end) {
            tree[node] = val; // We process R-to-L, so new val (index i) is always smaller/better
            return;
        }
        int mid = (start + end) / 2;
        if (idx <= mid) update(2 * node, start, mid, idx, val);
        else update(2 * node + 1, mid + 1, end, idx, val);
        tree[node] = Math.min(tree[2 * node], tree[2 * node + 1]);
    }

    int query(int node, int start, int end, int l, int r) {
        if (r < start || end < l) return Integer.MAX_VALUE;
        if (l <= start && end <= r) return tree[node];
        int mid = (start + end) / 2;
        return Math.min(query(2 * node, start, mid, l, r), query(2 * node + 1, mid + 1, end, l, r));
    }

    public int[] thresholdJump(int[] prices, int t) {
        int n = prices.length;
        TreeSet<Integer> sortedValues = new TreeSet<>();
        for (int p : prices) {
            sortedValues.add(p);
            // We don't strictly need p+t in compression if we use lower_bound logic on just p values
            // But adding p+t makes it easier to map exactly.
        }
        
        // Map values to ranks 0..m-1
        List<Integer> distinct = new ArrayList<>(sortedValues);
        Map<Integer, Integer> rankMap = new HashMap<>();
        for (int i = 0; i < distinct.size(); i++) {
            rankMap.put(distinct.get(i), i);
        }
        
        size = distinct.size();
        tree = new int[4 * size];
        Arrays.fill(tree, Integer.MAX_VALUE);
        
        int[] result = new int[n];
        
        for (int i = n - 1; i >= 0; i--) {
            int target = prices[i] + t;
            // Find rank of smallest value >= target
            int r = Collections.binarySearch(distinct, target);
            if (r < 0) r = -r - 1; // Insertion point
            
            if (r < size) {
                int nearestIdx = query(1, 0, size - 1, r, size - 1);
                if (nearestIdx != Integer.MAX_VALUE) {
                    result[i] = nearestIdx - i;
                } else {
                    result[i] = 0;
                }
            } else {
                result[i] = 0;
            }
            
            update(1, 0, size - 1, rankMap.get(prices[i]), i);
        }
        
        return result;
    }
}
```

### Python

```python
def threshold_jump(prices: list[int], t: int) -> list[int]:
    n = len(prices)
    # Coordinate Compression
    distinct = sorted(list(set(prices)))
    rank_map = {val: i for i, val in enumerate(distinct)}
    m = len(distinct)
    
    # Segment Tree (Min)
    tree = [float('inf')] * (4 * m)
    
    def update(node, start, end, idx, val):
        if start == end:
            tree[node] = val
            return
        mid = (start + end) // 2
        if idx <= mid:
            update(2 * node, start, mid, idx, val)
        else:
            update(2 * node + 1, mid + 1, end, idx, val)
        tree[node] = min(tree[2 * node], tree[2 * node + 1])
        
    def query(node, start, end, l, r):
        if r < start or end < l:
            return float('inf')
        if l <= start and end <= r:
            return tree[node]
        mid = (start + end) // 2
        return min(query(2 * node, start, mid, l, r),
                   query(2 * node + 1, mid + 1, end, l, r))
                   
    import bisect
    result = [0] * n
    
    for i in range(n - 1, -1, -1):
        target = prices[i] + t
        # Find rank >= target
        r = bisect.bisect_left(distinct, target)
        
        if r < m:
            nearest_idx = query(1, 0, m - 1, r, m - 1)
            if nearest_idx != float('inf'):
                result[i] = nearest_idx - i
        
        update(1, 0, m - 1, rank_map[prices[i]], i)
        
    return result
```

### C++

```cpp
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

class Solution {
    vector<int> tree;
    int size;

    void update(int node, int start, int end, int idx, int val) {
        if (start == end) {
            tree[node] = val;
            return;
        }
        int mid = (start + end) / 2;
        if (idx <= mid) update(2 * node, start, mid, idx, val);
        else update(2 * node + 1, mid + 1, end, idx, val);
        tree[node] = min(tree[2 * node], tree[2 * node + 1]);
    }

    int query(int node, int start, int end, int l, int r) {
        if (r < start || end < l) return 2e9;
        if (l <= start && end <= r) return tree[node];
        int mid = (start + end) / 2;
        return min(query(2 * node, start, mid, l, r), query(2 * node + 1, mid + 1, end, l, r));
    }

public:
    vector<int> thresholdJump(const vector<int>& prices, int t) {
        int n = prices.size();
        vector<int> distinct = prices;
        sort(distinct.begin(), distinct.end());
        distinct.erase(unique(distinct.begin(), distinct.end()), distinct.end());
        
        size = distinct.size();
        tree.assign(4 * size, 2e9);
        
        vector<int> result(n, 0);
        
        for (int i = n - 1; i >= 0; i--) {
            long long target = (long long)prices[i] + t;
            auto it = lower_bound(distinct.begin(), distinct.end(), target);
            
            if (it != distinct.end()) {
                int r = distance(distinct.begin(), it);
                int nearestIdx = query(1, 0, size - 1, r, size - 1);
                if (nearestIdx != 2e9) {
                    result[i] = nearestIdx - i;
                }
            }
            
            int rank = lower_bound(distinct.begin(), distinct.end(), prices[i]) - distinct.begin();
            update(1, 0, size - 1, rank, i);
        }
        
        return result;
    }
};
```

### JavaScript

```javascript
class Solution {
  thresholdJump(prices, t) {
    const n = prices.length;
    
    // Coordinate Compression
    const distinct = Array.from(new Set(prices)).sort((a, b) => a - b);
    const rankMap = new Map();
    distinct.forEach((val, idx) => rankMap.set(val, idx));
    const m = distinct.length;
    
    // Segment Tree
    const tree = new Int32Array(4 * m).fill(2e9);
    
    const update = (node, start, end, idx, val) => {
      if (start === end) {
        tree[node] = val;
        return;
      }
      const mid = Math.floor((start + end) / 2);
      if (idx <= mid) update(2 * node, start, mid, idx, val);
      else update(2 * node + 1, mid + 1, end, idx, val);
      tree[node] = Math.min(tree[2 * node], tree[2 * node + 1]);
    };
    
    const query = (node, start, end, l, r) => {
      if (r < start || end < l) return 2e9;
      if (l <= start && end <= r) return tree[node];
      const mid = Math.floor((start + end) / 2);
      return Math.min(query(2 * node, start, mid, l, r),
                      query(2 * node + 1, mid + 1, end, l, r));
    };
    
    const result = new Int32Array(n).fill(0);
    
    // Binary Search helper
    const lowerBound = (arr, target) => {
      let l = 0, r = arr.length;
      while (l < r) {
        const mid = Math.floor((l + r) / 2);
        if (arr[mid] < target) l = mid + 1;
        else r = mid;
      }
      return l;
    };
    
    for (let i = n - 1; i >= 0; i--) {
      const target = prices[i] + t;
      const r = lowerBound(distinct, target);
      
      if (r < m) {
        const nearestIdx = query(1, 0, m - 1, r, m - 1);
        if (nearestIdx !== 2e9) {
          result[i] = nearestIdx - i;
        }
      }
      
      update(1, 0, m - 1, rankMap.get(prices[i]), i);
    }
    
    return Array.from(result);
  }
}
```

## Test Case Walkthrough

**Input:** `3 1 4 6 5`, `t=2`

1.  **Distinct**: `[1, 3, 4, 5, 6]`. Ranks: `1->0, 3->1, 4->2, 5->3, 6->4`.
2.  `i=4` (5): Target `5+2=7`. `lower_bound(7)` -> index 5 (out of bounds). Res `0`. Update rank 3 (val 5) with index 4.
3.  `i=3` (6): Target `6+2=8`. `lower_bound(8)` -> out. Res `0`. Update rank 4 (val 6) with index 3.
4.  `i=2` (4): Target `4+2=6`. `lower_bound(6)` -> index 4 (val 6).
    -   Query range `[4, 4]`. Tree has index 3 at rank 4. Min is 3.
    -   Res `3 - 2 = 1`.
    -   Update rank 2 (val 4) with index 2.
5.  `i=1` (1): Target `1+2=3`. `lower_bound(3)` -> index 1 (val 3).
    -   Query range `[1, 4]`.
    -   Tree has: rank 2->idx 2, rank 3->idx 4, rank 4->idx 3.
    -   Min index is 2 (from rank 2).
    -   Res `2 - 1 = 1`.
    -   Update rank 0 (val 1) with index 1.
6.  `i=0` (3): Target `3+2=5`. `lower_bound(5)` -> index 3 (val 5).
    -   Query range `[3, 4]`.
    -   Tree has: rank 3->idx 4, rank 4->idx 3.
    -   Min index is 3 (from rank 4).
    -   Res `3 - 0 = 3`.
    -   Let's re-check. `3` needs `>= 5`.
    -   Future elements: `1, 4, 6, 5`.
    -   `6` (idx 3) >= 5. Dist 3.
    -   `5` (idx 4) >= 5. Dist 4.
    -   Nearest is `6` at idx 3. Dist 3.
    -   Why example says 2?
    -   Example output: `2 1 1 0 0`.
    -   For `3` (idx 0), answer `2`. This means index `0+2=2`. `p[2]=4`.
    -   Is `4 >= 3 + 2`? `4 >= 5`? No.
    -   Is the condition `p[j] - p[i] >= t`? Yes. `4 - 3 = 1`. `1 >= 2`? No.
    -   Maybe the example output corresponds to `t=1`?
    -   If `t=1`: `3` needs `>= 4`. `4` is at idx 2. Dist 2. Correct.
    -   `1` needs `>= 2`. `4` at idx 2. Dist 1. Correct.
    -   `4` needs `>= 5`. `6` at idx 3. Dist 1. Correct.
    -   `6` needs `>= 7`. None. 0.
    -   `5` needs `>= 6`. None. 0.
    -   Yes, the example output matches `t=1`.
    -   But the input says `5 2`.
    -   Okay, the example in the problem description has a mismatch between `t` and the output.
    -   I will trust the logic `p[j] >= p[i] + t`.
    -   My trace with `t=2` gave `3 1 1 0 0`.
    -   `3` needs `>= 5`. `6` (idx 3) is nearest. Dist 3.
    -   `1` needs `>= 3`. `4` (idx 2) is nearest. Dist 1.
    -   `4` needs `>= 6`. `6` (idx 3) is nearest. Dist 1.
    -   `6` needs `>= 8`. None.
    -   `5` needs `>= 7`. None.
    -   My code produces `3 1 1 0 0`.
    -   I will mention this discrepancy or just explain the logic clearly.

## Proof of Correctness

-   **Range Query**: By mapping values to ranks, we transform the condition `val >= target` into `rank >= target_rank`.
-   **Min Index**: The Segment Tree efficiently finds the minimum index in the suffix of ranks, which corresponds to the nearest future element satisfying the value condition.
-   **Right-to-Left**: Processing in reverse ensures that when we query for `p[i]`, the tree only contains indices `j > i`.

## Interview Extensions

1.  **Max Wait Time**: Find the maximum wait time instead of per-element.
2.  **Dynamic Updates**: What if prices change? (SegTree handles updates in `O(log N)`).

### C++ommon Mistakes

-   **Coordinate Compression**: Forgetting to compress values when they can be up to `10^9`.
-   **SegTree Range**: Querying `[0, size-1]` instead of `[target_rank, size-1]`.
-   **Infinity**: Initializing min-tree with 0 instead of infinity.
