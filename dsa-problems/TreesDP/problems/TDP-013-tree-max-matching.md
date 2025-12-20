---
title: "DP on Tree for Maximum Matching"
problem_id: TDP_TREE_MAX_MATCHING__6183
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
public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
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
    n = int(data[0])
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
    int n; cin >> n;
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
  const n = parseInt(lines[0]);
  // TODO
  console.log(0);
});
```

## Hints

<details>
<summary>Hint 1</summary>
Use DP with states: node matched vs unmatched.
</details>
