---
problem_id: BIT_DISTINCT_SUBARRAY_XORS__8412
display_id: BIT-012
slug: distinct-subarray-xors
title: "Distinct Subarray XORs"
difficulty: Medium
difficulty_score: 55
topics:
  - Bitwise Operations
  - XOR
  - Subarray
  - Trie
tags:
  - bitwise
  - xor
  - subarray
  - trie
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# BIT-012: Distinct Subarray XORs

## Problem Statement

Count the number of **distinct** values obtained by XORing elements of all possible subarrays of `a`.

![Problem Illustration](../images/BIT-012/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers a[i]

## Output Format

Print the number of distinct subarray XOR values.

## Constraints

- `1 <= n <= 10000`
- `0 <= a[i] <= 1000000000`

## Example

**Input:**

```
3
1 2 3
```

**Output:**

```
4
```

**Explanation:**

The distinct XORs across all subarrays are {0, 1, 2, 3}.

![Example Visualization](../images/BIT-012/example-1.png)

## Notes

- The total number of subarrays is n \* (n + 1) / 2.
- Use a set to track distinct XOR results.

## Related Topics

Bitwise Operations, Prefix XOR

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public int countDistinctSubarrayXors(int n, int[] a) {
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

        Solution sol = new Solution();
        System.out.println(sol.countDistinctSubarrayXors(n, a));
    }
}
```

### Python

```python
import sys

class Solution:
    def count_distinct_subarray_xors(self, n, a):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    a = list(map(int, input_data[1:n+1]))

    sol = Solution()
    print(sol.count_distinct_subarray_xors(n, a))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

class Solution {
public:
    int countDistinctSubarrayXors(int n, const vector<int>& a) {
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

    Solution sol;
    cout << sol.countDistinctSubarrayXors(n, a) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  countDistinctSubarrayXors(n, a) {
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
    a.push(parseInt(input[idx++]));
  }

  const sol = new Solution();
  console.log(sol.countDistinctSubarrayXors(n, a));
}

solve();
```
