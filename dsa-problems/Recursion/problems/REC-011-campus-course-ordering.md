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
    public List<List<Integer>> allOrderings(int n, int[][] edges) {
        // Your implementation here
        return new ArrayList<>();
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[][] edges = new int[m][2];
        for (int i = 0; i < m; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
        }

        Solution solution = new Solution();
        List<List<Integer>> result = solution.allOrderings(n, edges);
        if (result.isEmpty()) {
            System.out.println("NONE");
        } else {
            for (List<Integer> order : result) {
                StringBuilder sb = new StringBuilder();
                for (int i = 0; i < order.size(); i++) {
                    if (i > 0) sb.append(' ');
                    sb.append(order.get(i));
                }
                System.out.println(sb.toString());
            }
        }
        sc.close();
    }
}
```

### Python

```python
def all_orderings(n: int, edges: list[tuple[int, int]]) -> list[list[int]]:
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
    edges = [(int(next(it)), int(next(it))) for _ in range(m)]

    result = all_orderings(n, edges)
    if not result:
        print("NONE")
    else:
        for order in result:
            print(" ".join(str(x) for x in order))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> allOrderings(int n, const vector<pair<int,int>>& edges) {
        // Your implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<pair<int,int>> edges(m);
    for (int i = 0; i < m; i++) {
        cin >> edges[i].first >> edges[i].second;
    }

    Solution solution;
    vector<vector<int>> result = solution.allOrderings(n, edges);
    if (result.empty()) {
        cout << "NONE\n";
    } else {
        for (const auto& order : result) {
            for (int i = 0; i < (int)order.size(); i++) {
                if (i) cout << ' ';
                cout << order[i];
            }
            cout << "\n";
        }
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  allOrderings(n, edges) {
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
  const edges = [];
  for (let i = 0; i < m; i++) {
    const u = parseInt(data[idx++], 10);
    const v = parseInt(data[idx++], 10);
    edges.push([u, v]);
  }

  const solution = new Solution();
  const result = solution.allOrderings(n, edges);
  if (result.length === 0) {
    console.log("NONE");
  } else {
    console.log(result.map((order) => order.join(" ")).join("\n"));
  }
});
```
