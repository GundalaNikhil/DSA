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
import java.io.*;
import java.util.*;

class Solution {
    public int longestPalindromicPrefix(String s, char c) {
        //Implemention here
        return 0;
    }
}

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        List<String> lines = new ArrayList<>();
        String line;
        while ((line = br.readLine()) != null) {
            lines.add(line);
        }
        if (lines.size() < 2) return;
        String s = lines.get(0);
        String cLine = lines.get(1);
        if (cLine.isEmpty()) return;
        char c = cLine.charAt(0);

        Solution solution = new Solution();
        int result = solution.longestPalindromicPrefix(s, c);
        System.out.print(result);
    }
}
```

### Python

```python
import sys

def longest_palindromic_prefix(s, c):
    # //Implemention here
    return 0

def main():
    lines = sys.stdin.read().split('\n')
    if len(lines) < 2:
        return
    s = lines[0]
    c_line = lines[1]
    if c_line == '':
        return
    result = longest_palindromic_prefix(s, c_line[0])
    sys.stdout.write(str(result))

if __name__ == '__main__':
    main()
```

### C++

```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int longest_palindromic_prefix(const string& s, char c) {
    //Implemention here
    return 0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    vector<string> lines;
    string line;
    while (getline(cin, line)) {
        if (!line.empty() && line.back() == '\r') line.pop_back();
        lines.push_back(line);
    }
    if (lines.size() < 2) return 0;
    string s = lines[0];
    string cLine = lines[1];
    if (cLine.empty()) return 0;
    char c = cLine[0];

    int result = longest_palindromic_prefix(s, c);
    cout << result;
    return 0;
}
```

### JavaScript

```javascript
const fs = require("fs");

function longestPalindromicPrefix(s, c) {
  //Implemention here
  return 0;
}

const raw = fs.readFileSync(0, "utf8");
if (raw.length === 0) {
  process.exit(0);
}
const lines = raw.replace(/\r/g, "").split(/\n/);
if (lines.length < 2) {
  process.exit(0);
}
const s = lines[0];
const cLine = lines[1];
if (cLine.length === 0) {
  process.exit(0);
}
const result = longestPalindromicPrefix(s, cLine[0]);
process.stdout.write(String(result));
```

