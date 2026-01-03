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
import java.io.*;

class Solution {
    public String solve(String expr) {
        //Implement here
        return "";
    }
}

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String expr = br.readLine();
        if (expr != null) {
            Solution sol = new Solution();
            System.out.println(sol.solve(expr.trim()));
        }
    }
}
```

### Python

```python
def solve(expr: str) -> str:
    # //Implement here
    return 0

def main():
    import sys
    expr = sys.stdin.read().strip()
    if not expr:
        return

    result = solve(expr)
    print(result)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <string>
#include <stack>
#include <map>
#include <cctype>

using namespace std;

class Solution {
public:
    string solve(string expr) {
        //Implement here
        return "";
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    string expr;
    if (getline(cin, expr)) {
        // Trim right usage of trailing newlines if any
        while (!expr.empty() && isspace(expr.back())) expr.pop_back();
        while (!expr.empty() && isspace(expr.front())) expr.erase(0, 1);
        
        Solution sol;
        cout << sol.solve(expr) << endl;
    }
    
    return 0;
}
```

### JavaScript

```javascript
class Solution {
  solve(expr) {
    //Implement here
    return 0;
  }
}

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", (line) => {
  if (line.trim() !== "") {
    const solution = new Solution();
    console.log(solution.solve(line.trim()));
    process.exit(0);
  }
});
```

