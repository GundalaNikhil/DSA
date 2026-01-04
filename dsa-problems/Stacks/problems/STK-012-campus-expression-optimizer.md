---
problem_id: STK_CAMPUS_EXPRESSION_OPTIMIZER__4085
display_id: STK-012
slug: campus-expression-optimizer
title: "Campus Expression Optimizer"
difficulty: Medium
difficulty_score: 58
topics:
  - Stack
  - Parsing
  - Expressions
tags:
  - stack
  - infix
  - postfix
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# STK-012: Campus Expression Optimizer

## Problem Statement

Convert an infix expression to postfix. The expression contains single-letter operands, digits, operators `+ - * / % ^`, and parentheses.

Additionally:

- Detect syntax errors (mismatched parentheses or consecutive operators)
- Count redundant parenthesis pairs

Output the postfix expression or an error message, plus the redundant count.

![Problem Illustration](../images/STK-012/problem-illustration.png)

## Input Format

- First line: string `expr`

## Output Format

- If valid: one line `POSTFIX <postfix> <redundant_count>`
- If invalid: one line `ERROR <message> 0`

## Constraints

- `1 <= |expr| <= 10000`
- Operands are single uppercase letters or digits

## Example

**Input:**

```
A*((B+C)/D)
```

**Output:**

```
POSTFIX ABC+D/* 1
```

**Explanation:**

The outer parentheses are redundant; the postfix expression is `ABC+D/*`.

![Example Visualization](../images/STK-012/example-1.png)

## Notes

- Use operator stack with precedence and associativity
- Track previous token to detect invalid sequences
- Redundant parentheses enclose a single operand or have no effect
- Time complexity: O(n)

## Related Topics

Infix to Postfix, Stack, Parsing

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public String optimize(String expr) {
        // Implement here
        // Return in format "POSTFIX <result> <redundant>" or "ERROR <msg> 0"
        return "";
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String expr = sc.nextLine();
            Solution sol = new Solution();
            System.out.println(sol.optimize(expr));
        }
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def optimize(self, expr: str) -> str:
        # Implement here
        return ""

def solve():
    expr = sys.stdin.read().strip()
    if not expr:
        return
    sol = Solution()
    print(sol.optimize(expr))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <string>
#include <stack>
#include <vector>

using namespace std;

class Solution {
public:
    string optimize(string expr) {
        // Implement here
        return "";
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string expr;
    if (getline(cin, expr)) {
        Solution sol;
        cout << sol.optimize(expr) << endl;
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  optimize(expr) {
    // Implement here
    return "";
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false,
});

rl.on("line", (line) => {
  const expr = line.trim();
  if (expr) {
    const sol = new Solution();
    console.log(sol.optimize(expr));
  }
});
```
