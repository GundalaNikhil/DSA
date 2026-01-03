problem_id: HSH_LCS_HASH_TWO_STRINGS__7482
display_id: HSH-003
slug: lcs-hash-two-strings
title: "Longest Common Substring of Two Strings"
difficulty: Medium
difficulty_score: 50
topics:

- Hashing
- Binary Search
- String Algorithms
  tags:
- hashing
- binary-search
- lcs
- medium
  premium: true
  subscription_tier: basic
  time_limit: 2000
  memory_limit: 256

---

# HSH-003: Longest Common Substring of Two Strings

## Problem Statement

Given two strings `a` and `b`, find the length of their longest common substring using binary search combined with polynomial hashing.

A common substring is a contiguous sequence of characters that appears in both strings.

![Problem Illustration](../images/HSH-003/problem-illustration.png)

## Input Format

- First line: string `a`
- Second line: string `b`

## Output Format

- Single integer: length of the longest common substring

## Constraints

- `1 <= |a|, |b| <= 10^5`
- Strings contain only lowercase English letters

## Example

**Input:**

```
abcde
cdef
```

**Output:**

```
3
```

**Explanation:**

String a: "abcde"
String b: "cdef"

Common substrings:

- "c" (length 1)
- "cd" (length 2)
- "cde" (length 3) ← longest

Output: 3

![Example Visualization](../images/HSH-003/example-1.png)

## Notes

- Use binary search on the answer (length of substring)
- For each candidate length, use hashing to check if any substring of that length appears in both strings
- Store hashes of all substrings of length L from string a in a set
- Check if any substring of length L from string b matches
- Time complexity: O((|a| + |b|) \* log(min(|a|, |b|)))
- Space complexity: O(min(|a|, |b|))

## Related Topics

Binary Search, Hashing, Rolling Hash, Longest Common Substring

---

## Solution Template

### Java

```java
import java.io.*;
import java.util.*;

class Solution {
    public int longestCommonSubstring(String a, String b) {
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
        String a = lines.get(0);
        String b = lines.get(1);

        Solution solution = new Solution();
        int result = solution.longestCommonSubstring(a, b);
        System.out.print(result);
    }
}
```

### Python

```python
import sys

def longest_common_substring(a, b):
    # //Implemention here
    return 0

def main():
    lines = sys.stdin.read().split('\n')
    if len(lines) < 2:
        return
    a = lines[0]
    b = lines[1]
    result = longest_common_substring(a, b)
    sys.stdout.write(str(result))

if __name__ == '__main__':
    main()
```

### C++

```cpp
#include <iostream>
#include <string>

using namespace std;

int longest_common_substring(const string& a, const string& b) {
    //Implemention here
    return 0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string a, b;
    if (!getline(cin, a)) return 0;
    if (!getline(cin, b)) return 0;
    if (!a.empty() && a.back() == '\r') a.pop_back();
    if (!b.empty() && b.back() == '\r') b.pop_back();

    int result = longest_common_substring(a, b);
    cout << result;
    return 0;
}
```

### JavaScript

```javascript
const fs = require("fs");

function longestCommonSubstring(a, b) {
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
const a = lines[0];
const b = lines[1];
const result = longestCommonSubstring(a, b);
process.stdout.write(String(result));
```

