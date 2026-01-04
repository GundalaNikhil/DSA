---
problem_id: HSH_TWO_STRING_CONCAT_EQUAL__4156
display_id: HSH-010
slug: two-string-concat-equal
title: "Two-String Concatenation Equal Check"
difficulty: Medium
difficulty_score: 45
topics:
  - Hashing
  - String Algorithms
tags:
  - hashing
  - concatenation
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HSH-010: Two-String Concatenation Equal Check

## Problem Statement

Given four strings `a`, `b`, `c`, `d`, determine if `a + b == c + d` (concatenation) without explicitly creating the concatenated strings, using polynomial hashing.

![Problem Illustration](../images/HSH-010/problem-illustration.png)

## Input Format

- Four lines, each containing a string: `a`, `b`, `c`, `d`

## Output Format

- Single word: `true` or `false`

## Constraints

- `1 <= |a|, |b|, |c|, |d| <= 10^5`
- Strings contain only lowercase English letters

## Example

**Input:**

```
ab
cd
a
bcd
```

**Output:**

```
true
```

**Explanation:**

a + b = "ab" + "cd" = "abcd"
c + d = "a" + "bcd" = "abcd"

They are equal, so output is true.

![Example Visualization](../images/HSH-010/example-1.png)

## Notes

- Compute hash(a+b) as hash(a) \* B^|b| + hash(b)
- Compute hash(c+d) as hash(c) \* B^|d| + hash(d)
- Compare the two hashes
- Time complexity: O(|a| + |b| + |c| + |d|)
- Space complexity: O(1)

## Related Topics

Hashing, String Concatenation, Polynomial Hash

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public boolean isConcatEqual(String a, String b, String c, String d) {
        // Implement here
        return false;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String a = br.readLine();
        String b = br.readLine();
        String c = br.readLine();
        String d = br.readLine();
        if (a == null || b == null || c == null || d == null) return;

        Solution sol = new Solution();
        System.out.println(sol.isConcatEqual(a.trim(), b.trim(), c.trim(), d.trim()));
    }
}
```

### Python

```python
import sys

class Solution:
    def is_concat_equal(self, a, b, c, d):
        # Implement here
        return False

def solve():
    input_data = sys.stdin.read().splitlines()
    if len(input_data) < 4:
        return

    a = input_data[0].strip()
    b = input_data[1].strip()
    c = input_data[2].strip()
    d = input_data[3].strip()

    sol = Solution()
    print("true" if sol.is_concat_equal(a, b, c, d) else "false")

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
    bool isConcatEqual(string a, string b, string c, string d) {
        // Implement here
        return false;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    string a, b, c, d;
    if (!(cin >> a >> b >> c >> d)) return 0;

    Solution sol;
    cout << (sol.isConcatEqual(a, b, c, d) ? "true" : "false") << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  isConcatEqual(a, b, c, d) {
    // Implement here
    return false;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\r?\n/);
  if (input.length < 4) return;

  const a = input[0].trim();
  const b = input[1].trim();
  const c = input[2].trim();
  const d = input[3].trim();

  const sol = new Solution();
  console.log(sol.isConcatEqual(a, b, c, d));
}

solve();
```
