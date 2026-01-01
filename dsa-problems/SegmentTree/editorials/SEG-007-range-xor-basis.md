---
title: Range XOR Basis
slug: range-xor-basis
difficulty: Medium
difficulty_score: 56
tags:
- Segment Tree
- Linear Basis
- Bitwise
problem_id: SEG_RANGE_XOR_BASIS__8820
display_id: SEG-007
topics:
- Segment Tree
- Bitwise
- Linear Basis
---
# Range XOR Basis - Editorial

## Problem Summary

You are given an array `a` and need to support two operations:
1.  **SET i x**: Update `a[i] = x`.
2.  **MAXXOR l r**: Find the maximum XOR sum of any subset of elements in the range `a[l..r]`.


## Constraints

- `1 <= n, q <= 100000`
- `0 <= a[i], x <= 10^9`
- Indices are 0-based
## Real-World Scenario

Imagine a **Digital Signal Processing** system where you have a stream of signals. You want to combine a subset of signals (using XOR, which corresponds to addition in GF(2)) to produce the strongest possible signal (maximum value) within a specific time window. As new signals arrive or old ones are corrected, you need to re-evaluate the maximum potential signal strength.

## Problem Exploration

### 1. Linear Basis
The "Maximum Subset XOR" problem is classically solved using a **Linear Basis**.
A Linear Basis for a set of numbers is a minimal set of numbers such that any XOR sum achievable from the original set is also achievable from the basis.
-   Size of basis is at most `log(max(A_i)) ~= 30`.
-   We can merge two bases `B_1` and `B_2` by inserting every element of `B_2` into `B_1`. Size remains `<= 30`.
-   Merging takes `O(B^2)` or `O(B)` depending on implementation. Since `B` is small (30), this is efficient.

### 2. Segment Tree with Linear Basis
We can build a Segment Tree where each node stores the Linear Basis of the numbers in its range.
-   **Leaf Node**: Basis contains just `a[i]`.
-   **Internal Node**: Merge bases of left and right children.
-   **Update**: Update leaf, then re-merge up the tree. `O(B^2 log N)`.
-   **Query**: Query range `[l, r]`, merge bases of `O(log N)` segments, then compute max XOR. `O(B^2 log N)`.

With `B=30`, `B^2 ~= 900`. `N, Q = 100,000`.
`10^5 x 900 x 17 ~= 1.5 x 10^9`. This is a bit slow for 2 seconds.
We need to optimize the merge or be careful with constants.
Can we do better?
Standard merge is: take all elements of one basis and insert into other.
Since basis size is small, this is acceptable if implemented efficiently.

## Approaches

### Approach 1: Segment Tree with Linear Basis
-   **Node**: `vector<int> basis`.
-   **Merge**: Insert elements of `right` into `left`.
-   **Query**: Accumulate basis from relevant nodes.

## Implementations

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
        n = arr.length;
        tree = new Basis[4 * n];
        for(int i=0; i<4*n; i++) tree[i] = new Basis();
        
        build(arr, 0, 0, n - 1);
        
        List<Integer> results = new ArrayList<>();
        
        for (String[] op : ops) {
            if (op[0].equals("SET")) {
                int idx = Integer.parseInt(op[1]);
                int val = Integer.parseInt(op[2]);
                update(0, 0, n - 1, idx, val);
            } else {
                int l = Integer.parseInt(op[1]);
                int r = Integer.parseInt(op[2]);
                Basis res = query(0, 0, n - 1, l, r);
                results.add(res.maxXor());
            }
        }
        return results;
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
        self.b = [0] * 30
        
    def insert(self, x):
        for i in range(29, -1, -1):
            if (x >> i) & 1:
                if self.b[i] == 0:
                    self.b[i] = x
                    return
                x ^= self.b[i]
                
    def merge(self, other):
        for x in other.b:
            if x != 0:
                self.insert(x)
                
    def max_xor(self):
        res = 0
        for x in reversed(self.b):
            if (res ^ x) > res:
                res ^= x
        return res

def process(arr: list[int], ops: list[list[str]]) -> list[int]:
    n = len(arr)
    tree = [Basis() for _ in range(4 * n)]
    
    def build(node, start, end):
        if start == end:
            tree[node] = Basis()
            tree[node].insert(arr[start])
        else:
            mid = (start + end) // 2
            build(2 * node + 1, start, mid)
            build(2 * node + 2, mid + 1, end)
            
            # Merge logic: create new basis, merge children
            new_b = Basis()
            new_b.merge(tree[2 * node + 1])
            new_b.merge(tree[2 * node + 2])
            tree[node] = new_b

    def update(node, start, end, idx, val):
        if start == end:
            tree[node] = Basis()
            tree[node].insert(val)
        else:
            mid = (start + end) // 2
            if idx <= mid:
                update(2 * node + 1, start, mid, idx, val)
            else:
                update(2 * node + 2, mid + 1, end, idx, val)
                
            new_b = Basis()
            new_b.merge(tree[2 * node + 1])
            new_b.merge(tree[2 * node + 2])
            tree[node] = new_b

    def query(node, start, end, l, r):
        if l > end or r < start:
            return Basis()
        if l <= start and end <= r:
            return tree[node]
            
        mid = (start + end) // 2
        p1 = query(2 * node + 1, start, mid, l, r)
        p2 = query(2 * node + 2, mid + 1, end, l, r)
        
        res = Basis()
        res.merge(p1)
        res.merge(p2)
        return res

    build(0, 0, n - 1)
    results = []
    
    for op in ops:
        if op[0] == "SET":
            idx = int(op[1])
            val = int(op[2])
            update(0, 0, n - 1, idx, val)
        else:
            l = int(op[1])
            r = int(op[2])
            res = query(0, 0, n - 1, l, r)
            results.append(res.max_xor())
            
    return results

