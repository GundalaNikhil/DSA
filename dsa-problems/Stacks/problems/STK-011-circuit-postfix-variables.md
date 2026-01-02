---
problem_id: STK_CIRCUIT_POSTFIX_VARIABLES__7493
display_id: STK-011
slug: circuit-postfix-variables
title: "Circuit Postfix Evaluator with Variables"
difficulty: Medium
difficulty_score: 55
topics:
  - Stack
  - Expression Evaluation
  - Parsing
tags:
  - stack
  - postfix
  - parsing
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# STK-011: Circuit Postfix Evaluator with Variables

## Problem Statement

Evaluate a postfix expression with integers, operators `+ - * / %`, single-letter variables, and two extra stack operations:

- `DUP`: duplicate the top value
- `SWAP`: swap the top two values

A variable map provides values for letters. All operations are performed modulo `MOD = 1000000007`. Division uses integer division after modulo normalization.

![Problem Illustration](../images/STK-011/problem-illustration.png)

## Input Format

- First line: integer `t` (number of tokens)
- Second line: `t` space-separated tokens
- Third line: integer `m` (number of variables)
- Next `m` lines: `char value` pairs

## Output Format

- Single integer: evaluation result modulo `MOD`

## Constraints

- `1 <= t <= 10000`
- `0 <= m <= 26`
- Variable values fit in 64-bit signed integer

## Example

**Input:**

```
5
x 5 + y *
2
x 3
y 2
```

**Output:**

```
16
```

**Explanation:**

(3 + 5) * 2 = 16.

![Example Visualization](../images/STK-011/example-1.png)

## Notes

- Push numbers or variable values
- Apply modulo after each operation
- `DUP` and `SWAP` operate on the stack directly
- Assume the expression is valid

## Related Topics

Postfix Evaluation, Stack, Parsing

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public long evalPostfix(String[] tokens, Map<String, Integer> vars) {
        // Implementation here
        return 0;
    }
}

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String line = br.readLine();
        if (line == null) return;
        int numVars = Integer.parseInt(line.trim());
        
        Map<String, Integer> vars = new HashMap<>();
        for (int i = 0; i < numVars; i++) {
            String[] parts = br.readLine().trim().split("\\s+");
            vars.put(parts[0], Integer.parseInt(parts[1]));
        }
        
        String expr = br.readLine();
        if (expr == null) return;
        String[] tokens = expr.trim().split("\\s+");
        
        Solution sol = new Solution();
        System.out.println(sol.evalPostfix(tokens, vars));
    }
}
```

### Python

```python
import sys

def eval_postfix(tokens: list[str], vars: dict[str, int]) -> int:
    # Implementation here
    return 0

def main():
    import sys
    lines = sys.stdin.read().strip().split('\n')
    if not lines:
        return

    num_vars = int(lines[0])
    vars_dict = {}
    for i in range(1, num_vars + 1):
        parts = lines[i].split()
        var_name = parts[0]
        var_val = int(parts[1])
        vars_dict[var_name] = var_val

    expr = lines[num_vars + 1].strip()
    tokens = expr.split()
    result = eval_postfix(tokens, vars_dict)
    print(result)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <map>

using namespace std;

class Solution {
public:
    long evalPostfix(vector<string>& tokens, map<string, int>& vars) {
        // Implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int numVars;
    if (!(cin >> numVars)) return 0;
    
    map<string, int> vars;
    for (int i = 0; i < numVars; i++) {
        string name;
        int val;
        cin >> name >> val;
        vars[name] = val;
    }
    
    string line;
    getline(cin >> ws, line); // Consume newline and read line
    // Wait, cin >> ws consumes whitespace.
    // If expr is on next line, this works.
    
    stringstream ss(line);
    string token;
    vector<string> tokens;
    while (ss >> token) {
        tokens.push_back(token);
    }
    
    Solution sol;
    cout << sol.evalPostfix(tokens, vars) << endl;
    
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  evalPostfix(tokens, vars) {
    // Implementation here
    return null;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let lines = [];
rl.on("line", (line) => {
  lines.push(line);
});

rl.on("close", () => {
  if (lines.length === 0) return;
  
  const numVars = parseInt(lines[0].trim(), 10);
  const vars = new Map();
  
  for (let i = 1; i <= numVars; i++) {
    const parts = lines[i].trim().split(/\s+/);
    vars.set(parts[0], parseInt(parts[1], 10));
  }
  
  const expr = lines[numVars + 1].trim();
  const tokens = expr.split(/\s+/);
  
  const solution = new Solution();
  console.log(solution.evalPostfix(tokens, vars));
});
```
