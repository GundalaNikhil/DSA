---
problem_id: QUE_LAB_WINDOW_INSTABILITY__3951
display_id: QUE-007
slug: lab-window-instability
title: "Lab Window Instability"
difficulty: Medium
difficulty_score: 50
topics:
  - Sliding Window
  - Queue
  - Heaps
tags:
  - sliding-window
  - deque
  - median
  - medium
premium: true
subscription_tier: basic
---

# QUE-007: Lab Window Instability

## 📋 Problem Summary

We are given a series of sensor readings. For every sliding window of size $K$, we need to calculate the "instability" metric:
$$ \text{instability} = \lfloor \frac{\max - \min}{\text{median}} \rfloor $$
- If median is 0, output 0.
- Median is the lower median if $K$ is even.

## 🌍 Real-World Scenario

**Scenario Title:** Stock Market Volatility Analysis

Traders analyze stock prices over time windows (e.g., 1-hour moving window).
- **Max - Min:** Represents the range or spread of the price.
- **Median:** Represents the "typical" price, filtering out brief spikes.
- **(Max - Min) / Median:** This is a normalized volatility measure.
- A high value means the stock is swinging wildly relative to its price.
- A low value means it's stable.
- Computing this efficiently for millions of ticks is crucial for high-frequency trading algorithms.

**Why This Problem Matters:**

- **Signal Processing:** Normalizing noise amplitude by signal strength.
- **Quality Control:** Detecting unstable manufacturing processes.

