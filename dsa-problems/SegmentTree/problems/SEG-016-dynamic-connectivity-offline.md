---
problem_id: SEG_DYNAMIC_CONNECTIVITY_OFFLINE__6384
display_id: SEG-016
slug: dynamic-connectivity-offline
title: "Dynamic Connectivity Over Time (Offline)"
difficulty: Hard
difficulty_score: 78
topics:
  - Segment Tree
  - DSU Rollback
  - Offline Queries
tags:
  - segment-tree
  - dsu
  - offline
  - hard
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# SEG-016: Dynamic Connectivity Over Time (Offline)

## Problem Statement

You are given a sequence of events on an undirected graph with `n` nodes. The events are:

- `ADD u v`: add edge `(u, v)`
- `REMOVE u v`: remove edge `(u, v)`
- `QUERY u v`: ask whether `u` and `v` are connected at this time

Answer all queries in order. You must process the events offline.

![Problem Illustration](../images/SEG-016/problem-illustration.png)

## Input Format

- First line: integers `n` and `m` (number of nodes and events)
- Next `m` lines: events `ADD`, `REMOVE`, or `QUERY`

## Output Format

- For each `QUERY`, print `true` if connected, otherwise `false`

## Constraints

- `1 <= n <= 100000`
- `1 <= m <= 200000`
- `1 <= u, v <= n`

## Example

**Input:**

```
3 4
ADD 1 2
QUERY 1 2
REMOVE 1 2
QUERY 1 2
```

**Output:**

```
true
false
```

**Explanation:**

The first query is connected by edge (1,2). After removal, the nodes are disconnected.

![Example Visualization](../images/SEG-016/example-1.png)

## Notes

- Use a segment tree over time intervals
- Maintain a DSU with rollback to undo unions
- Map each edge to the active time intervals
- Process queries with depth-first traversal

## Related Topics

DSU Rollback, Offline Queries, Segment Tree

---

## Solution Template
### Java

```java
import java.util.*;

class Solution {
    public List<String> process(int n, List<String[]> events) {
        // Your implementation here
        return new ArrayList<>();
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        List<String[]> events = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            String op = sc.next();
            String u = sc.next();
            String v = sc.next();
            events.add(new String[]{op, u, v});
        }

        Solution solution = new Solution();
        List<String> out = solution.process(n, events);
        for (String line : out) System.out.println(line);
        sc.close();
    }
}
```

### Python

```python
def process(n: int, events: list[list[str]]) -> list[str]:
    # Your implementation here
    return []

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    events = []
    for _ in range(m):
        op = next(it)
        u = next(it)
        v = next(it)
        events.append([op, u, v])

    out = process(n, events)
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    vector<string> process(int n, const vector<vector<string>>& events) {
        // Your implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<vector<string>> events;
    events.reserve(m);
    for (int i = 0; i < m; i++) {
        string op, u, v;
        cin >> op >> u >> v;
        events.push_back({op, u, v});
    }

    Solution solution;
    vector<string> out = solution.process(n, events);
    for (const string& line : out) cout << line << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  process(n, events) {
    // Your implementation here
    return [];
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const m = parseInt(data[idx++], 10);
  const events = [];
  for (let i = 0; i < m; i++) {
    const op = data[idx++];
    const u = data[idx++];
    const v = data[idx++];
    events.push([op, u, v]);
  }

  const solution = new Solution();
  const out = solution.process(n, events);
  console.log(out.join("\n"));
});
```
