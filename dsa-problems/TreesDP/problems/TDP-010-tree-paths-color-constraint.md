---
title: "Tree Paths with Forbidden Colors"
problem_id: TDP_PATH_COLOR_CONSTRAINT__4927
difficulty: Medium
tags: [tree-dp, path-counting, color-constraint, dfs]
slug: tree-paths-color-constraint
time_limit: 2000
memory_limit: 256
---

## Problem Description

Given a tree with N nodes where each node has a color (1 to C), count the number of unordered pairs of nodes at exactly distance K where the path between them does NOT pass through any node with the forbidden color F.

---

## Input Format

- First line: N, K, F (nodes, target distance, forbidden color)
- Second line: N integers representing colors of nodes 1 to N
- Next N-1 lines: u, v (edges)

---

## Output Format

Print the count of valid node pairs.

---

## Examples

### Example 1

**Input:**

```
4 2 2
1 2 1 3
1 2
2 3
3 4
```

**Output:**

```
1
```

**Explanation:** Only pair (1,3) at distance 2, path avoids color 2... Actually node 2 has color 2, so path 1-2-3 is invalid. Only valid pair needs rechecking.

### Example 2

**Input:**

```
5 3 2
1 1 2 1 1
1 2
2 3
3 4
4 5
```

**Output:**

```
1
```

---

## Constraints

- 1 ≤ N ≤ 200,000
- 1 ≤ K ≤ 100,000
- 1 ≤ C ≤ 10
- 1 ≤ F ≤ C

---

## Solution Template

### Java

```java
import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), K = sc.nextInt(), F = sc.nextInt();

        int[] color = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            color[i] = sc.nextInt();
        }

        // TODO: Implement path counting with color filter

        System.out.println(0);
    }
}
```

### Python

```python
import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    n, K, F = int(data[idx]), int(data[idx+1]), int(data[idx+2])
    idx += 3

    color = [0] + [int(data[idx + i]) for i in range(n)]
    idx += n

    # TODO: Implement path counting with color filter

    print(0)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, K, F;
    cin >> n >> K >> F;

    vector<int> color(n + 1);
    for (int i = 1; i <= n; i++) cin >> color[i];

    // TODO: Implement path counting with color filter

    cout << 0 << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");
const rl = readline.createInterface({ input: process.stdin, terminal: false });

const lines = [];
rl.on("line", (line) => lines.push(line.trim()));
rl.on("close", () => {
  let idx = 0;
  const [n, K, F] = lines[idx++].split(" ").map(Number);
  const color = [0, ...lines[idx++].split(" ").map(Number)];

  // TODO: Implement path counting with color filter

  console.log(0);
});
```

---

## Hints

<details>
<summary>Hint 1</summary>
Use DP with state tracking: dp[node][distance][hasForbidden]
</details>

<details>
<summary>Hint 2</summary>
During DFS, merge child contributions to count valid pairs at distance K
</details>
