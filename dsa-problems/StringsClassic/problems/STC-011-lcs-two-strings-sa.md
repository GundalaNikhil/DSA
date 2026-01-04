---
problem_id: STC_LCS_TWO_STRINGS_SA__4927
display_id: STC-011
slug: lcs-two-strings-sa
title: "Longest Common Substring of Two Strings (SA)"
difficulty: Medium
difficulty_score: 56
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

# STC-011: Longest Common Substring of Two Strings (SA)

## Problem Statement

Given two strings `a` and `b`, find the length of their longest common substring. A substring is a contiguous segment of a string.

![Problem Illustration](../images/STC-011/problem-illustration.png)

## Input Format

- First line: string `a`
- Second line: string `b`

## Output Format

- Single integer: length of the longest common substring

## Constraints

- `1 <= |a|, |b| <= 100000`
- `|a| + |b| <= 200000`
- Strings contain lowercase English letters

## Example

**Input:**

```
abcd
bc
```

**Output:**

```
2
```

**Explanation:**

The longest common substring is "bc" with length 2.

![Example Visualization](../images/STC-011/example-1.png)

## Notes

- Build a suffix array for `a + '#' + b` with a separator not in the alphabet.
- The answer is the maximum LCP of adjacent suffixes from different strings.
- Time complexity: O(n log n) with suffix array + LCP.
- Space complexity: O(n).

## Related Topics

Suffix Array, LCP, Longest Common Substring

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int longestCommonSubstring(String a, String b) {
        // Implement here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String a = sc.next();
            if (sc.hasNext()) {
                String b = sc.next();
                Solution solution = new Solution();
                System.out.println(solution.longestCommonSubstring(a, b));
            }
        }
        sc.close();
    }
}
```

### Python

```python
import sys

def solve():
    input_data = sys.stdin.read().split()
    if len(input_data) < 2:
        return

    a = input_data[0]
    b = input_data[1]

    solution = Solution()
    print(solution.longest_common_substring(a, b))

class Solution:
    def longest_common_substring(self, a: str, b: str) -> int:
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
    int longestCommonSubstring(string a, string b) {
        // Implement here
        return 0;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string a, b;
    if (cin >> a >> b) {
        Solution sol;
        cout << sol.longestCommonSubstring(a, b) << endl;
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  longestCommonSubstring(a, b) {
    // Implement here
    return 0;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
rl.on("line", (line) => {
  if (line.trim()) input.push(...line.trim().split(/\s+/));
}).on("close", () => {
  if (input.length < 2) return;
  const a = input[0];
  const b = input[1];

  const sol = new Solution();
  console.log(sol.longestCommonSubstring(a, b));
});
```
