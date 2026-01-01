---
problem_id: GRD_LAB_KIT_DISTRIBUTION__5291
display_id: GRD-002
slug: lab-kit-distribution
title: "Lab Kit Distribution"
difficulty: Easy-Medium
difficulty_score: 35
topics:
  - Greedy Algorithms
  - Heap
  - Priority Queue
tags:
  - greedy
  - heap
  - priority-queue
  - distribution
  - medium
premium: true
subscription_tier: basic
---

# GRD-002: Lab Kit Distribution

## 📋 Problem Summary

You have `k` types of lab kits with varying quantities. You need to distribute these kits to `m` students. Each student needs exactly one kit of any type. Your goals are, in order:
1. Maximize the number of students who receive a kit.
2. Minimize the number of kit types that run out completely (reach zero quantity).

## 🌍 Real-World Scenario

**Scenario Title:** Disaster Relief Supply Management

Imagine you are coordinating disaster relief. You have stockpiles of different food rations (Type A, Type B, Type C). You have a line of people needing food.
- **Goal 1:** Feed as many people as possible.
- **Goal 2:** Maintain variety in your stockpile for as long as possible. If you run out of Type A completely, you lose the ability to accommodate specific dietary restrictions or nutritional balance that Type A might offer later.

By always distributing from the largest stockpile, you keep your options open and delay the moment any single resource type is completely exhausted.

**Why This Problem Matters:**

- **Inventory Health:** Preventing stockouts of specific items is often critical in supply chain management.
- **Load Balancing:** In server clusters, you want to send requests to the server with the most capacity to prevent any single server from crashing (reaching 0 capacity).

