---
problem_id: STK_LAB_MIXED_BRACKET_REPAIR__7391
display_id: STK-002
slug: lab-mixed-bracket-repair
title: "Lab Mixed Bracket Repair"
difficulty: Easy
difficulty_score: 34
topics:
  - Stack
  - Brackets
  - Greedy
tags:
  - stack
  - brackets
  - greedy
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# STK-002: Lab Mixed Bracket Repair

## Problem Statement

A string contains brackets from `()[]{}` and wildcards `?`. Each `?` can be replaced by any single bracket character. Determine if there exists a replacement so that the final string is balanced and well-nested.

Output `true` if possible, otherwise `false`.

![Problem Illustration](../images/STK-002/problem-illustration.png)

## Input Format

- First line: string `s`

## Output Format

- Single line: `true` or `false`

## Constraints

- `1 <= |s| <= 100000`
- `s` contains only `()[]{}` and `?`

## Example

**Input:**

```
(?[?])??
```

**Output:**

```
true
```

**Explanation:**

One valid replacement is `([[]])()`, which is balanced and well-nested.

![Example Visualization](../images/STK-002/example-1.png)

## Notes

- Use a stack to match bracket types
- Treat `?` as flexible to fix mismatches greedily
- The final string length must be even
- Time complexity: O(n)

## Related Topics

Stack, Bracket Matching, Greedy

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public boolean canBeBalanced(String s) {
        // Implement here
        return false;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String s = sc.next();
            Solution sol = new Solution();
            System.out.println(sol.canBeBalanced(s));
        }
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def can_be_balanced(self, s: str) -> bool:
        # Implement here
        return False

def solve():
    s = sys.stdin.read().strip()
    if not s:
        return
    sol = Solution()
    print(str(sol.can_be_balanced(s)).lower())

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <string>
#include <stack>

using namespace std;

class Solution {
public:
    bool canBeBalanced(string s) {
        // Implement here
        return false;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string s;
    if (cin >> s) {
        Solution sol;
        cout << (sol.canBeBalanced(s) ? "true" : "false") << endl;
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  canBeBalanced(s) {
    // Implement here
    return false;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false,
});

rl.on("line", (line) => {
  const s = line.trim();
  if (s) {
    const sol = new Solution();
    console.log(sol.canBeBalanced(s));
  }
});
```
