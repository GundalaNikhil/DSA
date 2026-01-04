---
problem_id: HSH_COUNT_PAIRS_EQUAL_DOUBLE_HASH__9418
display_id: HSH-015
slug: count-pairs-equal-double-hash
title: "Count Pairs with Equal Hash Mod Two Mods"
difficulty: Medium
difficulty_score: 50
topics:
  - Hashing
  - Combinatorics
  - String Algorithms
tags:
  - hashing
  - double-hash
  - pairs
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HSH-015: Count Pairs with Equal Hash Mod Two Mods

## Problem Statement

Given a string `s` and length `L`, count the number of pairs of substrings of length `L` that have equal hash values under two different moduli (assume collisions are negligible with double hashing).

Return the count of such pairs.

![Problem Illustration](../images/HSH-015/problem-illustration.png)

## Input Format

- First line: string `s`
- Second line: integer `L`

## Output Format

- Single integer: number of pairs with equal double hash

## Constraints

- `1 <= |s| <= 10^5`
- `1 <= L <= |s|`
- String contains only lowercase English letters

## Example

**Input:**

```
aaaa
2
```

**Output:**

```
3
```

**Explanation:**

String: "aaaa"
Length L: 2

All substrings of length 2:

- s[0..1] = "aa"
- s[1..2] = "aa"
- s[2..3] = "aa"

All three substrings are identical, so pairs with equal hash:

- (0,1), (0,2), (1,2)

Total: 3 pairs

![Example Visualization](../images/HSH-015/example-1.png)

## Notes

- Compute double hash (using two different moduli) for all substrings of length L
- Group substrings by their hash pair (hash1, hash2)
- For each group of size n, count C(n, 2) = n\*(n-1)/2 pairs
- Time complexity: O(n)
- Space complexity: O(n)

## Related Topics

Hashing, Double Hashing, Combinatorics, Substring Matching

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public long countEqualHashPairs(String s, int l) {
        // Implement here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        String lLine = br.readLine();
        if (s == null || lLine == null) return;
        int l = Integer.parseInt(lLine.trim());

        Solution sol = new Solution();
        System.out.println(sol.countEqualHashPairs(s.trim(), l));
    }
}
```

### Python

```python
import sys

class Solution:
    def count_equal_hash_pairs(self, s, l):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().splitlines()
    if len(input_data) < 2:
        return

    s = input_data[0].strip()
    l = int(input_data[1].strip())

    sol = Solution()
    print(sol.count_equal_hash_pairs(s, l))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    long long countEqualHashPairs(string s, int l) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    string s;
    int l;
    if (!(cin >> s >> l)) return 0;

    Solution sol;
    cout << sol.countEqualHashPairs(s, l) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  countEqualHashPairs(s, l) {
    // Implement here
    return 0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\r?\n/);
  if (input.length < 2) return;

  const s = input[0].trim();
  const l = parseInt(input[1].trim());

  const sol = new Solution();
  console.log(sol.countEqualHashPairs(s, l));
}

solve();
```
