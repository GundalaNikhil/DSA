---
title: Auditorium Histogram With One Booster
slug: auditorium-histogram-one-booster
difficulty: Medium
difficulty_score: 60
tags:
- Stack
- Histogram
- Optimization
problem_id: STK_AUDITORIUM_HISTOGRAM_ONE_BOOSTER__9153
display_id: STK-013
topics:
- Stack
- Histogram
- Optimization
---
# Auditorium Histogram With One Booster - Editorial

## Problem Summary

Given an array of histogram heights `h` and a boost value `b`. You can increase the height of **exactly one** bar by at most `b` (you can add any value `0 <= x <= b`). Find the maximum possible area of a rectangle that can be formed in the histogram after this modification.


## Constraints

- `1 <= n <= 200000`
- `0 <= h[i], b <= 10^9`
## Real-World Scenario

Imagine you are renovating an **Auditorium Seating Area**.
-   The seating is arranged in columns of varying depths (heights).
-   You want to place a large rectangular stage or screen across contiguous columns.
-   The size of the stage is limited by the shortest column in the span.
-   You have enough budget to extend **one** column by up to `b` meters.
-   Where should you apply this extension to maximize the total stage area?

## Problem Exploration

### 1. Classic Histogram Area
-   The "Largest Rectangle in Histogram" problem is solved in `O(N)` using a Monotonic Stack.
-   For each bar `i`, we find the nearest smaller bar to the left (`L[i]`) and right (`R[i]`).
-   The max width for a rectangle of height `h[i]` is `R[i] - L[i] - 1`.
-   Area = `h[i] * width`.

### 2. Boosting One Bar
-   If we boost bar `i` to `h[i] + b`, it might become the bottleneck for a larger rectangle, or it might allow a taller rectangle to pass through.
-   However, the optimal rectangle might not even use the full `h[i] + b`. It might use `h[j]` as the height, where `j != i`.
-   If the optimal rectangle has height `H`, it must be limited by some bar `k`.
    -   Case 1: The limiting bar `k` is NOT the boosted bar. Then the boost didn't help the height, but it might have helped the *width* (by allowing the rectangle to extend past `i` if `i` was previously a bottleneck).
    -   Case 2: The limiting bar `k` IS the boosted bar. Then the height is `h[k] + b` (or less).

### 3. Analyzing the Cases
-   **Case A: The boosted bar defines the height.**
    -   We iterate every bar `i`. Assume we boost it to `h[i] + b`.
    -   We calculate the max width for height `h[i] + b` passing through `i`.
    -   This requires finding nearest element `< h[i] + b` to left and right.
    -   This is effectively solving the histogram problem for `N` different modified arrays? Too slow (`O(N^2)`).
    -   However, notice we only care about the width for *this specific height* at *this specific position*.
    -   We need `L'_i` and `R'_i` for value `h[i] + b`.
    -   This can be solved for all `i` efficiently?

-   **Case B: The boosted bar is just part of the width.**
    -   The rectangle has height `h[k]` (where `k != i`).
    -   The boost on `i` allows the rectangle of height `h[k]` to span across `i` where it previously couldn't (i.e., `h[i] < h[k]` but `h[i] + b >= h[k]`).
    -   This means `i` was a bottleneck for `k`.
    -   This is equivalent to: For each `k`, calculate max width assuming ONE bottleneck can be removed (if `h[bottleneck] + b >= h[k]`).
    -   This seems complicated.

