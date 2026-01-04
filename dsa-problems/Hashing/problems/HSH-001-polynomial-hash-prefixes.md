---
problem_id: HSH_POLYNOMIAL_HASH_PREFIXES__3824
display_id: HSH-001
slug: polynomial-hash-prefixes
title: "Polynomial Hash of Prefixes"
difficulty: Easy
difficulty_score: 25
topics:
  - Hashing
  - Rolling Hash
  - String Algorithms
tags:
  - hashing
  - rolling-hash
  - polynomial-hash
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HSH-001: Polynomial Hash of Prefixes

## Problem Statement

Given a lowercase string `s`, compute the polynomial rolling hash for all prefixes using base `B` and modulus `M`.

The polynomial hash for a string is computed as:

- `hash("") = 0`
- `hash(s[0..i]) = (hash(s[0..i-1]) * B + s[i]) mod M`

where `s[i]` is treated as its ASCII value.

Return an array containing the hash values for all prefixes: `hash(s[0..0]), hash(s[0..1]), ..., hash(s[0..n-1])`.

![Problem Illustration](../images/HSH-001/problem-illustration.png)

## Input Format

- First line: string `s` (lowercase letters only)
- Second line: two integers `B M` (base and modulus)

## Output Format

- Single line with `n` space-separated integers representing hash values of all prefixes

## Constraints

- `1 <= |s| <= 2*10^5`
- `1 <= B <= 10^9 + 6`
- `1 <= M <= 10^9 + 7`
- String contains only lowercase English letters

## Example

**Input:**

```
abc
911382323 1000000007
```

**Output:**

```
97 374134515 549818522
```

**Explanation:**

String: "abc"

- Prefix "a": hash = 97 (ASCII of 'a')
- Prefix "ab": hash = (97 * 911382323 + 98) mod 1000000007 = 374134515
- Prefix "abc": hash = (374134515 * 911382323 + 99) mod 1000000007 = 549818522

![Example Visualization](../images/HSH-001/example-1.png)

## Notes

- Use modular arithmetic to prevent integer overflow
- Hash values depend on both the base and modulus chosen
- This technique is fundamental for string matching and comparison
- Time complexity: O(n)
- Space complexity: O(n) for storing results

## Related Topics

Polynomial Hash, Rolling Hash, String Hashing, Rabin-Karp

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public long[] computePrefixHashes(String s, long b, long m) {
        // Implement here
        return new long[0];
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        if (s == null) return;
        String line2 = br.readLine();
        if (line2 == null) return;
        String[] parts = line2.trim().split("\\s+");
        long b = Long.parseLong(parts[0]);
        long m = Long.parseLong(parts[1]);

        Solution sol = new Solution();
        long[] result = sol.computePrefixHashes(s, b, m);

        PrintWriter out = new PrintWriter(System.out);
        for (int i = 0; i < result.length; i++) {
            out.print(result[i] + (i == result.length - 1 ? "" : " "));
        }
        out.println();
        out.flush();
    }
}
```

### Python

```python
import sys

class Solution:
    def compute_prefix_hashes(self, s, b, m):
        # Implement here
        return []

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    s = input_data[0]
    b = int(input_data[1])
    m = int(input_data[2])

    sol = Solution()
    result = sol.compute_prefix_hashes(s, b, m)
    print(*(result))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<long long> computePrefixHashes(string s, long long b, long long m) {
        // Implement here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    string s;
    long long b, m;
    if (!(cin >> s >> b >> m)) return 0;

    Solution sol;
    vector<long long> result = sol.computePrefixHashes(s, b, m);

    for (int i = 0; i < result.size(); i++) {
        cout << result[i] << (i == result.size() - 1 ? "" : " ");
    }
    cout << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  computePrefixHashes(s, b, m) {
    // Implement here
    return [];
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 3) return;

  const s = input[0];
  const b = BigInt(input[1]);
  const m = BigInt(input[2]);

  const sol = new Solution();
  const result = sol.computePrefixHashes(s, b, m);
  console.log(result.join(" "));
}

solve();
```
