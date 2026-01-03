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
import java.io.*;
import java.util.*;

class Solution {
    public int detectPeriod(String s) {
        //Implemention here
        return 0;
    }
}

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        String line;
        while ((line = br.readLine()) != null) {
            sb.append(line).append(' ');
        }
        String input = sb.toString().trim();
        if (input.isEmpty()) return;
        String[] data = input.split("\\s+");
        int idx = 0;
        String s = data[idx++];
        Solution solution = new Solution();
        int result = solution.detectPeriod(s);
        System.out.print(result);
    }
}
```

### Python

```python
import sys

def detect_period(s):
    # //Implemention here
    return 0

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    s = data[idx]
    result = detect_period(s)
    sys.stdout.write(str(result))

if __name__ == '__main__':
    main()
```

### C++

```cpp
#include <iostream>
#include <string>

using namespace std;

int detect_period(const string& s) {
    //Implemention here
    return 0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;
    int result = detect_period(s);
    cout << result;
    return 0;
}
```

### JavaScript

```javascript
const fs = require("fs");

function detectPeriod(s) {
  //Implemention here
  return 0;
}

const input = fs.readFileSync(0, "utf8").trim();
if (input.length === 0) {
  process.exit(0);
}
const data = input.split(/\s+/);
let idx = 0;
const s = data[idx++];
const result = detectPeriod(s);
process.stdout.write(String(result));
```

