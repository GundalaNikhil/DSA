---
problem_id: HEP_K_CLOSEST_STREAM_WEIGHT__4950
display_id: HEP-011
slug: k-closest-stream-weight
title: "K Closest Points to Origin (Stream) with Weight"
difficulty: Medium
difficulty_score: 53
topics:
  - Heaps
  - Streaming
  - Geometry
tags:
  - heaps
  - streaming
  - geometry
  - medium
premium: true
subscription_tier: basic
---

# HEP-011: K Closest Points to Origin (Stream) with Weight

## 📋 Problem Summary

You receive a stream of points `(x, y)` with weight `w`.
Weighted distance $D = (x^2 + y^2) / w$.
Maintain the `k` points with the smallest $D$.
On `QUERY`, return IDs of these `k` points sorted by distance (asc).
IDs are 1-based, assigned sequentially.

## 🌍 Real-World Scenario

**Scenario Title:** Emergency Response Prioritization

Imagine an emergency dispatch system.
- Incidents occur at locations `(x, y)`.
- `w` represents urgency or priority (higher `w` means more urgent).
- The "cost" to respond is proportional to distance but inversely proportional to urgency.
- A high-priority incident far away might still be "closer" in terms of response rank than a low-priority incident nearby.
- You want to keep track of the top `k` incidents to dispatch units to.

