---
problem_id: STC_KMP_PREFIX_FUNCTION__5824
display_id: STC-001
slug: kmp-prefix-function
title: "Prefix Function (KMP) Construction"
difficulty: Easy
difficulty_score: 22
topics:
  - Strings
  - KMP
  - Prefix Function
tags:
  - strings
  - kmp
  - prefix-function
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# STC-001: Prefix Function (KMP) Construction

## Problem Statement

Given a string `s`, compute its prefix function array `pi`, where `pi[i]` is the length of the longest proper prefix of `s[0..i]` that is also a suffix of `s[0..i]`.

![Problem Illustration](../images/STC-001/problem-illustration.png)

## Input Format

- First line: string `s`

## Output Format

- Single line: `n` integers `pi[0..n-1]`, space-separated

## Constraints

- `1 <= |s| <= 200000`
- `s` contains lowercase English letters

## Example

**Input:**

```
ababa
```

**Output:**

```
0 0 1 2 3
```

**Explanation:**

The prefix function grows because the string repeats the pattern "ab".

![Example Visualization](../images/STC-001/example-1.png)

## Notes

- `pi[0] = 0`
- Use the standard linear KMP prefix computation
- Time complexity: O(n)
- Space complexity: O(n)

## Related Topics

KMP, Prefix Function, String Matching

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int[] prefixFunction(String s) {
        // Implement here
        return new int[0];
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String s = sc.next();
            Solution solution = new Solution();
            int[] pi = solution.prefixFunction(s);

            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < pi.length; i++) {
                if (i > 0) sb.append(' ');
                sb.append(pi[i]);
            }
            System.out.println(sb.toString());
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
    s = sys.stdin.read().strip()
    if not s:
        return

    solution = Solution()
    pi = solution.prefix_function(s)
    print(*(pi))

class Solution:
    def prefix_function(self, s: str) -> List[int]:
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
    vector<int> prefixFunction(string s) {
        // Implement here
        return {};
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string s;
    if (cin >> s) {
        Solution sol;
        vector<int> pi = sol.prefixFunction(s);
        for (int i = 0; i < pi.size(); i++) {
            cout << pi[i] << (i == pi.size() - 1 ? "" : " ");
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
  prefixFunction(s) {
    // Implement here
    return [];
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
  console.log(sol.prefixFunction(s).join(" "));
});
```