![Real-World Application](../images/QUE-007/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Sliding Window

Values: `[5, 1, 4, 6, 2]`, $K=3$.

1. **Window 1:** `[5, 1, 4]`
   - Sorted: `1, 4, 5`
   - Min: 1, Max: 5, Median: 4
   - Instability: $(5-1)/4 = 1$.

2. **Window 2:** `[1, 4, 6]`
   - Sorted: `1, 4, 6`
   - Min: 1, Max: 6, Median: 4
   - Instability: $(6-1)/4 = 1.25 \to 1$.

3. **Window 3:** `[4, 6, 2]`
   - Sorted: `2, 4, 6`
   - Min: 2, Max: 6, Median: 4
   - Instability: $(6-2)/4 = 1$.

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** $N, K$, array of integers.
- **Output:** Array of instability values.
- **Median Definition:** If sorted window is $w_0, \dots, w_{k-1}$, median is $w_{\lfloor (k-1)/2 \rfloor}$.
- **Division by Zero:** Handle median = 0 case.

## Naive Approach

### Intuition

For each window, extract elements, sort them to find min/max/median.

### Algorithm

1. Loop `i` from 0 to `n-k`.
2. Extract subarray `window = values[i : i+k]`.
3. Sort `window`.
4. `min = window[0]`, `max = window[k-1]`, `med = window[(k-1)/2]`.
5. Compute and print.

### Limitations

- **Time Complexity:** $O(N \cdot K \log K)$. With $N=200,000$, this is too slow.

## Optimal Approach

### Key Insight

We need three statistics efficiently:
1. **Min/Max:** Use **Monotonic Deques** (Sliding Window Minimum/Maximum). $O(N)$ total.
2. **Median:** Use **Two Heaps** (Min-Heap for upper half, Max-Heap for lower half) with **Lazy Deletion**. $O(N \log K)$.

### Algorithm

1. **Min/Max:** Maintain two deques.
   - `minDeque`: Stores indices of increasing values. Front is min.
   - `maxDeque`: Stores indices of decreasing values. Front is max.
2. **Median:** Maintain two heaps (`small` max-heap, `large` min-heap) and a `balance`.
   - Use a Hash Map `delayed` to track elements that left the window but are still in heaps.
   - **Add new element:** Push to `small`, then move top of `small` to `large`. Balance sizes so `small` has $\lceil K/2 \rceil$ elements.
   - **Remove old element:** Mark in `delayed`. Rebalance heaps if necessary. Prune tops of heaps if they are in `delayed`.
3. **Compute:** For each window, get min/max from deques, median from `small.top()`.

### Time Complexity

- **O(N log K)** due to heap operations.

### Space Complexity

- **O(N)** for heaps and delayed map (worst case lazy deletion).

![Algorithm Visualization](../images/QUE-007/algorithm-visualization.png)
![Algorithm Steps](../images/QUE-007/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public long[] windowInstability(int[] values, int k) {
        int n = values.length;
        long[] result = new long[n - k + 1];
        
        // Deques for Min/Max
        Deque<Integer> minDeque = new ArrayDeque<>();
        Deque<Integer> maxDeque = new ArrayDeque<>();
        
        // Heaps for Median
        PriorityQueue<Integer> small = new PriorityQueue<>(Collections.reverseOrder());
        PriorityQueue<Integer> large = new PriorityQueue<>();
        Map<Integer, Integer> delayed = new HashMap<>();
        
        for (int i = 0; i < n; i++) {
            // 1. Update Min/Max Deques
            while (!minDeque.isEmpty() && minDeque.peekFirst() <= i - k) minDeque.pollFirst();
            while (!minDeque.isEmpty() && values[minDeque.peekLast()] >= values[i]) minDeque.pollLast();
            minDeque.offerLast(i);
            
            while (!maxDeque.isEmpty() && maxDeque.peekFirst() <= i - k) maxDeque.pollFirst();
            while (!maxDeque.isEmpty() && values[maxDeque.peekLast()] <= values[i]) maxDeque.pollLast();
            maxDeque.offerLast(i);
            
            // 2. Update Median Heaps
            // Add new
            small.offer(values[i]);
            large.offer(small.poll());
            if (large.size() > small.size()) {
                small.offer(large.poll());
            }
            
            // Remove old (lazy)
            if (i >= k) {
                int out = values[i - k];
                delayed.put(out, delayed.getOrDefault(out, 0) + 1);
                
                // Rebalance logic if the removed element was effectively in one of the heaps
                // Note: We don't know exactly where 'out' is, but we can maintain balance invariant
                // Balance: small.size() >= large.size()
                // Actually, lazy removal is tricky. A simpler way for fixed window median is:
                // If out <= small.peek(), it's in small. Else in large.
                // But small.peek() might be 'out' itself (or a duplicate).
                // Let's use the standard balance check:
                // small should have ceil(k/2) valid elements.
                
                if (out <= small.peek()) {
                     // It was in small partition
                     // We need to remove it logically.
                     // Since we can't remove arbitrary node easily in Java PQ, we just decrement logical size count?
                     // No, standard lazy removal:
                     // Just rebalance sizes.
                     // If we assume it was in small, small effectively loses 1.
                     // If small becomes too small, move from large.
                } 
                // This logic is complex to implement perfectly with lazy deletion in Java.
                // Alternative: Use two TreeMaps/Multisets for O(log K) removal.
            }
            
            // Prune dead roots
            while (!small.isEmpty() && delayed.getOrDefault(small.peek(), 0) > 0) {
                int val = small.peek();
                delayed.put(val, delayed.get(val) - 1);
                small.poll();
            }
            while (!large.isEmpty() && delayed.getOrDefault(large.peek(), 0) > 0) {
                int val = large.peek();
                delayed.put(val, delayed.get(val) - 1);
                large.poll();
            }
        }
        
        // REWRITE: The lazy deletion logic above is insufficient because we need to know WHICH heap the element belonged to
        // to maintain the size invariant.
        // Let's use the "Dual PriorityQueue with Balance" class approach.
        return solveWithDualPQ(values, k);
    }

    private long[] solveWithDualPQ(int[] values, int k) {
        int n = values.length;
        long[] result = new long[n - k + 1];
        Deque<Integer> minD = new ArrayDeque<>();
        Deque<Integer> maxD = new ArrayDeque<>();
        MedianFinder mf = new MedianFinder();

        for (int i = 0; i < n; i++) {
            // Min/Max
            while (!minD.isEmpty() && minD.peekFirst() <= i - k) minD.pollFirst();
            while (!minD.isEmpty() && values[minD.peekLast()] >= values[i]) minD.pollLast();
            minD.offerLast(i);

            while (!maxD.isEmpty() && maxD.peekFirst() <= i - k) maxD.pollFirst();
            while (!maxD.isEmpty() && values[maxD.peekLast()] <= values[i]) maxD.pollLast();
            maxD.offerLast(i);

            // Median
            mf.add(values[i]);
            if (i >= k) mf.remove(values[i - k]);

            if (i >= k - 1) {
                int minVal = values[minD.peekFirst()];
                int maxVal = values[maxD.peekFirst()];
                int median = mf.getMedian();
                if (median == 0) result[i - k + 1] = 0;
                else result[i - k + 1] = (long)(maxVal - minVal) / median;
            }
        }
        return result;
    }

    static class MedianFinder {
        PriorityQueue<Integer> small = new PriorityQueue<>(Collections.reverseOrder());
        PriorityQueue<Integer> large = new PriorityQueue<>();
        // To handle lazy removal correctly, we track balance explicitly
        // Balance = small.size() - large.size() (considering only valid elements)
        // But since we can't know if a specific instance in heap is valid, we just track counts.
        // Actually, for sliding window, TreeMap is better in Java, but O(log K).
        // Let's use two TreeMaps (Multiset).
        
        // Re-implementation with TreeMap for correctness and simplicity
        TreeMap<Integer, Integer> smallMap = new TreeMap<>();
        TreeMap<Integer, Integer> largeMap = new TreeMap<>();
        int smallSize = 0;
        int largeSize = 0;

        void add(int val) {
            // Add to small first
            addMap(smallMap, val);
            smallSize++;
            
            // Move max of small to large
            int maxSmall = smallMap.lastKey();
            removeMap(smallMap, maxSmall);
            smallSize--;
            
            addMap(largeMap, maxSmall);
            largeSize++;
            
            // Rebalance: small should be >= large
            if (smallSize < largeSize) {
                int minLarge = largeMap.firstKey();
                removeMap(largeMap, minLarge);
                largeSize--;
                
                addMap(smallMap, minLarge);
                smallSize++;
            }
        }

        void remove(int val) {
            // Try to remove from small first
            if (smallMap.containsKey(val)) {
                // Check if it really belongs to small range
                // It must be <= small.lastKey()
                // Since small contains smaller elements, if val <= small.lastKey(), it's in small.
                // BUT wait, duplicates?
                // If val is in smallMap, we can just remove it?
                // Yes, because all elements in smallMap are <= all elements in largeMap.
                // So if val is in smallMap, it MUST be in the small partition.
                removeMap(smallMap, val);
                smallSize--;
            } else {
                removeMap(largeMap, val);
                largeSize--;
            }
            
            // Rebalance
            if (smallSize < largeSize) {
                int minLarge = largeMap.firstKey();
                removeMap(largeMap, minLarge);
                largeSize--;
                addMap(smallMap, minLarge);
                smallSize++;
            } else if (smallSize > largeSize + 1) {
                int maxSmall = smallMap.lastKey();
                removeMap(smallMap, maxSmall);
                smallSize--;
                addMap(largeMap, maxSmall);
                largeSize++;
            }
        }

        int getMedian() {
            return smallMap.lastKey();
        }

        void addMap(TreeMap<Integer, Integer> map, int val) {
            map.put(val, map.getOrDefault(val, 0) + 1);
        }

        void removeMap(TreeMap<Integer, Integer> map, int val) {
            int count = map.get(val);
            if (count == 1) map.remove(val);
            else map.put(val, count - 1);
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int k = sc.nextInt();
            int[] values = new int[n];
            for (int i = 0; i < n; i++) {
                values[i] = sc.nextInt();
            }
            Solution solution = new Solution();
            long[] result = solution.windowInstability(values, k);
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < result.length; i++) {
                if (i > 0) sb.append(' ');
                sb.append(result[i]);
            }
            System.out.println(sb.toString());
        }
        sc.close();
    }
}
```

### Python

```python
from typing import List
from collections import deque
import heapq
import sys

