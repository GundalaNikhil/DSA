---
title: "Binary Lifting for K-th Ancestor with Color Filter"
problem_id: TDP_KTH_ANCESTOR_COLOR__3741
difficulty: Medium
tags: [tree-dp, binary-lifting, ancestor-queries, color-filter]
slug: kth-ancestor-color-filter
time_limit: 2000
memory_limit: 256
---

## Problem Description

Given tree where each node has a color, answer queries: find k-th ancestor of node v with color c.

## Input Format

- Line 1: N
- Line 2: N colors
- Next N-1 lines: edges u v
- Next line: Q queries
- Next Q lines: v c k

## Output Format

For each query, print k-th ancestor with color c, or -1 if doesn't exist.

## Examples

### Example 1

**Input:**

```
5
1 2 1 2 1
1 2
1 3
2 4
2 5
3
4 2 1
5 1 2
3 1 1
```

**Output:**

```
2
1
1
```

### Example 2

**Input:**

```
3
1 1 2
1 2
2 3
2
3 1 1
3 1 2
```

**Output:**

```
2
1
```

## Constraints

- 1 ≤ N ≤ 200,000
- 1 ≤ Q ≤ 200,000
- 1 ≤ color[i] ≤ 10

## Solution Template

### Java

```java
import java.util.*;
public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] color = new int[n + 1];
        for (int i = 1; i <= n; i++) color[i] = sc.nextInt();
        // TODO: Implement
        int q = sc.nextInt();
        for (int i = 0; i < q; i++) {
            int v = sc.nextInt(), c = sc.nextInt(), k = sc.nextInt();
            System.out.println(-1);
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
    color = [0] + [int(data[idx + i]) for i in range(n)]
    idx += n
    # TODO: Implement
    q = int(data[idx + n - 1]); idx += n
    for _ in range(q):
        v, c, k = int(data[idx]), int(data[idx + 1]), int(data[idx + 2])
        idx += 3
        print(-1)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n; cin >> n;
    vector<int> color(n + 1);
    for (int i = 1; i <= n; i++) cin >> color[i];
    // TODO: Implement
    int q; cin >> q;
    while (q--) {
        int v, c, k; cin >> v >> c >> k;
        cout << -1 << "\n";
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
  const color = [0, ...lines[idx++].split(" ").map(Number)];
  // TODO: Implement
  const q = parseInt(lines[idx + n - 1]);
  idx += n;
  for (let i = 0; i < q; i++) {
    const [v, c, k] = lines[idx++].split(" ").map(Number);
    console.log(-1);
  }
});
```

## Hints

<details>
<summary>Hint 1</summary>
Use binary lifting to jump ancestors quickly.
</details>

<details>
<summary>Hint 2</summary>
Track color count along ancestor path.
</details>
