---
problem_id: BIT_PALINDROMES_BALANCED_ONES__8414
display_id: BIT-014
slug: bitwise-palindromes-balanced-ones
title: "Bitwise Palindromes With Balanced Ones"
difficulty: Medium
difficulty_score: 62
topics:
  - Bitwise Operations
  - Palindrome
  - Bit Counting
  - Number Theory
tags:
  - bitwise
  - palindrome
  - popcount
  - number-generation
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# BIT-014: Bitwise Palindromes With Balanced Ones

## Problem Statement

Count numbers in [L, R] whose binary representation is a palindrome and whose number of 1 bits is even.

![Problem Illustration](../images/BIT-014/problem-illustration.png)

## Input Format

- Single line: integers L R

## Output Format

Print the count of valid numbers in [L, R].

## Constraints

- `0 <= L <= R <= 1000000000000`

## Example

**Input:**

```
5 12
```

**Output:**

```
2
```

**Explanation:**

5 (101) and 9 (1001) are palindromes with an even number of 1 bits.

![Example Visualization](../images/BIT-014/example-1.png)

## Notes

- Leading zeros are not allowed in the binary representation.
- Use 64-bit arithmetic for the count.

## Related Topics

Bitwise Operations, Combinatorics

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public long countValidPalindromes(long l, long r) {
        // Implement here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextLong()) return;
        long l = sc.nextLong();
        long r = sc.nextLong();

        Solution sol = new Solution();
        System.out.println(sol.countValidPalindromes(l, r));
    }
}
```

### Python

```python
import sys

class Solution:
    def count_valid_palindromes(self, l, r):
        # Implement here
        return 0

def solve():
    line = sys.stdin.readline().split()
    if not line:
        return
    l, r = map(int, line)

    sol = Solution()
    print(sol.count_valid_palindromes(l, r))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>

using namespace std;

class Solution {
public:
    long long countValidPalindromes(long long l, long long r) {
        // Implement here
        return 0;
    }
};

int main() {
    long long l, r;
    if (!(cin >> l >> r)) return 0;

    Solution sol;
    cout << sol.countValidPalindromes(l, r) << endl;
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  countValidPalindromes(l, r) {
    // Implement here
    return BigInt(0);
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").trim().split(/\s+/);
  if (input.length < 2) return;

  const l = BigInt(input[0]);
  const r = BigInt(input[1]);

  const sol = new Solution();
  console.log(sol.countValidPalindromes(l, r).toString());
}

solve();
```
