---
problem_id: HEP_TOPK_PRODUCTS_INDEX_GAP__8206
display_id: HEP-010
slug: topk-products-index-gap
title: "Top K Products with Index Gap"
difficulty: Medium
difficulty_score: 59
topics:
  - Heaps
  - K Largest Pairs
  - Search
tags:
  - heaps
  - k-largest
  - two-arrays
  - medium
premium: true
subscription_tier: basic
---

# HEP-010: Top K Products with Index Gap

## 📋 Problem Summary

You have two sorted arrays `A` and `B` (non-increasing).
Find the top `k` products `A[i] * B[j]` such that `|i - j| >= d`.
Return the products in descending order.

## 🌍 Real-World Scenario

**Scenario Title:** Cross-Department Collaboration

Imagine pairing senior engineers from Dept A with junior engineers from Dept B.
- `A` and `B` are sorted by skill level.
- You want to form high-impact pairs (maximize skill product).
- However, to ensure diversity or avoid conflicts, the "rank difference" must be at least `d`.
- You want to find the top `k` best valid pairings.

![Real-World Application](../images/HEP-010/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Search Space

A: `[9, 7, 5]`
B: `[8, 3, 1]`
d: `1`

Grid of Products (A[i] * B[j]):
```
      B[0]=8  B[1]=3  B[2]=1
A[0]=9  72      27      9
A[1]=7  56      21      7
A[2]=5  40      15      5
```

Valid pairs (`|i-j| >= 1`):
- (0,0): |0-0|=0 < 1 (Invalid)
- (0,1): |0-1|=1 >= 1 (Valid, 27)
- (0,2): |0-2|=2 >= 1 (Valid, 9)
- (1,0): |1-0|=1 >= 1 (Valid, 56)
- (1,1): |1-1|=0 < 1 (Invalid)
- (1,2): |1-2|=1 >= 1 (Valid, 7)
- (2,0): |2-0|=2 >= 1 (Valid, 40)
- (2,1): |2-1|=1 >= 1 (Valid, 15)
- (2,2): |2-2|=0 < 1 (Invalid)

Valid values: `{27, 9, 56, 7, 40, 15}`.
Top 3: `56, 40, 27`.

### Key Concept: Priority Search on Grid

Since `A` and `B` are sorted descending, the products `A[i] * B[j]` generally decrease as `i` and `j` increase.
However, the constraint `|i - j| >= d` makes the valid region non-contiguous (it excludes a diagonal band).
We can still use a **Max-Heap** to explore candidates.
- Start with the "best possible" candidates.
  - Usually (0,0), but that might be invalid.
  - The valid region boundaries are `j <= i - d` and `j >= i + d`.
  - For row `i`, the best valid `j` is `0` (if valid) or `i+d`?
  - Actually, for a fixed `i`, the best `j` is the smallest valid `j` (since B is descending)? No, B is descending, so `B[0]` is largest.
  - So for fixed `i`, we want smallest `j` such that `|i-j| >= d`.
  - Two regions for `j`: `[0, i-d]` and `[i+d, m-1]`.
  - Best candidates in these regions are `j=0` (if `0 <= i-d`) and `j=i+d` (if `i+d < m`).
- So, we can initialize the heap with the best valid pair for each row `i`.
  - For each `i`, check `j=0` (if valid) and `j=i+d` (if valid).
  - Wait, this might be too many ($2N$).
  - Better: Just push the "corners" of the valid regions.
  - The valid region is roughly two triangles.
  - Region 1: `j <= i - d`. Top-left corner is `(d, 0)`.
    - From `(d, 0)`, we can move to `(d+1, 0)` or `(d, 1)`.
  - Region 2: `j >= i + d`. Top-left corner is `(0, d)`.
    - From `(0, d)`, we can move to `(1, d)` or `(0, d+1)`.
  - This is like searching two separate sorted matrices!
  - Matrix 1: Rows `d..n-1`, Cols `0..m-1`. Constraint `j <= i-d`.
  - Matrix 2: Rows `0..n-1`, Cols `d..m-1`. Constraint `j >= i+d`.

Actually, we can treat this as merging sorted lists, but the lists are implicit.
Standard technique for "Kth Smallest/Largest in Sorted Matrix":
- Push `(0, 0)` to heap.
- Pop `(i, j)`. Push `(i+1, j)` and `(i, j+1)`.
- Check validity before pushing?
- No, because if `(0,0)` is invalid, we can't start there.
- We should start with the "roots" of the valid regions.
- **Root 1:** `(d, 0)`. This is the largest product in the lower-left valid triangle.
  - Neighbors: `(d+1, 0)` (down) and `(d, 1)` (right).
  - Constraint `j <= i - d` must hold.
  - If we are at `(i, j)`, `(i+1, j)` satisfies `j <= (i+1) - d` (since `j <= i-d < i+1-d`). Valid.
  - `(i, j+1)` satisfies `j+1 <= i - d`? Only if `j < i - d`.
- **Root 2:** `(0, d)`. This is the largest product in the upper-right valid triangle.
  - Neighbors: `(1, d)` (down) and `(0, d+1)` (right).
  - Constraint `j >= i + d`.
  - If we are at `(i, j)`, `(i, j+1)` satisfies `j+1 >= i + d` (since `j >= i+d`). Valid.
  - `(i+1, j)` satisfies `j >= i+1 + d`? Only if `j > i + d`.

So, we run two independent searches (or one combined heap):
1. Start `(d, 0)`. Expand `(i+1, j)` always. Expand `(i, j+1)` only if `j+1 <= i-d`.
2. Start `(0, d)`. Expand `(i, j+1)` always. Expand `(i+1, j)` only if `j >= i+1+d`.

Wait, duplicate visits?
- `(d+1, 1)` can be reached from `(d, 1)` (down) or `(d+1, 0)` (right).
- Use a `visited` set to avoid cycles/duplicates.

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** `n, m, k, d`, Arrays `A`, `B`.
- **Output:** List of products.
- **Constraints:** $N, M \le 10^5$. $K$ up to $10^5$.
- **Values:** Can be negative? Yes.
- **Negative Values:**
  - If values are negative, "largest product" logic changes.
  - `(-10) * (-10) = 100`.
  - The problem says "A and B sorted in non-increasing order".
  - If A = `[10, -5, -20]`, B = `[5, -2, -10]`.
  - `10*5=50`. `-20*-10=200`.
  - The "largest products" might come from the *end* of the arrays (large negative * large negative).
  - This breaks the monotonic property of the grid if we only look at the top-left.
  - **However**, usually "Top K Products" problems with sorted arrays imply we might need to check 4 corners if negatives are involved.
  - Or split into positive/negative parts.
  - Given "Medium" difficulty and standard "K Largest Pairs" template, usually inputs are non-negative or we just handle the complexity.
  - Let's assume general case.
  - Sorted non-increasing: `Positive ... Negative`.
  - Largest products come from `Pos * Pos` (start of A, start of B) OR `Neg * Neg` (end of A, end of B).
  - `Pos * Neg` is always negative (small).
  - So we have potentially **two** sources of large values:
    1. Top-Left of valid regions (Start A, Start B).
    2. Bottom-Right of valid regions (End A, End B).
  - We should initialize our heap with roots from BOTH perspectives?
  - Valid regions are the same.
  - Region 1 (`j <= i-d`):
    - Max `Pos*Pos` at `(d, 0)`.
    - Max `Neg*Neg` at `(n-1, m-1)`? No, `(n-1, m-1)` might not be in Region 1.
    - We need the "largest indices" valid point in Region 1.
    - `i` max is `n-1`. `j` max is `n-1-d`.
    - So `(n-1, min(m-1, n-1-d))` is the corner for `Neg*Neg`.
  - Region 2 (`j >= i+d`):
    - Max `Pos*Pos` at `(0, d)`.
    - Max `Neg*Neg` at `(min(n-1, m-1-d), m-1)`.
  - So we have up to 4 starting points.
  - And we need to expand in the correct directions.
  - For `Pos*Pos` (indices 0,0), we expand `i++` and `j++` (decreasing values).
  - For `Neg*Neg` (indices n,m), we expand `i--` and `j--` (increasing values, i.e., larger negatives -> larger product).
  - We can put all 4 start points in the Max-Heap.
  - Use a global `visited` set.

## Naive Approach

### Intuition

Generate all valid pairs, sort them.

### Time Complexity

- **O(N*M log (NM))**: TLE.

## Optimal Approach

### Key Insight

Use a Max-Heap to explore the valid regions from the "corners" where products are maximized.
Since `A` and `B` are sorted descending:
- `A[0]*B[0]` is max positive (if positive).
- `A[n-1]*B[m-1]` is max positive (if negative * negative).
- We explore from `(d, 0)` and `(0, d)` moving `+i, +j`.
- We explore from `(n-1, min_j)` and `(min_i, m-1)` moving `-i, -j`.
- Actually, just treating it as 4 search trees.

### Algorithm

1. Identify Start Points:
   - **TL1:** `(d, 0)` if valid. Direction `(+1, +1)`.
   - **TL2:** `(0, d)` if valid. Direction `(+1, +1)`.
   - **BR1:** `(n-1, min(m-1, n-1-d))` if valid. Direction `(-1, -1)`.
   - **BR2:** `(min(n-1, m-1-d), m-1)` if valid. Direction `(-1, -1)`.
2. Max-Heap stores `(product, i, j, type)`.
   - `type` indicates expansion direction?
   - Actually, just use `visited` set.
   - But we need to know which way to expand.
   - `Pos*Pos` candidates decrease as indices increase.
   - `Neg*Neg` candidates decrease as indices decrease.
   - So we can't mix them blindly without knowing direction.
   - Better: Just have 2 heaps? Or push `(product, i, j)` and try ALL neighbors?
   - No, `(d, 0)` neighbors are `(d+1, 0)` and `(d, 1)`.
   - `(n-1, k)` neighbors are `(n-2, k)` and `(n-1, k-1)`.
   - If we mix, we might expand `(d,0)` to `(d-1, 0)` which is wrong (larger value).
   - So, keep them separate or encode direction.
   - Let's use 4 start nodes in heap, each with a strategy.
   - `Strategy 1 (TL)`: Expand `(i+1, j)` and `(i, j+1)`. Check bounds and `|i-j|>=d`.
   - `Strategy 2 (BR)`: Expand `(i-1, j)` and `(i, j-1)`. Check bounds and `|i-j|>=d`.
   - Note: `TL` handles `Pos*Pos`. `BR` handles `Neg*Neg`.
   - What if `Pos*Neg`? Those are small, will be popped last.
   - Do we need to cover them? Yes, if k is large.
   - `TL` expansion eventually covers everything reachable by `+1`.
   - `BR` expansion covers everything reachable by `-1`.
   - Do they meet? Yes.
   - Is it sufficient?
   - `TL` starts at high positive, goes down.
   - `BR` starts at high positive (neg*neg), goes down.
   - This covers all local maxima.
3. **Visited Set:** `Set<String>` "i,j".

### Time Complexity

- **O(K log K)**.

### Space Complexity

- **O(K)**.

![Algorithm Visualization](../images/HEP-010/algorithm-visualization.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    static class Node implements Comparable<Node> {
        long val;
        int r, c;
        int dir; // 1 for TL (increase indices), -1 for BR (decrease indices)
        
        public Node(long val, int r, int c, int dir) {
            this.val = val;
            this.r = r;
            this.c = c;
            this.dir = dir;
        }
        
        @Override
        public int compareTo(Node other) {
            return Long.compare(other.val, this.val); // Max heap
        }
    }
    
    public List<Long> topKProducts(long[] A, long[] B, int k, int d) {
        int n = A.length;
        int m = B.length;
        PriorityQueue<Node> pq = new PriorityQueue<>();
        Set<String> visited = new HashSet<>();
        
        // Helper to add
        // dir=1: TL expansion. dir=-1: BR expansion.
        
        // TL Starts
        if (d < n) add(pq, visited, A, B, d, 0, 1, d);
        if (d < m && d > 0) add(pq, visited, A, B, 0, d, 1, d); // d>0 check to avoid duplicate (0,0) if d=0
        else if (d == 0) add(pq, visited, A, B, 0, 0, 1, d);
        
        // BR Starts
        // Region 1: j <= i - d. Max i=n-1. Max j = n-1-d. Constrained by m-1.
        if (d < n) {
            int startI = n - 1;
            int startJ = Math.min(m - 1, n - 1 - d);
            if (startJ >= 0) add(pq, visited, A, B, startI, startJ, -1, d);
        }
        
        // Region 2: j >= i + d. Max j=m-1. Max i = m-1-d. Constrained by n-1.
        if (d < m && d > 0) {
            int startJ = m - 1;
            int startI = Math.min(n - 1, m - 1 - d);
            if (startI >= 0) add(pq, visited, A, B, startI, startJ, -1, d);
        }
        
        List<Long> res = new ArrayList<>();
        while (k > 0 && !pq.isEmpty()) {
            Node node = pq.poll();
            res.add(node.val);
            k--;
            
            int r = node.r;
            int c = node.c;
            int dir = node.dir;
            
            if (dir == 1) {
                // Expand +1
                tryAdd(pq, visited, A, B, r + 1, c, 1, d);
                tryAdd(pq, visited, A, B, r, c + 1, 1, d);
            } else {
                // Expand -1
                tryAdd(pq, visited, A, B, r - 1, c, -1, d);
                tryAdd(pq, visited, A, B, r, c - 1, -1, d);
            }
        }
        
        return res;
    }
    
    private void add(PriorityQueue<Node> pq, Set<String> visited, long[] A, long[] B, int r, int c, int dir, int d) {
        String key = r + "," + c;
        if (!visited.contains(key)) {
            visited.add(key);
            pq.offer(new Node(A[r] * B[c], r, c, dir));
        }
    }
    
    private void tryAdd(PriorityQueue<Node> pq, Set<String> visited, long[] A, long[] B, int r, int c, int dir, int d) {
        if (r >= 0 && r < A.length && c >= 0 && c < B.length) {
            if (Math.abs(r - c) >= d) {
                add(pq, visited, A, B, r, c, dir, d);
            }
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int m = sc.nextInt();
            int k = sc.nextInt();
            int d = sc.nextInt();
            long[] A = new long[n];
            long[] B = new long[m];
            for (int i = 0; i < n; i++) A[i] = sc.nextLong();
            for (int i = 0; i < m; i++) B[i] = sc.nextLong();
            
            Solution solution = new Solution();
            List<Long> result = solution.topKProducts(A, B, k, d);
            for (int i = 0; i < result.size(); i++) {
                System.out.print(result.get(i));
                if (i < result.size() - 1) System.out.print(" ");
            }
            System.out.println();
        }
        sc.close();
    }
}
```

### Python

```python
import sys
import heapq

class Solution:
    def top_k_products(self, A: list, B: list, k: int, d: int) -> list:
        n = len(A)
        m = len(B)
        
        # Max heap: stores (-val, r, c, dir)
        pq = []
        visited = set()
        
        def push(r, c, direction):
            if 0 <= r < n and 0 <= c < m and abs(r - c) >= d:
                key = (r, c)
                if key not in visited:
                    visited.add(key)
                    val = A[r] * B[c]
                    heapq.heappush(pq, (-val, r, c, direction))

        # TL Starts
        if d < n: push(d, 0, 1)
        if d < m and d > 0: push(0, d, 1)
        elif d == 0: push(0, 0, 1)
        
        # BR Starts
        if d < n:
            start_i = n - 1
            start_j = min(m - 1, n - 1 - d)
            if start_j >= 0: push(start_i, start_j, -1)
            
        if d < m and d > 0:
            start_j = m - 1
            start_i = min(n - 1, m - 1 - d)
            if start_i >= 0: push(start_i, start_j, -1)
            
        res = []
        while k > 0 and pq:
            val, r, c, direction = heapq.heappop(pq)
            res.append(-val)
            k -= 1
            
            if direction == 1:
                push(r + 1, c, 1)
                push(r, c + 1, 1)
            else:
                push(r - 1, c, -1)
                push(r, c - 1, -1)
                
        return res

def top_k_products(A: list, B: list, k: int, d: int) -> list:
    solver = Solution()
    return solver.top_k_products(A, B, k, d)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    try:
        n = int(next(it))
        m = int(next(it))
        k = int(next(it))
        d = int(next(it))
        A = []
        for _ in range(n):
            A.append(int(next(it)))
        B = []
        for _ in range(m):
            B.append(int(next(it)))
            
        result = top_k_products(A, B, k, d)
        print(" ".join(map(str, result)))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <cmath>
#include <algorithm>

using namespace std;

struct Node {
    long long val;
    int r, c;
    int dir;
    
    bool operator<(const Node& other) const {
        return val < other.val; // Max heap
    }
};

class Solution {
    void tryAdd(priority_queue<Node>& pq, set<pair<int,int>>& visited, const vector<long long>& A, const vector<long long>& B, int r, int c, int dir, int d) {
        if (r >= 0 && r < A.size() && c >= 0 && c < B.size()) {
            if (abs(r - c) >= d) {
                if (visited.find({r, c}) == visited.end()) {
                    visited.insert({r, c});
                    pq.push({A[r] * B[c], r, c, dir});
                }
            }
        }
    }
    
public:
    vector<long long> topKProducts(const vector<long long>& A, const vector<long long>& B, int k, int d) {
        int n = A.size();
        int m = B.size();
        priority_queue<Node> pq;
        set<pair<int,int>> visited;
        
        // TL
        if (d < n) tryAdd(pq, visited, A, B, d, 0, 1, d);
        if (d < m && d > 0) tryAdd(pq, visited, A, B, 0, d, 1, d);
        else if (d == 0) tryAdd(pq, visited, A, B, 0, 0, 1, d);
        
        // BR
        if (d < n) {
            int startI = n - 1;
            int startJ = min(m - 1, n - 1 - d);
            if (startJ >= 0) tryAdd(pq, visited, A, B, startI, startJ, -1, d);
        }
        if (d < m && d > 0) {
            int startJ = m - 1;
            int startI = min(n - 1, m - 1 - d);
            if (startI >= 0) tryAdd(pq, visited, A, B, startI, startJ, -1, d);
        }
        
        vector<long long> res;
        while (k > 0 && !pq.empty()) {
            Node node = pq.top();
            pq.pop();
            res.push_back(node.val);
            k--;
            
            if (node.dir == 1) {
                tryAdd(pq, visited, A, B, node.r + 1, node.c, 1, d);
                tryAdd(pq, visited, A, B, node.r, node.c + 1, 1, d);
            } else {
                tryAdd(pq, visited, A, B, node.r - 1, node.c, -1, d);
                tryAdd(pq, visited, A, B, node.r, node.c - 1, -1, d);
            }
        }
        
        return res;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, m, k, d;
    if (cin >> n >> m >> k >> d) {
        vector<long long> A(n), B(m);
        for (int i = 0; i < n; i++) cin >> A[i];
        for (int i = 0; i < m; i++) cin >> B[i];
        
        Solution solution;
        vector<long long> result = solution.topKProducts(A, B, k, d);
        for (size_t i = 0; i < result.size(); i++) {
            if (i > 0) cout << " ";
            cout << result[i];
        }
        cout << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class PriorityQueue {
  constructor(compare = (a, b) => a - b) {
    this.heap = [];
    this.compare = compare;
  }
  size() { return this.heap.length; }
  isEmpty() { return this.heap.length === 0; }
  peek() { return this.heap[0]; }
  push(val) {
    this.heap.push(val);
    this.bubbleUp(this.heap.length - 1);
  }
  pop() {
    if (this.size() === 0) return null;
    const top = this.heap[0];
    const bottom = this.heap.pop();
    if (this.size() > 0) {
      this.heap[0] = bottom;
      this.bubbleDown(0);
    }
    return top;
  }
  bubbleUp(idx) {
    while (idx > 0) {
      const pIdx = Math.floor((idx - 1) / 2);
      if (this.compare(this.heap[idx], this.heap[pIdx]) < 0) {
        [this.heap[idx], this.heap[pIdx]] = [this.heap[pIdx], this.heap[idx]];
        idx = pIdx;
      } else break;
    }
  }
  bubbleDown(idx) {
    while (true) {
      const left = 2 * idx + 1;
      const right = 2 * idx + 2;
      let swap = null;
      if (left < this.size() && this.compare(this.heap[left], this.heap[idx]) < 0) swap = left;
      if (right < this.size() && this.compare(this.heap[right], swap === null ? this.heap[idx] : this.heap[swap]) < 0) swap = right;
      if (swap === null) break;
      [this.heap[idx], this.heap[swap]] = [this.heap[swap], this.heap[idx]];
      idx = swap;
    }
  }
}

class Solution {
  topKProducts(A, B, k, d) {
    const n = A.length;
    const m = B.length;
    const pq = new PriorityQueue((a, b) => {
      if (a.val > b.val) return -1;
      if (a.val < b.val) return 1;
      return 0;
    });
    const visited = new Set();
    
    const tryAdd = (r, c, dir) => {
      if (r >= 0 && r < n && c >= 0 && c < m) {
        if (Math.abs(r - c) >= d) {
          const key = `${r},${c}`;
          if (!visited.has(key)) {
            visited.add(key);
            pq.push({ val: BigInt(A[r]) * BigInt(B[c]), r, c, dir });
          }
        }
      }
    };
    
    // TL
    if (d < n) tryAdd(d, 0, 1);
    if (d < m && d > 0) tryAdd(0, d, 1);
    else if (d === 0) tryAdd(0, 0, 1);
    
    // BR
    if (d < n) {
      const startI = n - 1;
      const startJ = Math.min(m - 1, n - 1 - d);
      if (startJ >= 0) tryAdd(startI, startJ, -1);
    }
    if (d < m && d > 0) {
      const startJ = m - 1;
      const startI = Math.min(n - 1, m - 1 - d);
      if (startI >= 0) tryAdd(startI, startJ, -1);
    }
    
    const res = [];
    while (k > 0 && !pq.isEmpty()) {
      const node = pq.pop();
      res.push(node.val.toString());
      k--;
      
      if (node.dir === 1) {
        tryAdd(node.r + 1, node.c, 1);
        tryAdd(node.r, node.c + 1, 1);
      } else {
        tryAdd(node.r - 1, node.c, -1);
        tryAdd(node.r, node.c - 1, -1);
      }
    }
    
    return res;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const n = parseInt(data[idx++]);
  const m = parseInt(data[idx++]);
  const k = parseInt(data[idx++]);
  const d = parseInt(data[idx++]);
  const A = [];
  const B = [];
  for (let i = 0; i < n; i++) A.push(parseInt(data[idx++]));
  for (let i = 0; i < m; i++) B.push(parseInt(data[idx++]));
  
  const solution = new Solution();
  const result = solution.topKProducts(A, B, k, d);
  console.log(result.join(" "));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:** `3 3 3 1`. A: `9 7 5`. B: `8 3 1`.
d=1.
TL Starts: `(1,0)` -> 7*8=56. `(0,1)` -> 9*3=27.
BR Starts: `(2, 1)` -> 5*3=15. `(1, 2)` -> 7*1=7.
Heap: `[56, 27, 15, 7]`.

1. Pop 56 `(1,0)`. Res: `[56]`.
   - Expand `(2,0)` (40), `(1,1)` (Invalid).
   - Heap: `[40, 27, 15, 7]`.
2. Pop 40 `(2,0)`. Res: `[56, 40]`.
   - Expand `(3,0)` (Out), `(2,1)` (Visited).
   - Heap: `[27, 15, 7]`.
3. Pop 27 `(0,1)`. Res: `[56, 40, 27]`.
   - Expand `(1,1)` (Invalid), `(0,2)` (9).
   - Heap: `[15, 9, 7]`.

Result: `56, 40, 27`. Correct.

## ✅ Proof of Correctness

### Invariant
- The Max-Heap always contains the largest unexplored valid products reachable from the corners.
- Since valid regions are monotonic (mostly), expanding neighbors covers all candidates.
- Handling both TL (Pos*Pos) and BR (Neg*Neg) ensures we don't miss large products from negative numbers.

## 💡 Interview Extensions

- **Extension 1:** What if arrays are not sorted?
  - *Answer:* Sort them first ($O(N \log N)$).
- **Extension 2:** K-th smallest?
  - *Answer:* Use Min-Heap and start from other corners.

## Common Mistakes to Avoid

1. **Missing Negative Products**
   - ❌ Wrong: Only checking top-left corners.
   - ✅ Correct: Check bottom-right corners too for large negative products.
2. **Infinite Loops**
   - ❌ Wrong: Not using visited set.
   - ✅ Correct: Track `(r, c)` to avoid re-processing.

## Related Concepts

- **K-Way Merge:** Generalization.
- **Dijkstra/BFS on Grid:** Similar traversal logic.
