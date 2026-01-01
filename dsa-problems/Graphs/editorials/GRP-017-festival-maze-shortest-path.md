---
problem_id: GRP_FESTIVAL_MAZE_SHORTEST__7418
display_id: GRP-017
slug: festival-maze-shortest-path
title: Festival Maze Shortest Path
difficulty: Medium
difficulty_score: 55
topics:
- State-Space Search
- BFS
- Shortest Path with Constraints
tags:
- graph
- bfs
- state-space
- shortest-path
- constraints
- hard
premium: true
subscription_tier: premium
---
# GRP-017: Festival Maze Shortest Path

## 📋 Problem Summary

Find shortest path in a grid maze where you can pass through at most K walls. Use state-space BFS where each state is (row, col, walls_remaining). Return minimum steps to reach destination or -1 if impossible.

## 🌍 Real-World Scenario

**Scenario Title:** Emergency Route Planning with Obstacles

Imagine planning an emergency evacuation route through a city where you can break through K barriers (walls) if necessary. You need the shortest path considering you have limited barrier-breaking capacity.

State-space BFS models this by tracking position AND remaining capacity. Each state represents a unique situation (location + resources), allowing optimal pathfinding with constraints. This applies to robotics, game AI, and resource-constrained navigation.

**Why This Problem Matters:**

- **Emergency Planning:** Routes with limited obstacle removal
- **Game AI:** Pathfinding with abilities (teleports, wall-breaks)
- **Robotics:** Navigation with limited battery/fuel
- **Network Routing:** Paths with limited relay hops

