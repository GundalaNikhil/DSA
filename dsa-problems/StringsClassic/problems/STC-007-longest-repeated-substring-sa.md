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
        // Your implementation here
        return "";
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();

        Solution solution = new Solution();
        System.out.println(solution.longestRepeated(s));
        sc.close();
    }
}
```

### Python

```python
def longest_repeated(s: str) -> str:
    # Your implementation here
    return ""

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    s = data[0]
    print(longest_repeated(s))

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
    string longestRepeated(const string& s) {
        // Your implementation here
        return "";
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;
    Solution solution;
    cout << solution.longestRepeated(s) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  longestRepeated(s) {
    // Your implementation here
    return "";
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  const s = data[0];
  const solution = new Solution();
  console.log(solution.longestRepeated(s));
});
```
