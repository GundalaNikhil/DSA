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

class Solution {
    public int longestPalindromicPrefix(String s, char c) {
        //Implement here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        try {
            byte[] bytes = System.in.readAllBytes();
            if (bytes.length == 0) return;
            String data = new String(bytes);
            String[] raw = data.split("\\n", -1);
            for (int i = 0; i < raw.length; i++) {
                if (raw[i].endsWith("\\r")) {
                    raw[i] = raw[i].substring(0, raw[i].length() - 1);
                }
            }
            String s;
            String cstr = "";
            if (raw.length == 1) {
                s = "";
                cstr = raw[0];
            } else {
                s = raw[0];
                for (int i = 1; i < raw.length; i++) {
                    if (!raw[i].isEmpty()) {
                        cstr = raw[i];
                        break;
                    }
                }
                if (cstr.isEmpty()) cstr = raw[1];
            }
            if (cstr.isEmpty()) return;
            char c = cstr.charAt(0);
            Solution solution = new Solution();
            System.out.println(solution.longestPalindromicPrefix(s, c));
        } catch (Exception e) {
            return;
        }
    }
}
```

### Python

```python
import sys

def longest_palindromic_prefix(s: str, c: str) -> int:
    # //Implement here
    return 0

def main():
    import sys
    lines = sys.stdin.read().strip().split('\n')
    if len(lines) < 1:
        return
    s = lines[0] if len(lines) > 0 else ''
    c = lines[1] if len(lines) > 1 else ''
    print(longest_palindromic_prefix(s, c))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    int longestPalindromicPrefix(string s, char c) {
        //Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string data((istreambuf_iterator<char>(cin)), istreambuf_iterator<char>());
    if (data.empty()) {
        return 0;
    }
    vector<string> lines;
    string cur;
    for (char ch : data) {
        if (ch == '\n') {
            lines.push_back(cur);
            cur.clear();
        } else if (ch != '\r') {
            cur.push_back(ch);
        }
    }
    lines.push_back(cur);

    string s;
    string cstr;
    if (lines.size() == 1) {
        s = "";
        cstr = lines[0];
    } else {
        s = lines[0];
        for (size_t i = 1; i < lines.size(); i++) {
            if (!lines[i].empty()) {
                cstr = lines[i];
                break;
            }
        }
        if (cstr.empty()) {
            cstr = lines[1];
        }
    }
    if (cstr.empty()) {
        return 0;
    }
    char c = cstr[0];
    Solution solution;
    cout << solution.longestPalindromicPrefix(s, c) << "\n";

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  longestPalindromicPrefix(s, c) {
    //Implement here
    return 0;
  }
}

const fs = require("fs");

const input = fs.readFileSync(0, "utf8");
if (input.length > 0) {
  const raw = input.split("\n").map((line) => line.replace(/\r$/, ""));
  let s = "";
  let cstr = "";
  if (raw.length === 1) {
    s = "";
    cstr = raw[0];
  } else {
    s = raw[0];
    for (let i = 1; i < raw.length; i++) {
      if (raw[i].length > 0) {
        cstr = raw[i];
        break;
      }
    }
    if (cstr.length === 0) cstr = raw[1];
  }
  if (cstr.length > 0) {
    const c = cstr[0];
    const solution = new Solution();
    console.log(solution.longestPalindromicPrefix(s, c));
  }
}
```

