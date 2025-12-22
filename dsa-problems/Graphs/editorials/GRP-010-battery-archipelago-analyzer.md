---
problem_id: GRP_BATTERY_ARCHIPELAGO__7194
display_id: GRP-010
slug: battery-archipelago-analyzer
title: "Battery Archipelago Analyzer"
difficulty: Medium
difficulty_score: 55
topics:
  - Grid Graph
  - Connected Components
  - BFS
  - DFS
tags:
  - graph
  - grid
  - connected-components
  - bfs
  - dfs
  - medium
premium: true
subscription_tier: basic
---

# GRP-010: Battery Archipelago Analyzer

## 📋 Problem Summary

Count connected components in a grid where land cells (elevation > 0) can be connected through bridge cells (elevation = -1). Bridges allow connectivity but don't count toward component size.

## 🌍 Real-World Scenario

**Scenario Title:** Island Chain Analysis with Underwater Tunnels

Imagine analyzing a chain of islands where some islands are connected by underwater tunnels (bridges). For environmental or administrative purposes, you need to count distinct island groups and find the largest group, where tunnels connect islands but aren't counted as land themselves.

This models real scenarios like the Florida Keys connected by bridges, or Japanese islands connected by underwater tunnels - the bridges/tunnels provide connectivity without being part of the land mass.

**Why This Problem Matters:**

- **Geographic Analysis:** Counting land masses with infrastructure connections
- **Network Topology:** Analyzing connected regions with special connectors
- **Image Segmentation:** Regions connected through special pixels
- **Urban Planning:** Analyzing districts connected by transit infrastructure

