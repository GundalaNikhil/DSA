---
problem_id: STK_NOTEBOOK_UNDO_SIMULATOR__4827
display_id: STK-001
slug: notebook-undo-simulator
title: "Notebook Undo Simulator"
difficulty: Easy
difficulty_score: 20
topics:
  - Stack
  - Simulation
  - Data Structures
tags:
  - stack
  - simulation
  - easy
  - commands
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# STK-001: Notebook Undo Simulator

## Problem Statement

You are implementing an undo buffer for a notebook editor. The buffer is a stack that supports:

- `PUSH x`: push value `x`
- `POP`: remove and output the top value
- `TOP`: output the top value without removing

If `POP` or `TOP` is called on an empty stack, output `EMPTY`.

![Problem Illustration](../images/STK-001/problem-illustration.png)

## Input Format

- First line: integer `m` (number of commands)
- Next `m` lines: one command (`PUSH x`, `POP`, or `TOP`)

## Output Format

- For each `POP` or `TOP` command, output one line:
  - the value at the top, or
  - `EMPTY` if the stack is empty

## Constraints

- `1 <= m <= 100000`
- `-10^9 <= x <= 10^9`

## Example

**Input:**

```
5
PUSH 10
PUSH -1
TOP
POP
TOP
```

**Output:**

```
-1
-1
10
```

**Explanation:**

The stack becomes [10, -1], TOP shows -1, POP removes -1, then TOP shows 10.

![Example Visualization](../images/STK-001/example-1.png)

## Notes

- Use an array or list as the underlying stack
- Each command runs in O(1)
- Only `POP` and `TOP` produce output
- Keep values as 64-bit to be safe

## Related Topics

Stack, Simulation, LIFO

---

## Solution Template
### Java

```java
import java.util.*;

class Solution {
    public List<String> process(List<String[]> ops) {
        //Implement here
        return new ArrayList<>();
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int m = sc.nextInt();
        List<String[]> ops = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            String op = sc.next();
            if (op.equals("PUSH")) {
                ops.add(new String[]{op, sc.next()});
            } else {
                ops.add(new String[]{op});
            }
        }

        Solution solution = new Solution();
        List<String> out = solution.process(ops);
        for (String s : out) System.out.println(s);
        sc.close();
    }
}
```

### Python

```python
def process(ops: list[list[str]]) -> list[str]:
    # //Implement here
    return 0

def main():
    import sys
    lines = sys.stdin.read().strip().split('\n')
    if not lines:
        return

    m = int(lines[0])
    ops = []
    for i in range(1, m + 1):
        parts = lines[i].split()
        ops.append(parts)

    result = process(ops)
    for r in result:
        print(r)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <vector>
#include <string>
#include <stack>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<string> process(const vector<vector<string>>& ops) {
        //Implement here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int m;
    if (!(cin >> m)) return 0;
    vector<vector<string>> ops;
    ops.reserve(m);
    for (int i = 0; i < m; i++) {
        string op;
        cin >> op;
        if (op == "PUSH") {
            string x;
            cin >> x;
            ops.push_back({op, x});
        } else {
            ops.push_back({op});
        }
    }

    Solution solution;
    vector<string> out = solution.process(ops);
    for (const string& s : out) cout << s << "\n";
    return 0;
}
```

### JavaScript

```javascript
class Solution {
  process(ops) {
    //Implement here
    return 0;
  }
}

const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const m = parseInt(data[idx++], 10);
  const ops = [];
  for (let i = 0; i < m; i++) {
    const op = data[idx++];
    if (op === "PUSH") {
      ops.push([op, data[idx++]]);
    } else {
      ops.push([op]);
    }
  }

  const solution = new Solution();
  const out = solution.process(ops);
  console.log(out.join("\n"));
});
```

