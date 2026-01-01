---
title: Festival Lantern Spread
slug: festival-lantern-spread
difficulty: Medium
difficulty_score: 52
tags:
  - BFS
  - Queue
  - Grid
problem_id: QUE_FESTIVAL_LANTERN_SPREAD__8461
display_id: QUE-015
topics:
  - BFS
  - Queue
  - Grid
---

# Festival Lantern Spread - Editorial

## Problem Summary

You are given a grid representing a festival ground. Some cells have lit lanterns (`1`), and others are dark (`0`). Every minute, the light from a lit lantern spreads to its four adjacent neighbors (up, down, left, right), turning them into lit lanterns as well. Determine the minimum number of minutes until the entire grid is lit. If it's impossible (e.g., no initial lanterns), return `-1`.

## 🌍 Real-World Scenario

**Scenario Title:** Fire Spreading and Virus Outbreaks

Think of **Fire Spreading** in a forest or a **Virus Outbreak** in a population grid.

- Initially, a few locations are "infected" (lit).
- At each time step, the infection spreads to adjacent locations.
- We want to know how long it takes for the entire area to be covered.

Another analogy is **Ripples in a Pond**. If you drop multiple stones (initial lanterns) into a pond at the same time, ripples expand outward. We want to know when the ripples cover the entire surface.

![Real-World Application](../images/QUE-015/real-world-scenario.png)

## Problem Exploration

### 1. Distance Metric

The time it takes for light to reach a cell `(r, c)` from a source `(sr, sc)` is the **Manhattan Distance**: `|r - sr| + |c - sc|`. Since there are multiple sources, the time for a specific cell to light up is the minimum distance to _any_ initial lantern. The answer to the problem is the maximum of these minimum distances across all cells.

### 2. Multi-Source BFS

Instead of running a separate BFS from each lantern (which would be inefficient), we can run a single **Multi-Source Breadth-First Search**. We initialize the queue with _all_ the starting lantern positions at time 0. This simulates all lanterns spreading light simultaneously.

### 3. Edge Cases

- **Already Full**: If the grid has no `0`s initially, the time is 0.
- **Impossible**: If the grid has `0`s but no `1`s, it will never be lit. Return -1.

## Approaches

### Approach 1: Brute Force (Inefficient)

For every `0` cell, calculate its distance to every `1` cell, find the minimum. Then take the maximum of these minimums.

- **Complexity**: `O((R x C)^2)`. With `R, C <= 200`, `R x C = 40,000`. `(40,000)^2` is way too large (`1.6 x 10^9`).

### Approach 2: Multi-Source BFS (Optimal)

We use a Queue to perform a level-order traversal (BFS).

