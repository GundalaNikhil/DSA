---
problem_id: DP_LIS_DIFF_RANGE__5881
display_id: DP-006
slug: strict-jump-lis-bounded
title: "Strict Jump LIS With Max Gap"
difficulty: Medium
difficulty_score: 64
topics:
  - Dynamic Programming
  - Segment Tree
  - Coordinate Compression
tags:
  - dp
  - lis
  - segment-tree
  - fenwick
  - medium
premium: true
subscription_tier: basic
time_limit: 3000
memory_limit: 256
---

# DP-006: Strict Jump LIS With Max Gap

## Problem Statement

You are given an integer array `a` of length `n` and two integers `d` and `g` (`d <= g`).

Find the length of the longest subsequence `a[i1], a[i2], ..., a[ik]` (with `i1 < i2 < ... < ik`) such that for every consecutive pair:

`d <= a[i(t+1)] - a[i(t)] <= g`

Return the maximum possible length `k`.

![Problem Illustration](../images/DP-006/problem-illustration.png)

## Input Format

- First line: integer `n`
- Second line: `n` space-separated integers `a[i]`
- Third line: two integers `d` and `g`

## Output Format

Print one integer: the length of the longest valid subsequence.

## Constraints

- `1 <= n <= 100000`
- `-10^9 <= a[i] <= 10^9`
- `0 <= d <= g <= 10^9`

## Example

**Input:**
```
5
1 3 4 9 10
2 6
```

**Output:**
```
3
```

**Explanation:**

One optimal subsequence is `1 -> 3 -> 9`:

- `3 - 1 = 2` (within [2,6])
- `9 - 3 = 6` (within [2,6])

So the answer is 3.

![Example Visualization](../images/DP-006/example-1.png)

## Notes

- This is a LIS-style problem, but the constraint is on the **difference range** `[d, g]`, not simply “increasing”.
- If `d = 0`, equal consecutive values are allowed (difference 0).
- `O(n^2)` DP will not pass for `n = 10^5`. You need a range-maximum data structure.

## Related Topics

Dynamic Programming, Coordinate Compression, Segment Tree / Fenwick Tree

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    static class SegTree {
        int n;
        int[] t;
        SegTree(int n) {
            this.n = n;
            this.t = new int[4 * n];
        }
        void update(int idx, int val) { update(1, 0, n - 1, idx, val); }
        private void update(int node, int l, int r, int idx, int val) {
            if (l == r) { t[node] = Math.max(t[node], val); return; }
            int mid = (l + r) >>> 1;
            if (idx <= mid) update(node << 1, l, mid, idx, val);
            else update(node << 1 | 1, mid + 1, r, idx, val);
            t[node] = Math.max(t[node << 1], t[node << 1 | 1]);
        }
        int query(int ql, int qr) {
            if (ql > qr) return 0;
            return query(1, 0, n - 1, ql, qr);
        }
        private int query(int node, int l, int r, int ql, int qr) {
            if (qr < l || r < ql) return 0;
            if (ql <= l && r <= qr) return t[node];
            int mid = (l + r) >>> 1;
            return Math.max(query(node << 1, l, mid, ql, qr), query(node << 1 | 1, mid + 1, r, ql, qr));
        }
    }

    private static int lowerBound(long[] a, long x) {
        int l = 0, r = a.length;
        while (l < r) {
            int m = (l + r) >>> 1;
            if (a[m] >= x) r = m;
            else l = m + 1;
        }
        return l;
    }

    private static int upperBound(long[] a, long x) {
        int l = 0, r = a.length;
        while (l < r) {
            int m = (l + r) >>> 1;
            if (a[m] <= x) l = m + 1;
            else r = m;
        }
        return l;
    }

    public int longestBoundedDiffSubsequence(int[] arr, long d, long g) {
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = sc.nextInt();
        long d = sc.nextLong();
        long g = sc.nextLong();
        System.out.println(new Solution().longestBoundedDiffSubsequence(a, d, g));
        sc.close();
    }
}
```

### Python

```python
from bisect import bisect_left, bisect_right

