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
time_limit: 2000
memory_limit: 256
---

# HEP-010: Top K Products with Index Gap

## Problem Statement

You are given two arrays `A` and `B`, each sorted in non-increasing order. Find the `k` largest products `A[i] * B[j]` subject to the constraint:

```
|i - j| >= d
```

Indices are 0-based. If fewer than `k` valid pairs exist, return all of them. Output products in descending order.

![Problem Illustration](../images/HEP-010/problem-illustration.png)

## Input Format

- First line: integers `n`, `m`, `k`, and `d`
- Second line: `n` integers for `A`
- Third line: `m` integers for `B`

## Output Format

- Single line of products in descending order

## Constraints

- `1 <= n, m <= 100000`
- `1 <= k <= min(100000, n * m)`
- `0 <= d < max(n, m)`
- `-10^9 <= A[i], B[j] <= 10^9`

## Example

**Input:**

```
3 3 3 1
9 7 5
8 3 1
```

**Output:**

```
56 40 27
```

**Explanation:**

Valid pairs with |i - j| >= 1 include:

- (1,0): 7 * 8 = 56
- (2,0): 5 * 8 = 40
- (0,1): 9 * 3 = 27

Top 3 products are 56, 40, 27.

![Example Visualization](../images/HEP-010/example-1.png)

## Notes

- Use a max-heap of candidate pairs
- Expand neighbors (i+1,j) and (i,j+1) when valid
- Track visited pairs to avoid duplicates
- Time complexity: O(k log k)
- Space complexity: O(k)

## Related Topics

Heaps, K Largest Pairs, Search, Two Arrays

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    static class Node implements Comparable<Node> {
        long val;
        int r, c;
        int dir; // 1 for TL (increase indices), -1 for BR (decrease indices)
        
        public Node(long val, int r, int c, int dir) {
        return 0;
    }
        
        @Override
        public int compareTo(Node other) {
        return 0;
    }
    }
    
    public List<Long> topKProducts(long[] A, long[] B, int k, int d) {
        return null;
    }
    
    private void add(PriorityQueue<Node> pq, Set<String> visited, long[] A, long[] B, int r, int c, int dir, int d) {
    }
    
    private void tryAdd(PriorityQueue<Node> pq, Set<String> visited, long[] A, long[] B, int r, int c, int dir, int d) {
    }
}

class Main {
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
        return []
def top_k_products(A: list, B: list, k: int, d: int) -> list:
    return []
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
    }
    
public:
    vector<long long> topKProducts(const vector<long long>& A, const vector<long long>& B, int k, int d) {
        return {};
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
    return 0;
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

