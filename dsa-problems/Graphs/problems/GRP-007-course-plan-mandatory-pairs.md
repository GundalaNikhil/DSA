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

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/dsa/graphs/grp_007.jpg)

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
import java.io.*;

class Solution {
    public List<Integer> findSchedule(int n, int m, List<int[]> prerequisites, int p, List<int[]> mandatoryPairs) {
        // Implement here
        return new ArrayList<>();
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String nLine = br.readLine();
        if (nLine == null) return;
        int n = Integer.parseInt(nLine.trim());

        String mLine = br.readLine();
        if (mLine == null) return;
        int m = Integer.parseInt(mLine.trim());

        List<int[]> prerequisites = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            String[] line = br.readLine().trim().split("\\s+");
            prerequisites.add(new int[]{Integer.parseInt(line[0]), Integer.parseInt(line[1])});
        }

        String pLine = br.readLine();
        if (pLine == null) return;
        int pCount = Integer.parseInt(pLine.trim());

        List<int[]> mandatoryPairs = new ArrayList<>();
        for (int i = 0; i < pCount; i++) {
            String[] line = br.readLine().trim().split("\\s+");
            mandatoryPairs.add(new int[]{Integer.parseInt(line[0]), Integer.parseInt(line[1])});
        }

        Solution sol = new Solution();
        List<Integer> result = sol.findSchedule(n, m, prerequisites, pCount, mandatoryPairs);

        if (result == null || result.isEmpty()) {
            System.out.println("-1");
        } else {
            PrintWriter out = new PrintWriter(System.out);
            for (int i = 0; i < result.size(); i++) {
                out.print(result.get(i) + (i == result.size() - 1 ? "" : " "));
            }
            out.println();
            out.flush();
        }
    }
}
```

### Python

```python
import sys

# Increase recursion depth for deep graphs
sys.setrecursionlimit(200000)

class Solution:
    def find_schedule(self, n, m, prerequisites, p, mandatory_pairs):
        # Implement here
        return []

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])

    idx = 2
    prereqs = []
    for _ in range(m):
        prereqs.append((int(input_data[idx]), int(input_data[idx+1])))
        idx += 2

    p = int(input_data[idx])
    idx += 1
    pairs = []
    for _ in range(p):
        pairs.append((int(input_data[idx]), int(input_data[idx+1])))
        idx += 2

    sol = Solution()
    result = sol.find_schedule(n, m, prereqs, p, pairs)
    if not result:
        print("-1")
    else:
        print(*(result))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> findSchedule(int n, int m, vector<pair<int, int>>& prerequisites, int p, vector<pair<int, int>>& mandatoryPairs) {
        // Implement here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<pair<int, int>> prerequisites(m);
    for (int i = 0; i < m; i++) {
        cin >> prerequisites[i].first >> prerequisites[i].second;
    }

    int p;
    if (!(cin >> p)) return 0;
    vector<pair<int, int>> mandatoryPairs(p);
    for (int i = 0; i < p; i++) {
        cin >> mandatoryPairs[i].first >> mandatoryPairs[i].second;
    }

    Solution sol;
    vector<int> result = sol.findSchedule(n, m, prerequisites, p, mandatoryPairs);

    if (result.empty()) {
        cout << "-1" << endl;
    } else {
        for (int i = 0; i < result.size(); i++) {
            cout << result[i] << (i == result.size() - 1 ? "" : " ");
        }
        cout << endl;
    }

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  findSchedule(n, m, prerequisites, p, mandatoryPairs) {
    // Implement here
    return [];
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const m = parseInt(input[idx++]);

  const prerequisites = [];
  for (let i = 0; i < m; i++) {
    prerequisites.push([parseInt(input[idx++]), parseInt(input[idx++])]);
  }

  const p = parseInt(input[idx++]);
  const mandatoryPairs = [];
  for (let i = 0; i < p; i++) {
    mandatoryPairs.push([parseInt(input[idx++]), parseInt(input[idx++])]);
  }

  const sol = new Solution();
  const result = sol.findSchedule(n, m, prerequisites, p, mandatoryPairs);
  if (result.length === 0) {
    console.log("-1");
  } else {
    console.log(result.join(" "));
  }
}

solve();
```
