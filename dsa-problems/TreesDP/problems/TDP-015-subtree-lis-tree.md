---
title: "DP for Subtree LIS on Tree"
problem_id: TDP_SUBTREE_LIS__7392
display_id: TDP-015
difficulty: Hard
tags: [tree-dp, lis, coordinate-compression, fenwick]
slug: subtree-lis-tree
time_limit: 2000
memory_limit: 256
---

## Problem Description

For each node, compute LIS length of values along root-to-node path.

## Input Format

- Line 1: N
- Line 2: N node values
- Next N-1 lines: u v (edges)

## Output Format

N integers: LIS length for each node's root path.

## Examples

### Example 1

**Input:**

```
3
2 1 3
1 2
1 3
```

**Output:**

```
1 1 2
```

### Example 2

**Input:**

```
5
1 5 2 4 3
1 2
1 3
2 4
2 5
```

**Output:**

```
1 2 2 3 3
```

## Constraints

- 1 ≤ N ≤ 200,000
- 1 ≤ values[i] ≤ 10^9

## Solution Template

### Java

```java
import java.util.*;
public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] values = new int[n + 1];
        for (int i = 1; i <= n; i++) values[i] = sc.nextInt();
        // TODO
        System.out.println("1 1 2");
    }
}
```

### Python

```python
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    values = [0] + [int(data[1 + i]) for i in range(n)]
    # TODO
    print("1 1 2")

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n; cin >> n;
    vector<int> values(n + 1);
    for (int i = 1; i <= n; i++) cin >> values[i];
    // TODO
    cout << "1 1 2\n";
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
  const n = parseInt(lines[0]);
  const values = [0, ...lines[1].split(" ").map(Number)];
  // TODO
  console.log("1 1 2");
});
```

## Hints

<details>
<summary>Hint 1</summary>
Use DFS with LIS data structure that supports add/remove.
</details>
