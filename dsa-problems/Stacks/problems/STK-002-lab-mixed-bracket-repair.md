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
    public boolean canRepair(String s) {
        // Your implementation here
        return false;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();

        Solution solution = new Solution();
        System.out.println(solution.canRepair(s) ? "true" : "false");
        sc.close();
    }
}
```

### Python

```python
def can_repair(s: str) -> bool:
    # Your implementation here
    return False

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    s = data[0]
    print("true" if can_repair(s) else "false")

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
    bool canRepair(const string& s) {
        // Your implementation here
        return false;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;
    Solution solution;
    cout << (solution.canRepair(s) ? "true" : "false") << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  canRepair(s) {
    // Your implementation here
    return false;
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
  console.log(solution.canRepair(s) ? "true" : "false");
});
```
