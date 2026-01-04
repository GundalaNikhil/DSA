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
    public void processCommands(int k, int m, List<String> commands) {
        // Implement here
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int k = sc.nextInt();
        int m = sc.nextInt();
        sc.nextLine();
        List<String> commands = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            commands.add(sc.nextLine());
        }
        Solution sol = new Solution();
        sol.processCommands(k, m, commands);
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def process_commands(self, k, m, commands):
        # Implement here
        pass

def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    k = int(input_data[0])
    m = int(input_data[1])
    commands = input_data[2:2+m]
    sol = Solution()
    sol.process_commands(k, m, commands)

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
    void processCommands(int k, int m, const vector<string>& commands) {
        // Implement here
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int k, m;
    if (!(cin >> k >> m)) return 0;
    string dummy;
    getline(cin, dummy);
    vector<string> commands(m);
    for (int i = 0; i < m; i++) {
        getline(cin, commands[i]);
    }
    Solution sol;
    sol.processCommands(k, m, commands);
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  processCommands(k, m, commands) {
    // Implement here
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\r?\n/);
  if (!input[0]) return;
  const k = parseInt(input[0]);
  const m = parseInt(input[1]);
  const commands = input.slice(2, 2 + m);
  const sol = new Solution();
  sol.processCommands(k, m, commands);
}

solve();
```
