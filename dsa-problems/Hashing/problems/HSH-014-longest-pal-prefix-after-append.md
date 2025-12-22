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
        // Your implementation here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        char c = sc.nextLine().charAt(0);

        Solution solution = new Solution();
        System.out.println(solution.longestPalindromicPrefix(s, c));
        sc.close();
    }
}
```

### Python

```python
def longest_palindromic_prefix(s: str, c: str) -> int:
    # Your implementation here
    return 0

def main():
    s = input().strip()
    c = input().strip()[0]

    result = longest_palindromic_prefix(s, c)
    print(result)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    int longestPalindromicPrefix(string s, char c) {
        // Your implementation here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    char c;
    getline(cin, s);
    cin >> c;

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
    // Your implementation here
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
  const s = data[0];
  const c = data[1][0];

  const solution = new Solution();
  console.log(solution.longestPalindromicPrefix(s, c));
});
```
