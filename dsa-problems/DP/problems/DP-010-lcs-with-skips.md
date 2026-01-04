---
problem_id: DP_LCS_SKIP_BUDGET__2297
display_id: DP-010
slug: lcs-with-skips
title: "LCS With Limited Skips in A"
difficulty: Medium
difficulty_score: 55
topics:
  - Dynamic Programming
  - Strings
  - Subsequence
tags:
  - dp
  - lcs
  - strings
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP-010: LCS With Limited Skips in A

## Problem Statement

You are given two lowercase strings `a` and `b`, and an integer `s`.

You may **delete** (skip) characters from `a`, but you are allowed to delete **at most `s` characters from `a`** in total. You can delete any number of characters from `b` (unlimited), as in a standard subsequence match.

Find the maximum length of a common subsequence you can obtain under this constraint. If no common subsequence satisfies the skip limit (i.e., every common subsequence would require more than `s` deletions from `a`), print `-1`.

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767513331/dsa/dp/wbiz0f0ylk8uta5ou5fo.jpg)

## Input Format

- First line: string `a`
- Second line: string `b`
- Third line: integer `s`

## Output Format

Print a single integer: the maximum feasible common subsequence length, or `-1` if none fits within the skip budget.

## Constraints

- `0 <= |a|, |b| <= 2000`
- `0 <= s <= |a|`
- Strings consist of lowercase English letters `a..z`

## Example

**Input:**

```
abcde
ace
2
```

**Output:**

```
3
```

**Explanation:**

- LCS is `"ace"` (length 3), which requires deleting `b` and `d` from `a` ⇒ 2 deletions
- Skip limit `s = 2` allows this, so answer is 3.

**If `s = 1` for the same strings, the best feasible length would be `-1`** because every common subsequence needs at least 2 deletions from `a`.

![Example Visualization](../images/DP-010/example-1.png)

## Notes

- Deleting characters from `b` is unrestricted (as in normal subsequence checking).
- The skip budget applies only to deletions from `a`.
- Returning `-1` indicates that even the maximum common subsequence exceeds the allowed deletions.

## Related Topics

Dynamic Programming, LCS, Strings, Subsequences

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public int maxLCSWithSkips(String a, String b, int s) {
        // Implement here
        return -1;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String a = br.readLine();
        String b = br.readLine();
        String sLine = br.readLine();
        if (a == null || b == null || sLine == null) return;
        int s = Integer.parseInt(sLine.trim());

        Solution sol = new Solution();
        System.out.println(sol.maxLCSWithSkips(a, b, s));
    }
}
```

### Python

```python
import sys

# Standard LCS DP might reach recursion depth for 2000,
# though iterative DP is preferred.
sys.setrecursionlimit(5000)

class Solution:
    def max_lcs_with_skips(self, a, b, s):
        # Implement here
        return -1

def solve():
    a = sys.stdin.readline().strip()
    b = sys.stdin.readline().strip()
    s_line = sys.stdin.readline().strip()
    if not s_line:
        return
    s = int(s_line)

    sol = Solution()
    print(sol.max_lcs_with_skips(a, b, s))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maxLCSWithSkips(string a, string b, int s) {
        // Implement here
        return -1;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    string a, b;
    int s;
    if (!(getline(cin, a))) return 0;
    if (!(getline(cin, b))) return 0;
    if (!(cin >> s)) return 0;

    // Trim potential \r
    if (!a.empty() && a.back() == '\r') a.pop_back();
    if (!b.empty() && b.back() == '\r') b.pop_back();

    Solution sol;
    cout << sol.maxLCSWithSkips(a, b, s) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  maxLCSWithSkips(a, b, s) {
    // Implement here
    return -1;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\r?\n/);
  const a = input[0] || "";
  const b = input[1] || "";
  const s = parseInt(input[2]);

  if (isNaN(s)) return;

  const sol = new Solution();
  console.log(sol.maxLCSWithSkips(a, b, s));
}

solve();
```
