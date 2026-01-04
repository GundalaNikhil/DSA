---
problem_id: REC_EXPRESSION_TARGET_ONE_FLIP__9316
display_id: REC-009
slug: expression-target-one-flip
title: "Expression Target With One Negation Flip"
difficulty: Medium
difficulty_score: 57
topics:
  - Recursion
  - Backtracking
  - Expressions
tags:
  - recursion
  - backtracking
  - expressions
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# REC-009: Expression Target With One Negation Flip

## Problem Statement

Given a digit string `s`, insert `+` or `-` operators between digits or concatenate digits to form an expression that evaluates to `T`.

You may also apply a unary negation to at most one operand chunk (write it with a leading `-` without adding an operator). Use at most `c` binary operators in total.

Return all valid expressions in lexicographic order. If none exist, output `NONE`.

![Problem Illustration](../images/REC-009/problem-illustration.png)

## Input Format

- First line: string `s`
- Second line: integer `T`
- Third line: integer `c`

## Output Format

- Each valid expression on its own line, in lexicographic order
- Output `NONE` if no expression matches

## Constraints

- `1 <= |s| <= 10`
- `0 <= c <= 9`
- `-10^9 <= T <= 10^9`
- No chunk may have leading zeros unless the chunk is exactly `"0"`

## Example

**Input:**

```
1203
-202
2
```

**Output:**

```
1+-203
```

**Explanation:**

Split into `1` and `203`, insert `+`, and apply the unary flip to `203`: `1 + (-203) = -202`.

![Example Visualization](../images/REC-009/example-1.png)

## Notes

- Track current value, previous operator count, and whether a flip has been used
- Avoid leading-zero chunks
- The unary flip applies to a chosen chunk only once
- Backtracking is required to explore all splits

## Related Topics

Backtracking, Expression Evaluation, Recursion

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public void findExpressions(String s, int target, int c) {
        // Implement here
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNext()) return;
        String s = sc.next();
        int target = sc.nextInt();
        int c = sc.nextInt();
        Solution sol = new Solution();
        sol.findExpressions(s, target, c);
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def find_expressions(self, s, target, c):
        # Implement here
        pass

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    s = input_data[0]
    target = int(input_data[1])
    c = int(input_data[2])
    sol = Solution()
    sol.find_expressions(s, target, c)

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
    void findExpressions(string s, int target, int c) {
        // Implement here
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string s;
    int target, c;
    if (!(cin >> s >> target >> c)) return 0;
    Solution sol;
    sol.findExpressions(s, target, c);
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  findExpressions(s, target, c) {
    // Implement here
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 3) return;
  const s = input[0];
  const target = parseInt(input[1]);
  const c = parseInt(input[2]);
  const sol = new Solution();
  sol.findExpressions(s, target, c);
}

solve();
```
