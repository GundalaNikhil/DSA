---
problem_id: REC_ROBOT_ROUTE_TURNS__7405
display_id: REC-005
slug: robot-route-turns
title: "Robot Route With Turns"
difficulty: Medium
difficulty_score: 52
topics:
  - Recursion
  - Backtracking
  - Grid
tags:
  - recursion
  - backtracking
  - grid
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# REC-005: Robot Route With Turns

## Problem Statement

A robot must move from the top-left cell `(0,0)` to the bottom-right cell `(r-1,c-1)` on a grid. You may move up, down, left, or right, but cannot enter blocked cells (`1`).

Find any valid path that uses at most `T` turns, where a turn is a change in movement direction between consecutive steps. If no path exists, output `NONE`.

![Problem Illustration](../images/REC-005/problem-illustration.png)

## Input Format

- First line: integers `r`, `c`, and `T`
- Next `r` lines: `c` space-separated integers (0 = open, 1 = blocked)

## Output Format

- One line with the path as coordinates `row,col` separated by spaces
- If no valid path exists, output `NONE`

## Constraints

- `1 <= r, c <= 8`
- `0 <= T <= 6`
- Grid values are `0` or `1`

## Example

**Input:**

```
3 3 2
0 0 0
1 1 0
0 0 0
```

**Output:**

```
0,0 0,1 0,2 1,2 2,2
```

**Explanation:**

The path goes right, right, down, down. It has one turn (right to down).

![Example Visualization](../images/REC-005/example-1.png)

## Notes

- Track the previous direction to count turns
- Use a visited grid to avoid cycles
- Stop early when turns exceed `T`
- Any valid path is acceptable

## Related Topics

Backtracking, Grid Search, Pruning

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long countPaths(int r, int c, int t) {
        // Implementation here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int r = sc.nextInt();
        int c = sc.nextInt();
        int T = sc.nextInt();
        
        Solution sol = new Solution();
        System.out.println(sol.countPaths(r, c, T));
        sc.close();
    }
}
```

### Python

```python
import sys

def count_paths(r: int, c: int, T: int) -> int:
    # Implementation here
    return 0

def main():
    import sys
    first_line = sys.stdin.read().strip().split()
    r = int(first_line[0])
    c = int(first_line[1])
    T = int(first_line[2])
    result = count_paths(r, c, T)
    print(result)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

class Solution {
public:
    long countPaths(int r, int c, int t) {
        // Implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int r, c, T;
    if (!(cin >> r >> c >> T)) return 0;
    
    Solution sol;
    cout << sol.countPaths(r, c, T) << endl;
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  countPaths(r, c, T) {
    // Implementation here
    return null;
  }
}

const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
let tokens = [];
rl.on('line', (line) => { tokens.push(...line.trim().split(/\s+/)); });
rl.on('close', () => {
    if(tokens.length===0) return;
    let ptr = 0;
    const r = parseInt(tokens[ptr++]);
    const c = parseInt(tokens[ptr++]);
    const T = parseInt(tokens[ptr++]);
    
    const sol = new Solution();
    console.log(sol.countPaths(r, c, T).toString());
});
```