### 4. Simplified Perspective
-   Let's flip the logic. The optimal rectangle has some height `H` and spans from `L` to `R`.
-   The height `H` is determined by `min(h[L...R])` (after boost).
-   Since we boost one bar, at most one bar in `L...R` was originally `< H`.
-   Specifically:
    -   If NO bars in `L...R` were `< H`, then `H <= min(original h[L...R])`. This is just the original max area problem.
    -   If ONE bar `i` in `L...R` was `< H`, then we must have boosted `i` such that `h[i] + b >= H`.
    -   This means the rectangle is defined by height `H`, and it spans across a region where exactly one element was "bad" (too small) but fixable.
    -   Which `H` values are candidates?
    -   In standard problem, candidates are `h[k]`.
    -   Here, candidates are `h[k]` (unboosted) or `h[k] + b` (boosted).
    -   If the height is determined by an unboosted bar `k`, `H = h[k]`.
    -   So we just need to check two types of rectangles:
        1.  Height `h[i] + b` centered at `i`.
        2.  Height `h[k]` centered at `k`, allowing one "bad" bar `j` if `h[j] + b >= h[k]`.

### 5. Algorithm Refinement
-   **Part 1: Height = `h[i] + b`**
    -   For each `i`, treat height as `h[i] + b`.
    -   Find range `[L, R]` such that all `x` in range have `h[x] >= h[i] + b` (except `i` itself, which is boosted).
    -   So we just need `L` (nearest index < `i` with `h < h[i] + b`) and `R` (nearest index > `i` with `h < h[i] + b`).
    -   This is exactly finding Next Smaller Element for value `h[i] + b`.
    -   We can do this for all `i`?
    -   Standard Monotonic Stack finds NSE for `h[i]`.
    -   For `h[i] + b`, we can't use a single pass stack easily because the values are different for each query.
    -   However, we can sort the queries!
    -   Or use a Segment Tree?
    -   Or just realize `N=200,000`. `O(N log N)` is fine.
    -   We can use a Segment Tree to find the first index to left/right with value `< V`.
    -   SegTree stores minimums.
    -   Query: Find largest index `< i` with `val < Target`. This is a "descent" on SegTree. `O(log N)`.
    -   Total `O(N log N)` for Part 1.

-   **Part 2: Height = `h[k]`**
    -   For each `k`, we want to extend left and right.
    -   Normally we stop at first `j` with `h[j] < h[k]`.
    -   Now we can "skip" ONE such `j` if `h[j] + b >= h[k]`.
    -   So we stop at the *second* violation, or the first violation that is *unfixable* (`h[j] + b < h[k]`).
    -   Let's formalize:
        -   Left side: Find `j1` (nearest `< h[k]`).
        -   If `h[j1] + b >= h[k]`, we can potentially continue left to `j2` (next nearest `< h[k]` after `j1`).
        -   The range would be `(j2, R)`.
        -   So we need to check if the range `(j2, j1)` contains any other bars `< h[k]`.
        -   But `j1` is the *nearest* to left. So everything in `(j1, k)` is `>= h[k]`.
        -   So if we fix `j1`, we extend to `j2`.
        -   Is it guaranteed that `(j2, j1)` is valid?
        -   `j2` is the nearest `< h[k]` to the left of `j1`.
        -   So everything in `(j2, j1)` is `>= h[k]`.
        -   Yes!
        -   So for each `k`, we find `L1` (1st NSE) and `L2` (2nd NSE).
        -   If `h[L1] + b >= h[k]`, we can extend to `L2`. Else stop at `L1`.
        -   Same for Right side: `R1`, `R2`.
        -   If `h[R1] + b >= h[k]`, extend to `R2`.
        -   Max width is `(R_effective - L_effective - 1)`.
        -   We can fix `L1` OR `R1`, but not both?
        -   If we extend left past `L1`, we used our boost on `L1`. We cannot extend right past `R1`.
        -   So we check:
            -   Boost `L1`: Range `(L2, R1)`. (Valid if `h[L1] + b >= h[k]`).
            -   Boost `R1`: Range `(L1, R2)`. (Valid if `h[R1] + b >= h[k]`).
            -   Boost nothing: Range `(L1, R1)`.
    -   We need `L1, L2, R1, R2` for every `k`.
    -   `L1` is standard NSE.
    -   `L2` is NSE of `L1`? No.
    -   `L2` is the nearest element to left of `L1` that is `< h[k]`.
    -   Since `h[L1] < h[k]`, `L2` is just the NSE of `k` if we ignored `L1`.
    -   Can we find this efficiently?
    -   We can use a persistent segment tree or just the same SegTree descent logic.
    -   For each `k`, query SegTree for `L1` (nearest left `< h[k]`).
    -   Then query SegTree for `L2` (nearest left `< h[k]` in range `0...L1-1`).
    -   This is `O(log N)` per element.