![Real-World Application](../images/GRP-017/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: State-Space BFS

```
Grid (0=empty, 1=wall):
[0] [1] [0]
[0] [1] [0]
[0] [0] [0]

Start: (0,0), End: (2,2), K=1

State space:
(0,0,1) → (1,0,1) → (2,0,1) → (2,1,1) → (2,2,1)
       ↘ (0,1,0) → (0,2,0) → (1,2,0) → (2,2,0)

Shortest path: 4 steps (breaking 1 wall)
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **State:** (row, col, walls_remaining)
- **Transition:** Move to adjacent cell, decrement walls_remaining if wall
- **Goal:** Reach destination with any walls_remaining ≥ 0
- **BFS guarantee:** First time reaching destination = shortest path

## Optimal Approach

### Algorithm

```
shortest_path_with_walls(grid, k):
    rows, cols = len(grid), len(grid[0])
    if (0,0) == (rows-1, cols-1):
        return 0
    
    queue = [(0, 0, k, 0)]  // (row, col, walls_left, steps)
    visited = {(0, 0, k)}
    
    while queue not empty:
        (r, c, walls, steps) = queue.dequeue()
        
        for (dr, dc) in [(0,1), (1,0), (0,-1), (-1,0)]:
            nr, nc = r + dr, c + dc
            
            if not valid(nr, nc):
                continue
            
            new_walls = walls - grid[nr][nc]
            
            if new_walls >= 0 and (nr, nc, new_walls) not in visited:
                if (nr, nc) == (rows-1, cols-1):
                    return steps + 1
                
                visited.add((nr, nc, new_walls))
                queue.enqueue((nr, nc, new_walls, steps + 1))
    
    return -1
```

### Time Complexity: **O(rows × cols × K)**
### Space Complexity: **O(rows × cols × K)**

![Algorithm Visualization](../images/GRP-017/algorithm-visualization.png)

## Implementations

### Java
```java
import java.util.*;

class Solution {
    private int[][] dirs = {{0,1}, {1,0}, {0,-1}, {-1,0}};

    public int shortestPath(List<String> grid) {
        if (grid == null || grid.isEmpty()) return -1;

        int rows = grid.size();
        int cols = grid.get(0).length();

        if (rows == 0 || cols == 0) return -1;
        if (rows == 1 && cols == 1) return 0;

        // Find start and end
        int startR = -1, startC = -1, endR = -1, endC = -1;
        int foodR = -1, foodC = -1;
        boolean hasFood = false;

        for (int i = 0; i < rows; i++) {
            String row = grid.get(i);
            for (int j = 0; j < Math.min(row.length(), cols); j++) {
                char cell = row.charAt(j);
                if (cell == 'S') {
                    startR = i;
                    startC = j;
                } else if (cell == 'E') {
                    endR = i;
                    endC = j;
                } else if (cell == 'F') {
                    foodR = i;
                    foodC = j;
                    hasFood = true;
                }
            }
        }

        if (startR == -1 || endR == -1) return -1;

        // BFS with state (r, c, has_visited_food)
        Queue<int[]> queue = new LinkedList<>();
        Set<String> visited = new HashSet<>();

        queue.offer(new int[]{startR, startC, 0, 0}); // r, c, has_food, dist
        visited.add(startR + "," + startC + ",0");

        while (!queue.isEmpty()) {
            int[] curr = queue.poll();
            int r = curr[0], c = curr[1], foodState = curr[2], dist = curr[3];

            // Check if at end with food
            if (r == endR && c == endC && foodState == 1) {
                return dist;
            }

            for (int[] dir : dirs) {
                int nr = r + dir[0];
                int nc = c + dir[1];

                if (nr < 0 || nr >= rows || nc < 0 || nc >= cols) continue;

                String cell = grid.get(nr);
                if (nc >= cell.length()) continue;

                char cellChar = cell.charAt(nc);
                if (cellChar == '#') continue;

                int newFoodState = foodState;
                if (cellChar == 'F') {
                    newFoodState = 1;
                }

                String key = nr + "," + nc + "," + newFoodState;
                if (!visited.contains(key)) {
                    visited.add(key);
                    queue.offer(new int[]{nr, nc, newFoodState, dist + 1});
                }
            }
        }

        return -1;
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
sys.setrecursionlimit(200000)
from collections import deque
from typing import List

def shortest_path(grid: List[List[str]]) -> int:
    if not grid: return -1
    rows, cols = len(grid), len(grid[0])
    
    start = None
    
    for i in range(rows):
        if len(grid[i]) != cols:
             # Handle jagged/inconsistent rows by skipping or erroring?
             # For now, let's just avoid crashing if possible, or assume valid input logic
             # But if loop goes to 'cols', we crash.
             # We should probably robustly find S/E/F even if jagged.
             pass
             
        for j in range(min(len(grid[i]), cols)):
            if grid[i][j] == 'S':
                start = (i, j)
    
    if not start: return -1
    
    # State: (r, c, visited_food)
    queue = deque([(start[0], start[1], 0, 0)]) # r, c, has_food, dist
    visited = set([(start[0], start[1], 0)])
    
    while queue:
        r, c, has_food, dist = queue.popleft()
        
        # Check current cell type - robust check
        if r >= rows or c >= len(grid[r]): continue
        
        cell = grid[r][c]
        
        current_has_food = 1 if cell == 'F' or has_food else 0
        
        if cell == 'E' and current_has_food:
            return dist

        for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols: # Bound checkout based on theoretical cols
                 # And actual check
                 if nc < len(grid[nr]) and grid[nr][nc] != '#':
                    if (nr, nc, current_has_food) not in visited:
                        visited.add((nr, nc, current_has_food))
                        queue.append((nr, nc, current_has_food, dist + 1))
                    
    return -1

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
#include <string>
using namespace std;

class Solution {
private:
    int dirs[4][2] = {{0,1}, {1,0}, {0,-1}, {-1,0}};

public:
    int shortestPathWithFood(vector<vector<char>>& grid) {
        int rows = grid.size();
        if (rows == 0) return -1;
        int cols = grid[0].size();

        int startR = -1, startC = -1;

        // Find starting position
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == 'S') {
                    startR = i;
                    startC = j;
                    break;
                }
            }
            if (startR != -1) break;
        }

        if (startR == -1) return -1;

        // State: (r, c, has_food, steps)
        queue<tuple<int,int,int,int>> q;
        set<tuple<int,int,int>> visited;

        q.push({startR, startC, 0, 0});
        visited.insert({startR, startC, 0});

        while (!q.empty()) {
            auto [r, c, hasFood, steps] = q.front();
            q.pop();

            int currentFood = hasFood;
            if (grid[r][c] == 'F') {
                currentFood = 1;
            }

            if (grid[r][c] == 'E' && currentFood) {
                return steps;
            }

            for (auto& dir : dirs) {
                int nr = r + dir[0];
                int nc = c + dir[1];

                if (nr < 0 || nr >= rows || nc < 0 || nc >= cols) continue;
                if (grid[nr][nc] == '#') continue;

                if (visited.find({nr, nc, currentFood}) == visited.end()) {
                    visited.insert({nr, nc, currentFood});
                    q.push({nr, nc, currentFood, steps + 1});
                }
            }
        }

        return -1;
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
    if (!grid || grid.length === 0) return -1;

    const rows = grid.length;
    const cols = grid[0].length;

    let start = null;

    // Find starting position
    for (let i = 0; i < rows; i++) {
      for (let j = 0; j < cols; j++) {
        if (grid[i][j] === 'S') {
          start = [i, j];
          break;
        }
      }
      if (start) break;
    }

    if (!start) return -1;

    // State: [r, c, hasFood, dist]
    const queue = [[start[0], start[1], 0, 0]];
    const visited = new Set([`${start[0]},${start[1]},0`]);
    const dirs = [[0,1], [1,0], [0,-1], [-1,0]];

    while (queue.length > 0) {
      const [r, c, hasFood, dist] = queue.shift();

      // Check current cell
      if (r < 0 || r >= rows || c < 0 || c >= cols) continue;

      const cell = grid[r][c];
      const currentHasFood = (cell === 'F' || hasFood) ? 1 : 0;

      // Check if reached exit with food
      if (cell === 'E' && currentHasFood) {
        return dist;
      }

      // Explore neighbors
      for (const [dr, dc] of dirs) {
        const nr = r + dr;
        const nc = c + dc;

        if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] !== '#') {
          const key = `${nr},${nc},${currentHasFood}`;
          if (!visited.has(key)) {
            visited.add(key);
            queue.push([nr, nc, currentHasFood, dist + 1]);
          }
        }
      }
    }

    return -1;
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

