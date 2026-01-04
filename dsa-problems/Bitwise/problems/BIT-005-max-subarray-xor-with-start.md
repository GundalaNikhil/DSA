---
problem_id: BIT_MAX_SUBARRAY_XOR_START__8405
display_id: BIT-005
slug: max-subarray-xor-with-start
title: "Max Subarray XOR With Start"
difficulty: Medium
difficulty_score: 50
topics:
  - Bitwise Operations
  - XOR
  - Trie
  - Prefix Sum
tags:
  - bitwise
  - xor
  - trie
  - prefix-xor
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# BIT-005: Max Subarray XOR With Start

## Problem Statement

Given an array of integers and a fixed starting index `s`, find the subarray `a[s...k]` (where `k >= s`) that has the maximum XOR sum.

![Problem Illustration](../images/BIT-005/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers a[i]
- Third line: integer s (0-based)

## Output Format

Print the maximum XOR of a subarray starting at s.

## Constraints

- `1 <= n <= 200000`
- `0 <= a[i] <= 1000000000`

## Example

**Input:**

```
4
3 8 2 6
1
```

**Output:**

```
12
```

**Explanation:**

The subarray [8, 2, 6] has XOR 12, which is the maximum among subarrays starting at 1.

![Example Visualization](../images/BIT-005/example-1.png)

## Notes

- Index s is 0-based.
- The subarray must start at s but can end at any index >= s.

## Related Topics

Bitwise Operations, XOR, Trie

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public long maxSubarrayXorStartingAtS(int n, long[] a, int s) {
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
            String[] parts = aLine.trim().split("\\s+");
            for (int i = 0; i < n; i++) {
                a[i] = Long.parseLong(parts[i]);
            }
        }

        String sLine = br.readLine();
        if (sLine == null) return;
        int s = Integer.parseInt(sLine.trim());

        Solution sol = new Solution();
        System.out.println(sol.maxSubarrayXorStartingAtS(n, a, s));
    }
}
```

### Python

```python
import sys

class Solution:
    def max_subarray_xor_starting_at_s(self, n, a, s):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    a = list(map(int, input_data[1:n+1]))
    s = int(input_data[n+1])

    sol = Solution()
    print(sol.max_subarray_xor_starting_at_s(n, a, s))

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
    long long maxSubarrayXorStartingAtS(int n, vector<long long>& a, int s) {
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

    int s;
    cin >> s;

    Solution sol;
    cout << sol.maxSubarrayXorStartingAtS(n, a, s) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  maxSubarrayXorStartingAtS(n, a, s) {
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
    a.push(BigInt(input[idx++]));
  }
  const s = parseInt(input[idx++]);

  const sol = new Solution();
  console.log(sol.maxSubarrayXorStartingAtS(n, a, s).toString());
}

solve();
```