![Real-World Application](../images/HEP-011/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Heap Maintenance

`k=2`.
Stream:
1. ID 1: `(1,1), w=1`. $D = 2/1 = 2$. Heap: `[(2, 1)]`.
2. ID 2: `(2,2), w=1`. $D = 8/1 = 8$. Heap: `[(8, 2), (2, 1)]` (Max-Heap).
3. ID 3: `(1,1), w=10`. $D = 2/10 = 0.2$.
   - Heap full. Max is 8 (ID 2).
   - $0.2 < 8$. Pop 8. Push 0.2.
   - Heap: `[(2, 1), (0.2, 3)]`.

Query: Sort heap. `(0.2, 3), (2, 1)`. Output: `3 1`.

### Key Concept: Max-Heap for Top K Smallest

To keep the `k` *smallest* values, we use a **Max-Heap** of size `k`.
- The root of the Max-Heap is the largest of the `k` smallest.
- When a new value comes:
  - If heap size < k: Push.
  - If heap size == k: Compare new value with root.
    - If new < root: Pop root, Push new.
    - Else: Ignore new (it's larger than the k-th smallest).

### Floating Point Precision

The distance is $(x^2 + y^2) / w$.
Comparing $A/B$ vs $C/D$:
- Avoid division.
- Check $A \cdot D < C \cdot B$.
- Use `long` (64-bit integer) for cross-multiplication to avoid precision issues.
- $x, y \le 10^6 \implies x^2+y^2 \approx 2 \cdot 10^{12}$.
- $w \le 10^6$.
- Cross product: $(2 \cdot 10^{12}) \cdot 10^6 = 2 \cdot 10^{18}$.
- Fits in signed 64-bit integer (max $\approx 9 \cdot 10^{18}$).

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** `ADD` and `QUERY`.
- **Output:** IDs.
- **Tie-Breaking:**
  - For `QUERY` output: Ascending distance. If tie, smaller ID first.
  - For Heap maintenance: If new distance == max distance in heap, do we replace?
    - We want the `k` smallest.
    - If tie, we prefer smaller ID?
    - The problem says "break ties by smaller id" for output.
    - Usually, "k closest" implies we want the set of k best.
    - If we have `(Dist=10, ID=5)` in heap (root) and new is `(Dist=10, ID=6)`.
      - 6 is worse than 5 (larger ID). Don't replace.
    - If new is `(Dist=10, ID=4)`.
      - 4 is better than 5. Replace.
    - So, strict ordering: `(D1, ID1) < (D2, ID2)` if `D1 < D2` or `D1 == D2 && ID1 < ID2`.
    - Max-Heap keeps the "worst" of the best.
    - "Worst" means largest Distance, or same Distance and largest ID.

## Naive Approach

### Intuition

Store all points. Sort on query.

### Time Complexity

- **O(Q * N log N)**: Too slow.

## Optimal Approach

### Key Insight

Use Max-Heap of size `k`.
Store objects `Point { long num; long den; int id; }`.
Comparator:
- `compare(a, b)`:
  - `valA = a.num * b.den`
  - `valB = b.num * a.den`
  - If `valA != valB`, return `compare(valA, valB)`.
  - Else return `compare(a.id, b.id)`.

### Algorithm

1. `id_counter = 1`.
2. Max-Heap `pq`.
3. **ADD:**
   - Calculate `num = x*x + y*y`, `den = w`.
   - Create `p = new Point(num, den, id)`.
   - If `pq.size() < k`: `pq.push(p)`.
   - Else:
     - Compare `p` with `pq.peek()`.
     - If `p` is "smaller" (better) than `pq.peek()`:
       - `pq.pop()`.
       - `pq.push(p)`.
   - `id_counter++`.
4. **QUERY:**
   - Create copy of heap elements.
   - Sort copy by "smaller" logic.
   - Output IDs.

### Time Complexity

- **O(Q log K)**.
- Query takes **O(K log K)**.

### Space Complexity

- **O(K)**.

![Algorithm Visualization](../images/HEP-011/algorithm-visualization.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    static class Point implements Comparable<Point> {
        long num, den;
        int id;
        
        public Point(long num, long den, int id) {
            this.num = num;
            this.den = den;
            this.id = id;
        }
        
        // Compare for Max-Heap (Reverse of "Better")
        // We want "Worst" at top.
        // Worst = Larger Distance, or Same Distance + Larger ID.
        @Override
        public int compareTo(Point other) {
            // this vs other
            // distA = num/den, distB = other.num/other.den
            // Compare num*other.den vs other.num*den
            long val1 = this.num * other.den;
            long val2 = other.num * this.den;
            
            if (val1 != val2) {
                return Long.compare(val1, val2);
            }
            return Integer.compare(this.id, other.id);
        }
    }
    
    public List<String> processOperations(int k, List<String[]> operations) {
        PriorityQueue<Point> pq = new PriorityQueue<>(Collections.reverseOrder());
        List<String> results = new ArrayList<>();
        int currentId = 1;
        
        for (String[] op : operations) {
            if (op[0].equals("ADD")) {
                long x = Long.parseLong(op[1]);
                long y = Long.parseLong(op[2]);
                long w = Long.parseLong(op[3]);
                
                Point p = new Point(x * x + y * y, w, currentId++);
                
                if (pq.size() < k) {
                    pq.offer(p);
                } else {
                    Point top = pq.peek();
                    // If p is "better" (smaller) than top, replace.
                    // p < top means p.compareTo(top) < 0
                    if (p.compareTo(top) < 0) {
                        pq.poll();
                        pq.offer(p);
                    }
                }
            } else {
                if (pq.isEmpty()) {
                    results.add("EMPTY");
                } else {
                    List<Point> list = new ArrayList<>(pq);
                    Collections.sort(list); // Sorts ascending (Smallest first)
                    StringBuilder sb = new StringBuilder();
                    for (int i = 0; i < list.size(); i++) {
                        sb.append(list.get(i).id);
                        if (i < list.size() - 1) sb.append(" ");
                    }
                    results.add(sb.toString());
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
            int k = sc.nextInt();
            List<String[]> operations = new ArrayList<>();
            for (int i = 0; i < q; i++) {
                String op = sc.next();
                if (op.equals("ADD")) {
                    String x = sc.next();
                    String y = sc.next();
                    String w = sc.next();
                    operations.add(new String[]{op, x, y, w});
                } else {
                    operations.add(new String[]{op});
                }
            }
            Solution solution = new Solution();
            List<String> result = solution.processOperations(k, operations);
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

class Point:
    def __init__(self, num, den, pid):
        self.num = num
        self.den = den
        self.pid = pid
        
    def __lt__(self, other):
        # Less than means "Better" (Smaller Dist or Smaller ID)
        val1 = self.num * other.den
        val2 = other.num * self.den
        if val1 != val2:
            return val1 < val2
        return self.pid < other.pid
        
    def __eq__(self, other):
        return self.num * other.den == other.num * self.den and self.pid == other.pid

class Solution:
    def process_operations(self, k: int, operations: list) -> list:
        # Max-Heap stores "Worst" elements.
        # Python heapq is Min-Heap.
        # To simulate Max-Heap of Points, we need to invert comparison.
        # Or store wrapper objects.
        # Let's use a wrapper that inverts __lt__.
        
        class MaxHeapItem:
            def __init__(self, p):
                self.p = p
            def __lt__(self, other):
                # We want Max-Heap behavior: pop the LARGEST.
                # heapq pops SMALLEST.
                # So we want "Largest" to be "Smallest" in wrapper.
                # Wrapper A < Wrapper B if A.p > B.p
                return other.p < self.p
        
        pq = [] # Stores MaxHeapItem
        results = []
        current_id = 1
        
        for op in operations:
            if op[0] == "ADD":
                x = int(op[1])
                y = int(op[2])
                w = int(op[3])
                p = Point(x*x + y*y, w, current_id)
                current_id += 1
                
                if len(pq) < k:
                    heapq.heappush(pq, MaxHeapItem(p))
                else:
                    # Peek top (Worst)
                    top = pq[0].p
                    # If p is better than top (p < top), replace
                    if p < top:
                        heapq.heapreplace(pq, MaxHeapItem(p))
                        
            else:
                if not pq:
                    results.append("EMPTY")
                else:
                    # Extract, sort
                    items = [item.p for item in pq]
                    items.sort()
                    res_ids = [str(item.pid) for item in items]
                    results.append(" ".join(res_ids))
                    
        return results

def process_operations(k: int, operations: list) -> list:
    solver = Solution()
    return solver.process_operations(k, operations)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    try:
        q = int(next(it))
        k = int(next(it))
        operations = []
        for _ in range(q):
            op = next(it)
            if op == "ADD":
                x = next(it)
                y = next(it)
                w = next(it)
                operations.append([op, x, y, w])
            else:
                operations.append([op])
        
        result = process_operations(k, operations)
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
#include <algorithm>

using namespace std;

struct Point {
    long long num, den;
    int id;
    
    // operator< for "Better" (Smaller)
    bool operator<(const Point& other) const {
        // val1 = num/den, val2 = other.num/other.den
        // num * other.den < other.num * den
        // Use __int128 for safety if needed, but constraints say long long is enough (10^18)
        long long val1 = num * other.den;
        long long val2 = other.num * den;
        if (val1 != val2) return val1 < val2;
        return id < other.id;
    }
};

// Comparator for Max-Heap (we want "Worst" at top, i.e., Largest)
struct MaxHeapComp {
    bool operator()(const Point& a, const Point& b) {
        // Returns true if a < b (so b is at top)
        // We want "Larger" at top.
        // Standard priority_queue is Max-Heap using <.
        // So if a < b, b is considered "larger" and goes to top.
        // Our < defines "Better".
        // We want "Worse" at top.
        // Worse means Larger Dist or Larger ID.
        // So if a is Better than b, a < b.
        // Then b (Worse) is at top. Correct.
        return a < b;
    }
};

class Solution {
public:
    vector<string> processOperations(int k, const vector<vector<string>>& operations) {
        priority_queue<Point, vector<Point>, MaxHeapComp> pq;
        vector<string> results;
        int currentId = 1;
        
        for (const auto& op : operations) {
            if (op[0] == "ADD") {
                long long x = stoll(op[1]);
                long long y = stoll(op[2]);
                long long w = stoll(op[3]);
                Point p = {x * x + y * y, w, currentId++};
                
                if (pq.size() < k) {
                    pq.push(p);
                } else {
                    const Point& top = pq.top();
                    // If p is Better than top (p < top), replace
                    if (p < top) {
                        pq.pop();
                        pq.push(p);
                    }
                }
            } else {
                if (pq.empty()) {
                    results.push_back("EMPTY");
                } else {
                    vector<Point> temp;
                    // Copy heap
                    priority_queue<Point, vector<Point>, MaxHeapComp> copy = pq;
                    while (!copy.empty()) {
                        temp.push_back(copy.top());
                        copy.pop();
                    }
                    // Sort by Better (Ascending)
                    sort(temp.begin(), temp.end());
                    
                    string line = "";
                    for (size_t i = 0; i < temp.size(); i++) {
                        if (i > 0) line += " ";
                        line += to_string(temp[i].id);
                    }
                    results.push_back(line);
                }
            }
        }
        return results;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int q, k;
    if (cin >> q >> k) {
        vector<vector<string>> operations;
        for (int i = 0; i < q; i++) {
            string op;
            cin >> op;
            if (op == "ADD") {
                string x, y, w;
                cin >> x >> y >> w;
                operations.push_back({op, x, y, w});
            } else {
                operations.push_back({op});
            }
        }
        
        Solution solution;
        vector<string> result = solution.processOperations(k, operations);
        for (const string& s : result) cout << s << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class PriorityQueue {
  constructor(compare) {
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

class Solution {
  processOperations(k, operations) {
    // Max-Heap: Compare(a, b) < 0 means a should be above b.
    // We want "Worse" (Larger) at top.
    // So if a > b, a should be above.
    // compare(a, b) should return -1 if a > b.
    const pq = new PriorityQueue((a, b) => {
      // Compare a vs b.
      // valA = a.num * b.den
      // valB = b.num * a.den
      const valA = a.num * b.den;
      const valB = b.num * a.den;
      
      if (valA > valB) return -1; // a is larger (worse), so a up
      if (valA < valB) return 1;
      if (a.id > b.id) return -1; // a is larger id (worse), so a up
      if (a.id < b.id) return 1;
      return 0;
    });
    
    const results = [];
    let currentId = 1;
    
    for (const op of operations) {
      if (op[0] === "ADD") {
        const x = BigInt(op[1]);
        const y = BigInt(op[2]);
        const w = BigInt(op[3]);
        const p = { num: x * x + y * y, den: w, id: currentId++ };
        
        if (pq.size() < k) {
          pq.push(p);
        } else {
          const top = pq.peek();
          // Check if p is better than top
          // p < top
          const valP = p.num * top.den;
          const valTop = top.num * p.den;
          
          let isBetter = false;
          if (valP < valTop) isBetter = true;
          else if (valP === valTop && p.id < top.id) isBetter = true;
          
          if (isBetter) {
            pq.pop();
            pq.push(p);
          }
        }
      } else {
        if (pq.isEmpty()) {
          results.push("EMPTY");
        } else {
          const list = [];
          // Copy heap
          const tempPQ = new PriorityQueue(pq.compare);
          pq.heap.forEach(item => tempPQ.push(item));
          while (!tempPQ.isEmpty()) list.push(tempPQ.pop());
          
          // List comes out Worst to Best (because pop removes top)
          // Wait, pop removes root (Worst).
          // So we get Worst, 2nd Worst...
          // We want Best to Worst (Ascending).
          // So reverse the list.
          list.reverse();
          
          results.push(list.map(item => item.id).join(" "));
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
  const k = parseInt(data[idx++]);
  const operations = [];
  for (let i = 0; i < q; i++) {
    const type = data[idx++];
    if (type === "ADD") {
      const x = data[idx++];
      const y = data[idx++];
      const w = data[idx++];
      operations.push([type, x, y, w]);
    } else {
      operations.push([type]);
    }
  }
  
  const solution = new Solution();
  const result = solution.processOperations(k, operations);
  console.log(result.join("\n"));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:** `3 1`.
1. `ADD 1 1 1`: $D=2$. ID=1. Heap: `[(2, 1)]`.
2. `ADD 2 2 1`: $D=8$. ID=2.
   - Heap full (k=1). Top is `(2, 1)`.
   - New `(8, 2)`. Is 8 < 2? No. Ignore.
   - Heap: `[(2, 1)]`.
3. `QUERY`: Output `1`.

Wait, example output says `1`.
My manual trace:
- `ADD 1 1 1` -> Dist 2.
- `ADD 2 2 1` -> Dist 8.
- k=1. We want smallest.
- Heap has `(2, 1)`.
- New is `(8, 2)`.
- `8 > 2`. New is worse. Keep `(2, 1)`.
- Query: `1`. Correct.

**Another Case:** k=2.
1. `ADD 1 1 1` (2, 1). Heap: `[(2, 1)]`.
2. `ADD 2 2 1` (8, 2). Heap: `[(8, 2), (2, 1)]`. (Max at top: 8).
3. `ADD 1 1 10` (0.2, 3).
   - Top is 8.
   - 0.2 < 8. Replace.
   - Heap: `[(2, 1), (0.2, 3)]`. (Max at top: 2).
4. `QUERY`: Sort `(0.2, 3), (2, 1)`. Output `3 1`.

## ✅ Proof of Correctness

### Invariant
- The Max-Heap maintains the `k` smallest elements seen so far.
- The root is the largest of these `k`.
- Any new element smaller than the root belongs in the set of `k` smallest, replacing the root.

## 💡 Interview Extensions

- **Extension 1:** Weighted median?
  - *Answer:* Two heaps (min/max) balancing weights.
- **Extension 2:** Moving window?
  - *Answer:* Sliding window logic with lazy deletion.

## Common Mistakes to Avoid

1. **Floating Point Errors**
   - ❌ Wrong: `double dist = (x*x+y*y)/w`.
   - ✅ Correct: Cross-multiplication `a.num * b.den < b.num * a.den`.
2. **Heap Direction**
   - ❌ Wrong: Min-Heap for top k smallest (keeps k largest).
   - ✅ Correct: Max-Heap to evict large elements.

## Related Concepts

- **Top K Elements:** Standard heap pattern.
- **Streaming Algorithms:** Reservoir sampling (related).
