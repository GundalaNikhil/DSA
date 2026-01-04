---
problem_id: BIT_PAIRWISE_XOR_BAND_PARITY__8404
display_id: BIT-004
slug: pairwise-xor-band-index-parity
title: "Pairwise XOR in Band With Index Parity"
difficulty: Medium
difficulty_score: 55
topics:
  - Bitwise Operations
  - XOR
  - Trie
  - Array
tags:
  - bitwise
  - xor
  - trie
  - counting
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# BIT-004: Pairwise XOR in Band With Index Parity

## Problem Statement

Given an array and range `[L, U]`, count the number of index pairs `(i, j)` such that `i < j`, `i + j` is even, and the XOR sum `a[i] ^ a[j]` falls within `[L, U]`.

![Problem Illustration](../images/BIT-004/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers a[i]
- Third line: integers L and U

## Output Format

Print the number of valid pairs.

## Constraints

- `1 <= n <= 100000`
- `0 <= a[i] <= 1000000000`
- `0 <= L <= U <= 1000000000`

## Example

**Input:**

```
4
2 3 1 7
1 4
```

**Output:**

```
2
```

**Explanation:**

Valid pairs are (0,2): 2 XOR 1 = 3 and (1,3): 3 XOR 7 = 4. Both have i + j even.

![Example Visualization](../images/BIT-004/example-1.png)

## Notes

- Indices are 0-based.
- Only pairs with i + j even are counted.

## Related Topics

Bitwise Operations, XOR, Counting

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public long countPairsInBand(int n, int[] a, int l, int u) {
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

        int[] a = new int[n];
        String aLine = br.readLine();
        if (aLine != null) {
            String[] parts = aLine.trim().split("\\s+");
            for (int i = 0; i < n; i++) {
                a[i] = Integer.parseInt(parts[i]);
            }
        }

        String luLine = br.readLine();
        if (luLine == null) return;
        String[] luParts = luLine.trim().split("\\s+");
        int l = Integer.parseInt(luParts[0]);
        int u = Integer.parseInt(luParts[1]);

        Solution sol = new Solution();
        System.out.println(sol.countPairsInBand(n, a, l, u));
    }
}
```

### Python

```python
import sys

class Solution:
    def count_pairs_in_band(self, n, a, l, u):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    a = list(map(int, input_data[1:n+1]))
    l = int(input_data[n+1])
    u = int(input_data[n+2])

    sol = Solution()
    print(sol.count_pairs_in_band(n, a, l, u))

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
    long long countPairsInBand(int n, vector<int>& a, int l, int u) {
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

    int l, u;
    cin >> l >> u;

    Solution sol;
    cout << sol.countPairsInBand(n, a, l, u) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  countPairsInBand(n, a, l, u) {
    // Implement here
    return 0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 3) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const a = [];
  for (let i = 0; i < n; i++) {
    a.push(parseInt(input[idx++]));
  }
  const l = parseInt(input[idx++]);
  const u = parseInt(input[idx++]);

  const sol = new Solution();
  console.log(sol.countPairsInBand(n, a, l, u).toString());
}

solve();
```
