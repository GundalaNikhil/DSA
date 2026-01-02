---
problem_id: SEG_RANGE_XOR_BASIS__8820
display_id: SEG-007
slug: range-xor-basis
title: "Range XOR Basis"
difficulty: Medium
difficulty_score: 56
topics:
  - Segment Tree
  - Bitwise
  - Linear Basis
tags:
  - segment-tree
  - xor
  - linear-basis
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# SEG-007: Range XOR Basis

## Problem Statement

Maintain an array `a` with point updates and queries asking for the maximum XOR value obtainable from any subset of elements in `a[l..r]`.

Operations:

- `SET i x`: set `a[i] = x`
- `MAXXOR l r`: output the maximum subset XOR in `[l, r]`

![Problem Illustration](../images/SEG-007/problem-illustration.png)

## Input Format

- First line: integers `n` and `q`
- Second line: `n` space-separated integers
- Next `q` lines: `SET` or `MAXXOR`

## Output Format

- For each `MAXXOR`, print the maximum XOR value

## Constraints

- `1 <= n, q <= 100000`
- `0 <= a[i], x <= 10^9`
- Indices are 0-based

## Example

**Input:**

```
3 1
1 2 3
MAXXOR 0 2
```

**Output:**

```
3
```

**Explanation:**

The maximum XOR from subset `{1,2}` is 3.

![Example Visualization](../images/SEG-007/example-1.png)

## Notes

- Store a linear basis in each segment tree node
- Merge bases when combining segments
- Query basis to compute max XOR
- Time per operation: O(log n * B)

## Related Topics

