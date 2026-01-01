---
problem_id: HEP_RUNNING_MEDIAN_DELETE_THRESHOLD__4217
display_id: HEP-001
slug: running-median-with-delete-threshold
title: "Running Median with Delete and Threshold"
difficulty: Medium
difficulty_score: 55
topics:
  - Heaps
  - Median
  - Data Streams
tags:
  - heaps
  - median
  - lazy-deletion
  - medium
premium: true
subscription_tier: basic
---

# HEP-001: Running Median with Delete and Threshold

## 📋 Problem Summary

You need to maintain a multiset of integers supporting `ADD`, `DEL`, and `MEDIAN` operations.
- `ADD x`: Insert `x`.
- `DEL x`: Remove one instance of `x`.
- `MEDIAN`: Return the median if the size is at least `T`. If empty, return `EMPTY`. If size < `T`, return `NA`.

## 🌍 Real-World Scenario

**Scenario Title:** Real-Time Sensor Data Filtering

Imagine a monitoring system for a nuclear reactor.
- Sensors stream temperature readings continuously (`ADD`).
- Occasionally, a sensor reading is flagged as erroneous and retracted (`DEL`).
- To monitor the "typical" temperature, you need the **Median**.
- However, calculating the median is only statistically significant if you have enough data points (Threshold `T`). If you have too few readings, reporting a median is misleading (`NA`).

