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
    public List<String> process(List<String[]> ops) {
        // Your implementation here
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
    # Your implementation here
    return []

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    m = int(next(it))
    ops = []
    for _ in range(m):
        op = next(it)
        if op == "PUSH":
            ops.append([op, next(it)])
        else:
            ops.append([op])

    out = process(ops)
    sys.stdout.write("\n".join(out))

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
    vector<string> process(const vector<vector<string>>& ops) {
        // Your implementation here
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
const readline = require("readline");

class Solution {
  process(ops) {
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
