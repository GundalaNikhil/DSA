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
    // Implement underlying stack logic here
    private List<Long> stack = new ArrayList<>();

    public String push(long x) {
        stack.add(x);
        return null;
    }

    public String pop() {
        if (stack.isEmpty()) return "EMPTY";
        return String.valueOf(stack.remove(stack.size() - 1));
    }

    public String top() {
        if (stack.isEmpty()) return "EMPTY";
        return String.valueOf(stack.get(stack.size() - 1));
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int m = sc.nextInt();
            Solution sol = new Solution();
            for (int i = 0; i < m; i++) {
                String cmd = sc.next();
                if (cmd.equals("PUSH")) {
                    sol.push(sc.nextLong());
                } else if (cmd.equals("POP")) {
                    System.out.println(sol.pop());
                } else if (cmd.equals("TOP")) {
                    System.out.println(sol.top());
                }
            }
        }
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def __init__(self):
        self.stack = []

    def push(self, x: int):
        self.stack.append(x)

    def pop(self) -> str:
        if not self.stack:
            return "EMPTY"
        return str(self.stack.pop())

    def top(self) -> str:
        if not self.stack:
            return "EMPTY"
        return str(self.stack[-1])

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    m = int(input_data[0])
    sol = Solution()
    idx = 1
    for _ in range(m):
        cmd = input_data[idx]
        idx += 1
        if cmd == "PUSH":
            sol.push(int(input_data[idx]))
            idx += 1
        elif cmd == "POP":
            print(sol.pop())
        elif cmd == "TOP":
            print(sol.top())

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
private:
    vector<long long> stack;

public:
    void push(long long x) {
        stack.push_back(x);
    }

    string pop() {
        if (stack.empty()) return "EMPTY";
        long long val = stack.back();
        stack.pop_back();
        return to_string(val);
    }

    string top() {
        if (stack.empty()) return "EMPTY";
        return to_string(stack.back());
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int m;
    if (cin >> m) {
        Solution sol;
        for (int i = 0; i < m; i++) {
            string cmd;
            cin >> cmd;
            if (cmd == "PUSH") {
                long long x;
                cin >> x;
                sol.push(x);
            } else if (cmd == "POP") {
                cout << sol.pop() << "\n";
            } else if (cmd == "TOP") {
                cout << sol.top() << "\n";
            }
        }
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  constructor() {
    this.stack = [];
  }

  push(x) {
    this.stack.push(x);
  }

  pop() {
    if (this.stack.length === 0) return "EMPTY";
    return this.stack.pop().toString();
  }

  top() {
    if (this.stack.length === 0) return "EMPTY";
    return this.stack[this.stack.length - 1].toString();
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false,
});

let sol = new Solution();
let m = -1;
let count = 0;

rl.on("line", (line) => {
  if (m === -1) {
    m = parseInt(line.trim());
    return;
  }
  if (count < m) {
    const parts = line.trim().split(/\s+/);
    const cmd = parts[0];
    if (cmd === "PUSH") {
      sol.push(BigInt(parts[1]));
    } else if (cmd === "POP") {
      process.stdout.write(sol.pop() + "\n");
    } else if (cmd === "TOP") {
      process.stdout.write(sol.top() + "\n");
    }
    count++;
  }
});
```