![Real-World Application](../images/HEP-001/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Two Heaps Approach

We use two heaps:
1. **Max-Heap (Left):** Stores the smaller half of numbers.
2. **Min-Heap (Right):** Stores the larger half of numbers.

Invariant:
- `size(Left) == size(Right)` OR `size(Left) == size(Right) + 1`.
- All elements in `Left` <= All elements in `Right`.

```text
       Left (Max-Heap)       Right (Min-Heap)
           [5]                    [8]
          /   \                  /   \
        [3]   [2]              [10]  [12]

Median = Top of Left (5)
```

**Lazy Deletion:**
Since standard heaps don't support efficient arbitrary deletion, we use **Lazy Deletion**.
- When `DEL x` comes, we don't search and remove `x` immediately (`O(N)`).
- Instead, we record that `x` is "to be deleted" in a frequency map (`debt`).
- We only physically remove `x` from the top of the heap when it surfaces during `top()` or `pop()` operations.
- We maintain `valid_size` variables for each heap to track the count of non-deleted elements.

### Key Concept: Balancing Heaps with Lazy Deletion

1. **Add:** Push to appropriate heap. Rebalance.
2. **Delete:** Increment debt count. Update valid sizes. **Do not rebalance yet.** Rebalancing happens only if the valid size difference violates the invariant.
3. **Median:**
   - Clean the tops of both heaps (remove "dead" elements).
   - Ensure balance (move elements if needed).
   - Return `Left.top()`.

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** Operations list.
- **Output:** Strings for `MEDIAN` queries.
- **Constraints:** `Q <= 10^5`, Values up to `10^9`.
- **Median Definition:** Lower middle. If sorted array is `[1, 2, 3, 4]`, median is `2`.

## Naive Approach

### Intuition

Maintain a sorted list.
- `ADD`: Insert in sorted order (`O(N)`).
- `DEL`: Remove (`O(N)`).
- `MEDIAN`: Access middle (`O(1)`).

### Time Complexity

- **O(Q * N)**: Too slow for `10^5` operations.

## Optimal Approach

### Key Insight

Use **Two Heaps** with **Lazy Deletion**.
- `ADD`: `O(log N)`.
- `DEL`: `O(log N)` (amortized).
- `MEDIAN`: `O(1)` (after cleaning).

### Algorithm

1. `maxHeap` (Left), `minHeap` (Right).
2. `debt` map: stores counts of deleted numbers.
3. `balance` variable: `valid_left - valid_right`.
4. **ADD(x):**
   - If `x <= maxHeap.top()`, push to Left. Else Right.
   - Update `balance`.
   - Rebalance if `balance` is not 0 or 1.
5. **DEL(x):**
   - Increment `debt[x]`.
   - Determine which heap `x` "belongs" to (conceptually) to update `balance`.
     - *Tricky part:* We don't know if the specific instance of `x` we are deleting is in Left or Right if `x` can be in both.
     - *Better Strategy:* Just track global valid count. For balancing, we rely on the `size()` of heaps including dead elements, but clean tops frequently.
     - *Refined Strategy:*
       - Push `x` to `debt`.
       - If `x <= current_median`, decrement `valid_left`. Else `valid_right`.
       - Rebalance based on `valid_left` and `valid_right`.
6. **Rebalance:**
   - While `valid_left > valid_right + 1`: Move from Left to Right.
   - While `valid_right > valid_left`: Move from Right to Left.
   - *Crucial:* Before moving an element from top of heap, **clean** the heap (pop deleted elements).

### Time Complexity

- **O(Q log N)**.

### Space Complexity

- **O(N)**.

![Algorithm Visualization](../images/HEP-001/algorithm-visualization.png)

## Implementations

### Java
```java
import java.util.*;

class Solution {
    private PriorityQueue<Integer> left; // Max heap
    private PriorityQueue<Integer> right; // Min heap
    private Map<Integer, Integer> leftDebt;
    private Map<Integer, Integer> rightDebt;
    private Map<Integer, Integer> globalCounts;
    private int validLeft, validRight;

    public List<String> processOperations(int T, List<String[]> operations) {
        left = new PriorityQueue<>(Collections.reverseOrder());
        right = new PriorityQueue<>();
        leftDebt = new HashMap<>();
        rightDebt = new HashMap<>();
        globalCounts = new HashMap<>();
        validLeft = 0;
        validRight = 0;
        
        List<String> results = new ArrayList<>();
        
        for (String[] op : operations) {
            String type = op[0];
            if (type.equals("ADD")) {
                int x = Integer.parseInt(op[1]);
                globalCounts.put(x, globalCounts.getOrDefault(x, 0) + 1);
                add(x);
            } else if (type.equals("DEL")) {
                int x = Integer.parseInt(op[1]);
                if (globalCounts.getOrDefault(x, 0) > 0) {
                    globalCounts.put(x, globalCounts.get(x) - 1);
                    del(x);
                }
            } else {
                results.add(getMedian(T));
            }
        }
        return results;
    }
    
    private void add(int x) {
        cleanLeft();
        if (left.isEmpty() || x <= left.peek()) {
            left.offer(x);
            validLeft++;
        } else {
            right.offer(x);
            validRight++;
        }
        rebalance();
    }
    
    private void del(int x) {
        cleanLeft();
        cleanRight();
        
        boolean inLeft = false;
        if (!left.isEmpty() && x <= left.peek()) inLeft = true;
        else inLeft = false;
        
        if (inLeft) {
            leftDebt.put(x, leftDebt.getOrDefault(x, 0) + 1);
            validLeft--;
        } else {
            rightDebt.put(x, rightDebt.getOrDefault(x, 0) + 1);
            validRight--;
        }
        
        rebalance();
    }
    
    private String getMedian(int T) {
        cleanLeft();
        
        int total = validLeft + validRight;
        if (total == 0) return "EMPTY";
        if (total < T) return "NA";
        
        // Safety check for empty queue though logic implies it shouldn't be empty if total > 0
        if (left.isEmpty()) return "EMPTY"; 
        return String.valueOf(left.peek());
    }
    
    private void rebalance() {
        // Invariant: validLeft == validRight OR validLeft == validRight + 1
        
        cleanLeft();
        cleanRight();
        
        while (validLeft > validRight + 1) {
            cleanLeft(); // ensure top is valid
            if (left.isEmpty()) break; 
            int val = left.poll();
            validLeft--;
            right.offer(val);
            validRight++;
            cleanLeft();
        }
        
        cleanRight();
        while (validRight > validLeft) {
            cleanRight(); // ensure top is valid
            if (right.isEmpty()) break;
            int val = right.poll();
            validRight--;
            left.offer(val);
            validLeft++;
            cleanRight();
        }
    }
    
    private void cleanLeft() {
        while (!left.isEmpty() && leftDebt.getOrDefault(left.peek(), 0) > 0) {
            int val = left.poll();
            leftDebt.put(val, leftDebt.get(val) - 1);
        }
    }

    private void cleanRight() {
        while (!right.isEmpty() && rightDebt.getOrDefault(right.peek(), 0) > 0) {
            int val = right.poll();
            rightDebt.put(val, rightDebt.get(val) - 1);
        }
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int q = sc.nextInt();
            int T = sc.nextInt();
            List<String[]> operations = new ArrayList<>();
            for (int i = 0; i < q; i++) {
                String op = sc.next();
                if (op.equals("ADD") || op.equals("DEL")) {
                    String x = sc.next();
                    operations.add(new String[]{op, x});
                } else {
                    operations.add(new String[]{op});
                }
            }
            Solution solution = new Solution();
            List<String> result = solution.processOperations(T, operations);
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

class Solution:
    def process_operations(self, T: int, operations: list) -> list:
        # Left is max heap (store negative values), Right is min heap
        left = []
        right = []
       
        left_debt = defaultdict(int)
        right_debt = defaultdict(int)
        
        # logical counts
        l_cnt = 0
        r_cnt = 0
        
        results = []
        
        def clean_left():
            while left and left_debt[-left[0]] > 0:
                val = -heapq.heappop(left)
                left_debt[val] -= 1

        def clean_right():
            while right and right_debt[right[0]] > 0:
                val = heapq.heappop(right)
                right_debt[val] -= 1
        
        def balance():
            # maximize l_cnt, r_cnt constraint: 
            # l_cnt == r_cnt OR l_cnt == r_cnt + 1
            
            # Clean first to ensure tops are valid candidates for moving
            clean_left()
            clean_right()
            
            nonlocal l_cnt, r_cnt
            
            while l_cnt > r_cnt + 1:
                clean_left() # ensure we move a valid item
                val = -heapq.heappop(left)
                heapq.heappush(right, val)
                l_cnt -= 1
                r_cnt += 1
                clean_left()
                
            clean_right()
            while r_cnt > l_cnt:
                clean_right()
                val = heapq.heappop(right)
                heapq.heappush(left, -val)
                r_cnt -= 1
                l_cnt += 1
                clean_right()

        counts = defaultdict(int)
        for op_data in operations:
            op = op_data[0]
            
            if op == "ADD":
                x = int(op_data[1])
                counts[x] += 1
                # Naive push then balance
                # Push to left first? Or compare with left top?
                
                clean_left()
                if not left or x <= -left[0]:
                    heapq.heappush(left, -x)
                    l_cnt += 1
                else:
                    heapq.heappush(right, x)
                    r_cnt += 1
                
                balance()
                
            elif op == "DEL":
                x = int(op_data[1])
                if counts[x] > 0:
                    counts[x] -= 1
                    # Decide where to delete from
                    clean_left()
                    clean_right()
                    
                    
                    
                    deleted = False
                    if left and x <= -left[0]:
                         left_debt[x] += 1
                         l_cnt -= 1
                         deleted = True
                    else:
                        right_debt[x] += 1
                        r_cnt -= 1
                        deleted = True
                    
                    if deleted:
                        balance()
                    
            elif op == "MEDIAN":
                clean_left()
                # total valid size
                if (l_cnt + r_cnt) == 0:
                    results.append("EMPTY")
                elif (l_cnt + r_cnt) < T:
                    results.append("NA")
                else:
                    results.append(str(-left[0]))
        
        return results

def process_operations(T: int, operations: list) -> list:
    solver = Solution()
    return solver.process_operations(T, operations)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    
    q_str = next(it, None)
    if q_str is None: return
    q = int(q_str)
    t_str = next(it, None)
    if t_str is None: return
    T = int(t_str)
    
    operations = []
    for _ in range(q):
        op = next(it)
        if op in ("ADD", "DEL"):
            x = next(it)
            operations.append([op, x])
        else:
            operations.append([op])
    
    result = process_operations(T, operations)
    print("\n".join(result))

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

using namespace std;

class Solution {
    priority_queue<int> left; // Max heap
    priority_queue<int, vector<int>, greater<int>> right; // Min heap
    unordered_map<int, int> leftDebt;
    unordered_map<int, int> rightDebt;
    unordered_map<int, int> global_counts;
    int validLeft = 0;
    int validRight = 0;

    void cleanLeft() {
        while (!left.empty() && leftDebt[left.top()] > 0) {
            leftDebt[left.top()]--;
            left.pop();
        }
    }

    void cleanRight() {
        while (!right.empty() && rightDebt[right.top()] > 0) {
            rightDebt[right.top()]--;
            right.pop();
        }
    }

    void rebalance() {
        while (validLeft > validRight + 1) {
            cleanLeft();
            int val = left.top(); left.pop();
            validLeft--;
            right.push(val);
            validRight++;
        }
        while (validRight > validLeft) {
            cleanRight();
            int val = right.top(); right.pop();
            validRight--;
            left.push(val);
            validLeft++;
        }
        cleanLeft();
        cleanRight();
    }

public:
    vector<string> processOperations(int T, const vector<vector<string>>& operations) {
        vector<string> results;
        
        for (const auto& op : operations) {
            if (op[0] == "ADD") {
                int x = stoi(op[1]);
                global_counts[x]++;
                
                cleanLeft();
                if (left.empty() || x <= left.top()) {
                    left.push(x);
                    validLeft++;
                } else {
                    right.push(x);
                    validRight++;
                }
                rebalance();
            } else if (op[0] == "DEL") {
                int x = stoi(op[1]);
                if (global_counts[x] > 0) {
                    global_counts[x]--;
                    // debt[x]++; // REMOVED
                    
                    cleanLeft();
                    cleanRight();
                    
                    bool inLeft = false;
                    // Decision logic: same as python
                    // if left is not empty and x <= left.top, it belongs to left
                    if (!left.empty() && x <= left.top()) inLeft = true;
                    else inLeft = false;
                    
                    if (inLeft) {
                        leftDebt[x]++;
                        validLeft--;
                    } else {
                        rightDebt[x]++;
                        validRight--;
                    }
                    
                    rebalance();
                }
            } else {
                cleanLeft();
                int total = validLeft + validRight;
                if (total == 0) results.push_back("EMPTY");
                else if (total < T) results.push_back("NA");
                else results.push_back(to_string(left.top()));
            }
        }
        return results;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int q, T;
    if (cin >> q >> T) {
        vector<vector<string>> operations;
        for (int i = 0; i < q; i++) {
            string op;
            cin >> op;
            if (op == "ADD" || op == "DEL") {
                string x;
                cin >> x;
                operations.push_back({op, x});
            } else {
                operations.push_back({op});
            }
        }
        
        Solution solution;
        vector<string> result = solution.processOperations(T, operations);
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

class Solution {
  processOperations(T, operations) {
    const left = new PriorityQueue((a, b) => b - a); // Max heap
    const right = new PriorityQueue((a, b) => a - b); // Min heap
    const leftDebt = new Map();
    const rightDebt = new Map();
    const globalCounts = new Map();
    let validLeft = 0;
    let validRight = 0;
    
    const cleanLeft = () => {
      while (!left.isEmpty()) {
        const val = left.peek();
        if ((leftDebt.get(val) || 0) > 0) {
          left.pop();
          leftDebt.set(val, leftDebt.get(val) - 1);
        } else {
          break;
        }
      }
    };

    const cleanRight = () => {
      while (!right.isEmpty()) {
        const val = right.peek();
        if ((rightDebt.get(val) || 0) > 0) {
          right.pop();
          rightDebt.set(val, rightDebt.get(val) - 1);
        } else {
          break;
        }
      }
    };
    
    const rebalance = () => {
      cleanLeft();
      cleanRight();
      
      while (validLeft > validRight + 1) {
        cleanLeft();
        if (left.isEmpty()) break;
        const val = left.pop();
        validLeft--;
        right.push(val);
        validRight++;
        cleanLeft();
      }
      
      cleanRight();
      while (validRight > validLeft) {
        cleanRight();
        if (right.isEmpty()) break;
        const val = right.pop();
        validRight--;
        left.push(val);
        validLeft++;
        cleanRight();
      }
    };
    
    const results = [];
    
    for (const opData of operations) {
      const op = opData[0];
      if (op === "ADD") {
        const x = parseInt(opData[1]);
        globalCounts.set(x, (globalCounts.get(x) || 0) + 1);
        
        cleanLeft();
        if (left.isEmpty() || x <= left.peek()) {
          left.push(x);
          validLeft++;
        } else {
          right.push(x);
          validRight++;
        }
        rebalance();
      } else if (op === "DEL") {
        const x = parseInt(opData[1]);
        if ((globalCounts.get(x) || 0) > 0) {
          globalCounts.set(x, globalCounts.get(x) - 1);
          
          cleanLeft();
          cleanRight();
          
          let inLeft = false;
          if (!left.isEmpty() && x <= left.peek()) inLeft = true;
          else inLeft = false;
          
          if (inLeft) {
            leftDebt.set(x, (leftDebt.get(x) || 0) + 1);
            validLeft--;
          } else {
            rightDebt.set(x, (rightDebt.get(x) || 0) + 1);
            validRight--;
          }
          
          rebalance();
        }
      } else {
        cleanLeft();
        const total = validLeft + validRight;
        if (total === 0) results.push("EMPTY");
        else if (total < T) results.push("NA");
        else results.push(left.peek().toString());
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
  const T = parseInt(data[idx++]);
  const operations = [];
  for (let i = 0; i < q; i++) {
    const op = data[idx++];
    if (op === "ADD" || op === "DEL") {
      const x = data[idx++];
      operations.push([op, x]);
    } else {
      operations.push([op]);
    }
  }
  
  const solution = new Solution();
  const result = solution.processOperations(T, operations);
  console.log(result.join("\n"));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
4 2
ADD 1
ADD 5
DEL 1
MEDIAN
```

1. `ADD 1`:
   - Left: `{1}`, Right: `{}`. Valid: 1, 0.
2. `ADD 5`:
   - 5 > 1. Push Right.
   - Left: `{1}`, Right: `{5}`. Valid: 1, 1. Balanced.
3. `DEL 1`:
   - `1` is in Left. `validLeft` becomes 0.
   - Debt: `{1: 1}`.
   - Rebalance: `validRight` (1) > `validLeft` (0).
   - Move from Right to Left.
   - Right pop `5`. Left push `5`.
   - Left: `{1, 5}` (1 is dead). Right: `{}`.
   - Valid: 1, 0.
4. `MEDIAN`:
   - Clean Left. Top is `5` (1 is dead, popped).
   - Total valid size: 1.
   - T=2.
   - Output: `NA`.

## ✅ Proof of Correctness

### Invariant
- `validLeft` and `validRight` accurately track the count of non-deleted elements.
- `Left` contains `validLeft` smallest elements. `Right` contains `validRight` largest.
- `validLeft` is always equal to `validRight` or `validRight + 1`.
- Lazy deletion ensures we don't scan heaps, keeping operations logarithmic.

## 💡 Interview Extensions

- **Extension 1:** Sliding Window Median?
  - *Answer:* Same logic, `ADD` new element, `DEL` old element leaving window.
- **Extension 2:** Percentile instead of Median?
  - *Answer:* Adjust the ratio of `validLeft` vs `validRight` (e.g., 90% vs 10%).

### Common Mistakes to Avoid

1. **Incorrect Valid Counts**
   - ❌ Wrong: Decrementing valid count only when physically removing from heap.
   - ✅ Correct: Decrement immediately upon `DEL` request to keep balance logic correct.
2. **Infinite Loops**
   - ❌ Wrong: Not cleaning heaps before `peek` or `pop` during rebalance.
   - ✅ Correct: Always pop dead elements first.

## Related Concepts

- **Lazy Propagation:** Similar concept in Segment Trees.
- **Balanced BST:** Can also solve this (Order Statistic Tree).
