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
        // Your implementation here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        
        List<int[]> edges = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            edges.add(new int[]{u, v});
        }
        
        sc.nextLine(); // consume newline
        String[] vipArr = sc.nextLine().trim().split("\\s+");
        Set<Integer> vips = new HashSet<>();
        for (String s : vipArr) {
            if (!s.isEmpty()) {
                vips.add(Integer.parseInt(s));
            }
        }
        
        Solution solution = new Solution();
        System.out.println(solution.maxComponentSize(n, edges, vips));
        sc.close();
    }
}
```

### Python

```python
from typing import List, Set

def max_component_size(n: int, edges: List[tuple], vips: Set[int]) -> int:
    # Your implementation here
    return 0

def main():
    n = int(input())
    m = int(input())
    
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    
    vip_list = list(map(int, input().split()))
    vips = set(vip_list)
    
    result = max_component_size(n, edges, vips)
    print(result)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <unordered_set>
#include <sstream>
using namespace std;

class Solution {
public:
    int maxComponentSize(int n, vector<pair<int,int>>& edges, unordered_set<int>& vips) {
        // Your implementation here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, m;
    cin >> n >> m;
    
    vector<pair<int,int>> edges;
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        edges.push_back({u, v});
    }
    
    cin.ignore();
    string line;
    getline(cin, line);
    istringstream iss(line);
    unordered_set<int> vips;
    int vip;
    while (iss >> vip) {
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
    // Your implementation here
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
  let ptr = 0;
  const n = parseInt(data[ptr++]);
  const m = parseInt(data[ptr++]);
  
  const edges = [];
  for (let i = 0; i < m; i++) {
    const [u, v] = data[ptr++].split(" ").map(Number);
    edges.push([u, v]);
  }
  
  const vipArr = data[ptr++].split(" ").map(Number);
  const vips = new Set(vipArr);
  
  const solution = new Solution();
  console.log(solution.maxComponentSize(n, edges, vips));
});
```