![Real-World Application](../images/GRD-002/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Leveling the Piles

Imagine the quantities as stacks of blocks. We want to take blocks away such that we avoid hitting the ground (0) for any stack.

```text
Initial State:
   [ ]
   [ ]      [ ]
   [ ] [ ]  [ ]
    A   B    C
   (3) (1)  (2)

Student 1 takes from A (Largest):
            [ ]
   [ ] [ ]  [ ]
   [ ] [ ]  [ ]
    A   B    C
   (2) (1)  (2)

Student 2 takes from A or C (Largest is 2):
   Let's pick A.
       [ ]  [ ]
   [ ] [ ]  [ ]
    A   B    C
   (1) (1)  (2)

...and so on.
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Fulfilled Count:** This is simply `min(m, sum(quantities))`. You can't give more than you have, and you can't give more than needed.
- **Zeroed Types:** A type counts as "zeroed" if its final quantity is exactly 0.
- **Tie-breaking:** If multiple types have the same maximum quantity, picking any of them is fine for the optimal solution.

## Naive Approach

### Intuition

For each student, scan the entire array of quantities to find the maximum. Decrement it. Repeat `m` times.

### Algorithm

1. Loop `m` times.
2. Inside, loop `k` times to find index of max value.
3. Decrement that value.
4. If all values are 0, stop.

### Time Complexity

- **O(m * k)**: For each student, we scan `k` elements. With `m, k` up to `10^5`, this is `10^10` operations, which will TLE.

### Space Complexity

- **O(1)**: No extra space beyond input.

### Limitations

- Too slow for large inputs.

## Optimal Approach

### Key Insight

We always want the current maximum. A **Max-Heap (Priority Queue)** is the perfect data structure for repeatedly accessing and updating the maximum element efficiently.

### Algorithm

1. Calculate total available kits. `fulfilled = min(m, total)`.
2. Insert all non-zero quantities into a Max-Heap.
3. Iterate `fulfilled` times:
   - Extract max `q` from heap.
   - Decrement `q`.
   - If `q > 0`, push it back into the heap.
   - If `q == 0`, we don't push it back (it's exhausted).
4. The number of zeroed types is `k - heap.size()` (assuming we started with `k` types; if some were initially 0, handle accordingly).
   - Better: Count how many types end up at 0. Or simply `initial_non_zero_types - final_heap_size + initial_zero_types`.
   - Simplest: Just simulate. If `q` becomes 0, it's effectively removed from consideration for future "max" picks, but we need to count it as zeroed at the end.

### Time Complexity

- **O(m log k)**: We perform `m` extractions and insertions. Each heap operation is `log k`.
- **O(k)**: To build the initial heap.
- Total: **O(m log k)**.

### Space Complexity

- **O(k)**: To store the heap.

### Why This Is Optimal

Greedily reducing the largest pile minimizes the variance between pile heights. By keeping piles as equal as possible, we minimize the chance that any single pile hits zero before necessary.

![Algorithm Visualization](../images/GRD-002/algorithm-visualization.png)

## Implementations

### Java
```java
import java.util.*;

class Solution {
    public int[] distributeKits(int k, int m, int[] quantities) {
        // PriorityQueue is min-heap by default, use reverseOrder for max-heap
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        
        long totalKits = 0;
        int initialZeros = 0;
        
        for (int q : quantities) {
            if (q > 0) {
                pq.offer(q);
                totalKits += q;
            } else {
                initialZeros++;
            }
        }
        
        int fulfilled = (int) Math.min((long) m, totalKits);
        int toDistribute = fulfilled;
        
        while (toDistribute > 0 && !pq.isEmpty()) {
            int maxQ = pq.poll();
            maxQ--;
            toDistribute--;
            
            if (maxQ > 0) {
                pq.offer(maxQ);
            }
        }
        
        // Zeroed types = Total types - Types remaining in heap
        // Or: Initial zeros + (Initial non-zeros - Final non-zeros)
        int remainingTypes = pq.size();
        int zeroedTypes = k - remainingTypes;
        
        return new int[]{fulfilled, zeroedTypes};
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        
        int k = sc.nextInt();
        int m = sc.nextInt();
        
        int[] quantities = new int[k];
        for (int i = 0; i < k; i++) {
            quantities[i] = sc.nextInt();
        }
        
        Solution solution = new Solution();
        int[] result = solution.distributeKits(k, m, quantities);
        System.out.println(result[0] + " " + result[1]);
        sc.close();
    }
}
```

### Python
```python
import heapq
import sys

def distribute_kits(k: int, m: int, quantities: list) -> tuple:
    # Python's heapq is a min-heap. We push negative values to simulate max-heap.
    pq = []
    total_kits = 0
    
    for q in quantities:
        if q > 0:
            heapq.heappush(pq, -q)
            total_kits += q
            
    fulfilled = min(m, total_kits)
    to_distribute = fulfilled
    
    while to_distribute > 0 and pq:
        # Pop largest (most negative)
        max_q = -heapq.heappop(pq)
        max_q -= 1
        to_distribute -= 1
        
        if max_q > 0:
            heapq.heappush(pq, -max_q)
            
    # Remaining types in heap are those > 0
    remaining_types = len(pq)
    zeroed_types = k - remaining_types
    
    return (fulfilled, zeroed_types)

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
        
    iterator = iter(data)
    k = int(next(iterator))
    m = int(next(iterator))
    
    quantities = []
    for _ in range(k):
        quantities.append(int(next(iterator)))
        
    fulfilled, zeroed = distribute_kits(k, m, quantities)
    print(f"{fulfilled} {zeroed}")

if __name__ == "__main__":
    main()
```

### C++
```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <numeric>

using namespace std;

class Solution {
public:
    pair<int,int> distributeKits(int k, int m, vector<int>& quantities) {
        priority_queue<int> pq;
        long long totalKits = 0;
        
        for (int q : quantities) {
            if (q > 0) {
                pq.push(q);
                totalKits += q;
            }
        }
        
        int fulfilled = min((long long)m, totalKits);
        int toDistribute = fulfilled;
        
        while (toDistribute > 0 && !pq.empty()) {
            int maxQ = pq.top();
            pq.pop();
            
            maxQ--;
            toDistribute--;
            
            if (maxQ > 0) {
                pq.push(maxQ);
            }
        }
        
        int remainingTypes = pq.size();
        int zeroedTypes = k - remainingTypes;
        
        return {fulfilled, zeroedTypes};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k, m;
    if (!(cin >> k >> m)) return 0;

    vector<int> quantities(k);
    for (int i = 0; i < k; i++) {
        cin >> quantities[i];
    }

    Solution solution;
    pair<int,int> result = solution.distributeKits(k, m, quantities);
    cout << result.first << " " << result.second << "\n";

    return 0;
}
```

### JavaScript
```javascript
const readline = require("readline");

// Simple MaxHeap implementation for JS since it doesn't have a built-in one
class MaxHeap {
  constructor() {
    this.heap = [];
  }
  
  push(val) {
    this.heap.push(val);
    this._siftUp();
  }
  
  pop() {
    if (this.size() === 0) return null;
    if (this.size() === 1) return this.heap.pop();
    
    const max = this.heap[0];
    this.heap[0] = this.heap.pop();
    this._siftDown();
    return max;
  }
  
  size() {
    return this.heap.length;
  }
  
  _siftUp() {
    let nodeIdx = this.heap.length - 1;
    while (nodeIdx > 0) {
      const parentIdx = Math.floor((nodeIdx - 1) / 2);
      if (this.heap[nodeIdx] <= this.heap[parentIdx]) break;
      [this.heap[nodeIdx], this.heap[parentIdx]] = [this.heap[parentIdx], this.heap[nodeIdx]];
      nodeIdx = parentIdx;
    }
  }
  
  _siftDown() {
    let nodeIdx = 0;
    while (nodeIdx < this.heap.length) {
      let maxChildIdx = null;
      const leftChildIdx = 2 * nodeIdx + 1;
      const rightChildIdx = 2 * nodeIdx + 2;
      
      if (leftChildIdx < this.heap.length) maxChildIdx = leftChildIdx;
      if (rightChildIdx < this.heap.length && this.heap[rightChildIdx] > this.heap[leftChildIdx]) {
        maxChildIdx = rightChildIdx;
      }
      
      if (maxChildIdx === null || this.heap[nodeIdx] >= this.heap[maxChildIdx]) break;
      
      [this.heap[nodeIdx], this.heap[maxChildIdx]] = [this.heap[maxChildIdx], this.heap[nodeIdx]];
      nodeIdx = maxChildIdx;
    }
  }
}

class Solution {
  distributeKits(k, m, quantities) {
    const pq = new MaxHeap();
    let totalKits = 0;
    
    for (const q of quantities) {
      if (q > 0) {
        pq.push(q);
        totalKits += q;
      }
    }
    
    const fulfilled = Math.min(m, totalKits);
    let toDistribute = fulfilled;
    
    while (toDistribute > 0 && pq.size() > 0) {
      let maxQ = pq.pop();
      maxQ--;
      toDistribute--;
      
      if (maxQ > 0) {
        pq.push(maxQ);
      }
    }
    
    const remainingTypes = pq.size();
    const zeroedTypes = k - remainingTypes;
    
    return [fulfilled, zeroedTypes];
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  if (data.length === 0) return;
  
  let ptr = 0;
  const [k, m] = data[ptr++].split(" ").map(Number);
  const quantities = data[ptr++].split(" ").map(Number);

  const solution = new Solution();
  const [fulfilled, zeroed] = solution.distributeKits(k, m, quantities);
  console.log(`${fulfilled} ${zeroed}`);
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
3 4
3 1 2
```

**Initialization:**
- Heap: `[3, 2, 1]` (Max-Heap)
- Total Kits: 6
- Fulfilled: `min(4, 6) = 4`

**Iteration:**

| Step | Heap State (Before) | Action | Heap State (After) | Remaining to Distribute |
| :--- | :--- | :--- | :--- | :--- |
| 1 | `[3, 2, 1]` | Pop 3, push 2 | `[2, 2, 1]` | 3 |
| 2 | `[2, 2, 1]` | Pop 2, push 1 | `[2, 1, 1]` | 2 |
| 3 | `[2, 1, 1]` | Pop 2, push 1 | `[1, 1, 1]` | 1 |
| 4 | `[1, 1, 1]` | Pop 1, push 0 (discard) | `[1, 1]` | 0 |

**Result:**
- Fulfilled: 4
- Remaining types in heap: 2
- Original types: 3
- Zeroed types: `3 - 2 = 1`

**Output:** `4 1`

![Example Visualization](../images/GRD-002/example-1.png)

## ✅ Proof of Correctness

### Invariant
At any step, the heap contains the current quantities of all non-zero kit types.

### Why Greedy Works
Suppose we deviate from the greedy strategy and take from a smaller pile `S` instead of the largest pile `L` (`S < L`).
- The new state is `S-1, L`.
- The greedy state is `S, L-1`.
- Since `S < L`, `S-1` is closer to 0 than `L-1` is. In fact, `S-1` is the most dangerous state.
- By reducing `L`, we keep the minimum value in the set as high as possible (or at least don't lower it unnecessarily).
- This maximizes the time until any pile hits 0.

## 💡 Interview Extensions

- **Extension 1:** What if we want to minimize the variance of the remaining quantities?
  - *Answer:* The same greedy strategy works! It tends to equalize the values.
- **Extension 2:** What if `m` is extremely large (`10^18`)?
  - *Answer:* We can't simulate. We need binary search on the "water level" (the final height of the piles).
- **Extension 3:** What if taking a kit has a cost associated with the type?
  - *Answer:* Then it becomes a Min-Cost Flow problem or a different greedy strategy based on cost.

### Common Mistakes to Avoid

1. **Sorting Only Once**
   - ❌ Wrong: Sort array, take from largest, decrement.
   - ⚠️ Issue: After decrementing, the order might change. You need to re-sort or use a Heap.
   - ✅ Correct: Use a Max-Heap.

2. **Ignoring Initial Zeros**
   - ❌ Wrong: `zeroed = heap.size()`.
   - ✅ Correct: `zeroed = k - heap.size()`. Some types might have been 0 to start with and never entered the heap.

3. **Integer Overflow**
   - ❌ Wrong: Using `int` for total sum if quantities are large.
   - ✅ Correct: Use `long` (Java/C++) for summing quantities, though `m` fits in int here.

## Related Concepts

- **Heap / Priority Queue:** Efficient max extraction.
- **Load Balancing:** Distributing tasks to resources.
- **Water Filling Algorithm:** Related concept for equalizing levels.
