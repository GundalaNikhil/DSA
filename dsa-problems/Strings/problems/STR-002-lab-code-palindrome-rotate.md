---
problem_id: STR_LAB_CODE_PALINDROME_ROTATE__1002
display_id: STR-002
slug: lab-code-palindrome-rotate
title: "Lab Code Palindrome Rotate"
difficulty: Easy
difficulty_score: 28
topics:
  - String Manipulation
  - Palindromes
  - Frequency Analysis
tags:
  - string-processing
  - rotation
  - palindrome-check
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# STR-002: Lab Code Palindrome Rotate

## Problem Statement

You are given a string `s` consisting of lowercase letters. Determine if any rotation of the string can form a palindrome.

A rotation of a string is obtained by moving characters from the beginning to the end. For example, rotations of "abc" are "abc", "bca", and "cab".

A palindrome is a string that reads the same forwards and backwards.

## Input Format

- A single string `s` (1 ≤ |s| ≤ 2 × 10^5)

## Output Format

- `true` if any rotation can form a palindrome, `false` otherwise

## Constraints

- `1 ≤ |s| ≤ 2 × 10^5`
- `s` contains only lowercase English letters

## Example 1

**Input:**

```
aab
```

**Output:**

```
true
```

**Explanation:**

- Rotation "aba" is a palindrome

## Example 2

**Input:**

```
abc
```

**Output:**

```
false
```

**Explanation:**

- No rotation of "abc" can form a palindrome
- All rotations: "abc", "bca", "cab" - none are palindromes

## Notes

- Use frequency analysis: a string can form a palindrome if at most one character has an odd count
- This applies to any rotation since character frequencies don't change
- O(n) time complexity using frequency counting

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public boolean canRotateToPalindrome(String s) {
        // Implement here
        return false;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String s = sc.next();
            Solution sol = new Solution();
            System.out.println(sol.canRotateToPalindrome(s));
        }
        sc.close();
    }
}
```

### Python

```python
import sys

def solve():
    s = sys.stdin.read().strip()
    if not s:
        return
    solution = Solution()
    print(str(solution.can_rotate_to_palindrome(s)).lower())

class Solution:
    def can_rotate_to_palindrome(self, s: str) -> bool:
        # Implement here
        return False

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    bool canRotateToPalindrome(string s) {
        // Implement here
        return false;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string s;
    if (cin >> s) {
        Solution sol;
        cout << (sol.canRotateToPalindrome(s) ? "true" : "false") << endl;
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  canRotateToPalindrome(s) {
    // Implement here
    return false;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", (line) => {
  const s = line.trim();
  if (s) {
    const sol = new Solution();
    console.log(sol.canRotateToPalindrome(s));
  }
});
```
