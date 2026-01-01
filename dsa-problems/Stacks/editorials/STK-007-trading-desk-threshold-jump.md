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


## Constraints

- `1 <= n <= 200000`
- `0 <= p[i], t <= 10^9`
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

### 2. Segment Tree Approach
-   This problem requires finding the nearest future index with a value threshold.
-   We use **Coordinate Compression** with a **Segment Tree** to efficiently query minimum indices.
-   The approach:
    1. Map all values to ranks using coordinate compression.
    2. Build a Segment Tree that stores minimum indices for value ranges.
    3. Process prices from right to left.
    4. For each position, query for the nearest future price meeting the threshold.
-   **Complexity**: `O(N log N)` for both coordinate compression and segment tree operations.

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
import java.io.*;

class Solution {
    int[] tree;
    int m;

    void update(int node, int start, int end, int idx, int val) {
        if (start == end) {
            tree[node] = val;
            return;
        }
        int mid = (start + end) / 2;
        if (idx <= mid) {
            update(2 * node, start, mid, idx, val);
        } else {
            update(2 * node + 1, mid + 1, end, idx, val);
        }
        tree[node] = Math.min(tree[2 * node], tree[2 * node + 1]);
    }

    int query(int node, int start, int end, int l, int r) {
        if (r < start || end < l) {
            return Integer.MAX_VALUE;
        }
        if (l <= start && end <= r) {
            return tree[node];
        }
        int mid = (start + end) / 2;
        return Math.min(query(2 * node, start, mid, l, r),
                        query(2 * node + 1, mid + 1, end, l, r));
    }

    public int[] thresholdJump(int[] prices, int t) {
        int n = prices.length;
        
        // Coordinate Compression
        Set<Integer> distinctSet = new TreeSet<>();
        for (int p : prices) distinctSet.add(p);
        List<Integer> distinct = new ArrayList<>(distinctSet);
        m = distinct.size();
        
        Map<Integer, Integer> rankMap = new HashMap<>();
        for (int i = 0; i < m; i++) rankMap.put(distinct.get(i), i);
        
        // Segment Tree (Min Index)
        tree = new int[4 * m];
        Arrays.fill(tree, Integer.MAX_VALUE);
        
        int[] result = new int[n];
        
        for (int i = n - 1; i >= 0; i--) {
            int target = prices[i] + t;
            
            // Find rank >= target using binary search on distinct list
            int r = Collections.binarySearch(distinct, target);
            if (r < 0) r = -r - 1; // Insertion point
            
            if (r < m) {
                int nearestIdx = query(1, 0, m - 1, r, m - 1);
                if (nearestIdx != Integer.MAX_VALUE) {
                    result[i] = nearestIdx - i;
                }
            }
            
            update(1, 0, m - 1, rankMap.get(prices[i]), i);
        }
        return result;
    }
}

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        // Read N
        String line = "";
        while ((line = br.readLine()) != null && line.trim().isEmpty()) {}
        if (line == null) return;
        int n = Integer.parseInt(line.trim());
        
        // Read Array
        List<Integer> list = new ArrayList<>();
        StringTokenizer st = new StringTokenizer("");
        
        while (list.size() < n) {
            while (!st.hasMoreTokens()) {
                String l = br.readLine();
                if (l == null) break;
                st = new StringTokenizer(l);
            }
            if (!st.hasMoreTokens()) break;
            list.add(Integer.parseInt(st.nextToken()));
        }
        
        int[] prices = new int[list.size()];
        for(int i=0; i<list.size(); i++) prices[i] = list.get(i);
        
        // Read T
        while (!st.hasMoreTokens()) {
            String l = br.readLine();
            if (l == null) break;
            st = new StringTokenizer(l);
        }
        int t = 0;
        if (st.hasMoreTokens()) {
            t = Integer.parseInt(st.nextToken());
        }
        
        Solution sol = new Solution();
        int[] res = sol.thresholdJump(prices, t);
        for (int val : res) {
            System.out.println(val);
        }
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


def main():
    import sys
    lines = sys.stdin.read().strip().split('\n')
    if not lines:
        return

    n = int(lines[0])
    prices = list(map(int, lines[1].split()))
    t = int(lines[2])
    result = threshold_jump(prices, t)
    for r in result:
        print(r)

if __name__ == "__main__":
    main()
```

### C++
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <climits>

using namespace std;

class Solution {
    vector<int> tree;
    int m;

    void update(int node, int start, int end, int idx, int val) {
        if (start == end) {
            tree[node] = val;
            return;
        }
        int mid = (start + end) / 2;
        if (idx <= mid) {
            update(2 * node, start, mid, idx, val);
        } else {
            update(2 * node + 1, mid + 1, end, idx, val);
        }
        tree[node] = min(tree[2 * node], tree[2 * node + 1]);
    }

    int query(int node, int start, int end, int l, int r) {
        if (r < start || end < l) {
            return INT_MAX;
        }
        if (l <= start && end <= r) {
            return tree[node];
        }
        int mid = (start + end) / 2;
        return min(query(2 * node, start, mid, l, r),
                   query(2 * node + 1, mid + 1, end, l, r));
    }

public:
    vector<int> thresholdJump(vector<int>& prices, int t) {
        int n = prices.size();
        
        // Coordinate Compression
        vector<int> distinct = prices;
        sort(distinct.begin(), distinct.end());
        distinct.erase(unique(distinct.begin(), distinct.end()), distinct.end());
        
        m = distinct.size();
        map<int, int> rankMap;
        for (int i = 0; i < m; i++) rankMap[distinct[i]] = i;
        
        tree.assign(4 * m, INT_MAX);
        vector<int> result(n, 0);
        
        for (int i = n - 1; i >= 0; i--) {
            long long target = (long long)prices[i] + t;
            
            // Find rank >= target
            auto it = lower_bound(distinct.begin(), distinct.end(), target);
            int r = distance(distinct.begin(), it);
            
            if (r < m) {
                int nearestIdx = query(1, 0, m - 1, r, m - 1);
                if (nearestIdx != INT_MAX) {
                    result[i] = nearestIdx - i;
                }
            }
            
            update(1, 0, m - 1, rankMap[prices[i]], i);
        }
        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    if (!(cin >> n)) return 0;
    
    vector<int> prices(n);
    for (int i = 0; i < n; i++) {
        cin >> prices[i];
    }
    
    int t;
    cin >> t;
    
    Solution sol;
    vector<int> res = sol.thresholdJump(prices, t);
    
    for (int val : res) {
        cout << val << "\n";
    }
    
    return 0;
}
```

