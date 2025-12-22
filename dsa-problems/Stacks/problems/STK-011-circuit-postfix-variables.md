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

class Solution {
    public long eval(List<String> tokens, Map<String, Long> vars) {
        // Your implementation here
        return 0L;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        List<String> tokens = new ArrayList<>();
        for (int i = 0; i < t; i++) tokens.add(sc.next());
        int m = sc.nextInt();
        Map<String, Long> vars = new HashMap<>();
        for (int i = 0; i < m; i++) {
            String k = sc.next();
            long v = sc.nextLong();
            vars.put(k, v);
        }

        Solution solution = new Solution();
        System.out.println(solution.eval(tokens, vars));
        sc.close();
    }
}
```

### Python

```python
def eval_postfix(tokens: list[str], vars: dict[str, int]) -> int:
    # Your implementation here
    return 0

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    t = int(next(it))
    tokens = [next(it) for _ in range(t)]
    m = int(next(it))
    vars = {}
    for _ in range(m):
        k = next(it)
        v = int(next(it))
        vars[k] = v

    print(eval_postfix(tokens, vars))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
    long long eval(const vector<string>& tokens, const unordered_map<string,long long>& vars) {
        // Your implementation here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (!(cin >> t)) return 0;
    vector<string> tokens(t);
    for (int i = 0; i < t; i++) cin >> tokens[i];
    int m;
    cin >> m;
    unordered_map<string,long long> vars;
    for (int i = 0; i < m; i++) {
        string k;
        long long v;
        cin >> k >> v;
        vars[k] = v;
    }

    Solution solution;
    cout << solution.eval(tokens, vars) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  eval(tokens, vars) {
    // Your implementation here
    return 0;
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
  let idx = 0;
  const t = parseInt(data[idx++], 10);
  const tokens = [];
  for (let i = 0; i < t; i++) tokens.push(data[idx++]);
  const m = parseInt(data[idx++], 10);
  const vars = new Map();
  for (let i = 0; i < m; i++) {
    const k = data[idx++];
    const v = parseInt(data[idx++], 10);
    vars.set(k, v);
  }

  const solution = new Solution();
  console.log(solution.eval(tokens, vars).toString());
});
```
