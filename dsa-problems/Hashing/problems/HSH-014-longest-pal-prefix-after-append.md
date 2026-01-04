---
problem_id: HSH_LONGEST_PAL_PREFIX_AFTER_APPEND__3764
display_id: HSH-014
slug: longest-pal-prefix-after-append
title: "Longest Palindromic Prefix After One Append"
difficulty: Medium
difficulty_score: 55
topics:
  - Hashing
  - Palindrome
  - String Algorithms
tags:
  - hashing
  - palindrome
  - prefix
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HSH-014: Longest Palindromic Prefix After One Append

## Problem Statement

Given a string `s` and a character `c`, append `c` to the end of `s` to create a new string. Find the length of the longest prefix of this new string that is also a palindrome.

![Problem Illustration](../images/HSH-014/problem-illustration.png)

## Input Format

- First line: string `s`
- Second line: character `c`

## Output Format

- Single integer: length of longest palindromic prefix after appending `c`

## Constraints

- `1 <= |s| <= 10^5`
- String `s` and character `c` are lowercase English letters

## Example

**Input:**

```
abac
a
```

**Output:**

```
3
```

**Explanation:**

Original string: "abac"
After appending 'a': "abaca"

Palindromic prefixes:

- "a" (length 1)
- "aba" (length 3) ← longest

Output: 3

![Example Visualization](../images/HSH-014/example-1.png)

## Notes

- Compute forward and reverse hashes for the new string
- Check each prefix length from longest to shortest
- Use hashing to verify if prefix is palindrome
- Time complexity: O(n)
- Space complexity: O(n)

## Related Topics

Palindrome, Hashing, Prefix, String Algorithms

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public int longestPalindromicPrefixAfterAppend(String s, char c) {
        // Implement here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        String cLine = br.readLine();
        if (s == null || cLine == null) return;
        char c = cLine.trim().charAt(0);

        Solution sol = new Solution();
        System.out.println(sol.longestPalindromicPrefixAfterAppend(s.trim(), c));
    }
}
```

### Python

```python
import sys

class Solution:
    def longest_palindromic_prefix_after_append(self, s, c):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().splitlines()
    if len(input_data) < 2:
        return

    s = input_data[0].strip()
    c = input_data[1].strip()[0]

    sol = Solution()
    print(sol.longest_palindromic_prefix_after_append(s, c))

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
    int longestPalindromicPrefixAfterAppend(string s, char c) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    string s;
    char c;
    if (!(cin >> s >> c)) return 0;

    Solution sol;
    cout << sol.longestPalindromicPrefixAfterAppend(s, c) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  longestPalindromicPrefixAfterAppend(s, c) {
    // Implement here
    return 0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\r?\n/);
  if (input.length < 2) return;

  const s = input[0].trim();
  const c = input[1].trim()[0];

  const sol = new Solution();
  console.log(sol.longestPalindromicPrefixAfterAppend(s, c));
}

solve();
```
