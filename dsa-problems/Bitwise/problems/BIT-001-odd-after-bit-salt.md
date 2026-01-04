---
problem_id: BIT_XOR_ODD_OCCURRENCE__8401
display_id: BIT-001
slug: odd-after-bit-salt
title: "Odd After Bit Salt"
difficulty: Easy
difficulty_score: 30
topics:
  - Bitwise Operations
  - XOR
  - Array
  - Mathematics
tags:
  - bitwise
  - xor
  - array
  - mathematics
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# BIT-001: Odd After Bit Salt

## Problem Statement

Each array element x is transformed to x XOR salt, where salt is the same for all elements. In the transformed multiset, exactly one value appears an odd number of times and all others appear an even number of times.
Find that odd-occurring value without explicitly building the transformed array.

![Problem Illustration](../images/BIT-001/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers a[i]
- Third line: integer salt

## Output Format

Print the transformed value that appears an odd number of times.

## Constraints

- `1 <= n <= 200000`
- `-1000000000 <= a[i] <= 1000000000`
- `-1000000000 <= salt <= 1000000000`

## Example

**Input:**

```
7
4 1 2 1 2 4 7
3
```

**Output:**

```
4
```

**Explanation:**

XOR all values with salt and use XOR aggregation; the odd-occurring transformed
value is 4.

![Example Visualization](../images/BIT-001/example-1.png)

## Notes

- XOR is associative and cancels even counts.
- You do not need to materialize the transformed array.

## Related Topics

Bitwise Operations, XOR, Arrays

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public long findOddOccurring(int n, long[] a, long salt) {
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

        String saltLine = br.readLine();
        if (saltLine == null) return;
        long salt = Long.parseLong(saltLine.trim());

        Solution sol = new Solution();
        System.out.println(sol.findOddOccurring(n, a, salt));
    }
}
```

### Python

```python
import sys

class Solution:
    def find_odd_occurring(self, n, a, salt):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    a = list(map(int, input_data[1:n+1]))
    salt = int(input_data[n+1])

    sol = Solution()
    print(sol.find_odd_occurring(n, a, salt))

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
    long long findOddOccurring(int n, vector<long long>& a, long long salt) {
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

    long long salt;
    cin >> salt;

    Solution sol;
    cout << sol.findOddOccurring(n, a, salt) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  findOddOccurring(n, a, salt) {
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
  const salt = BigInt(input[idx++]);

  const sol = new Solution();
  console.log(sol.findOddOccurring(n, a, salt).toString());
}

solve();
```
