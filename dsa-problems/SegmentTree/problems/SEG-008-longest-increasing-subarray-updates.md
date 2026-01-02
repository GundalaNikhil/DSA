---
problem_id: SEG_LONGEST_INCREASING_SUBARRAY_UPDATES__2654
display_id: SEG-008
slug: longest-increasing-subarray-updates
title: "Longest Increasing Subarray After Updates"
difficulty: Medium
difficulty_score: 55
topics:
  - Segment Tree
  - Dynamic Arrays
  - Monotonicity
tags:
  - segment-tree
  - increasing
  - updates
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# SEG-008: Longest Increasing Subarray After Updates

## Problem Statement

Given an array `a`, you must handle point updates. After each update, output the length of the longest strictly increasing contiguous subarray.

Operation:

- `SET i x`: set `a[i] = x`

![Problem Illustration](../images/SEG-008/problem-illustration.png)

## Input Format

- First line: integers `n` and `q`
- Second line: `n` space-separated integers
- Next `q` lines: `SET i x`

## Output Format

- For each update, print the current longest increasing subarray length

## Constraints

- `1 <= n, q <= 200000`
- `-10^9 <= a[i], x <= 10^9`

## Example

**Input:**

```
3 1
1 2 1
SET 2 3
```

**Output:**

```
3
```

**Explanation:**

After the update the array becomes `[1, 2, 3]`, which is strictly increasing.

![Example Visualization](../images/SEG-008/example-1.png)

## Notes

- Store prefix and suffix increasing lengths per segment
- Merge using boundary comparisons between segments
- Update affects only O(log n) nodes
- The answer is the max length stored at the root

## Related Topics

Segment Tree, Range Merge, Dynamic Updates

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    static class Node {
        int maxLen;
        int prefLen;
        int suffLen;
        int len;
        int leftVal;
        int rightVal;
        
        Node(int val) {
            maxLen = prefLen = suffLen = len = 1;
            leftVal = rightVal = val;
        }
        
        Node() {}
    }
    
    private Node[] tree;
    private int n;

    public int[] process(int[] arr, int[][] updates) {
        return null;
    }

    private Node merge(Node left, Node right) {
        Node res = new Node();
        res.len = left.len + right.len;
        res.leftVal = left.leftVal;
        res.rightVal = right.rightVal;
        
        res.maxLen = Math.max(left.maxLen, right.maxLen);
        res.prefLen = left.prefLen;
        res.suffLen = right.suffLen;
        
        if (left.rightVal < right.leftVal) {
            res.maxLen = Math.max(res.maxLen, left.suffLen + right.prefLen);
            if (left.prefLen == left.len) {
                res.prefLen = left.len + right.prefLen;
            }
            if (right.suffLen == right.len) {
                res.suffLen = right.len + left.suffLen;
            }
        }
        return res;
    }

    private void build(int[] arr, int node, int start, int end) {
        if (start == end) {
            tree[node] = new Node(arr[start]);
        } else {
            int mid = (start + end) / 2;
            build(arr, 2 * node + 1, start, mid);
            build(arr, 2 * node + 2, mid + 1, end);
            tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2]);
        }
    }

    private void update(int node, int start, int end, int idx, int val) {
        if (start == end) {
            tree[node] = new Node(val);
        } else {
            int mid = (start + end) / 2;
            if (idx <= mid) update(2 * node + 1, start, mid, idx, val);
            else update(2 * node + 2, mid + 1, end, idx, val);
            tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2]);
        }
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
            int[][] updates = new int[q][2];
            for (int i = 0; i < q; i++) {
                String type = sc.next(); // SET
                updates[i][0] = sc.nextInt();
                updates[i][1] = sc.nextInt();
            }
            Solution sol = new Solution();
            int[] results = sol.process(arr, updates);
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

class Node:
    def __init__(self, val=None):
        return 0
def process(arr: list[int], updates: list[tuple[int, int]]) -> list[int]:
    return []
def main():
    import sys
    def input_gen():
        return 0
    it = input_gen()
    n = int(next(it))
    q = int(next(it))
    arr = [int(next(it)) for _ in range(n)]
    updates = []
    for _ in range(q):
        type = next(it) # SET
        updates.append((int(next(it)), int(next(it))))
    
    results = process(arr, updates)
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

using namespace std;

struct Node {
    int maxLen;
    int prefLen;
    int suffLen;
    int len;
    int leftVal;
    int rightVal;
    
    Node() : maxLen(0), prefLen(0), suffLen(0), len(0), leftVal(0), rightVal(0) {}
    Node(int val) : maxLen(1), prefLen(1), suffLen(1), len(1), leftVal(val), rightVal(val) {}
};

class Solution {
    vector<Node> tree;
    int n;

    Node merge(const Node& left, const Node& right) {
        return 0;
    }

    void build(const vector<int>& arr, int node, int start, int end) {
    }

    void update(int node, int start, int end, int idx, int val) {
    }

public:
    vector<int> process(const vector<int>& inputArr, const vector<pair<int,int>>& updates) {
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
    vector<pair<int, int>> updates(q);
    for (int i = 0; i < q; i++) {
        string type;
        cin >> type; // SET
        cin >> updates[i].first >> updates[i].second;
    }
    Solution sol;
    vector<int> results = sol.process(arr, updates);
    for (int res : results) {
        cout << res << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
class Solution {
  process(arr, updates) {
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
  const updates = [];
  for (let i = 0; i < q; i++) {
    const type = data[idx++]; // SET
    updates.push([parseInt(data[idx++], 10), parseInt(data[idx++], 10)]);
  }
  const solution = new Solution();
  const out = solution.process(arr, updates);
  console.log(out.join("\n"));
});
```

