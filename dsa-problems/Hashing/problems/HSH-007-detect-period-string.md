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

class Solution {
    private static final long MOD = 1_000_000_007L;
    private static final long BASE = 313L;
    
    public int detectPeriod(String s) {
        return 0;
    }
    
    private long getHash(long[] h, long[] p, int l, int r) {
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String s = sc.nextLine();
            Solution solution = new Solution();
            System.out.println(solution.detectPeriod(s));
        }
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def detect_period(self, s: str) -> int:
        return 0
def detect_period(s: str) -> int:
    return 0
def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    s = input_data[0]
    print(detect_period(s))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

class Solution {
    const long long MOD = 1e9 + 7;
    const long long BASE = 313;

public:
    int detectPeriod(string s) {
        return 0;
    }
    
    long long getHash(const vector<long long>& h, const vector<long long>& p, int l, int r) {
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    string s;
    if (getline(cin, s)) {
        Solution solution;
        cout << solution.detectPeriod(s) << "\n";
    }
    
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  detectPeriod(s) {
    return 0;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  if (data.length === 0) return;
  const s = data[0];

  const solution = new Solution();
  console.log(solution.detectPeriod(s));
});
```

