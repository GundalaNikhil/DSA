---
problem_id: STC_PALINDROMIC_TREE_EERTREE__2893
display_id: STC-013
slug: palindromic-tree-eertree
title: "Palindromic Tree (Eertree) Construction"
difficulty: Hard
difficulty_score: 68
topics:
  - Strings
  - Palindromes
  - Eertree
tags:
  - strings
  - palindromes
  - eertree
  - hard
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# STC-013: Palindromic Tree (Eertree) Construction

## Problem Statement

Build a palindromic tree (eertree) for a string `s` and output the number of distinct palindromic substrings in `s`.

![Problem Illustration](../images/STC-013/problem-illustration.png)

## Input Format

- First line: string `s`

## Output Format

- Single integer: count of distinct palindromic substrings

## Constraints

- `1 <= |s| <= 100000`
- `s` contains lowercase English letters

## Example

**Input:**

```
aba
```

**Output:**

```
3
```

**Explanation:**

Distinct palindromic substrings are "a", "b", and "aba".

![Example Visualization](../images/STC-013/example-1.png)

## Notes

- The eertree has two root nodes for lengths -1 and 0.
- Each node represents a distinct palindrome.
- The answer is the number of nodes minus the two roots.
- Time complexity: O(n) with a fixed alphabet.

## Related Topics

Eertree, Palindromes, String Data Structures

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int countDistinctPalindromes(String s) {
        // Implement here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String s = sc.next();
            Solution solution = new Solution();
            System.out.println(solution.countDistinctPalindromes(s));
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
    print(solution.count_distinct_palindromes(s))

class Solution:
    def count_distinct_palindromes(self, s: str) -> int:
        # Implement here
        return 0

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    int countDistinctPalindromes(string s) {
        // Implement here
        return 0;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string s;
    if (cin >> s) {
        Solution sol;
        cout << sol.countDistinctPalindromes(s) << endl;
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  countDistinctPalindromes(s) {
    // Implement here
    return 0;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", (line) => {
  const s = line.trim();
  if (!s) return;

  const sol = new Solution();
  console.log(sol.countDistinctPalindromes(s));
});
```
