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
    public void solve(int n, int m, List<String> events) {
        // Implement here
        // For each QUERY, print "true" or "false"
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int m = sc.nextInt();
            sc.nextLine(); // consume newline
            List<String> events = new ArrayList<>();
            for (int i = 0; i < m; i++) {
                events.add(sc.nextLine());
            }
            Solution sol = new Solution();
            sol.solve(n, m, events);
        }
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def solve(self, n, m, events):
        # Implement here
        # For each QUERY, print "true" or "false"
        pass

def main_solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    first_line = list(map(int, input_data[0].split()))
    n, m = first_line[0], first_line[1]
    events = input_data[1:1+m]

    sol = Solution()
    sol.solve(n, m, events)

if __name__ == "__main__":
    main_solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    void solve(int n, int m, const vector<string>& events) {
        // Implement here
        // For each QUERY, cout << (connected ? "true" : "false") << endl;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    if (cin >> n >> m) {
        string dummy;
        getline(cin, dummy); // consume newline
        vector<string> events(m);
        for (int i = 0; i < m; i++) {
            getline(cin, events[i]);
        }

        Solution sol;
        sol.solve(n, m, events);
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  solve(n, m, events) {
    // Implement here
    // For each QUERY, console.log(connected ? "true" : "false");
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false,
});

let input = [];
rl.on("line", (line) => {
  if (line.trim()) input.push(line.trim());
}).on("close", () => {
  if (input.length < 1) return;
  const [n, m] = input[0].split(/\s+/).map(Number);
  const events = input.slice(1, 1 + m);

  const sol = new Solution();
  sol.solve(n, m, events);
});
```
