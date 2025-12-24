---
problem_id: HEP_PRIORITY_QUEUE_DECREASE_KEY__8091
display_id: HEP-016
slug: priority-queue-decrease-key
title: "Priority Queue with Decrease-Key"
difficulty: Medium
difficulty_score: 55
topics:
  - Heaps
  - Priority Queue
  - Data Structures
tags:
  - heaps
  - priority-queue
  - decrease-key
  - medium
premium: true
subscription_tier: basic
---

# HEP-016: Priority Queue with Decrease-Key

## 📋 Problem Summary

Implement a Min-Priority Queue supporting:
1. `INSERT id value`: Add element.
2. `DECREASE id delta`: Reduce value of existing element by `delta`.
3. `EXTRACT`: Remove and return element with minimum value.
   - Tie-breaker: Lexicographically smallest `id`.
   - If empty, return `EMPTY`.

## 🌍 Real-World Scenario

**Scenario Title:** Dijkstra's Algorithm Optimization

In network routing (OSPF) or map navigation (GPS), Dijkstra's algorithm finds the shortest path.
- It maintains a set of "tentative distances" to nodes.
- When a shorter path to a node is found, we must update its priority in the queue.
- This "Decrease Key" operation is critical for performance (`O(E log V)` vs `O(E log V)` with lazy deletion vs `O(E + V log V)` with Fibonacci Heap).
- You are implementing the core data structure that enables efficient pathfinding updates.