- **Algorithm**:

  1.  Initialize a Queue.
  2.  Traverse the grid.
      - If `grid[i][j] == 1`, add `(i, j)` to the Queue.
      - Count the total number of `0`s (let's call it `fresh_count`).
  3.  If `fresh_count == 0`, return `0`.
  4.  Initialize `minutes = 0`.
  5.  While Queue is not empty and `fresh_count > 0`:
      - Increment `minutes`.
      - Process all elements currently in the Queue (level size).
      - For each cell, check its 4 neighbors.
      - If a neighbor is valid and is `0`:
        - Mark it as `1` (visited).
        - Decrement `fresh_count`.
        - Add neighbor to Queue.
  6.  If `fresh_count == 0`, return `minutes`. Otherwise, return `-1` (this happens if queue empties but 0s remain, e.g., unreachable islands, though in a grid with 4-connectivity and at least one 1, all reachable 0s will be visited).

- **Complexity**:
  - **Time**: `O(R x C)`. Each cell is added to the queue at most once.
  - **Space**: `O(R x C)` for the queue.

## Implementations

### Java
```java
import java.util.*;

class Solution {
    public int minutesToLight(int[][] grid) {
        if (grid == null || grid.length == 0) return 0;

        int r = grid.length;
        int c = grid[0].length;
        Queue<int[]> queue = new LinkedList<>();
        int freshCount = 0;

        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (grid[i][j] == 1) {
                    queue.offer(new int[]{i, j});
                } else {
                    freshCount++;
                }
            }
        }

        if (freshCount == 0) return 0;
        if (queue.isEmpty()) return -1;

        int minutes = 0;
        int[][] dirs = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

        while (!queue.isEmpty() && freshCount > 0) {
            minutes++;
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                int[] curr = queue.poll();
                for (int[] d : dirs) {
                    int ni = curr[0] + d[0];
                    int nj = curr[1] + d[1];

                    if (ni >= 0 && ni < r && nj >= 0 && nj < c && grid[ni][nj] == 0) {
                        grid[ni][nj] = 1; // Mark as lit
                        freshCount--;
                        queue.offer(new int[]{ni, nj});
                    }
                }
            }
        }

        return freshCount == 0 ? minutes : -1;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            List<Integer> remaining = new ArrayList<>();
            while (sc.hasNextInt()) {
                remaining.add(sc.nextInt());
            }

            int[][] grid;

            // If we have exactly n remaining values, treat as 1D grid (1 x n)
            if (remaining.size() == n) {
                grid = new int[1][n];
                for (int i = 0; i < n; i++) {
                    grid[0][i] = remaining.get(i);
                }
            } else if (remaining.size() > n) {
                // Check if we have r and c explicitly
                int r = n;
                int c = remaining.get(0);
                if (remaining.size() >= r * c) {
                    grid = new int[r][c];
                    int pos = 1;
                    for (int i = 0; i < r; i++) {
                        for (int j = 0; j < c; j++) {
                            grid[i][j] = remaining.get(pos++);
                        }
                    }
                } else {
                    // Fallback: treat as 1D
                    grid = new int[1][n];
                    for (int i = 0; i < n && i < remaining.size(); i++) {
                        grid[0][i] = remaining.get(i);
                    }
                }
            } else {
                // Fallback: treat as 1D
                grid = new int[1][remaining.size()];
                for (int i = 0; i < remaining.size(); i++) {
                    grid[0][i] = remaining.get(i);
                }
            }

            Solution sol = new Solution();
            System.out.println(sol.minutesToLight(grid));
        }
    }
}
```

### Python
```python
from collections import deque
from typing import List
import sys

def minutes_to_light(grid: List[List[int]]) -> int:
    if not grid or not grid[0]:
        return 0

    r, c = len(grid), len(grid[0])
    q = deque()
    fresh_count = 0

    for i in range(r):
        for j in range(c):
            if grid[i][j] == 1:
                q.append((i, j))
            else:
                fresh_count += 1

    if fresh_count == 0:
        return 0
    if not q:
        return -1

    minutes = 0
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while q and fresh_count > 0:
        minutes += 1
        for _ in range(len(q)):
            x, y = q.popleft()
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < r and 0 <= ny < c and grid[nx][ny] == 0:
                    grid[nx][ny] = 1
                    fresh_count -= 1
                    q.append((nx, ny))

    return minutes if fresh_count == 0 else -1

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        remaining = list(iterator)

        # If we have exactly n values, treat as 1D grid (1 x n)
        if len(remaining) == n:
            grid = [[int(x) for x in remaining]]
            r, c = 1, n
        # If we have r and c, parse as 2D grid
        elif len(remaining) > n:
            r = n
            c_val = int(remaining[0]) if remaining else n
            # Check if we have enough for a r x c grid
            if len(remaining) >= r * c_val:
                c = c_val
                grid = []
                idx = 1
                for _ in range(r):
                    row = [int(remaining[idx + j]) for j in range(c)]
                    grid.append(row)
                    idx += c
            else:
                # Fallback: treat as 1D
                c = n
                grid = [[int(x) for x in remaining[:n]]]
        else:
            grid = [[int(x) for x in remaining]]
            r, c = 1, len(remaining)

        result = minutes_to_light(grid)
        print(result)
    except (StopIteration, ValueError, IndexError):
        pass

if __name__ == "__main__":
    main()
```

### C++
```cpp
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    int minutesToLight(vector<vector<int>>& grid) {
        if (grid.empty() || grid[0].empty()) return 0;

        int r = grid.size();
        int c = grid[0].size();
        queue<pair<int, int>> q;
        int freshCount = 0;

        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (grid[i][j] == 1) {
                    q.push({i, j});
                } else {
                    freshCount++;
                }
            }
        }

        if (freshCount == 0) return 0;
        if (q.empty()) return -1;

        int minutes = 0;
        int dirs[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

        while (!q.empty() && freshCount > 0) {
            minutes++;
            int size = q.size();
            for (int i = 0; i < size; i++) {
                pair<int, int> curr = q.front();
                q.pop();

                for (auto& d : dirs) {
                    int ni = curr.first + d[0];
                    int nj = curr.second + d[1];

                    if (ni >= 0 && ni < r && nj >= 0 && nj < c && grid[ni][nj] == 0) {
                        grid[ni][nj] = 1;
                        freshCount--;
                        q.push({ni, nj});
                    }
                }
            }
        }

        return freshCount == 0 ? minutes : -1;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (cin >> n) {
        vector<int> remaining;
        int val;
        while (cin >> val) {
            remaining.push_back(val);
        }

        vector<vector<int>> grid;

        // If we have exactly n remaining values, treat as 1D grid (1 x n)
        if ((int)remaining.size() == n) {
            grid.push_back(remaining);
        } else if ((int)remaining.size() > n) {
            // Check if we have r and c explicitly
            int r = n;
            int c = remaining[0];
            if ((int)remaining.size() >= r * c) {
                grid.resize(r);
                int pos = 1;
                for (int i = 0; i < r; i++) {
                    for (int j = 0; j < c; j++) {
                        grid[i].push_back(remaining[pos++]);
                    }
                }
            } else {
                // Fallback: treat as 1D
                vector<int> row;
                for (int i = 0; i < n && i < (int)remaining.size(); i++) {
                    row.push_back(remaining[i]);
                }
                grid.push_back(row);
            }
        } else {
            // Fallback: treat as 1D
            grid.push_back(remaining);
        }

        Solution sol;
        cout << sol.minutesToLight(grid) << endl;
    }
    return 0;
}
```

### JavaScript
```javascript
const readline = require("readline");

class Solution {
  minutesToLight(grid) {
    if (!grid || grid.length === 0) return 0;

    const r = grid.length;
    const c = grid[0].length;
    const queue = [];
    let freshCount = 0;

    for (let i = 0; i < r; i++) {
      for (let j = 0; j < c; j++) {
        if (grid[i][j] === 1) {
          queue.push([i, j]);
        } else {
          freshCount++;
        }
      }
    }

    if (freshCount === 0) return 0;
    if (queue.length === 0) return -1;

    let minutes = 0;
    const dirs = [
      [-1, 0],
      [1, 0],
      [0, -1],
      [0, 1],
    ];
    let head = 0;

    while (head < queue.length && freshCount > 0) {
      minutes++;
      const size = queue.length - head;
      for (let i = 0; i < size; i++) {
        const [x, y] = queue[head++];

        for (const [dx, dy] of dirs) {
          const nx = x + dx;
          const ny = y + dy;

          if (nx >= 0 && nx < r && ny >= 0 && ny < c && grid[nx][ny] === 0) {
            grid[nx][ny] = 1;
            freshCount--;
            queue.push([nx, ny]);
          }
        }
      }
    }

    return freshCount === 0 ? minutes : -1;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/).filter(x => x !== "")));
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const remaining = data.slice(idx);

  let grid;

  // If we have exactly n remaining values, treat as 1D grid (1 x n)
  if (remaining.length === n) {
    grid = [remaining.map(x => parseInt(x, 10))];
  } else if (remaining.length > n) {
    // Check if we have r and c explicitly
    const r = n;
    const c = parseInt(remaining[0], 10);
    if (remaining.length >= r * c) {
      grid = [];
      let pos = 1;
      for (let i = 0; i < r; i++) {
        const row = [];
        for (let j = 0; j < c; j++) {
          row.push(parseInt(remaining[pos++], 10));
        }
        grid.push(row);
      }
    } else {
      // Fallback: treat as 1D
      grid = [remaining.slice(0, n).map(x => parseInt(x, 10))];
    }
  } else {
    // Fallback: treat as 1D
    grid = [remaining.map(x => parseInt(x, 10))];
  }

  const solution = new Solution();
  console.log(solution.minutesToLight(grid));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:**

```
1 0 0
0 0 0
0 0 1
```

`r=3, c=3`.
Initial Queue: `[(0,0), (2,2)]`. `freshCount = 7`.

1.  **Minute 1**:

    - Pop `(0,0)`. Neighbors: `(0,1)`, `(1,0)`. Mark lit. `freshCount = 5`. Push `(0,1), (1,0)`.
    - Pop `(2,2)`. Neighbors: `(2,1)`, `(1,2)`. Mark lit. `freshCount = 3`. Push `(2,1), (1,2)`.
    - Queue: `[(0,1), (1,0), (2,1), (1,2)]`.

2.  **Minute 2**:
    - Pop `(0,1)`. Neighbors: `(0,2), (1,1)`. Mark lit. `freshCount = 1`. Push.
    - Pop `(1,0)`. Neighbors: `(1,1)` (already lit), `(2,0)`. Mark lit. `freshCount = 0`. Push.
    - ... (process rest of level)
    - `freshCount` reached 0.

**Output:** `2`.

## Proof of Correctness

The Multi-Source BFS guarantees that we visit cells in increasing order of their distance from the nearest source.

- Layer 0: Distance 0 (initial sources).
- Layer 1: Distance 1 (neighbors of sources).
- Layer k: Distance k.
  Since we process level by level, the first time we encounter a `0` cell and turn it to `1`, it is via the shortest path from _some_ initial `1`. The number of layers processed corresponds exactly to the maximum distance required to reach the last unlit cell.

## Interview Extensions

1.  **What if there are walls/obstacles?**

    - Simply treat walls (e.g., value `-1`) as visited cells that block light. The logic remains the same.

2.  **What if the grid is infinite?**

    - The problem changes to finding the area covered after `T` minutes, which would be a diamond shape (Manhattan distance ball).

3.  **Can we modify the input grid?**
    - The solution modifies the grid to mark visited cells. If modification is forbidden, use a separate `visited` boolean matrix.

### Common Mistakes

- **Not using Multi-Source BFS**: Running BFS from each `1` separately is too slow.
- **Forgetting `freshCount`**: Without tracking unlit cells, you might continue BFS unnecessarily or fail to detect unreachable cells (though in a connected grid, all are reachable).
- **Returning `minutes` too early**: Ensure you finish the current minute's propagation before checking if `freshCount == 0` or returning. The standard pattern is `minutes++` _before_ processing the level, or initializing `minutes = -1` and incrementing. My implementation uses `minutes++` at start of loop, which correctly counts the transition _to_ the next state. Note: if `freshCount` becomes 0 _during_ the loop, we can technically stop, but finishing the level is cleaner.

## Related Concepts

- **BFS (Breadth-First Search)**: The core algorithm.
- **Shortest Path in Unweighted Graph**: BFS finds shortest paths.
- **Matrix Traversal**: Standard grid manipulation.