class FenwickMax:
    def __init__(self, n: int):
        return 0
    def update(self, i: int, val: int) -> None:
        pass
    def query_prefix(self, i: int) -> int:
        return 0
def longest_bounded_diff_subsequence(a: list[int], d: int, g: int) -> int:
    return 0
def main():
    n = int(input())
    a = list(map(int, input().split()))
    d, g = map(int, input().split())
    print(longest_bounded_diff_subsequence(a, d, g))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <sstream>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <numeric>
#include <limits>
#include <cmath>
#include <cstring>
#include <utility>
using namespace std;

struct SegTree {
    int n;
    vector<int> t;
    SegTree(int n): n(n), t(4*n, 0) {}
    void update(int idx, int val) { update(1, 0, n-1, idx, val); }
    void update(int node, int l, int r, int idx, int val) {
        if (l==r) { t[node]=max(t[node], val); return; }
        int mid=(l+r)/2;
        if (idx<=mid) update(node*2, l, mid, idx, val);
        else update(node*2+1, mid+1, r, idx, val);
        t[node]=max(t[node*2], t[node*2+1]);
    }
    int query(int ql, int qr) {
        if (ql>qr) return 0;
        return query(1, 0, n-1, ql, qr);
    }
    int query(int node, int l, int r, int ql, int qr) {
        if (qr<l || r<ql) return 0;
        if (ql<=l && r<=qr) return t[node];
        int mid=(l+r)/2;
        return max(query(node*2, l, mid, ql, qr), query(node*2+1, mid+1, r, ql, qr));
    }
};

class Solution {
public:
    int longestBoundedDiffSubsequence(const vector<long long>& a, long long d, long long g) {
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<long long> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    long long d, g;
    cin >> d >> g;

    Solution sol;
    cout << sol.longestBoundedDiffSubsequence(a, d, g) << '\n';
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class SegTree {
  constructor(n) {
    this.n = n;
    this.t = new Array(4 * n).fill(0);
  }
  update(idx, val, node = 1, l = 0, r = this.n - 1) {
    if (l === r) {
      if (val > this.t[node]) this.t[node] = val;
      return;
    }
    const mid = (l + r) >> 1;
    if (idx <= mid) this.update(idx, val, node << 1, l, mid);
    else this.update(idx, val, node << 1 | 1, mid + 1, r);
    const left = this.t[node << 1], right = this.t[node << 1 | 1];
    this.t[node] = left > right ? left : right;
  }
  query(ql, qr, node = 1, l = 0, r = this.n - 1) {
    if (ql > qr) return 0;
    if (qr < l || r < ql) return 0;
    if (ql <= l && r <= qr) return this.t[node];
    const mid = (l + r) >> 1;
    const a = this.query(ql, qr, node << 1, l, mid);
    const b = this.query(ql, qr, node << 1 | 1, mid + 1, r);
    return a > b ? a : b;
  }
}

function lowerBound(arr, x) {
  let l = 0, r = arr.length;
  while (l < r) {
    const m = (l + r) >> 1;
    if (arr[m] >= x) r = m;
    else l = m + 1;
  }
  return l;
}

function upperBound(arr, x) {
  let l = 0, r = arr.length;
  while (l < r) {
    const m = (l + r) >> 1;
    if (arr[m] <= x) l = m + 1;
    else r = m;
  }
  return l;
}

class Solution {
  longestBoundedDiffSubsequence(a, d, g) {
    return 0;
  }
}

const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
const lines = [];
rl.on("line", (line) => lines.push(line.trim()));
rl.on("close", () => {
  let idx = 0;
  const n = Number(lines[idx++]);
  const a = lines[idx++].split(" ").map(Number);
  const [d, g] = lines[idx++].split(" ").map(Number);
  const sol = new Solution();
  console.log(sol.longestBoundedDiffSubsequence(a, d, g));
});
```