def main():
    import sys
    def input_gen():

        for line in sys.stdin:

            for token in line.split():

                yield token

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
        if (start == end) {
            tree[node].insert(arr[start]);
        } else {
            int mid = (start + end) / 2;
            build(arr, 2 * node + 1, start, mid);
            build(arr, 2 * node + 2, mid + 1, end);
            
            tree[node] = tree[2 * node + 1];
            tree[node].merge(tree[2 * node + 2]);
        }
    }

    void update(int node, int start, int end, int idx, int val) {
        if (start == end) {
            tree[node] = Basis();
            tree[node].insert(val);
        } else {
            int mid = (start + end) / 2;
            if (idx <= mid) update(2 * node + 1, start, mid, idx, val);
            else update(2 * node + 2, mid + 1, end, idx, val);
            
            tree[node] = tree[2 * node + 1];
            tree[node].merge(tree[2 * node + 2]);
        }
    }

    Basis query(int node, int start, int end, int l, int r) {
        if (l > end || r < start) return Basis();
        if (l <= start && end <= r) return tree[node];
        
        int mid = (start + end) / 2;
        Basis p1 = query(2 * node + 1, start, mid, l, r);
        Basis p2 = query(2 * node + 2, mid + 1, end, l, r);
        
        p1.merge(p2);
        return p1;
    }

public:
    vector<int> process(const vector<int>& arr, const vector<vector<string>>& ops) {
        n = arr.size();
        tree.assign(4 * n, Basis());
        
        build(arr, 0, 0, n - 1);
        
        vector<int> results;
        for (const auto& op : ops) {
            if (op[0] == "SET") {
                int idx = stoi(op[1]);
                int val = stoi(op[2]);
                update(0, 0, n - 1, idx, val);
            } else {
                int l = stoi(op[1]);
                int r = stoi(op[2]);
                Basis res = query(0, 0, n - 1, l, r);
                results.push_back(res.maxXor());
            }
        }
        return results;
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
    class Basis {
      constructor() {
        this.b = new Int32Array(30).fill(0);
      }
      
      insert(x) {
        for (let i = 29; i >= 0; i--) {
          if ((x >> i) & 1) {
            if (this.b[i] === 0) {
              this.b[i] = x;
              return;
            }
            x ^= this.b[i];
          }
        }
      }
      
      merge(other) {
        for (let i = 0; i < 30; i++) {
          if (other.b[i] !== 0) this.insert(other.b[i]);
        }
      }
      
      maxXor() {
        let res = 0;
        for (let i = 29; i >= 0; i--) {
          if ((res ^ this.b[i]) > res) res ^= this.b[i];
        }
        return res;
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

## 🧪 Test Case Walkthrough (Dry Run)
**Input:**
`3 1`
`1 2 3`
`MAXXOR 0 2`

1.  **Build**:
    -   Leaf `[0]`: Basis `{1}`.
    -   Leaf `[1]`: Basis `{2}`.
    -   Leaf `[2]`: Basis `{3}`.
    -   Root `[0, 2]`: Merge `{1}`, `{2}`, `{3}`.
        -   Insert 1: B=`{1}`.
        -   Insert 2: B=`{1, 2}`.
        -   Insert 3: `3 oplus 2 = 1`, `1 oplus 1 = 0`. 3 is linearly dependent. B remains `{1, 2}`.
2.  **Query**: `MAXXOR 0 2`.
    -   Returns basis `{1, 2}`.
    -   `maxXor`:
        -   Start 0.
        -   Bit 1 (val 2): `0 ^ 2 = 2 > 0`. Res=2.
        -   Bit 0 (val 1): `2 ^ 1 = 3 > 2`. Res=3.
3.  **Result**: 3.

## Proof of Correctness

-   **Linear Basis Property**: The basis of a union of sets is the merge of their bases.
-   **Segment Tree**: Correctly decomposes range into `O(log N)` canonical sub-ranges. Merging their bases gives the basis for the full range.

## Interview Extensions

1.  **Persistent Basis?**
    -   If we need to query past versions, use Persistent Segment Tree.
2.  **Greedy Basis Construction**:
    -   Standard algorithm is greedy (Gaussian elimination). It always finds *a* basis.
3.  **Basis Intersection**:
    -   Much harder. Intersection of vector spaces.

### Common Mistakes

-   **Basis Size**: 30 bits is enough for `10^9`. Don't use 64 unless needed.
-   **Merge Logic**: Don't just copy arrays. You must `insert` elements to maintain the triangular basis property.