### JavaScript
```javascript
class Solution {
  update(node, start, end, idx, val) {
    if (start === end) {
      this.tree[node] = val;
      return;
    }
    const mid = Math.floor((start + end) / 2);
    if (idx <= mid) {
      this.update(2 * node, start, mid, idx, val);
    } else {
      this.update(2 * node + 1, mid + 1, end, idx, val);
    }
    this.tree[node] = Math.min(this.tree[2 * node], this.tree[2 * node + 1]);
  }

  query(node, start, end, l, r) {
    if (r < start || end < l) {
      return Infinity;
    }
    if (l <= start && end <= r) {
      return this.tree[node];
    }
    const mid = Math.floor((start + end) / 2);
    return Math.min(this.query(2 * node, start, mid, l, r),
                    this.query(2 * node + 1, mid + 1, end, l, r));
  }

  thresholdJump(prices, t) {
    const n = prices.length;
    
    // Coordinate Compression
    // Use Set for distinct, then sort
    const distinct = Array.from(new Set(prices)).sort((a, b) => a - b);
    const m = distinct.length;
    const rankMap = new Map();
    distinct.forEach((val, i) => rankMap.set(val, i));
    
    // Segment Tree
    // Size 4*m
    this.tree = new Array(4 * m).fill(Infinity);
    
    const result = new Array(n).fill(0);
    
    for (let i = n - 1; i >= 0; i--) {
      const target = prices[i] + t;
      
      // bisect_left logic
      let l = 0, r = m;
      while (l < r) {
        const mid = Math.floor((l + r) / 2);
        if (distinct[mid] < target) {
          l = mid + 1;
        } else {
          r = mid;
        }
      }
      const rank = l;
      
      if (rank < m) {
        const nearestIdx = this.query(1, 0, m - 1, rank, m - 1);
        if (nearestIdx !== Infinity) {
          result[i] = nearestIdx - i;
        }
      }
      
      this.update(1, 0, m - 1, rankMap.get(prices[i]), i);
    }
    return result;
  }
}

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => {
  const parts = line.trim().split(/\s+/).filter(x => x !== "");
  for (const p of parts) data.push(p);
});

rl.on("close", () => {
  if (data.length === 0) return;
  
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const prices = [];
  for (let i = 0; i < n; i++) {
    prices.push(parseInt(data[idx++], 10));
  }
  const t = parseInt(data[idx++], 10);
  
  const solution = new Solution();
  const res = solution.thresholdJump(prices, t);
  console.log(res.join("\n"));
});
```

## 🧪 Test Case Walkthrough (Dry Run)
**Input:** `3 1 4 6 5`, `t=2`

1.  **Distinct**: `[1, 3, 4, 5, 6]`. Ranks: `1->0, 3->1, 4->2, 5->3, 6->4`.
2.  Process right to left:
    -   `i=4` (5): Target `5+2=7`. No element >= 7. Res `0`.
    -   `i=3` (6): Target `6+2=8`. No element >= 8. Res `0`.
    -   `i=2` (4): Target `4+2=6`. Element `6` at index 3. Res `3 - 2 = 1`.
    -   `i=1` (1): Target `1+2=3`. Element `3` at index 0, `4` at index 2. Nearest is index 2. Res `2 - 1 = 1`.
    -   `i=0` (3): Target `3+2=5`. Element `5` at index 4, `6` at index 3. Nearest is index 3. Res `3 - 0 = 3`.

**Output:** `3 1 1 0 0`

## Proof of Correctness

-   **Range Query**: By mapping values to ranks, we transform the condition `val >= target` into `rank >= target_rank`.
-   **Min Index**: The Segment Tree efficiently finds the minimum index in the suffix of ranks, which corresponds to the nearest future element satisfying the value condition.
-   **Right-to-Left**: Processing in reverse ensures that when we query for `p[i]`, the tree only contains indices `j > i`.

## Interview Extensions

1.  **Max Wait Time**: Find the maximum wait time instead of per-element.
2.  **Dynamic Updates**: What if prices change? (SegTree handles updates in `O(log N)`).

### Common Mistakes

-   **Coordinate Compression**: Forgetting to compress values when they can be up to `10^9`.
-   **SegTree Range**: Querying `[0, size-1]` instead of `[target_rank, size-1]`.
-   **Infinity**: Initializing min-tree with 0 instead of infinity.
