---
problem_id: REC_CAMPUS_COURSE_ORDERING__5184
display_id: REC-011
slug: campus-course-ordering
title: "Campus Course Ordering"
difficulty: Medium
difficulty_score: 55
topics:
  - Recursion
  - Backtracking
  - Graphs
tags:
  - recursion
  - topological-sort
  - backtracking
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# REC-011: Campus Course Ordering

## Problem Statement

A student must take `n` courses labeled `0` to `n-1`. You are given prerequisite pairs `(u, v)` meaning course `u` must be taken before course `v`.

List all possible valid course orderings.

![Problem Illustration](../images/REC-011/problem-illustration.png)

## Input Format

- First line: integers `n` and `m`
- Next `m` lines: two integers `u` and `v`

## Output Format

- Each valid ordering on its own line as space-separated course IDs
- Output `NONE` if no ordering exists

## Constraints

- `1 <= n <= 8`
- `0 <= m <= 15`
- Course IDs are in `[0, n-1]`

## Example

**Input:**

```
3 2
0 1
0 2
```

**Output:**

```
0 1 2
0 2 1
```

**Explanation:**

Course 0 must come before both 1 and 2, so both orders are valid.

![Example Visualization](../images/REC-011/example-1.png)

## Notes

- Use backtracking with indegree counts
- Choose any zero-indegree node at each step
- Prune if no available node exists
- Time complexity can be O(n!) in worst case

## Related Topics

Topological Sort, Backtracking, Graphs

---

## Solution Template
### Java

```java
import java.util.*;

class Solution {
    public List<Integer> findOrder(int n, int[][] edges) {
        //Implement here
        return new ArrayList<>();
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        
        int[][] edges = new int[m][2];
        for(int i=0; i<m; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
        }
        
        Solution sol = new Solution();
        List<Integer> res = sol.findOrder(n, edges);
        if(res.isEmpty()) {
            System.out.println("IMPOSSIBLE");
        } else {
            for(int i=0; i<res.size(); i++) {
                System.out.print(res.get(i) + (i==res.size()-1?"":" "));
            }
            System.out.println();
        }
        sc.close();
    }
}
```

### Python

```python
def find_topological_order(n: int, edges: list[tuple[int, int]]) -> list[int]:
    # //Implement here
    return 0

def main():
    import sys
    lines = sys.stdin.read().strip().split('\n')
    if not lines:
        return

    first = lines[0].split()
    n = int(first[0])
    m = int(first[1])

    edges = []
    for i in range(1, 1 + m):
        if i < len(lines):
            parts = lines[i].split()
            u, v = int(parts[0]), int(parts[1])
            edges.append((u, v))

    result = find_topological_order(n, edges)
    if not result:
        print("IMPOSSIBLE")
    else:
        print(" ".join(str(x) for x in result))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> findOrder(int n, const vector<pair<int, int>>& edges) {
        //Implement here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<pair<int, int>> edges(m);
    for(int i=0; i<m; i++) {
        cin >> edges[i].first >> edges[i].second;
    }

    Solution sol;
    vector<int> res = sol.findOrder(n, edges);
    if (res.empty()) {
        cout << "IMPOSSIBLE" << endl;
    } else {
        for (size_t i = 0; i < res.size(); i++) {
            cout << res[i] << (i == res.size() - 1 ? "" : " ");
        }
        cout << endl;
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require('readline');
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
let tokens = [];
rl.on('line', (line) => { tokens.push(...line.trim().split(/\s+/)); });
rl.on('close', () => {
    if(tokens.length===0) return;
    let ptr = 0;
    const n = parseInt(tokens[ptr++]);
    const m = parseInt(tokens[ptr++]);
    
    const edges = [];
    for(let i=0; i<m; i++) {
        edges.push([parseInt(tokens[ptr++]), parseInt(tokens[ptr++])]);
    }
    
    const sol = new Solution();
    const res = sol.findOrder(n, edges);
    if (res.length === 0) {
        console.log("IMPOSSIBLE");
    } else {
        console.log(res.join(" "));
    }
});

class Solution {
  findOrder(n, edges) {
    //Implement here
    return 0;
  }
}
```

