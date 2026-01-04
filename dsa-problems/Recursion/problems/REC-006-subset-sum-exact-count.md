---
problem_id: REC_SUBSET_SUM_EXACT_COUNT__1854
display_id: REC-006
slug: subset-sum-exact-count
title: "Subset Sum Exact Count"
difficulty: Medium
difficulty_score: 43
topics:
  - Recursion
  - Backtracking
  - Subset Sum
tags:
  - recursion
  - subset-sum
  - backtracking
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# REC-006: Subset Sum Exact Count

## Problem Statement

Given an array `arr`, determine whether there exists a subset of exactly `k` elements that sums to `target`. Return one such subset if it exists, otherwise output `NONE`.

![Problem Illustration](../images/REC-006/problem-illustration.png)

## Input Format

- First line: integers `n`, `k`, and `target`
- Second line: `n` space-separated integers `arr[i]`

## Output Format

- One line with a valid subset (space-separated), or `NONE` if no solution exists

## Constraints

- `1 <= n <= 20`
- `0 <= k <= n`
- `|arr[i]| <= 10000`
- `|target| <= 10^9`

## Example

**Input:**

```
4 2 7
4 1 6 2
```

**Output:**

```
1 6
```

**Explanation:**

The subset `{1, 6}` uses exactly two elements and sums to 7.

![Example Visualization](../images/REC-006/example-1.png)

## Notes

- Use recursion to choose or skip each element
- Track how many elements have been chosen
- Prune when remaining elements are insufficient to reach `k`
- Any valid subset is acceptable

## Related Topics

Backtracking, Subset Sum, Pruning

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public void findSubset(int n, int k, long target, long[] arr) {
        // Implement here
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int k = sc.nextInt();
        long target = sc.nextLong();
        long[] arr = new long[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextLong();
        Solution sol = new Solution();
        sol.findSubset(n, k, target, arr);
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def find_subset(self, n, k, target, arr):
        # Implement here
        pass

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    k = int(input_data[1])
    target = int(input_data[2])
    arr = [int(x) for x in input_data[3:3+n]]
    sol = Solution()
    sol.find_subset(n, k, target, arr)

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
    void findSubset(int n, int k, long long target, vector<long long>& arr) {
        // Implement here
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, k;
    long long target;
    if (!(cin >> n >> k >> target)) return 0;
    vector<long long> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    Solution sol;
    sol.findSubset(n, k, target, arr);
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require('fs');

class Solution {
  findSubset(n, k, target, arr) {
    // Implement here
  }
}

function solve() {
  const input = fs.readFileSync(0, 'utf8').split(/\s+/);
  if (input.length < 3) return;
  const n = parseInt(input[0]);
  const k = parseInt(input[1]);
  const target = BigInt(input[2]);
  const arr = [];
  for (int i = 0; i < n; i++) {
    arr.push(BigInt(input[3 + i]));
  }
  const sol = new Solution();
  sol.findSubset(n, k, target, arr);
}

solve();
```
