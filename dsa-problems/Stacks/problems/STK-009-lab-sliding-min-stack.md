---
problem_id: STK_LAB_SLIDING_MIN_STACK__5027
display_id: STK-009
slug: lab-sliding-min-stack
title: "Lab Sliding-Min Stack"
difficulty: Medium
difficulty_score: 52
topics:
  - Stack
  - Range Minimum
  - Data Structures
tags:
  - stack
  - min-stack
  - queries
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# STK-009: Lab Sliding-Min Stack

## Problem Statement

Maintain a stack with operations:

- `PUSH x`
- `POP`: remove and output top value
- `MIN k`: output the minimum among the top `k` elements (top counts as 1)

If `POP` is called on an empty stack, output `EMPTY`. If `MIN k` is requested with fewer than `k` elements, output `NA`.

![Problem Illustration](../images/STK-009/problem-illustration.png)

## Input Format

- First line: integer `m`
- Next `m` lines: commands as above

## Output Format

- For each `POP` and `MIN`, output one line with the result

## Constraints

- `1 <= m <= 100000`
- `-10^9 <= x <= 10^9`
- `1 <= k <= 100000`

## Example

**Input:**

```
6
PUSH 5
PUSH 1
PUSH 3
MIN 2
POP
MIN 2
```

**Output:**

```
1
3
1
```

**Explanation:**

Top 2 elements are [1,3], min is 1. POP removes 3. Top 2 are [5,1], min is 1.

![Example Visualization](../images/STK-009/example-1.png)

## Notes

- Store prefix mins to answer `MIN` quickly
- Use an auxiliary stack of minimums with counts
- Keep size to validate `MIN k`
- Time complexity per operation: O(1) amortized

## Related Topics

Stack, Min Stack, Range Queries

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    private List<Long> stack = new ArrayList<>();
    // Prefix minimums or min stack logic here

    public void push(long x) {
        // Implement
    }

    public String pop() {
        // Implement
        return "";
    }

    public String min(int k) {
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
                } else if (cmd.equals("MIN")) {
                    System.out.println(sol.min(sc.nextInt()));
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
        # Min stack structures

    def push(self, x: int):
        # Implement
        pass

    def pop(self) -> str:
        # Implement
        return ""

    def min(self, k: int) -> str:
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
        elif cmd == "MIN":
            print(sol.min(int(input_data[idx])))
            idx += 1

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

    string min_k(int k) {
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
            } else if (cmd == "MIN") {
                int k;
                cin >> k;
                cout << sol.min_k(k) << "\n";
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
    // Implement
  }

  pop() {
    // Implement
    return "";
  }

  min(k) {
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
    } else if (cmd === "MIN") {
      process.stdout.write(sol.min(parseInt(parts[1])) + "\n");
    }
    count++;
  }
});
```
