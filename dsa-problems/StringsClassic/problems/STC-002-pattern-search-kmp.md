---
problem_id: STC_PATTERN_SEARCH_KMP__6142
display_id: STC-002
slug: pattern-search-kmp
title: "Pattern Search With KMP"
difficulty: Easy
difficulty_score: 30
topics:
  - Strings
  - KMP
  - Pattern Matching
tags:
  - strings
  - kmp
  - pattern-search
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# STC-002: Pattern Search With KMP

## Problem Statement

Given a pattern `p` and text `t`, find all starting indices where `p` occurs in `t` using the KMP algorithm.

Indices are 0-based and should be returned in increasing order.

![Problem Illustration](../images/STC-002/problem-illustration.png)

## Input Format

- First line: pattern string `p`
- Second line: text string `t`

## Output Format

- Single line: space-separated indices of all occurrences
- If there are no occurrences, print an empty line

## Constraints

- `1 <= |p|, |t| <= 200000`
- `p` and `t` contain lowercase English letters

## Example

**Input:**

```
aba
ababa
```

**Output:**

```
0 2
```

**Explanation:**

The pattern "aba" occurs at positions 0 and 2.

![Example Visualization](../images/STC-002/example-1.png)

## Notes

- Use the prefix function for `p`
- KMP runs in O(|p| + |t|)
- Overlapping matches should be included
- Output order must be increasing

## Related Topics

KMP, Pattern Matching, Prefix Function

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int[] findOccurrences(String p, String t) {
        // Implement here
        return new int[0];
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String p = sc.next();
            if (sc.hasNext()) {
                String t = sc.next();
                Solution solution = new Solution();
                int[] result = solution.findOccurrences(p, t);

                if (result.length == 0) {
                    System.out.println("");
                } else {
                    StringBuilder sb = new StringBuilder();
                    for (int i = 0; i < result.length; i++) {
                        if (i > 0) sb.append(' ');
                        sb.append(result[i]);
                    }
                    System.out.println(sb.toString());
                }
            }
        }
        sc.close();
    }
}
```

### Python

```python
import sys
from typing import List

def solve():
    input_data = sys.stdin.read().split()
    if len(input_data) < 2:
        return

    p = input_data[0]
    t = input_data[1]

    solution = Solution()
    result = solution.find_occurrences(p, t)

    print(*(result))

class Solution:
    def find_occurrences(self, p: str, t: str) -> List[int]:
        # Implement here
        return []

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
    vector<int> findOccurrences(string p, string t) {
        // Implement here
        return {};
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string p, t;
    if (cin >> p >> t) {
        Solution sol;
        vector<int> result = sol.findOccurrences(p, t);
        for (int i = 0; i < result.size(); i++) {
            cout << result[i] << (i == result.size() - 1 ? "" : " ");
        }
        cout << endl;
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  findOccurrences(p, t) {
    // Implement here
    return [];
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
  const p = input[0];
  const t = input[1];
  const sol = new Solution();
  console.log(sol.findOccurrences(p, t).join(" "));
});
```