Linear Basis, Segment Tree, Bitwise

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    static class Basis {
        int[] b = new int[30];
        
        void insert(int x) {
            for (int i = 29; i >= 0; i--) {
                if (((x >> i) & 1) == 1) {
                    if (b[i] == 0) {
                        b[i] = x;
                        return;
                    }
                    x ^= b[i];
                }
            }
        }
        
        void merge(Basis other) {
            for (int i = 0; i < 30; i++) {
                if (other.b[i] != 0) {
                    insert(other.b[i]);
                }
            }
        }
        
        int maxXor() {
            int res = 0;
            for (int i = 29; i >= 0; i--) {
                if ((res ^ b[i]) > res) {
                    res ^= b[i];
                }
            }
            return res;
        }
    }
    
    private Basis[] tree;
    private int n;

    public List<Integer> process(int[] arr, List<String[]> ops) {
        return null;
    }

    private void build(int[] arr, int node, int start, int end) {
        if (start == end) {
            tree[node] = new Basis();
            tree[node].insert(arr[start]);
        } else {
            int mid = (start + end) / 2;
            build(arr, 2 * node + 1, start, mid);
            build(arr, 2 * node + 2, mid + 1, end);
            
            tree[node] = new Basis();
            tree[node].merge(tree[2 * node + 1]);
            tree[node].merge(tree[2 * node + 2]);
        }
    }

    private void update(int node, int start, int end, int idx, int val) {
        if (start == end) {
            tree[node] = new Basis();
            tree[node].insert(val);
        } else {
            int mid = (start + end) / 2;
            if (idx <= mid) update(2 * node + 1, start, mid, idx, val);
            else update(2 * node + 2, mid + 1, end, idx, val);
            
            tree[node] = new Basis();
            tree[node].merge(tree[2 * node + 1]);
            tree[node].merge(tree[2 * node + 2]);
        }
    }

    private Basis query(int node, int start, int end, int l, int r) {
        if (l > end || r < start) return new Basis();
        if (l <= start && end <= r) return tree[node];
        
        int mid = (start + end) / 2;
        Basis p1 = query(2 * node + 1, start, mid, l, r);
        Basis p2 = query(2 * node + 2, mid + 1, end, l, r);
        
        Basis res = new Basis();
        res.merge(p1);
        res.merge(p2);
        return res;
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
            List<String[]> ops = new ArrayList<>();
            for (int i = 0; i < q; i++) {
                String type = sc.next();
                ops.add(new String[]{type, sc.next(), sc.next()});
            }
            Solution sol = new Solution();
            List<Integer> results = sol.process(arr, ops);
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

class Basis:
    def __init__(self):
        return 0
    def insert(self, x):
        return 0
    def merge(self, other):
        return 0
    def max_xor(self):
        return 0
def process(arr: list[int], ops: list[list[str]]) -> list[int]:
    return []
def main():
    import sys
    def input_gen():
        return 0
    it = input_gen()
    n = int(next(it))
    q = int(next(it))
    arr = [int(next(it)) for _ in range(n)]
    ops = []
    for _ in range(q):
        type = next(it)
        ops.append([type, next(it), next(it)])
    
    results = process(arr, ops)
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

struct Basis {
    int b[30] = {0};
    
    void insert(int x) {
        for (int i = 29; i >= 0; i--) {
            if ((x >> i) & 1) {
                if (!b[i]) {
                    b[i] = x;
                    return;
                }
                x ^= b[i];
            }
        }
    }
    
    void merge(const Basis& other) {
        for (int i = 0; i < 30; i++) {
            if (other.b[i]) insert(other.b[i]);
        }
    }
    
    int maxXor() {
        int res = 0;
        for (int i = 29; i >= 0; i--) {
            if ((res ^ b[i]) > res) res ^= b[i];
        }
        return res;
    }
};

class Solution {
    vector<Basis> tree;
    int n;

    void build(const vector<int>& arr, int node, int start, int end) {
    }

    void update(int node, int start, int end, int idx, int val) {
    }

    Basis query(int node, int start, int end, int l, int r) {
        return 0;
    }

public:
    vector<int> process(const vector<int>& arr, const vector<vector<string>>& ops) {
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
    vector<vector<string>> ops(q);
    for (int i = 0; i < q; i++) {
        string type, a, b;
        cin >> type >> a >> b;
        ops[i] = {type, a, b};
    }
    Solution sol;
    vector<int> results = sol.process(arr, ops);
    for (int res : results) {
        cout << res << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
class Solution {
  process(arr, ops) {
    return 0;
  }
      insert(x) {
    return 0;
  }
      
      merge(other) {
    return 0;
  }
      
      maxXor() {
    return 0;
  }
    }

    const n = arr.length;
    const tree = new Array(4 * n).fill(null).map(() => new Basis());

    const build = (node, start, end) => {
      if (start === end) {
        tree[node] = new Basis();
        tree[node].insert(arr[start]);
      } else {
        const mid = Math.floor((start + end) / 2);
        build(2 * node + 1, start, mid);
        build(2 * node + 2, mid + 1, end);
        
        tree[node] = new Basis();
        tree[node].merge(tree[2 * node + 1]);
        tree[node].merge(tree[2 * node + 2]);
      }
    };

    const update = (node, start, end, idx, val) => {
      if (start === end) {
        tree[node] = new Basis();
        tree[node].insert(val);
      } else {
        const mid = Math.floor((start + end) / 2);
        if (idx <= mid) update(2 * node + 1, start, mid, idx, val);
        else update(2 * node + 2, mid + 1, end, idx, val);
        
        tree[node] = new Basis();
        tree[node].merge(tree[2 * node + 1]);
        tree[node].merge(tree[2 * node + 2]);
      }
    };

    const query = (node, start, end, l, r) => {
      if (l > end || r < start) return new Basis();
      if (l <= start && end <= r) return tree[node];
      
      const mid = Math.floor((start + end) / 2);
      const p1 = query(2 * node + 1, start, mid, l, r);
      const p2 = query(2 * node + 2, mid + 1, end, l, r);
      
      const res = new Basis();
      res.merge(p1);
      res.merge(p2);
      return res;
    };

    build(0, 0, n - 1);
    const results = [];

    for (const op of ops) {
      if (op[0] === "SET") {
        const idx = parseInt(op[1], 10);
        const val = parseInt(op[2], 10);
        update(0, 0, n - 1, idx, val);
      } else {
        const l = parseInt(op[1], 10);
        const r = parseInt(op[2], 10);
        const res = query(0, 0, n - 1, l, r);
        results.push(res.maxXor());
      }
    }
    return results;
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
  const ops = [];
  for (let i = 0; i < q; i++) {
    ops.push([data[idx++], data[idx++], data[idx++]]);
  }
  const solution = new Solution();
  const out = solution.process(arr, ops);
  console.log(out.join("\n"));
});
```

