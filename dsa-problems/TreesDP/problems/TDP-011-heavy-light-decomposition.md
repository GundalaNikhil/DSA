---
title: "Heavy-Light Decomposition Basics"
problem_id: TDP_HEAVY_LIGHT_DECOMP__8154
display_id: TDP-011
difficulty: Medium
tags: [tree-dp, heavy-light-decomposition, path-queries, segment-tree]
slug: heavy-light-decomposition
time_limit: 2000
memory_limit: 256
---

## Problem Description

Given a weighted tree, preprocess it to answer path sum queries efficiently. Use Heavy-Light Decomposition to partition the tree into chains.

---

## Input Format

- Line 1: N (number of nodes)
- Line 2: N integers (node values)
- Next N-1 lines: u, v (edges)
- Next line: Q (number of queries)
- Next Q lines: u, v (query sum on path from u to v)

---

## Output Format

For each query, print the sum of values on the path from u to v.

---

## Examples

### Example 1

**Input:**

```
5
1 2 3 4 5
1 2
1 3
2 4
2 5
3
1 4
3 5
4 5
```

**Output:**

```
7
11
11
```

### Example 2

**Input:**

```
3
10 20 30
1 2
2 3
2
1 3
1 2
```

**Output:**

```
60
30
```

---

## Constraints

- 1 ≤ N ≤ 200,000
- 1 ≤ Q ≤ 200,000
- 1 ≤ values[i] ≤ 10^9

---

## Solution Template

### Java

```java
import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int[] values = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            values[i] = sc.nextInt();
        }

        // TODO: Implement HLD

        int q = sc.nextInt();
        for (int i = 0; i < q; i++) {
            int u = sc.nextInt(), v = sc.nextInt();
            System.out.println(0);
        }
    }
}
```

### Python

```python
def main():
    import sys
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    values = [0] + [int(data[idx + i]) for i in range(n)]
    idx += n

    # TODO: Implement HLD

    q = int(data[idx]); idx += 1
    for _ in range(q):
        u, v = int(data[idx]), int(data[idx + 1])
        idx += 2
        print(0)

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

    // TODO: Implement HLD

    int q; cin >> q;
    for (int i = 0; i < q; i++) {
        int u, v; cin >> u >> v;
        cout << 0 << "\n";
    }
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
  const n = parseInt(lines[idx++]);
  const values = [0, ...lines[idx++].split(" ").map(Number)];

  // TODO: Implement HLD

  const q = parseInt(lines[idx++]);
  for (let i = 0; i < q; i++) {
    const [u, v] = lines[idx++].split(" ").map(Number);
    console.log(0);
  }
});
```

---

## Hints

<details>
<summary>Hint 1</summary>
Partition tree into heavy chains where heavy child has largest subtree.
</details>

<details>
<summary>Hint 2</summary>
Build segment tree over chain positions for range sum queries.
</details>