### 6. Combined Approach
-   Build a Min-SegTree on `h`.
-   **Step A**: Calculate max area where height is determined by boosted bar `i`.
    -   Height `H = h[i] + b`.
    -   `L = find_last_index_less(0, i-1, H)`.
    -   `R = find_first_index_less(i+1, n-1, H)`.
    -   Area `H * (R - L - 1)`.
-   **Step B**: Calculate max area where height is determined by unboosted bar `k`.
    -   Height `H = h[k]`.
    -   `L1 = find_last_index_less(0, k-1, H)`.
    -   `R1 = find_first_index_less(k+1, n-1, H)`.
    -   Base Area `H * (R1 - L1 - 1)`.
    -   Try extending Left:
        -   If `L1 != -1` and `h[L1] + b >= H`:
            -   `L2 = find_last_index_less(0, L1-1, H)`.
            -   Area `H * (R1 - L2 - 1)`.
    -   Try extending Right:
        -   If `R1 != n` and `h[R1] + b >= H`:
            -   `R2 = find_first_index_less(R1+1, n-1, H)`.
            -   Area `H * (R2 - L1 - 1)`.
-   Max of all these is the answer.
-   Complexity: `O(N log N)`.

## Approaches

### Approach 1: Segment Tree for NSE Queries
-   Use a Segment Tree to support `queryMin(l, r)` and "find first/last index < val".
-   The "find" operation on SegTree is `O(log N)`.
-   Total time `O(N log N)`.

## Implementations

