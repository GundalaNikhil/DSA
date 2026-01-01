---
problem_id: HEP_DYNAMIC_MEDIAN_OF_MEDIANS__7312
display_id: HEP-009
slug: dynamic-median-of-medians
title: "Dynamic Median of Medians"
difficulty: Medium
difficulty_score: 60
topics:
  - Heaps
  - Medians
  - Union-Find
tags:
  - heaps
  - median
  - union-find
  - medium
premium: true
subscription_tier: basic
---

# HEP-009: Dynamic Median of Medians

## 📋 Problem Summary

You need to manage multiple groups of numbers and support:
1. `NEW id m ...`: Create a group `id` with initial numbers.
2. `ADD id x`: Add `x` to group `id`.
3. `MERGE id1 id2`: Merge group `id2` into `id1`.
4. `QUERY`: Find the median of the medians of all non-empty groups.

The "median" of a group is the lower median if size is even.
The "median of medians" is the median of the set of group medians.

## 🌍 Real-World Scenario

**Scenario Title:** Consolidated Census Data

Imagine a country with many districts.
- Each district maintains a median income statistic.
- Districts can be merged (administrative redistricting).
- New census data comes in (ADD).
- The central government wants to know the "Median of District Medians" to gauge the typical district's economic health.
- This requires a system that efficiently handles local updates, merges, and global queries.

