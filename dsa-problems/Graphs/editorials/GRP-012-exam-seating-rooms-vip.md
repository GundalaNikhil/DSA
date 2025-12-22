---
problem_id: GRP_EXAM_SEATING_VIP__8341
display_id: GRP-012
slug: exam-seating-rooms-vip
title: "Exam Seating Rooms VIP"
difficulty: Medium
difficulty_score: 50
topics:
  - Union-Find
  - Disjoint Set Union
  - Connected Components
tags:
  - graph
  - union-find
  - dsu
  - connected-components
  - medium
premium: true
subscription_tier: basic
---

# GRP-012: Exam Seating Rooms VIP

## 📋 Problem Summary

Determine if VIP students can be seated such that all VIPs in each connected component are in the same room. Use Union-Find to group students by friendships, then check if VIP constraints are satisfiable.

## 🌍 Real-World Scenario

**Scenario Title:** Conference Room Assignment with Team Constraints

Imagine organizing a conference where attendees have team affiliations (friendships) and some are VIPs requiring special seating. Teams (connected components) must stay together, and all VIPs in a team must be in the same designated room.

Union-Find efficiently groups people into teams based on friendships. Then we verify that each team has at most one VIP room requirement, ensuring feasible room assignments without conflicts.

**Why This Problem Matters:**

- **Event Planning:** Seating arrangements with group constraints
- **Network Partitioning:** Grouping nodes with special requirements
- **Resource Allocation:** Assigning resources to connected groups
- **Social Network Analysis:** Identifying communities with leaders

![Real-World Application](../images/GRP-012/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Union-Find with VIP Constraints

```
Students: 0, 1, 2, 3, 4
Friendships: (0,1), (2,3)
VIP assignments: {0: room_A, 1: room_A, 3: room_B}

Union-Find groups:
Component 1: {0, 1} - VIPs: 0→room_A, 1→room_A ✓ (same room)
Component 2: {2, 3} - VIPs: 3→room_B ✓ (only one VIP)
Component 3: {4} - No VIPs ✓

Result: FEASIBLE
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Friendships:** Undirected edges forming connected components
- **VIP assignments:** Map from student ID to required room
- **Feasibility:** All VIPs in same component must have same room assignment
- **Return:** true if feasible, false otherwise

## Optimal Approach

### Algorithm

```
is_seating_feasible(n, friendships, vip_rooms):
    uf = UnionFind(n)
    
    // Build connected components
    for (u, v) in friendships:
        uf.union(u, v)
    
    // Group VIPs by component
    component_vip_rooms = {}  // component_root -> set of required rooms
    
    for student, room in vip_rooms:
        root = uf.find(student)
        if root not in component_vip_rooms:
            component_vip_rooms[root] = set()
        component_vip_rooms[root].add(room)
    
    // Check each component has at most one required room
    for root, rooms in component_vip_rooms:
        if len(rooms) > 1:
            return false  // Conflict: VIPs in same component need different rooms
    
    return true
```

### Time Complexity: **O(n + m × α(n))** where α is inverse Ackermann
### Space Complexity: **O(n)**

![Algorithm Visualization](../images/GRP-012/algorithm-visualization.png)

## Implementations

### Java

```java
import java.util.*;

class UnionFind {
    private int[] parent;
    private int[] rank;
    
    public UnionFind(int n) {
        parent = new int[n];
        rank = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
    }
    
    public int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);  // Path compression
        }
        return parent[x];
    }
    
    public void union(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        
        if (rootX != rootY) {
            if (rank[rootX] < rank[rootY]) {
                parent[rootX] = rootY;
            } else if (rank[rootX] > rank[rootY]) {
                parent[rootY] = rootX;
            } else {
                parent[rootY] = rootX;
                rank[rootX]++;
            }
        }
    }
}

class Solution {
    public boolean isSeatingFeasible(int n, int[][] friendships, Map<Integer, String> vipRooms) {
        UnionFind uf = new UnionFind(n);
        
        // Build connected components
        for (int[] edge : friendships) {
            uf.union(edge[0], edge[1]);
        }
        
        // Group VIPs by component
        Map<Integer, Set<String>> componentVipRooms = new HashMap<>();
        
        for (Map.Entry<Integer, String> entry : vipRooms.entrySet()) {
            int student = entry.getKey();
            String room = entry.getValue();
            int root = uf.find(student);
            
            componentVipRooms.putIfAbsent(root, new HashSet<>());
            componentVipRooms.get(root).add(room);
        }
        
        // Check each component has at most one required room
        for (Set<String> rooms : componentVipRooms.values()) {
            if (rooms.size() > 1) {
                return false;
            }
        }
        
        return true;
    }
}
```

### Python

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

def is_seating_feasible(n, friendships, vip_rooms):
    uf = UnionFind(n)
    
    # Build connected components
    for u, v in friendships:
        uf.union(u, v)
    
    # Group VIPs by component
    component_vip_rooms = {}
    
    for student, room in vip_rooms.items():
        root = uf.find(student)
        if root not in component_vip_rooms:
            component_vip_rooms[root] = set()
        component_vip_rooms[root].add(room)
    
    # Check each component has at most one required room
    for rooms in component_vip_rooms.values():
        if len(rooms) > 1:
            return False
    
    return True
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <string>
using namespace std;

class UnionFind {
private:
    vector<int> parent;
    vector<int> rank;
    
public:
    UnionFind(int n) : parent(n), rank(n, 0) {
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
    }
    
    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);  // Path compression
        }
        return parent[x];
    }
    
    void unite(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        
        if (rootX != rootY) {
            if (rank[rootX] < rank[rootY]) {
                parent[rootX] = rootY;
            } else if (rank[rootX] > rank[rootY]) {
                parent[rootY] = rootX;
            } else {
                parent[rootY] = rootX;
                rank[rootX]++;
            }
        }
    }
};

class Solution {
public:
    bool isSeatingFeasible(int n, vector<vector<int>>& friendships, 
                          unordered_map<int, string>& vipRooms) {
        UnionFind uf(n);
        
        // Build connected components
        for (auto& edge : friendships) {
            uf.unite(edge[0], edge[1]);
        }
        
        // Group VIPs by component
        unordered_map<int, unordered_set<string>> componentVipRooms;
        
        for (auto& [student, room] : vipRooms) {
            int root = uf.find(student);
            componentVipRooms[root].insert(room);
        }
        
        // Check each component has at most one required room
        for (auto& [root, rooms] : componentVipRooms) {
            if (rooms.size() > 1) {
                return false;
            }
        }
        
        return true;
    }
};
```

