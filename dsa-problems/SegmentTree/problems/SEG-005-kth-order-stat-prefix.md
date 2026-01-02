---
problem_id: SEG_KTH_ORDER_STAT_PREFIX__7093
display_id: SEG-005
slug: kth-order-stat-prefix
title: "K-th Order Statistic in Prefix"
difficulty: Medium
difficulty_score: 57
topics:
  - Segment Tree
  - Persistent Data Structures
  - Order Statistics
tags:
  - segment-tree
  - persistent
  - kth-statistic
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# SEG-005: K-th Order Statistic in Prefix

## Problem Statement

Given an array `a`, answer queries of the form `PREFIX r k`: find the k-th smallest value in the prefix `a[0..r]`.

All indices are 0-based. It is guaranteed that `1 <= k <= r+1`.

![Problem Illustration](../images/SEG-005/problem-illustration.png)

## Input Format

- First line: integers `n` and `q`
- Second line: `n` space-separated integers
- Next `q` lines: `PREFIX r k`

## Output Format

- For each query, output the k-th smallest value

## Constraints

- `1 <= n, q <= 200000`
- `-10^9 <= a[i] <= 10^9`

## Example

**Input:**

```
4 1
5 1 3 2
PREFIX 3 2
```

**Output:**

```
2
```

**Explanation:**

The prefix is `[5,1,3,2]`, sorted as `[1,2,3,5]`, so the 2nd smallest is 2.

![Example Visualization](../images/SEG-005/example-1.png)

## Notes

- Coordinate-compress values for the segment tree domain
- Build a persistent segment tree for each prefix
- Query the tree to find the k-th smallest
- Time per query: O(log n)

## Related Topics

Persistent Segment Tree, Order Statistics, Prefix Queries

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    static class Node {
        int count;
        Node left, right;
        
        Node(int count, Node left, Node right) {
            this.count = count;
            this.left = left;
            this.right = right;
        }
    }
    
    private Node[] roots;
    private int[] unique;
    
    public int[] kthPrefix(int[] arr, int[][] queries) {
        return null;
    }
    
    private Node build(int l, int r) {
        return 0;
    }
    
    private Node update(Node node, int l, int r, int idx) {
        return 0;
    }
    
    private int query(Node node, int l, int r, int k) {
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int q = sc.nextInt();
            int[] arr = new int[n];
            for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
            int[][] queries = new int[q][2];
            for (int i = 0; i < q; i++) {
                String type = sc.next(); // PREFIX
                queries[i][0] = sc.nextInt();
                queries[i][1] = sc.nextInt();
            }
            Solution sol = new Solution();
            int[] results = sol.kthPrefix(arr, queries);
            for (int res : results) {
                System.out.println(res);
            }
        }
        sc.close();
    }
}
```

### Python

```python
import sys

# Increase recursion depth for deep trees
sys.setrecursionlimit(200000)

class Node:
    def __init__(self, count=0, left=None, right=None):
        return 0
def kth_prefix(arr: list[int], queries: list[tuple[int, int]]) -> list[int]:
    return []
def main():
    import sys
    # Increase recursion depth for deep trees
    sys.setrecursionlimit(300000)
    def input_gen():
        return 0

        for line in sys.stdin:

            for token in line.split():

                yield token

    it = input_gen()
    n = int(next(it))
    q = int(next(it))
    arr = [int(next(it)) for _ in range(n)]
    queries = []
    for _ in range(q):
        type = next(it) # PREFIX
        queries.append((int(next(it)), int(next(it))))
    
    results = kth_prefix(arr, queries)
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

struct Node {
    int count;
    Node *left, *right;
    
    Node(int count, Node* left, Node* right) : count(count), left(left), right(right) {}
};

class Solution {
    vector<Node*> roots;
    vector<int> unique;
    
    Node* build(int l, int r) {
        if (l == r) return new Node(0, nullptr, nullptr);
        int mid = (l + r) / 2;
        return new Node(0, build(l, mid), build(mid + 1, r));
    }
    
    Node* update(Node* node, int l, int r, int idx) {
        if (l == r) {
            return new Node(node->count + 1, nullptr, nullptr);
        }
        int mid = (l + r) / 2;
        Node* left = node->left;
        Node* right = node->right;
        if (idx <= mid) {
            left = update(left, l, mid, idx);
        } else {
            right = update(right, mid + 1, r, idx);
        }
        return new Node(left->count + right->count, left, right);
    }
    
    int query(Node* node, int l, int r, int k) {
        return 0;
    }

public:
    vector<int> kthPrefix(const vector<int>& arr, const vector<pair<int,int>>& queries) {
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    if (!(cin >> n >> q)) return 0;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    vector<pair<int, int>> queries(q);
    for (int i = 0; i < q; i++) {
        string type;
        cin >> type; // PREFIX
        cin >> queries[i].first >> queries[i].second;
    }
    Solution sol;
    vector<int> results = sol.kthPrefix(arr, queries);
    for (int res : results) {
        cout << res << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
class Solution {
  kthPrefix(arr, queries) {
    return 0;
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
  const q = parseInt(data[idx++], 10);
  const arr = [];
  for (let i = 0; i < n; i++) arr.push(parseInt(data[idx++], 10));
  const queries = [];
  for (let i = 0; i < q; i++) {
    const type = data[idx++]; // PREFIX
    queries.push([parseInt(data[idx++], 10), parseInt(data[idx++], 10)]);
  }
  const solution = new Solution();
  const out = solution.kthPrefix(arr, queries);
  console.log(out.join("\n"));
});
```

