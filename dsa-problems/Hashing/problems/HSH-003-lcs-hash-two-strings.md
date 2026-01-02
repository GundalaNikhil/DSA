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
import java.util.*;

class Solution {
    public int longestCommonSubstring(String a, String b) {
        // Implementation here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String a = sc.nextLine();
            String b = sc.nextLine();
            Solution solution = new Solution();
            System.out.println(solution.longestCommonSubstring(a, b));
        }
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def longest_common_substring(self, a: str, b: str) -> int:
        # Implementation here
        return 0

def main():
    lines = sys.stdin.read().strip().split('\n')
    if len(lines) < 2:
        return

    a = lines[0] if len(lines) > 0 else ""
    b = lines[1] if len(lines) > 1 else ""
    print(longest_common_substring(a, b))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <string>
#include <unordered_set>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int longestCommonSubstring(string a, string b) {
        // Implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string a, b;
    if (getline(cin, a) && getline(cin, b)) {
        Solution solution;
        cout << solution.longestCommonSubstring(a, b) << "\n";
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  longestCommonSubstring(a, b) {
    // Implementation here
    return null;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  if (data.length < 2) return;
  const a = data[0];
  const b = data[1];

  const solution = new Solution();
  console.log(solution.longestCommonSubstring(a, b));
});
```
