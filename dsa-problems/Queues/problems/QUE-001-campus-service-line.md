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
    public void processCommands(int m, List<String> commands) {
        // Implement here
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int m = sc.nextInt();
        sc.nextLine();
        List<String> commands = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            commands.add(sc.nextLine());
        }
        Solution sol = new Solution();
        sol.processCommands(m, commands);
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def process_commands(self, m, commands):
        # Implement here
        pass

def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    m = int(input_data[0])
    commands = input_data[1:m+1]
    sol = Solution()
    sol.process_commands(m, commands)

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
    void processCommands(int m, const vector<string>& commands) {
        // Implement here
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int m;
    if (!(cin >> m)) return 0;
    string dummy;
    getline(cin, dummy);
    vector<string> commands(m);
    for (int i = 0; i < m; i++) {
        getline(cin, commands[i]);
    }
    Solution sol;
    sol.processCommands(m, commands);
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  processCommands(m, commands) {
    // Implement here
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\r?\n/);
  if (!input[0]) return;
  const m = parseInt(input[0]);
  const commands = input.slice(1, m + 1);
  const sol = new Solution();
  sol.processCommands(m, commands);
}

solve();
```