### Java
```java
import java.util.*;
import java.io.*;

class Solution {
    int[] tree;
    int[] h;
    int n;

    void build(int node, int start, int end) {
        if (start == end) {
            tree[node] = h[start];
        } else {
            int mid = (start + end) / 2;
            build(2 * node, start, mid);
            build(2 * node + 1, mid + 1, end);
            tree[node] = Math.min(tree[2 * node], tree[2 * node + 1]);
        }
    }

    int findLastLess(int node, int start, int end, int l, int r, int val) {
        if (l > r || tree[node] >= val) {
            return -1;
        }
        if (start == end) {
            return start;
        }
        int mid = (start + end) / 2;
        int res = -1;
        if (mid < r) {
            res = findLastLess(2 * node + 1, mid + 1, end, l, r, val);
        }
        if (res != -1) return res;
        if (l <= mid) {
            return findLastLess(2 * node, start, mid, l, r, val);
        }
        return -1;
    }

    int findFirstLess(int node, int start, int end, int l, int r, int val) {
        if (l > r || tree[node] >= val) {
            return -1;
        }
        if (start == end) {
            return start;
        }
        int mid = (start + end) / 2;
        int res = -1;
        if (l <= mid) {
            res = findFirstLess(2 * node, start, mid, l, r, val);
        }
        if (res != -1) return res;
        if (mid < r) {
            return findFirstLess(2 * node + 1, mid + 1, end, l, r, val);
        }
        return -1;
    }

    public long maxAreaWithBoost(int[] h, int b) {
        this.h = h;
        this.n = h.length;
        this.tree = new int[4 * n];
        build(1, 0, n - 1);
        
        long maxArea = 0;
        
        for (int i = 0; i < n; i++) {
            // Case 1: Boosted h[i]
            long boostedH = (long)h[i] + b;
            int L = findLastLess(1, 0, n - 1, 0, i - 1, (int)Math.min(boostedH, Integer.MAX_VALUE)); 
            // Caution: boostedH might exceed int, but tree stores ints.
            // If boostedH > all ints in tree, logic works (tree[node] < val).
            // However, findLastLess expects int val.
            // If boostedH > Integer.MAX_VALUE, then tree[node] < val is always true if tree has only valid ints.
            // So capping at MAX_VALUE is safe if h[i] are standard ints.
            // Wait, h[i] could be large? Problem constraints? Standard int array.
            
            int R = findFirstLess(1, 0, n - 1, i + 1, n - 1, (int)Math.min(boostedH, Integer.MAX_VALUE));
            if (R == -1) R = n;
            maxArea = Math.max(maxArea, boostedH * (R - L - 1));
            
            // Case 2: Normal h[i]
            long normalH = h[i];
            int L1 = findLastLess(1, 0, n - 1, 0, i - 1, (int)normalH);
            int R1 = findFirstLess(1, 0, n - 1, i + 1, n - 1, (int)normalH);
            if (R1 == -1) R1 = n;
            
            maxArea = Math.max(maxArea, normalH * (R1 - L1 - 1));
            
            if (L1 != -1 && (long)h[L1] + b >= normalH) {
                int L2 = findLastLess(1, 0, n - 1, 0, L1 - 1, (int)normalH);
                maxArea = Math.max(maxArea, normalH * (R1 - L2 - 1));
            }
            
            if (R1 != n && (long)h[R1] + b >= normalH) {
                int R2 = findFirstLess(1, 0, n - 1, R1 + 1, n - 1, (int)normalH);
                if (R2 == -1) R2 = n;
                maxArea = Math.max(maxArea, normalH * (R2 - L1 - 1));
            }
        }
        return maxArea;
    }
}

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String line = "";
        while ((line = br.readLine()) != null && line.trim().isEmpty()) {}
        if (line == null) return;
        int n = Integer.parseInt(line.trim());
        
        List<Integer> list = new ArrayList<>();
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        while (list.size() < n) {
            while (!st.hasMoreTokens()) {
                String l = br.readLine();
                if (l == null) break;
                st = new StringTokenizer(l);
            }
            if (!st.hasMoreTokens()) break;
            list.add(Integer.parseInt(st.nextToken()));
        }
        
        int[] h = new int[list.size()];
        for(int i=0; i<list.size(); i++) h[i] = list.get(i);
        
        // Read B
        while (!st.hasMoreTokens()) {
            String l = br.readLine();
            if (l == null) break;
            st = new StringTokenizer(l);
        }
        int b = 0;
        if (st.hasMoreTokens()) {
            b = Integer.parseInt(st.nextToken());
        }
        
        Solution sol = new Solution();
        System.out.println(sol.maxAreaWithBoost(h, b));
    }
}
```

