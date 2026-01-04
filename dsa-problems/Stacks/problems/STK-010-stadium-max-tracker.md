---
problem_id: STK_STADIUM_MAX_TRACKER__3658
display_id: STK-010
slug: stadium-max-tracker
title: "Stadium Max Tracker"
difficulty: Medium
difficulty_score: 40
topics:
  - Stack
  - Data Structures
  - Design
tags:
  - stack
  - max-stack
  - design
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# STK-010: Stadium Max Tracker

## Problem Statement

Design a stack that supports:

- `PUSH x`
- `POP`: remove and output the top
- `TOP`: output the top without removing
- `GETMAX`: output the current maximum element

If the stack is empty for `POP`, `TOP`, or `GETMAX`, output `EMPTY`.

![Problem Illustration](../images/STK-010/problem-illustration.png)

## Input Format

- First line: integer `m`
- Next `m` lines: commands

## Output Format

- For each command except `PUSH`, output one line with the result

## Constraints

- `1 <= m <= 100000`
- `-10^9 <= x <= 10^9`

## Example

**Input:**

```
6
PUSH 2
PUSH 9
PUSH 5
GETMAX
POP
GETMAX
```

**Output:**

```
9
5
9
```

**Explanation:**

Max is 9, POP removes 5, then max is still 9.

![Example Visualization](../images/STK-010/example-1.png)

## Notes

- Maintain an auxiliary stack for current maxima
- Each operation is O(1)
- Popping must update the max stack
- Use 64-bit integers if needed

## Related Topics

Stack Design, Max Stack, Data Structures

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    // Implement underlying stack and max stack logic

    public void push(long x) {
        // Implement
    }

    public String pop() {
        // Implement
        return "";
    }

    public String top() {
        // Implement
        return "";
    }

    public String getMax() {
        // Implement
        return "";
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
                } else if (cmd.equals("GETMAX")) {
                    System.out.println(sol.getMax());
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
        # Implement
        pass

    def push(self, x: int):
        # Implement
        pass

    def pop(self) -> str:
        # Implement
        return ""

    def top(self) -> str:
        # Implement
        return ""

    def get_max(self) -> str:
        # Implement
        return ""

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
        elif cmd == "GETMAX":
            print(sol.get_max())

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
    void push(long long x) {
        // Implement
    }

    string pop() {
        // Implement
        return "";
    }

    string top() {
        // Implement
        return "";
    }

    string get_max() {
        // Implement
        return "";
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
            } else if (cmd == "GETMAX") {
                cout << sol.get_max() << "\n";
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
    // Implement
  }

  push(x) {
    // Implement
  }

  pop() {
    // Implement
    return "";
  }

  top() {
    // Implement
    return "";
  }

  getMax() {
    // Implement
    return "";
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
    } else if (cmd === "GETMAX") {
      process.stdout.write(sol.getMax() + "\n");
    }
    count++;
  }
});
```
