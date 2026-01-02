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
time_limit: 2000
memory_limit: 256
---

# HEP-009: Dynamic Median of Medians

## Problem Statement

Maintain multiple groups of numbers. Each group has its own median (lower middle if even). You must support the following operations:

- `NEW id m` followed by `m` integers: create a new group
- `ADD id x`: insert `x` into group `id`
- `MERGE id1 id2`: merge group `id2` into `id1`
- `QUERY`: output the median of the current group medians

If no groups contain elements, output `EMPTY`.

![Problem Illustration](../images/HEP-009/problem-illustration.png)

## Input Format

- First line: integer `q` (number of operations)
- Next operations:
  - `NEW id m` then a line with `m` integers
  - `ADD id x`
  - `MERGE id1 id2`
  - `QUERY`

## Output Format

- For each `QUERY`, output one line with the median of medians or `EMPTY`

## Constraints

- `1 <= q <= 100000`
- `1 <= id <= 100000`
- Total elements across all groups `<= 100000`
- `-10^9 <= value <= 10^9`

## Example

**Input:**

```
4
NEW 1 2
1 3
NEW 2 1
2
MERGE 1 2
QUERY
```

**Output:**

```
2
```

**Explanation:**

After merging, group 1 contains [1, 2, 3]. Its median is 2, which is also the median of all group medians.

![Example Visualization](../images/HEP-009/example-1.png)

## Notes

- Maintain two heaps for each group to track its median
- Track medians globally using another pair of heaps
- Merge smaller group into larger group for efficiency
- Time complexity: O((n + q) log n)
- Space complexity: O(n)

## Related Topics

Heaps, Median Maintenance, Union-Find, Merging

---

## Solution Template

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
        return null;
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
        return 0
    def add(self, val):
        return 0
    def rebalance(self):
        return 0
    def get_median(self):
        return 0
    def size(self):
        return 0
    def get_elements(self):
        return 0
class Solution:
    def process_operations(self, operations: list) -> list:
        return []
def process_operations(operations: list) -> list:
    return []
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
    }
    
    void removeFromGlobal(int val) {
    }
    
    void rebalanceGlobal() {
    }
    
public:
    vector<string> processOperations(const vector<vector<string>>& operations) {
        return "";
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
    return 0;
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

