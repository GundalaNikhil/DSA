---
problem_id: GRP_FESTIVAL_MAZE_SHORTEST__7418
display_id: GRP-017
slug: festival-maze-shortest-path
title: "Festival Maze Shortest Path"
difficulty: Medium
difficulty_score: 55
topics:
  - Grid Graph
  - BFS
  - State Space Search
  - Shortest Path
tags:
  - graph
  - grid
  - bfs
  - state-space
  - shortest-path
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRP-017: Festival Maze Shortest Path

## Problem Statement

You are given a 2D grid representing a festival maze with the following cells:
- `S`: Start position (exactly one)
- `E`: Exit position (exactly one)
- `F`: Food stall (at least one)
- `#`: Wall (impassable)
- `.`: Open cell (passable)

You can move 4-directionally (up, down, left, right) through non-wall cells.

**Rule**: You must visit at least one food stall (`F`) before reaching the exit (`E`).

Find the minimum number of steps from `S` to `E` while satisfying the food stall visit rule, or return `-1` if impossible.

![Problem Illustration](../images/GRP-017/problem-illustration.png)

## Input Format

- First line: two integers `r c` (number of rows and columns)
- Next `r` lines: strings of length `c` representing the grid

## Output Format

- Single integer: minimum steps from S to E visiting at least one F, or `-1` if impossible

## Constraints

- `1 <= r, c <= 400`
- Total cells `<= 160,000`
- Grid contains exactly one `S`, exactly one `E`, and at least one `F`

## Example

**Input:**
```
3 3
SF.
###E
.F.
```

**Output:**
```
4
```

**Explanation:**

Grid layout:
```
S F .
# # # E
. F .
```

The optimal path demonstrates the constraint requirement:
```
S . F
# . .
. . E
```

Path: S(0,0) → (0,1) → F(0,2) → (1,2) → (2,2)=E: 4 steps ✓

![Example Visualization](../images/GRP-017/example-1.png)

## Notes

- Use BFS with state tracking: (row, col, visited_food_stall)
- State space: (r, c, {0, 1}) where 0 = haven't visited F yet, 1 = have visited F
- Start from S with state (row_S, col_S, 0)
- When you reach a food stall F, flip the visited flag to 1
- Can only reach E when visited_food_stall = 1
- Time complexity: O(r × c × 2) = O(r × c)
- Use a queue with (row, col, has_visited_food, steps)

## Related Topics

Grid Graph, BFS, State Space Search, Shortest Path with Constraints, Multi-State BFS

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int shortestPath(List<String> grid) {
        // Implementation here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        try {
            int r = sc.nextInt();
            int c = sc.nextInt();
            sc.nextLine(); // consume newline

            List<String> grid = new ArrayList<>();
            for (int i = 0; i < r; i++) {
                if (sc.hasNextLine()) {
                    String line = sc.nextLine();
                    grid.add(line);
                } else {
                    grid.add("");
                }
            }

            Solution solution = new Solution();
            int result = solution.shortestPath(grid);
            System.out.println(result);
        } finally {
            sc.close();
        }
    }
}
```

### Python

```python
import sys

def shortest_path(grid: List[List[str]]) -> int:
    # Implementation here
    return 0

def main():
    try:
        # Use splitlines to preserve row structure
        lines = sys.stdin.read().splitlines()
    except Exception:
        return

    if not lines:
        return
        
    # Wrapper to handle potential empty lines or whitespace issues
    # Filter out empty lines?
    valid_lines = [l.strip() for l in lines if l.strip()]
    if not valid_lines: return
    
    try:
        # First valid line should be r c
        header = valid_lines[0].split()
        if len(header) < 2: return
        r, c = int(header[0]), int(header[1])
        
        # Next r lines are grid
        # If valid_lines has fewer than r+1 lines, it's partial input, fixable or crash
        # Just safely grab up to r lines
        
        grid = []
        for i in range(r):
            if i + 1 < len(valid_lines):
                row_str = valid_lines[i+1]
                # Ensure we only take first c chars if line is longer? 
                # Or just list(row_str)
                grid.append(list(row_str))
            else:
                grid.append([]) # Empty row filler
                
        result = shortest_path(grid)
        print(result)
        
    except ValueError:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <tuple>

using namespace std;

class Solution {
public:
    int shortestPathWithFood(vector<vector<char>>& grid) {
        // Implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int r, c;
    cin >> r >> c;

    vector<vector<char>> grid(r, vector<char>(c));
    for (int i = 0; i < r; i++) {
        string line;
        cin >> line;
        for (int j = 0; j < c && j < line.length(); j++) {
            grid[i][j] = line[j];
        }
    }

    Solution solution;
    cout << solution.shortestPathWithFood(grid) << endl;

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  shortestPath(grid) {
    // Implementation here
    return null;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  // Filter out empty lines
  const validLines = data.filter(line => line.length > 0);

  if (validLines.length === 0) return;

  try {
    // Parse header (r c)
    const header = validLines[0].split(/\s+/);
    if (header.length < 2) return;
    const r = Number(header[0]);
    const c = Number(header[1]);

    // Parse grid - safely handle missing lines
    const grid = [];
    for (let i = 0; i < r; i++) {
      if (i + 1 < validLines.length) {
        grid.push(validLines[i+1].split(''));
      } else {
        grid.push([]); // Empty row filler for missing lines
      }
    }

      // Only run algorithm if we have a complete grid
    if (grid.length === r) {
      const solution = new Solution();
      console.log(solution.shortestPath(grid));
    }
  } catch (e) {
    // Silently handle parse errors
  }
});
```
