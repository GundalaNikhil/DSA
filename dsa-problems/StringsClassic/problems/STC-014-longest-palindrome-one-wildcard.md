---
problem_id: STC_LONGEST_PAL_ONE_WILDCARD__7405
display_id: STC-014
slug: longest-palindrome-one-wildcard
title: "Longest Palindromic Substring With One Wildcard"
difficulty: Medium
difficulty_score: 55
topics:
  - Strings
  - Palindromes
  - Two Pointers
tags:
  - strings
  - palindromes
  - wildcard
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# STC-014: Longest Palindromic Substring With One Wildcard

## Problem Statement

You are given a string `s` of lowercase letters and at most one wildcard character `?`. The wildcard can be replaced by any single lowercase letter.

Find the longest substring of `s` that can become a palindrome after choosing a replacement for `?` (if it lies inside the substring). If multiple substrings have the same maximum length, return the one with the smallest starting index.

![Problem Illustration](../images/STC-014/problem-illustration.png)

## Input Format

- First line: string `s`

## Output Format

- Single line: the chosen substring from `s` (with `?` unchanged)

## Constraints

- `1 <= |s| <= 200000`
- `s` contains lowercase English letters and at most one `?`

## Example

**Input:**

```
ab?ba
```

**Output:**

```
ab?ba
```

**Explanation:**

The entire string can be a palindrome by replacing `?` with `c`, so the longest substring is the full string.

![Example Visualization](../images/STC-014/example-1.png)

## Notes

- If the string has no `?`, this is the standard longest palindromic substring problem.
- When a `?` is inside the substring, it can match any opposing character.
- Use center expansion or a modified Manacher algorithm to stay within O(n).
- Return the leftmost answer on ties.

## Related Topics

Palindromes, Manacher, Two Pointers

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int longestWildcardPalindrome(String s) {
        //Implement here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String s = sc.next();
            Solution solution = new Solution();
            System.out.println(solution.longestWildcardPalindrome(s));
        }
        sc.close();
    }
}
```

### Python

```python
def longest_wildcard_palindrome(s: str) -> int:
    # //Implement here
    return 0

def main():
    import sys
    sys.setrecursionlimit(200000)
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    s = input_data[0]
    print(longest_wildcard_palindrome(s))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int longestWildcardPalindrome(const string& s) {
        //Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (cin >> s) {
        Solution solution;
        cout << solution.longestWildcardPalindrome(s) << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  longestWildcardPalindrome(s) {
    //Implement here
    return 0;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => {
  const parts = line.trim().split(/\s+/);
  for (const part of parts) {
    if (part) data.push(part);
  }
});

rl.on("close", () => {
  if (data.length === 0) return;
  const s = data[0];
  const solution = new Solution();
  console.log(solution.longestWildcardPalindrome(s));
});
```

