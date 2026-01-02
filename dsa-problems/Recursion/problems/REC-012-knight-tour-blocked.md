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
    int N;
    int total_unblocked;
    boolean[][] blocked;
    boolean[][] visited;
    int[] dr = {-2, -2, -1, -1, 1, 1, 2, 2};
    int[] dc = {-1, 1, -2, 2, -2, 2, -1, 1};

    public boolean knightTour(int n, boolean[][] blk) {
        return false;
    }

    int countOnward(int r, int c) {
        int cnt = 0;
        for(int i=0; i<8; i++) {
            int nr = r + dr[i];
            int nc = c + dc[i];
            if(nr >= 0 && nr < N && nc >= 0 && nc < N && !blocked[nr][nc] && !visited[nr][nc]) {
                cnt++;
            }
        }
        return cnt;
    }

    boolean dfs(int r, int c, int count) {
        if (count == total_unblocked) return true;

        List<int[]> moves = new ArrayList<>(); // {priority, dr_index}
        for(int i=0; i<8; i++) {
            int nr = r + dr[i];
            int nc = c + dc[i];
            if(nr >= 0 && nr < N && nc >= 0 && nc < N && !blocked[nr][nc] && !visited[nr][nc]) {
                moves.add(new int[]{countOnward(nr, nc), i});
            }
        }
        
        if(moves.isEmpty()) return false;
        
        moves.sort((a, b) -> Integer.compare(a[0], b[0]));

        for(int[] p : moves) {
            int i = p[1];
            int nr = r + dr[i];
            int nc = c + dc[i];
            
            visited[nr][nc] = true;
            if(dfs(nr, nc, count + 1)) return true;
            visited[nr][nc] = false;
        }
        return false;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if(!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int b = sc.nextInt();
        
        boolean[][] blocked = new boolean[n][n];
        for(int i=0; i<b; i++) {
            if(sc.hasNextInt()) {
                int r = sc.nextInt();
                int c = sc.nextInt();
                if(r >= 0 && r < n && c >= 0 && c < n) blocked[r][c] = true;
            }
        }
        
        Solution sol = new Solution();
        if(sol.knightTour(n, blocked)) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }
        sc.close();
    }
}
```

### Python

```python
def knight_tour_possible(n: int, blocked: list[list[bool]]) -> bool:
    return False
def main():
    import sys
    lines = sys.stdin.read().strip().split('\n')
    if len(lines) < 2:
        return
    n = int(lines[0])
    b = int(lines[1])
    blocked = [[False] * n for _ in range(n)]

    for i in range(2, 2 + b):
        if i < len(lines):
            parts = lines[i].strip().split()
            if len(parts) >= 2:
                r, c = int(parts[0]), int(parts[1])
                if 0 <= r < n and 0 <= c < n:
                    blocked[r][c] = True

    result = knight_tour_possible(n, blocked)
    print("YES" if result else "NO")

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
    int N;
    int total_unblocked;
    vector<vector<bool>> blocked;
    vector<vector<bool>> visited;
    int dr[8] = {-2, -2, -1, -1, 1, 1, 2, 2};
    int dc[8] = {-1, 1, -2, 2, -2, 2, -1, 1};

public:
    bool knightTour(int n, const vector<vector<bool>>& blk) {
        return false;
    }

    int countOnward(int r, int c) {
        return 0;
    }

    bool dfs(int r, int c, int count) {
        return false;
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n, b;
    if (!(cin >> n >> b)) return 0;
    
    vector<vector<bool>> blocked(n, vector<bool>(n, false));
    for(int i=0; i<b; i++) {
        int r, c;
        cin >> r >> c;
        if(r >= 0 && r < n && c >= 0 && c < n) blocked[r][c] = true;
    }
    
    Solution sol;
    if(sol.knightTour(n, blocked)) cout << "YES" << endl;
    else cout << "NO" << endl;
    return 0;
}
```

### JavaScript

```javascript
const readline = require('readline');
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
let tokens = [];
rl.on('line', (line) => { tokens.push(...line.trim().split(/\s+/)); });
rl.on('close', () => {
    if(tokens.length===0) return;
    let ptr = 0;
    const n = parseInt(tokens[ptr++]);
    const b = parseInt(tokens[ptr++]);
    
    // JS 2D array
    const blocked = Array.from({length: n}, () => Array(n).fill(false));
    for(let i=0; i<b; i++) {
        if(ptr < tokens.length) {
            const r = parseInt(tokens[ptr++]);
            const c = parseInt(tokens[ptr++]);
            if(r >= 0 && r < n && c >= 0 && c < n) blocked[r][c] = true;
        }
    }
    
    const sol = new Solution();
    if(sol.knightTour(n, blocked)) {
        console.log("YES");
    } else {
        console.log("NO");
    }
});

class Solution {
    knightTour(n, blocked) {
    return 0;
  }
    
    vis(r, c, val) {
    return 0;
  }
    
    isVis(r, c) {
    return 0;
  }
    
    countOnward(r, c) {
    return 0;
  }
    
    dfs(r, c, count) {
    return 0;
  }
}
```