class MedianFinder:
    def __init__(self):
        self.small = [] # Max heap (negative values)
        self.large = [] # Min heap
        self.delayed = {} # Lazy removal
        self.small_size = 0
        self.large_size = 0

    def add(self, num: int):
        # Add to small
        heapq.heappush(self.small, -num)
        # Move to large
        val = -heapq.heappop(self.small)
        heapq.heappush(self.large, val)
        
        self.large_size += 1
        
        # Rebalance: small needs to be size k or k+1
        if self.small_size < self.large_size:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)
            self.large_size -= 1
            self.small_size += 1

    def remove(self, num: int):
        self.delayed[num] = self.delayed.get(num, 0) + 1
        
        # Determine which heap it effectively belongs to
        # small.peek is the median (or close to it)
        # If num <= small.peek(), it's in small
        small_top = -self.small[0] if self.small else float('-inf')
        
        if num <= small_top:
            self.small_size -= 1
        else:
            self.large_size -= 1
            
        # Prune dead roots
        self.prune()
        
        # Rebalance sizes
        if self.small_size < self.large_size:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)
            self.large_size -= 1
            self.small_size += 1
        elif self.small_size > self.large_size + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
            self.small_size -= 1
            self.large_size += 1
            
        self.prune()

    def prune(self):
        while self.small and self.delayed.get(-self.small[0], 0) > 0:
            val = -heapq.heappop(self.small)
            self.delayed[val] -= 1
        while self.large and self.delayed.get(self.large[0], 0) > 0:
            val = heapq.heappop(self.large)
            self.delayed[val] -= 1

    def get_median(self) -> int:
        return -self.small[0]

