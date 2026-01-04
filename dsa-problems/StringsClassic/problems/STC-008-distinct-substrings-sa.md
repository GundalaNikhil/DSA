---
problem_id: STC_DISTINCT_SUBSTRINGS_SA__9517
display_id: STC-008
slug: distinct-substrings-sa
title: "Distinct Substrings Count via SA/LCP"
difficulty: Medium
difficulty_score: 46
topics:
  - Strings
  - Suffix Array
  - Counting
tags:
  - strings
  - suffix-array
  - counting
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# STC-008: Distinct Substrings Count via SA/LCP

## Problem Statement

Given a string `s`, compute the number of distinct substrings. Use the formula:

```
count = n*(n+1)/2 - sum(LCP)
```

where `LCP` is the array of longest common prefixes between adjacent suffixes in suffix array order.

![Problem Illustration](../images/STC-008/problem-illustration.png)

## Input Format

- First line: string `s`

## Output Format

- Single integer: number of distinct substrings

## Constraints

- `1 <= |s| <= 100000`
- `s` contains lowercase English letters

## Example

**Input:**

```
aaa
```

**Output:**

```
3
```

**Explanation:**

Distinct substrings are "a", "aa", "aaa".

![Example Visualization](../images/STC-008/example-1.png)

## Notes

- Build suffix array and LCP array
- Use 64-bit arithmetic for the total count
- Time complexity: O(n log n)
- Space complexity: O(n)

## Related Topics

Suffix Array, LCP, Counting

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long countDistinct(String s) {
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
            System.out.println(solution.countDistinct(s));
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
    print(solution.count_distinct(s))

class Solution:
    def count_distinct(self, s: str) -> int:
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
    long long countDistinct(string s) {
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
        cout << sol.countDistinct(s) << endl;
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  countDistinct(s) {
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
  console.log(sol.countDistinct(s));
});
```
