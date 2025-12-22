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
    public List<Long> topKProducts(long[] A, long[] B, int k, int d) {
        // Your implementation here
        return new ArrayList<>();
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
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
            if (i + 1 < result.size()) System.out.print(" ");
        }
        System.out.println();
        sc.close();
    }
}
```

### Python

```python
from typing import List

def top_k_products(A: List[int], B: List[int], k: int, d: int) -> List[int]:
    # Your implementation here
    return []

def main():
    n, m, k, d = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    result = top_k_products(A, B, k, d)
    print(" ".join(str(x) for x in result))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<long long> topKProducts(const vector<long long>& A, const vector<long long>& B, int k, int d) {
        // Your implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, k, d;
    cin >> n >> m >> k >> d;
    vector<long long> A(n), B(m);
    for (int i = 0; i < n; i++) cin >> A[i];
    for (int i = 0; i < m; i++) cin >> B[i];

    Solution solution;
    vector<long long> result = solution.topKProducts(A, B, k, d);
    for (int i = 0; i < (int)result.size(); i++) {
        if (i) cout << " ";
        cout << result[i];
    }
    cout << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  topKProducts(A, B, k, d) {
    // Your implementation here
    return [];
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
  const n = parseInt(data[idx++], 10);
  const m = parseInt(data[idx++], 10);
  const k = parseInt(data[idx++], 10);
  const d = parseInt(data[idx++], 10);
  const A = [];
  const B = [];
  for (let i = 0; i < n; i++) A.push(parseInt(data[idx++], 10));
  for (let i = 0; i < m; i++) B.push(parseInt(data[idx++], 10));

  const solution = new Solution();
  const result = solution.topKProducts(A, B, k, d);
  console.log(result.join(" "));
});
```
