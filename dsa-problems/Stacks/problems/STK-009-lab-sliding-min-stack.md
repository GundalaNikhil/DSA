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
            } else if (op.equals("MIN")) {
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
        elif op == "MIN":
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
        } else if (op == "MIN") {
            string k;
            cin >> k;
            ops.push_back({op, k});
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
    } else if (op === "MIN") {
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