![Real-World Application](../images/GRP-010/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Grid with Bridges

```
Grid (elevation values):
[2]  [-1]  [3]
[0]  [-1]  [0]
[1]  [ 0]  [4]

Land cells (>0): {(0,0)=2, (0,2)=3, (2,0)=1, (2,2)=4}
Bridge cells (-1): {(0,1), (1,1)}
Water cells (0): {(1,0), (1,2), (2,1)}

Connectivity via bridges:
- (0,0) connects to (0,2) via bridge (0,1)
- (0,2) connects to (2,2) via bridge (1,1)
- (2,0) is isolated

Components:
1. {(0,0), (0,2), (2,2)} - size 3
2. {(2,0)} - size 1

Output: 2 components, largest size = 3
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Land cells:** elevation > 0, counted in component size
- **Bridge cells:** elevation = -1, allow connectivity but not counted
- **Water cells:** elevation = 0, block connectivity
- **4-directional movement:** Up, down, left, right only

## Optimal Approach

### Algorithm

```
analyze_archipelago(grid):
    visited = [[false] * cols for _ in rows]
    components = 0
    max_size = 0
    
    for i in 0 to rows-1:
        for j in 0 to cols-1:
            if grid[i][j] > 0 and not visited[i][j]:
                size = bfs(i, j, grid, visited)
                components++
                max_size = max(max_size, size)
    
    return (components, max_size)

bfs(start_r, start_c, grid, visited):
    queue = [(start_r, start_c)]
    visited[start_r][start_c] = true
    size = 1  // Count starting land cell
    
    while queue not empty:
        (r, c) = queue.dequeue()
        
        for (dr, dc) in [(0,1), (1,0), (0,-1), (-1,0)]:
            nr, nc = r + dr, c + dc
            if valid(nr, nc) and not visited[nr][nc]:
                if grid[nr][nc] > 0:
                    // Land cell
                    visited[nr][nc] = true
                    queue.enqueue((nr, nc))
                    size++
                elif grid[nr][nc] == -1:
                    // Bridge cell - traverse but don't count
                    visited[nr][nc] = true
                    queue.enqueue((nr, nc))
    
    return size
```

### Time Complexity: **O(rows × cols)**
### Space Complexity: **O(rows × cols)**

![Algorithm Visualization](../images/GRP-010/algorithm-visualization.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    private int[][] dirs = {{0,1}, {1,0}, {0,-1}, {-1,0}};
    
    public int[] analyzeArchipelago(int[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;
        boolean[][] visited = new boolean[rows][cols];
        int components = 0;
        int maxSize = 0;
        
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] > 0 && !visited[i][j]) {
                    int size = bfs(i, j, grid, visited);
                    components++;
                    maxSize = Math.max(maxSize, size);
                }
            }
        }
        
        return new int[]{components, maxSize};
    }
    
    private int bfs(int startR, int startC, int[][] grid, boolean[][] visited) {
        int rows = grid.length;
        int cols = grid[0].length;
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{startR, startC});
        visited[startR][startC] = true;
        int size = 1;
        
        while (!queue.isEmpty()) {
            int[] curr = queue.poll();
            int r = curr[0], c = curr[1];
            
            for (int[] dir : dirs) {
                int nr = r + dir[0];
                int nc = c + dir[1];
                
                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && !visited[nr][nc]) {
                    if (grid[nr][nc] > 0) {
                        visited[nr][nc] = true;
                        queue.offer(new int[]{nr, nc});
                        size++;
                    } else if (grid[nr][nc] == -1) {
                        visited[nr][nc] = true;
                        queue.offer(new int[]{nr, nc});
                    }
                }
            }
        }
        
        return size;
    }
}
```

### Python

```python
from collections import deque
from typing import List

def analyze_archipelago(grid: List[List[int]]) -> tuple:
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    components = 0
    max_size = 0
    
    def bfs(start_r, start_c):
        queue = deque([(start_r, start_c)])
        visited[start_r][start_c] = True
        size = 1
        
        while queue:
            r, c = queue.popleft()
            
            for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                    if grid[nr][nc] > 0:
                        visited[nr][nc] = True
                        queue.append((nr, nc))
                        size += 1
                    elif grid[nr][nc] == -1:
                        visited[nr][nc] = True
                        queue.append((nr, nc))
        
        return size
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] > 0 and not visited[i][j]:
                size = bfs(i, j)
                components += 1
                max_size = max(max_size, size)
    
    return (components, max_size)
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

class Solution {
private:
    int dirs[4][2] = {{0,1}, {1,0}, {0,-1}, {-1,0}};
    
    int bfs(int startR, int startC, vector<vector<int>>& grid, vector<vector<bool>>& visited) {
        int rows = grid.size();
        int cols = grid[0].size();
        queue<pair<int,int>> q;
        q.push({startR, startC});
        visited[startR][startC] = true;
        int size = 1;
        
        while (!q.empty()) {
            auto [r, c] = q.front();
            q.pop();
            
            for (auto& dir : dirs) {
                int nr = r + dir[0];
                int nc = c + dir[1];
                
                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && !visited[nr][nc]) {
                    if (grid[nr][nc] > 0) {
                        visited[nr][nc] = true;
                        q.push({nr, nc});
                        size++;
                    } else if (grid[nr][nc] == -1) {
                        visited[nr][nc] = true;
                        q.push({nr, nc});
                    }
                }
            }
        }
        
        return size;
    }
    
public:
    pair<int,int> analyzeArchipelago(vector<vector<int>>& grid) {
        int rows = grid.size();
        int cols = grid[0].size();
        vector<vector<bool>> visited(rows, vector<bool>(cols, false));
        int components = 0;
        int maxSize = 0;
        
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] > 0 && !visited[i][j]) {
                    int size = bfs(i, j, grid, visited);
                    components++;
                    maxSize = max(maxSize, size);
                }
            }
        }
        
        return {components, maxSize};
    }
};
```

### JavaScript

```javascript
class Solution {
  analyzeArchipelago(grid) {
    const rows = grid.length;
    const cols = grid[0].length;
    const visited = Array.from({ length: rows }, () => Array(cols).fill(false));
    let components = 0;
    let maxSize = 0;
    
    const bfs = (startR, startC) => {
      const queue = [[startR, startC]];
      visited[startR][startC] = true;
      let size = 1;
      const dirs = [[0,1], [1,0], [0,-1], [-1,0]];
      
      while (queue.length > 0) {
        const [r, c] = queue.shift();
        
        for (const [dr, dc] of dirs) {
          const nr = r + dr;
          const nc = c + dc;
          
          if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && !visited[nr][nc]) {
            if (grid[nr][nc] > 0) {
              visited[nr][nc] = true;
              queue.push([nr, nc]);
              size++;
            } else if (grid[nr][nc] === -1) {
              visited[nr][nc] = true;
              queue.push([nr, nc]);
            }
          }
        }
      }
      
      return size;
    };
    
    for (let i = 0; i < rows; i++) {
      for (let j = 0; j < cols; j++) {
        if (grid[i][j] > 0 && !visited[i][j]) {
          const size = bfs(i, j);
          components++;
          maxSize = Math.max(maxSize, size);
        }
      }
    }
    
    return [components, maxSize];
  }
}
```

## 🧪 Test Case Walkthrough (Dry Run)

Grid:
```
[2]  [-1]  [3]
[0]  [-1]  [0]
[1]  [ 0]  [4]
```

BFS from (0,0):
- Visit (0,0) land, size=1
- Visit (0,1) bridge (don't count)
- Visit (0,2) land, size=2
- Visit (1,1) bridge (don't count)
- Visit (2,2) land, size=3
- Component 1: size=3

BFS from (2,0):
- Visit (2,0) land, size=1
- No unvisited neighbors
- Component 2: size=1

Result: 2 components, max size = 3

![Example Visualization](../images/GRP-010/example-1.png)

## ✅ Proof of Correctness

**Theorem:** BFS correctly identifies connected components with bridge cells.

**Proof:** BFS explores all reachable cells (land and bridges). By only counting land cells in size and starting BFS only from unvisited land cells, we correctly identify and measure each component.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Handle diagonal connectivity
- **Extension 2:** Find perimeter of each component
- **Extension 3:** Identify which components are connected by bridges
- **Extension 4:** Handle multiple bridge types with different properties

## Common Mistakes to Avoid

1. **Counting Bridge Cells in Size**
   - ❌ Wrong: Incrementing size for bridge cells
   - ✅ Correct: Only count land cells (elevation > 0)
   - **Impact:** Incorrect component sizes

2. **Not Traversing Through Bridges**
   - ❌ Wrong: Treating bridges like water (blocking)
   - ✅ Correct: Traverse bridges but don't count them
   - **Description:** Misses connected components

3. **Starting BFS from Bridges**
   - ❌ Wrong: Starting BFS from bridge cells
   - ✅ Correct: Only start from land cells
   - **Prevention:** Check `grid[i][j] > 0` before starting BFS

4. **Forgetting to Mark Bridges as Visited**
   - ❌ Wrong: Only marking land cells as visited
   - ✅ Correct: Mark both land and bridge cells as visited
   - **Description:** Infinite loops or duplicate counting

5. **Wrong Boundary Checks**
   - ❌ Wrong: Not checking grid boundaries
   - ✅ Correct: Validate `0 <= nr < rows and 0 <= nc < cols`
   - **Description:** Array index out of bounds

## Related Concepts

- **Standard Island Counting:** Without bridge cells
- **Union-Find on Grids:** Alternative approach
- **Flood Fill:** Similar BFS/DFS application
- **Perimeter Calculation:** Related grid problem
- **Image Segmentation:** Computer vision application
