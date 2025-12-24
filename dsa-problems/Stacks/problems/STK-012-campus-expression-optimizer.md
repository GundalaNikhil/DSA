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
    public String solve(String expr) {
        // Your implementation here
        return "";
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String expr = sc.next();

        Solution solution = new Solution();
        System.out.println(solution.solve(expr));
        sc.close();
    }
}
```

### Python

```python
def solve(expr: str) -> str:
    # Your implementation here
    return ""

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    expr = data[0]
    print(solve(expr))

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
    string solve(const string& expr) {
        // Your implementation here
        return "";
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string expr;
    if (!(cin >> expr)) return 0;
    Solution solution;
    cout << solution.solve(expr) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  solve(expr) {
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
  const expr = data[0];
  const solution = new Solution();
  console.log(solution.solve(expr));
});
```
