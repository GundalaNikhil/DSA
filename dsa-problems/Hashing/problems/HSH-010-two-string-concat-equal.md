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

class Solution {
    private static final long MOD = 1_000_000_007L;
    private static final long BASE = 313L;

    public boolean checkConcatenationEqual(String a, String b, String c, String d) {
        return false;
    }

    private long computeHash(String s) {
        long h = 0;
        for (char ch : s.toCharArray()) {
            h = (h * BASE + ch) % MOD;
        }
        return h;
    }

    private long combine(long h1, long h2, int len2) {
        long p = 1;
        long b = BASE;
        // Modular exponentiation for B^len2
        int exp = len2;
        while (exp > 0) {
            if ((exp & 1) == 1) p = (p * b) % MOD;
            b = (b * b) % MOD;
            exp >>= 1;
        }

        return (h1 * p + h2) % MOD;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String a = sc.nextLine();
            String b = sc.nextLine();
            String c = sc.nextLine();
            String d = sc.nextLine();

            Solution solution = new Solution();
            System.out.println(solution.checkConcatenationEqual(a, b, c, d));
        }
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def check_concatenation_equal(self, a: str, b: str, c: str, d: str) -> bool:
        return False
def check_concatenation_equal(a: str, b: str, c: str, d: str) -> bool:
    return False
def main():
    import sys
    lines = sys.stdin.read().strip().split('\n')
    if len(lines) < 4:
        # Pad with empty strings if needed
        while len(lines) < 4:
            lines.append('')
    a = lines[0] if len(lines) > 0 else ''
    b = lines[1] if len(lines) > 1 else ''
    c = lines[2] if len(lines) > 2 else ''
    d = lines[3] if len(lines) > 3 else ''
    result = check_concatenation_equal(a, b, c, d)
    print("true" if result else "false")

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <string>

using namespace std;

class Solution {
    const long long MOD = 1e9 + 7;
    const long long BASE = 313;

public:
    bool checkConcatenationEqual(string a, string b, string c, string d) {
        return false;
    }

    long long computeHash(const string& s) {
        long long h = 0;
        for (char ch : s) {
            h = (h * BASE + ch) % MOD;
        }
        return h;
    }

    long long combine(long long h1, long long h2, int len2) {
        long long p = 1;
        long long b = BASE;
        int exp = len2;
        while (exp > 0) {
            if (exp & 1) p = (p * b) % MOD;
            b = (b * b) % MOD;
            exp >>= 1;
        }
        return (h1 * p + h2) % MOD;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string a, b, c, d;
    if (getline(cin, a) && getline(cin, b) && getline(cin, c) && getline(cin, d)) {
        Solution solution;
        cout << (solution.checkConcatenationEqual(a, b, c, d) ? "true" : "false") << "\n";
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  checkConcatenationEqual(a, b, c, d) {
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
  if (data.length < 4) return;
  const [a, b, c, d] = data;

  const solution = new Solution();
  console.log(solution.checkConcatenationEqual(a, b, c, d) ? "true" : "false");
});
```

