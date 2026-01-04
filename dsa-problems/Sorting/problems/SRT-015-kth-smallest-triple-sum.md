---
problem_id: SRT_KTH_SMALLEST_TRIPLE_SUM__7904
display_id: SRT-015
slug: kth-smallest-triple-sum
title: "Kth Smallest Triple Sum"
difficulty: Medium
difficulty_score: 59
topics:
  - Sorting
  - Binary Search
  - Two Pointers
tags:
  - sorting
  - binary-search
  - two-pointers
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# SRT-015: Kth Smallest Triple Sum

## Problem Statement

Given an array `a`, consider all sums `a[i] + a[j] + a[k]` with `i < j < k`. Find the k-th smallest such sum.

![Problem Illustration](../images/SRT-015/problem-illustration.png)

## Input Format

- First line: integers `n` and `k`
- Second line: `n` space-separated integers

## Output Format

- Single integer: the k-th smallest triple sum

## Constraints

- `3 <= n <= 100000`
- `1 <= k <= n*(n-1)*(n-2)/6`
- `-10^9 <= a[i] <= 10^9`

## Example

**Input:**

```
4 2
1 2 4 7
```

**Output:**

```
10
```

**Explanation:**

Triple sums are 7, 10, 12, 13 in sorted order; the 2nd is 10.

![Example Visualization](../images/SRT-015/example-1.png)

## Notes

- Sort the array first
- Use binary search on the possible sum range
- Count triples with sum <= mid using two pointers
- Time complexity: O(n^2 log R)

## Related Topics

Binary Search, Two Pointers, Sorting

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long findKthSmallestTripleSum(int n, long k, long[] a) {
        // Implement here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            long k = sc.nextLong();
            long[] a = new long[n];
            for (int i = 0; i < n; i++) a[i] = sc.nextLong();

            Solution sol = new Solution();
            System.out.println(sol.findKthSmallestTripleSum(n, k, a));
        }
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def find_kth_smallest_triple_sum(self, n: int, k: int, a: list) -> int:
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    k = int(input_data[1])
    a = [int(x) for x in input_data[2:]]

    sol = Solution()
    print(sol.find_kth_smallest_triple_sum(n, k, a))

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
    long long findKthSmallestTripleSum(int n, long long k, vector<long long>& a) {
        // Implement here
        return 0;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    long long k;
    if (cin >> n >> k) {
        vector<long long> a(n);
        for (int i = 0; i < n; i++) cin >> a[i];

        Solution sol;
        cout << sol.findKthSmallestTripleSum(n, k, a) << endl;
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  findKthSmallestTripleSum(n, k, a) {
    // Implement here
    return 0n;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false,
});

let input = [];
rl.on("line", (line) => {
  if (line.trim()) input.push(...line.trim().split(/\s+/));
}).on("close", () => {
  if (input.length < 2) return;
  const n = parseInt(input[0]);
  const k = BigInt(input[1]);
  const a = input.slice(2).map(BigInt);

  const sol = new Solution();
  console.log(sol.findKthSmallestTripleSum(n, k, a).toString());
});
```
