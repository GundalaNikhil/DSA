---
problem_id: REC_DORM_ROOM_PATHS__5731
display_id: REC-001
slug: dorm-room-paths
title: "Dorm Room Paths"
difficulty: Easy
difficulty_score: 22
topics:
  - Recursion
  - Dynamic Programming
  - Grid
tags:
  - recursion
  - memoization
  - grid
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# REC-001: Dorm Room Paths

## Problem Statement

A student can move only right or down through a dorm hallway grid from the top-left corner `(0,0)` to the bottom-right corner `(r-1,c-1)`. There are no blocked cells.

Count the total number of distinct paths. Use recursion with memoization to avoid recomputation.

![Problem Illustration](../images/REC-001/problem-illustration.png)

## Input Format

- First line: two integers `r` and `c` (rows and columns)

## Output Format

- Single integer: number of distinct paths

## Constraints

- `1 <= r, c <= 25`
- Answer fits in 64-bit signed integer

## Example

**Input:**

```
2 3
```

**Output:**

```
3
```

**Explanation:**

The valid paths are: RRD, RDR, and DRR.

![Example Visualization](../images/REC-001/example-1.png)

## Notes

- Base case: reaching the last cell counts as 1 path
- Memoize the number of paths from each cell
- Time complexity: O(r * c)
- Space complexity: O(r * c)

## Related Topics

Recursion, Memoization, Grid DP

---

## Solution Template
### Java

```java
import java.util.*;

class Solution {
    public long countPaths(int r, int c) {
        //Implement here
        return 0L;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int r = sc.nextInt();
        int c = sc.nextInt();
        Solution sol = new Solution();
        System.out.println(sol.countPaths(r, c));
        sc.close();
    }
}
```

### Python

```python
import sys

# Increase recursion depth for deep grids
sys.setrecursionlimit(2000)

def count_paths(r: int, c: int) -> int:
    # //Implement here
    return 0

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data or len(data) < 2:
        return

    r = int(data[0])
    c = int(data[1])
    print(count_paths(r, c))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    long long countPaths(int r, int c) {
        //Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int r; cin >> r;
    int c; cin >> c;
    Solution sol;
    cout << sol.countPaths(r, c) << endl;
    return 0;
}
```

### JavaScript

```javascript
class Solution {
  countPaths(r, c) {
    //Implement here
    return 0;
  }
}

const readline = require('readline');
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
let tokens = [];
rl.on('line', (line) => { tokens.push(...line.trim().split(/\s+/)); });
rl.on('close', () => {
    if(tokens.length===0) return;
    let ptr = 0;
    const r = parseInt(tokens[ptr++]);
    const c = parseInt(tokens[ptr++]);
    const sol = new Solution();
    console.log(sol.countPaths(r, c));
});
```

