---
title: "DP on Tree for Maximum Matching"
problem_id: TDP_TREE_MAX_MATCHING__6183
display_id: TDP-013
difficulty: Medium
tags: [tree-dp, matching, graph-theory]
slug: tree-max-matching
time_limit: 2000
memory_limit: 256
---

## Problem Description

Find maximum matching in a tree. A matching is a set of edges with no shared vertices.

## Input Format

- Line 1: N
- Next N-1 lines: u v (edges)

## Output Format

Maximum matching size.

## Examples

### Example 1

**Input:**

```
4
1 2
2 3
3 4
```

**Output:**

```
2
```

### Example 2

**Input:**

```
7
1 2
1 3
2 4
2 5
3 6
3 7
```

**Output:**

```
3
```

## Constraints

- 1 ≤ N ≤ 200,000

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int maxMatching(int n, int[][] edges) {
        // Implement here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();

        int[][] edges = new int[n - 1][2];
        for (int i = 0; i < n - 1; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
        }

        Solution solution = new Solution();
        System.out.println(solution.maxMatching(n, edges));
    }
}
```

### Python

```python
from typing import List
import sys

sys.setrecursionlimit(200000)

class Solution:
    def max_matching(self, n: int, edges: List[List[int]]) -> int:
        # Implement here
        return 0

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))

        edges = []
        for _ in range(n - 1):
            u = int(next(iterator))
            v = int(next(iterator))
            edges.append([u, v])

        solution = Solution()
        print(solution.max_matching(n, edges))
    except StopIteration:
        pass

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
public:
    int maxMatching(int n, const vector<vector<int>>& edges) {
        // Implement here
        return 0;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    if (!(cin >> n)) return 0;

    vector<vector<int>> edges(n - 1, vector<int>(2));
    for (int i = 0; i < n - 1; i++) {
        cin >> edges[i][0] >> edges[i][1];
    }

    Solution solution;
    cout << solution.maxMatching(n, edges) << endl;

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  maxMatching(n, edges) {
    // Implement here
    return 0;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const lines = [];
rl.on("line", (line) => {
  lines.push(line);
}).on("close", () => {
  const tokens = lines
    .join(" ")
    .split(/\s+/)
    .filter((t) => t !== "");
  if (tokens.length === 0) return;

  let idx = 0;
  const n = parseInt(tokens[idx++]);

  const edges = [];
  for (let i = 0; i < n - 1; i++) {
    const u = parseInt(tokens[idx++]);
    const v = parseInt(tokens[idx++]);
    edges.push([u, v]);
  }

  const solution = new Solution();
  console.log(solution.maxMatching(n, edges));
});
```

## Hints

<details>
<summary>Hint 1</summary>
Use DP with states: node matched vs unmatched.
</details>