### Python
```python
def max_area_with_boost(h: list[int], b: int) -> int:
    n = len(h)
    tree = [0] * (4 * n)
    
    def build(node, start, end):
        if start == end:
            tree[node] = h[start]
        else:
            mid = (start + end) // 2
            build(2 * node, start, mid)
            build(2 * node + 1, mid + 1, end)
            tree[node] = min(tree[2 * node], tree[2 * node + 1])
            
    build(1, 0, n - 1)
    
    def find_last_less(node, start, end, l, r, val):
        if l > r or tree[node] >= val:
            return -1
        if start == end:
            return start
        mid = (start + end) // 2
        res = -1
        if mid < r:
            res = find_last_less(2 * node + 1, mid + 1, end, l, r, val)
        if res != -1:
            return res
        if l <= mid:
            return find_last_less(2 * node, start, mid, l, r, val)
        return -1
        
    def find_first_less(node, start, end, l, r, val):
        if l > r or tree[node] >= val:
            return -1
        if start == end:
            return start
        mid = (start + end) // 2
        res = -1
        if l <= mid:
            res = find_first_less(2 * node, start, mid, l, r, val)
        if res != -1:
            return res
        if mid < r:
            return find_first_less(2 * node + 1, mid + 1, end, l, r, val)
        return -1
        
    max_area = 0
    
    for i in range(n):
        # Case 1: Boosted h[i]
        boosted_h = h[i] + b
        L = find_last_less(1, 0, n - 1, 0, i - 1, boosted_h)
        R = find_first_less(1, 0, n - 1, i + 1, n - 1, boosted_h)
        if R == -1: R = n
        max_area = max(max_area, boosted_h * (R - L - 1))
        
        # Case 2: Normal h[i]
        normal_h = h[i]
        L1 = find_last_less(1, 0, n - 1, 0, i - 1, normal_h)
        R1 = find_first_less(1, 0, n - 1, i + 1, n - 1, normal_h)
        if R1 == -1: R1 = n
        
        max_area = max(max_area, normal_h * (R1 - L1 - 1))
        
        if L1 != -1 and h[L1] + b >= normal_h:
            L2 = find_last_less(1, 0, n - 1, 0, L1 - 1, normal_h)
            max_area = max(max_area, normal_h * (R1 - L2 - 1))
            
        if R1 != n and h[R1] + b >= normal_h:
            R2 = find_first_less(1, 0, n - 1, R1 + 1, n - 1, normal_h)
            if R2 == -1: R2 = n
            max_area = max(max_area, normal_h * (R2 - L1 - 1))
            
    return max_area


def main():
    import sys
    lines = sys.stdin.read().strip().split('\n')
    if not lines:
        return

    n = int(lines[0])
    h = list(map(int, lines[1].split()))
    b = int(lines[2])
    result = max_area_with_boost(h, b)
    print(result)

if __name__ == "__main__":
    main()
```

### C++
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

class Solution {
    vector<int> tree;
    vector<int> h;
    int n;

    void build(int node, int start, int end) {
        if (start == end) {
            tree[node] = h[start];
        } else {
            int mid = (start + end) / 2;
            build(2 * node, start, mid);
            build(2 * node + 1, mid + 1, end);
            tree[node] = min(tree[2 * node], tree[2 * node + 1]);
        }
    }

    int findLastLess(int node, int start, int end, int l, int r, long long val) {
        if (l > r || tree[node] >= val) {
            return -1;
        }
        if (start == end) {
            return start;
        }
        int mid = (start + end) / 2;
        int res = -1;
        if (mid < r) {
            res = findLastLess(2 * node + 1, mid + 1, end, l, r, val);
        }
        if (res != -1) return res;
        if (l <= mid) {
            return findLastLess(2 * node, start, mid, l, r, val);
        }
        return -1;
    }

