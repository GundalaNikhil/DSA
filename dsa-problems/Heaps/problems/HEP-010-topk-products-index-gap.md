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

- (1,0): 7 \* 8 = 56
- (2,0): 5 \* 8 = 40
- (0,1): 9 \* 3 = 27

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
import java.io.*;

class Solution {
    public List<Long> getTopKProducts(int n, int m, int k, int d, long[] a, long[] b) {
        // Implement here
        return new ArrayList<>();
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String firstLine = br.readLine();
        if (firstLine == null) return;
        String[] parts = firstLine.trim().split("\\s+");
        int n = Integer.parseInt(parts[0]);
        int m = Integer.parseInt(parts[1]);
        int k = Integer.parseInt(parts[2]);
        int d = Integer.parseInt(parts[3]);

        long[] a = new long[n];
        String[] aVals = br.readLine().trim().split("\\s+");
        for (int i = 0; i < n; i++) a[i] = Long.parseLong(aVals[i]);

        long[] b = new long[m];
        String[] bVals = br.readLine().trim().split("\\s+");
        for (int i = 0; i < m; i++) b[i] = Long.parseLong(bVals[i]);

        Solution sol = new Solution();
        List<Long> result = sol.getTopKProducts(n, m, k, d, a, b);

        PrintWriter out = new PrintWriter(System.out);
        for (int i = 0; i < result.size(); i++) {
            out.print(result.get(i) + (i == result.size() - 1 ? "" : " "));
        }
        out.println();
        out.flush();
    }
}
```

### Python

```python
import sys

class Solution:
    def get_top_k_products(self, n, m, k, d, a, b):
        # Implement here
        return []

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    idx = 0
    n = int(input_data[idx++])
    m = int(input_data[idx++])
    k = int(input_data[idx++])
    d = int(input_data[idx++])

    a = list(map(int, input_data[idx:idx+n]))
    idx += n
    b = list(map(int, input_data[idx:idx+m]))

    sol = Solution()
    result = sol.get_top_k_products(n, m, k, d, a, b)
    print(*(result))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<long long> getTopKProducts(int n, int m, int k, int d, vector<long long>& a, vector<long long>& b) {
        // Implement here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m, k, d;
    if (!(cin >> n >> m >> k >> d)) return 0;

    vector<long long> a(n), b(m);
    for (int i = 0; i < n; i++) cin >> a[i];
    for (int i = 0; i < m; i++) cin >> b[i];

    Solution sol;
    vector<long long> result = sol.getTopKProducts(n, m, k, d, a, b);

    for (int i = 0; i < result.size(); i++) {
        cout << result[i] << (i == result.size() - 1 ? "" : " ");
    }
    cout << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  getTopKProducts(n, m, k, d, a, b) {
    // Implement here
    return [];
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 4) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const m = parseInt(input[idx++]);
  const k = parseInt(input[idx++]);
  const d = parseInt(input[idx++]);

  const a = [];
  for (let i = 0; i < n; i++) a.push(BigInt(input[idx++]));
  const b = [];
  for (let i = 0; i < m; i++) b.push(BigInt(input[idx++]));

  const sol = new Solution();
  const result = sol.getTopKProducts(n, m, k, d, a, b);
  console.log(result.join(" "));
}

solve();
```
