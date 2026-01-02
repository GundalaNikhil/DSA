---
problem_id: GRP_COURSE_PLAN_MANDATORY__5183
display_id: GRP-007
slug: course-plan-mandatory-pairs
title: "Course Plan with Mandatory Pairs"
difficulty: Medium
difficulty_score: 55
topics:
  - Topological Sort
  - Directed Acyclic Graph
  - Graph Contraction
tags:
  - graph
  - topological-sort
  - dag
  - scheduling
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRP-007: Course Plan with Mandatory Pairs

## Problem Statement

You are given `n` courses (numbered 0 to n-1) with prerequisite relationships forming a Directed Acyclic Graph (DAG). Additionally, you have pairs of courses that must appear adjacent to each other (in any order) in the final schedule.

Produce a topological ordering of courses that:
1. Respects all prerequisite constraints (if A is a prerequisite of B, A must come before B)
2. Ensures that for each mandatory pair (u, v), courses u and v are adjacent in the final ordering

Return the valid schedule as a list of course numbers. If no valid schedule exists, return an empty list.

![Problem Illustration](../images/GRP-007/problem-illustration.png)

## Input Format

- First line: integer `n` (number of courses)
- Second line: integer `m` (number of prerequisite edges)
- Next `m` lines: two integers `u v` representing "course u must be taken before course v"
- Next line: integer `p` (number of mandatory adjacent pairs)
- Next `p` lines: two integers `a b` representing "courses a and b must be adjacent in the schedule"

## Output Format

- If valid ordering exists: space-separated integers representing the course schedule
- If no valid ordering exists: print `-1`

## Constraints

- `1 <= n <= 10^5`
- `0 <= m <= 2*10^5`
- `0 <= p <= 10^5`
- `0 <= u, v, a, b < n`
- The prerequisite graph is guaranteed to be a DAG (no cycles)

## Example

**Input:**
```
4
2
0 2
1 2
1
2 3
```

**Output:**
```
0 1 2 3
```

**Explanation:**

Prerequisites:
- Course 0 must come before course 2
- Course 1 must come before course 2

Mandatory adjacent pair:
- Courses 2 and 3 must be adjacent

One valid ordering is: [0, 1, 2, 3]
- Satisfies 0 → 2 (0 before 2)
- Satisfies 1 → 2 (1 before 2)
- Courses 2 and 3 are adjacent

Another valid ordering would be: [1, 0, 2, 3]

![Example Visualization](../images/GRP-007/example-1.png)

## Notes

- First, verify that prerequisite constraints allow the adjacency pairs (e.g., if A must come before both B and C, then B and C cannot be in an adjacency pair unless one depends on the other)
- One approach: contract each adjacency pair into a super-node, then run topological sort on the contracted graph
- When expanding super-nodes back to individual courses, ensure the pair ordering respects prerequisites
- Use Kahn's algorithm or DFS-based topological sort
- Time complexity: O(n + m + p)

## Related Topics

Topological Sort, DAG, Graph Contraction, Scheduling, Kahn's Algorithm

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    private int[] parent;

    public List<Integer> courseSchedule(int n, List<int[]> prerequisites, List<int[]> pairs) {
        return null;
    }

    private int find(int x) {
        return 0;
    }

    private void union(int x, int y) {
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();

        List<int[]> prerequisites = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            prerequisites.add(new int[]{u, v});
        }

        // Handle optional pairs input
        List<int[]> pairs = new ArrayList<>();
        if (sc.hasNextInt()) {
            int p = sc.nextInt();
            for (int i = 0; i < p; i++) {
                if (sc.hasNextInt()) {
                    int a = sc.nextInt();
                    if (sc.hasNextInt()) {
                        int b = sc.nextInt();
                        pairs.add(new int[]{a, b});
                    }
                }
            }
        }

        Solution solution = new Solution();
        List<Integer> result = solution.courseSchedule(n, prerequisites, pairs);

        if (result.isEmpty()) {
            System.out.println(-1);
        } else {
            for (int i = 0; i < result.size(); i++) {
                System.out.print(result.get(i));
                if (i < result.size() - 1) System.out.print(" ");
            }
            System.out.println();
        }
        sc.close();
    }
}
```

### Python

```python
import sys
sys.setrecursionlimit(200000)
from typing import List, Tuple
from collections import defaultdict, deque

def course_schedule(n: int, prerequisites: List[Tuple[int, int]], pairs: List[Tuple[int, int]]) -> List[int]:
    return []
def main():
    try:
        input_data = sys.stdin.read().split()
    except Exception:
        return

    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        
        prerequisites = []
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            prerequisites.append((u, v))
        
        # Handle optional pairs input
        try:
            p = int(next(iterator))
            pairs = []
            for _ in range(p):
                a = int(next(iterator))
                b = int(next(iterator))
                pairs.append((a, b))
        except StopIteration:
            pairs = []
            
        result = course_schedule(n, prerequisites, pairs)
        
        if not result:
            print(-1)
        else:
            print(' '.join(map(str, result)))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
using namespace std;

class Solution {
private:
    vector<int> parent;

    int find(int x) {
        return 0;
    }

    void unionNodes(int x, int y) {
    }

public:
    vector<int> courseSchedule(int n, vector<pair<int,int>>& prerequisites, vector<pair<int,int>>& pairs) {
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    vector<pair<int,int>> prerequisites;
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        prerequisites.push_back({u, v});
    }

    int p = 0;
    cin >> p;
    vector<pair<int,int>> pairs;
    for (int i = 0; i < p; i++) {
        int a, b;
        cin >> a >> b;
        pairs.push_back({a, b});
    }

    Solution solution;
    vector<int> result = solution.courseSchedule(n, prerequisites, pairs);

    if (result.empty()) {
        cout << -1 << endl;
    } else {
        for (int i = 0; i < result.size(); i++) {
            cout << result[i];
            if (i < result.size() - 1) cout << " ";
        }
        cout << endl;
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  courseSchedule(n, prerequisites, pairs) {
    return 0;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  const tokens = data.join(" ").split(/\s+/);
  let ptr = 0;
  const n = Number(tokens[ptr++]);
  const m = Number(tokens[ptr++]);

  const prerequisites = [];
  for (let i = 0; i < m; i++) {
    const u = Number(tokens[ptr++]);
    const v = Number(tokens[ptr++]);
    prerequisites.push([u, v]);
  }

  // Handle optional pairs input
  let pairs = [];
  if (ptr < tokens.length) {
    const p = Number(tokens[ptr++]);
    for (let i = 0; i < p; i++) {
      const a = Number(tokens[ptr++]);
      const b = Number(tokens[ptr++]);
      pairs.push([a, b]);
    }
  }

  const solution = new Solution();
  const result = solution.courseSchedule(n, prerequisites, pairs);

  if (result.length === 0) {
    console.log(-1);
  } else {
    console.log(result.join(" "));
  }
});
```