### JavaScript

```javascript
class UnionFind {
  constructor(n) {
    this.parent = Array.from({ length: n }, (_, i) => i);
    this.rank = Array(n).fill(0);
  }
  
  find(x) {
    if (this.parent[x] !== x) {
      this.parent[x] = this.find(this.parent[x]);  // Path compression
    }
    return this.parent[x];
  }
  
  union(x, y) {
    const rootX = this.find(x);
    const rootY = this.find(y);
    
    if (rootX !== rootY) {
      if (this.rank[rootX] < this.rank[rootY]) {
        this.parent[rootX] = rootY;
      } else if (this.rank[rootX] > this.rank[rootY]) {
        this.parent[rootY] = rootX;
      } else {
        this.parent[rootY] = rootX;
        this.rank[rootX]++;
      }
    }
  }
}

class Solution {
  isSeatingFeasible(n, friendships, vipRooms) {
    const uf = new UnionFind(n);
    
    // Build connected components
    for (const [u, v] of friendships) {
      uf.union(u, v);
    }
    
    // Group VIPs by component
    const componentVipRooms = new Map();
    
    for (const [student, room] of Object.entries(vipRooms)) {
      const root = uf.find(parseInt(student));
      if (!componentVipRooms.has(root)) {
        componentVipRooms.set(root, new Set());
      }
      componentVipRooms.get(root).add(room);
    }
    
    // Check each component has at most one required room
    for (const rooms of componentVipRooms.values()) {
      if (rooms.size > 1) {
        return false;
      }
    }
    
    return true;
  }
}
```

## 🧪 Test Case Walkthrough (Dry Run)

n=5, friendships=[(0,1), (2,3)], vipRooms={0:'A', 1:'A', 3:'B'}

1. Union operations: {0,1}, {2,3}, {4}
2. Find roots: 0→0, 1→0, 2→2, 3→2, 4→4
3. Group VIPs:
   - Component 0: rooms={'A'} (from students 0,1)
   - Component 2: rooms={'B'} (from student 3)
4. Check: All components have ≤1 room → FEASIBLE

![Example Visualization](../images/GRP-012/example-1.png)

## ✅ Proof of Correctness

**Theorem:** Union-Find correctly identifies connected components and detects VIP conflicts.

**Proof:** Union-Find groups students into disjoint sets. If two VIPs in the same set require different rooms, it's impossible to satisfy both constraints.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Assign rooms to maximize VIP satisfaction
- **Extension 2:** Handle capacity constraints per room
- **Extension 3:** Minimize number of rooms used
- **Extension 4:** Handle dynamic friendship additions

## Common Mistakes to Avoid

1. **Not Using Path Compression**
   - ❌ Wrong: Simple find without path compression
   - ✅ Correct: Implement path compression in find()
   - **Impact:** O(n) find operations instead of O(α(n))

2. **Forgetting Union by Rank**
   - ❌ Wrong: Always attaching to first root
   - ✅ Correct: Attach smaller tree to larger tree
   - **Description:** Degrades to O(n) worst case

3. **Not Grouping by Component Root**
   - ❌ Wrong: Grouping VIPs by student ID
   - ✅ Correct: Group by component root (find(student))
   - **Prevention:** Always use find() to get canonical representative

4. **Checking Individual VIPs**
   - ❌ Wrong: Comparing VIPs pairwise
   - ✅ Correct: Group all VIPs in component, check set size
   - **Description:** Inefficient and error-prone

5. **Modifying During Iteration**
   - ❌ Wrong: Modifying Union-Find while checking
   - ✅ Correct: Build components first, then check
   - **Description:** Can cause incorrect results

## Related Concepts

- **Kruskal's MST:** Uses Union-Find for cycle detection
- **Connected Components:** Standard Union-Find application
- **Dynamic Connectivity:** Online Union-Find queries
- **Bipartite Checking:** Can use Union-Find with parity
- **Network Reliability:** Component analysis