![Real-World Application](../images/HEP-016/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Decrease Key Operation

Heap (Min):
      (10, A)
     /       \
 (20, B)   (30, C)

Operation: `DECREASE C 25`.
New Value for C: `30 - 25 = 5`.

Step 1: Update value.
      (10, A)
     /       \
 (20, B)   (5, C)

Step 2: Bubble Up (Percolate Up).
5 < 10. Swap C and A.

      (5, C)
     /      \
 (20, B)  (10, A)

Result: Heap property restored.

### Key Concept: Index Map

Standard Binary Heaps support `push` and `pop` in `O(log N)`.
To support `decrease-key` in `O(log N)`, we need to find the element in the heap array instantly.
- **Solution:** Maintain a Hash Map `id -> index`.
- `map[id]` stores the current position of `id` in the heap array.
- When swapping elements during bubble-up/down, update the map.

### Lazy Deletion vs. Explicit Decrease Key

- **Lazy Deletion:** When updating, just push a new pair `(new_val, id)`. When popping, ignore stale entries.
  - Pros: Easy to implement with standard library PQ.
  - Cons: Heap size grows to `O(Operations)`. Space overhead.
- **Explicit Decrease Key:** Modify the element in place and re-heapify.
  - Pros: Heap size stays `O(N)`. Optimal space.
  - Cons: Requires custom Heap implementation with index tracking.
  - **This problem requires Explicit Decrease Key** (implied by "Implement a priority queue" and efficiency context, though lazy deletion can pass on looser constraints). Given "Medium" and specific operations, a custom heap is the intended educational goal.

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** `INSERT`, `DECREASE`, `EXTRACT`.
- **Output:** `value id` or `EMPTY`.
- **Tie-Breaking:** If values equal, smaller `id` string comes first.
- **Constraints:** IDs are alphanumeric. Values fit in integer.

## Naive Approach

### Intuition

Use a list. Scan for min (`O(N)`). Scan for ID to update (`O(N)`).

### Time Complexity

- **O(Q * N)**: Too slow.

## Optimal Approach

### Key Insight

Custom Binary Heap with a `Map<String, Integer>` to track indices.

### Algorithm

1. **Data Structures:**
   - `heap`: Array of `Node { id, value }`.
   - `pos`: Map `id -> index in heap`.
2. **INSERT(id, val):**
   - Add to end of `heap`.
   - Update `pos`.
   - `bubbleUp(size - 1)`.
3. **DECREASE(id, delta):**
   - Find index `i = pos[id]`.
   - `heap[i].value -= delta`.
   - `bubbleUp(i)`.
4. **EXTRACT:**
   - If empty, return `EMPTY`.
   - Result = `heap[0]`.
   - Remove `id` from `pos`.
   - Move last element to `heap[0]`. Update its `pos`.
   - `bubbleDown(0)`.
   - Return Result.
5. **Bubble Up/Down:**
   - Standard heap logic.
   - **Crucial:** When swapping `i` and `j`, update `pos[heap[i].id]` and `pos[heap[j].id]`.
   - **Comparator:** `val1 < val2` OR `val1 == val2 && id1 < id2`.

### Time Complexity

- **O(Q log N)**.

### Space Complexity

- **O(N)**.

![Algorithm Visualization](../images/HEP-016/algorithm-visualization.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    static class Node {
        String id;
        long value;
        public Node(String id, long value) {
            this.id = id;
            this.value = value;
        }
    }
    
    // Custom Min Heap
    List<Node> heap = new ArrayList<>();
    Map<String, Integer> pos = new HashMap<>();
    
    private void swap(int i, int j) {
        Node n1 = heap.get(i);
        Node n2 = heap.get(j);
        
        heap.set(i, n2);
        heap.set(j, n1);
        
        pos.put(n1.id, j);
        pos.put(n2.id, i);
    }
    
    private boolean less(int i, int j) {
        Node n1 = heap.get(i);
        Node n2 = heap.get(j);
        if (n1.value != n2.value) {
            return n1.value < n2.value;
        }
        return n1.id.compareTo(n2.id) < 0;
    }
    
    private void bubbleUp(int k) {
        while (k > 0) {
            int p = (k - 1) / 2;
            if (less(k, p)) {
                swap(k, p);
                k = p;
            } else {
                break;
            }
        }
    }
    
    private void bubbleDown(int k) {
        int half = heap.size() / 2;
        while (k < half) {
            int child = 2 * k + 1;
            int right = child + 1;
            if (right < heap.size() && less(right, child)) {
                child = right;
            }
            if (less(child, k)) {
                swap(k, child);
                k = child;
            } else {
                break;
            }
        }
    }
    
    public List<String> processOperations(List<String[]> operations) {
        List<String> results = new ArrayList<>();
        heap.clear();
        pos.clear();
        
        for (String[] op : operations) {
            String type = op[0];
            if (type.equals("INSERT")) {
                String id = op[1];
                long val = Long.parseLong(op[2]);
                Node node = new Node(id, val);
                heap.add(node);
                pos.put(id, heap.size() - 1);
                bubbleUp(heap.size() - 1);
            } else if (type.equals("DECREASE")) {
                String id = op[1];
                long delta = Long.parseLong(op[2]);
                if (pos.containsKey(id)) {
                    int idx = pos.get(id);
                    heap.get(idx).value -= delta;
                    bubbleUp(idx);
                }
            } else if (type.equals("EXTRACT")) {
                if (heap.isEmpty()) {
                    results.add("EMPTY");
                } else {
                    Node min = heap.get(0);
                    results.add(min.value + " " + min.id);
                    
                    int lastIdx = heap.size() - 1;
                    Node last = heap.remove(lastIdx);
                    pos.remove(min.id);
                    
                    if (lastIdx > 0) {
                        heap.set(0, last);
                        pos.put(last.id, 0);
                        bubbleDown(0);
                    }
                }
            }
        }
        return results;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int q = sc.nextInt();
            List<String[]> operations = new ArrayList<>();
            for (int i = 0; i < q; i++) {
                String op = sc.next();
                if (op.equals("INSERT")) {
                    String id = sc.next();
                    String value = sc.next();
                    operations.add(new String[]{op, id, value});
                } else if (op.equals("DECREASE")) {
                    String id = sc.next();
                    String delta = sc.next();
                    operations.add(new String[]{op, id, delta});
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

class Solution:
    def process_operations(self, operations: list) -> list:
        heap = [] # List of [value, id]
        pos = {}  # id -> index
        
        def swap(i, j):
            heap[i], heap[j] = heap[j], heap[i]
            pos[heap[i][1]] = i
            pos[heap[j][1]] = j
            
        def less(i, j):
            # Compare heap[i] and heap[j]
            # Tie-break: smaller id
            v1, id1 = heap[i]
            v2, id2 = heap[j]
            if v1 != v2:
                return v1 < v2
            return id1 < id2
            
        def bubble_up(k):
            while k > 0:
                p = (k - 1) // 2
                if less(k, p):
                    swap(k, p)
                    k = p
                else:
                    break
                    
        def bubble_down(k):
            n = len(heap)
            while True:
                left = 2 * k + 1
                if left >= n:
                    break
                child = left
                right = left + 1
                if right < n and less(right, left):
                    child = right
                
                if less(child, k):
                    swap(k, child)
                    k = child
                else:
                    break
                    
        results = []
        
        for op in operations:
            type = op[0]
            if type == "INSERT":
                gid = op[1]
                val = int(op[2])
                heap.append([val, gid])
                pos[gid] = len(heap) - 1
                bubble_up(len(heap) - 1)
                
            elif type == "DECREASE":
                gid = op[1]
                delta = int(op[2])
                if gid in pos:
                    idx = pos[gid]
                    heap[idx][0] -= delta
                    bubble_up(idx)
                    
            elif type == "EXTRACT":
                if not heap:
                    results.append("EMPTY")
                else:
                    val, gid = heap[0]
                    results.append(f"{val} {gid}")
                    
                    last = heap.pop()
                    del pos[gid]
                    
                    if heap:
                        heap[0] = last
                        pos[last[1]] = 0
                        bubble_down(0)
                        
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
            if op == "INSERT":
                gid = next(it)
                val = next(it)
                operations.append([op, gid, val])
            elif op == "DECREASE":
                gid = next(it)
                delta = next(it)
                operations.append([op, gid, delta])
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
#include <unordered_map>

using namespace std;

struct Node {
    string id;
    long long value;
};

class Solution {
    vector<Node> heap;
    unordered_map<string, int> pos;
    
    bool less(int i, int j) {
        if (heap[i].value != heap[j].value) {
            return heap[i].value < heap[j].value;
        }
        return heap[i].id < heap[j].id;
    }
    
    void swapNodes(int i, int j) {
        swap(heap[i], heap[j]);
        pos[heap[i].id] = i;
        pos[heap[j].id] = j;
    }
    
    void bubbleUp(int k) {
        while (k > 0) {
            int p = (k - 1) / 2;
            if (less(k, p)) {
                swapNodes(k, p);
                k = p;
            } else {
                break;
            }
        }
    }
    
    void bubbleDown(int k) {
        int n = heap.size();
        while (true) {
            int left = 2 * k + 1;
            if (left >= n) break;
            int child = left;
            int right = left + 1;
            if (right < n && less(right, left)) {
                child = right;
            }
            if (less(child, k)) {
                swapNodes(k, child);
                k = child;
            } else {
                break;
            }
        }
    }

public:
    vector<string> processOperations(const vector<vector<string>>& operations) {
        vector<string> results;
        heap.clear();
        pos.clear();
        
        for (const auto& op : operations) {
            if (op[0] == "INSERT") {
                string id = op[1];
                long long val = stoll(op[2]);
                heap.push_back({id, val});
                pos[id] = heap.size() - 1;
                bubbleUp(heap.size() - 1);
            } else if (op[0] == "DECREASE") {
                string id = op[1];
                long long delta = stoll(op[2]);
                if (pos.count(id)) {
                    int idx = pos[id];
                    heap[idx].value -= delta;
                    bubbleUp(idx);
                }
            } else if (op[0] == "EXTRACT") {
                if (heap.empty()) {
                    results.push_back("EMPTY");
                } else {
                    Node minNode = heap[0];
                    results.push_back(to_string(minNode.value) + " " + minNode.id);
                    
                    pos.erase(minNode.id);
                    Node last = heap.back();
                    heap.pop_back();
                    
                    if (!heap.empty()) {
                        heap[0] = last;
                        pos[last.id] = 0;
                        bubbleDown(0);
                    }
                }
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
            if (op == "INSERT") {
                string id, val;
                cin >> id >> val;
                operations.push_back({op, id, val});
            } else if (op == "DECREASE") {
                string id, delta;
                cin >> id >> delta;
                operations.push_back({op, id, delta});
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

class Solution {
  constructor() {
    this.heap = []; // {id, value}
    this.pos = new Map(); // id -> index
  }
  
  swap(i, j) {
    const t = this.heap[i];
    this.heap[i] = this.heap[j];
    this.heap[j] = t;
    
    this.pos.set(this.heap[i].id, i);
    this.pos.set(this.heap[j].id, j);
  }
  
  less(i, j) {
    const n1 = this.heap[i];
    const n2 = this.heap[j];
    if (n1.value !== n2.value) {
      return n1.value < n2.value;
    }
    return n1.id < n2.id;
  }
  
  bubbleUp(k) {
    while (k > 0) {
      const p = Math.floor((k - 1) / 2);
      if (this.less(k, p)) {
        this.swap(k, p);
        k = p;
      } else {
        break;
      }
    }
  }
  
  bubbleDown(k) {
    const n = this.heap.length;
    while (true) {
      const left = 2 * k + 1;
      if (left >= n) break;
      let child = left;
      const right = left + 1;
      if (right < n && this.less(right, left)) {
        child = right;
      }
      if (this.less(child, k)) {
        this.swap(k, child);
        k = child;
      } else {
        break;
      }
    }
  }
  
  processOperations(operations) {
    const results = [];
    this.heap = [];
    this.pos.clear();
    
    for (const op of operations) {
      const type = op[0];
      if (type === "INSERT") {
        const id = op[1];
        const val = BigInt(op[2]);
        this.heap.push({ id, value: val });
        this.pos.set(id, this.heap.length - 1);
        this.bubbleUp(this.heap.length - 1);
      } else if (type === "DECREASE") {
        const id = op[1];
        const delta = BigInt(op[2]);
        if (this.pos.has(id)) {
          const idx = this.pos.get(id);
          this.heap[idx].value -= delta;
          this.bubbleUp(idx);
        }
      } else if (type === "EXTRACT") {
        if (this.heap.length === 0) {
          results.push("EMPTY");
        } else {
          const min = this.heap[0];
          results.push(`${min.value} ${min.id}`);
          
          this.pos.delete(min.id);
          const last = this.heap.pop();
          
          if (this.heap.length > 0) {
            this.heap[0] = last;
            this.pos.set(last.id, 0);
            this.bubbleDown(0);
          }
        }
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
    if (type === "INSERT") {
      const id = data[idx++];
      const val = data[idx++];
      operations.push([type, id, val]);
    } else if (type === "DECREASE") {
      const id = data[idx++];
      const delta = data[idx++];
      operations.push([type, id, delta]);
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
INSERT id1 5
INSERT id2 3
DECREASE id1 4
EXTRACT
EXTRACT
```

1. `INSERT id1 5`: Heap `[(5, id1)]`. Map `{id1: 0}`.
2. `INSERT id2 3`: Heap `[(5, id1), (3, id2)]`. Bubble up `(3, id2)`.
   - Swap. Heap `[(3, id2), (5, id1)]`. Map `{id2: 0, id1: 1}`.
3. `DECREASE id1 4`:
   - `pos[id1] = 1`.
   - `heap[1].value = 5 - 4 = 1`.
   - Bubble up index 1.
   - `(1, id1)` vs `(3, id2)`. 1 < 3. Swap.
   - Heap `[(1, id1), (3, id2)]`. Map `{id1: 0, id2: 1}`.
4. `EXTRACT`:
   - Min `(1, id1)`. Output `1 id1`.
   - Move last `(3, id2)` to 0. Remove last.
   - Heap `[(3, id2)]`. Map `{id2: 0}`.
   - Bubble down 0. No children.
5. `EXTRACT`:
   - Min `(3, id2)`. Output `3 id2`.
   - Empty.

Output matches example.

## ✅ Proof of Correctness

### Invariant
- The binary heap property (parent <= child) is maintained after every operation.
- The `pos` map always correctly points to the index of each ID in the heap array, allowing `O(1)` access for updates.

## 💡 Interview Extensions

- **Extension 1:** Increase Key?
  - *Answer:* Similar, but bubble down.
- **Extension 2:** Delete arbitrary ID?
  - *Answer:* Decrease key to `-infinity`, then extract min.

### Common Mistakes to Avoid

1. **Map Sync**
   - ❌ Wrong: Forgetting to update map during swap.
   - ✅ Correct: Update map for BOTH swapped elements.
2. **Tie-Breaking**
   - ❌ Wrong: Ignoring IDs when values equal.
   - ✅ Correct: Use ID string comparison as secondary key.

## Related Concepts

- **Dijkstra/Prim:** Uses this exact structure.
- **Fibonacci Heap:** Theoretical optimization.
