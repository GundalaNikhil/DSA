---
problem_id: QUE_CAMPUS_SERVICE_LINE__4821
display_id: QUE-001
slug: campus-service-line
title: "Campus Service Line"
difficulty: Easy
difficulty_score: 18
topics:
  - Queue
  - Simulation
  - Data Streams
tags:
  - queue
  - simulation
  - easy
  - data-structures
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# QUE-001: Campus Service Line

## Problem Statement

A campus service desk handles students in a strict first-in-first-out order. You must implement a queue that supports the following commands:

- `ENQUEUE x`: add student ID `x` to the back of the line
- `DEQUEUE`: remove and report the student at the front
- `FRONT`: report the student at the front without removing

If a `DEQUEUE` or `FRONT` is issued when the queue is empty, output `EMPTY`.

![Problem Illustration](../images/QUE-001/problem-illustration.png)

## Input Format

- First line: integer `m` (number of commands)
- Next `m` lines: command is `ENQUEUE x`, `DEQUEUE`, or `FRONT`

## Output Format

- For each `DEQUEUE` or `FRONT`, output the front value or `EMPTY`

## Constraints

- `1 <= m <= 100000`
- `-10^9 <= x <= 10^9`
- Commands are valid strings as described above

## Example

**Input:**

```
6
ENQUEUE 12
ENQUEUE -5
FRONT
DEQUEUE
FRONT
DEQUEUE
```

**Output:**

```
12
12
-5
-5
```

**Explanation:**

The queue starts empty. Sequence: ENQUEUE 12 -> [12], ENQUEUE -5 -> [12, -5], FRONT -> 12, DEQUEUE -> removes 12, FRONT -> -5, DEQUEUE -> removes -5.

![Example Visualization](../images/QUE-001/example-1.png)

## Notes

- A dynamic array with head/tail indices is sufficient
- Each command can be processed in O(1) amortized time
- Output is required only for `DEQUEUE` and `FRONT`
- Space complexity is O(m) in the worst case

## Related Topics

Queue, Simulation, FIFO

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public List<String> processCommands(List<String[]> commands) {
        return null;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int m = sc.nextInt();
            List<String[]> commands = new ArrayList<>();
    
            for (int i = 0; i < m; i++) {
                String op = sc.next();
                if (op.equals("ENQUEUE")) {
                    String x = sc.next();
                    commands.add(new String[]{op, x});
                } else {
                    commands.add(new String[]{op});
                }
            }
    
            Solution solution = new Solution();
            List<String> result = solution.processCommands(commands);
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
from collections import deque
from typing import List
import sys

def process_commands(commands: List[List[str]]) -> List[str]:
    return []
def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        m = int(next(iterator))
        commands = []
        for _ in range(m):
            op = next(iterator)
            if op == "ENQUEUE":
                val = next(iterator)
                commands.append([op, val])
            else:
                commands.append([op])
        
        result = process_commands(commands)
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
#include <queue>

using namespace std;

class Solution {
public:
    vector<string> processCommands(const vector<vector<string>>& commands) {
        return "";
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int m;
    if (cin >> m) {
        vector<vector<string>> commands;
        commands.reserve(m);
        for (int i = 0; i < m; i++) {
            string op;
            cin >> op;
            if (op == "ENQUEUE") {
                string val;
                cin >> val;
                commands.push_back({op, val});
            } else {
                commands.push_back({op});
            }
        }
    
        Solution solution;
        vector<string> result = solution.processCommands(commands);
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
  processCommands(commands) {
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
  const m = parseInt(data[idx++], 10);
  const commands = [];

  for (let i = 0; i < m; i++) {
    const op = data[idx++];
    if (op === "ENQUEUE") {
      const x = data[idx++];
      commands.push([op, x]);
    } else {
      commands.push([op]);
    }
  }

  const solution = new Solution();
  const result = solution.processCommands(commands);
  console.log(result.join("\n"));
});
```

