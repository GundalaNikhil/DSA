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
import java.io.*;

class Solution {
    public int countChanges(String s) {
        return 0;
    }
}

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        String line;
        while ((line = br.readLine()) != null) {
            sb.append(line);
        }
        String s = sb.toString().trim();
        
        if (s.isEmpty()) {
            System.out.println(0);
            return;
        }

        Solution sol = new Solution();
        System.out.println(sol.countChanges(s));
    }
}
```

### Python

```python
def count_changes(s: str) -> int:
    return 0
def main():
    import sys
    s = sys.stdin.read().strip()
    result = count_changes(s)
    print(result)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <string>
#include <stack>
#include <vector>
#include <map>

using namespace std;

class Solution {
public:
    int countChanges(string s) {
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    // Read all input until EOF
    string s;
    char c;
    while (cin.get(c)) {
        s += c;
    }
    
    // Trim string (remove trailing newline/whitespace if any)
    while (!s.empty() && isspace(s.back())) s.pop_back();
    while (!s.empty() && isspace(s.front())) s.erase(0, 1);

    if (s.empty()) {
        cout << 0 << endl;
        return 0;
    }

    Solution sol;
    cout << sol.countChanges(s) << endl;
    
    return 0;
}
```

### JavaScript

```javascript
class Solution {
  countChanges(s) {
    return 0;
  }
}

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = "";
rl.on("line", (line) => {
  data += line;
});

rl.on("close", () => {
  const s = data.trim();
  if (s.length === 0) {
      console.log(0);
      return;
  }
  const solution = new Solution();
  console.log(solution.countChanges(s));
});
```