![Real-World Application](../images/HEP-009/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Hierarchical Structure

**Level 1: Groups**
Group A: `[1, 5, 10]`. Median = 5.
Group B: `[2, 8]`. Median = 2.
Group C: `[20]`. Median = 20.

**Level 2: Global Medians**
Set of Medians: `{5, 2, 20}`.
Sorted: `[2, 5, 20]`.
Global Median: 5.

**Operation: MERGE A B**
- Group A absorbs B: `[1, 5, 10, 2, 8]`. Sorted: `[1, 2, 5, 8, 10]`.
- New Median of A: 5.
- Group B is gone.
- Global Set: `{5, 20}`.
- Global Median: 5 (lower of 5, 20).

### Key Concept: Two-Layer Heap System

1. **Local Layer (Per Group):**
   - Each group maintains two heaps (`LeftMax`, `RightMin`) to track its own median efficiently.
   - `LeftMax` stores smaller half. `RightMin` stores larger half.
   - Median is `LeftMax.top()`.

2. **Global Layer:**
   - We need the median of the *current medians*.
   - We can maintain a global structure of medians.
   - Since medians change upon ADD/MERGE, we need to update this global structure.
   - A `Multiset` or another pair of Heaps (`GlobalLeft`, `GlobalRight`) works.
   - **Lazy Deletion** is crucial because we can't efficiently find and remove old medians from standard heaps.

### Merging Strategy

When merging `id2` into `id1`:
- We must combine the elements of `id2` into `id1`.
- **Small-to-Large Heuristic:** Always merge the smaller group into the larger one to keep complexity low (`O(N log^2 N)` or `O(N log N)`).
- However, the problem says `MERGE id1 id2` means `id2` into `id1`. We can swap internals (rename) if `id2` is larger, but we must ensure `id1` remains the identifier.
- After merging, the median of `id1` changes.
- Update Global structure: Remove old `median(id1)` and `median(id2)`, insert new `median(id1)`.

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** Operations. `id` are strings or ints? Example uses `1`, `2`. Assume strings or convert to int.
- **Output:** Median or `EMPTY`.
- **Constraints:** Total elements `10^5`. `Q <= 10^5`.
- **Median Definition:** Lower median for even size.

## Naive Approach

### Intuition

Store full lists for each group. Sort on every query.

### Time Complexity

- **O(Q * N log N)**: Too slow.

## Optimal Approach

### Key Insight

Use **Two Heaps** for each group. Use **Two Heaps with Lazy Deletion** for the global medians.
Use **Union-Find** (or just a map) to track active groups if IDs are dynamic.
We can just move elements.

**Data Structures:**
- `Map<ID, Group>`: Stores heaps for each group.
- `GlobalHeaps`: Two heaps (`GL`, `GR`) storing medians of all groups.
- `LazyMap`: Tracks invalid entries in `GlobalHeaps`.

**Operations:**
1. **NEW:** Create group. Calculate median. Add to Global.
2. **ADD:** Insert to group heaps. Rebalance. Old median `M_old -> M_new`.
   - Global: Remove `M_old` (lazy), Add `M_new`.
3. **MERGE:**
   - Merge heaps of `id2` into `id1`.
   - Heuristic: If `id2` is larger, swap the underlying data structures of `id1` and `id2` (move `id1` elements to `id2`, then update map so `id1` points to `id2`'s data).
   - Recalculate median.
   - Global: Remove old medians of `id1`, `id2`. Add new median.
4. **QUERY:**
   - Clean Global heaps.
   - Return `GL.top()`.

### Time Complexity

- **O(N log^2 N)** or **O(N log N)** depending on merge strategy.
- With small-to-large merging, amortized cost is good.

### Space Complexity

- **O(N)**.

![Algorithm Visualization](../images/HEP-009/algorithm-visualization.png)

## Implementations

### Java
```java
import java.util.*;

class Solution {
    static class Group {
        PriorityQueue<Integer> left = new PriorityQueue<>(Collections.reverseOrder());
        PriorityQueue<Integer> right = new PriorityQueue<>();
        
        void add(int val) {
            if (left.isEmpty() || val <= left.peek()) {
                left.offer(val);
            } else {
                right.offer(val);
            }
            rebalance();
        }
        
        void rebalance() {
            while (left.size() > right.size() + 1) {
                right.offer(left.poll());
            }
            while (right.size() > left.size()) {
                left.offer(right.poll());
            }
        }
        
        int getMedian() {
            if (left.isEmpty()) return 0;
            return left.peek();
        }
        
        int size() {
            return left.size() + right.size();
        }
    }
    
    // Global heaps with tracking
    PriorityQueue<Integer> gLeft = new PriorityQueue<>(Collections.reverseOrder());
    PriorityQueue<Integer> gRight = new PriorityQueue<>();
    Map<Integer, Integer> gDeletedLeft = new HashMap<>();
    Map<Integer, Integer> gDeletedRight = new HashMap<>();
    Map<Integer, Integer> gInLeft = new HashMap<>();
    Map<Integer, Integer> gInRight = new HashMap<>();
    int gLeftSize = 0;
    int gRightSize = 0;
    
    Map<String, Group> groups = new HashMap<>();
    
    private void cleanGlobal() {
        while (!gLeft.isEmpty()) {
            int val = gLeft.peek();
            if (gDeletedLeft.getOrDefault(val, 0) > 0) {
                gDeletedLeft.put(val, gDeletedLeft.get(val) - 1);
                gLeft.poll();
            } else {
                break;
            }
        }
        while (!gRight.isEmpty()) {
            int val = gRight.peek();
            if (gDeletedRight.getOrDefault(val, 0) > 0) {
                gDeletedRight.put(val, gDeletedRight.get(val) - 1);
                gRight.poll();
            } else {
                break;
            }
        }
    }
    
    private void addToGlobal(int val) {
        cleanGlobal();
        if (gLeft.isEmpty() || val <= gLeft.peek()) {
            gLeft.offer(val);
            gInLeft.put(val, gInLeft.getOrDefault(val, 0) + 1);
            gLeftSize++;
        } else {
            gRight.offer(val);
            gInRight.put(val, gInRight.getOrDefault(val, 0) + 1);
            gRightSize++;
        }
        rebalanceGlobal();
    }
    
    private void removeFromGlobal(int val) {
        if (gInLeft.getOrDefault(val, 0) > 0) {
            gInLeft.put(val, gInLeft.get(val) - 1);
            gDeletedLeft.put(val, gDeletedLeft.getOrDefault(val, 0) + 1);
            gLeftSize--;
        } else {
            gInRight.put(val, gInRight.getOrDefault(val, 0) - 1);
            gDeletedRight.put(val, gDeletedRight.getOrDefault(val, 0) + 1);
            gRightSize--;
        }
        rebalanceGlobal();
    }
    
    private void rebalanceGlobal() {
        while (gLeftSize > gRightSize + 1) {
            cleanGlobal();
            if (gLeft.isEmpty()) break; // Should not happen if sizes consistent
            int val = gLeft.poll();
            gInLeft.put(val, gInLeft.getOrDefault(val, 0) - 1);
            
            gRight.offer(val);
            gInRight.put(val, gInRight.getOrDefault(val, 0) + 1);
            gLeftSize--;
            gRightSize++;
            cleanGlobal();
        }
        while (gRightSize > gLeftSize) {
            cleanGlobal();
            if (gRight.isEmpty()) break;
            int val = gRight.poll();
            gInRight.put(val, gInRight.getOrDefault(val, 0) - 1);
            
            gLeft.offer(val);
            gInLeft.put(val, gInLeft.getOrDefault(val, 0) + 1);
            gLeftSize++;
            gRightSize--;
            cleanGlobal();
        }
    }
    
    public List<String> processOperations(List<String[]> operations) {
        List<String> results = new ArrayList<>();
        
        for (String[] op : operations) {
            String type = op[0];
            if (type.equals("NEW")) {
                String id = op[1];
                Group g = new Group();
                for (int i = 2; i < op.length; i++) {
                    g.add(Integer.parseInt(op[i]));
                }
                groups.put(id, g);
                if (g.size() > 0) addToGlobal(g.getMedian());
                
            } else if (type.equals("ADD")) {
                String id = op[1];
                int x = Integer.parseInt(op[2]);
                Group g = groups.get(id);
                if (g != null) {
                    if (g.size() > 0) removeFromGlobal(g.getMedian());
                    g.add(x);
                    if (g.size() > 0) addToGlobal(g.getMedian());
                }
                
            } else if (type.equals("MERGE")) {
                String id1 = op[1];
                String id2 = op[2];
                Group g1 = groups.get(id1);
                Group g2 = groups.get(id2);
                
                if (g1 != null && g2 != null) {
                    if (g1.size() > 0) removeFromGlobal(g1.getMedian());
                    if (g2.size() > 0) removeFromGlobal(g2.getMedian());
                    
                    if (g1.size() < g2.size()) {
                        for (int val : g1.left) g2.add(val);
                        for (int val : g1.right) g2.add(val);
                        groups.put(id1, g2);
                    } else {
                        for (int val : g2.left) g1.add(val);
                        for (int val : g2.right) g1.add(val);
                    }
                    groups.remove(id2);
                    Group merged = groups.get(id1);
                    if (merged.size() > 0) addToGlobal(merged.getMedian());
                }
                
            } else if (type.equals("QUERY")) {
                cleanGlobal();
                if (gLeftSize == 0) results.add("EMPTY");
                else results.add(String.valueOf(gLeft.peek()));
            }
        }
        return results;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int q = sc.nextInt();
            List<String[]> operations = new ArrayList<>();
            for (int i = 0; i < q; i++) {
                String op = sc.next();
                if (op.equals("NEW")) {
                    String id = sc.next();
                    int m = sc.nextInt();
                    String[] line = new String[2 + m];
                    line[0] = op;
                    line[1] = id;
                    for (int j = 0; j < m; j++) line[2 + j] = sc.next();
                    operations.add(line);
                } else if (op.equals("ADD")) {
                    String id = sc.next();
                    String x = sc.next();
                    operations.add(new String[]{op, id, x});
                } else if (op.equals("MERGE")) {
                    String id1 = sc.next();
                    String id2 = sc.next();
                    operations.add(new String[]{op, id1, id2});
                } else {
                    operations.add(new String[]{op});
                }
            }
            Solution solution = new Solution();
            List<String> result = solution.processOperations(operations);
            for (String s : result) System.out.println(s);
        }
        sc.close();
    }
}
```

### Python
```python
import sys
import heapq
from collections import defaultdict

class Group:
    def __init__(self):
        self.left = [] # Max heap (negated)
        self.right = [] # Min heap
        
    def add(self, val):
        if not self.left or val <= -self.left[0]:
            heapq.heappush(self.left, -val)
        else:
            heapq.heappush(self.right, val)
        self.rebalance()
        
    def rebalance(self):
        while len(self.left) > len(self.right) + 1:
            heapq.heappush(self.right, -heapq.heappop(self.left))
        while len(self.right) > len(self.left):
            heapq.heappush(self.left, -heapq.heappop(self.right))
            
    def get_median(self):
        if not self.left: return 0
        return -self.left[0]
        
    def size(self):
        return len(self.left) + len(self.right)
        
    def get_elements(self):
        return [-x for x in self.left] + self.right

class Solution:
    def process_operations(self, operations: list) -> list:
        groups = {}
        
        g_left = []
        g_right = []
        g_in_left = defaultdict(int)
        g_in_right = defaultdict(int)
        g_deleted_left = defaultdict(int)
        g_deleted_right = defaultdict(int)
        g_left_size = 0
        g_right_size = 0
        
        def clean_global():
            while g_left:
                val = -g_left[0]
                if g_deleted_left[val] > 0:
                    g_deleted_left[val] -= 1
                    heapq.heappop(g_left)
                else:
                    break
            while g_right:
                val = g_right[0]
                if g_deleted_right[val] > 0:
                    g_deleted_right[val] -= 1
                    heapq.heappop(g_right)
                else:
                    break
                
        def add_to_global(val):
            nonlocal g_left_size, g_right_size
            if val is None: return
            if not g_left or val <= -g_left[0]:
                heapq.heappush(g_left, -val)
                g_in_left[val] += 1
                g_left_size += 1
            else:
                heapq.heappush(g_right, val)
                g_in_right[val] += 1
                g_right_size += 1
            rebalance_global()
            
        def remove_from_global(val):
            nonlocal g_left_size, g_right_size
            if val is None: return
            if g_in_left[val] > 0:
                g_in_left[val] -= 1
                g_deleted_left[val] += 1
                g_left_size -= 1
            else:
                g_in_right[val] -= 1
                g_deleted_right[val] += 1
                g_right_size -= 1
            rebalance_global()
            
        def rebalance_global():
            nonlocal g_left_size, g_right_size
            while g_left_size > g_right_size + 1:
                clean_global()
                val = -heapq.heappop(g_left)
                g_in_left[val] -= 1
                # We don't need to increment deleted here because we popped it
                heapq.heappush(g_right, val)
                g_in_right[val] += 1
                g_left_size -= 1
                g_right_size += 1
            while g_right_size > g_left_size:
                clean_global()
                val = heapq.heappop(g_right)
                g_in_right[val] -= 1
                heapq.heappush(g_left, -val)
                g_in_left[val] += 1
                g_left_size += 1
                g_right_size -= 1
                
        results = []
        
        for op in operations:
            type = op[0]
            if type == "NEW":
                gid, m = op[1], int(op[2])
                g = Group()
                for x in op[3:]:
                    g.add(int(x))
                groups[gid] = g
                add_to_global(g.get_median() if g.size() > 0 else None)
                
            elif type == "ADD":
                gid = op[1]
                if gid in groups:
                    x = int(op[2])
                    g = groups[gid]
                    old_med = g.get_median() if g.size() > 0 else None
                    remove_from_global(old_med)
                    g.add(x)
                    add_to_global(g.get_median())
                    
            elif type == "MERGE":
                gid1, gid2 = op[1], op[2]
                if gid1 in groups and gid2 in groups:
                    g1, g2 = groups[gid1], groups[gid2]
                    remove_from_global(g1.get_median() if g1.size() > 0 else None)
                    remove_from_global(g2.get_median() if g2.size() > 0 else None)
                    
                    if g1.size() < g2.size():
                        for x in g1.get_elements(): g2.add(x)
                        groups[gid1] = g2
                    else:
                        for x in g2.get_elements(): g1.add(x)
                    del groups[gid2]
                    add_to_global(groups[gid1].get_median() if groups[gid1].size() > 0 else None)
                    
            elif type == "QUERY":
                clean_global()
                if g_left_size == 0:
                    results.append("EMPTY")
                else:
                    results.append(str(-g_left[0]))
                    
        return results

def process_operations(operations: list) -> list:
    solver = Solution()
    return solver.process_operations(operations)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    try:
        q = int(next(it))
        operations = []
        for _ in range(q):
            op = next(it)
            if op == "NEW":
                gid = next(it)
                m = int(next(it))
                vals = [next(it) for _ in range(m)]
                operations.append([op, gid, m] + vals)
            elif op == "ADD":
                gid = next(it)
                x = next(it)
                operations.append([op, gid, x])
            elif op == "MERGE":
                gid1 = next(it)
                gid2 = next(it)
                operations.append([op, gid1, gid2])
            else:
                operations.append([op])
        
        result = process_operations(operations)
        print("\n".join(result))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <unordered_map>
#include <set>

using namespace std;

// Use multiset for easier deletion in C++
struct Group {
    multiset<int> left, right;
    
    void add(int val) {
        if (left.empty() || val <= *left.rbegin()) {
            left.insert(val);
        } else {
            right.insert(val);
        }
        rebalance();
    }
    
    void rebalance() {
        while (left.size() > right.size() + 1) {
            right.insert(*left.rbegin());
            left.erase(prev(left.end()));
        }
        while (right.size() > left.size()) {
            left.insert(*right.begin());
            right.erase(right.begin());
        }
    }
    
    int getMedian() {
        if (left.empty()) return 0;
        return *left.rbegin();
    }
    
    int size() { return left.size() + right.size(); }
    
    void mergeFrom(Group& other) {
        for (int x : other.left) add(x);
        for (int x : other.right) add(x);
        other.left.clear();
        other.right.clear();
    }
};

class Solution {
    unordered_map<string, Group> groups;
    multiset<int> gLeft, gRight;
    
    void addToGlobal(int val) {
        if (gLeft.empty() || val <= *gLeft.rbegin()) {
            gLeft.insert(val);
        } else {
            gRight.insert(val);
        }
        rebalanceGlobal();
    }
    
    void removeFromGlobal(int val) {
        auto it = gLeft.find(val);
        if (it != gLeft.end()) {
            gLeft.erase(it);
        } else {
            it = gRight.find(val);
            if (it != gRight.end()) gRight.erase(it);
        }
        rebalanceGlobal();
    }
    
    void rebalanceGlobal() {
        while (gLeft.size() > gRight.size() + 1) {
            gRight.insert(*gLeft.rbegin());
            gLeft.erase(prev(gLeft.end()));
        }
        while (gRight.size() > gLeft.size()) {
            gLeft.insert(*gRight.begin());
            gRight.erase(gRight.begin());
        }
    }
    
public:
    vector<string> processOperations(const vector<vector<string>>& operations) {
        vector<string> results;
        
        for (const auto& op : operations) {
            if (op[0] == "NEW") {
                string id = op[1];
                Group g;
                for (size_t i = 2; i < op.size(); i++) {
                    g.add(stoi(op[i]));
                }
                groups[id] = g;
                if (g.size() > 0) addToGlobal(g.getMedian());
                
            } else if (op[0] == "ADD") {
                string id = op[1];
                int x = stoi(op[2]);
                if (groups.count(id)) {
                    if (groups[id].size() > 0) removeFromGlobal(groups[id].getMedian());
                    groups[id].add(x);
                    if (groups[id].size() > 0) addToGlobal(groups[id].getMedian());
                }
                
            } else if (op[0] == "MERGE") {
                string id1 = op[1];
                string id2 = op[2];
                if (groups.count(id1) && groups.count(id2)) {
                    if (groups[id1].size() > 0) removeFromGlobal(groups[id1].getMedian());
                    if (groups[id2].size() > 0) removeFromGlobal(groups[id2].getMedian());
                    
                    if (groups[id1].size() < groups[id2].size()) {
                        groups[id2].mergeFrom(groups[id1]);
                        groups[id1] = move(groups[id2]); // Move content
                    } else {
                        groups[id1].mergeFrom(groups[id2]);
                    }
                    groups.erase(id2);
                    if (groups[id1].size() > 0) addToGlobal(groups[id1].getMedian());
                }
                
            } else if (op[0] == "QUERY") {
                if (gLeft.empty()) results.push_back("EMPTY");
                else results.push_back(to_string(*gLeft.rbegin()));
            }
        }
        return results;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int q;
    if (cin >> q) {
        vector<vector<string>> operations;
        for (int i = 0; i < q; i++) {
            string op;
            cin >> op;
            if (op == "NEW") {
                string gid;
                int m;
                cin >> gid >> m;
                vector<string> line = {op, gid};
                for (int j = 0; j < m; j++) {
                    string x;
                    cin >> x;
                    line.push_back(x);
                }
                operations.push_back(line);
            } else if (op == "ADD") {
                string gid, x;
                cin >> gid >> x;
                operations.push_back({op, gid, x});
            } else if (op == "MERGE") {
                string gid1, gid2;
                cin >> gid1 >> gid2;
                operations.push_back({op, gid1, gid2});
            } else {
                operations.push_back({op});
            }
        }
        
        Solution solution;
        vector<string> result = solution.processOperations(operations);
        for (const string& s : result) cout << s << "\n";
    }
    return 0;
}
```

### JavaScript
```javascript
const readline = require("readline");

class PriorityQueue {
  constructor(compare = (a, b) => a - b) {
    this.heap = [];
    this.compare = compare;
  }
  size() { return this.heap.length; }
  isEmpty() { return this.heap.length === 0; }
  peek() { return this.heap[0]; }
  push(val) {
    this.heap.push(val);
    this.bubbleUp(this.heap.length - 1);
  }
  pop() {
    if (this.size() === 0) return null;
    const top = this.heap[0];
    const bottom = this.heap.pop();
    if (this.size() > 0) {
      this.heap[0] = bottom;
      this.bubbleDown(0);
    }
    return top;
  }
  bubbleUp(idx) {
    while (idx > 0) {
      const pIdx = Math.floor((idx - 1) / 2);
      if (this.compare(this.heap[idx], this.heap[pIdx]) < 0) {
        [this.heap[idx], this.heap[pIdx]] = [this.heap[pIdx], this.heap[idx]];
        idx = pIdx;
      } else break;
    }
  }
  bubbleDown(idx) {
    while (true) {
      const left = 2 * idx + 1;
      const right = 2 * idx + 2;
      let swap = null;
      if (left < this.size() && this.compare(this.heap[left], this.heap[idx]) < 0) swap = left;
      if (right < this.size() && this.compare(this.heap[right], swap === null ? this.heap[idx] : this.heap[swap]) < 0) swap = right;
      if (swap === null) break;
      [this.heap[idx], this.heap[swap]] = [this.heap[swap], this.heap[idx]];
      idx = swap;
    }
  }
}

class Group {
  constructor() {
    this.left = new PriorityQueue((a, b) => b - a);
    this.right = new PriorityQueue((a, b) => a - b);
  }
  add(val) {
    if (this.left.isEmpty() || val <= this.left.peek()) {
      this.left.push(val);
    } else {
      this.right.push(val);
    }
    this.rebalance();
  }
  rebalance() {
    while (this.left.size() > this.right.size() + 1) {
      this.right.push(this.left.pop());
    }
    while (this.right.size() > this.left.size()) {
      this.left.push(this.right.pop());
    }
  }
  getMedian() {
    if (this.left.isEmpty()) return 0;
    return this.left.peek();
  }
  size() { return this.left.size() + this.right.size(); }
  getAll() {
    const res = [];
    while (!this.left.isEmpty()) res.push(this.left.pop());
    while (!this.right.isEmpty()) res.push(this.right.pop());
    return res;
  }
}

class Solution {
  processOperations(operations) {
    const groups = new Map();
    const gLeft = new PriorityQueue((a, b) => b - a);
    const gRight = new PriorityQueue((a, b) => a - b);
    
    const gDeletedLeft = new Map();
    const gDeletedRight = new Map();
    const gInLeft = new Map();
    const gInRight = new Map();
    
    let gLeftSize = 0;
    let gRightSize = 0;
    
    const cleanGlobal = () => {
      while (!gLeft.isEmpty() && (gDeletedLeft.get(gLeft.peek()) || 0) > 0) {
        const val = gLeft.pop();
        gDeletedLeft.set(val, gDeletedLeft.get(val) - 1);
      }
      while (!gRight.isEmpty() && (gDeletedRight.get(gRight.peek()) || 0) > 0) {
        const val = gRight.pop();
        gDeletedRight.set(val, gDeletedRight.get(val) - 1);
      }
    };
    
    const rebalanceGlobal = () => {
      while (gLeftSize > gRightSize + 1) {
        cleanGlobal();
        if (gLeft.isEmpty()) break;
        const val = gLeft.pop();
        gInLeft.set(val, (gInLeft.get(val) || 0) - 1);
        
        gRight.push(val);
        gInRight.set(val, (gInRight.get(val) || 0) + 1);
        gLeftSize--;
        gRightSize++;
        cleanGlobal();
      }
      while (gRightSize > gLeftSize) {
        cleanGlobal();
        if (gRight.isEmpty()) break;
        const val = gRight.pop();
        gInRight.set(val, (gInRight.get(val) || 0) - 1);
        
        gLeft.push(val);
        gInLeft.set(val, (gInLeft.get(val) || 0) + 1);
        gLeftSize++;
        gRightSize--;
        cleanGlobal();
      }
    };
    
    const addToGlobal = (val) => {
      cleanGlobal();
      if (gLeft.isEmpty() || val <= gLeft.peek()) {
        gLeft.push(val);
        gInLeft.set(val, (gInLeft.get(val) || 0) + 1);
        gLeftSize++;
      } else {
        gRight.push(val);
        gInRight.set(val, (gInRight.get(val) || 0) + 1);
        gRightSize++;
      }
      rebalanceGlobal();
    };
    
    const removeFromGlobal = (val) => {
      if ((gInLeft.get(val) || 0) > 0) {
        gInLeft.set(val, gInLeft.get(val) - 1);
        gDeletedLeft.set(val, (gDeletedLeft.get(val) || 0) + 1);
        gLeftSize--;
      } else {
        gInRight.set(val, (gInRight.get(val) || 0) - 1);
        gDeletedRight.set(val, (gDeletedRight.get(val) || 0) + 1);
        gRightSize--;
      }
      rebalanceGlobal();
    };
    
    const results = [];
    
    for (const op of operations) {
      const type = op[0];
      if (type === "NEW") {
        const gid = op[1];
        const g = new Group();
        for (let i = 2; i < op.length; i++) g.add(parseInt(op[i]));
        groups.set(gid, g);
        if (g.size() > 0) addToGlobal(g.getMedian());
        
      } else if (type === "ADD") {
        const gid = op[1];
        const x = parseInt(op[2]);
        if (groups.has(gid)) {
          const g = groups.get(gid);
          if (g.size() > 0) removeFromGlobal(g.getMedian());
          g.add(x);
          if (g.size() > 0) addToGlobal(g.getMedian());
        }
        
      } else if (type === "MERGE") {
        const gid1 = op[1];
        const gid2 = op[2];
        if (groups.has(gid1) && groups.has(gid2)) {
          let g1 = groups.get(gid1);
          let g2 = groups.get(gid2);
          
          if (g1.size() > 0) removeFromGlobal(g1.getMedian());
          if (g2.size() > 0) removeFromGlobal(g2.getMedian());
          
          if (g1.size() < g2.size()) {
            const elems = g1.getAll();
            for (const x of elems) g2.add(x);
            groups.set(gid1, g2);
          } else {
            const elems = g2.getAll();
            for (const x of elems) g1.add(x);
          }
          groups.delete(gid2);
          if (groups.get(gid1).size() > 0) addToGlobal(groups.get(gid1).getMedian());
        }
        
      } else if (type === "QUERY") {
        cleanGlobal();
        if (gLeftSize === 0) results.push("EMPTY");
        else results.push(gLeft.peek().toString());
      }
    }
    return results;
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
  const q = parseInt(data[idx++]);
  const operations = [];
  for (let i = 0; i < q; i++) {
    const type = data[idx++];
    if (type === "NEW") {
      const gid = data[idx++];
      const m = parseInt(data[idx++]);
      const vals = [];
      for (let j = 0; j < m; j++) vals.push(data[idx++]);
      operations.push([type, gid, ...vals]);
    } else if (type === "ADD") {
      const gid = data[idx++];
      const x = data[idx++];
      operations.push([type, gid, x]);
    } else if (type === "MERGE") {
      const gid1 = data[idx++];
      const gid2 = data[idx++];
      operations.push([type, gid1, gid2]);
    } else {
      operations.push([type]);
    }
  }
  
  const solution = new Solution();
  const result = solution.processOperations(operations);
  console.log(result.join("\n"));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
NEW 1 2 1 3
NEW 2 1 2
MERGE 1 2
QUERY
```

1. `NEW 1`: `[1, 3]`. Median 1. Global: `{1}`.
2. `NEW 2`: `[2]`. Median 2. Global: `{1, 2}`. Median 1.
3. `MERGE 1 2`:
   - Remove 1, 2 from Global.
   - Merge `[2]` into `[1, 3]`. Group 1: `[1, 2, 3]`. Median 2.
   - Add 2 to Global. Global: `{2}`.
4. `QUERY`: Output 2.

## ✅ Proof of Correctness

### Invariant
- Each group maintains its median correctly using two heaps.
- The global heaps maintain the median of group medians correctly.
- Lazy deletion ensures we don't process stale data.
- Small-to-large merging ensures efficiency.

## 💡 Interview Extensions

- **Extension 1:** Delete group?
  - *Answer:* Just remove its median from global.
- **Extension 2:** Median of all elements (not median of medians)?
  - *Answer:* Much harder with merges. Requires Segment Tree or Fenwick Tree if values are bounded.

### Common Mistakes to Avoid

1. **Lazy Deletion Logic**
   - ❌ Wrong: Decrementing size without checking if element was in Left or Right.
   - ✅ Correct: Infer location based on value vs top, but handle stale tops carefully.
2. **Merge Direction**
   - ❌ Wrong: Always merging 2 into 1 without checking size.
   - ✅ Correct: Merge smaller into larger to avoid `O(N^2)`.

## Related Concepts

- **Median of Medians:** Selection algorithm.
- **Union-Find:** Managing sets.
