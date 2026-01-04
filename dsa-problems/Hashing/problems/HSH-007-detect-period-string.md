---
problem_id: HSH_DETECT_PERIOD_STRING__6183
display_id: HSH-007
slug: detect-period-string
title: "Detect Period of String"
difficulty: Medium
difficulty_score: 50
topics:
  - Hashing
  - String Algorithms
  - Periodicity
tags:
  - hashing
  - period
  - pattern
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HSH-007: Detect Period of String

## Problem Statement

Determine the smallest period `p` of string `s`. The period is the smallest positive integer `p` such that `s` can be represented as the repetition of a substring of length `p`.

If no such period exists (i.e., the string cannot be formed by repeating a substring), return the length of the string.

![Problem Illustration](../images/HSH-007/problem-illustration.png)

## Input Format

- Single line: string `s`

## Output Format

- Single integer: smallest period of the string

## Constraints

- `1 <= |s| <= 2*10^5`
- String contains only lowercase English letters

## Example

**Input:**

```
ababab
```

**Output:**

```
2
```

**Explanation:**

String: "ababab"

The string can be formed by repeating "ab" (length 2) three times.
Periods to check:

- Period 1: "a" repeated → "aaaaaa" ≠ "ababab"
- Period 2: "ab" repeated → "ababab" ✓

Smallest period: 2

![Example Visualization](../images/HSH-007/example-1.png)

## Notes

- Check divisors of string length as potential periods
- Use hashing to verify if s equals concatenation of s[0..p-1] repeated
- Time complexity: O(n log n)
- Space complexity: O(n)

## Related Topics

String Period, Pattern Matching, Hashing, KMP Failure Function

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public int findSmallestPeriod(String s) {
        // Implement here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        if (s == null) return;

        Solution sol = new Solution();
        System.out.println(sol.findSmallestPeriod(s.trim()));
    }
}
```

### Python

```python
import sys

class Solution:
    def find_smallest_period(self, s):
        # Implement here
        return 0

def solve():
    s = sys.stdin.read().strip()
    if not s:
        return

    sol = Solution()
    print(sol.find_smallest_period(s))

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
    int findSmallestPeriod(string s) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    string s;
    if (!(cin >> s)) return 0;

    Solution sol;
    cout << sol.findSmallestPeriod(s) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  findSmallestPeriod(s) {
    // Implement here
    return 0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").trim();
  if (!input) return;

  const sol = new Solution();
  console.log(sol.findSmallestPeriod(input));
}

solve();
```
