---
problem_id: BIT_SUBSET_AND_EQUALS_X__8410
display_id: BIT-010
slug: subset-and-equals-x
title: "Subset AND Equals X"
difficulty: Medium
difficulty_score: 52
topics:
  - Bitwise Operations
  - AND
  - Subset
  - Dynamic Programming
tags:
  - bitwise
  - and-operation
  - subset
  - dp
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# BIT-010: Subset AND Equals X

## Problem Statement

Given an array of integers and a target `X`, count the number of non-empty subsets such that the bitwise AND of the subset elements is exactly `X`.

![Problem Illustration](../images/BIT-010/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers a[i]
- Third line: integer X

## Output Format

Print the number of non-empty subsets with AND equal to X.

## Constraints

- `1 <= n <= 20`
- `0 <= a[i], X <= 1000000`

## Example

**Input:**

```
3
6 4 2
2
```

**Output:**

```
2
```

**Explanation:**

The subsets [6, 2] and [2] have AND equal to 2.

![Example Visualization](../images/BIT-010/example-1.png)

## Notes

- The empty subset does not count.
- Use 64-bit integers for the count.

## Related Topics

Bitwise Operations, DP, Subsets

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public long countSubsetsWithAndX(int n, int[] a, int x) {
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

        int x = sc.nextInt();

        Solution sol = new Solution();
        System.out.println(sol.countSubsetsWithAndX(n, a, x));
    }
}
```

### Python

```python
import sys

class Solution:
    def count_subsets_with_and_x(self, n, a, x):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    a = list(map(int, input_data[1:n+1]))
    x = int(input_data[n+1])

    sol = Solution()
    print(sol.count_subsets_with_and_x(n, a, x))

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
    long long countSubsetsWithAndX(int n, const vector<int>& a, int x) {
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

    int x;
    cin >> x;

    Solution sol;
    cout << sol.countSubsetsWithAndX(n, a, x) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  countSubsetsWithAndX(n, a, x) {
    // Implement here
    return BigInt(0);
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
  const x = parseInt(input[idx++]);

  const sol = new Solution();
  console.log(sol.countSubsetsWithAndX(n, a, x).toString());
}

solve();
```