def window_instability(values: List[int], k: int) -> List[int]:
    n = len(values)
    result = []
    min_dq = deque()
    max_dq = deque()
    mf = MedianFinder()
    
    for i in range(n):
        # Min Deque
        while min_dq and min_dq[0] <= i - k:
            min_dq.popleft()
        while min_dq and values[min_dq[-1]] >= values[i]:
            min_dq.pop()
        min_dq.append(i)
        
        # Max Deque
        while max_dq and max_dq[0] <= i - k:
            max_dq.popleft()
        while max_dq and values[max_dq[-1]] <= values[i]:
            max_dq.pop()
        max_dq.append(i)
        
        # Median
        mf.add(values[i])
        if i >= k:
            mf.remove(values[i-k])
            
        if i >= k - 1:
            min_val = values[min_dq[0]]
            max_val = values[max_dq[0]]
            med = mf.get_median()
            if med == 0:
                result.append(0)
            else:
                result.append((max_val - min_val) // med)
                
    return result

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        k = int(next(iterator))
        values = [int(next(iterator)) for _ in range(n)]
        
        result = window_instability(values, k)
        print(" ".join(map(str, result)))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <deque>
#include <set>

using namespace std;

class Solution {
public:
    vector<long long> windowInstability(const vector<int>& values, int k) {
        int n = values.size();
        vector<long long> result;
        deque<int> minD, maxD;
        
        // Use multiset for median (simplest in C++ as it supports deletion)
        // Two multisets: small (max), large (min)
        multiset<int> small, large;
        
        auto balance = [&]() {
            while (small.size() > large.size() + 1) {
                large.insert(*small.rbegin());
                small.erase(prev(small.end()));
            }
            while (large.size() > small.size()) {
                small.insert(*large.begin());
                large.erase(large.begin());
            }
        };
        
        auto add = [&](int val) {
            small.insert(val);
            large.insert(*small.rbegin());
            small.erase(prev(small.end()));
            balance();
        };
        
        auto remove = [&](int val) {
            auto it = small.find(val);
            if (it != small.end()) {
                small.erase(it);
            } else {
                large.erase(large.find(val));
            }
            balance();
        };
        
        for (int i = 0; i < n; i++) {
            // Min/Max Deques
            while (!minD.empty() && minD.front() <= i - k) minD.pop_front();
            while (!minD.empty() && values[minD.back()] >= values[i]) minD.pop_back();
            minD.push_back(i);
            
            while (!maxD.empty() && maxD.front() <= i - k) maxD.pop_front();
            while (!maxD.empty() && values[maxD.back()] <= values[i]) maxD.pop_back();
            maxD.push_back(i);
            
            // Median
            add(values[i]);
            if (i >= k) remove(values[i - k]);
            
            if (i >= k - 1) {
                int minVal = values[minD.front()];
                int maxVal = values[maxD.front()];
                int med = *small.rbegin();
                if (med == 0) result.push_back(0);
                else result.push_back((long long)(maxVal - minVal) / med);
            }
        }
        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (cin >> n >> k) {
        vector<int> values(n);
        for (int i = 0; i < n; i++) {
            cin >> values[i];
        }
    
        Solution solution;
        vector<long long> result = solution.windowInstability(values, k);
        for (int i = 0; i < (int)result.size(); i++) {
            if (i) cout << ' ';
            cout << result[i];
        }
        cout << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

// Simple MinPriorityQueue / MaxPriorityQueue polyfill for JS environment
// Or use a sorted array with binary search insertion (O(K) insertion)
// Since K can be large, O(K) is bad.
// However, JS doesn't have built-in Heap or TreeMap.
// For competitive programming in JS without libraries, implementing a Heap is standard.
// Here, we'll implement a basic Heap.

class Heap {
  constructor(compare) {
    this.data = [];
    this.compare = compare; // (a, b) => boolean (true if a should be above b)
  }
  size() { return this.data.length; }
  peek() { return this.data[0]; }
  push(val) {
    this.data.push(val);
    this.bubbleUp(this.data.length - 1);
  }
  pop() {
    const top = this.data[0];
    const bottom = this.data.pop();
    if (this.data.length > 0) {
      this.data[0] = bottom;
      this.bubbleDown(0);
    }
    return top;
  }
  bubbleUp(idx) {
    while (idx > 0) {
      const p = Math.floor((idx - 1) / 2);
      if (this.compare(this.data[idx], this.data[p])) {
        [this.data[idx], this.data[p]] = [this.data[p], this.data[idx]];
        idx = p;
      } else break;
    }
  }
  bubbleDown(idx) {
    while (true) {
      const left = 2 * idx + 1;
      const right = 2 * idx + 2;
      let swap = idx;
      if (left < this.data.length && this.compare(this.data[left], this.data[swap])) swap = left;
      if (right < this.data.length && this.compare(this.data[right], this.data[swap])) swap = right;
      if (swap !== idx) {
        [this.data[idx], this.data[swap]] = [this.data[swap], this.data[idx]];
        idx = swap;
      } else break;
    }
  }
}

class MedianFinder {
  constructor() {
    this.small = new Heap((a, b) => a > b); // Max Heap
    this.large = new Heap((a, b) => a < b); // Min Heap
    this.delayed = new Map();
    this.smallSize = 0;
    this.largeSize = 0;
  }
  add(val) {
    this.small.push(val);
    const maxSmall = this.small.pop();
    this.large.push(maxSmall);
    this.largeSize++;
    
    if (this.smallSize < this.largeSize) {
      this.small.push(this.large.pop());
      this.largeSize--;
      this.smallSize++;
    }
  }
  remove(val) {
    this.delayed.set(val, (this.delayed.get(val) || 0) + 1);
    const smallTop = this.small.size() > 0 ? this.small.peek() : -Infinity;
    if (val <= smallTop) this.smallSize--;
    else this.largeSize--;
    
    this.prune();
    
    if (this.smallSize < this.largeSize) {
      this.small.push(this.large.pop());
      this.largeSize--;
      this.smallSize++;
    } else if (this.smallSize > this.largeSize + 1) {
      this.large.push(this.small.pop());
      this.smallSize--;
      this.largeSize++;
    }
    this.prune();
  }
  prune() {
    while (this.small.size() > 0 && (this.delayed.get(this.small.peek()) || 0) > 0) {
      const val = this.small.pop();
      this.delayed.set(val, this.delayed.get(val) - 1);
    }
    while (this.large.size() > 0 && (this.delayed.get(this.large.peek()) || 0) > 0) {
      const val = this.large.pop();
      this.delayed.set(val, this.delayed.get(val) - 1);
    }
  }
  getMedian() {
    return this.small.peek();
  }
}

class Solution {
  windowInstability(values, k) {
    const result = [];
    const minD = []; // Indices
    const maxD = []; // Indices
    const mf = new MedianFinder();
    
    for (let i = 0; i < values.length; i++) {
      // Min Deque
      while (minD.length > 0 && minD[0] <= i - k) minD.shift();
      while (minD.length > 0 && values[minD[minD.length - 1]] >= values[i]) minD.pop();
      minD.push(i);
      
      // Max Deque
      while (maxD.length > 0 && maxD[0] <= i - k) maxD.shift();
      while (maxD.length > 0 && values[maxD[maxD.length - 1]] <= values[i]) maxD.pop();
      maxD.push(i);
      
      // Median
      mf.add(values[i]);
      if (i >= k) mf.remove(values[i - k]);
      
      if (i >= k - 1) {
        const minVal = values[minD[0]];
        const maxVal = values[maxD[0]];
        const med = mf.getMedian();
        if (med === 0) result.push(0);
        else result.push(Math.floor((maxVal - minVal) / med));
      }
    }
    return result;
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
  const n = parseInt(data[idx++], 10);
  const k = parseInt(data[idx++], 10);
  const values = [];
  for (let i = 0; i < n; i++) {
    values.push(parseInt(data[idx++], 10));
  }

  const solution = new Solution();
  const result = solution.windowInstability(values, k);
  console.log(result.join(" "));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

Input: `5 1 4 6 2`, `k=3`

1. `i=0` (5): MinD`[0]`, MaxD`[0]`, Med`{5}`.
2. `i=1` (1): MinD`[1]`, MaxD`[0,1]`, Med`{1,5}`.
3. `i=2` (4): MinD`[1,2]`, MaxD`[2]`, Med`{1,4,5}`.
   - Window `[5, 1, 4]`. Min=1, Max=5, Med=4. Res=1.
4. `i=3` (6): Remove 5. Add 6.
   - MinD`[1,2,3]`, MaxD`[3]`. Med`{1,4,6}`.
   - Window `[1, 4, 6]`. Min=1, Max=6, Med=4. Res=1.
5. `i=4` (2): Remove 1. Add 2.
   - MinD`[4]`, MaxD`[3,4]`. Med`{2,4,6}`.
   - Window `[4, 6, 2]`. Min=2, Max=6, Med=4. Res=1.

Result: `1 1 1`.

## ✅ Proof of Correctness

### Invariant
Deques correctly maintain min/max candidates in $O(1)$. Dual heaps correctly maintain the median property with $O(\log K)$ updates.

### Why the approach is correct
Combining these standard sliding window techniques allows computing the complex metric efficiently.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** What if $K$ varies?
  - *Hint:* Standard sliding window techniques don't apply directly. Segment Trees or Treaps might be needed.
- **Extension 2:** Percentile instead of Median?
  - *Hint:* Dual heaps can be generalized to two heaps of size $P \times K$ and $(1-P) \times K$.

## Common Mistakes to Avoid

1. **Lazy Deletion Balance**
   - ❌ Wrong: Only checking `delayed` count without adjusting `smallSize`/`largeSize`.
   - ✅ Correct: Must logically track which heap the removed element belonged to.
2. **Deque Indices**
   - ❌ Wrong: Storing values in Deque.
   - ✅ Correct: Store indices to check expiry `i - k`.

## Related Concepts

- **Sliding Window Median:** The core subproblem here.
- **Monotonic Queue:** Used for Min/Max.
