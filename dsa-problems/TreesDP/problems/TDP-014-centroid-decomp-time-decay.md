---
title: "Centroid Decomposition with Time-Decay Queries"
problem_id: TDP_CENTROID_TIME_DECAY__9247
display_id: TDP-014
difficulty: Hard
tags: [tree-dp, centroid-decomposition, time-decay, advanced]
slug: centroid-decomp-time-decay
time_limit: 2000
memory_limit: 256
---

## Problem Description

Weighted tree with node values and timestamps. Query: find minimum (distance × decay + value) to any marked node.

## Input Format

- Line 1: N D (nodes, decay constant)
- Next N-1 lines: u v w (edges)
- Next line: Q (queries)
- Q lines: type params

## Output Format

Per query output.

## Examples

### Example 1

**Input:**

```
3 1000
1 2 10
2 3 20
2
1 1 100 0
2 2 0
```

**Output:**

```
110
```

### Example 2

**Input:**

```
5 500
1 2 5
1 3 10
2 4 7
2 5 3
3
1 1 50 0
1 4 80 0
2 5 0
```

**Output:**

```
62
```

## Constraints

- 1 ≤ N ≤ 100,000
- 1 ≤ Q ≤ 100,000

## Solution Template

### Java

```java
import java.util.*;
public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), D = sc.nextInt();
        // TODO
        System.out.println(0);
    }
}
```

### Python

```python
def main():
    import sys
    data = sys.stdin.read().split()
    n, D = int(data[0]), int(data[1])
    # TODO
    print(0)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, D; cin >> n >> D;
    // TODO
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
  const [n, D] = lines[0].split(" ").map(Number);
  // TODO
  console.log(0);
});
```

## Hints

<details>
<summary>Hint 1</summary>
Use centroid decomposition for tree queries.
</details>
