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
    public List<String> expressions(String s, long target, int maxOps) {
        // Your implementation here
        return new ArrayList<>();
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        long target = sc.nextLong();
        int maxOps = sc.nextInt();

        Solution solution = new Solution();
        List<String> result = solution.expressions(s, target, maxOps);
        if (result.isEmpty()) {
            System.out.println("NONE");
        } else {
            for (String line : result) {
                System.out.println(line);
            }
        }
        sc.close();
    }
}
```

### Python

```python
def expressions(s: str, target: int, max_ops: int) -> list[str]:
    # Your implementation here
    return []

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    s = data[0]
    target = int(data[1])
    max_ops = int(data[2])

    result = expressions(s, target, max_ops)
    if not result:
        print("NONE")
    else:
        print("\n".join(result))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    vector<string> expressions(const string& s, long long target, int maxOps) {
        // Your implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    long long target;
    int maxOps;
    if (!(cin >> s >> target >> maxOps)) return 0;
    Solution solution;
    vector<string> result = solution.expressions(s, target, maxOps);
    if (result.empty()) {
        cout << "NONE\n";
    } else {
        for (const string& line : result) {
            cout << line << "\n";
        }
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  expressions(s, target, maxOps) {
    // Your implementation here
    return [];
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
  const target = parseInt(data[1], 10);
  const maxOps = parseInt(data[2], 10);

  const solution = new Solution();
  const result = solution.expressions(s, target, maxOps);
  if (result.length === 0) {
    console.log("NONE");
  } else {
    console.log(result.join("\n"));
  }
});
```
