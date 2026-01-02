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
import java.io.*;

class Solution {
    public List<String> process(List<String[]> ops) {
        // Implementation here
        return new ArrayList<>();
    }
}

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String line = br.readLine();
        if (line == null) return;
        
        int m = Integer.parseInt(line.trim());
        List<String[]> ops = new ArrayList<>();
        
        for (int i = 0; i < m; i++) {
            String l = br.readLine();
            if (l != null) {
                ops.add(l.trim().split("\\s+"));
            }
        }
        
        Solution sol = new Solution();
        List<String> res = sol.process(ops);
        
        for (String s : res) {
            System.out.println(s);
        }
    }
}
```

### Python

```python
import sys

def process(ops: list[list[str]]) -> list[str]:
    # Implementation here
    return []

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
#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <sstream>

using namespace std;

class Solution {
public:
    vector<string> process(const vector<vector<string>>& ops) {
        // Implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int m;
    if (!(cin >> m)) return 0;
    
    vector<vector<string>> ops;
    string method;
    
    for (int i = 0; i < m; i++) {
        cin >> method;
        if (method == "PUSH") {
            string val;
            cin >> val;
            ops.push_back({method, val});
        } else {
            ops.push_back({method});
        }
    }
    
    Solution sol;
    vector<string> res = sol.process(ops);
    
    for (const string& s : res) {
        cout << s << "\n";
    }
    
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  process(ops) {
    // Implementation here
    return null;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let lines = [];
rl.on("line", (line) => {
  lines.push(line);
});

rl.on("close", () => {
  if (lines.length === 0) return;
  
  const m = parseInt(lines[0].trim(), 10);
  const ops = [];
  
  for (let i = 1; i <= m; i++) { // Read m lines
    if (i < lines.length) {
      ops.push(lines[i].trim().split(/\s+/));
    }
  }
  
  const solution = new Solution();
  const res = solution.process(ops);
  console.log(res.join("\n"));
});
```
