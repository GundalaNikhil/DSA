---
problem_id: REC_KNIGHT_TOUR_BLOCKED__7742
display_id: REC-012
slug: knight-tour-blocked
title: "Knight Tour With Blocked Cells"
difficulty: Medium
difficulty_score: 60
topics:
  - Recursion
  - Backtracking
  - Chess
tags:
  - recursion
  - backtracking
  - knight-tour
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# REC-012: Knight Tour With Blocked Cells

## Problem Statement

On an `n x n` board, a knight starts at `(0,0)` and must visit every unblocked cell exactly once using standard knight moves.

Some cells are blocked and cannot be visited. Output any valid path that visits all unblocked cells, or `NONE` if impossible.

![Problem Illustration](../images/REC-012/problem-illustration.png)

## Input Format

- First line: integer `n`
- Second line: integer `b` (number of blocked cells)
- Next `b` lines: two integers `r` and `c` for each blocked cell

## Output Format

- One line with the path as `row,col` coordinates separated by spaces
- Output `NONE` if no tour exists

## Constraints

- `1 <= n <= 5`
- `0 <= b < n * n`
- `(0,0)` is guaranteed to be unblocked

## Example

**Input:**

```
2
3
0 1
1 0
1 1
```

**Output:**

```
0,0
```

**Explanation:**

Only the start cell is unblocked, so the tour is just `(0,0)`.

![Example Visualization](../images/REC-012/example-1.png)

## Notes

- Track visited cells and remaining unblocked count
- Knight moves are (±2, ±1) and (±1, ±2)
- Backtracking is required due to branching
- Any valid tour is acceptable

## Related Topics

Backtracking, Graph Traversal, Recursion

---

## Solution Template
### Java

```java
import java.util.*;

class Solution {
    public List<int[]> knightTour(int n, boolean[][] blocked) {
        // Your implementation here
        return new ArrayList<>();
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int b = sc.nextInt();
        boolean[][] blocked = new boolean[n][n];
        for (int i = 0; i < b; i++) {
            int r = sc.nextInt();
            int c = sc.nextInt();
            blocked[r][c] = true;
        }

        Solution solution = new Solution();
        List<int[]> path = solution.knightTour(n, blocked);
        if (path.isEmpty()) {
            System.out.println("NONE");
        } else {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < path.size(); i++) {
                if (i > 0) sb.append(' ');
                sb.append(path.get(i)[0]).append(',').append(path.get(i)[1]);
            }
            System.out.println(sb.toString());
        }
        sc.close();
    }
}
```

### Python

```python
def knight_tour(n: int, blocked: list[list[bool]]) -> list[tuple[int, int]]:
    # Your implementation here
    return []

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    b = int(next(it))
    blocked = [[False] * n for _ in range(n)]
    for _ in range(b):
        r = int(next(it))
        c = int(next(it))
        blocked[r][c] = True

    path = knight_tour(n, blocked)
    if not path:
        print("NONE")
    else:
        print(" ".join(f"{r},{c}" for r, c in path))

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
    vector<pair<int,int>> knightTour(int n, const vector<vector<bool>>& blocked) {
        // Your implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, b;
    if (!(cin >> n >> b)) return 0;
    vector<vector<bool>> blocked(n, vector<bool>(n, false));
    for (int i = 0; i < b; i++) {
        int r, c;
        cin >> r >> c;
        blocked[r][c] = true;
    }

    Solution solution;
    vector<pair<int,int>> path = solution.knightTour(n, blocked);
    if (path.empty()) {
        cout << "NONE\n";
    } else {
        for (int i = 0; i < (int)path.size(); i++) {
            if (i) cout << ' ';
            cout << path[i].first << ',' << path[i].second;
        }
        cout << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  knightTour(n, blocked) {
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
  const n = parseInt(data[idx++], 10);
  const b = parseInt(data[idx++], 10);
  const blocked = Array.from({ length: n }, () => Array(n).fill(false));
  for (let i = 0; i < b; i++) {
    const r = parseInt(data[idx++], 10);
    const c = parseInt(data[idx++], 10);
    blocked[r][c] = true;
  }

  const solution = new Solution();
  const path = solution.knightTour(n, blocked);
  if (path.length === 0) {
    console.log("NONE");
  } else {
    console.log(path.map((p) => ``p[0],`{p[1]}`).join(" "));
  }
});
```
