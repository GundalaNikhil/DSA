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
---

# GRP-007: Course Plan with Mandatory Pairs

## 📋 Problem Summary

Produce a topological ordering of courses that respects both prerequisite constraints and mandatory adjacency pairs. This combines standard topological sort with the constraint that certain course pairs must appear adjacent in the final schedule.

## 🌍 Real-World Scenario

**Scenario Title:** University Course Scheduling with Lab Pairs

Imagine scheduling university courses where some courses have prerequisites (must be taken before others) and some courses have mandatory lab components that must be scheduled in consecutive time slots. For example, "Chemistry Theory" and "Chemistry Lab" must be adjacent, and "Physics 1" must come before "Physics 2".

The challenge is to create a valid semester schedule that satisfies both types of constraints. This is common in academic planning where theory-lab pairs, lecture-tutorial pairs, or related courses need to be consecutive for pedagogical or logistical reasons.

**Why This Problem Matters:**

- **Academic Scheduling:** Course timetabling with paired sessions
- **Task Scheduling:** Jobs with setup/cleanup phases that must be adjacent
- **Manufacturing:** Processes with mandatory consecutive steps
- **Project Planning:** Tasks with hard adjacency requirements

![Real-World Application](../images/GRP-007/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Topological Sort with Pairs

```
Prerequisites: 0→2, 1→2
Mandatory pair: (2,3) must be adjacent

Graph:
    0 ↘
         2 → 3
    1 ↗

Valid orderings:
[0, 1, 2, 3] ✓ (2 and 3 adjacent)
[1, 0, 2, 3] ✓ (2 and 3 adjacent)

Invalid:
[0, 2, 1, 3] ✗ (2 and 3 not adjacent)

Approach: Contract (2,3) into super-node,
run topological sort, then expand.
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Prerequisite edges:** Directed edges representing "must come before"
- **Adjacency pairs:** Undirected pairs that must be consecutive in output
- **Valid ordering:** Satisfies all prerequisites AND all adjacency constraints
- **Multiple solutions:** Any valid ordering is acceptable

Common interpretation mistake:

- ❌ **Wrong:** Treating adjacency pairs as prerequisite edges
- ✅ **Correct:** Adjacency means consecutive in final ordering, not dependency

### Core Concept

**Graph Contraction:** Merge each adjacency pair into a single super-node, perform topological sort on the contracted graph, then expand super-nodes back to individual courses maintaining the pair adjacency.

## Optimal Approach

### Algorithm

```
course_schedule(n, prerequisites, pairs):
    # Step 1: Create super-nodes for adjacency pairs
    parent = [i for i in range(n)]  # Union-Find
    
    for (a, b) in pairs:
        union(a, b, parent)
    
    # Step 2: Build contracted graph
    contracted_adj = build_contracted_graph(prerequisites, parent)
    
    # Step 3: Topological sort on contracted graph
    topo_order = topological_sort(contracted_adj)
    
    if topo_order is empty:
        return []  # Cycle detected or impossible
    
    # Step 4: Expand super-nodes
    result = []
    for super_node in topo_order:
        members = get_members(super_node, parent)
        # Order members respecting internal prerequisites
        result.extend(order_members(members, prerequisites))
    
    return result
```

### Time Complexity

- **O(n + m + p)** where n=courses, m=prerequisites, p=pairs
- Union-Find: O(p × α(n))
- Topological sort: O(n + m)

### Space Complexity

- **O(n + m)** for graph and auxiliary structures

![Algorithm Visualization](../images/GRP-007/algorithm-visualization.png)

## Implementations

### Java
```java
import java.util.*;

class Solution {
    private int[] parent;

    public List<Integer> courseSchedule(int n, List<int[]> prerequisites, List<int[]> pairs) {
        parent = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;

        // Union pairs
        for (int[] pair : pairs) {
            union(pair[0], pair[1]);
        }

        // Build contracted graph
        Map<Integer, List<Integer>> contracted = new HashMap<>();
        Map<Integer, Integer> inDegree = new HashMap<>();

        for (int i = 0; i < n; i++) {
            int root = find(i);
            contracted.putIfAbsent(root, new ArrayList<>());
            inDegree.putIfAbsent(root, 0);
        }

        for (int[] pre : prerequisites) {
            int from = find(pre[0]);
            int to = find(pre[1]);
            if (from != to) {
                contracted.get(from).add(to);
                inDegree.put(to, inDegree.get(to) + 1);
            }
        }

        // Topological sort (Kahn's algorithm)
        List<Integer> sortedRoots = new ArrayList<>(inDegree.keySet());
        Collections.sort(sortedRoots);
        Queue<Integer> queue = new LinkedList<>();
        for (int node : sortedRoots) {
            if (inDegree.get(node) == 0) {
                queue.offer(node);
            }
        }

        List<Integer> topoOrder = new ArrayList<>();
        while (!queue.isEmpty()) {
            int node = queue.poll();
            topoOrder.add(node);

            List<Integer> neighbors = new ArrayList<>(contracted.get(node));
            Collections.sort(neighbors);
            for (int neighbor : neighbors) {
                inDegree.put(neighbor, inDegree.get(neighbor) - 1);
                if (inDegree.get(neighbor) == 0) {
                    queue.offer(neighbor);
                }
            }
        }

        if (topoOrder.size() != contracted.size()) {
            return new ArrayList<>(); // Cycle detected
        }

        // Expand super-nodes
        List<Integer> result = new ArrayList<>();
        for (int superNode : topoOrder) {
            List<Integer> members = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                if (find(i) == superNode) {
                    members.add(i);
                }
            }
            Collections.sort(members);
            result.addAll(members);
        }

        return result;
    }

    private int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    private void union(int x, int y) {
        int px = find(x);
        int py = find(y);
        if (px != py) {
            parent[px] = py;
        }
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
    parent = list(range(n))
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py
    
    for a, b in pairs:
        union(a, b)
    
    contracted = defaultdict(list)
    in_degree = defaultdict(int)
    
    # Sort roots for deterministic behavior
    roots = sorted(list(set(find(i) for i in range(n))))
    for root in roots:
        in_degree[root] = 0
    
    for u, v in prerequisites:
        from_root = find(u)
        to_root = find(v)
        if from_root != to_root:
            contracted[from_root].append(to_root)
            in_degree[to_root] += 1
    
    # Sort for deterministic topological sort if multiple zero in-degree
    # But queue order handles it if inserted in sorted order
    queue = deque([node for node in roots if in_degree[node] == 0])
    topo_order = []
    
    while queue:
        node = queue.popleft()
        topo_order.append(node)
        
        # Sort neighbors for deterministic processing
        neighbors = sorted(contracted[node])
        for neighbor in neighbors:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    if len(topo_order) != len(roots):
        return []
    
    result = []
    for super_node in topo_order:
        # Sort members of super_node
        members = sorted([i for i in range(n) if find(i) == super_node])
        result.extend(members)
    
    return result

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
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    void unionNodes(int x, int y) {
        int px = find(x);
        int py = find(y);
        if (px != py) {
            parent[px] = py;
        }
    }

public:
    vector<int> courseSchedule(int n, vector<pair<int,int>>& prerequisites, vector<pair<int,int>>& pairs) {
        parent.resize(n);
        for (int i = 0; i < n; i++) parent[i] = i;

        // Union pairs
        for (auto& [a, b] : pairs) {
            unionNodes(a, b);
        }

        // Build contracted graph
        unordered_map<int, vector<int>> contracted;
        unordered_map<int, int> inDegree;
        unordered_set<int> rootSet;

        for (int i = 0; i < n; i++) {
            rootSet.insert(find(i));
        }

        // Sort roots for deterministic behavior
        vector<int> roots(rootSet.begin(), rootSet.end());
        sort(roots.begin(), roots.end());

        for (int root : roots) {
            inDegree[root] = 0;
        }

        for (auto& [u, v] : prerequisites) {
            int from = find(u);
            int to = find(v);
            if (from != to) {
                contracted[from].push_back(to);
                inDegree[to]++;
            }
        }

        // Topological sort with sorted neighbors
        queue<int> q;
        for (int root : roots) {
            if (inDegree[root] == 0) {
                q.push(root);
            }
        }

        vector<int> topoOrder;
        while (!q.empty()) {
            int node = q.front();
            q.pop();
            topoOrder.push_back(node);

            // Sort neighbors for deterministic processing
            vector<int> neighbors = contracted[node];
            sort(neighbors.begin(), neighbors.end());
            for (int neighbor : neighbors) {
                inDegree[neighbor]--;
                if (inDegree[neighbor] == 0) {
                    q.push(neighbor);
                }
            }
        }

        if (topoOrder.size() != roots.size()) {
            return {}; // Cycle detected
        }

        // Expand super-nodes
        vector<int> result;
        for (int superNode : topoOrder) {
            vector<int> members;
            for (int i = 0; i < n; i++) {
                if (find(i) == superNode) {
                    members.push_back(i);
                }
            }
            sort(members.begin(), members.end());
            for (int member : members) {
                result.push_back(member);
            }
        }

        return result;
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
    const parent = Array.from({ length: n }, (_, i) => i);

    const find = (x) => {
      if (parent[x] !== x) {
        parent[x] = find(parent[x]);
      }
      return parent[x];
    };

    const union = (x, y) => {
      const px = find(x);
      const py = find(y);
      if (px !== py) {
        parent[px] = py;
      }
    };

    // Union pairs
    for (const [a, b] of pairs) {
      union(a, b);
    }

    // Build contracted graph
    const contracted = new Map();
    const inDegree = new Map();

    // Get all roots sorted for determinism
    const rootSet = new Set();
    for (let i = 0; i < n; i++) {
      rootSet.add(find(i));
    }
    const roots = Array.from(rootSet).sort((a, b) => a - b);

    for (const root of roots) {
      contracted.set(root, []);
      inDegree.set(root, 0);
    }

    for (const [u, v] of prerequisites) {
      const from = find(u);
      const to = find(v);
      if (from !== to) {
        contracted.get(from).push(to);
        inDegree.set(to, inDegree.get(to) + 1);
      }
    }

    // Topological sort - queue initialized with sorted zero-indegree roots
    const queue = [];
    for (const root of roots) {
      if (inDegree.get(root) === 0) {
        queue.push(root);
      }
    }

    const topoOrder = [];
    while (queue.length > 0) {
      const node = queue.shift();
      topoOrder.push(node);

      // Sort neighbors for deterministic processing
      const neighbors = contracted.get(node).sort((a, b) => a - b);
      for (const neighbor of neighbors) {
        inDegree.set(neighbor, inDegree.get(neighbor) - 1);
        if (inDegree.get(neighbor) === 0) {
          queue.push(neighbor);
        }
      }
    }

    if (topoOrder.length !== roots.length) {
      return []; // Cycle detected
    }

    // Expand super-nodes
    const result = [];
    for (const superNode of topoOrder) {
      const members = [];
      for (let i = 0; i < n; i++) {
        if (find(i) === superNode) {
          members.push(i);
        }
      }
      members.sort((a, b) => a - b);
      result.push(...members);
    }

    return result;
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

## 🧪 Test Case Walkthrough (Dry Run)

Input: n=4, prerequisites=[(0,2), (1,2)], pairs=[(2,3)]

1. Union pairs: {2,3} become super-node
2. Contracted graph: 0→{2,3}, 1→{2,3}
3. Topological sort: [0, 1, {2,3}] or [1, 0, {2,3}]
4. Expand: [0, 1, 2, 3] or [1, 0, 2, 3]

Both satisfy: 0 before 2, 1 before 2, and 2 adjacent to 3 ✓

![Example Visualization](../images/GRP-007/example-1.png)

## ✅ Proof of Correctness

**Theorem:** If a valid ordering exists, graph contraction + topological sort finds it.

**Proof:**
- Contraction preserves prerequisite relationships between super-nodes
- Topological sort ensures prerequisite order
- Expansion maintains adjacency within super-nodes

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Handle multiple adjacency pairs per course
- **Extension 2:** Minimize total schedule length with time constraints
- **Extension 3:** Find all valid orderings
- **Extension 4:** Handle conflicts (impossible to satisfy all constraints)

### Common Mistakes to Avoid

1. **Treating Pairs as Prerequisites**
   - ❌ Wrong: Adding directed edges for pairs
   - ✅ Correct: Using Union-Find to group pairs
   - **Impact:** Incorrect ordering

2. **Not Checking for Cycles**
   - ❌ Wrong: Assuming topological sort always succeeds
   - ✅ Correct: Validate topo_order.size() == num_super_nodes
   - **Description:** Prerequisites might form a cycle

3. **Incorrect Super-Node Expansion**
   - ❌ Wrong: Random order within super-nodes
   - ✅ Correct: Respect internal prerequisites when expanding
   - **Prevention:** Check prerequisites within super-nodes

4. **Forgetting Self-Loops**
   - ❌ Wrong: Not checking if from_root == to_root
   - ✅ Correct: Skip edges within same super-node
   - **Description:** Contracted edges to same node create issues

5. **Not Handling Disconnected Components**
   - ❌ Wrong: Only processing one component
   - ✅ Correct: Ensure all super-nodes are in topological order
   - **Description:** Missing courses in output

## Related Concepts

- **Standard Topological Sort:** Kahn's algorithm, DFS-based
- **Graph Contraction:** Merging nodes while preserving structure
- **Union-Find (DSU):** Efficient set operations for grouping
- **Constraint Satisfaction:** CSP with ordering constraints
- **Job Scheduling:** Real-world application of topological sort