## 🧪 Test Case Walkthrough (Dry Run)

Grid: `[[0,1,0],[0,1,0],[0,0,0]]`, K=1

| Step | Queue | Visited States | Action |
|-----:|:------|:---------------|:-------|
| 0 | [(0,0,1,0)] | {(0,0,1)} | Start |
| 1 | [(1,0,1,1),(0,1,0,1)] | {(0,0,1),(1,0,1),(0,1,0)} | Explore from (0,0) |
| 2 | [(0,1,0,1),(2,0,1,2)] | {(0,0,1),(1,0,1),(0,1,0),(2,0,1)} | Explore from (1,0) |
| 3 | [(2,0,1,2),(0,2,0,2)] | {(0,0,1),(1,0,1),(0,1,0),(2,0,1),(0,2,0)} | Explore from (0,1) |
| 4 | [(0,2,0,2),(2,1,1,3)] | Add (2,1,1) | Explore from (2,0) |
| 5 | [(2,1,1,3),(1,2,0,3)] | Add (1,2,0) | Explore from (0,2) |
| 6 | [(1,2,0,3),(2,2,1,4)] | Reach (2,2)! | Return 4 |

Answer: 4

![Example Visualization](../images/GRP-017/example-1.png)

## ✅ Proof of Correctness

**Theorem:** State-space BFS finds shortest path with constraints.

**Proof:** BFS explores states in increasing order of steps. Each state (r,c,k) is unique. First time reaching destination = shortest path for that state configuration.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Return the actual path, not just length
- **Extension 2:** Handle different costs for breaking walls
- **Extension 3:** Multiple types of obstacles with different K values
- **Extension 4:** Bidirectional BFS for optimization

### Common Mistakes to Avoid

1. **Wrong State Representation**
   - ❌ Wrong: Only tracking (row, col)
   - ✅ Correct: Track (row, col, walls_remaining)
   - **Impact:** Incorrect shortest path

2. **Not Checking Walls Remaining**
   - ❌ Wrong: Allowing negative walls_remaining
   - ✅ Correct: Only proceed if new_walls >= 0
   - **Description:** Violates constraint

3. **Visiting Same State Multiple Times**
   - ❌ Wrong: Only checking (row, col) in visited
   - ✅ Correct: Check (row, col, walls_remaining) in visited
   - **Prevention:** Different wall counts = different states

4. **Early Termination at Wrong State**
   - ❌ Wrong: Returning when reaching destination with any K
   - ✅ Correct: Return first time reaching destination (BFS guarantees shortest)
   - **Description:** BFS naturally finds shortest path

5. **Not Handling Start == End**
   - ❌ Wrong: Not checking if start is destination
   - ✅ Correct: Return 0 if start == destination
   - **Description:** Edge case

## Related Concepts

- **Standard BFS:** Without state tracking
- **Dijkstra with State:** Weighted version
- **A* Search:** Heuristic-guided state-space search
- **Dynamic Programming:** Alternative for some constraint problems
- **Multi-dimensional BFS:** General state-space technique
