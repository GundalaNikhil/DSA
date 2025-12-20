---
problem_id: GRP_LIBRARY_FIRE_EXHAUSTION__6285
display_id: GRP-011
slug: library-fire-with-exhaustion
title: "Library Fire With Exhaustion"
difficulty: Medium
difficulty_score: 55
topics:
  - Grid Graph
  - Multi-Source BFS
  - State Tracking
tags:
  - graph
  - grid
  - bfs
  - multi-source
  - simulation
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRP-011: Library Fire With Exhaustion

## Problem Statement

You are given a 2D grid representing a library where:

- `0` = empty cell
- `1` = wall (impassable)
- `2` = fire source cell

Additionally, you have a parallel stamina grid where each fire source cell has an initial stamina value (between 1 and 10).

Fire spreads as follows:

- Each minute, active fire cells spread to their 4 adjacent neighbors (up, down, left, right)
- When a fire spreads to a neighbor, the stamina value decreases by 1
- A fire cell continues spreading to neighbors while its stamina > 0
- Once stamina reaches 0, that fire cell stops spreading (but remains burning)

Your task: Compute the number of minutes until no new cells ignite. If any empty cell never catches fire, return `-1`.

![Problem Illustration](../images/GRP-011/problem-illustration.png)

## Input Format

- First line: two integers `r c` (number of rows and columns)
- Next `r` lines: `c` space-separated integers representing the grid (0=empty, 1=wall, 2=fire)
- Next `r` lines: `c` space-separated integers representing the stamina grid (positive values for fire sources, 0 elsewhere)

## Output Format

- Single integer: total minutes until no new ignitions occur, or `-1` if some empty cell never burns

## Constraints

- `1 <= r, c <= 200`
- Cell values: 0 (empty), 1 (wall), 2 (fire source)
- Stamina values: 0 to 10
- At least one fire source exists

## Example

**Input:**

```
2 2
2 0
0 0
2 0
0 0
```

**Output:**

```
2
```

**Explanation:**

Initial grid:

```
[2] [0]
[0] [0]
```

Initial stamina:

```
[2] [0]
[0] [0]
```

Minute 0: Fire at (0,0) with stamina 2
Minute 1: Fire spreads to (0,1) and (1,0), stamina becomes 1 at these new cells
Minute 2: Fire spreads from (0,1) to (1,1) and from (1,0) to (1,1), but stamina is now 0, so spreading stops

All cells have been ignited after 2 minutes.

![Example Visualization](../images/GRP-011/example-1.png)

## Notes

- Use multi-source BFS starting from all initial fire sources
- Track remaining stamina for each fire spread
- Only spread to neighbors if current stamina > 0
- Walls cannot burn
- If any empty cell remains unreached, return -1
- Time complexity: O(r × c × max_stamina)

## Related Topics

Multi-Source BFS, Grid Graph, Simulation, State Tracking, Fire Spread

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int fireSpreadTime(int[][] grid, int[][] stamina) {
        // Your implementation here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int r = sc.nextInt();
        int c = sc.nextInt();

        int[][] grid = new int[r][c];
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                grid[i][j] = sc.nextInt();
            }
        }

        int[][] stamina = new int[r][c];
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                stamina[i][j] = sc.nextInt();
            }
        }

        Solution solution = new Solution();
        System.out.println(solution.fireSpreadTime(grid, stamina));
        sc.close();
    }
}
```

### Python

```python
from collections import deque
from typing import List

def fire_spread_time(grid: List[List[int]], stamina: List[List[int]]) -> int:
    # Your implementation here
    return 0

def main():
    r, c = map(int, input().split())

    grid = []
    for _ in range(r):
        row = list(map(int, input().split()))
        grid.append(row)

    stamina = []
    for _ in range(r):
        row = list(map(int, input().split()))
        stamina.append(row)

    result = fire_spread_time(grid, stamina)
    print(result)

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
    int fireSpreadTime(vector<vector<int>>& grid, vector<vector<int>>& stamina) {
        // Your implementation here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int r, c;
    cin >> r >> c;

    vector<vector<int>> grid(r, vector<int>(c));
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            cin >> grid[i][j];
        }
    }

    vector<vector<int>> stamina(r, vector<int>(c));
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            cin >> stamina[i][j];
        }
    }

    Solution solution;
    cout << solution.fireSpreadTime(grid, stamina) << "\n";

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  fireSpreadTime(grid, stamina) {
    // Your implementation here
    return 0;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  let ptr = 0;
  const [r, c] = data[ptr++].split(" ").map(Number);

  const grid = [];
  for (let i = 0; i < r; i++) {
    const row = data[ptr++].split(" ").map(Number);
    grid.push(row);
  }

  const stamina = [];
  for (let i = 0; i < r; i++) {
    const row = data[ptr++].split(" ").map(Number);
    stamina.push(row);
  }

  const solution = new Solution();
  console.log(solution.fireSpreadTime(grid, stamina));
});
```
