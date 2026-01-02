---
problem_id: QUE_CIRCULAR_SHUTTLE_BUFFER_OVERWRITE__7314
display_id: QUE-002
slug: circular-shuttle-buffer-overwrite
title: "Circular Shuttle Buffer with Overwrite"
difficulty: Easy
difficulty_score: 28
topics:
  - Queue
  - Circular Buffer
  - Simulation
tags:
  - queue
  - circular-buffer
  - simulation
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# QUE-002: Circular Shuttle Buffer with Overwrite
## Problem Statement
A campus shuttle system stores the last `k` sensor readings in a circular buffer. You must implement a fixed-capacity circular queue with the following commands:

- `ENQ x`: insert `x` at the rear if the buffer is not full (report success)
- `ENQ_OVR x`: insert `x`, overwriting the oldest value if full (report overwritten or `NONE`)
- `DEQ`: remove and report the front value
- `FRONT` / `REAR`: report value without removing
- `ISEMPTY` / `ISFULL`: report whether the buffer is empty/full
![Problem Illustration](../images/QUE-002/problem-illustration.png)
## Input Format
- First line: integer `k` (capacity)
- Second line: integer `m` (number of commands)
- Next `m` lines: one command per line
## Output Format
- For each command that reports a value, output one line: `ENQ` -> `true`/`false`, `ENQ_OVR` -> overwritten or `NONE`, `DEQ`/`FRONT`/`REAR` -> value or `EMPTY`, `ISEMPTY`/`ISFULL` -> `true`/`false`
## Constraints
- `1 <= k <= 100000`
- `1 <= m <= 100000`
- `-10^9 <= x <= 10^9`

## Example

**Input:**

```
2
6
ENQ 5
ENQ 6
ENQ 7
ENQ_OVR 8
FRONT
REAR
```

**Output:**

```
true
true
false
5
6
8
```

**Explanation:**

Sequence: ENQ 5 -> success, ENQ 6 -> success, ENQ 7 -> fails (full), ENQ_OVR 8 -> overwrites 5, FRONT -> 6, REAR -> 8.

![Example Visualization](../images/QUE-002/example-1.png)

## Notes

- Track head, tail, and current size
- All operations must be O(1)
- `ENQ_OVR` advances both head and tail when overwriting
- Use modulo arithmetic for wraparound

## Related Topics

Queue, Circular Buffer, Simulation

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public List<String> processOperations(int k, List<String[]> operations) {
        return null;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int k = sc.nextInt();
            int m = sc.nextInt();
            List<String[]> operations = new ArrayList<>();
    
            for (int i = 0; i < m; i++) {
                String op = sc.next();
                if (op.equals("ENQ") || op.equals("ENQ_OVR")) {
                    String x = sc.next();
                    operations.add(new String[]{op, x});
                } else {
                    operations.add(new String[]{op});
                }
            }
    
            Solution solution = new Solution();
            List<String> result = solution.processOperations(k, operations);
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
from typing import List
import sys

def process_operations(k: int, operations: List[List[str]]) -> List[str]:
    return []
def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        k = int(next(iterator))
        m = int(next(iterator))
        operations = []
        for _ in range(m):
            op = next(iterator)
            if op in ("ENQ", "ENQ_OVR"):
                val = next(iterator)
                operations.append([op, val])
            else:
                operations.append([op])

        result = process_operations(k, operations)
        print("\n".join(result))
    except StopIteration:
        pass

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
    vector<string> processOperations(int k, const vector<vector<string>>& operations) {
        return "";
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k, m;
    if (cin >> k >> m) {
        vector<vector<string>> operations;
        operations.reserve(m);
        for (int i = 0; i < m; i++) {
            string op;
            cin >> op;
            if (op == "ENQ" || op == "ENQ_OVR") {
                string val;
                cin >> val;
                operations.push_back({op, val});
            } else {
                operations.push_back({op});
            }
        }
    
        Solution solution;
        vector<string> result = solution.processOperations(k, operations);
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
  processOperations(k, operations) {
    return 0;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/).filter(x => x !== "")));
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const k = parseInt(data[idx++], 10);
  const m = parseInt(data[idx++], 10);
  const operations = [];

  for (let i = 0; i < m; i++) {
    const op = data[idx++];
    if (op === "ENQ" || op === "ENQ_OVR") {
      const x = data[idx++];
      operations.push([op, x]);
    } else {
      operations.push([op]);
    }
  }

  const solution = new Solution();
  const result = solution.processOperations(k, operations);
  console.log(result.join("\n"));
});
```