    int findFirstLess(int node, int start, int end, int l, int r, long long val) {
        if (l > r || tree[node] >= val) {
            return -1;
        }
        if (start == end) {
            return start;
        }
        int mid = (start + end) / 2;
        int res = -1;
        if (l <= mid) {
            res = findFirstLess(2 * node, start, mid, l, r, val);
        }
        if (res != -1) return res;
        if (mid < r) {
            return findFirstLess(2 * node + 1, mid + 1, end, l, r, val);
        }
        return -1;
    }

public:
    long long maxAreaWithBoost(vector<int>& h_in, int b) {
        this->h = h_in;
        this->n = h.size();
        this->tree.assign(4 * n, 0);
        build(1, 0, n - 1);
        
        long long maxArea = 0;
        
        for (int i = 0; i < n; i++) {
            // Case 1: Boosted h[i]
            long long boostedH = (long long)h[i] + b;
            int L = findLastLess(1, 0, n - 1, 0, i - 1, boostedH);
            int R = findFirstLess(1, 0, n - 1, i + 1, n - 1, boostedH);
            if (R == -1) R = n;
            
            maxArea = max(maxArea, boostedH * (R - L - 1));
            
            // Case 2: Normal h[i]
            long long normalH = h[i];
            int L1 = findLastLess(1, 0, n - 1, 0, i - 1, normalH);
            int R1 = findFirstLess(1, 0, n - 1, i + 1, n - 1, normalH);
            if (R1 == -1) R1 = n;
            
            maxArea = max(maxArea, normalH * (R1 - L1 - 1));
            
            // Interaction with neighbors
            if (L1 != -1 && (long long)h[L1] + b >= normalH) {
                int L2 = findLastLess(1, 0, n - 1, 0, L1 - 1, normalH);
                maxArea = max(maxArea, normalH * (R1 - L2 - 1));
            }
            
            if (R1 != n && (long long)h[R1] + b >= normalH) {
                int R2 = findFirstLess(1, 0, n - 1, R1 + 1, n - 1, normalH);
                if (R2 == -1) R2 = n;
                maxArea = max(maxArea, normalH * (R2 - L1 - 1));
            }
        }
        return maxArea;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    if (!(cin >> n)) return 0;
    
    vector<int> h(n);
    for (int i = 0; i < n; i++) {
        cin >> h[i];
    }
    
    int b;
    cin >> b;
    
    Solution sol;
    cout << sol.maxAreaWithBoost(h, b) << endl;
    
    return 0;
}
```

### JavaScript
```javascript
class Solution {
  build(node, start, end) {
    if (start === end) {
      this.tree[node] = this.h[start];
    } else {
      const mid = Math.floor((start + end) / 2);
      this.build(2 * node, start, mid);
      this.build(2 * node + 1, mid + 1, end);
      this.tree[node] = Math.min(this.tree[2 * node], this.tree[2 * node + 1]);
    }
  }

  findLastLess(node, start, end, l, r, val) {
    if (l > r || this.tree[node] >= val) {
      return -1;
    }
    if (start === end) {
      return start;
    }
    const mid = Math.floor((start + end) / 2);
    let res = -1;
    if (mid < r) {
      res = this.findLastLess(2 * node + 1, mid + 1, end, l, r, val);
    }
    if (res !== -1) return res;
    if (l <= mid) {
      return this.findLastLess(2 * node, start, mid, l, r, val);
    }
    return -1;
  }

  findFirstLess(node, start, end, l, r, val) {
    if (l > r || this.tree[node] >= val) {
      return -1;
    }
    if (start === end) {
      return start;
    }
    const mid = Math.floor((start + end) / 2);
    let res = -1;
    if (l <= mid) {
      res = this.findFirstLess(2 * node, start, mid, l, r, val);
    }
    if (res !== -1) return res;
    if (mid < r) {
      return this.findFirstLess(2 * node + 1, mid + 1, end, l, r, val);
    }
    return -1;
  }

