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

(3 + 5) \* 2 = 16.

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

class Solution {
    public long evaluate(int t, String[] tokens, Map<Character, Long> variables) {
        // Implement here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int t = sc.nextInt();
            sc.nextLine(); // Consume newline
            String[] tokens = sc.nextLine().split("\\s+");
            int m = sc.nextInt();
            Map<Character, Long> variables = new HashMap<>();
            for (int i = 0; i < m; i++) {
                char var = sc.next().charAt(0);
                long val = sc.nextLong();
                variables.put(var, val);
            }
            Solution sol = new Solution();
            System.out.println(sol.evaluate(t, tokens, variables));
        }
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def evaluate(self, t: int, tokens: list, variables: dict) -> int:
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    t = int(input_data[0])
    tokens = input_data[1].split()
    m = int(input_data[2])
    variables = {}
    for i in range(m):
        var, val = input_data[3+i].split()
        variables[var] = int(val)
    sol = Solution()
    print(sol.evaluate(t, tokens, variables))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <sstream>

using namespace std;

class Solution {
public:
    long long evaluate(int t, const vector<string>& tokens, unordered_map<char, long long>& variables) {
        // Implement here
        return 0;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    if (cin >> t) {
        string line;
        getline(cin, line); // consume newline
        getline(cin, line);
        stringstream ss(line);
        vector<string> tokens;
        string token;
        while (ss >> token) tokens.push_back(token);

        int m;
        cin >> m;
        unordered_map<char, long long> variables;
        for (int i = 0; i < m; i++) {
            char var;
            long long val;
            cin >> var >> val;
            variables[var] = val;
        }

        Solution sol;
        cout << sol.evaluate(t, tokens, variables) << endl;
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  evaluate(t, tokens, variables) {
    // Implement here
    return 0;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false,
});

let input = [];
rl.on("line", (line) => {
  if (line.trim()) input.push(line.trim());
}).on("close", () => {
  if (input.length < 3) return;
  const t = parseInt(input[0]);
  const tokens = input[1].split(/\s+/);
  const m = parseInt(input[2]);
  const variables = {};
  for (let i = 0; i < m; i++) {
    const [varName, val] = input[3 + i].split(/\s+/);
    variables[varName] = BigInt(val);
  }
  const sol = new Solution();
  console.log(sol.evaluate(t, tokens, variables).toString());
});
```
