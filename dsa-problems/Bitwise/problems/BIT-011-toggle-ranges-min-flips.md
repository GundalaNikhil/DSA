---
problem_id: BIT_TOGGLE_RANGES_MIN_FLIPS__8411
display_id: BIT-011
slug: toggle-ranges-min-flips
title: "Toggle Ranges Minimum Flips"
difficulty: Medium
difficulty_score: 45
topics:
  - Bitwise Operations
  - Array
  - Greedy
  - Flipping
tags:
  - bitwise
  - array-transformation
  - greedy
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# BIT-011: Toggle Ranges Minimum Flips

## Problem Statement

You may flip all bits in any chosen subarray (0 -> 1, 1 -> 0). Find the minimum number of flips required to convert binary array A into binary array B.

![Problem Illustration](../images/BIT-011/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated bits of A
- Third line: n space-separated bits of B

## Output Format

Print the minimum number of flips.

## Constraints

- `1 <= n <= 200000`

## Example

**Input:**

```
4
0 1 1 0
1 0 1 1
```

**Output:**

```
2
```

**Explanation:**

Mismatch segments are indices 0..1 and 3, so two flips are sufficient.

![Example Visualization](../images/BIT-011/example-1.png)

## Notes

- A flip inverts every bit in the chosen subarray.
- Count contiguous mismatch runs to minimize flips.

## Related Topics

Bitwise Operations, Greedy

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public int minFlipsToConvert(int n, int[] a, int[] b) {
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
        for (int i = 0; i < n; i++) a[i] = sc.nextInt();

        int[] b = new int[n];
        for (int i = 0; i < n; i++) b[i] = sc.nextInt();

        Solution sol = new Solution();
        System.out.println(sol.minFlipsToConvert(n, a, b));
    }
}
```

### Python

```python
import sys

class Solution:
    def min_flips_to_convert(self, n, a, b):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    a = list(map(int, input_data[1:n+1]))
    b = list(map(int, input_data[n+1:2*n+1]))

    sol = Solution()
    print(sol.min_flips_to_convert(n, a, b))

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
    int minFlipsToConvert(int n, const vector<int>& a, const vector<int>& b) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n), b(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    for (int i = 0; i < n; i++) cin >> b[i];

    Solution sol;
    cout << sol.minFlipsToConvert(n, a, b) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  minFlipsToConvert(n, a, b) {
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
  for (let i = 0; i < n; i++) a.push(parseInt(input[idx++]));

  const b = [];
  for (let i = 0; i < n; i++) b.push(parseInt(input[idx++]));

  const sol = new Solution();
  console.log(sol.minFlipsToConvert(n, a, b));
}

solve();
```