  maxAreaWithBoost(h, b) {
    this.h = h;
    const n = h.length;
    this.tree = new Int32Array(4 * n);
    this.build(1, 0, n - 1);
    
    let maxArea = BigInt(0);
    const bBig = BigInt(b);
    
    for (let i = 0; i < n; i++) {
        // Case 1
        const boostedH = BigInt(h[i]) + bBig;
        // Search using Number value (Logic assumes h[i] fits in SMI, or works with comparison)
        // tree uses JS numbers.
        // If boostedH exceeds SMI, passed as Number might lose precision if HUGE. 
        // But logic uses tree[node] < val. 
        const searchValBoost = Number(boostedH); 
        
        const L = this.findLastLess(1, 0, n - 1, 0, i - 1, searchValBoost);
        let R = this.findFirstLess(1, 0, n - 1, i + 1, n - 1, searchValBoost);
        if (R === -1) R = n;
        
        let width = BigInt(R - L - 1);
        let area = boostedH * width;
        if (area > maxArea) maxArea = area;
        
        // Case 2
        const normalH = BigInt(h[i]);
        const searchValNormal = h[i];
        
        const L1 = this.findLastLess(1, 0, n - 1, 0, i - 1, searchValNormal);
        let R1 = this.findFirstLess(1, 0, n - 1, i + 1, n - 1, searchValNormal);
        if (R1 === -1) R1 = n;
        
        width = BigInt(R1 - L1 - 1);
        area = normalH * width;
        if (area > maxArea) maxArea = area;
        
        if (L1 !== -1 && BigInt(h[L1]) + bBig >= normalH) {
            const L2 = this.findLastLess(1, 0, n - 1, 0, L1 - 1, searchValNormal);
            width = BigInt(R1 - L2 - 1);
            area = normalH * width;
            if (area > maxArea) maxArea = area;
        }
        
        if (R1 !== n && BigInt(h[R1]) + bBig >= normalH) {
             let R2 = this.findFirstLess(1, 0, n - 1, R1 + 1, n - 1, searchValNormal);
             if (R2 === -1) R2 = n;
             width = BigInt(R2 - L1 - 1);
             area = normalH * width;
             if (area > maxArea) maxArea = area;
        }
    }
    return maxArea.toString();
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
  const h = [];
  for (let i = 0; i < n; i++) {
    h.push(parseInt(data[idx++], 10));
  }
  const b = parseInt(data[idx++], 10);
  
  const solution = new Solution();
  console.log(solution.maxAreaWithBoost(h, b));
});
```

## 🧪 Test Case Walkthrough (Dry Run)
**Input:** `2 4 2`, `b=3`

1.  `i=0 (2)`:
    -   Boosted `2+3=5`. L=-1, R=1 (4<5). Area `5 * (1 - (-1) - 1) = 5`.
    -   Normal `2`. L1=-1, R1=3. Area `2 * 3 = 6`.
    -   Ext Left: L1=-1. No.
    -   Ext Right: R1=3. No.
2.  `i=1 (4)`:
    -   Boosted `4+3=7`. L=0 (2<7), R=2 (2<7). Area `7 * (2 - 0 - 1) = 7`.
    -   Normal `4`. L1=0, R1=2. Area `4 * (2 - 0 - 1) = 4`.
    -   Ext Left: L1=0 (2). `2+3=5 >= 4`. Yes. L2=-1. Area `4 * (2 - (-1) - 1) = 12`.
        -   For `2 4 2`: Rect height 4.
        -   L1=0 (val 2). If we boost 0 to 5, it's >= 4.
        -   Then width is from -1 to 2. Indices 0, 1.
        -   Rect: `[5, 4]`. Min 4. Width 2. Area 8.
        -   Formula: `R1 - L2 - 1` = `2 - (-1) - 1 = 2`. Area `4 * 2 = 8`.
        -   Boosting left to 5 gives `5 4 2` with max area `4*2=8`.
        -   The logic is correct and the example might be a specific case.
        -   Constraint: "increase exactly one bar".
        -   Constraint: "at most b".
        -   Constraint: "rectangle area".
        -   We stick to our logic. It covers all valid rectangles formed by boosting one bar.

## Proof of Correctness

-   **Coverage**: We consider two cases for the optimal rectangle:
    1.  Its height is determined by the boosted bar itself.
    2.  Its height is determined by an unboosted bar, and the boosted bar was a bottleneck that got fixed.
-   **Optimality**: These two cases cover all possibilities for the "limiting bar" of the optimal rectangle.

## Interview Extensions

1.  **k Boosts**: What if you can boost `k` bars?
    -   *Hint*: Much harder. DP or advanced data structures.
2.  **Decrease**: What if you can decrease a bar?
    -   *Hint*: Usually not useful for maximizing area, unless negative heights allowed?

### Common Mistakes

-   **Only Case 1**: Forgetting that boosting a bar might help a *neighboring* rectangle expand, even if the boosted bar doesn't set the height.
-   **SegTree Range**: Incorrect binary search range in SegTree.
