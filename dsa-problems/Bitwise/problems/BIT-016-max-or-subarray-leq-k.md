---
problem_id: BIT_MAX_OR_SUBARRAY_LEQ_K__8416
display_id: BIT-016
slug: max-or-subarray-leq-k
title: "Max Bitwise OR Subarray <= K"
difficulty: Medium
difficulty_score: 50
topics:
  - Bitwise Operations
  - OR
  - Sliding Window
  - Array
tags:
  - bitwise
  - or-operation
  - sliding-window
  - subarray
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# BIT-016: Max Bitwise OR Subarray <= K

## Problem Statement

Find the length of the longest subarray `nums[i..j]` such that `nums[i] | nums[i+1] | ... | nums[j] <= K`.

![Problem Illustration](../images/BIT-016/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers a[i]
- Third line: integer K

## Output Format

Print the maximum length of a subarray with OR <= K.

## Constraints

- `1 <= n <= 200000`
- `0 <= a[i], K <= 1000000000`

## Example

**Input:**

```
4
1 2 4 1
7
```

**Output:**

```
4
```

**Explanation:**

The OR of the entire array is 7, so the maximum length is 4.

![Example Visualization](../images/BIT-016/example-1.png)

## Notes

- Use a sliding window with bit counts.
- All elements and K are non-negative.

## Related Topics

Bitwise Operations, Sliding Window

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public int maxSubarrayLengthOrLeqK(int n, int[] a, int k) {
        // Implement here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();

        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }

        int k = sc.nextInt();

        Solution sol = new Solution();
        System.out.println(sol.maxSubarrayLengthOrLeqK(n, a, k));
    }
}
```

### Python

```python
import sys

class Solution:
    def max_subarray_length_or_leq_k(self, n, a, k):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    a = list(map(int, input_data[1:n+1]))
    if len(input_data) > n+1:
        k = int(input_data[n+1])
    else:
        k = 0 # Should ideally be provided

    sol = Solution()
    print(sol.max_subarray_length_or_leq_k(n, a, k))

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
    int maxSubarrayLengthOrLeqK(int n, const vector<int>& a, int k) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    int k;
    cin >> k;

    Solution sol;
    cout << sol.maxSubarrayLengthOrLeqK(n, a, k) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  maxSubarrayLengthOrLeqK(n, a, k) {
    // Implement here
    return 0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const a = [];
  for (let i = 0; i < n; i++) {
    a.push(parseInt(input[idx++]));
  }
  const k = parseInt(input[idx++]);

  const sol = new Solution();
  console.log(sol.maxSubarrayLengthOrLeqK(n, a, k));
}

solve();
```
