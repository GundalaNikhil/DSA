---
problem_id: GRP_EXAM_SEATING_VIP__3928
display_id: GRP-012
slug: exam-seating-rooms-vip
title: "Exam Seating Rooms with VIP Isolation"
difficulty: Easy-Medium
difficulty_score: 40
topics:
  - Union-Find
  - Connected Components
  - Disjoint Set Union
tags:
  - graph
  - union-find
  - dsu
  - connected-components
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRP-012: Exam Seating Rooms with VIP Isolation

## Problem Statement

You are given an undirected graph where nodes represent students who prefer to sit together (connected by edges). Some students are designated as VIPs.

**Constraint**: No connected component can contain more than one VIP.

Your task is to remove the minimum number of edges such that no component contains more than one VIP, then return the size of the largest remaining connected component.

![Problem Illustration](../images/GRP-012/problem-illustration.png)

## Input Format

- First line: integer `n` (number of students/nodes)
- Second line: integer `m` (number of edges)
- Next `m` lines: two integers `u v` representing an edge between students `u` and `v`
- Last line: space-separated integers representing VIP student IDs

## Output Format

- Single integer: the size of the largest connected component after edge removals

## Constraints

- `1 <= n <= 10^5`
- `0 <= m <= 2*10^5`
- `0 <= u, v < n`
- Number of VIPs `<= n`

## Example

**Input:**
```
5
3
0 1
1 2
3 4
2 3
```

**Output:**
```
3
```

**Explanation:**

Edges: (0,1), (1,2), (3,4)
VIPs: {2, 3}

Initial components:
- Component 1: {0, 1, 2} (contains VIP 2)
- Component 2: {3, 4} (contains VIP 3)

Since VIPs 2 and 3 are already in different components, no edges need to be removed.

Final components:
- Component 1: {0, 1, 2} → size 3
- Component 2: {3, 4} → size 2

Largest component size = 3

![Example Visualization](../images/GRP-012/example-1.png)

## Notes

- Use Disjoint Set Union (DSU / Union-Find) to track components
- Track which components contain VIPs
- When processing an edge (u, v):
  - If both components already have a VIP, skip the edge
  - Otherwise, union the components
- After processing all valid edges, find the maximum component size
- Time complexity: O(m × α(n)) where α is the inverse Ackermann function (nearly constant)

## Related Topics

Union-Find, DSU, Connected Components, Graph Constraints, Component Tracking

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int maxComponentSize(int n, List<int[]> edges, Set<Integer> vips) {
        // Implementation here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        
        List<int[]> edges = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            edges.add(new int[]{u, v});
        }
        
        Set<Integer> vips = new HashSet<>();
        if (sc.hasNextLine()) sc.nextLine(); // Consume newline
        if (sc.hasNextLine()) {
            String line = sc.nextLine();
            Scanner lineSc = new Scanner(line);
            while (lineSc.hasNextInt()) {
                vips.add(lineSc.nextInt());
            }
            lineSc.close();
        }
        
        Solution solution = new Solution();
        System.out.println(solution.maxComponentSize(n, edges, vips));
        sc.close();
    }
}
```

### Python

```python
import sys

def max_component_size(n: int, edges: list[tuple[int, int]], vips: set[int]) -> int:
    # Implementation here
    return 0

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        
        edges = []
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            edges.append((u, v))
            
        vips = set()
        # Remaining tokens are VIPs
        for token in iterator:
            vips.add(int(token))
            
        print(max_component_size(n, edges, vips))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <unordered_set>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maxComponentSize(int n, vector<pair<int, int>>& edges, unordered_set<int>& vips) {
        // Implementation here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, m;
    if (!(cin >> n >> m)) return 0;
    
    vector<pair<int, int>> edges(m);
    for (int i = 0; i < m; i++) {
        cin >> edges[i].first >> edges[i].second;
    }
    
    unordered_set<int> vips;
    string line;
    getline(cin >> ws, line); // consume rest of line and read next
    stringstream ss(line);
    int vip;
    while (ss >> vip) {
        vips.insert(vip);
    }
    
    Solution solution;
    cout << solution.maxComponentSize(n, edges, vips) << "\n";
    
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  maxComponentSize(n, edges, vips) {
    // Implementation here
    return null;
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
  
  let ptr = 0;
  const n = parseInt(data[ptr++], 10);
  const m = parseInt(data[ptr++], 10);
  
  const edges = [];
  for (let i = 0; i < m; i++) {
    const u = parseInt(data[ptr++], 10);
    const v = parseInt(data[ptr++], 10);
    edges.push([u, v]);
  }
  
  const vips = [];
  while (ptr < data.length) {
    vips.push(parseInt(data[ptr++], 10));
  }
  
  const solution = new Solution();
  console.log(solution.maxComponentSize(n, edges, vips));
});
```
