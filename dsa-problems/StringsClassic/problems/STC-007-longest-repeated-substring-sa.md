---
problem_id: STC_LONGEST_REPEATED_SUBSTRING_SA__2764
display_id: STC-007
slug: longest-repeated-substring-sa
title: "Longest Repeated Substring via SA/LCP"
difficulty: Medium
difficulty_score: 50
topics:
  - Strings
  - Suffix Array
  - LCP
tags:
  - strings
  - suffix-array
  - lcp
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# STC-007: Longest Repeated Substring via SA/LCP

## Problem Statement

Given a string `s`, find the longest substring that appears at least twice. If multiple substrings have the same maximum length, return the lexicographically smallest one. If no repeated substring exists, output `NONE`.

![Problem Illustration](../images/STC-007/problem-illustration.png)

## Input Format

- First line: string `s`

## Output Format

- Single line: the longest repeated substring, or `NONE`

## Constraints

- `1 <= |s| <= 100000`
- `s` contains lowercase English letters

## Example

**Input:**

```
cababa
```

**Output:**

```
aba
```

**Explanation:**

The substring "aba" appears twice and is the longest repeated substring.

![Example Visualization](../images/STC-007/example-1.png)

## Notes

- Build suffix array and LCP array
- The maximum LCP value gives the length
- Track the smallest substring among ties
- Time complexity: O(n log n)

## Related Topics

Suffix Array, LCP, String Algorithms

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public String longestRepeated(String s) {
        // Implement here
        return "NONE";
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String s = sc.next();
            Solution solution = new Solution();
            System.out.println(solution.longestRepeated(s));
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
    print(solution.longest_repeated(s))

class Solution:
    def longest_repeated(self, s: str) -> str:
        # Implement here
        return "NONE"

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
    string longestRepeated(string s) {
        // Implement here
        return "NONE";
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string s;
    if (cin >> s) {
        Solution sol;
        cout << sol.longestRepeated(s) << endl;
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  longestRepeated(s) {
    // Implement here
    return "NONE";
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
  console.log(sol.longestRepeated(s));
});
```
