---
problem_id: HEP_SLIDING_WINDOW_KTH_SMALLEST__2665
display_id: HEP-007
slug: sliding-window-kth-smallest
title: "Sliding Window Kth Smallest"
difficulty: Medium
difficulty_score: 58
topics:
  - Heaps
  - Sliding Window
  - Order Statistics
tags:
  - heaps
  - sliding-window
  - order-statistics
  - medium
premium: true
subscription_tier: basic
---

# HEP-007: Sliding Window Kth Smallest

## 📋 Problem Summary

You have an array `arr` of size `n`.
Consider a sliding window of size `w`.
For each window position, find the `k`-th smallest element.
Return the list of `k`-th smallest elements.

## 🌍 Real-World Scenario

**Scenario Title:** Stock Market Volatility Analysis

Traders often look at the "median" or "25th percentile" price of a stock over the last `w` minutes to gauge trends without being affected by outliers.
- If `k = w/2`, you are finding the **Running Median**.
- If `k = 1`, you are finding the **Running Minimum**.
- If `k = w`, you are finding the **Running Maximum**.
This problem generalizes all these to the "Running K-th Percentile".

![Real-World Application](../images/HEP-007/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Two-Heap Strategy

Window: `[1, 5, 2, 8, 3]`, `k=3` (Median).
Sorted: `[1, 2, 3, 5, 8]`. 3rd smallest is 3.

We maintain two heaps (or balanced BSTs):
1. **Left Heap (Max-Heap):** Stores the smallest `k` elements.
2. **Right Heap (Min-Heap):** Stores the remaining `w-k` elements.

Invariant:
- Size of Left Heap = `k`.
- Size of Right Heap = `w-k`.
- `max(Left) <= min(Right)`.

The answer is always `Left.top()`.

**Sliding:**
- **Add** new element `x`.
- **Remove** old element `y`.

Steps:
1. Remove `y`:
   - If `y` was in Left, remove it. Left size decreases.
   - If `y` was in Right, remove it. Right size decreases.
2. Add `x`:
   - Insert into appropriate heap to maintain order.
3. Rebalance:
   - Ensure Left has exactly `k` elements.
   - Move elements between heaps if sizes are off.

### Key Concept: Lazy Deletion

Standard heaps don't support efficient removal of arbitrary elements (`O(N)`).
We use **Lazy Deletion**:
- Keep a `deleted` map (or hash table) of counts of elements to be removed.
- When `top()` of a heap is in `deleted`, pop it and decrement count.
- We also need to track the *logical* size of heaps, not just physical size.

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** `n`, `w`, `k`, array `arr`.
- **Output:** Array of size `n-w+1`.
- **Constraints:** `N <= 2 x 10^5`. `W <= N`.
- **Values:** Integers, can be negative.

## Naive Approach

### Intuition

For each window, copy elements, sort them, pick index `k-1`.

### Time Complexity

- **O(N * W log W)**: Too slow if `W` is large.

## Optimal Approach

### Key Insight

Use **Two Heaps with Lazy Deletion**.
- **Max-Heap `L`**: Stores smallest `k` elements.
- **Min-Heap `R`**: Stores largest `w-k` elements.
- **Balance**: `L.size == k`.
- **Lazy Removal**: Use a hash map `to_remove` to mark elements that left the window but are still in heaps. Clean up tops lazily.

### Algorithm

1. Initialize `L` (Max-Heap), `R` (Min-Heap), `to_remove` map.
2. `balance` function:
   - While `L.size > k`: Move top of `L` to `R`.
   - While `L.size < k`: Move top of `R` to `L`.
   - While `L.top` > `R.top`: Swap tops (if heaps not empty).
   - We must track `L_valid_size` and `R_valid_size` explicitly.
3. **Add(val)**:
   - If `L` empty or `val < L.top`: push to `L`, `L_valid++`.
   - Else: push to `R`, `R_valid++`.
   - Rebalance.
4. **Remove(val)**:
   - Increment `to_remove[val]`.
   - If `val` can be in `L` (i.e., `val <= L.top`): `L_valid--`.
   - Else: `R_valid--`.
   - Clean tops: `while L.top in to_remove: pop L`. Same for `R`.
   - Rebalance.
5. **Rebalance Logic**:
   - While `L_valid > k`:
     - Move `L.top` to `R`. (Pop L, Push R).
     - `L_valid--`, `R_valid++`.
     - Clean `L`.
   - While `L_valid < k`:
     - Move `R.top` to `L`.
     - `L_valid++`, `R_valid--`.
     - Clean `R`.
   - Note: We rely on `L.top` being the k-th smallest.

### Time Complexity

- **O(N log W)**.

### Space Complexity

- **O(N)** (due to lazy deletion, heap can grow up to N).

![Algorithm Visualization](../images/HEP-007/algorithm-visualization.png)

## Implementations

### Java
```java
import java.util.*;

class Solution {
    static class DualHeap {
        int k;
        PriorityQueue<Integer> small; // Max heap (simulated)
        PriorityQueue<Integer> large; // Min heap
        int smallCount; // Logical count
        int largeCount; // Logical count
        Map<Integer, Integer> lazy;
        Map<Integer, Integer> inSmall;
        Map<Integer, Integer> inLarge;

        public DualHeap(int k) {
            this.k = k;
            this.small = new PriorityQueue<>(Collections.reverseOrder());
            this.large = new PriorityQueue<>();
            this.smallCount = 0;
            this.largeCount = 0;
            this.lazy = new HashMap<>();
            this.inSmall = new HashMap<>();
            this.inLarge = new HashMap<>();
        }

        private void prune(PriorityQueue<Integer> heap) {
            while (!heap.isEmpty()) {
                int val = heap.peek();
                if (lazy.getOrDefault(val, 0) > 0) {
                    lazy.put(val, lazy.get(val) - 1);
                    heap.poll();
                } else {
                    break;
                }
            }
        }

        public void add(int x) {
            if (smallCount < k) {
                small.offer(x);
                smallCount++;
                inSmall.put(x, inSmall.getOrDefault(x, 0) + 1);
            } else {
                prune(small);
                if (small.isEmpty()) { // Should be rare given smallCount >= k check
                     small.offer(x);
                     smallCount++;
                     inSmall.put(x, inSmall.getOrDefault(x, 0) + 1);
                } else {
                    int smallMax = small.peek();
                    if (x <= smallMax) {
                        small.poll();
                        inSmall.put(smallMax, inSmall.get(smallMax) - 1);
                        
                        small.offer(x);
                        inSmall.put(x, inSmall.getOrDefault(x, 0) + 1);
                        
                        large.offer(smallMax);
                        inLarge.put(smallMax, inLarge.getOrDefault(smallMax, 0) + 1);
                        largeCount++;
                    } else {
                        large.offer(x);
                        inLarge.put(x, inLarge.getOrDefault(x, 0) + 1);
                        largeCount++;
                    }
                }
            }
            balance();
        }

        public void remove(int x) {
            lazy.put(x, lazy.getOrDefault(x, 0) + 1);
            if (inSmall.getOrDefault(x, 0) > 0) {
                inSmall.put(x, inSmall.get(x) - 1);
                smallCount--;
            } else {
                inLarge.put(x, inLarge.getOrDefault(x, 0) - 1); // Note: might be 0 if bug, but logic should hold
                largeCount--;
            }
            balance();
        }

        private void balance() {
            prune(small);
            prune(large);

            while (smallCount < k && !large.isEmpty()) {
                prune(large);
                if (large.isEmpty()) break;
                
                int val = large.poll();
                inLarge.put(val, inLarge.get(val) - 1);
                
                small.offer(val);
                inSmall.put(val, inSmall.getOrDefault(val, 0) + 1);
                smallCount++;
                largeCount--;
                prune(small); 
            }
            
            while (smallCount > k) {
                prune(small);
                 if (small.isEmpty()) break;
                 
                int val = small.poll();
                inSmall.put(val, inSmall.get(val) - 1);
                
                large.offer(val);
                inLarge.put(val, inLarge.getOrDefault(val, 0) + 1);
                smallCount--;
                largeCount++;
                prune(large);
            }
        }

        public Integer getKthSmallest() {
            prune(small);
            if (small.isEmpty()) return null;
            return small.peek();
        }
    }

    public List<Integer> kthSmallestInWindows(int[] arr, int w, int k) {
        int n = arr.length;
        if (w > n) return Collections.emptyList();

        DualHeap dh = new DualHeap(k);
        List<Integer> result = new ArrayList<>();

        for (int i = 0; i < w; i++) {
            dh.add(arr[i]);
        }
        result.add(dh.getKthSmallest());

        for (int i = w; i < n; i++) {
            dh.remove(arr[i - w]);
            dh.add(arr[i]);
            result.add(dh.getKthSmallest());
        }

        return result;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int w = sc.nextInt();
            int k = sc.nextInt();
            int[] arr = new int[n];
            for (int i = 0; i < n; i++) {
                arr[i] = sc.nextInt();
            }

            Solution solution = new Solution();
            List<Integer> result = solution.kthSmallestInWindows(arr, w, k);
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < result.size(); i++) {
                if (i > 0) sb.append(" ");
                sb.append(result.get(i));
            }
            System.out.println(sb.toString());
        }
        sc.close();
    }
}
```

### Python
```python
import sys
import heapq
from collections import Counter, defaultdict

class DualHeap:
    def __init__(self, k):
        self.k = k
        self.small = []  # Max-heap (simulated with negative values) storing k smallest
        self.large = []  # Min-heap storing the rest
        self.small_count = 0  # Logical count
        self.large_count = 0  # Logical count
        self.lazy = Counter()
        # Track which heap each value was placed in (counts per heap)
        self.in_small = defaultdict(int)
        self.in_large = defaultdict(int)
    
    def _prune(self, heap, is_small):
        # Remove invalid elements from top of heap
        while heap:
            val = -heap[0] if is_small else heap[0]
            if self.lazy[val] > 0:
                self.lazy[val] -= 1
                heapq.heappop(heap)
            else:
                break
    
    def add(self, x):
        # Add to small heap initially
        if self.small_count < self.k:
            heapq.heappush(self.small, -x)
            self.small_count += 1
            self.in_small[x] += 1
        else:
            # Check if x belongs in small or large
            self._prune(self.small, True)
            if not self.small:  # Small heap is empty after pruning
                heapq.heappush(self.small, -x)
                self.small_count += 1
                self.in_small[x] += 1
            else:
                small_max = -self.small[0]
                if x <= small_max:
                    heapq.heappop(self.small)
                    self.in_small[small_max] -= 1
                    heapq.heappush(self.small, -x)
                    self.in_small[x] += 1
                    heapq.heappush(self.large, small_max)
                    self.in_large[small_max] += 1
                    self.large_count += 1
                else:
                    heapq.heappush(self.large, x)
                    self.in_large[x] += 1
                    self.large_count += 1
        self._balance()

    def remove(self, x):
        # Use tracking to determine which heap the element is in
        self.lazy[x] += 1
        
        if self.in_small[x] > 0:
            self.in_small[x] -= 1
            self.small_count -= 1
        else:
            self.in_large[x] -= 1
            self.large_count -= 1
            
        self._balance()

    def _balance(self):
        # Ensure small has exactly k elements if possible
        self._prune(self.small, True)
        self._prune(self.large, False)
        
        while self.small_count < self.k and self.large:
            self._prune(self.large, False)
            if not self.large: break
            val = heapq.heappop(self.large)
            self.in_large[val] -= 1
            heapq.heappush(self.small, -val)
            self.in_small[val] += 1
            self.small_count += 1
            self.large_count -= 1
            self._prune(self.small, True) # Just in case

        while self.small_count > self.k: # Should rarely happen with add logic but good for safety
            self._prune(self.small, True)
            val = -heapq.heappop(self.small)
            self.in_small[val] -= 1
            heapq.heappush(self.large, val)
            self.in_large[val] += 1
            self.small_count -= 1
            self.large_count += 1
            self._prune(self.large, False)

    def get_kth_smallest(self):
        self._prune(self.small, True)
        if self.small:
            return -self.small[0]
        return None

class Solution:
    def kth_smallest_in_windows(self, arr: list, w: int, k: int) -> list:
        n = len(arr)
        if w > n: return []
        
        dh = DualHeap(k)
        result = []
        
        for i in range(w):
            dh.add(arr[i])
            
        result.append(dh.get_kth_smallest())
        
        for i in range(w, n):
            dh.remove(arr[i - w])
            dh.add(arr[i])
            result.append(dh.get_kth_smallest())
            
        return result

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    try:
        n = int(next(it))
        w = int(next(it))
        k = int(next(it))
        arr = []
        for _ in range(n):
            arr.append(int(next(it)))
            
        solution = Solution()
        result = solution.kth_smallest_in_windows(arr, w, k)
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
#include <set>

using namespace std;

class Solution {
public:
    vector<int> kthSmallestInWindows(const vector<int>& arr, int w, int k) {
        // In C++, we can use multiset which supports deletion!
        // This simplifies things immensely compared to Java/Python heaps.
        // O(N log W)
        
        multiset<int> window;
        vector<int> result;
        
        // Optimization: Maintain an iterator to the k-th element?
        // Yes, "Moving Iterator" technique.
        // O(N) if we just move iterator, but insertion is O(log W).
        
        auto mid = window.begin(); // Points to k-th element (0-indexed k-1)
        
        for (int i = 0; i < arr.size(); i++) {
            window.insert(arr[i]);
            
            if (i < w) {
                // Initial build
                if (window.size() == k) {
                    mid = prev(window.end());
                } else if (window.size() > k) {
                    if (arr[i] < *mid) mid--;
                }
            } else {
                // Slide
                int out = arr[i - w];
                int in = arr[i];
                
                // Insert logic relative to mid
                if (in < *mid) mid--;
                
                // Remove logic
                // Be careful: mid can be invalidated if we erase it
                auto it = window.lower_bound(out); // Find ONE instance
                // If duplicates, any instance works, but we must be careful if it is mid
                
                if (it == mid) {
                    // We are removing the element mid points to.
                    // We need to shift mid.
                    // If we remove mid, the next element becomes the new k-th?
                    // So mid should move to next.
                    auto next_it = next(mid);
                    window.erase(it);
                    mid = next_it;
                } else {
                    if (*it < *mid) {
                        // Removed from left of mid, mid shifts right (to larger)
                        window.erase(it);
                        mid++;
                    } else {
                        // Removed from right of mid, mid stays (relative index same)
                        window.erase(it);
                    }
                }
            }
            
            if (i >= w - 1) {
                // Adjust mid to be exactly k-th
                // Due to insert/remove, mid can be off by 1
                // Rely on `advance` for safety in the medium solution.
                // No, O(K) is too slow.
                // Use two multisets L and R to match other languages.
                // L size = k. R size = w-k.
            }
        }
        
        // Re-implementation with Two Multisets for clarity and robustness
        multiset<int> L, R;
        result.clear();
        
        for (int i = 0; i < arr.size(); i++) {
            int val = arr[i];
            
            // ADD
            if (L.empty() || val <= *L.rbegin()) {
                L.insert(val);
            } else {
                R.insert(val);
            }
            
            // REMOVE
            if (i >= w) {
                int out = arr[i - w];
                auto itL = L.find(out);
                if (itL != L.end()) {
                    L.erase(itL);
                } else {
                    auto itR = R.find(out);
                    if (itR != R.end()) R.erase(itR);
                }
            }
            
            // BALANCE
            while (L.size() < k && !R.empty()) {
                L.insert(*R.begin());
                R.erase(R.begin());
            }
            while (L.size() > k) {
                R.insert(*L.rbegin());
                L.erase(prev(L.end()));
            }
            
            if (i >= w - 1) {
                result.push_back(*L.rbegin());
            }
        }
        
        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, w, k;
    if (cin >> n >> w >> k) {
        vector<int> arr(n);
        for (int i = 0; i < n; i++) cin >> arr[i];
        
        Solution solution;
        vector<int> result = solution.kthSmallestInWindows(arr, w, k);
        for (size_t i = 0; i < result.size(); i++) {
            if (i > 0) cout << " ";
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

class DualHeap {
  constructor(k) {
    this.k = k;
    this.small = new PriorityQueue((a, b) => b - a); // Max heap
    this.large = new PriorityQueue((a, b) => a - b); // Min heap
    this.smallCount = 0;
    this.largeCount = 0;
    this.lazy = new Map();
    this.inSmall = new Map();
    this.inLarge = new Map();
  }

  prune(heap) {
    while (!heap.isEmpty()) {
      const val = heap.peek();
      if ((this.lazy.get(val) || 0) > 0) {
        this.lazy.set(val, this.lazy.get(val) - 1);
        heap.pop();
      } else {
        break;
      }
    }
  }

  add(x) {
    if (this.smallCount < this.k) {
      this.small.push(x);
      this.smallCount++;
      this.inSmall.set(x, (this.inSmall.get(x) || 0) + 1);
    } else {
      this.prune(this.small);
      if (this.small.isEmpty()) {
        this.small.push(x);
        this.smallCount++;
        this.inSmall.set(x, (this.inSmall.get(x) || 0) + 1);
      } else {
        const smallMax = this.small.peek();
        if (x <= smallMax) {
          this.small.pop();
          this.inSmall.set(smallMax, this.inSmall.get(smallMax) - 1);
          
          this.small.push(x);
          this.inSmall.set(x, (this.inSmall.get(x) || 0) + 1);
          
          this.large.push(smallMax);
          this.inLarge.set(smallMax, (this.inLarge.get(smallMax) || 0) + 1);
          this.largeCount++;
        } else {
          this.large.push(x);
          this.inLarge.set(x, (this.inLarge.get(x) || 0) + 1);
          this.largeCount++;
        }
      }
    }
    this.balance();
  }

  remove(x) {
    this.lazy.set(x, (this.lazy.get(x) || 0) + 1);
    if ((this.inSmall.get(x) || 0) > 0) {
      this.inSmall.set(x, this.inSmall.get(x) - 1);
      this.smallCount--;
    } else {
      this.inLarge.set(x, (this.inLarge.get(x) || 0) - 1);
      this.largeCount--;
    }
    this.balance();
  }

  balance() {
    this.prune(this.small);
    this.prune(this.large);
    
    while (this.smallCount < this.k && !this.large.isEmpty()) {
      this.prune(this.large);
      if (this.large.isEmpty()) break;
      
      const val = this.large.pop();
      this.inLarge.set(val, this.inLarge.get(val) - 1);
      
      this.small.push(val);
      this.inSmall.set(val, (this.inSmall.get(val) || 0) + 1);
      this.smallCount++;
      this.largeCount--;
      this.prune(this.small);
    }
    
    while (this.smallCount > this.k) {
      this.prune(this.small);
      if (this.small.isEmpty()) break;
      
      const val = this.small.pop();
      this.inSmall.set(val, this.inSmall.get(val) - 1);
      
      this.large.push(val);
      this.inLarge.set(val, (this.inLarge.get(val) || 0) + 1);
      this.smallCount--;
      this.largeCount++;
      this.prune(this.large);
    }
  }

  getKthSmallest() {
    this.prune(this.small);
    if (this.small.isEmpty()) return null;
    return this.small.peek();
  }
}

class Solution {
  kthSmallestInWindows(arr, w, k) {
    const n = arr.length;
    if (w > n) return [];
    
    const dh = new DualHeap(k);
    const result = [];
    
    for (let i = 0; i < w; i++) {
        dh.add(arr[i]);
    }
    const val = dh.getKthSmallest();
    if(val !== null) result.push(val);
    
    for (let i = w; i < n; i++) {
        dh.remove(arr[i - w]);
        dh.add(arr[i]);
        const v = dh.getKthSmallest();
        if(v !== null) result.push(v);
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
  const n = parseInt(data[idx++]);
  const w = parseInt(data[idx++]);
  const k = parseInt(data[idx++]);
  const arr = [];
  for (let i = 0; i < n; i++) {
    arr.push(parseInt(data[idx++]));
  }
  
  const solution = new Solution();
  const result = solution.kthSmallestInWindows(arr, w, k);
  console.log(result.join(" "));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:** `arr=[1, 3, 2, 6, 4]`, `w=3`, `k=2`.

1. `i=0, val=1`: L=[1], R=[]. Sizes: 1, 0. (Need k=2).
2. `i=1, val=3`: L=[1], R=[3]. Rebalance: Move 3 to L? No, L.max < R.min.
   - L=[3, 1], R=[]. Sizes: 2, 0.
3. `i=2, val=2`: L=[3, 1]. `2 < 3`. Insert to L. L=[3, 2, 1]. Sizes: 3, 0.
   - `leftSize > k` (3 > 2). Move L top (3) to R.
   - L=[2, 1], R=[3]. Sizes: 2, 1.
   - Output: L.peek() = 2.
4. `i=3, val=6`: Remove `arr[0]=1`.
   - `1 <= 2`. Decrement `leftSize` -> 1. Mark 1 deleted.
   - Add 6. `6 > 2`. Insert R. R=[3, 6]. Sizes: 1, 2.
   - Rebalance: `leftSize < k` (1 < 2). Move R top (3) to L.
   - L=[3, 2, (1 del)], R=[6]. Sizes: 2, 1.
   - Output: L.peek() = 3.
5. `i=4, val=4`: Remove `arr[1]=3`.
   - `3 <= 3`. Decrement `leftSize` -> 1. Mark 3 deleted.
   - Add 4. `4 > 3` (old peek). Insert R. R=[6, 4]. Sizes: 1, 2.
   - Rebalance: `leftSize < k`. Move R top (4) to L.
   - L=[4, 2, (1 del), (3 del)], R=[6]. Sizes: 2, 1.
   - Output: L.peek() = 4.

Result: `2, 3, 4`. Correct.

## ✅ Proof of Correctness

### Invariant
- `L` contains `k` valid elements. `R` contains `w-k` valid elements.
- `max(L) <= min(R)`.
- `L.peek()` is the k-th smallest element.
- Lazy deletion ensures amortized efficiency.

## 💡 Interview Extensions

- **Extension 1:** Stream of numbers?
  - *Answer:* Same logic, just no removal (or infinite window).
- **Extension 2:** Fractional K (e.g., median)?
  - *Answer:* Same logic, set `k = w/2`.

### Common Mistakes to Avoid

1. **Size Tracking**
   - ❌ Wrong: Using `heap.size()` which includes deleted elements.
   - ✅ Correct: Maintain explicit `validSize` counters.
2. **Lazy Deletion**
   - ❌ Wrong: Forgetting to clean heaps before peeking/popping.
   - ✅ Correct: Always `clean()` before accessing top.

## Related Concepts

- **Median of Medians:** Selection algorithm.
- **Two Heaps Pattern:** Standard for median maintenance.
