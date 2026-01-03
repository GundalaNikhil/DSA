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
        //Implement here
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
def longest_common_substring(a: str, b: str) -> int:
    # //Implement here
    return 0

def main():
    import sys
    sys.setrecursionlimit(200000)
    input_data = sys.stdin.read().split()
    if len(input_data) < 2:
        return
    a, b = input_data[0], input_data[1]
    print(longest_common_substring(a, b))

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
    int longestCommonSubstring(const string& a, const string& b) {
        //Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string a, b;
    if (cin >> a >> b) {
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
  if (data.length < 2) return;
  const a = data[0];
  const b = data[1];
  const solution = new Solution();
  console.log(solution.longestCommonSubstring(a, b).toString());
});
```

