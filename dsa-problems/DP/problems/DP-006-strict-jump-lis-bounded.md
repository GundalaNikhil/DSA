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

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767513328/dsa/dp/e7iapogzin4mggqfz0w1.jpg)

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

### Python

### C++

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public int longestSubsequence(int n, long[] a, long d, long g) {
        // Implement here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String nLine = br.readLine();
        if (nLine == null) return;
        int n = Integer.parseInt(nLine.trim());

        long[] a = new long[n];
        String aLine = br.readLine();
        if (aLine != null) {
            String[] aParts = aLine.trim().split("\\s+");
            for (int i = 0; i < n; i++) {
                a[i] = Long.parseLong(aParts[i]);
            }
        }

        String dgLine = br.readLine();
        if (dgLine == null) return;
        String[] dgParts = dgLine.trim().split("\\s+");
        long d = Long.parseLong(dgParts[0]);
        long g = Long.parseLong(dgParts[1]);

        Solution sol = new Solution();
        System.out.println(sol.longestSubsequence(n, a, d, g));
    }
}
```

### Python

```python
import sys

class Solution:
    def longest_subsequence(self, n, a, d, g):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    a = list(map(int, input_data[1:1+n]))
    d = int(input_data[1+n])
    g = int(input_data[2+n])

    sol = Solution()
    print(sol.longest_subsequence(n, a, d, g))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int longestSubsequence(int n, const vector<long long>& a, long long d, long long g) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    long long d, g;
    cin >> d >> g;

    Solution sol;
    cout << sol.longestSubsequence(n, a, d, g) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  longestSubsequence(n, a, d, g) {
    // Implement here
    return 0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 1) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const a = [];
  for (let i = 0; i < n; i++) {
    a.push(BigInt(input[idx++]));
  }
  const d = BigInt(input[idx++]);
  const g = BigInt(input[idx++]);

  const sol = new Solution();
  console.log(sol.longestSubsequence(n, a, d, g));
}

solve();
```
