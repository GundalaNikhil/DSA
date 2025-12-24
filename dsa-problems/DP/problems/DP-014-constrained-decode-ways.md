---
problem_id: DP_CONSTRAINED_DECODE__3012
display_id: DP-014
slug: constrained-decode-ways
title: "Constrained Decode Ways"
difficulty: Medium
difficulty_score: 50
topics:
  - Dynamic Programming
  - Strings
  - Combinatorics
tags:
  - dp
  - decoding
  - strings
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP-014: Constrained Decode Ways

## Problem Statement

A digit string encodes letters `1 -> A`, `2 -> B`, ..., `26 -> Z`. You must count how many distinct decodings exist under an extra rule:

- Any digit `0` is valid **only** when immediately preceded by `2`, forming the two-digit code `20`. No other placement of `0` is allowed.

Return the number of valid decodings modulo `1_000_000_007`.

![Problem Illustration](../images/DP-014/problem-illustration.png)

## Input Format

- Single line: a digit string `s` (no spaces).

## Output Format

- Single integer: number of valid decodings modulo `1_000_000_007`.

## Constraints

- `1 <= |s| <= 100000`
- `s` consists of digits `0-9`
- Leading zeros invalidate the string

## Example

**Input:**
```
2012
```

**Output:**
```
2
```

**Explanation:**

Two decodings satisfy the rule:

- `20 1 2`
- `20 12`

![Example Visualization](../images/DP-014/example-1.png)

## Notes

- The pair `10` is **invalid** because `0` must follow an even digit forming `20` only.
- Standalone `0` makes the entire string invalid.
- Use modulo arithmetic throughout to avoid overflow.

## Related Topics

Dynamic Programming, Strings, Combinatorics

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    static final long MOD = 1_000_000_007L;

    public long decodeWays(String s) {
        int n = s.length();
        if (n == 0 || s.charAt(0) == '0') return 0;
        long prev2 = 1; // dp[i-2]
        long prev1 = 1; // dp[i-1]
        for (int i = 1; i < n; i++) {
            char c = s.charAt(i);
            int pair = (s.charAt(i - 1) - '0') * 10 + (c - '0');
            long cur = 0;
            if (c != '0') {
                cur = (cur + prev1) % MOD; // single digit
                if ((pair == 20) || (pair > 10 && pair <= 26)) {
                    cur = (cur + prev2) % MOD; // valid pair
                }
            } else { // c == '0'
                if (pair == 20) cur = (cur + prev2) % MOD;
            }
            prev2 = prev1;
            prev1 = cur;
        }
        return prev1 % MOD;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNext()) return;
        String s = sc.next();
        Solution sol = new Solution();
        System.out.println(sol.decodeWays(s));
        sc.close();
    }
}
```

### Python

```python
MOD = 1_000_000_007

def decode_ways(s: str) -> int:
    n = len(s)
    if n == 0 or s[0] == "0":
        return 0
    prev2, prev1 = 1, 1  # dp[i-2], dp[i-1]
    for i in range(1, n):
        c = s[i]
        pair = int(s[i-1:i+1])
        cur = 0
        if c != "0":
            cur = (cur + prev1) % MOD
            if (pair == 20) or (10 < pair <= 26):
                cur = (cur + prev2) % MOD
        else:
            if pair == 20:
                cur = (cur + prev2) % MOD
        prev2, prev1 = prev1, cur
    return prev1 % MOD

def main() -> None:
    import sys
    data = sys.stdin.read().strip()
    if not data:
        return
    print(decode_ways(data.split()[0]))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <bits/stdc++.h>
using namespace std;
const long long MOD = 1'000'000'007LL;

long long decodeWays(const string& s) {
    int n = s.size();
    if (n == 0 || s[0] == '0') return 0;
    long long prev2 = 1, prev1 = 1;
    for (int i = 1; i < n; ++i) {
        int pair = (s[i - 1] - '0') * 10 + (s[i] - '0');
        long long cur = 0;
        if (s[i] != '0') {
            cur = (cur + prev1) % MOD;
            if (pair == 20 || (pair > 10 && pair <= 26)) cur = (cur + prev2) % MOD;
        } else {
            if (pair == 20) cur = (cur + prev2) % MOD;
        }
        prev2 = prev1;
        prev1 = cur;
    }
    return prev1 % MOD;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string s;
    if (!(cin >> s)) return 0;
    cout << decodeWays(s) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const MOD = 1_000_000_007n;
const fs = require("fs");

function decodeWays(s) {
  if (s.length === 0 || s[0] === "0") return 0;
  let prev2 = 1n, prev1 = 1n;
  for (let i = 1; i < s.length; i++) {
    const pair = Number(s[i - 1]) * 10 + Number(s[i]);
    let cur = 0n;
    if (s[i] !== "0") {
      cur = (cur + prev1) % MOD;
      if (pair === 20 || (pair > 10 && pair <= 26)) cur = (cur + prev2) % MOD;
    } else {
      if (pair === 20) cur = (cur + prev2) % MOD;
    }
    prev2 = prev1;
    prev1 = cur;
  }
  return Number(prev1 % MOD);
}

function main() {
  const data = fs.readFileSync(0, "utf8").trim();
  if (!data) return;
  console.log(decodeWays(data.split(/\\s+/)[0]));
}

main();
```
