---
problem_id: SEG_K_SMALLEST_PREFIX_UPDATES__9461
display_id: SEG-014
slug: k-smallest-prefix-updates
title: "K Smallest Prefix Updates"
difficulty: Medium
difficulty_score: 50
topics:
  - Segment Tree
  - Range Assignment
  - Prefix Updates
tags:
  - segment-tree
  - assignment
  - prefix
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# SEG-014: K Smallest Prefix Updates

## Problem Statement

Maintain an array `a` under prefix assignment updates. The operations are:

- `SETPREFIX k x`: set `a[0..k-1] = x`
- `SUM l r`: output the sum of `a[l..r]`

![Problem Illustration](../images/SEG-014/problem-illustration.png)

## Input Format

- First line: integers `n` and `q`
- Second line: `n` space-separated integers
- Next `q` lines: `SETPREFIX` or `SUM`

## Output Format

- For each `SUM`, print the range sum

## Constraints

- `1 <= n, q <= 200000`
- `-10^9 <= a[i], x <= 10^9`
- `1 <= k <= n`

## Example

**Input:**

```
3 2
1 2 3
SETPREFIX 2 5
SUM 0 2
```

**Output:**

```
13
```

**Explanation:**

After the prefix assignment, the array is `[5, 5, 3]`, so the sum is 13.

![Example Visualization](../images/SEG-014/example-1.png)

## Notes

- This is a range assignment on a prefix
- Use a segment tree with lazy assignment tags
- Each operation is O(log n)
- Sums may require 64-bit integers

## Related Topics

Segment Tree, Range Assignment, Prefix Updates

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    static class Node {
        long sum;
        long lazySet;
        boolean hasLazy;
        
        Node() {
            lazySet = 0;
            hasLazy = false;
        }
    }
    
    private Node[] tree;
    private int n;

    public List<Long> process(long[] arr, List<String[]> ops) {
        return null;
    }

    private void push(int node, int start, int end) {
        if (tree[node].hasLazy) {
            int mid = (start + end) / 2;
            long val = tree[node].lazySet;
            
            tree[2 * node + 1].lazySet = val;
            tree[2 * node + 1].hasLazy = true;
            tree[2 * node + 1].sum = val * (mid - start + 1);
            
            tree[2 * node + 2].lazySet = val;
            tree[2 * node + 2].hasLazy = true;
            tree[2 * node + 2].sum = val * (end - mid);
            
            tree[node].hasLazy = false;
        }
    }

    private void build(long[] arr, int node, int start, int end) {
        if (start == end) {
            tree[node].sum = arr[start];
        } else {
            int mid = (start + end) / 2;
            build(arr, 2 * node + 1, start, mid);
            build(arr, 2 * node + 2, mid + 1, end);
            tree[node].sum = tree[2 * node + 1].sum + tree[2 * node + 2].sum;
        }
    }

    private void update(int node, int start, int end, int l, int r, long val) {
        if (l > end || r < start) return;
        if (l <= start && end <= r) {
            tree[node].lazySet = val;
            tree[node].hasLazy = true;
            tree[node].sum = val * (end - start + 1);
            return;
        }
        
        push(node, start, end);
        int mid = (start + end) / 2;
        update(2 * node + 1, start, mid, l, r, val);
        update(2 * node + 2, mid + 1, end, l, r, val);
        tree[node].sum = tree[2 * node + 1].sum + tree[2 * node + 2].sum;
    }

    private long query(int node, int start, int end, int l, int r) {
        if (l > end || r < start) return 0;
        if (l <= start && end <= r) return tree[node].sum;
        
        push(node, start, end);
        int mid = (start + end) / 2;
        return query(2 * node + 1, start, mid, l, r) + 
               query(2 * node + 2, mid + 1, end, l, r);
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int q = sc.nextInt();
            long[] arr = new long[n];
            for (int i = 0; i < n; i++) arr[i] = sc.nextLong();
            List<String[]> ops = new ArrayList<>();
            for (int i = 0; i < q; i++) {
                String type = sc.next();
                ops.add(new String[]{type, sc.next(), sc.next()});
            }
            Solution sol = new Solution();
            List<Long> results = sol.process(arr, ops);
            for (long res : results) {
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

# Increase recursion depth just in case
sys.setrecursionlimit(200000)

class Solution:
    def process(self, arr: list[int], ops: list[list[str]]) -> list[int]:
        return []
def main():
    import sys
    sys.setrecursionlimit(300000)
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
    
    sol = Solution()
    results = sol.process(arr, ops)
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <vector>
#include <string>
#include <iostream>

using namespace std;

struct Node {
    long long sum;
    long long lazySet;
    bool hasLazy;
};

class Solution {
    vector<Node> tree;
    int n;

    void push(int node, int start, int end) {
    }

    void build(const vector<long long>& arr, int node, int start, int end) {
    }

    void update(int node, int start, int end, int l, int r, long long val) {
    }

    long long query(int node, int start, int end, int l, int r) {
        if (l > end || r < start) return 0;
        if (l <= start && end <= r) return tree[node].sum;
        
        push(node, start, end);
        int mid = (start + end) / 2;
        return query(2 * node + 1, start, mid, l, r) + 
               query(2 * node + 2, mid + 1, end, l, r);
    }

public:
    vector<long long> process(const vector<long long>& arr, const vector<vector<string>>& ops) {
        n = arr.size();
        tree.assign(4 * n, {0, 0, false});
        
        build(arr, 0, 0, n - 1);
        
        vector<long long> results;
        for (const auto& op : ops) {
            if (op[0] == "SETPREFIX") {
                int k = stoi(op[1]);
                long long x = stoll(op[2]);
                if (k > 0) update(0, 0, n - 1, 0, k - 1, x);
            } else {
                int l = stoi(op[1]);
                int r = stoi(op[2]);
                results.push_back(query(0, 0, n - 1, l, r));
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
    vector<long long> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    vector<vector<string>> ops(q);
    for (int i = 0; i < q; i++) {
        string type, a, b;
        cin >> type >> a >> b;
        ops[i] = {type, a, b};
    }
    Solution sol;
    vector<long long> results = sol.process(arr, ops);
    for (long long res : results) {
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
    const type = data[idx++];
    ops.push([type, data[idx++], data[idx++]]);
  }
  const solution = new Solution();
  const out = solution.process(arr, ops);
  console.log(out.join("\n"));
});
```

