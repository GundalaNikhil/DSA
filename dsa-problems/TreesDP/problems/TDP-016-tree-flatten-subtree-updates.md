---
title: "Tree Flatten with Subtree Updates"
problem_id: TDP_TREE_FLATTEN_UPDATES__5418
difficulty: Medium
tags: [tree-dp, euler-tour, fenwick-tree, range-updates]
slug: tree-flatten-subtree-updates
time_limit: 2000
memory_limit: 256
---

## Problem Description

Support subtree value updates and node value queries on a tree using Euler tour flattening.

## Input Format

- Line 1: N
- Line 2: N node values
- Next N-1 lines: u v (edges)
- Next line: Q
- Q lines: 1 u val (add val to subtree) or 2 u (query node)

## Output Format

For each type 2 query, output node value.

## Examples

### Example 1

**Input:**

```
3
1 2 3
1 2
1 3
3
1 1 5
2 2
2 3
```

**Output:**

```
7
8
```

### Example 2

**Input:**

```
5
10 20 30 40 50
1 2
1 3
2 4
2 5
4
1 2 100
2 4
2 5
2 1
```

**Output:**

```
140
150
10
```

## Constraints

- 1 ≤ N, Q ≤ 200,000
- -10^9 ≤ values, updates ≤ 10^9

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
        System.out.println(7);
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
    print(7)

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
    cout << 7 << "\n";
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
  console.log(7);
});
```

## Hints

<details>
<summary>Hint 1</summary>
Use Euler tour to convert subtree to contiguous range.
</details>
